"""Build the four preprint figures.

Figures 1, 2 and 4 are computed from the sealed counts and the adjudication record so they
cannot drift from the numbers in the text. Figure 3 takes the three published-claim results
from chunk 7; each value is annotated with its source.

Output: manuscript/figures/fig{1..4}_*.{png,pdf}
"""

import csv
import math
import re
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

ROOT = Path(__file__).resolve().parent.parent
FIGDIR = ROOT / "manuscript" / "figures"
FIGDIR.mkdir(parents=True, exist_ok=True)

# Okabe-Ito: colourblind-safe, prints legibly in greyscale.
INK = "#22222a"
GREY = "#8a8a94"
BLUE = "#0072B2"
ORANGE = "#E69F00"
RED = "#D55E00"
GREEN = "#009E73"
LIGHT = "#dcdce4"

plt.rcParams.update({
    "figure.dpi": 150, "savefig.dpi": 300, "savefig.bbox": "tight",
    "font.size": 9, "axes.labelsize": 9.5, "axes.titlesize": 10.5,
    "axes.edgecolor": INK, "axes.labelcolor": INK, "text.color": INK,
    "xtick.color": INK, "ytick.color": INK, "axes.spines.top": False,
    "axes.spines.right": False, "axes.axisbelow": True,
})

DATASETS = ["ocean_conservative", "soil", "wastewater"]
LABEL = {"ocean_conservative": "Ocean\n(curated)", "soil": "Soil", "wastewater": "Wastewater"}
DENOM = {"ocean_conservative": 31772, "soil": 1151, "wastewater": 77}
DNC = ["dcm", "glycoside_hydrolase", "xtmA", "xtmB"]
UNRES = ["dsrC_tusE", "folate", "queuosine"]


def wilson(k, n, z=1.96):
    if n <= 0:
        return (0.0, 0.0)
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    m = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (max(0.0, (c - m) / d) * 100, min(1.0, (c + m) / d) * 100)


def counts():
    with open(ROOT / "data" / "adjudication_counts_SEALED.tsv", encoding="utf-8",
              newline="") as fh:
        return {r["family"]: {d: int(r[d]) for d in DATASETS}
                for r in csv.DictReader(fh, delimiter="\t")}


def excluded(cts, fams, ds, hold=None):
    k = sum(cts[f][ds] for f in fams if f in cts and f != hold)
    return k, DENOM[ds]


def save(fig, name):
    for ext in ("png", "pdf"):
        fig.savefig(FIGDIR / f"{name}.{ext}")
    plt.close(fig)
    print("  wrote", name)


# ---------------------------------------------------------------- figure 1
def fig1(cts):
    """The four-rule spread. The point is the SPREAD, not any single bar."""
    rules = [("Inclusive", []), ("Strict", DNC), ("Maximally strict", DNC + UNRES)]
    fig, ax = plt.subplots(figsize=(6.6, 3.5))
    width, gap = 0.26, 0.02
    colours = [LIGHT, ORANGE, RED]
    for i, (rname, fams) in enumerate(rules):
        xs, ys, los, his = [], [], [], []
        for j, ds in enumerate(DATASETS):
            k, n = excluded(cts, fams, ds)
            pct = 100 * k / n
            lo, hi = wilson(k, n)
            xs.append(j + (i - 1) * (width + gap))
            ys.append(pct)
            los.append(max(0, pct - lo))
            his.append(max(0, hi - pct))
        ax.bar(xs, ys, width, label=rname, color=colours[i],
               edgecolor=INK, linewidth=0.6, zorder=3)
        ax.errorbar(xs, ys, yerr=[los, his], fmt="none", ecolor=INK,
                    elinewidth=0.9, capsize=2.5, zorder=4)
        # label above the upper interval, not the bar, so the two never collide
        for x, y, h in zip(xs, ys, his):
            if y > 0.4:
                ax.text(x, y + h + 1.1, f"{y:.1f}", ha="center", fontsize=7.5, color=INK)
    ax.set_xticks(range(len(DATASETS)))
    ax.set_xticklabels([LABEL[d] for d in DATASETS])
    ax.set_ylabel("AMG record excluded (%)")
    ax.set_title("Excluded share depends on which pre-registered rule is applied",
                 loc="left", pad=9)
    ax.set_ylim(0, 56)
    ax.grid(axis="y", color=LIGHT, linewidth=0.7, zorder=0)
    ax.legend(frameon=False, ncol=3, loc="upper left", bbox_to_anchor=(0, 1.0), fontsize=8)
    ax.text(0, -0.30, "Wilson 95% intervals. The confidence-limited rule is identical to "
                      "strict (all four\nDOES NOT COUNT verdicts were high confidence) and "
                      "is not plotted separately.",
            transform=ax.transAxes, fontsize=7, color=GREY, va="top")
    save(fig, "fig1_four_rule_spread")


# ---------------------------------------------------------------- figure 2
def fig2(cts):
    """Leave-one-out. This figure exists to show a fragility, not to hide it."""
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.4), layout="constrained")
    panels = [("Strict", DNC, axes[0]), ("Maximally strict", DNC + UNRES, axes[1])]
    for rname, fams, ax in panels:
        base_k, base_n = excluded(cts, fams, "ocean_conservative")
        base = 100 * base_k / base_n
        rows = []
        for f in fams:
            if f not in cts:
                continue
            k, n = excluded(cts, fams, "ocean_conservative", hold=f)
            rows.append((100 * k / n, f))
        rows.sort()
        ys = range(len(rows))
        cols = [RED if f == "dcm" else BLUE for _, f in rows]
        ax.barh(list(ys), [v for v, _ in rows], color=cols, edgecolor=INK,
                linewidth=0.6, height=0.62, zorder=3)
        ax.axvline(base, color=INK, linestyle="--", linewidth=1.1, zorder=4)
        # baseline annotation sits at the BOTTOM, clear of the panel title, and to the
        # LEFT of the line so the dashes never cut through the text
        ax.text(base - base * 0.02, -0.85, f"baseline {base:.2f}%", fontsize=7.5,
                color=INK, ha="right", va="center")
        ax.set_yticks(list(ys))
        ax.set_yticklabels([f for _, f in rows], fontsize=8)
        for i, (v, _) in enumerate(rows):
            ax.text(v + base * 0.02, i, f"{v:.2f}%", va="center", fontsize=7.5, color=INK)
        ax.set_xlim(0, base * 1.34)
        ax.set_ylim(-1.4, len(rows) - 0.4)
        ax.set_xlabel("Ocean excluded share (%)")
        ax.set_title(rname, loc="left", fontsize=9.5)
        ax.grid(axis="x", color=LIGHT, linewidth=0.7, zorder=0)
    fig.suptitle("One family carries the strict result; the maximally-strict result is "
                 "distributed", x=0.01, ha="left", fontsize=10.5)
    fig.text(0.01, -0.06, "Each bar is the ocean excluded share when that family alone is "
                          "held at COUNTS. Removing `dcm` collapses the strict result from "
                          "18.31% to 0.07%; `dcm` is also a protocol worked example, so its "
                          "verdict was fixed before evidence was weighed (§3.4).",
             fontsize=7, color=GREY, va="top", wrap=True)
    save(fig, "fig2_leave_one_out")


# ---------------------------------------------------------------- figure 3
def fig3():
    """The paper's key figure: what happens to three published claims.

    Values from results/chunk7_downstream_claims.txt.
    """
    fig, axes = plt.subplots(1, 3, figsize=(9.0, 3.5), layout="constrained")
    stages = ["As\npublished", "Strict", "Maximally\nstrict"]

    # -- wastewater: vAMGs remaining, and the specific genes the abstract names
    ax = axes[0]
    total = [101, 101, 72]
    named = [27, 27, 0]          # queuosine-pathway genes the abstract names as most common
    ax.bar(range(3), total, color=LIGHT, edgecolor=INK, linewidth=0.6, zorder=3,
           label="other vAMGs")
    ax.bar(range(3), named, color=RED, edgecolor=INK, linewidth=0.6, zorder=4,
           label="genes named in\nthe abstract")
    for i, (t, nm) in enumerate(zip(total, named)):
        ax.text(i, t + 3, str(t), ha="center", fontsize=8)
    ax.set_ylim(0, 152)          # headroom so the legend never sits on a bar
    ax.set_title("Wastewater — destroyed", loc="left", color=RED, fontsize=9.5)
    ax.set_ylabel("vAMGs in the catalogue")
    ax.legend(frameon=False, fontsize=6.8, loc="upper center", ncol=1,
              handlelength=1.2, borderpad=0.2, labelspacing=0.3)

    # -- ocean: prevalence claim
    ax = axes[1]
    vals = [19.0, 17.4, 16.9]
    ax.bar(range(3), vals, color=[LIGHT, ORANGE, ORANGE], edgecolor=INK,
           linewidth=0.6, zorder=3)
    for i, v in enumerate(vals):
        ax.text(i, v + 0.45, f"{v:.1f}%", ha="center", fontsize=8)
    ax.set_ylim(0, 24)
    ax.set_title("Ocean — moves ~11%", loc="left", color=ORANGE, fontsize=9.5)
    ax.set_ylabel("Virus populations carrying an AMG (%)")

    # -- soil: comparative claim
    ax = axes[2]
    abund = [1.25, 1.25, 1.25]
    rich = [2.54, 2.54, 2.55]
    w = 0.36
    ax.bar([i - w / 2 for i in range(3)], abund, w, color=GREEN, edgecolor=INK,
           linewidth=0.6, zorder=3, label="abundance")
    ax.bar([i + w / 2 for i in range(3)], rich, w, color=BLUE, edgecolor=INK,
           linewidth=0.6, zorder=3, label="richness")
    for i in range(3):
        ax.text(i - w / 2, abund[i] + 0.06, f"{abund[i]:.2f}", ha="center", fontsize=7.5)
        ax.text(i + w / 2, rich[i] + 0.06, f"{rich[i]:.2f}", ha="center", fontsize=7.5)
    ax.axhline(1.0, color=GREY, linewidth=0.8, linestyle=":")
    ax.set_ylim(0, 3.3)
    ax.set_title("Soil — untouched", loc="left", color=GREEN, fontsize=9.5)
    ax.set_ylabel("Heavy / Clean ratio")
    ax.legend(frameon=False, fontsize=7, loc="upper right")

    for ax in axes:
        ax.set_xticks(range(3))
        ax.set_xticklabels(stages, fontsize=7.5)
        ax.grid(axis="y", color=LIGHT, linewidth=0.7, zorder=0)
    fig.suptitle("Disputed families cancel in comparisons and persist in descriptions",
                 x=0.01, ha="left", fontsize=10.5)
    fig.text(0.01, -0.05, "One claim from each catalogue's own abstract, all three fixed "
                          "before any was recomputed. The wastewater claim names the "
                          "queuosine genes as the most common vAMGs; those genes are the "
                          "disputed family, so the claim's subject and the contested set are "
                          "the same object.",
             fontsize=7, color=GREY, va="top", wrap=True)
    save(fig, "fig3_published_claims")


# ---------------------------------------------------------------- figure 4
def fig4():
    """Evidence tier across all 35 families, split by verdict."""
    text = (ROOT / "results" / "chunk5_worksheet_pass1_completed.md").read_text(
        encoding="utf-8")
    fams = []
    for b in re.split(r"\n##\s+", text):
        m = re.search(r"`(\w+)`", b.split("\n")[0])
        if not m:
            continue
        t = re.search(r"\*\*Evidence tier\*\*\s*\|([^|\n]*)", b)
        v = re.search(r"\*\*VERDICT\*\*\s*\|([^|\n]*)", b)
        if not (t and v):
            continue
        # best (lowest-numbered = strongest) tier, ignoring parenthetical commentary
        head = re.split(r"[(;]", t.group(1).replace("*", ""))[0]
        nums = [int(n) for n in re.findall(r"\d", head)]
        verdict = re.sub(r"[*\s]+", " ", v.group(1)).strip().upper()
        if nums:
            fams.append((min(nums), verdict))
    order = ["COUNTS", "UNRESOLVABLE", "DOES NOT COUNT"]
    cmap = {"COUNTS": LIGHT, "UNRESOLVABLE": ORANGE, "DOES NOT COUNT": RED}
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    tiers = [1, 2, 3, 4, 5, 6]
    bottom = [0] * len(tiers)
    for verdict in order:
        vals = [sum(1 for t, v in fams if t == tier and v == verdict) for tier in tiers]
        ax.bar(tiers, vals, bottom=bottom, color=cmap[verdict], edgecolor=INK,
               linewidth=0.6, zorder=3, label=verdict.title())
        bottom = [b + v for b, v in zip(bottom, vals)]
    for tier, tot in zip(tiers, bottom):
        if tot:
            ax.text(tier, tot + 0.25, str(tot), ha="center", fontsize=8)
    ax.set_xticks(tiers)
    ax.set_xticklabels(["1\nknockout", "2\npurified", "3\ntiming", "4\ncontext",
                        "5\ndivergence", "6\nchemistry\nonly"], fontsize=7.5)
    ax.set_xlabel("Highest tier of phage-specific evidence found")
    ax.set_ylabel("Gene families")
    ax.set_ylim(0, max(bottom) + 2.6)
    ax.yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(integer=True))  # counts
    ax.set_title("Half the adjudicated families rest on chemical plausibility alone",
                 loc="left", pad=9)
    ax.grid(axis="y", color=LIGHT, linewidth=0.7, zorder=0)
    ax.legend(frameon=False, fontsize=8, loc="upper left")
    ax.text(0, -0.34, "Tier 6 alone can never rule a family out under the protocol, so these "
                      "17 families default to\ncounting. Eight of the 35 have no "
                      "phage-specific evidence of any kind (§3.3).",
            transform=ax.transAxes, fontsize=7, color=GREY, va="top")
    save(fig, "fig4_evidence_tiers")
    return fams


if __name__ == "__main__":
    cts = counts()
    print("building figures ->", FIGDIR)
    fig1(cts)
    fig2(cts)
    fig3()
    fams = fig4()
    print("families plotted in fig4:", len(fams))
