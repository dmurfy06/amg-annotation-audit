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

---

# THE NUMBERS, recomputed against the frozen accession list

**These supersede every earlier figure in the project.** Script: `chunk2_final_shares.py`.
Rubric: **29 KO + 49 Pfam accessions**, 6 flagged AMBIGUOUS. No text is matched anywhere.

*strict* = INCLUDED accessions only · *wide* = INCLUDED + AMBIGUOUS (the folate/queuosine
branch point: `folE`, `folE2`, `queD`). **Per gene**, since rows over-count multi-domain proteins.

| Catalogue | namespace | n genes | strict | wide |
|---|---|---|---|---|
| **Ocean, curated** | KO | 29,973 | **22.63%** [22.16–23.10] | **30.19%** [29.67–30.71] |
| Ocean, curated | Pfam | 83,987 | 7.94% [7.76–8.13] | 11.21% [11.00–11.43] |
| Ocean, pre-curation | KO | 87,602 | 12.69% [12.47–12.91] | 18.02% [17.77–18.28] |
| Ocean, pre-curation | Pfam | 235,379 | 17.24% [17.09–17.40] | 19.67% [19.51–19.83] |
| **Soil** | Pfam | 3,226 | **21.26%** [19.89–22.71] | **22.94%** [21.52–24.42] |
| Soil | KO | 698 | 7.45% [5.73–9.64] | 14.76% [12.32–17.58] |
| **Wastewater** | KO | 77 | **19.48%** [12.18–29.69] | **37.66%** [27.67–48.83] |
| Wastewater | Pfam | 32 | 15.62% [6.86–31.75] | 37.50% [22.93–54.75] |

## Four things the recomputation establishes

**1. The wastewater result validates independently.** The accession route gives **19.48%**; the
figure derived from the paper's prose was **19.8%**. Two entirely independent methods — one
reading a sentence, one intersecting accession sets — agree to within a third of a percentage
point. Nothing forced that.

**2. H2 survives and strengthens. Curation still makes it worse.** Ocean, KO, per gene:
**12.69% → 22.63%** from permissive to curated, strict rubric. The disputed share **nearly
doubles** under curation. Non-overlapping intervals. This was the project's most interesting
claim and it holds under a method that had no way to know what answer was wanted.

**3. The namespace effect is real but it is not a bias — it reverses.**

| | via KO | via Pfam |
|---|---|---|
| Ocean, curated | **22.63%** | 7.94% |
| Soil | 7.45% | **21.26%** |

Ocean is KO-high and Pfam-low; **soil is the exact mirror image.** So this is not "one namespace
inflates the count". It is that **different environments carry different disputed families, and
those families are visible in different identifier systems** — ocean's disputed content is `dcm`
(cleanly KEGG-annotated), soil's is glycosyltransferases (cleanly Pfam-annotated).

That is a sharper and more defensible claim than the earlier version, and it is still not in
Martin *et al.*

**4. The ambiguous set is the single biggest lever, and it is exactly what Chunk 5 must decide.**
Wastewater moves **19.48% → 37.66%** on whether `folE`/`queD` count. That one biochemical
judgement — is GTP cyclohydrolase I doing folate work or queuosine work in a phage? — moves the
headline by 18 percentage points. It cannot be settled by counting, and pretending otherwise is
what the old regex was doing silently.

**Range across everything tested: 7.4% to 37.7%.** Every route still shows a substantial
disputed share. But the honest headline is a matrix, and the adjudication is now visibly
load-bearing rather than decorative.

---

## Wastewater — obtained 2026-08-05

Daniel fetched **Dataset S4** of the ES&T Supporting Information through a browser (ACS returns
HTTP 403 to automated download; the data was free the whole time, only the robot was blocked).

**101 vAMG calls**, matching the paper's stated figure exactly, carrying **both** a kofamscan KO
(76.2%) and an hmmsearch Pfam accession (31.7%). The paper's own *text* carries zero KO
accessions, which is why 19.8% could only ever be derived from prose before this table arrived.

**The hard gate in `06_project_brief.md` is now passed for all three catalogues.**

## A note on Pfam identifiers, which nearly broke the recomputation

Soil publishes Pfam **short names** (`Glyco_trans_1_2`), not accessions — 0 of 4,583 rows carried
a `PF#####`. Matching by accession therefore returned **0.00%** for soil on the first run.

The wrong fix would have been to match soil's Pfam *descriptions* against the list, which
reintroduces text matching through the back door. The right fix was to resolve names to
accessions through **Pfam's own mapping** (`Pfam-A.clans.tsv`, 30,134 families), which now
resolves **98.9%** of soil rows. The remaining 52 are families renamed or retired upstream.

Worth recording as a general point: *"it carries Pfam"* is not one thing. A catalogue may publish
accessions, short names, or descriptions, and only the first is stable.

## Where this leaves the numbers

Nothing here overturns the project — every route tested still shows a substantial disputed share,
**7.4% to 37.7%**. What changed is that **no single number can carry the result.** Three choices
must be declared every time: namespace (KO / Pfam), unit (call / gene), and whether the
ambiguous branch-point genes count.

Less quotable. Considerably harder to attack. And the adjudication is now visibly load-bearing —
one biochemical judgement about `folE` moves the wastewater headline by 18 points.
