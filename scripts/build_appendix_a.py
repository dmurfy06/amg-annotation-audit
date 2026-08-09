"""Generate Appendix A and inject it into the manuscript between markers.

Appendix A is the actual result table - all 35 families with their verdicts - so it belongs
in the paper, not in a side file the submitted PDF cannot reach. This script regenerates it
from the adjudication record and writes it directly into preprint_draft.md between
<!-- APPENDIX_A_START --> and <!-- APPENDIX_A_END -->, so the table can never drift from the
verdicts it reports and there is only one file to submit.

Two columns are compressed for print. The worksheet records tiers and confidence with prose
qualifiers ("6 (chemistry only; no Tier 1-5 available)", "high (in the unresolvability)")
which are useful in the working record and unreadable in a 6.5-inch table column; the
qualifier is dropped here and the full text remains in
results/chunk5_worksheet_pass1_completed.md. The basis-for-inclusion strings are replaced by
single-letter codes with a legend.

Output: rewrites the Appendix A block inside manuscript/preprint_draft.md
"""

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANUSCRIPT = ROOT / "manuscript" / "preprint_draft.md"
START = "<!-- APPENDIX_A_START -->"
END = "<!-- APPENDIX_A_END -->"

SECOND_PASS = {"dsrC_tusE", "dut", "folate", "glycoside_hydrolase", "glycosyltransferase",
               "NAMPT", "nrdH", "phoH", "queuosine", "rfbC", "speD", "TALDO1"}


def clean(s: str) -> str:
    s = re.sub(r"<br\s*/?>", " ", s or "")
    s = re.sub(r"[*`]", "", s)
    return re.sub(r"\s+", " ", s).strip()


def short(s: str) -> str:
    """Drop the prose qualifier: '6 (chemistry only...)' -> '6'."""
    return re.split(r"[(;]", clean(s))[0].strip() or "—"


def basis_codes(s: str) -> str:
    codes = []
    if ">=1%" in s or "≥1%" in s:
        codes.append("A")
    if "Martin" in s:
        codes.append("M")
    if "control" in s.lower():
        codes.append("C")
    return " ".join(codes) or "—"


def main() -> None:
    text = (ROOT / "results" / "chunk5_worksheet_pass1_completed.md").read_text(encoding="utf-8")
    adj = {}
    for block in re.split(r"\n##\s+", text):
        m = re.search(r"`(\w+)`", block.split("\n")[0])
        if not m:
            continue

        def field(pat):
            r = re.search(pat + r"\s*\|([^|\n]*)", block, re.I)
            return clean(r.group(1)) if r else ""

        verdict = field(r"\*\*VERDICT\*\*")
        if not verdict:
            continue
        adj[m.group(1)] = {
            "verdict": verdict.upper(),
            "tier": short(field(r"\*\*Evidence tier\*\*")),
            "conf": short(field(r"\*\*Confidence\*\*")),
            "resolve": field(r"resolving experiment\*\*"),
        }

    fams = list(csv.DictReader(
        open(ROOT / "data" / "adjudication_families.tsv", encoding="utf-8", newline=""),
        delimiter="\t"))
    counts = {r["family"]: r for r in csv.DictReader(
        open(ROOT / "data" / "adjudication_counts_SEALED.tsv", encoding="utf-8", newline=""),
        delimiter="\t")}

    L = []
    L.append("Verdicts, evidence tiers and per-catalogue call counts for every adjudicated")
    L.append("family. Generated directly from the adjudication record by")
    L.append("`scripts/build_appendix_a.py`, not transcribed, so it cannot drift from the")
    L.append("verdicts it reports.")
    L.append("")
    L.append("**Marks.** `2P` — re-rated in the second pass (§2.5). `C` — protocol control,")
    L.append("verdict fixed in advance. **Basis codes.** A — met the abundance threshold;")
    L.append("M — named by Martin *et al.*; C — control. Tier and confidence are given without")
    L.append("the prose qualifiers recorded in the worksheet; the full text is in")
    L.append("`results/chunk5_worksheet_pass1_completed.md`.")
    L.append("")
    L.append("| # | Family | Verdict | Tier | Conf. | Ocean | Soil | WW | Basis |")
    L.append("|---|---|---|---|---|---|---|---|---|")
    missing = []
    for f in fams:
        name = f["family"]
        a = adj.get(name)
        if not a:
            missing.append(name)
            continue
        c = counts.get(name, {})
        marks = []
        if name in SECOND_PASS:
            marks.append("2P")
        if (f.get("control") or "").strip():
            marks.append("C")
        label = "`%s`%s" % (name, (" " + " ".join(marks)) if marks else "")
        verdict = {"COUNTS": "counts",
                   "DOES NOT COUNT": "**does not count**",
                   "UNRESOLVABLE": "**unresolvable**"}.get(a["verdict"], a["verdict"].lower())
        L.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            f["order"], label, verdict, a["tier"], a["conf"],
            c.get("ocean_conservative", "—"), c.get("soil", "—"),
            c.get("wastewater", "—"), basis_codes(f["basis_for_inclusion"])))

    L.append("")
    L.append("**Resolving experiments for the three unresolvable families.** Each unresolvable")
    L.append("verdict must name the experiment that would settle it, or the family is")
    L.append("*unresearched* rather than unresolvable and defaults to COUNTS (§2.3).")
    L.append("")
    for name, a in adj.items():
        if a["verdict"] == "UNRESOLVABLE":
            L.append("- **`%s`** — %s" % (name, a["resolve"] or "(none recorded)"))

    L.append("")
    L.append("**Accessions.** Family membership is by accession, never by text match (§2.2).")
    L.append("")
    L.append("| Family | KEGG accessions |")
    L.append("|---|---|")
    for f in fams:
        L.append("| `%s` | %s |" % (f["family"], f["accessions"].replace(",", ", ")))

    body = "\n".join(L)
    doc = MANUSCRIPT.read_text(encoding="utf-8")
    if START not in doc or END not in doc:
        raise SystemExit("markers %s / %s not found in %s" % (START, END, MANUSCRIPT.name))
    new = re.sub(re.escape(START) + r".*?" + re.escape(END),
                 START + "\n\n" + body + "\n\n" + END, doc, flags=re.S)
    MANUSCRIPT.write_text(new, encoding="utf-8")
    print("injected Appendix A: %d families, %d missing %s"
          % (len(fams) - len(missing), len(missing), missing or ""))


if __name__ == "__main__":
    main()
