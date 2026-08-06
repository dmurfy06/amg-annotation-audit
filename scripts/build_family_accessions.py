"""
build_family_accessions.py — generate the CANDIDATE accession list that replaces free-text
matching, per Amendment 1 of 08_adjudication_protocol.md.

WHAT THIS IS, AND WHAT IT IS NOT
    It is a *proposal generator*. It sweeps the harmonised calls, finds every KEGG KO and Pfam
    accession whose official description plausibly belongs to one of the six frozen families,
    and writes them out with their descriptions and per-catalogue call counts.

    It is NOT the frozen list. Generation is mechanical; INCLUSION IS A JUDGEMENT, and the
    protocol requires that judgement to be made accession by accession and recorded.

WHY THIS IS BETTER THAN THE REGEX IT REPLACES
    The generator still uses text patterns — there is no other way to propose candidates from
    thousands of accessions. The difference is what a human then reviews:

        before : a regex, applied invisibly to 349,272 rows. Unreviewable.
        after  : ~40 accessions on one page, each with its official name and its call count.

    A wrong accession is now a visible line someone can object to. A wrong regex was a silent
    difference of thousands of calls that took a full harmonisation to notice.

    So the patterns below are deliberately WIDE. Over-proposing is cheap — a bad candidate is
    struck out during review. Under-proposing is what caused the 9x soil error, because a
    missing accession never appears anywhere to be questioned.

Output
    data/family_accessions.tsv   — candidate list, for review and freezing

Usage:
    .venv/Scripts/python.exe scripts/build_family_accessions.py
"""

import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TSV = ROOT / "data" / "harmonised_calls.tsv"
KEGG = ROOT / "data" / "kegg_ko_list.tsv"
OUT = ROOT / "data" / "family_accessions.tsv"
REPORT = ROOT / "results" / "chunk2_family_accessions.txt"

# Deliberately wide. Over-proposal is corrected by review; under-proposal is invisible.
PROPOSE = {
    "dcm": r"cytosine.{0,25}methyl|\bdcm\b|DNA methylase|C-5 cytosine|methyltransferase.{0,10}cytosine",
    "queuosine": r"\bque[CDEFAG]\b|queuosine|deazaguanine|preQ|tetrahydropterin|"
                 r"nitrile reductase|7-carboxy|epoxyqueuosine|tRNA-guanine transglycosylase",
    "dsrC_tusE": r"\bdsrC\b|\btusE\b|dissimilatory sulf|sulphur relay|sulfur relay|DsrC",
    "folate": r"folate|folE|dihydropteroate|dihydrofolate|dihydroneopterin|"
              r"GTP cyclohydrolase I|aminodeoxychorismate|tetrahydrofolate",
    "glycoside_hydrolase": r"glycosid(e|yl)\s*hydrolase|glucosidase|galactosidase|chitinase|"
                           r"lysozyme|cellulase|muramidase|glucanase",
    "glycosyltransferase": r"glycosyl\s*transferase|glycosyltransferase",
}
COMPILED = {k: re.compile(v, re.I) for k, v in PROPOSE.items()}

# Named in Amendment 1 as ambiguous BEFORE any counting: both sit at the branch point where
# folate and queuosine biosynthesis diverge, so no single family assignment is defensible.
AMBIGUOUS_HINT = {
    "K01495": "folE / GTP cyclohydrolase I — first step of BOTH folate and queuosine",
    "PF01227": "GTP cyclohydrolase I — first step of BOTH folate and queuosine",
    "K01737": "queD / 6-pyruvoyl tetrahydropterin synthase — pterin shared with folate",
    "PF01242": "6-pyruvoyl tetrahydropterin synthase — pterin shared with folate",
    # Found during the accession-by-accession review, 2026-08-05. Same branch point as folE:
    # GTP cyclohydrolase IB is an alternative to folE and feeds the identical shared step.
    "K09007": "folE2 / GTP cyclohydrolase IB — same folate/queuosine branch point as folE",
    "PF02649": "Type I GTP cyclohydrolase folE2 — same branch point as folE",
}

# REVIEW DECISIONS, 2026-08-05. Recorded per Amendment 1: generation is mechanical, inclusion
# is a judgement. Each exclusion states its reason and is auditable on one line.
#
# These are exactly the errors the accession list exists to expose. Under free-text matching
# every one of them was an invisible contribution of thousands of calls.
EXCLUDE = {
    "PF13385": (
        "glycoside_hydrolase",
        "STRUCTURAL FOLD, NOT AN ACTIVITY. 'Concanavalin A-like lectin/glucanases "
        "superfamily' is a shared beta-sandwich fold. Concanavalin A is a lectin — it BINDS "
        "sugars, it does not hydrolyse them. Matched only via the substring 'glucanases'. "
        "This single accession was 21,567 of the family's 21,690 calls (99.4%). Same class of "
        "error as the 47.5% CAZy artefact: a pattern hitting a fold name rather than a function."
    ),
    "K14652": (
        "folate",
        "WRONG PATHWAY. ribBA is GTP cyclohydrolase II — RIBOFLAVIN biosynthesis. Folate and "
        "queuosine use GTP cyclohydrolase I. Matched only on the shared string 'GTP "
        "cyclohydrolase'. Roman numerals distinguish two unrelated enzymes here."
    ),
}

PFAM_RE = re.compile(r"^(.*?)\s*\[(PF\d{5})[.\d]*\]")


def main() -> None:
    ko_name = {}
    for line in KEGG.read_text(encoding="utf-8").splitlines():
        p = line.split("\t")
        if len(p) >= 2:
            ko_name[p[0].replace("ko:", "")] = p[1].strip()

    rows = []
    with TSV.open(encoding="utf-8") as fh:
        hdr = fh.readline().rstrip("\n").split("\t")
        for line in fh:
            rows.append(dict(zip(hdr, line.rstrip("\n").split("\t"))))

    # Observed accessions -> official description, and per-catalogue call counts.
    ko_counts = defaultdict(Counter)
    pf_counts = defaultdict(Counter)
    pf_desc = {}
    for r in rows:
        cat = r["catalogue"]
        if r["ko"]:
            ko_counts[r["ko"]][cat] += 1
        pid = r["pfam_id"]
        if pid.startswith("PF"):
            pf_counts[pid][cat] += 1
            if pid not in pf_desc:
                for part in r["pfam_text"].split(";"):
                    m = PFAM_RE.match(part.strip())
                    if m and m.group(2) == pid:
                        pf_desc[pid] = m.group(1)
                        break

    excluded = []

    def classify(acc, family):
        if acc in EXCLUDE and EXCLUDE[acc][0] == family:
            return "EXCLUDED", EXCLUDE[acc][1]
        if acc in AMBIGUOUS_HINT:
            return "AMBIGUOUS", AMBIGUOUS_HINT[acc]
        return "INCLUDED", ""

    cats = ["ocean_conservative", "ocean_permissive", "soil", "wastewater"]
    lines = ["family\tnamespace\taccession\tofficial_description\t"
             + "\t".join(cats) + "\ttotal\tstatus\tnote"]
    summary = defaultdict(lambda: [0, 0])

    for family, pat in COMPILED.items():
        for acc, desc in sorted(ko_name.items()):
            if acc in ko_counts and pat.search(desc):
                c = ko_counts[acc]
                tot = sum(c.values())
                status, note = classify(acc, family)
                lines.append(f"{family}\tKO\t{acc}\t{desc}\t"
                             + "\t".join(str(c.get(x, 0)) for x in cats)
                             + f"\t{tot}\t{status}\t{note}")
                if status == "EXCLUDED":
                    excluded.append((acc, family, tot, note))
                else:
                    summary[family][0] += 1
                    summary[family][1] += tot
        for acc in sorted(pf_counts):
            desc = pf_desc.get(acc, "")
            if desc and pat.search(desc):
                c = pf_counts[acc]
                tot = sum(c.values())
                status, note = classify(acc, family)
                lines.append(f"{family}\tPFAM\t{acc}\t{desc}\t"
                             + "\t".join(str(c.get(x, 0)) for x in cats)
                             + f"\t{tot}\t{status}\t{note}")
                if status == "EXCLUDED":
                    excluded.append((acc, family, tot, note))
                else:
                    summary[family][0] += 1
                    summary[family][1] += tot

    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    out = [f"FAMILY ACCESSION LIST — {len(lines)-1} candidates proposed, reviewed 2026-08-05",
           "=" * 78,
           "Per Amendment 1: generation is mechanical, inclusion is a judgement. Every decision",
           "below is recorded on one line and can be objected to without rerunning anything.", "",
           "  INCLUDED / AMBIGUOUS counts, after review:"]
    for fam in PROPOSE:
        n, tot = summary[fam]
        out.append(f"    {fam:<24} {n:>3} accessions   {tot:>7,} calls")
    amb = sum(1 for ln in lines[1:] if "\tAMBIGUOUS\t" in ln)
    out += ["", f"  AMBIGUOUS — reported separately, never forced into one family: {amb}"]
    if excluded:
        out += ["", "  EXCLUDED BY REVIEW — the errors this method exists to expose:"]
        for acc, fam, tot, note in sorted(excluded, key=lambda x: -x[2]):
            out += [f"    {acc}  ({fam}) — would have contributed {tot:,} calls"]
            for i in range(0, len(note), 88):
                out.append(f"        {note[i:i+88]}")
    out += ["", f"  Written to {OUT.relative_to(ROOT)}."]
    print("\n".join(out))
    REPORT.parent.mkdir(exist_ok=True)
    REPORT.write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
