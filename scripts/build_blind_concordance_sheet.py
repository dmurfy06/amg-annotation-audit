"""Build the blind concordance sheet for the 12 judgement-call families.

Both raters must see the same *evidence* and none of the same *conclusions*.
The dossiers were written before the first adjudication and carry my framing in
places, so this removes:

  1. passages naming a verdict (COUNTS / DOES NOT COUNT / UNRESOLVABLE)
  2. "Tier available: N" - tier is a field the second rater assigns
  3. pre-named resolving experiments - naming one implies UNRESOLVABLE is live

A blunt blockquote-drop was tried first and removed real evidence with the
steers (nrdH lost the shared-dNTP-pool fact; glycosyltransferase lost its whole
HOST/VIRAL framing). So the five affected families get explicit hand-written
edits below, each asserted to match, and everything else is generic.

What survives for every family: what the enzyme does, the phage-specific
literature with citations, and the case for HOST and VIRAL side by side.
"""

import io
import os
import re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VAULT = (r"C:\Users\danie\OneDrive\Documente\Obsidian Vault"
         r"\1 Projects\Research Project 2026")

# Every family where evidence was found and had to be weighed - the only places
# two raters applying the same rule could legitimately diverge. Families decided
# mechanically (Tier 6 only -> COUNTS) are excluded: agreement there is forced
# by the rule and measures nothing.
JUDGEMENT_FAMILIES = [
    "dsrC_tusE", "dut", "folate", "glycoside_hydrolase",
    "glycosyltransferase", "NAMPT", "nrdH", "phoH",
    "queuosine", "rfbC", "speD", "TALDO1",
]

VERDICT_WORDS = re.compile(r"DOES NOT COUNT|COUNTS|UNRESOLVABLE|verdict", re.I)

# Worksheet section numbers -> family, so cross-references survive renumbering.
SECTION_MAP = {
    7: "galE", 8: "glmS", 10: "glycosyltransferase", 11: "gmd", 17: "manB",
    22: "phoH", 25: "pseB", 26: "queuosine", 28: "rfbB", 29: "rfbC",
    31: "tagD", 33: "UGDH",
}

# (pattern, replacement) applied to the raw section before generic cleanup.
# Each must match exactly once or the build fails loudly - the dossiers can
# drift, and a silent miss would leak a steer into a blind sheet.
PRE_EDITS = {
    "dsrC_tusE": [
        (r"\*\*Tier available: 3.4\*\* for the ecology; \*\*effectively 0\*\* for "
         r"telling which gene the\s+environmental calls actually are\.",
         "**Note.** Nothing in the environmental data tells you which of the two "
         "genes a given call actually is."),
        (r"\*\*Resolving experiment, if UNRESOLVABLE:\*\*.*?K11179\.", ""),
    ],
    "nrdH": [
        (r"\*\*Tier available: 4.5\.\*\* No experiment separates.*?"
         r"experiment problem to name\.",
         "**A complication.** No experiment separates \"the host's dNTP pool\" "
         "from \"the phage's\" during infection, **because during infection they "
         "are the same pool.**"),
    ],
    "queuosine": [
        (r"> That may be a genuine \*\*UNRESOLVABLE\*\*\..*?systematically\.",
         "> Thiaville's chemical detection was done for a single phage; nobody "
         "has repeated it\n> systematically."),
    ],
    "rfbC": [
        (r"\*\*Case for HOST / VIRAL:\*\* as .10, and with less of the "
         r"precursor-ambiguity caveat\. If you reach\s+different verdicts for "
         r".10 and .29, be sure you can say why\.",
         "**Case for HOST / VIRAL:** as for `glycosyltransferase` above, and "
         "with less of the\nprecursor-ambiguity caveat."),
    ],
    "glycosyltransferase": [
        (r"> Three defensible readings, all permitted:.*?"
         r"stronger paper than hiding it\.",
         "> The protocol has no category for \"the rule cannot classify this.\" "
         "Whatever you decide,\n> record in the Note field that the rule "
         "underdetermined it."),
    ],
}


def read(path):
    return io.open(path, encoding="utf-8").read()


def split_sections(text):
    out = {}
    for part in re.split(r"^## ", text, flags=re.M)[1:]:
        head = part.split("\n", 1)[0]
        name = head.split("`")[1] if "`" in head else head.strip()
        out[name] = part
    return out


def deref_sections(text):
    """Turn worksheet '<section-sign>10' cross-refs into family names."""
    def sub(m):
        fam = SECTION_MAP.get(int(m.group(1)))
        return "`%s`" % fam if fam else "another family"
    return re.sub(r"\u00a7\s*(\d+)", sub, text)


def strip_leaks(family, body):
    text = "\n".join(body.split("\n")[1:])  # drop heading line

    for pattern, repl in PRE_EDITS.get(family, []):
        text, n = re.subn(pattern, repl, text, flags=re.S)
        if n != 1:
            raise SystemExit(
                "pre-edit for %s matched %d times (expected 1) - dossier text "
                "has drifted, refusing to build a sheet that may leak" % (family, n))

    # generic: remaining tier/resolving-experiment paragraphs
    text = re.sub(r"\*\*Tier available.*?(?=\n\s*\n|\Z)", "", text, flags=re.S)
    text = re.sub(r"\*\*Resolving experiment.*?(?=\n\s*\n|\Z)", "", text, flags=re.S)

    # generic: evidence-quality/tier hints in subheadings ("- good", "- Tier 1-2")
    text = re.sub(r"\*\*Phage-specific evidence[^*]*\*\*",
                  "**Phage-specific evidence.**", text)
    # that turns a trailing ':' into '.', so re-capitalise what follows
    text = re.sub(r"(\*\*Phage-specific evidence\.\*\*\s+)([a-z])",
                  lambda m: m.group(1) + m.group(2).upper(), text)

    text = deref_sections(text)
    # deref can restate a name already in the sentence: "`phoH` has (`phoH`)"
    text = re.sub(r"(`(\w+)`[^.`]{0,40}?)\s*\(`\2`\)", r"\1", text)

    # safety net: nothing naming a verdict may survive
    leftover = [ln for ln in text.split("\n") if VERDICT_WORDS.search(ln)]
    if leftover:
        raise SystemExit("verdict language survived in %s:\n  %s"
                         % (family, "\n  ".join(leftover)))

    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    text = re.sub(r"\n*-{3,}\s*$", "", text).strip()
    return text


def accession_lines(worksheet, family):
    """Pull '- **K01520** - ...' lines. Verdict rows are never read."""
    for part in re.split(r"^## \d+\. ", worksheet, flags=re.M)[1:]:
        head = part.split("\n", 1)[0]
        name = head.split("`")[1] if "`" in head else head.strip()
        if name != family:
            continue
        accs = [ln for ln in part.split("\n") if ln.startswith("- **K")]
        why = [ln for ln in part.split("\n") if ln.startswith("*Included because")]
        return accs, (why[0] if why else "")
    raise SystemExit("no worksheet section for %s" % family)


TABLE = """| Field | Your answer |
|---|---|
| **VERDICT** — COUNTS / DOES NOT COUNT / UNRESOLVABLE | |
| **Evidence tier** — 1 to 6 | |
| **Confidence** — low / moderate / high | |
| **Resolving experiment** — *required only if UNRESOLVABLE* | |
| **Note** — *optional; only if something surprised you* | |
"""

HEADER = """---
tags: [project, research, adjudication, concordance, active]
---

# Blind Concordance Sheet — 12 judgement families

**This is the only adjudication file left in the vault. That is deliberate.**
The completed worksheet and the evidence dossiers have been moved into the repo so nothing
can leak in while you work.

> [!danger] Don't go looking for the earlier verdicts
> The entire value of this exercise is that you reach your answers without seeing anyone
> else's. Read them first and you are not a second rater, you are an echo — and the
> concordance number becomes worthless with no way for anyone to tell.

## What this is

Twelve families. Every one is a case where evidence **was** found and had to be weighed —
the only places two raters applying the same rule could legitimately diverge. The other 23
families were decided mechanically by the protocol (no Tier 1–5 evidence, so the family
cannot be ruled out, so it stays in), and two raters must agree on those by construction.
Measuring agreement there would inflate the number while testing nothing.

**You are not writing arguments.** This is standard inter-rater practice: apply the rubric,
record the code. Three fields per family, plus a resolving experiment if you say the evidence
can't settle it. **A note is only needed if something surprised you.**

Roughly **4–6 hours**. Two sittings is a good rate. Stop when you're tired — a verdict
written badly at 1am is worse than no verdict.

## The rule, for reference

**Counts as an AMG only if BOTH:** the product acts on a **host** molecule, **and** the
effect is to **sustain or redirect host metabolism** — not to serve a discrete step of the
viral lifecycle (entry, genome protection, replication, assembly, egress).

**Default is COUNTS.** A family only leaves the record on positive Tier 1–5 evidence.
Tier 6 (chemistry alone) can never move a family out by itself — that would restate the
Martin *et al.* argument rather than test it.

**UNRESOLVABLE requires naming the experiment that would settle it.** If you can't name one,
the family is *unresearched*, not unresolvable, and defaults to COUNTS. Keep UNRESOLVABLE for
"the evidence conflicts", never for "there is no evidence".

| Tier | What it looks like |
|---|---|
| **1** | The gene was knocked out of a phage and the effect measured |
| **2** | The **phage's own** protein was purified or structured and its substrate shown |
| **3** | Expression timing across infection (early / middle / late) |
| **4** | The gene sits consistently among structural or replication genes |
| **5** | The phage copy has diverged from host copies in a telling way |
| **6** | Chemistry alone — *"this enzyme does X, so presumably…"* |

> [!note] What was removed from the evidence below, and why
> These extracts are the dossiers minus three things: any passage naming a verdict, my
> "tier available" assessments, and the pre-named resolving experiments. You assign the tier
> yourself, which makes tier agreement a real measurement rather than a copied one.
>
> **The case for HOST and the case for VIRAL are kept in full for every family**, along with
> every citation. Five families needed hand-written edits because a blunt strip took evidence
> with it — `dsrC_tusE`, `nrdH`, `queuosine`, `rfbC`, `glycosyltransferase`. Those edits are
> in `scripts/build_blind_concordance_sheet.py` if you want to audit them.

---

"""


def footer(appendix):
    return """## Appendix A — the nucleotide-sugar and cell-surface literature
%s

---

## When you're done

Tell Claude. Then, and only then:

1. Your verdicts are compared against the first pass — **agreement on all three fields**
2. The four controls are checked (`psbA`/`psbD` → COUNTS, `xtmA`/`xtmB` → DOES NOT COUNT)
3. **The sealed counts are opened** for the first time
4. The disputed share is recomputed under your verdicts, four ways

> [!important] Disagreements are the valuable output, not the failures
> A family where two raters applying the same written rule reach different answers is a
> family where judgement is load-bearing. Those are exactly the ones the paper should
> discuss at length — and you can't find them without this step.

## Related

- [[Adjudication Protocol]] — the rules and why they're shaped that way
- [[How To Adjudicate]] — the longer mechanics
- [[Where We Are]] · [[Project Auxiliary MOC]]
""" % appendix


def main():
    dossiers = read(os.path.join(REPO, "results", "chunk5_evidence_dossiers.md"))
    worksheet = read(os.path.join(REPO, "results", "chunk5_worksheet.md"))
    secs = split_sections(dossiers)

    m = re.search(r"^#{1,3} .*Appendix A.*$", dossiers, flags=re.M)
    if not m:
        raise SystemExit("Appendix A not found - five families cite it")
    nxt = re.search(r"^#{1,2} ", dossiers[m.end():], flags=re.M)
    appendix = dossiers[m.end(): m.end() + (nxt.start() if nxt else len(dossiers))]
    appendix = deref_sections(re.sub(r"\n*-{3,}\s*$", "", appendix.strip()))
    if VERDICT_WORDS.search(appendix):
        raise SystemExit("verdict language in Appendix A")

    chunks, report = [HEADER], []
    for n, fam in enumerate(JUDGEMENT_FAMILIES, 1):
        if fam not in secs:
            raise SystemExit("no dossier section for %s" % fam)
        evidence = strip_leaks(fam, secs[fam])
        accs, why = accession_lines(worksheet, fam)
        report.append((fam, len(evidence), len(accs),
                       "yes" if fam in PRE_EDITS else "-"))

        chunks.append("## %d. `%s`\n\n" % (n, fam))
        chunks.append("\n".join(accs) + "\n\n")
        if why:
            chunks.append(why + "\n\n")
        chunks.append("### Evidence\n\n" + evidence + "\n\n")
        chunks.append("### Your call\n\n" + TABLE + "\n---\n\n")

    chunks.append(footer(appendix))
    out = "".join(chunks)

    dest = os.path.join(VAULT, "Adjudication", "Blind Concordance Sheet.md")
    io.open(dest, "w", encoding="utf-8").write(out)

    print("wrote %s (%d chars)\n" % (dest, len(out)))
    print("%-22s %9s %6s  %s" % ("family", "evidence", "accs", "hand-edited"))
    for fam, ln, na, edited in report:
        print("%-22s %9d %6d  %s" % (fam, ln, na, edited))
    print("\nAppendix A: %d chars" % len(appendix))
    print("verdict words anywhere in sheet:", len(VERDICT_WORDS.findall(out)))


if __name__ == "__main__":
    main()
