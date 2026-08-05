"""
orphan_enzyme_census.py — how many EC entries still have no associated sequence?

An "orphan enzyme" is an activity characterised experimentally but with no gene/protein
sequence assigned, so it is invisible to sequence-similarity annotation.

Published censuses (all pre-2015):
  2006 : 1,444 of 3,927 retained EC numbers had no sequence  = 36.8%
  ~2014: orphan fraction reported to have fallen 38% -> 22%; >1,000 orphans remain
No census found after ~2014.

The ENZYME nomenclature database publishes every EC entry with `DR` lines listing
UniProtKB cross-references. An entry with no DR line has no associated sequence.
That makes the census directly countable.

This is a DATA CHECK for candidate A2, not the study itself — it establishes whether the
question is answerable before any commitment is made.

Usage:
    python scripts/orphan_enzyme_census.py
"""

import gzip
import io
import urllib.request
from collections import Counter
from pathlib import Path

ENZYME_DAT = "https://ftp.expasy.org/databases/enzyme/enzyme.dat"
OUT = Path(__file__).resolve().parent.parent / "data" / "enzyme_dat_census.tsv"


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "research-project/0.1"})
    with urllib.request.urlopen(req, timeout=180) as r:
        raw = r.read()
    if raw[:2] == b"\x1f\x8b":  # gzip magic number
        raw = gzip.decompress(raw)
    return raw.decode("utf-8", errors="replace")


def parse_enzyme_dat(text: str) -> list[dict]:
    """ENZYME flat file: entries separated by '//'. ID = EC number, DE = description,
    DR = UniProt cross-references, CC = comments (transferred/deleted entries)."""
    entries = []
    cur: dict = {}
    for line in text.splitlines():
        if line.startswith("//"):
            if cur.get("ec"):
                entries.append(cur)
            cur = {}
            continue
        if len(line) < 2:
            continue
        tag, _, rest = line.partition("   ")
        rest = rest.strip()
        if tag == "ID":
            cur = {"ec": rest, "de": "", "n_dr": 0, "cc": ""}
        elif tag == "DE":
            cur["de"] = cur.get("de", "") + rest
        elif tag == "DR":
            # each DR line holds several 'ACC, NAME;' pairs
            cur["n_dr"] = cur.get("n_dr", 0) + rest.count(";")
        elif tag == "CC":
            cur["cc"] = cur.get("cc", "") + rest
    return entries


def main() -> None:
    print(f"downloading {ENZYME_DAT} ...")
    text = fetch(ENZYME_DAT)
    print(f"  {len(text):,} characters")

    entries = parse_enzyme_dat(text)
    print(f"  parsed {len(entries):,} EC entries\n")

    # Transferred and deleted entries are not real activities and must be excluded —
    # the historical censuses counted "retained" EC numbers only.
    def is_retired(e: dict) -> bool:
        d = (e["de"] + " " + e["cc"]).lower()
        return "transferred entry" in d or "deleted entry" in d

    retained = [e for e in entries if not is_retired(e)]
    retired = len(entries) - len(retained)

    orphans = [e for e in retained if e["n_dr"] == 0]

    print("=== ORPHAN ENZYME CENSUS (today) ===")
    print(f"Total EC entries in file        : {len(entries):,}")
    print(f"Transferred / deleted (excluded): {retired:,}")
    print(f"Retained EC entries             : {len(retained):,}")
    print(f"...with NO UniProt cross-ref    : {len(orphans):,}")
    print(f"ORPHAN FRACTION                 : {len(orphans) / len(retained):.1%}")
    print()
    print("For comparison (published):")
    print("  2006 : 1,444 / 3,927 = 36.8%")
    print("  ~2014: reported ~22%, >1,000 orphans")
    print()

    top = Counter(e["ec"].split(".")[0] for e in orphans)
    allc = Counter(e["ec"].split(".")[0] for e in retained)
    names = {
        "1": "Oxidoreductases", "2": "Transferases", "3": "Hydrolases",
        "4": "Lyases", "5": "Isomerases", "6": "Ligases", "7": "Translocases",
    }
    print("--- orphan rate by EC top-level class ---")
    print(f"{'class':<6} {'orphans':>8} {'total':>8} {'rate':>7}  name")
    for k in sorted(allc):
        rate = top.get(k, 0) / allc[k]
        print(f"{k:<6} {top.get(k,0):>8} {allc[k]:>8} {rate:>6.1%}  {names.get(k,'?')}")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8") as fh:
        fh.write("ec\tn_uniprot_xrefs\tdescription\n")
        for e in retained:
            fh.write(f"{e['ec']}\t{e['n_dr']}\t{e['de']}\n")
    print(f"\nwrote {OUT}")


if __name__ == "__main__":
    main()
