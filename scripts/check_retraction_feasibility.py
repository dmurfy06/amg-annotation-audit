"""
check_retraction_feasibility.py — does the data exist in the shape the question needs?

THE QUESTION (candidate R1, Phase 2b):
    Curated biochemical databases advertise themselves as holding *experimentally validated*
    knowledge. Each entry cites the primary literature that validates it. Some of that
    literature has since been retracted.

    Do these databases still carry entries whose supporting evidence has been retracted?

THIS SCRIPT DOES NOT ANSWER THAT. It only checks whether the question is askable:
  1. Do the target resources expose per-entry literature identifiers?  (PMIDs)
  2. Can the set of retracted publications be obtained from a citable source?
  3. Is the intersection non-empty — and small enough to adjudicate by hand?

Design notes:
  * Retraction status comes from **PubMed's own publication type** `Retracted Publication[pt]`,
    not from a scraped list. PubMed is citable, free, and needs no personal data in a URL.
    (The Retraction Watch database is larger and richer, but its Crossref endpoint requires
    an email address embedded in the query string — Daniel can pull that himself later if the
    intersection justifies it.)
  * Everything is cached to data/ so this is run once, not per-experiment.
  * A zero-length successful HTTP response is NOT an error. Learned the hard way on RCSB.

Usage:
    python scripts/check_retraction_feasibility.py
"""

import io
import json
import re
import tarfile
import time
import urllib.parse
import urllib.request
import zipfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)

UA = {"User-Agent": "research-project/0.1 (undergraduate research project)"}
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"


def get(url: str, timeout: int = 180) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def cached(name: str, url: str) -> bytes:
    p = DATA / name
    if p.exists():
        print(f"  using cached {p.name} ({p.stat().st_size:,} bytes)")
        return p.read_bytes()
    print(f"  downloading {url}")
    b = get(url)
    p.write_bytes(b)
    print(f"  cached -> {p.name} ({len(b):,} bytes)")
    return b


# --------------------------------------------------------------------------- resources

def mibig_pmids() -> dict[str, set[str]]:
    """MIBiG: biosynthetic gene clusters. Sells itself on *experimental validation*."""
    print("\n[MIBiG 4.0]")
    raw = cached("mibig_json_4.0.tar.gz",
                 "https://dl.secondarymetabolites.org/mibig/mibig_json_4.0.tar.gz")
    tf = tarfile.open(fileobj=io.BytesIO(raw))
    out: dict[str, set[str]] = {}
    for n in tf.getnames():
        if not n.endswith(".json"):
            continue
        try:
            rec = json.loads(tf.extractfile(n).read().decode("utf-8"))
        except Exception:
            continue
        acc = rec.get("accession") or Path(n).stem
        pmids = set()
        # references appear as "pubmed:12345678" strings, scattered through the record
        for m in re.finditer(r"pubmed:(\d+)", json.dumps(rec)):
            pmids.add(m.group(1))
        if pmids:
            out[acc] = pmids
    print(f"  entries with >=1 PMID : {len(out):,}")
    print(f"  unique PMIDs          : {len(set().union(*out.values())):,}")
    return out


def drugage_pmids() -> dict[str, set[str]]:
    """DrugAge: compounds reported to extend lifespan. Every row cites its source study."""
    print("\n[DrugAge]")
    raw = cached("drugage.zip", "https://genomics.senescence.info/drugs/dataset.zip")
    zf = zipfile.ZipFile(io.BytesIO(raw))
    name = [n for n in zf.namelist() if n.endswith(".csv")][0]
    text = zf.read(name).decode("utf-8", "replace")
    header = text.splitlines()[0].split(",")
    print(f"  file: {name}")
    print(f"  columns: {header}")
    # find the PubMed column by name
    idx = next((i for i, h in enumerate(header) if "pubmed" in h.lower()), None)
    if idx is None:
        print("  !! no pubmed column found — cannot use this resource")
        return {}
    import csv as _csv
    out: dict[str, set[str]] = {}
    for row in _csv.reader(io.StringIO(text)):
        if not row or row is None or len(row) <= idx or row[0] == header[0]:
            continue
        pm = re.sub(r"\D", "", row[idx] or "")
        if pm:
            out.setdefault(f"{row[0]}|{row[1] if len(row) > 1 else ''}", set()).add(pm)
    print(f"  rows with a PMID      : {len(out):,}")
    if out:
        print(f"  unique PMIDs          : {len(set().union(*out.values())):,}")
    return out


def mcsa_pmids() -> dict[str, set[str]]:
    """M-CSA: catalytic mechanisms, hand-curated from primary literature by the Thornton group."""
    print("\n[M-CSA]")
    p = DATA / "mcsa_entries.json"
    if p.exists():
        print(f"  using cached {p.name} ({p.stat().st_size:,} bytes)")
        results = json.loads(p.read_text(encoding="utf-8"))
    else:
        results = []
        url = "https://www.ebi.ac.uk/thornton-srv/m-csa/api/entries/?format=json&page_size=200"
        while url:
            page = json.loads(get(url).decode("utf-8"))
            results.extend(page.get("results", []))
            url = page.get("next")
            print(f"    fetched {len(results)} ...")
            time.sleep(0.4)
        p.write_text(json.dumps(results), encoding="utf-8")
        print(f"  cached -> {p.name}")
    out: dict[str, set[str]] = {}
    for rec in results:
        blob = json.dumps(rec)
        pmids = set(re.findall(r'"pubmed_id"\s*:\s*"?(\d{4,9})"?', blob))
        pmids |= set(re.findall(r"pubmed[/:](\d{4,9})", blob))
        if pmids:
            out[str(rec.get("mcsa_id"))] = pmids
    print(f"  entries with >=1 PMID : {len(out):,}")
    if out:
        print(f"  unique PMIDs          : {len(set().union(*out.values())):,}")
    return out


# --------------------------------------------------------------------------- retractions

def _esearch_ids(term: str, retmax: int = 9000) -> tuple[int, list[str]]:
    """One esearch call. Returns (total_count, ids). NCBI caps retstart+retmax at 10,000,
    so callers must partition the query rather than paginate past that."""
    q = urllib.parse.quote(term)
    raw = get(f"{EUTILS}/esearch.fcgi?db=pubmed&term={q}&retmode=json&retmax={retmax}")
    try:
        js = json.loads(raw.decode("utf-8", "replace"))
    except json.JSONDecodeError:
        # NCBI returns an HTML error page under load; treat as a soft failure, not a crash
        print(f"    !! non-JSON response for {term!r} ({len(raw)} bytes) — retrying once")
        time.sleep(3)
        js = json.loads(get(f"{EUTILS}/esearch.fcgi?db=pubmed&term={q}"
                            f"&retmode=json&retmax={retmax}").decode("utf-8", "replace"))
    res = js["esearchresult"]
    return int(res["count"]), res.get("idlist", [])


def retracted_pmids() -> set[str]:
    """Every PubMed record typed 'Retracted Publication'. This is PubMed's own flag.

    Partitioned by publication year because esearch will not return records beyond
    position 10,000 in a single result set."""
    print("\n[PubMed: Retracted Publication[pt]]")
    p = DATA / "pubmed_retracted_pmids.json"
    if p.exists():
        print(f"  using cached {p.name}")
        return set(json.loads(p.read_text(encoding="utf-8")))

    base = '"Retracted Publication"[Publication Type]'
    total, _ = _esearch_ids(base, retmax=0)
    print(f"  total retracted publications in PubMed: {total:,}")

    pmids: set[str] = set()
    for year in range(1950, 2027):
        n, ids = _esearch_ids(f"{base} AND {year}[dp]")
        if n > 9000:
            print(f"    !! {year} has {n:,} — exceeds one page, would need finer splitting")
        pmids |= set(ids)
        if n:
            print(f"    {year}: {n:>5,}   (running total {len(pmids):,})")
        time.sleep(0.35)

    print(f"  collected {len(pmids):,} of {total:,} "
          f"({len(pmids)/total:.1%} — remainder have no indexed publication year)")
    p.write_text(json.dumps(sorted(pmids)), encoding="utf-8")
    return pmids


# --------------------------------------------------------------------------- main

def main() -> None:
    resources = {
        "MIBiG (biosynthetic gene clusters)": mibig_pmids(),
        "DrugAge (lifespan-extending compounds)": drugage_pmids(),
        "M-CSA (catalytic mechanisms)": mcsa_pmids(),
    }
    retracted = retracted_pmids()
    print(f"  retracted PMIDs held: {len(retracted):,}")

    print("\n" + "=" * 72)
    print("INTERSECTION — entries whose cited evidence includes a retracted paper")
    print("=" * 72)
    for label, entries in resources.items():
        if not entries:
            print(f"\n{label}: no usable references — SKIPPED")
            continue
        all_pmids = set().union(*entries.values())
        hit_pmids = all_pmids & retracted
        hit_entries = {k: sorted(v & retracted) for k, v in entries.items() if v & retracted}
        print(f"\n{label}")
        print(f"   entries            : {len(entries):,}")
        print(f"   unique PMIDs cited : {len(all_pmids):,}")
        print(f"   RETRACTED PMIDs    : {len(hit_pmids)}")
        print(f"   AFFECTED ENTRIES   : {len(hit_entries)}")
        for k, v in sorted(hit_entries.items())[:25]:
            print(f"        {k:<28} {', '.join(v)}")

    print("\nNote: a hit means the entry *cites* a retracted paper. Whether the annotation")
    print("actually depends on it is a separate question, and is the real work.")


if __name__ == "__main__":
    main()
