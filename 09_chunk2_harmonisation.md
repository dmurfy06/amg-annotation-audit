# 09 — Harmonisation, deduplication, and a defect in the frozen rubric (Chunk 2)

**Run 2026-08-05.** Scripts: `harmonise_catalogues.py`, `chunk2_dedup_impact.py`,
`chunk2_namespace_matching.py`, `inspect_catalogues.py`.
Outputs: `results/chunk2_*.txt`. Harmonised table: `data/harmonised_calls.tsv` (regenerable).

---

## What was built

One row per AMG call, 13 columns, **349,171 rows** across ocean (permissive + conservative) and
soil. The schema separates two things the original analysis conflated:

| Column | Why it is its own column |
|---|---|
| `description` | the catalogue's own gene description — **KEGG-derived** in DRAM-v output |
| `pfam_text` | **Pfam's own wording**, which is different |

Matching `description` and calling the result a Pfam measurement produces a KEGG answer wearing
a Pfam label. That mistake was made and caught during this chunk.

## Duplicates — measured, then classified

| Catalogue | dup gene_ids | surplus rows | share of table | conflicting KOs |
|---|---|---|---|---|
| Ocean conservative | 1,451 | 1,810 | **2.04%** | **0** |
| Soil | 822 | 1,306 | **28.50%** | **0** |

The red team's "~1,800 duplicates" is confirmed at 1,810. **No gene anywhere carries conflicting
KO assignments**, so deduplication cannot change which family a gene belongs to — only how many
times it is counted.

Soil is the problem: **28.5% of its rows are repeat genes**, because a multi-domain protein
legitimately gets one row per Pfam domain. Counting rows counts domains, not genes.

### Deduplication moves the soil headline, and it moves it down

| | per row | per distinct gene | shift |
|---|---|---|---|
| Ocean conservative (KO) | 25.08% [24.61–25.56] | **26.59%** [26.09–27.09] | +1.5 pts |
| **Soil (Pfam)** | 30.26% [28.95–31.61] | **22.67%** [21.27–24.14] | **−7.6 pts** |

A gene counts as disputed if *any* of its rows is, so collapsing can only lower a proportion.
**The published-style soil figure of ~29.8% is a per-domain count. Per gene it is 22.7%.**
Both must be reported, and which one is "the" answer is a decision, not a fact.

---

## THE DEFECT — the frozen rubric silently under-matches outside KEGG

The rubric was written as regexes against **KEGG's wording**. Pfam spells the same biology
differently, and a regex that finds nothing raises no error:

| Family | KEGG says | Pfam says | frozen pattern finds |
|---|---|---|---|
| glycosyltransferase | `glycosyltransferase` | **`Glycosyl transferases group 1`** | 83 of 1,238 |
| `dcm` | `DNA (cytosine-5-)-methyltransferase` | **`C-5 cytosine-specific DNA methylase`** | 0 of 5,277 |

Applying the frozen patterns literally:

| | frozen patterns | corrected per-namespace | |
|---|---|---|---|
| **Soil (Pfam)** | **3.38%** | **30.26%** | 9× under-count |
| Ocean (Pfam) | 1.55% | 11.00% | 7× under-count |
| Ocean (KO) | 25.08% | 25.08% | unaffected — KEGG is what it was written for |

> [!warning] The recorded soil result was not reproducible from the repository
> The published-style figure (29.8%, "glycosyltransferases 1,238") reproduces **exactly** —
> 1,238 — but only with a space-tolerant pattern that **is not the one in the frozen script**,
> and **no soil script was ever committed**. The discrepancy was undetectable until the
> catalogues were harmonised.
>
> The number was never wrong. Its provenance was missing, which for an audit project is the
> more serious failure. Every figure now has a committed script behind it.

**Note the direction.** These corrections *raise* the disputed share — they favour this
project's own hypothesis. That is exactly why the defect, the correction, and both numbers are
reported together rather than the better number quietly replacing the worse one.

The old **47.5% lesson still holds and is not undone**: matching bare `GT\d+`/`GH\d+` against the
CAZy column wrongly caught "NAD dependent epimerase/dehydratase" (268 rows) and "short chain
dehydrogenase" (117). Those stay excluded. One source per category.

---

## The finding this produced, and it is better than the correction

**The same catalogue, measured in two namespaces, gives two different answers:**

| Ocean conservative, one table | rows carrying it | disputed share |
|---|---|---|
| via **KEGG KO** | 31,772 (35.8%) | **25.08%** [24.61–25.56] |
| via **Pfam** | 85,768 (96.7%) | **11.00%** [10.79–11.21] |

Same genes. Same rubric. Same environment, same tool, same paper. **A 2.3-fold difference purely
from which identifier system you count in** — and the Pfam route covers **2.7× more of the
record**, so the more-cited number rests on the smaller denominator.

This is much stronger than the previous version of the namespace claim, which compared *different
catalogues* and could always be attributed to environment or pipeline. Measured **within one
table**, those explanations are gone.

The composition differs too, and revealingly:

| Family | via KO | via Pfam |
|---|---|---|
| `dcm` | 5,797 | 5,381 |
| queuosine | 2,156 | 1,304 |
| **folate / one-carbon** | **3** | **2,721** |

---

## The problem this exposes, which Chunk 2 cannot solve on its own

That folate row is not a bug to be patched. It is a **biological ambiguity the counting method
cannot resolve**:

- **`folE` / GTP cyclohydrolase I** (1,369 Pfam hits) is the first step of folate biosynthesis
  **and** the first step of queuosine biosynthesis. The wastewater paper calls it a queuosine
  gene. KEGG's description says neither "folate" nor "que", so the KO route misses it entirely.
- **`queD` / 6-pyruvoyl tetrahydropterin synthase** (1,336 Pfam hits) is a queuosine gene, but
  its Pfam description contains "pterin", so a folate pattern catches it.

So **which family a gene belongs to is a biological judgement**, and it changes the answer by
thousands of calls. That judgement is exactly what Chunk 5 exists to make.

> [!important] Chunks 2 and 5 are entangled, and the plan did not anticipate it
> The counting cannot be finalised before the adjudication, because the counting depends on
> family-membership decisions the adjudication is supposed to make. Pretending otherwise means
> the regex quietly makes those decisions instead — which is how folE ended up counted as folate
> in one namespace and nothing at all in the other.

### The fix, proposed — and it needs Daniel's sign-off

**Stop matching free text. Define each family as an explicit list of KO and Pfam accessions.**

Regex-on-description has now failed in **three distinct ways in one sitting**:

1. **over-matching** — CAZy codes catching dehydrogenases (the old 47.5%)
2. **under-matching** — Pfam spelling (`Glycosyl transferases`, `methylase`)
3. **cross-family leakage** — `pterin` pulling a queuosine gene into folate

Accessions have none of these failure modes: `K00558` and `PF00145` are stable, unambiguous, and
mean the same thing to everyone. The lists become part of the frozen rubric, auditable line by
line, and a reviewer can check membership without rerunning anything.

**This is a change to how the pre-registered rubric is applied, so it must be an appended,
dated amendment to `08_adjudication_protocol.md` — not a silent edit.** The families themselves
do not change; only how membership is determined.

---

## Wastewater — still outstanding, and now precisely specified

No per-gene table in `sources/`. The paper's text carries **zero KO accessions**, confirming the
19.8% came from prose naming `folE`/`queD`/`queE`, not identifiers.

**The data exists.** The SI listing includes a dataset *"functional annotation of vAMGs"*,
"available free of charge" at <https://pubs.acs.org/doi/10.1021/acs.est.2c07800>. ACS returns
**HTTP 403** to automated download, so it needs fetching through a browser — same route as the
paper PDF.

Until then the cross-catalogue claim rests on two catalogues with per-gene data, not three.

## Where this leaves the numbers

Nothing here overturns the project. The disputed share is still substantial on every route
tested — 11% to 30% depending on namespace and denominator. But **"25.1%" can no longer be
reported as a single figure.** The honest statement is a matrix over three choices, each of which
must be declared: namespace (KO / Pfam), unit (call / gene), and family membership (pending
adjudication).

That is a less quotable result and a more defensible one.
