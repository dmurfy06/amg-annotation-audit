"""Generate Appendix A of the preprint: the 35 adjudicated families, one row each.

Pulls verdict / tier / confidence / resolving experiment out of the completed pass-1
worksheet and joins them to the frozen family list and the (now unsealed) counts.
Regenerating from source rather than transcribing means the table cannot drift from
the adjudication record.

Output: manuscript/appendix_a_families.md
"""
import csv, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "manuscript" / "appendix_a_families.md"

def clean(s: str) -> str:
    s = re.sub(r"<br>", " ", s or "")
    s = re.sub(r"[*`]", "", s)
    return re.sub(r"\s+", " ", s).strip()

# --- worksheet: family -> fields
text = (ROOT / "results" / "chunk5_worksheet_pass1_completed.md").read_text(encoding="utf-8")
adj = {}
for block in re.split(r"\n##\s+", text):
    head = block.split("\n")[0]
    m = re.search(r"`(\w+)`", head)
    if not m:
        continue
    def field(pat):
        r = re.search(pat + r"\s*\|([^|\n]*)", block, re.I)
        return clean(r.group(1)) if r else ""
    v = field(r"\*\*VERDICT\*\*")
    if not v:
        continue
    adj[m.group(1)] = {
        "verdict": v.upper(),
        "tier": field(r"\*\*Evidence tier\*\*"),
        "conf": field(r"\*\*Confidence\*\*"),
        "resolve": field(r"resolving experiment\*\*"),
    }

# --- frozen family list (order, accessions, basis, control)
fams = list(csv.DictReader(
    open(ROOT / "data" / "adjudication_families.tsv", encoding="utf-8", newline=""),
    delimiter="\t"))

# --- unsealed counts
counts = {r["family"]: r for r in csv.DictReader(
    open(ROOT / "data" / "adjudication_counts_SEALED.tsv", encoding="utf-8", newline=""),
    delimiter="\t")}

# families where the second rater independently re-rated
SECOND_PASS = {"dsrC_tusE","dut","folate","glycoside_hydrolase","glycosyltransferase",
               "NAMPT","nrdH","phoH","queuosine","rfbC","speD","TALDO1"}

lines = [
    "## Appendix A — the 35 adjudicated families",
    "",
    "Generated from the adjudication record by `scripts/build_appendix_a.py`; not transcribed.",
    "",
    "`2P` marks the 12 families re-rated in the second pass (§2.5). `C` marks a protocol",
    "control, whose verdict was fixed in advance and which therefore tests the rule rather",
    "than the rater. Counts are calls per catalogue, from the sealed file.",
    "",
    "| # | Family | Verdict | Tier | Conf. | Ocean | Soil | WW | Basis for inclusion |",
    "|---|---|---|---|---|---|---|---|---|",
]
missing = []
for f in fams:
    name = f["family"]
    a = adj.get(name)
    if not a:
        missing.append(name)
        continue
    c = counts.get(name, {})
    marks = []
    if name in SECOND_PASS: marks.append("2P")
    if (f.get("control") or "").strip(): marks.append("C")
    label = "`%s`%s" % (name, (" " + " ".join(marks)) if marks else "")
    verdict = {"COUNTS": "counts", "DOES NOT COUNT": "**does not count**",
               "UNRESOLVABLE": "**unresolvable**"}.get(a["verdict"], a["verdict"].lower())
    lines.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
        f["order"], label, verdict, a["tier"] or "—", a["conf"] or "—",
        c.get("ocean_conservative","—"), c.get("soil","—"), c.get("wastewater","—"),
        f["basis_for_inclusion"]))

lines += ["", "### Resolving experiments for the unresolvable families", ""]
for name, a in adj.items():
    if a["verdict"] == "UNRESOLVABLE":
        lines.append("- **`%s`** — %s" % (name, a["resolve"] or "(none recorded)"))

lines += ["", "### Accessions", "",
          "| Family | Accessions |", "|---|---|"]
for f in fams:
    lines.append("| `%s` | %s |" % (f["family"], f["accessions"].replace(",", ", ")))

OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("wrote %s — %d families, %d missing %s" % (OUT.name, len(fams) - len(missing),
                                                 len(missing), missing or ""))
