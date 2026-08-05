"""
amg_record_composition.py — the decisive data check for candidate R4.

QUESTION:
    `amg_database_audit.py` showed that every gene family Martin et al. (2025, Nature
    Microbiology) name as probably-not-an-AMG is present in VIBRANT's AMG database, and that
    those 53 KOs are 1.9% of that database.

    But **database composition is not record composition.** One abundant glycoside hydrolase
    may be called thousands of times while hundreds of obscure KOs are never hit. What matters
    is how often the suspect categories are actually CALLED in a real catalogue.

DATA:
    Table S4/S5 of "Virus-encoded auxiliary metabolic genes throughout the global oceans"
    (Microbiome 2024, doi:10.1186/s40168-024-01876-z), Zenodo 10.5281/zenodo.12668289.
    Raw DRAM-v output, one row per AMG call:
        Table_S5_Conservative_AMGs :  88,731 calls  (their curated catalogue)
        Table_S4_Permissive_AMGs   : 255,860 calls  (before curation)

    Having both lets us ask whether curation removes the suspect categories or not.

METHOD NOTE — the rubric is fixed in advance:
    SUSPECTS below is copied unchanged from amg_database_audit.py, which was written before
    this table was downloaded. Patterns are NOT tuned to these results. Two independent
    matching routes are reported separately because they have different reliability:
        (a) KEGG KO accession  — exact, trustworthy
        (b) free-text description / CAZy hit — fuzzy, indicative only
    Do not merge them into one headline number.

Usage:
    .venv/Scripts/python.exe scripts/amg_record_composition.py
"""

import re
from collections import Counter
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent
XLSX = ROOT / "data" / "GlobalAMGs_SOM.xlsx"
KEGG = ROOT / "data" / "kegg_ko_list.tsv"

# Pre-registered. Identical to amg_database_audit.py. Not tuned to the results below.
SUSPECTS = {
    "dcm — DNA cytosine methyltransferase": r"\bdcm\b",
    "queC/D/E/F — queuosine biosynthesis": r"\bque[CDEF]\b",
    "dsrC / tusE — sulfur relay": r"\bdsrC\b|\btusE\b",
    "folate / one-carbon": r"folate|dihydrofolate",
    "glycoside hydrolases": r"glycoside hydrolase|glucosidase|galactosidase|chitinase|lysozyme",
    "glycosyltransferases": r"glycosyltransferase",
}
COMPILED = {k: re.compile(v, re.I) for k, v in SUSPECTS.items()}


def load_kegg() -> dict[str, str]:
    ko = {}
    for line in KEGG.read_text(encoding="utf-8").splitlines():
        p = line.split("\t")
        if len(p) >= 2:
            ko[p[0].replace("ko:", "")] = p[1].strip()
    return ko


def scan(ws, ko_name: dict[str, str], label: str) -> None:
    it = ws.iter_rows(values_only=True)
    hdr = list(next(it))
    ix = {name: hdr.index(name) for name in
          ("kegg_id", "kegg_hit", "gene_description", "cazy_hits",
           "auxiliary_score", "rank", "amg_flags") if name in hdr}

    total = 0
    with_ko = 0
    by_ko = Counter()        # exact route
    by_text = Counter()      # fuzzy route
    cazy_hits = 0
    aux_of_suspects = Counter()
    aux_all = Counter()

    for row in it:
        if row is None or all(v is None for v in row):
            continue
        total += 1

        def cell(name):
            i = ix.get(name)
            return "" if i is None or row[i] is None else str(row[i])

        aux = cell("auxiliary_score")
        aux_all[aux] += 1

        # (a) exact: KEGG KO accession -> KEGG's own description
        kid = cell("kegg_id").strip()
        m = re.search(r"K\d{5}", kid)
        matched_exact = False
        if m:
            with_ko += 1
            desc = ko_name.get(m.group(0), "")
            for lab, pat in COMPILED.items():
                if pat.search(desc):
                    by_ko[lab] += 1
                    matched_exact = True

        # (b) fuzzy: whatever free text DRAM-v attached
        text = " ".join((cell("gene_description"), cell("kegg_hit"), cell("cazy_hits")))
        for lab, pat in COMPILED.items():
            if pat.search(text):
                by_text[lab] += 1
        if cell("cazy_hits").strip():
            cazy_hits += 1
        if matched_exact:
            aux_of_suspects[aux] += 1

    print(f"\n{'=' * 74}\n{label}\n{'=' * 74}")
    print(f"  AMG calls                       : {total:,}")
    print(f"  with a KEGG KO accession        : {with_ko:,}  ({with_ko/total:.1%})")
    print(f"  with a CAZy hit                 : {cazy_hits:,}  ({cazy_hits/total:.1%})")

    print(f"\n  (a) EXACT — matched via KEGG KO accession:")
    tot_ko = sum(by_ko.values())
    for lab in SUSPECTS:
        n = by_ko[lab]
        print(f"      {lab:<40} {n:>8,}")
    print(f"      {'TOTAL':<40} {tot_ko:>8,}"
          f"   = {tot_ko/total:.2%} of all calls,"
          f" {tot_ko/with_ko:.2%} of KO-assigned calls" if with_ko else "")

    print(f"\n  (b) FUZZY — matched on free-text description / CAZy (indicative only):")
    tot_tx = sum(by_text.values())
    for lab in SUSPECTS:
        n = by_text[lab]
        print(f"      {lab:<40} {n:>8,}")
    print(f"      {'TOTAL (may double-count)':<40} {tot_tx:>8,}   = {tot_tx/total:.2%} of all calls")

    print(f"\n  DRAM-v auxiliary_score distribution (1 = highest confidence):")
    for k in sorted(aux_all, key=lambda x: (x is None, str(x))):
        n = aux_all[k]
        s = aux_of_suspects.get(k, 0)
        print(f"      score {str(k):<6} {n:>8,} calls    of which named-suspect: {s:>6,}")


def main() -> None:
    ko_name = load_kegg()
    print(f"KEGG orthology entries loaded: {len(ko_name):,}")
    wb = openpyxl.load_workbook(XLSX, read_only=True, data_only=True)
    scan(wb["Table_S5_Conservative_AMGs"], ko_name, "CONSERVATIVE catalogue (post-curation)")
    scan(wb["Table_S4_Permissive_AMGs"], ko_name, "PERMISSIVE catalogue (pre-curation)")
    print("\nReminder: a match means the call falls in a category Martin et al. argue should be")
    print("reconsidered. It does not prove any individual call is wrong. That is the project.")


if __name__ == "__main__":
    main()
