"""
check_n1_feasibility.py — is niche N1 (disulfide functional non-equivalence) viable?

N1 asks whether structurally equivalent disulfide bonds are functionally equivalent,
tested across proteins with MAVE measurement data.

That requires proteins that have BOTH:
  (a) MAVE data, and
  (b) annotated disulfide bonds that the MAVE actually covers.

Livesey & Marsh (bioRxiv 2025.07.31.667868) assembled the best-curated set of MAVE
datasets available — 37 human proteins, listed in their Table 1. That set is the
realistic ceiling for this question. This script extracts those accessions and asks
UniProt how many carry disulfide bonds.

Usage:
    python scripts/check_n1_feasibility.py
"""

import re
import time
from pathlib import Path

import urllib.request
import urllib.parse

REFS = Path(__file__).resolve().parent.parent / "refs" / "vep_mave_2025.txt"

# Standard UniProt accession pattern (UniProtKB accession format specification).
ACC_RE = re.compile(
    r"\b([OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9](?:[A-Z][A-Z0-9]{2}[0-9]){1,2})\b"
)


def accessions_from_table1(text: str) -> list[str]:
    """Table 1 lists targets as 'GENE / ACCESSION'. Take everything from its heading on."""
    idx = text.find("Table 1. Summary of 37 MAVE datasets")
    if idx == -1:
        raise SystemExit("Could not locate Table 1 heading in the extracted text.")
    table = text[idx:]
    seen: dict[str, None] = {}
    for m in ACC_RE.finditer(table):
        seen.setdefault(m.group(1), None)
    return list(seen)


def uniprot_disulfides(accs: list[str]) -> list[dict]:
    """Query UniProt REST for disulfide features, in batches."""
    fields = "accession,protein_name,length,ft_disulfid,cc_subcellular_location"
    rows: list[dict] = []
    header: list[str] = []

    for i in range(0, len(accs), 25):
        chunk = accs[i : i + 25]
        query = " OR ".join(f"accession:{a}" for a in chunk)
        url = (
            "https://rest.uniprot.org/uniprotkb/search?"
            + urllib.parse.urlencode(
                {"query": query, "fields": fields, "format": "tsv", "size": 500}
            )
        )
        with urllib.request.urlopen(url, timeout=90) as r:
            lines = r.read().decode("utf-8").splitlines()
        if not lines:
            continue
        if not header:
            header = lines[0].split("\t")
        for line in lines[1:]:
            rows.append(dict(zip(header, line.split("\t"))))
        time.sleep(0.4)
    return rows


def main() -> None:
    text = REFS.read_text(encoding="utf-8")
    accs = accessions_from_table1(text)
    print(f"UniProt accessions found in Table 1: {len(accs)}")

    rows = uniprot_disulfides(accs)
    print(f"UniProt records retrieved            : {len(rows)}\n")

    ds_key = next(k for k in rows[0] if "Disulfide" in k)
    loc_key = next((k for k in rows[0] if "Subcellular" in k), None)

    with_ds = []
    for r in rows:
        n = r.get(ds_key, "").count("DISULFID")
        if n:
            with_ds.append((n, r))

    print("=== N1 FEASIBILITY ===")
    print(f"Proteins in the curated MAVE set      : {len(rows)}")
    print(f"...with >=1 annotated disulfide bond  : {len(with_ds)}")
    print(f"...with >=3 (enough to compare within): {sum(1 for n, _ in with_ds if n >= 3)}")
    print(f"Total disulfide bonds available       : {sum(n for n, _ in with_ds)}\n")

    if with_ds:
        print("--- proteins carrying disulfides ---")
        for n, r in sorted(with_ds, key=lambda x: -x[0]):
            name = r.get("Protein names", "")[:52]
            loc = (r.get(loc_key, "") or "")[:44] if loc_key else ""
            print(f"  {r['Entry']:<8} bonds={n:<3} len={r['Length']:<6} {name}")
            if loc:
                print(f"           {loc}")


if __name__ == "__main__":
    main()
