"""
chunk2_dedup_impact.py — does deduplication change the published disputed shares?

WHY THIS EXISTS (Rule 5: suspect your own best result)
    harmonise_catalogues.py found the soil catalogue is 28.5% surplus rows — 822 gene_ids
    appear more than once, contributing 1,306 extra rows out of 4,583. The soil figure of
    29.8% was computed PER ROW (1,365/4,583).

    A protein with three Pfam domains legitimately produces three rows. That is not an error
    in the source data — but counting it as three "AMG calls" inflates any per-call
    proportion, and if one of those domains is a glycosyltransferase the GENE is disputed
    once, not three times.

    So: recompute every disputed share on distinct genes and see whether the headline moves.
    If it does, the per-row figure has to be corrected before it goes any further.

    Reads data/harmonised_calls.tsv, produced by harmonise_catalogues.py.

Usage:
    .venv/Scripts/python.exe scripts/chunk2_dedup_impact.py
"""

import math
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TSV = ROOT / "data" / "harmonised_calls.tsv"
KEGG = ROOT / "data" / "kegg_ko_list.tsv"
OUT = ROOT / "results" / "chunk2_dedup_impact.txt"

# Pre-registered rubric, copied unchanged from amg_record_composition.py.
SUSPECTS = {
    "dcm": r"\bdcm\b",
    "queC/D/E/F": r"\bque[CDEF]\b",
    "dsrC/tusE": r"\bdsrC\b|\btusE\b",
    "folate/one-carbon": r"folate|dihydrofolate",
    "glycoside hydrolases": r"glycoside hydrolase|glucosidase|galactosidase|chitinase|lysozyme",
    "glycosyltransferases": r"glycosyltransferase",
}
COMPILED = {k: re.compile(v, re.I) for k, v in SUSPECTS.items()}

_out = []


def say(s: str = "") -> None:
    print(s)
    _out.append(s)


def wilson(k: int, n: int) -> tuple[float, float]:
    if n == 0:
        return (0.0, 0.0)
    z = 1.959963985
    p, d = k / n, 1 + 1.959963985**2 / n
    c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((c - h) / d, (c + h) / d)


def pct(k: int, n: int) -> str:
    if n == 0:
        return "n/a"
    lo, hi = wilson(k, n)
    return f"{k/n:6.2%}  [{lo:.2%}–{hi:.2%}]"


def load_kegg() -> dict[str, str]:
    ko = {}
    for line in KEGG.read_text(encoding="utf-8").splitlines():
        p = line.split("\t")
        if len(p) >= 2:
            ko[p[0].replace("ko:", "")] = p[1].strip()
    return ko


def is_suspect(row: dict, ko_name: dict[str, str], route: str) -> bool:
    """route 'ko'   — match KEGG's own description of the accession (exact, trustworthy)
       route 'pfam' — match the Pfam domain description only (one source, per the
                      47.5% artefact lesson: never match across heterogeneous columns)"""
    if route == "ko":
        if not row["ko"]:
            return False
        text = ko_name.get(row["ko"], "")
    else:
        text = row["description"]
    return any(p.search(text) for p in COMPILED.values())


def analyse(rows: list[dict], label: str, route: str, ko_name) -> None:
    denom_rows = [r for r in rows if (r["ko"] if route == "ko" else r["description"])]
    n_rows = len(denom_rows)
    sus_rows = sum(1 for r in denom_rows if is_suspect(r, ko_name, route))

    # Collapse to genes. A gene is disputed if ANY of its rows is disputed.
    genes = defaultdict(list)
    for r in denom_rows:
        genes[r["gene_id"]].append(r)
    n_genes = len(genes)
    sus_genes = sum(1 for rs in genes.values()
                    if any(is_suspect(r, ko_name, route) for r in rs))

    say(f"\n  {label}   (matched via {route.upper()})")
    say(f"    per ROW  : {sus_rows:>6,} / {n_rows:>6,}   {pct(sus_rows, n_rows)}")
    say(f"    per GENE : {sus_genes:>6,} / {n_genes:>6,}   {pct(sus_genes, n_genes)}")
    if n_rows and n_genes:
        shift = (sus_genes / n_genes) - (sus_rows / n_rows)
        verdict = "NEGLIGIBLE" if abs(shift) < 0.005 else "MATERIAL — the per-row figure must be corrected"
        say(f"    shift    : {shift:+.2%} percentage points   -> {verdict}")


def main() -> None:
    ko_name = load_kegg()
    rows = []
    with TSV.open(encoding="utf-8") as fh:
        hdr = fh.readline().rstrip("\n").split("\t")
        for line in fh:
            rows.append(dict(zip(hdr, line.rstrip("\n").split("\t"))))

    say("CHUNK 2 — does deduplication move the published numbers?")
    say("=" * 78)
    say("A gene is counted as disputed if ANY of its rows is disputed, so collapsing can only")
    say("lower a proportion, never raise it.")

    by_cat = defaultdict(list)
    for r in rows:
        by_cat[r["catalogue"]].append(r)

    say("\nOCEAN — the 25.1% headline")
    analyse(by_cat["ocean_conservative"], "ocean conservative", "ko", ko_name)
    analyse(by_cat["ocean_permissive"], "ocean permissive", "ko", ko_name)

    say("\nSOIL — the 29.8% headline, computed per row on a table that is 28.5% surplus rows")
    analyse(by_cat["soil"], "soil", "pfam", ko_name)

    say("\nSOIL via KEGG, for comparison with the ocean route")
    analyse(by_cat["soil"], "soil", "ko", ko_name)

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("\n".join(_out) + "\n", encoding="utf-8")
    say(f"\nWrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
