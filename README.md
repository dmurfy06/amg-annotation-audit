# Project Auxiliary

**Are viral "auxiliary metabolic genes" auxiliary at all?**

Bacteriophages carry genes resembling host metabolic enzymes. For twenty years the field has
catalogued these as **auxiliary metabolic genes (AMGs)** and read them as evidence that viruses
reprogram host metabolism. A 2025 *Nature Microbiology* Perspective argues that many of the
most-counted categories are doing something **essential for the virus itself** — evading host
restriction enzymes, modifying the viral chromosome, breaking into the cell — and called this
"an epidemic of misannotation".

**They named the suspect gene families. They counted none of them. Nobody has.**

> **The question:** how much of the viral AMG record rests on gene categories the field's own
> experts say should not count?

## Established so far

All figures are **accession-based** (29 KO + 49 Pfam accessions, no text matching), **per gene**.
*strict* = disputed accessions only; *wide* additionally counts the folate/queuosine branch-point
genes (`folE`, `folE2`, `queD`), whose assignment the adjudication must settle.

| Catalogue | Pipeline | namespace | strict | wide |
|---|---|---|---|---|
| **Ocean, curated**, *Microbiome* 2024 | DRAM-v | KO | **22.6%** | **30.2%** |
| Ocean, curated | DRAM-v | Pfam | 7.9% | 11.2% |
| Ocean, **pre-curation** | DRAM-v | KO | 12.7% | 18.0% |
| **Soil**, *ISME J* 2022 | VIBRANT + DRAM-v | Pfam | **21.3%** | **22.9%** |
| Soil | VIBRANT + DRAM-v | KO | 7.5% | 14.8% |
| **Wastewater**, *ES&T* 2023 | custom hmmer | KO | **19.5%** | **37.7%** |

**Every route gives a substantial disputed share — 7.4% to 37.7%.** Three further results:

1. **The wastewater number validated itself.** 19.5% by accession against 19.8% derived
   independently by reading the paper's prose. Two unrelated methods, a third of a point apart.
2. **Curation makes it worse.** Ocean KO, per gene: **12.7% → 22.6%**. Curation nearly doubles
   the disputed share, non-overlapping intervals.
3. **The namespace effect reverses.** Ocean is KO-high/Pfam-low; **soil is the mirror image.**
   So it is not that one identifier system inflates the count — different environments carry
   different disputed families, each cleanly visible in a different system. Not in Martin *et al.*

**One judgement moves the headline 18 points:** wastewater runs 19.5% → 37.7% purely on whether
`folE`/`queD` count. That is why the adjudication is the project.

## Start here

| File | What it is |
|---|---|
| **`06_project_brief.md`** | **The plan. Read this first.** Question, pre-registered rubric, hypotheses, analysis steps, limitations |
| `07_flag_semantics.md` | Chunk 1 result. What DRAM-v's flags mean, and why the `F`-flag worry was backwards |
| **`08_adjudication_protocol.md`** | **The rules for judging gene families, fixed before any was judged.** Read before Chunk 5 |
| `09_chunk2_harmonisation.md` | Chunk 2. One schema, deduplication, and a defect found in the frozen rubric |
| `10_chunk4_own_criteria.md` | Chunk 4. Each paper against its own stated rule — and why H4 failed |
| `05_redteam.md` | Every objection to the project and its answer. 7 attacks: 3 fail, 3 land, 1 standing risk |
| `04_feasibility.md` | Compute, data, skills, timeline. The binding constraint is not compute |
| `03_novelty_audit.md` | Why 15 other candidates died, with the citation that killed each |
| `02b_candidates.md` | The second candidate round, from which this project came |
| `01_landscape.md`, `02_candidates.md` | The original landscape scan and candidate list |

## Setup — start here if you have just cloned this

No third-party data is committed to this repository. Fetch it:

```bash
python -m venv .venv && .venv/Scripts/python.exe -m pip install pypdf openpyxl
```

```bash
.venv/Scripts/python.exe scripts/fetch_reference_data.py
```

That retrieves the KEGG orthology list, both tools' AMG definition files, and the DRAM/VIBRANT
source and wiki — **pinned to the exact commits cited by line number in `07_flag_semantics.md`**,
so those citations cannot drift.

**What is deliberately not fetched:** the three published AMG catalogues. They are large
publisher-hosted supplements; DOIs are in `06_project_brief.md`. The ocean one
(`GlobalAMGs_SOM.xlsx`, 114 MB, Zenodo 10.5281/zenodo.12668289) is needed to reproduce the
headline numbers.

> **Why nothing is vendored.** KEGG data is © Kanehisa Laboratories — free to query
> academically, **not** free to redistribute. DRAM and VIBRANT are GPL-3.0 and belong to their
> authors. Fetching on demand keeps the analysis reproducible without republishing anyone
> else's work.

## Layout

```
scripts/    analysis code — run with .venv/Scripts/python.exe
results/    script outputs, kept as the record of each chunk
data/       fetched datasets — gitignored, see Setup
refs/       fetched tool source + papers extracted to text — gitignored
sources/    original PDFs and supplementary workbooks as supplied — gitignored
.venv/      Python 3.13 + pypdf + openpyxl
```

### The scripts that matter

| Script | Does |
|---|---|
| `amg_database_audit.py` | Audits VIBRANT and DRAM AMG definitions against the rubric |
| `amg_record_composition.py` | Measures the disputed share in the ocean catalogue |
| `dramv_flag_semantics.py` | Establishes DRAM-v flag meanings and tests `F` against a baseline |
| `fetch_reference_data.py` | Re-downloads all third-party data, pinned to cited commits |
| `harmonise_catalogues.py` | Chunk 2: one schema across catalogues; classifies duplicates |
| `chunk2_namespace_matching.py` | Applies the rubric per namespace, showing every string matched |
| `pdf_to_text.py` | PDF → text with page markers, so quotes can be cited by page |
| `check_retraction_feasibility.py` | The pattern for testing whether data exists before designing anything |

Run anything with:

```bash
.venv/Scripts/python.exe scripts/amg_database_audit.py
```

## Notes, learning and progress live in Obsidian

This folder is the **work**. Understanding, decisions and progress live in the vault:

```
C:\Users\danie\OneDrive\Documente\Obsidian Vault\1 Projects\Research Project 2026\
```

Start at **Project Auxiliary MOC**. The split is deliberate — if something only makes sense
while looking at code it belongs here; if it should still make sense in a year, it belongs there.

## Next action

**Chunk 5 — the adjudication.** Everything upstream is done and it is now the only thing
standing between the project and a write-up. Rules are fixed in
`08_adjudication_protocol.md`; the frozen family list is `data/family_accessions.tsv`.

Chunks 1, 2, 3 and 4 are complete — `07_`, `09_`, `08_`, `10_`.

> **Carried forward:** the H1 pre-registration in `06_project_brief.md` is **spent** and all
> catalogue measurements are exploratory. **H4 failed** in the form it was written — see
> `10_chunk4_own_criteria.md`. Every disputed-share figure is accession-based per Amendment 1;
> earlier text-matched numbers are void.

## House rules, each bought with a dead candidate

1. Search the citing literature before ranking anything.
2. Verify the data exists in the shape the question needs, before designing.
3. If a short script answers the whole question in one sitting, that is a figure — the project is
   the question the figure raises.
4. Read the figures, not the abstract.
5. **Suspect your own best result — and your worst.** Five numbers here have been artefacts:
   an "83-fold" difference, a "47.5%" share, a false "UNSAFE" verdict, a "68% F-flagged" worry
   with no baseline, and a "3.4%" soil share from a rubric that could not spell Pfam. They run
   in **both** directions — over-claiming and over-killing — so "it looks too good" is only half
   the trigger. The other half is *compared to what?*
6. **Never trust a pattern you have not watched match real strings.** Print what it matched.
   Free-text matching fails silently in three ways: over-match, under-match, and leakage
   between categories.
