# 04 — Feasibility: R4, viral auxiliary metabolic genes

**Phase 4 of 7.** 2026-08-05. The job is to prove the project is **impossible** on one consumer
laptop with no budget. It is not, and the reason is worth stating precisely: the binding
constraint is not compute, it is **manual retrieval of supplementary tables from paywalled
journals**.

---

## Compute, storage, memory — not a constraint, by a wide margin

| Resource | Requirement | Budget | Verdict |
|---|---|---|---|
| Storage | ~200 MB total, already downloaded | ~50 GB | **0.4% used** |
| RAM | openpyxl `read_only` streaming; peak well under 1 GB | 16 GB | fine |
| Compute | full 88,729-row scan ≈ seconds; 255,859-row scan ≈ under a minute | 8 h | trivial |
| GPU / cluster | none needed | none available | fine |
| Cost | £0 — every source is open | £0 | fine |

Current footprint on disk:

| File | Size |
|---|---|
| `GlobalAMGs_SOM.xlsx` (ocean catalogue) | 113.8 MB |
| `kegg_ko_list.tsv` | ~3 MB |
| `VIBRANT_AMGs.tsv` + `DRAM_amg_database.tsv` | 44 KB |

**This is the least computationally demanding candidate the project has produced.** Feasibility
cannot kill it.

---

## The real constraint: getting catalogues two and three

The red team requires ≥2 further independent catalogues. Their availability is the actual gate.

| Candidate dataset | Status | Note |
|---|---|---|
| **Global ocean** (*Microbiome* 2024) | ✅ **verified working** | 88,729 conservative + 255,859 permissive calls, full DRAM-v output, Zenodo, open |
| **Global RNA virome** (*iMetaOmics* 2025) | ✅ obtainable | GitHub `YangZhao-LZU/RNA_AMG` + supplementary xlsx. **But only 256 AMGs**, and RNA viruses are a different biology — a weak comparator, useful mainly as a contrast |
| **Wastewater** (*ES&T*, [doi:10.1021/acs.est.2c07800](https://doi.org/10.1021/acs.est.2c07800)) | ⚠️ **needs Daniel** | ACS returns HTTP 403 to automated access. **The single most valuable second dataset** — it headlines queuosine genes as the most common AMGs, so it is the direct test case |
| **Soil viromes** (several, incl. *ISME J* organochlorine study) | ⚠️ unverified | Supplementary tables exist and include "DRAM-v information"; each needs checking individually |
| IMG/VR | ❌ not attempted | Almost certainly too large; unnecessary if the above work |

**Conclusion:** one catalogue is verified and sufficient to produce the primary result. A second
and third are obtainable but each requires a manual download, some through the university
library. That is a scheduling problem, not a feasibility failure.

> [!warning] The one thing that could still kill this
> If the additional catalogues turn out **not to publish gene-level annotation** — only summary
> counts or pathway-level totals — the cross-dataset generalisation is impossible and the
> project shrinks back to a single-catalogue report.
>
> **Test this before writing anything else.** One download each, checking only whether a
> per-gene table with KO or PFAM identifiers exists. Same discipline that killed R1 in forty
> minutes.

---

## Skills gap — what actually has to be learned

Honest mapping against a stated ceiling of A-level Edexcel Maths and no unaided coding.

| Needed | Current | How it gets closed |
|---|---|---|
| Reading DRAM-v / VIBRANT output semantics (`auxiliary_score`, `amg_flags`) | none | Tool documentation. **Required** — the `F` flag on 68% of `dcm` calls must be understood, not assumed |
| Proportions with confidence intervals | percentages only | Binomial CI. One concept, genuinely learnable in an afternoon |
| Comparing proportions between catalogues | none | Chi-square or Fisher's exact. Standard, well-documented |
| Pre-registration practice | none | Writing the plan *is* the learning |
| **The biochemical adjudication** | **this is his taught strength** | Year 1–2 metabolism: nucleotide biosynthesis, one-carbon pools, cofactor chemistry, cell-surface polysaccharides |

That last row is the point. **The hardest part of this project is the part his degree has
already prepared him for**, and the parts he lacks are two statistical concepts, not a new
discipline. Compare E1, which needed crystallographic validation theory from scratch.

New concepts to log in [[Concepts Queue]]: binomial confidence intervals · comparing two
proportions · pre-registration · the difference between a call and an abundance.

---

## Time, against a bursty schedule

Planned as resumable checkpoints, not weekly milestones, because term-time capacity is near zero.

| Chunk | Work | Effort | Resumable? |
|---|---|---|---|
| 0 | *(done)* enumeration + ocean catalogue result | — | ✅ complete |
| 1 | Verify catalogues 2–3 publish gene-level tables | half a day | ✅ hard stop if they don't |
| 2 | Confirm DRAM-v/VIBRANT flag semantics; handle the ~1,800 duplicate rows | 1 day | ✅ |
| 3 | Write and freeze the pre-registered rubric | 1–2 days | ✅ **must precede chunk 4** |
| 4 | Extend the measurement to catalogues 2–3 | 2–3 days | ✅ |
| 5 | **The adjudication** — gene family by gene family from biochemistry | 3–4 weeks | ✅ per family |
| 6 | Abundance weighting | 1 week | ✅ |
| 7 | Test whether exclusion changes a published conclusion | 1 week | ✅ |
| 8 | Write-up, figures, code release | 2 weeks | ✅ |

Roughly **8–10 weeks part-time**, and every chunk ends at a point where the work can be put down
and picked up months later. Chunk 5 is the substance and is naturally parcelled one gene family
at a time — the ideal shape for bursty availability.

---

## Verdict

**Feasible, with one gate.** Compute, storage, cost and skills are all comfortably inside
budget; the biochemistry is a strength rather than a gap. The only genuine risk is whether
catalogues two and three publish gene-level annotation — **and that must be tested in chunk 1,
before any further design work.**

**Proceed to Phase 6.**
