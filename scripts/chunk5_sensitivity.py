"""Chunk 5 sensitivity: how much of the adjudicated headline rests on any single family?

The strict-rule result for the ocean catalogue is 18.31%, of which `dcm` alone supplies
5,797 of 5,818 excluded calls. A number that concentrated is a number a reviewer will
attack, so it is reported here with the concentration made explicit rather than left for
someone else to find.

Two distinct sensitivities are computed, because they answer different questions:

  VERDICT sensitivity  - the family is held at COUNTS instead of its adjudicated verdict.
                         "What if this verdict is wrong?" Numerator falls, denominator
                         is unchanged.
  PRESENCE sensitivity - the family is dropped from the analysis entirely, from both
                         numerator and denominator. "What does the rest of the record
                         look like without it?"

Leave-one-out is run across all 35 families, not just `dcm`. Restricting it to the family
already known to dominate would only confirm what prompted the check; running it over
everything is what shows whether anything *else* is load-bearing.

Inputs:  data/adjudication_counts_SEALED.tsv  (opened after both pre-registered gates
         passed: 12/12 verdict concordance, all four controls correct)
         verdicts hard-coded below from results/chunk5_worksheet_pass1_completed.md
Output:  results/chunk5_sensitivity.txt
"""

import csv
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SEALED = ROOT / "data" / "adjudication_counts_SEALED.tsv"
OUT = ROOT / "results" / "chunk5_sensitivity.txt"

DATASETS = ["ocean_conservative", "soil", "wastewater"]
LABEL = {"ocean_conservative": "Ocean, curated", "soil": "Soil", "wastewater": "Wastewater"}

# KO-assigned AMG calls per catalogue - the denominators from chunk 2. These are the
# totals the disputed share is a share OF; the sealed file covers only the 35 adjudicated
# families, which is 75.5% of the ocean denominator.
DENOM = {"ocean_conservative": 31772, "soil": 1151, "wastewater": 77}

DOES_NOT_COUNT = ["dcm", "glycoside_hydrolase", "xtmA", "xtmB"]
UNRESOLVABLE = ["dsrC_tusE", "folate", "queuosine"]

# All four DOES NOT COUNT verdicts were recorded at high confidence, which makes the
# confidence-limited rule identical to strict in this run. That is reported, not dropped:
# a pre-registered analysis that turns out degenerate is a result about the run.
HIGH_CONF_DNC = ["dcm", "glycoside_hydrolase", "xtmA", "xtmB"]

RULES = [
    ("Inclusive", []),
    ("Strict", DOES_NOT_COUNT),
    ("Maximally strict", DOES_NOT_COUNT + UNRESOLVABLE),
    ("Confidence-limited", HIGH_CONF_DNC),
]

# Families whose verdict is fixed by the protocol's worked examples rather than produced
# by the adjudication. This matters for `dcm` specifically: it carries 99.6% of the ocean
# strict exclusion, so the ocean strict figure was largely determined when the protocol
# was written, not when the evidence was weighed.
PRE_SPECIFIED = {"dcm", "psbA", "psbD", "xtmA", "xtmB"}


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    """Wilson score interval. Used rather than the normal approximation because the
    wastewater denominator is 77 and soil exclusions run to single figures, where the
    normal interval crosses zero and stops meaning anything."""
    if n <= 0:
        return (0.0, 0.0)
    p = k / n
    d = 1 + z * z / n
    centre = p + z * z / (2 * n)
    margin = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (max(0.0, (centre - margin) / d) * 100, min(1.0, (centre + margin) / d) * 100)


def load_counts() -> dict[str, dict[str, int]]:
    with open(SEALED, encoding="utf-8", newline="") as fh:
        return {
            r["family"]: {ds: int(r[ds]) for ds in DATASETS}
            for r in csv.DictReader(fh, delimiter="\t")
        }


def excluded(counts, families, dataset, hold_as_counts=None, drop=None):
    """Excluded calls and denominator under a rule.

    hold_as_counts - family keeps its calls in the record (verdict sensitivity)
    drop           - family leaves the analysis entirely, numerator and denominator
                     (presence sensitivity)
    """
    fams = [f for f in families if f != hold_as_counts and f != drop]
    k = sum(counts[f][dataset] for f in fams if f in counts)
    n = DENOM[dataset]
    if drop and drop in counts:
        n -= counts[drop][dataset]
    return k, n


def main() -> None:
    counts = load_counts()
    out: list[str] = []

    def w(line: str = "") -> None:
        out.append(line)

    w("CHUNK 5 SENSITIVITY - dependence of the adjudicated headline on single families")
    w("=" * 86)
    w("Seal opened after both pre-registered gates passed:")
    w("  - concordance: 12/12 verdicts, 12/12 confidence, 11/12 tier (one disagreement, `rfbC`)")
    w("  - controls:    psbA/psbD -> COUNTS, xtmA/xtmB/dcm -> DOES NOT COUNT, all correct")
    w()
    w("Verdict tally, 35 families: 28 COUNTS / 4 DOES NOT COUNT / 3 UNRESOLVABLE")
    w()

    # ---- headline -------------------------------------------------------------
    w("=" * 86)
    w("HEADLINE - excluded share of the KO-assigned AMG record, four pre-registered rules")
    w("=" * 86)
    w("%-22s %24s %22s %20s" % ("rule", LABEL["ocean_conservative"], LABEL["soil"],
                                LABEL["wastewater"]))
    w("-" * 92)
    for name, fams in RULES:
        cells = []
        for ds in DATASETS:
            k, n = excluded(counts, fams, ds)
            lo, hi = wilson(k, n)
            cells.append("%6.2f%% [%5.2f-%5.2f] n=%-5d" % (k / n * 100, lo, hi, k))
        w("%-22s %24s %22s %20s" % (name, cells[0], cells[1], cells[2]))
    w()
    w("NOTE: 'Confidence-limited' is identical to 'Strict' because all four DOES NOT COUNT")
    w("verdicts were recorded at high confidence. The rule is degenerate in this run. It is")
    w("reported rather than dropped - it was pre-registered, and its degeneracy is a fact")
    w("about the evidence base, not a reason to hide the row.")
    w()

    # ---- concentration --------------------------------------------------------
    w("=" * 86)
    w("CONCENTRATION - what actually carries each exclusion")
    w("=" * 86)
    for rule_name, fams in [("Strict", DOES_NOT_COUNT),
                            ("Maximally strict", DOES_NOT_COUNT + UNRESOLVABLE)]:
        w()
        w("%s:" % rule_name)
        for ds in DATASETS:
            total = sum(counts[f][ds] for f in fams if f in counts)
            if not total:
                w("  %-20s no calls excluded" % LABEL[ds])
                continue
            parts = sorted(((counts[f][ds], f) for f in fams if f in counts), reverse=True)
            frag = " | ".join("%s %d (%.1f%%)" % (f, c, 100 * c / total)
                              for c, f in parts if c)
            w("  %-20s %d calls: %s" % (LABEL[ds], total, frag))
    w()
    w("The ocean strict result is `dcm` and essentially nothing else. `dcm` is also one of")
    w("the protocol's PRE-SPECIFIED worked examples - its verdict was fixed when the rules")
    w("were written, not when the evidence was weighed. So the ocean strict figure is not")
    w("an output of the adjudication in the way the maximally-strict figure is.")
    w()

    # ---- leave-one-out --------------------------------------------------------
    w("=" * 86)
    w("LEAVE-ONE-OUT - every family, both sensitivities, ocean curated")
    w("=" * 86)
    w("Only families that change a figure are listed; the other 28 move nothing by")
    w("construction, because COUNTS families are never in the numerator.")
    w()

    for rule_name, fams in [("Strict", DOES_NOT_COUNT),
                            ("Maximally strict", DOES_NOT_COUNT + UNRESOLVABLE)]:
        base_k, base_n = excluded(counts, fams, "ocean_conservative")
        base = base_k / base_n * 100
        w("%s - baseline %.2f%%" % (rule_name, base))
        w("  %-22s %10s %10s %10s   %s" % ("family held/dropped", "verdict->", "presence->",
                                           "swing", "pre-specified?"))
        rows = []
        for fam in fams:
            if fam not in counts:
                continue
            vk, vn = excluded(counts, fams, "ocean_conservative", hold_as_counts=fam)
            pk, pn = excluded(counts, fams, "ocean_conservative", drop=fam)
            v = vk / vn * 100 if vn else 0.0
            p = pk / pn * 100 if pn else 0.0
            rows.append((abs(base - v), fam, v, p))
        for swing, fam, v, p in sorted(rows, reverse=True):
            w("  %-22s %9.2f%% %9.2f%% %9.2f pp   %s"
              % (fam, v, p, base - v, "YES" if fam in PRE_SPECIFIED else "-"))
        w()

    # ---- the honest summary ---------------------------------------------------
    w("=" * 86)
    w("WHAT THIS MEANS FOR THE WRITE-UP")
    w("=" * 86)
    k_all, n_all = excluded(counts, DOES_NOT_COUNT, "ocean_conservative")
    k_no, n_no = excluded(counts, DOES_NOT_COUNT, "ocean_conservative", hold_as_counts="dcm")
    w("1. Strict exclusion in the ocean catalogue is 18.31%% with `dcm` and %.2f%% without it."
      % (k_no / n_no * 100))
    w("   The strict rule is, for practical purposes, a statement about one gene family.")
    w()
    w("2. The cross-environment claim survives only under the maximally-strict rule, where")
    w("   `folate` and `queuosine` - both UNRESOLVABLE, both genuinely contested - do the")
    w("   work. That is the defensible headline, and it should be stated as resting on")
    w("   unresolved families rather than on ruled-out ones.")
    w()
    w("3. Wastewater has zero strict exclusion. Its 37.66% maximally-strict figure is")
    w("   entirely `folate` + `queuosine` on a denominator of 77 calls, CI [27.7-48.8].")
    w("   Report the interval every time; the point estimate alone overstates the precision.")
    w()
    w("4. Only 4 of 35 families were ruled out, and 3 of those 4 are protocol controls or")
    w("   near-zero in abundance. The adjudication's main finding is not that the record is")
    w("   full of miscounted families - it is that most families cannot be ruled out on")
    w("   current evidence, and that the disputed mass sits in three unresolvable ones.")

    OUT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(out))


if __name__ == "__main__":
    main()
