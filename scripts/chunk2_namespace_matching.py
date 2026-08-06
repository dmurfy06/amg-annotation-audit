"""
chunk2_namespace_matching.py — apply the frozen rubric correctly in each annotation
namespace, and SHOW every string it matched so under- and over-matching are both visible.

THE PROBLEM THIS SOLVES
    The frozen rubric was written as regexes against KEGG's wording. Applied literally to
    Pfam it silently under-matches, because Pfam spells the same biology differently:

        family                KEGG says                     Pfam says
        glycosyltransferase   "glycosyltransferase"         "Glycosyl transferases group 1"
        dcm                   "DNA (cytosine-5-)-methyl-    "C-5 cytosine-specific DNA
                               transferase"                  methylase [PF00145.17]"

    Matching r"glycosyltransferase" against Pfam finds 83 of 1,238 real hits. Matching
    r"...methyltransferase" against Pfam finds 0 of 5,277 real dcm hits. Neither failure
    raises an error; both just quietly produce a smaller number.

    A second, subtler trap: in DRAM-v output `gene_description` is KEGG-DERIVED. Matching it
    and calling the result a Pfam measurement produces a KEGG answer wearing a Pfam label.
    This script matches `pfam_text` (Pfam's own wording) for the Pfam route. Nothing else.

THE RULE ADOPTED, AND IT IS THE REAL LESSON
    Never trust a pattern you have not seen matched against real strings. Every family and
    namespace below prints its distinct matched strings with counts, so over-matching (the
    47.5% artefact) and under-matching (this one) are both caught by looking.

    The families are UNCHANGED from the frozen rubric. Only spelling tolerance changes.
    Note the direction: these corrections RAISE the disputed share, i.e. they favour the
    project's own hypothesis — which is why both figures are always reported together.

Usage:
    .venv/Scripts/python.exe scripts/chunk2_namespace_matching.py
"""

import math
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TSV = ROOT / "data" / "harmonised_calls.tsv"
KEGG = ROOT / "data" / "kegg_ko_list.tsv"
OUT = ROOT / "results" / "chunk2_namespace_matching.txt"

# Same six families as the frozen rubric. One pattern per namespace, each verified against
# the strings actually present in the data (see the VALIDATION section of the output).
FAMILIES = {
    "dcm — DNA cytosine methyltransferase": {
        "ko":   r"\bdcm\b|DNA \(cytosine-5-\)-methyltransferase",
        "pfam": r"C-5 cytosine-specific DNA methylase|cytosine[- ]specific.{0,20}methyl",
    },
    "queC/D/E/F — queuosine biosynthesis": {
        "ko":   r"\bque[CDEF]\b|queuosine",
        "pfam": r"\bque[CDEF]\b|queuosine|7-cyano-7-deazaguanine|7-carboxy-7-deazaguanine|preQ",
    },
    "dsrC / tusE — sulfur relay": {
        "ko":   r"\bdsrC\b|\btusE\b",
        "pfam": r"\bdsrC\b|\btusE\b|dissimilatory sulphite|dissimilatory sulfite",
    },
    "folate / one-carbon": {
        "ko":   r"folate|dihydrofolate",
        "pfam": r"folate|dihydropteroate|dihydroneopterin|GTP cyclohydrolase I|pterin",
    },
    "glycoside hydrolases": {
        "ko":   r"glycoside hydrolase|glucosidase|galactosidase|chitinase|lysozyme",
        "pfam": r"glycosid(e|yl)\s*hydrolase|glucosidase|galactosidase|chitinase|lysozyme",
    },
    "glycosyltransferases": {
        "ko":   r"glycosyltransferase",
        "pfam": r"glycosyl\s*transferase",
    },
}
COMPILED = {f: {ns: re.compile(p, re.I) for ns, p in d.items()} for f, d in FAMILIES.items()}
# The literal frozen KEGG-worded patterns, kept to quantify the defect.
FROZEN = {f: re.compile(d["ko"].split("|")[0], re.I) for f, d in FAMILIES.items()}

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
        return "n/a"
    lo, hi = wilson(k, n)
    return f"{k/n:6.2%} [{lo:.2%}–{hi:.2%}]"


def load_kegg() -> dict[str, str]:
    ko = {}
    for line in KEGG.read_text(encoding="utf-8").splitlines():
        p = line.split("\t")
        if len(p) >= 2:
            ko[p[0].replace("ko:", "")] = p[1].strip()
    return ko


def text_for(r: dict, ns: str, ko_name: dict[str, str]) -> str:
    """The ONLY string a given namespace is allowed to match against."""
    if ns == "ko":
        return ko_name.get(r["ko"], "") if r["ko"] else ""
    return r["pfam_text"]


def report(rows, label, ns, ko_name, validate=True):
    pool = [r for r in rows if text_for(r, ns, ko_name)]
    if not pool:
        say(f"\n  {label} — no rows carry a {ns.upper()} identifier")
        return

    per_family = Counter()
    matched_strings = defaultdict(Counter)
    sus_rows = frozen_rows = 0
    genes = defaultdict(bool)

    for r in pool:
        t = text_for(r, ns, ko_name)
        hit = False
        for fam, pats in COMPILED.items():
            if pats[ns].search(t):
                per_family[fam] += 1
                matched_strings[fam][t[:70]] += 1
                hit = True
        sus_rows += hit
        genes[r["gene_id"]] |= hit
        if any(p.search(t) for p in FROZEN.values()):
            frozen_rows += 1

    n_rows, n_genes = len(pool), len(genes)
    sus_genes = sum(1 for v in genes.values() if v)

    say(f"\n  {label}  —  matched on {ns.upper()} ({n_rows:,} rows carry one)")
    for fam, n in per_family.most_common():
        say(f"      {fam:<40} {n:>7,}")
    say(f"    {'DISPUTED, per row':<44} {sus_rows:>7,}  {pct(sus_rows, n_rows)}")
    say(f"    {'DISPUTED, per distinct gene':<44} {sus_genes:>7,}  {pct(sus_genes, n_genes)}"
        f"  (of {n_genes:,})")
    if frozen_rows != sus_rows:
        say(f"    {'frozen KEGG-worded patterns would give':<44} {frozen_rows:>7,}"
            f"  {pct(frozen_rows, n_rows)}   <- the defect")

    if validate and matched_strings:
        say(f"    VALIDATION — every distinct string matched, so false positives are visible:")
        for fam in per_family:
            top = matched_strings[fam].most_common(3)
            extra = len(matched_strings[fam]) - len(top)
            say(f"      [{fam}]")
            for s, n in top:
                say(f"         {n:>6,}  {s}")
            if extra > 0:
                say(f"         … and {extra} other distinct string(s)")


def main() -> None:
    ko_name = load_kegg()
    rows = []
    with TSV.open(encoding="utf-8") as fh:
        hdr = fh.readline().rstrip("\n").split("\t")
        for line in fh:
            rows.append(dict(zip(hdr, line.rstrip("\n").split("\t"))))
    by_cat = defaultdict(list)
    for r in rows:
        by_cat[r["catalogue"]].append(r)

    say("CHUNK 2 — the frozen rubric, applied correctly per namespace")
    say("=" * 78)

    say("\nOCEAN CONSERVATIVE — the same catalogue, measured two ways")
    report(by_cat["ocean_conservative"], "ocean conservative", "ko", ko_name)
    report(by_cat["ocean_conservative"], "ocean conservative", "pfam", ko_name)

    say("\nSOIL — the 29.8% headline")
    report(by_cat["soil"], "soil", "pfam", ko_name)
    report(by_cat["soil"], "soil", "ko", ko_name, validate=False)

    say("\nOCEAN PERMISSIVE — for the curation comparison (H2)")
    report(by_cat["ocean_permissive"], "ocean permissive", "ko", ko_name, validate=False)
    report(by_cat["ocean_permissive"], "ocean permissive", "pfam", ko_name, validate=False)

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("\n".join(_out) + "\n", encoding="utf-8")
    say(f"\nWrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
