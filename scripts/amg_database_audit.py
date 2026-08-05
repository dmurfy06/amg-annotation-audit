"""
amg_database_audit.py — feasibility probe for candidate R4.

THE QUESTION:
    Martin et al. (2025, Nature Microbiology) argue that the rush to catalogue viral auxiliary
    metabolic genes (AMGs) has produced "an epidemic of misannotation", and name specific gene
    families they believe are wrongly counted as AMGs: dcm, queC/D/E/F, dsrC/tusE, glycoside
    hydrolases, folate biosynthesis genes.

    They do not measure how much of the record those categories account for. Neither did the
    2021 PeerJ viromics-standards paper, which raised the same concern four years earlier and
    explicitly declined to catalogue which genes are affected.

    So: how much of the AMG record is built on categories the field's own experts doubt?

THIS SCRIPT only establishes that the question is askable. It checks whether the AMG
definitions used by the two standard tools are obtainable and machine-readable, and whether
Martin et al.'s named suspects are actually present in them.

Data sources, all citable and all tiny:
  * VIBRANT  files/VIBRANT_AMGs.tsv        (Kieft, Zhou & Anantharaman 2020)  ~22 KB
  * DRAM     data/amg_database.tsv         (Shaffer et al. 2020)              ~22 KB
  * KEGG     rest.kegg.jp/list/ko          — to turn KO accessions into names

NOTE ON A TRAP AVOIDED: VIBRANT keys its AMG database on **KEGG KO** accessions; DRAM keys
its on **PFAM**. 242 of DRAM's 279 rows carry no KO at all. Comparing "number of AMG entries"
between the two tools therefore compares two different namespaces and is meaningless. An
earlier version of this analysis produced an impressive-looking 83-fold difference that was
purely an artefact of that mismatch.

Usage:
    python scripts/amg_database_audit.py
"""

import re
import urllib.request
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)
UA = {"User-Agent": "research-project/0.1 (undergraduate research project)"}

SOURCES = {
    "VIBRANT_AMGs.tsv":
        "https://raw.githubusercontent.com/AnantharamanLab/VIBRANT/master/files/VIBRANT_AMGs.tsv",
    "DRAM_amg_database.tsv":
        "https://raw.githubusercontent.com/WrightonLabCSU/DRAM/master/data/amg_database.tsv",
    "kegg_ko_list.tsv":
        "https://rest.kegg.jp/list/ko",
}

# The gene families Martin et al. 2025 name as probably-not-AMGs. Patterns match KEGG
# descriptions. Kept explicit and separate from the data so the rubric is auditable —
# this is the pre-registered suspect list, not something discovered after looking.
SUSPECTS = {
    "dcm — DNA cytosine methyltransferase": r"\bdcm\b",
    "queC/D/E/F — queuosine biosynthesis": r"\bque[CDEF]\b",
    "dsrC / tusE — sulfur relay": r"\bdsrC\b|\btusE\b",
    "folate / one-carbon": r"folate|dihydrofolate",
    "glycoside hydrolases": r"glycoside hydrolase|glucosidase|galactosidase|chitinase|lysozyme",
    "glycosyltransferases": r"glycosyltransferase",
}


def cached(name: str) -> str:
    p = DATA / name
    if p.exists():
        print(f"  cached  {name} ({p.stat().st_size:,} bytes)")
        return p.read_text(encoding="utf-8")
    req = urllib.request.Request(SOURCES[name], headers=UA)
    with urllib.request.urlopen(req, timeout=180) as r:
        txt = r.read().decode("utf-8", "replace")
    p.write_text(txt, encoding="utf-8")
    print(f"  fetched {name} ({len(txt):,} bytes)")
    return txt


def main() -> None:
    print("[sources]")
    vib_txt = cached("VIBRANT_AMGs.tsv")
    dram_txt = cached("DRAM_amg_database.tsv")
    kegg_txt = cached("kegg_ko_list.tsv")

    ko_name = {}
    for line in kegg_txt.splitlines():
        parts = line.split("\t")
        if len(parts) >= 2:
            ko_name[parts[0].replace("ko:", "")] = parts[1].strip()

    vibrant = {l.strip() for l in vib_txt.strip().splitlines()[1:] if l.strip()}

    dram_lines = dram_txt.strip().splitlines()
    cols = dram_lines[0].split("\t")
    dram_rows = [dict(zip(cols, l.split("\t"))) for l in dram_lines[1:]]

    # NB: compute these OUTSIDE the f-strings. A regex quantifier like {5} inside an f-string
    # is parsed as a replacement field, which silently produced a count of 0 here.
    KO_RE = re.compile(r"K\d{5}")
    n_ko = sum(1 for r in dram_rows if KO_RE.fullmatch(r["KO"].strip()))
    n_pfam = sum(1 for r in dram_rows if r.get("PFAM", "").strip())

    print(f"\nKEGG orthology entries      : {len(ko_name):,}")
    print(f"VIBRANT AMG database (KO)   : {len(vibrant):,} accessions")
    print(f"DRAM AMG database           : {len(dram_rows):,} rows")
    print(f"   with a KEGG KO           : {n_ko:,}")
    print(f"   with a PFAM              : {n_pfam:,}")
    print("   -> the two tools use DIFFERENT NAMESPACES; entry counts are not comparable")

    # DRAM ships its own provenance columns. This is the interesting part.
    print("\n[DRAM self-reported provenance]")
    ver = Counter(r.get("verified", "").strip() for r in dram_rows)
    print(f"   verified=TRUE  : {ver.get('TRUE', 0):>4}")
    print(f"   verified=FALSE : {ver.get('FALSE', 0):>4}"
          f"   ({ver.get('FALSE', 0) / len(dram_rows):.0%} of the database)")
    print("   most-cited supporting references:")
    for ref, n in Counter(r.get("reference", "").strip() for r in dram_rows).most_common(5):
        print(f"        {n:>4}  {ref[:64]}")

    # Are Martin et al.'s named suspects actually in there?
    print("\n[Martin et al. 2025 named suspects — present in VIBRANT's AMG database?]")
    total = 0
    for label, pat in SUSPECTS.items():
        hits = [k for k in sorted(vibrant) if re.search(pat, ko_name.get(k, ""), re.I)]
        total += len(hits)
        print(f"   {label:<40} {len(hits):>3} KOs")
        for k in hits[:4]:
            print(f"        {k}  {ko_name.get(k, '?')[:88]}")
    print(f"\n   TOTAL KOs matching a named suspect category: {total}"
          f"  ({total / len(vibrant):.1%} of VIBRANT's AMG database)")

    print("\nWhat this does and does not show:")
    print("  DOES: every gene family named in the Nature Microbiology perspective is present")
    print("        in the AMG database of a standard tool, and can be enumerated.")
    print("  DOES NOT: establish that any individual call is wrong. Deciding whether a gene is")
    print("        auxiliary or essential to viral replication is biochemistry, not string")
    print("        matching, and that adjudication is the actual project.")


if __name__ == "__main__":
    main()
