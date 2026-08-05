# 02 — Candidate Projects (v2)

**Phase 2 of 7.** Rewritten 2026-08-04 after Daniel identified two problems with v1:

1. **Anchoring.** 8 of 15 candidates and 4 of the top 5 were metal-site work. I had hand-picked
   a list of metalloenzymes, then "discovered" that metals were interesting — circular.
2. **Missing a third of the brief.** Phase 0 named three sub-areas; v1 delivered structural
   biology and a little chemoinformatics, and **zero** omics re-analysis.

**The fix that reopened omics:** v1 killed omics on file size, assuming raw data. Raw
mass-spec and FASTQ files are 10–100+ GB. But the **processed layer** — counts matrices, GEO
series matrix files, supplementary tables, summary statistics — is megabytes. That assumption
was doing all the work, and it was wrong.

**Retained from v1:** the three best, marked **[KEPT]**.

**Verification key:** ✅ verified by direct query · ⚠️ from a search snippet, needs checking ·
❓ unchecked. **DATA CHECK** states whether data is verified to exist in usable form.

---

## Field distribution (the thing v1 got wrong)

| Field | Candidates | Count |
|---|---|---|
| Enzymology & functional annotation | A1, A2, A3, A4 | 4 |
| Comparative genomics & metabolism | B1, B2, B3 | 3 |
| Transcriptomics / omics re-analysis | C1, C2, C3 | 3 |
| Microbiology & AMR | D1, D2 | 2 |
| Structural biology | E1, E2 | 2 |
| Chemoinformatics | F1 | 1 |
| **Total** | | **15** |

v1 had 13 of 15 in structural biology. These fifteen have **six independent failure modes**
rather than effectively four, so a single publication can no longer remove half the list.

---

# GROUP A — Enzymology and functional annotation

*Closest to your taught strength (enzymes, kinetics, metabolism), smallest data, and the
group with the most "old question, new data" structure.*

---

### A1 ⭐⭐ — Has enzyme misannotation actually got worse?

**Question.** Schnoes *et al.* (2009) measured misannotation of molecular function across four
public databases and found error propagating and increasing over time. Seventeen years later,
what is the rate now?

**Why this is the strongest candidate on the list.** The field openly *speculates* about the
answer without measuring it. One recent source states that Schnoes found ~3% of sequences
misannotated in 2005 data, and that "15 years later this number is **likely** much higher" ⚠️.
That word "likely" is the entire opportunity — a landmark paper's central measurement, widely
cited, never repeated, with the field guessing at the current value.

This is precisely one of your acceptable-novelty categories: *a re-analysis that tests an
assumption an existing paper made but never checked.* It is also the rare case where a
**null result is publishable and interesting** — "misannotation has not worsened, and here is
why" would be genuinely newsworthy given how often the opposite is asserted.

**Hypothesis (pre-specified, directional).** Misannotation rate in automatically-annotated
databases (TrEMBL, GenBank NR) has increased relative to 2005 levels, while manually curated
Swiss-Prot has remained low — and the *gap between them* has widened.

**Datasets.** Schnoes *et al.*, *PLOS Comput Biol* 2009, [PMC2781113](https://pmc.ncbi.nlm.nih.gov/articles/PMC2781113/) ✅ —
their 37 enzyme families and gold-standard sets define the method · UniProtKB/Swiss-Prot and
TrEMBL current releases (REST API) · EC numbers from ENZYME/Rhea · M-CSA for catalytic
residues.

**Tools.** UniProt REST API · Biopython · **HMMER** (family membership) · **BLAST+** ·
pandas/statsmodels · matplotlib.

**Figure.** Misannotation rate per database, 2005 vs 2026, per enzyme family, with confidence
intervals. **Table.** Per-family rates and the specific propagating misannotations found.

**Null result.** Rates unchanged or improved → curation and automated pipelines have kept
pace, contradicting a widely repeated assumption. Publishable.

**DATA CHECK ⚠️.** UniProt is trivially accessible. The risk is whether the 2009 paper's
gold-standard family definitions are recoverable in enough detail to replicate — **verify by
reading their methods and supplementary material before committing.** If not recoverable, the
project becomes "measure it with a defensible new gold standard", which is weaker but alive.

**Threat.** Someone may have re-measured it quietly inside a database paper. Phase 3 priority.

---

### A2 ⭐ — The orphan enzyme census, redone

**Question.** How many EC-classified enzyme activities still have no associated sequence, and
which have been resolved since the last systematic census?

**Background.** Orphan enzymes are activities characterised experimentally but with no gene
sequence assigned — so they are invisible to BLAST-style annotation. Reported: the orphan
fraction fell from 38% to 22% over ten years, but **>1,000 orphans remain among ~5,000 EC
entries**, and counting all reactions in metabolic databases pushes it to nearly 50% ⚠️.

**Why the gap plausibly exists.** The systematic censuses are ~2014 (*Biology Direct*;
*PLOS ONE* "Finding Sequences for over 270 Orphan Enzymes") ✅. Since then the sequence
databases have grown enormously and deep-learning EC predictors arrived (DeepES,
*Bioinformatics* 2025, btaf053 ✅). Nobody appears to have re-run the census against the
current state.

**Hypothesis.** The orphan fraction has continued to fall, but non-uniformly — orphans persist
disproportionately in EC classes tied to secondary metabolism and to organisms with few
sequenced genomes, rather than being randomly distributed.

**Tools.** ENZYME/ExplorEnz · UniProt · Rhea/MetaCyc · BLAST+ · pandas.

**Figure.** Orphan fraction per EC class over time. **Table.** Currently orphaned ECs, ranked
by how long they have been orphaned.

**Null.** Orphans are randomly distributed across EC classes → no structural explanation.

**DATA CHECK ⚠️.** EC lists are small and downloadable. Needs confirmation that "has a
sequence" can be determined reliably and reproducibly.

---

### A3 — Pseudoenzymes outside the kinases

**Question.** Pseudoenzymes make up an estimated 5–10% of proteins in enzyme families ⚠️, but
the systematic work is concentrated on pseudokinases (86 families mapped ⚠️), pseudophosphatases
and pseudoproteases. What is the pseudoenzyme fraction in metabolic enzyme families nobody has
counted?

**Method.** Catalytic residues from **M-CSA** (Mechanism and Catalytic Site Atlas) ✅; check
which family members have lost them.

**Null.** Metabolic families show the same 5–10% rate → pseudoenzymes are a uniform
evolutionary phenomenon, not a signalling-specific one. Genuinely informative.

**DATA CHECK ❓.** M-CSA coverage per family is unverified and is the likely killer.

---

### A4 — How stable are EC annotations?

**Question.** How often does a protein's assigned EC number change between UniProt releases,
and are some enzyme classes systematically unstable?

**Why interesting.** Annotation churn is a direct, measurable proxy for how confident the
field actually is — as opposed to how confident the database looks at any single moment.
Nobody has to be wrong for this to be revealing.

**DATA CHECK ❓.** Requires archived UniProt releases. Check availability first — this is a
one-command test and should be done before any further thought.

---

# GROUP B — Comparative genomics and metabolism

---

### B1 — Biosynthesis versus dependence, for a cofactor that isn't B12

**Question.** For cobamides (B12), a landmark comparative-genomics study across ~11,000
bacterial species found **86% of bacteria have cobamide-dependent enzymes but only 37% can
synthesise cobamides de novo** ⚠️ — with extreme asymmetry (Actinobacteria 57% synthesise;
Bacteroidetes 0.6% synthesise but 96% depend) ⚠️. Does the same supply–demand gap exist for
other cofactors — biotin, thiamine, folate, riboflavin, lipoate, molybdopterin?

**Why the gap plausibly exists.** The B12 analysis is the famous one because B12 is famous. The
same analysis for less glamorous cofactors is entirely mechanical once the pathway definitions
exist — which is exactly why nobody gets excited about doing it, and exactly why it may be
undone.

**Hypothesis.** Cofactors with higher biosynthetic cost (more enzymatic steps) show larger
gaps between dependence and synthesis capability, because the incentive to lose the pathway
and scavenge is greater.

**Tools.** KEGG or MetaCyc pathway definitions · NCBI/GTDB genomes · **HMMER** for pathway
enzyme detection · pandas.

**Figure.** Dependence vs biosynthesis capability per cofactor, per phylum.
**Null.** No relationship between pathway cost and the dependence gap.

**DATA CHECK ⚠️.** Genome-scale but at the *annotation* level, not assembly — likely
laptop-feasible if restricted to a few thousand representative genomes. **Estimate the download
size before committing.**

**Threat.** Note this brushes comparative genomics, which you excluded in Phase 0. Included
because the question is metabolic biochemistry rather than phylogenetics — say if it's still out.

---

### B2 — Metabolic pathway completeness in an understudied clade
Narrow version of B1. Lower ceiling, higher chance of finishing.

### B3 — Do gut microbiome CAZyme repertoires match host diet?
Core of 89 CAZyme families present across 85% of gut microbiomes ⚠️; "CAZotypes" already
described ⚠️. **Likely WOUNDED on arrival** — retained so Phase 3 can confirm the kill.

---

# GROUP C — Transcriptomics and omics re-analysis

*The group v1 wrongly eliminated. All of these use processed data only — no raw files.*

---

### C1 ⭐ — Studies of the same condition that disagree

**Question.** Take a well-defined condition with many independent GEO datasets. How often do
independent studies of the same comparison disagree about the direction of change for the same
gene — and is disagreement predictable from study characteristics (platform, sample size, year,
tissue handling)?

**Why this is a good shape.** It measures the field's reproducibility using data already
public, needs no new experiment, and has an unambiguous null. It also directly matches your
own criterion: *contradictions between two published datasets that nobody has reconciled.*

**Hypothesis.** Disagreement is concentrated in low-expression and low-effect-size genes, and
is predicted by sample size more than by platform.

**Datasets.** GEO **series matrix / processed counts only** — typically 1–50 MB per series.
Accessions to be selected and recorded in Phase 4.

**Tools.** GEOquery (Bioconductor) or direct download · **limma** / **DESeq2** / **edgeR** ·
statsmodels · matplotlib. **This is the candidate that would teach you the standard
differential-expression toolchain**, which is the single most CV-relevant skill set on this
whole list.

**Figure.** Concordance rate vs gene expression level and effect size, across study pairs.

**Null.** Disagreement is random with respect to study characteristics → no predictable
structure, which would itself be worth reporting.

**DATA CHECK ⚠️.** GEO processed data is definitely small enough. Must verify that enough
independent studies exist for one specific condition — **this is the make-or-break number and
must be counted before Phase 6.**

---

### C2 — What is different about understudied genes?
Understudied genes reportedly show contrasting RNA tissue-specificity signatures versus
well-characterised ones ⚠️. Narrow question: is "understudied" predictable from expression
pattern alone — i.e. are we ignoring these genes for a reason, or by historical accident?
**DATA CHECK ⚠️.** HPA and GTEx summary tables are downloadable.

### C3 — mRNA–protein discordance in an unexamined tissue
Cross-tissue correlation is established at 0.36–0.5 across 14 tissues ⚠️, and a kidney-specific
follow-up exists ✅. **Likely WOUNDED** — the general result is done; only specific tissues
remain. Retained for Phase 3 to confirm.

---

# GROUP D — Microbiology and AMR

### D1 — Resistance-gene co-occurrence in one species
NCBI Pathogen Detection holds >639,000 genomes ⚠️ with AMRFinderPlus annotations. Narrow
question: within a single species, which resistance genes co-occur more than chance, and does
co-occurrence structure differ between clinical and food isolates?
**DATA CHECK ⚠️.** MicroBIGG-E allows tabular download — verify it can be filtered server-side
rather than requiring a full download.
**Threat.** A 2024 study already analysed 639,087 genomes for prevalence ⚠️ — but prevalence is
not co-occurrence. Phase 3 must separate these carefully.
**Fit.** Connects directly to the AMR material in your Microbiology module.

### D2 — Are resistance genes annotated consistently across databases?
CARD vs AMRFinderPlus vs ResFinder on the same genomes. A disagreement study — same shape as
C1, different field.

---

# GROUP E — Structural biology *(reduced from 10 to 2)*

### E1 **[KEPT]** ⭐ — Metal assignment in the superoxide dismutase family
Cu (Z=29) and Zn (Z=30) differ by one electron and are near-indistinguishable in electron
density; Cu,Zn-SOD is the abundant family that puts both in one site, with Mn-SOD and Fe-SOD
as built-in controls.
**DATA CHECK ✅ — the only fully verified one on this list.** 523 entries at EC 1.15.1.1;
ZN=227, CU=151, MN=111, FE=71. Verified by direct RCSB query, `scripts/count_pdb_families.py`.
**Tools.** RCSB APIs · gemmi/Biopython · CheckMyMetal · PDBe validation reports.
**Threat.** MetalPDB, MESPEUS (*NAR* 2024), 2024 CheckMyMetal update may already break out SOD.

### E2 **[KEPT]** — Catalytic vs structural zinc in alcohol dehydrogenase
Elegant within-structure control: both sites in the same file, so resolution and deposition
year control themselves. **DATA CHECK ✅.** 237 entries at EC 1.1.1.1, 201 with ZN.

---

# GROUP F — Chemoinformatics

### F1 **[KEPT]** — Targets whose only bioactivity data is in patents
ChEMBL added 381 patent datasets, 99,948 bioactivity values, 1,322 targets — and for **154
targets patents are the only source** ⚠️. What kind of targets are these, and is patent
chemistry different from literature chemistry?
**Tools.** ChEMBL API · **RDKit** · scikit-learn · Pharos.
**Why it suits you.** Tiny data, RDKit installs natively on Windows, no WSL needed.
**DATA CHECK ⚠️.** Verify the 154 figure against the source paper.

---

## Ranking going into Phase 3

| Rank | Candidate | Field | Why |
|---|---|---|---|
| 1 | **A1** misannotation re-measured | Enzymology / annotation | Tests an unchecked assumption in a landmark paper; null result is publishable; tiny data; closest to your taught biochemistry |
| 2 | **E1** SOD metal assignment | Structural biology | Only fully passed data check; clean internal controls |
| 3 | **C1** GEO disagreement | Transcriptomics | Teaches the most CV-relevant toolchain (DESeq2/limma); unambiguous null |
| 4 | **A2** orphan enzyme census | Enzymology | Old census, new data; pure biochemistry |
| 5 | **B1** cofactor supply–demand | Comparative metabolism | Mechanical extension of a famous result to unglamorous cases |
| 6 | **F1** patent-only targets | Chemoinformatics | Tiny data, native Windows, uncorrelated risk |

Note the top six now span **five different fields**. If any one is scooped, the others survive.

---

## What Phase 3 must destroy first

1. **A1** — has anyone re-measured Schnoes? Search database-curation papers, UniProt release
   papers, and annotation-quality reviews. Also verify the "3% in 2005" figure against the
   actual paper rather than a snippet.
2. **A2** — check whether a post-2020 orphan census exists.
3. **C1** — count how many independent GEO studies exist for one condition. If under ~8, dead.
4. **E1** — check MetalPDB / MESPEUS / CheckMyMetal 2024 supplementary data for SOD.
5. **B1** — check whether the cobamide analysis has been repeated for other cofactors.
6. **F1** — verify the 154-target figure.

---

## Provenance log

| Date | Source | Method | Status |
|---|---|---|---|
| 2026-08-04 | RCSB PDB API, 12 EC + 48 metal queries | `scripts/count_pdb_families.py` | ✅ |
| 2026-08-04 | Livesey & Marsh bioRxiv 2025.07.31.667868 | fetched by Daniel; `scripts/pdf_to_text.py` | ✅ killed v1's N1–N2 |
| 2026-08-04 | MaveDB API; UniProt REST | PowerShell; `scripts/check_n1_feasibility.py` | ✅ |
| 2026-08-04 | ~22 web searches across 6 fields | WebSearch | ✅ |
