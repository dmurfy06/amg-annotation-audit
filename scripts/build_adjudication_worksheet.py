"""
build_adjudication_worksheet.py — CHUNK 5 setup. Freeze the family list and produce the
blinded worksheet Daniel fills in.

WHAT THIS DOES AND DOES NOT DO
    It does NOT adjudicate anything. Verdicts are Daniel's, per 08_adjudication_protocol.md.
    This script only does the mechanical part the protocol specifies:

      1. apply the stated inclusion rule to freeze WHICH families get judged
      2. sort them ALPHABETICALLY, so the high-impact families cannot be judged first and
         anchor everything after
      3. STRIP THE CALL COUNTS, so judging happens blind
      4. emit one worksheet entry per family with the fields the protocol requires

THE INCLUSION RULE, quoted from the protocol (fixed before this script existed):
      1. >=1% of KO-assigned AMG calls AND >=10 calls, in the SAME catalogue
         (Amendment 2 — the bare percentage was degenerate at n=77); OR
      2. named by Martin et al. (2025); OR
      3. designated a positive or negative control.

BLINDING — the point of it
    Daniel already knows dcm is the biggest family. That cannot be unknown, and the protocol
    handles it by declaring those families "protocol-guided but not blind". But he does NOT
    know the counts for the ~40 families that qualified on the 1% rule, and those must stay
    unknown while they are judged. So this worksheet carries NO abundance information at all.

    Counts are written to a SEPARATE file that is not needed until every verdict is closed.

CONTROLS (protocol section "Controls"), adjudicated inside the run, unlabelled:
    positive — psbA, psbD. Canonical experimentally-supported AMGs. MUST come out COUNTS.
    negative — phage terminase large/small subunit. The DNA-packaging motor; there is no
               weaker candidate for "host metabolic modulation" in all of phage biology.
               MUST come out DOES NOT COUNT.
    If either fails, the protocol is broken and gets revised and re-run before any verdict
    is used.

Usage:
    .venv/Scripts/python.exe scripts/build_adjudication_worksheet.py
"""

import csv
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TSV = ROOT / "data" / "harmonised_calls.tsv"
ACC = ROOT / "data" / "family_accessions.tsv"
KEGG = ROOT / "data" / "kegg_ko_list.tsv"
OUT_LIST = ROOT / "data" / "adjudication_families.tsv"
OUT_SHEET = ROOT / "results" / "chunk5_worksheet.md"
OUT_COUNTS = ROOT / "data" / "adjudication_counts_SEALED.tsv"

CATALOGUES = ["ocean_conservative", "soil", "wastewater"]
THRESHOLD = 0.01
# Amendment 2: a percentage threshold means nothing when the denominator cannot support it.
# At n=77 (wastewater) 1% is 0.77 calls, so the bare percentage selected for mere presence
# rather than abundance. Both conditions must now hold in the SAME catalogue.
MIN_CALLS = 10

CONTROLS = {
    "K02703": ("positive", "psbA"),
    "K02706": ("positive", "psbD"),
    "K06909": ("negative", "xtmB"),
    "K07474": ("negative", "xtmA"),
}


def gene_symbol(desc: str) -> str:
    """KEGG descriptions look like 'queD, ptpS, PTS; 6-pyruvoyl...'. Take the first symbol."""
    head = desc.split(";")[0]
    return head.split(",")[0].strip() or "?"


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
    by_cat = defaultdict(list)
    for r in rows:
        by_cat[r["catalogue"]].append(r)

    # --- rule 2: Martin-named families, already frozen in family_accessions.tsv ----------
    martin_ko = {}
    for r in csv.DictReader(ACC.open(encoding="utf-8"), delimiter="\t"):
        if r["status"] != "EXCLUDED" and r["namespace"] == "KO":
            martin_ko[r["accession"]] = r["family"]

    # --- rule 1: any KO at >=1% of KO-assigned calls in any catalogue -------------------
    qualifying = {}
    for cat in CATALOGUES:
        pool = [r for r in by_cat[cat] if r["ko"]]
        if not pool:
            continue
        for ko, n in Counter(r["ko"] for r in pool).items():
            if n / len(pool) >= THRESHOLD and n >= MIN_CALLS:      # Amendment 2: both, same catalogue
                qualifying.setdefault(ko, set()).add(cat)

    # --- assemble adjudication units ----------------------------------------------------
    units = {}
    for ko, fam in martin_ko.items():
        units.setdefault(fam, {"label": fam, "kos": set(), "basis": set(), "control": ""})
        units[fam]["kos"].add(ko)
        units[fam]["basis"].add("named by Martin et al.")
    for ko, cats in qualifying.items():
        if ko in martin_ko:
            units[martin_ko[ko]]["basis"].add(f">=1% and >=10 calls in {', '.join(sorted(cats))}")
            continue
        lab = gene_symbol(ko_name.get(ko, ko))
        units.setdefault(lab, {"label": lab, "kos": set(), "basis": set(), "control": ""})
        units[lab]["kos"].add(ko)
        units[lab]["basis"].add(f">=1% and >=10 calls in {', '.join(sorted(cats))}")
    for ko, (kind, lab) in CONTROLS.items():
        units.setdefault(lab, {"label": lab, "kos": set(), "basis": set(), "control": kind})
        units[lab]["kos"].add(ko)
        units[lab]["basis"].add("control")
        units[lab]["control"] = kind

    ordered = sorted(units.values(), key=lambda u: u["label"].lower())

    # --- frozen list (no counts) --------------------------------------------------------
    with OUT_LIST.open("w", encoding="utf-8", newline="") as fh:
        fh.write("order\tfamily\taccessions\tbasis_for_inclusion\tcontrol\n")
        for i, u in enumerate(ordered, 1):
            fh.write(f"{i}\t{u['label']}\t{','.join(sorted(u['kos']))}\t"
                     f"{'; '.join(sorted(u['basis']))}\t{u['control']}\n")

    # --- sealed counts, NOT to be opened until every verdict is closed ------------------
    with OUT_COUNTS.open("w", encoding="utf-8", newline="") as fh:
        fh.write("family\t" + "\t".join(CATALOGUES) + "\ttotal\n")
        for u in ordered:
            c = {cat: sum(1 for r in by_cat[cat] if r["ko"] in u["kos"]) for cat in CATALOGUES}
            fh.write(f"{u['label']}\t" + "\t".join(str(c[x]) for x in CATALOGUES)
                     + f"\t{sum(c.values())}\n")

    # --- the worksheet ------------------------------------------------------------------
    L = ["# Chunk 5 — Adjudication Worksheet",
         "",
         f"**{len(ordered)} families**, frozen by the rule in `08_adjudication_protocol.md` and "
         "ordered **alphabetically** so the big families cannot anchor the run.",
         "",
         "> [!warning] This worksheet deliberately contains NO call counts.",
         "> Abundance is in `data/adjudication_counts_SEALED.tsv`. **Do not open it until every",
         "> verdict below is written.** Knowing that a family is worth 5,000 calls while deciding",
         "> whether it counts is exactly the bias the protocol exists to prevent.",
         "",
         "## The rule, for reference",
         "",
         "**Counts as an AMG only if BOTH:** the product acts on a **host** molecule, **and** the",
         "effect is to **sustain or redirect host metabolism** — not to serve a discrete step of",
         "the viral lifecycle (entry, genome protection, replication, assembly, egress).",
         "",
         "Default verdict is **COUNTS**. A family only leaves the record on positive Tier 1–5",
         "evidence. Tier 6 (chemistry alone) can never move a family out by itself.",
         "",
         "**UNRESOLVABLE must name the experiment that would resolve it** — otherwise the family",
         "is unresearched, not unresolvable, and defaults to COUNTS.",
         "",
         "---",
         ""]

    for i, u in enumerate(ordered, 1):
        L.append(f"## {i}. `{u['label']}`")
        L.append("")
        for ko in sorted(u["kos"]):
            L.append(f"- **{ko}** — {ko_name.get(ko, '(no KEGG description)')}")
        L.append("")
        L.append(f"*Included because: {'; '.join(sorted(u['basis']))}*")
        L.append("")
        L.append("| | |")
        L.append("|---|---|")
        L.append("| **Part 1 — substrate** | host / viral — *what does the product act on?* |")
        L.append("| **Part 2 — consequence** | sustains host metabolism / discrete lifecycle step |")
        L.append("| **Evidence tier** | 1–6 (see protocol) |")
        L.append("| **Citations** | |")
        L.append("| **VERDICT** | COUNTS / DOES NOT COUNT / UNRESOLVABLE |")
        L.append("| **Confidence** | high / low |")
        L.append("| **If unresolvable — resolving experiment** | |")
        L.append("")
        L.append("**Argument (half a page):**")
        L.append("")
        L.append("")
        L.append("---")
        L.append("")

    OUT_SHEET.parent.mkdir(exist_ok=True)
    OUT_SHEET.write_text("\n".join(L), encoding="utf-8")

    print(f"FROZEN ADJUDICATION LIST — {len(ordered)} families")
    print("=" * 70)
    n_ctrl = sum(1 for u in ordered if u["control"])
    n_martin = sum(1 for u in ordered if any("Martin" in b for b in u["basis"]))
    print(f"  named by Martin et al.        : {n_martin}")
    print(f"  qualified on the >=1% rule    : {len(ordered) - n_martin - n_ctrl}")
    print(f"  controls (pos/neg)            : {n_ctrl}")
    print(f"  total KEGG accessions covered : {sum(len(u['kos']) for u in ordered)}")
    print()
    print("  Alphabetical order, as fixed by the protocol:")
    for i, u in enumerate(ordered, 1):
        tag = f"  [{u['control'].upper()} CONTROL]" if u["control"] else ""
        print(f"    {i:>2}. {u['label']}{tag}")
    print()
    print(f"  worksheet : {OUT_SHEET.relative_to(ROOT)}")
    print(f"  frozen list: {OUT_LIST.relative_to(ROOT)}")
    print(f"  SEALED counts: {OUT_COUNTS.relative_to(ROOT)}  <- do not open until verdicts are done")


if __name__ == "__main__":
    main()
