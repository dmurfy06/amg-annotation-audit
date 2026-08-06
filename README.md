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

| Catalogue | Environment | Pipeline | Disputed share | Dominated by |
|---|---|---|---|---|
| Ocean, *Microbiome* 2024 | marine | DRAM-v | **25.1%** of KO-assigned calls | `dcm` 5,797 · queuosine 2,156 |
| *(same table, via Pfam)* | marine | DRAM-v | **11.0%** of Pfam-assigned calls | `dcm` 5,381 · folate 2,721 |
| Wastewater, *ES&T* 2023 | activated sludge | custom hmmer/kofamscan | **19.8%** (20/101) | queuosine, `folE` |
| Soil, *ISME J* 2022 | contaminated soil | VIBRANT + DRAM-v | **29.8%** (1,365/4,583) | glycosyltransferases 1,238 |

Three environments, three independent pipelines, all 20–30%. Plus: **curation raises the
disputed share** (13.4% → 25.1%), and **the composition is annotation-namespace dependent**.

## Start here

| File | What it is |
|---|---|
| **`06_project_brief.md`** | **The plan. Read this first.** Question, pre-registered rubric, hypotheses, analysis steps, limitations |
| `07_flag_semantics.md` | Chunk 1 result. What DRAM-v's flags mean, and why the `F`-flag worry was backwards |
| **`08_adjudication_protocol.md`** | **The rules for judging gene families, fixed before any was judged.** Read before Chunk 5 |
| `09_chunk2_harmonisation.md` | Chunk 2. One schema, deduplication, and a defect found in the frozen rubric |
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

**A decision, then Chunk 4.** Chunk 2 found the frozen rubric under-matches badly outside
KEGG (soil: 3.4% literal vs 30.3% corrected) and that family membership is a biological
judgement the regexes were making silently. The proposed fix — define families by explicit
KO/Pfam accession lists — is a change to how the pre-registered rubric is applied and needs an
appended amendment to `08_adjudication_protocol.md`. See `09_chunk2_harmonisation.md`.

Also outstanding: the wastewater per-gene table, which exists and is free but needs fetching
through a browser (ACS blocks automated download).

Chunks 1, 2 and 3 are done — `07_`, `09_` and `08_`.

> **Correction carried from Chunk 3:** the H1 pre-registration in `06_project_brief.md` is
> **spent** — catalogues 2 and 3 had already been examined when it was written. All three
> catalogue measurements are **exploratory** and must be reported as such.

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
