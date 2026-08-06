"""
chunk2_final_shares.py — the disputed share, recomputed against the FROZEN accession list.

This supersedes every earlier figure in the project. All of those (25.1%, 11.0%, 29.8%, 22.7%)
were produced by matching free text and are void under Amendment 1 of the adjudication protocol.

WHAT IT DOES
    Loads data/family_accessions.tsv — the reviewed, frozen list — and classifies every call by
    ACCESSION MEMBERSHIP only. No text is matched anywhere in this script.

WHAT IT REPORTS, AND WHY ALL OF IT TOGETHER
    Three choices change the answer and each must be declared, so all three are always shown:

      namespace   KO or Pfam        — a call can only be judged in a namespace it carries
      unit        row or gene       — soil rows are per Pfam DOMAIN, so rows overcount genes
      ambiguity   strict or wide    — whether folE/queD/folE2 count (Amendment 1, clause 3)

    The gap between strict and wide is itself a declared result, not a footnote.

NOTE ON WHAT "DISPUTED" MEANS HERE
    It means "belongs to a family Martin et al. argue should be reconsidered". It does NOT mean
    the call is wrong. Deciding that is the Chunk 5 adjudication, which has not run.

Usage:
    .venv/Scripts/python.exe scripts/chunk2_final_shares.py
"""

import csv
import math
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TSV = ROOT / "data" / "harmonised_calls.tsv"
ACC = ROOT / "data" / "family_accessions.tsv"
OUT = ROOT / "results" / "chunk2_final_shares.txt"

CATALOGUES = [
    ("ocean_conservative", "Ocean, curated (Microbiome 2024)"),
    ("ocean_permissive", "Ocean, pre-curation"),
    ("soil", "Soil (ISME J 2022)"),
    ("wastewater", "Wastewater (ES&T 2023)"),
]

_out = []


def say(s: str = "") -> None:
    print(s)
    _out.append(s)


def wilson(k: int, n: int) -> tuple[float, float]:
    if n == 0:
        return (0.0, 0.0)
    z = 1.959963985
    p, d = k / n, 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((c - h) / d, (c + h) / d)


def pct(k: int, n: int) -> str:
    if n == 0:
        return "         —"
    lo, hi = wilson(k, n)
    return f"{k/n*100:6.2f}% [{lo*100:5.2f}–{hi*100:5.2f}]"


def load_accessions():
    """-> {namespace: {accession: (family, status)}}  for INCLUDED and AMBIGUOUS only."""
    table = {"KO": {}, "PFAM": {}}
    with ACC.open(encoding="utf-8") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            if r["status"] == "EXCLUDED":
                continue
            table[r["namespace"]][r["accession"]] = (r["family"], r["status"])
    return table


def main() -> None:
    acc = load_accessions()
    say("DISPUTED SHARE — recomputed against the frozen accession list")
    say("=" * 78)
    say(f"Rubric: {len(acc['KO'])} KO + {len(acc['PFAM'])} Pfam accessions, "
        f"{sum(1 for d in acc.values() for v in d.values() if v[1]=='AMBIGUOUS')} of them AMBIGUOUS.")
    say("No text is matched in this script. Membership is by accession only.")
    say("")
    say("  strict = INCLUDED accessions only")
    say("  wide   = INCLUDED + AMBIGUOUS (folE, folE2, queD — the folate/queuosine branch point)")

    rows = []
    with TSV.open(encoding="utf-8") as fh:
        hdr = fh.readline().rstrip("\n").split("\t")
        for line in fh:
            rows.append(dict(zip(hdr, line.rstrip("\n").split("\t"))))
    by_cat = defaultdict(list)
    for r in rows:
        by_cat[r["catalogue"]].append(r)

    for cat, label in CATALOGUES:
        pool_all = by_cat.get(cat, [])
        if not pool_all:
            continue
        say(f"\n{'=' * 78}\n{label}   —   {len(pool_all):,} calls\n{'=' * 78}")
        say(f"  {'namespace / unit':<26} {'n':>8}  {'strict':>21}  {'wide (+ambiguous)':>21}")
        say(f"  {'-'*26} {'-'*8}  {'-'*21}  {'-'*21}")

        for ns, key in (("KO", "ko"), ("PFAM", "pfam_id")):
            pool = [r for r in pool_all if r[key] in acc[ns]] or None
            denom = [r for r in pool_all if r[key]]
            if not denom:
                continue
            strict_rows = sum(1 for r in denom
                              if r[key] in acc[ns] and acc[ns][r[key]][1] == "INCLUDED")
            wide_rows = sum(1 for r in denom if r[key] in acc[ns])

            g_strict, g_wide, g_all = defaultdict(bool), defaultdict(bool), set()
            for r in denom:
                g_all.add(r["gene_id"])
                if r[key] in acc[ns]:
                    g_wide[r["gene_id"]] = True
                    if acc[ns][r[key]][1] == "INCLUDED":
                        g_strict[r["gene_id"]] = True

            say(f"  {ns + ', per call':<26} {len(denom):>8,}  "
                f"{pct(strict_rows, len(denom)):>21}  {pct(wide_rows, len(denom)):>21}")
            say(f"  {ns + ', per gene':<26} {len(g_all):>8,}  "
                f"{pct(sum(g_strict.values()), len(g_all)):>21}  "
                f"{pct(sum(g_wide.values()), len(g_all)):>21}")

            fam = Counter()
            for r in denom:
                if r[key] in acc[ns]:
                    f, st = acc[ns][r[key]]
                    fam[f + ("  (AMBIGUOUS)" if st == "AMBIGUOUS" else "")] += 1
            if fam:
                say(f"      composition ({ns}): " + " · ".join(
                    f"{k} {v:,}" for k, v in fam.most_common()))

    say(f"\n{'=' * 78}\nWHAT SUPERSEDES WHAT\n{'=' * 78}")
    say("  Every earlier figure — 25.1%, 13.4%, 11.0%, 29.8%, 22.7%, 19.8% — was produced by")
    say("  free-text matching and is VOID under Amendment 1. The table above replaces them.")
    say("  Nothing here is an adjudication: 'disputed' means 'in a family Martin et al. argue")
    say("  should be reconsidered', not 'wrong'. Chunk 5 decides that.")

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("\n".join(_out) + "\n", encoding="utf-8")
    say(f"\nWrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
