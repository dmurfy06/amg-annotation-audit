"""
dramv_flag_semantics.py — CHUNK 1. What do DRAM-v's amg_flags letters mean, and does the
`F` flag actually behave the way the project has been assuming?

WHY THIS EXISTS
    68% of `dcm` calls in the ocean catalogue were observed to carry an `F` flag, and the
    project brief says: do not guess what that signifies. It has now been established from
    DRAM's source code and documentation (see refs/dram_docs/, and 07_flag_semantics.md):

        F = the gene starts within 5,000 bases of a contig end, or ends within 5,000 bases
            of the other end.  annotate_vgfs.py::get_metabolic_flags, length_from_end=5000

    F is therefore POSITIONAL, not biological. It is a statement about assembly, not about
    the gene. And DRAM-v keeps F-flagged genes by default (--remove_fs defaults to False).

THE CHECK THIS SCRIPT RUNS
    A raw "68% of dcm calls are F-flagged" number means nothing on its own. If 68% of ALL
    calls are F-flagged, dcm is unremarkable and there is nothing here. The question is
    whether the suspect categories are ENRICHED for F relative to the catalogue baseline.

    Rule 5 of this project: suspect your own best result. So this reports the baseline
    first, every proportion carries a Wilson 95% interval, and the comparison is explicit.

    It also reconstructs which DRAM-v filter the authors actually ran, from the flag and
    auxiliary-score distributions of their published table.

Usage:
    .venv/Scripts/python.exe scripts/dramv_flag_semantics.py
"""

import math
import re
from collections import Counter
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent
XLSX = ROOT / "data" / "GlobalAMGs_SOM.xlsx"
KEGG = ROOT / "data" / "kegg_ko_list.tsv"

# Pre-registered rubric. Copied unchanged from amg_record_composition.py.
SUSPECTS = {
    "dcm — DNA cytosine methyltransferase": r"\bdcm\b",
    "queC/D/E/F — queuosine biosynthesis": r"\bque[CDEF]\b",
    "dsrC / tusE — sulfur relay": r"\bdsrC\b|\btusE\b",
    "folate / one-carbon": r"folate|dihydrofolate",
    "glycoside hydrolases": r"glycoside hydrolase|glucosidase|galactosidase|chitinase|lysozyme",
    "glycosyltransferases": r"glycosyltransferase",
}
COMPILED = {k: re.compile(v, re.I) for k, v in SUSPECTS.items()}

# Established from DRAM source + wiki, not assumed. See 07_flag_semantics.md.
FLAG_MEANING = {
    "V": "viral      — VOGDB replication/structure category",
    "M": "metabolic  — in DRAM's distillate (genes DRAM calls metabolic)",
    "K": "known AMG  — identifier from a previously reported AMG",
    "E": "verified   — previously reported AMG, experimentally verified",
    "A": "attachment — CAZy identifier used for host attachment/entry",
    "P": "peptidase  — MEROPS identifier typical of viral peptidases (UNDOCUMENTED)",
    "T": "transposon — a transposon is present somewhere on the contig",
    "F": "near end   — gene within 5,000 bp of a contig end (POSITIONAL, not biological)",
    "B": "3-in-a-row — three consecutive genes all carry M",
    "J": "(never assigned — the code that would set J is commented out)",
}


def wilson(k: int, n: int) -> tuple[float, float]:
    """95% Wilson score interval. No scipy dependency."""
    if n == 0:
        return (0.0, 0.0)
    z = 1.959963985
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((c - h) / d, (c + h) / d)


def pct(k: int, n: int) -> str:
    if n == 0:
        return "     n/a"
    lo, hi = wilson(k, n)
    return f"{k/n:6.1%}  [{lo:.1%}–{hi:.1%}]"


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
    ix = {n: hdr.index(n) for n in
          ("kegg_id", "auxiliary_score", "amg_flags", "scaffold", "gene_id") if n in hdr}

    total = 0
    with_ko = 0
    letter_counts = Counter()          # how often each letter appears at all
    aux_counts = Counter()             # auxiliary score distribution
    f_by_aux = Counter()               # F-flagged, by auxiliary score
    suspect_tot = Counter()            # calls per suspect category (KO route)
    suspect_f = Counter()              # of those, how many carry F
    any_suspect_tot = 0
    any_suspect_f = 0
    f_total = 0
    ko_assigned_f = 0

    for row in it:
        if row is None or all(v is None for v in row):
            continue
        total += 1

        def cell(name):
            i = ix.get(name)
            return "" if i is None or row[i] is None else str(row[i])

        flags = cell("amg_flags")
        aux = cell("auxiliary_score").strip()
        has_f = "F" in flags

        for ch in set(flags):
            letter_counts[ch] += 1
        aux_counts[aux] += 1
        if has_f:
            f_total += 1
            f_by_aux[aux] += 1

        kid = cell("kegg_id").strip()
        m = re.search(r"K\d{5}", kid)
        if not m:
            continue
        with_ko += 1
        if has_f:
            ko_assigned_f += 1
        desc = ko_name.get(m.group(0), "")
        hit_any = False
        for lab, pat in COMPILED.items():
            if pat.search(desc):
                suspect_tot[lab] += 1
                if has_f:
                    suspect_f[lab] += 1
                hit_any = True
        if hit_any:
            any_suspect_tot += 1
            if has_f:
                any_suspect_f += 1

    print(f"\n{'=' * 78}\n{label}\n{'=' * 78}")
    print(f"  AMG calls                : {total:,}")
    print(f"  with a KEGG KO           : {with_ko:,} ({with_ko/total:.1%})")

    print(f"\n  --- Which flag letters actually occur -----------------------------------")
    for ch in "VMKEAPTFBJ":
        n = letter_counts.get(ch, 0)
        mark = "  <-- ABSENT" if n == 0 else ""
        print(f"      {ch}  {n:>8,}  {n/total:6.1%}   {FLAG_MEANING[ch]}{mark}")
    other = {c: n for c, n in letter_counts.items() if c not in FLAG_MEANING}
    if other:
        print(f"      UNEXPECTED LETTERS: {other}")

    print(f"\n  --- Auxiliary score distribution (reconstructs the filter they ran) -----")
    for k in sorted(aux_counts, key=lambda x: (x == "", x)):
        n = aux_counts[k]
        print(f"      score {k or '(blank)':<8} {n:>8,}  {n/total:6.1%}"
              f"   of which F-flagged: {f_by_aux.get(k,0):>7,}")

    print(f"\n  --- THE CHECK: is the F flag enriched in the suspect categories? --------")
    print(f"      {'stratum':<44} {'n':>8}   {'% F-flagged  [95% CI]':>24}")
    print(f"      {'-'*44} {'-'*8}   {'-'*24}")
    print(f"      {'BASELINE — all AMG calls':<44} {total:>8,}   {pct(f_total, total)}")
    print(f"      {'BASELINE — KO-assigned calls only':<44} {with_ko:>8,}   {pct(ko_assigned_f, with_ko)}")
    print(f"      {'-'*44} {'-'*8}   {'-'*24}")
    for lab in SUSPECTS:
        n = suspect_tot[lab]
        if n:
            print(f"      {lab:<44} {n:>8,}   {pct(suspect_f[lab], n)}")
    print(f"      {'-'*44} {'-'*8}   {'-'*24}")
    print(f"      {'ALL suspect categories combined':<44} {any_suspect_tot:>8,}   {pct(any_suspect_f, any_suspect_tot)}")

    if with_ko and any_suspect_tot:
        base = ko_assigned_f / with_ko
        obs = any_suspect_f / any_suspect_tot
        print(f"\n      Suspect F-rate / KO-assigned baseline F-rate = {obs/base:.2f}x"
              if base else "")


def main() -> None:
    ko_name = load_kegg()
    print(f"KEGG orthology entries loaded: {len(ko_name):,}")
    print("\nF = 'gene within 5,000 bp of a contig end' — established from")
    print("annotate_vgfs.py::get_metabolic_flags (length_from_end=5000), not assumed.")
    wb = openpyxl.load_workbook(XLSX, read_only=True, data_only=True)
    scan(wb["Table_S5_Conservative_AMGs"], ko_name, "CONSERVATIVE catalogue (post-curation)")
    scan(wb["Table_S4_Permissive_AMGs"], ko_name, "PERMISSIVE catalogue (pre-curation)")


if __name__ == "__main__":
    main()
