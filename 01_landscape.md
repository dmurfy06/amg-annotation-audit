# 01 — Landscape Scan

**Phase 1 of 7.** Written 2026-08-04. Author: Claude (research supervisor role), directed by Daniel.

**Purpose.** Identify areas where public data massively outstrips the analysis performed on
it, and where the *reason* for the gap is structural rather than accidental. This document
does **not** propose projects — that is Phase 2. It maps territory and, importantly, records
what was already eliminated during scanning.

**Scope filter applied.** Daniel's chosen sub-areas: structural/protein biophysics, omics
re-analysis, chemoinformatics/drug–target. Excluded by his choice: evolution/sequence
families as a primary focus (retained only where a structural question borders it).

**Method.** ~20 searches across Google/Bing web search, PubMed E-utilities, and targeted
fetches. Queries deliberately varied across technical phrasing, lay phrasing, tool names and
database names. Every factual claim below carries a verification status.

---

## Verification key

| Mark | Meaning |
|---|---|
| ✅ | Source URL or PMID directly returned by a search tool; citation is real |
| ⚠️ | Claim taken from a search-result snippet; the *paper* is real but the specific number needs checking against the paper itself |
| ❓ | Could not access — Daniel must fetch (see Action Items) |

**No number, DOI or accession in this document was written from memory.** Where I could not
verify, it is marked ❓ and listed in Action Items rather than guessed.

---

## The structural asymmetry — why gaps exist at all

Two findings frame everything below.

**1. Deposited omics data is barely reused.** Reported reuse rates per dataset: PRIDE
(proteomics) **0.12**, MassIVE (proteomics) **0.01**, ArrayExpress (transcriptomics)
**0.18** ⚠️. Source: Perez-Riverol et al., *Quantifying the impact of public omics data*,
Nat Commun 2019, [PMID 31383865](https://pubmed.ncbi.nlm.nih.gov/31383865/) ✅. Also
reported there: transcriptomics datasets keep attracting reanalysis until ~12 years old,
whereas **proteomics datasets are rarely reused after 3 years** ⚠️. That decay curve is
itself a map of where the neglected data sits.

**2. Structural space is annotated far behind its coverage.** Foldseek clustering of the
AlphaFold DB produced **2.30 million non-singleton structural clusters, of which 31% lack
annotation** ⚠️. Source: Barrio-Hernandez et al., *Clustering predicted structures at the
scale of the known protein universe*, Nature 2023 ✅
(https://www.nature.com/articles/s41586-023-06510-w).

The gap is therefore real and large. The difficulty is not *finding* unanalysed data — it is
finding unanalysed data where a **narrow, answerable, laptop-sized question** exists that
someone has not already answered.

---

## What Phase 1 already killed

Recording these matters as much as the survivors. Each was a plausible-sounding direction
eliminated *during* scanning, before reaching Phase 2.

| Direction | Killed by | Status |
|---|---|---|
| AlphaFold-based druggable-genome survey of a parasite | Done for *T. cruzi* (Front Cell Infect Microbiol 2022; Mdpi Pharmaceuticals 2026), *Plasmodium falciparum* (npj Drug Discovery 2025), *Schistosoma* (PMC12533970), *Wuchereria bancrofti* (arXiv 2510.07337) ✅ | **DEAD** |
| Cross-source bioactivity discordance in ChEMBL | Kalliokoski et al., PLOS ONE 2013 (65% of IC50 pairs differ >0.3 log, 27% >1 log ⚠️); Landrum & Riniker, *J Chem Inf Model* 2024, [doi:10.1021/acs.jcim.4c00049](https://pubs.acs.org/doi/10.1021/acs.jcim.4c00049) ✅ | **DEAD** in general form |
| ML prediction of enzyme kinetic parameters from BRENDA/SABIO-RK | Saturated: UniKP (Nat Commun 2023), CatPred (Nat Commun 2025), CataPro (Nat Commun 2025), RealKcat (bioRxiv 2025), KinForm (npj Syst Biol Appl) ✅ | **DEAD** |
| Meltome Atlas reanalysis for thermostability determinants | Dominant training set for TemStaPro, DeepTm, TemBERTure, DeepSTABp, SaProt ⚠️ | **DEAD** |
| NAD/NADP cofactor specificity determinants in Rossmann folds | Cofactory; Rossmann-toolbox (Bioinformatics 2021, [PMID 34571541](https://pubmed.ncbi.nlm.nih.gov/34571541/)) ✅ | **DEAD** |
| Generic metal-binding-site prediction on AlphaFold models | Metal3D, AlphaFill, ZincSight (PMC12572635), Fe-S/Zn metalloproteome expansion (JMB 2021), zinc-predictor benchmark (*JCIM* 2025, doi:10.1021/acs.jcim.5c00549) ✅ | **DEAD** |
| Structural comparison of AlphaFold2 vs ESMFold vs OmegaFold | Done, bioRxiv 2025 (~1,300 PDB structures) ✅ | **DEAD** |
| AlphaFold3 performance on intrinsically disordered proteins | First systematic evaluation, bioRxiv Dec 2025 ✅ | **DEAD** |
| SLC superfamily structural/evolutionary classification | Ferrada & Superti-Furga, *iScience* 2022 — 455 genes, 24 distinct TM folds ✅ | **DEAD** |
| Apolipoprotein/lipoprotein structural analysis | apoB100 solved by cryo-EM + AF2 + MD, *Nature* 2024 ✅. Requires experimental data he cannot generate | **DEAD** for a dry-lab undergrad |
| VEP performance in intrinsically disordered regions | *PLOS Comput Biol* 2025, [doi:10.1371/journal.pcbi.1013400](https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1013400) ✅ | **DEAD** |
| AlphaMissense stratified by soluble / transmembrane / mitochondrial | *Sci Data* 2024, [PMID 38744964](https://pubmed.ncbi.nlm.nih.gov/38744964/) ✅ | **DEAD** for those categories |

**Eleven directions eliminated before Phase 2.** This is the intended behaviour.

---

## The twelve surviving niches

Graded **A** (gap looks genuine and laptop-sized), **B** (plausible but with a known
threat), **C** (probably dead or probably infeasible — retained so the reasoning is on
record).

---

### N1 — Are structurally equivalent disulfide bonds functionally equivalent? ⭐ Grade A

**The gap.** Textbook biochemistry treats a disulfide bond as a disulfide bond. Daniel's own
closed LDLR project produced strong evidence against that: checked against the Tabet et al.
measurement map, cysteine substitutions in LDLR modules **LA1/LA2/LA6 were ~0–10% damaging
while LA3/4/5/7 were 77–100% damaging** (Mann–Whitney p = 2.8×10⁻²⁶), and **104 of 247
"certainly pathogenic" disulfide-breakers were functional**. That is a single-protein
observation. Whether it generalises across proteins has not obviously been asked.

**Why the gap plausibly exists.** The literature contains scattered single-protein
anecdotes — HIV envelope glycoprotein (only 2 of 10 disulfides rescued by paired Ala
substitution), the secretin receptor, ABCG2 ⚠️ — but these are individually published
across decades and different subfields, in exactly the pattern that stops anyone
aggregating them. Meanwhile MaveDB now holds **>7 million variant effect measurements**
across many proteins (MaveDB 2024, *Genome Biology*,
[PMID 39838450](https://pubmed.ncbi.nlm.nih.gov/39838450/)) ✅, and UniProt annotates
disulfide bonds per protein. Nobody obviously joined those two.

**Data needed.** MaveDB (API, free, small); UniProt disulfide/domain feature annotations
(REST, tiny); AlphaFold DB for solvent accessibility and local environment (per-structure
files, few MB each).

**Tools.** Biopython, requests/pandas, scipy/statsmodels, DSSP or Biopython's SASA for
burial, matplotlib. All native-Windows installable.

**Laptop verdict.** Trivially feasible. Total data well under 1 GB.

**Known threat.** A MaveDB-wide meta-analysis may already have stratified by UniProt feature
type. Must be destroyed properly in Phase 3.

**Daniel-specific advantage.** He already understands this problem, has a working feature
pipeline, and — unusually — has already been burned by the naive version of the claim. That
is a genuine head start, not a shortcut.

---

### N2 — Where do variant effect predictors fail, measured against measurement rather than labels? Grade B

**The gap.** VEP benchmarking is dominated by ClinVar labels. Daniel's post-mortem
demonstrated concretely why that is dangerous: his model scored ROC-AUC 0.853 against
ClinVar but Spearman ρ = −0.198 against measured function. Stratifying VEP accuracy by
*biochemical micro-context* — disulfide-bonded cysteine, metal-coordinating residue,
cofactor contact, catalytic residue — against MaveDB measurements rather than labels, is a
narrower question than the ones already published.

**Why the gap plausibly exists.** Stratification has been done by *coarse* category —
disordered vs ordered ✅, soluble vs transmembrane vs mitochondrial ✅ — because those
categories are easy to compute proteome-wide. Fine biochemical annotations require joining
UniProt feature tables, which is fiddly and unglamorous.

**Data needed.** MaveDB; AlphaMissense bulk predictions (large — needs a downscoping plan,
see Phase 4); UniProt features; possibly dbNSFP via MyVariant.info (Daniel's prior project
already used this successfully).

**⚠️ MAJOR THREAT — UNRESOLVED.** A bioRxiv preprint, *"Why variant effect predictors and
multiplexed assays agree and disagree"* (2025.07.31.667868), may cover exactly this.
**I was blocked by HTTP 403 and could not read it** ❓. This must be resolved before N2 can
be scored. See Action Items.

---

### N3 — Variant tolerance at metal-coordinating residues Grade B

**The gap.** Metal-site *prediction* is saturated (see kill table). Metal-site *variant
tolerance* — how much function is actually lost when you mutate a coordinating residue, and
whether that varies by metal, geometry, or coordination number — is a different question,
answerable from MAVE measurements.

**Why the gap plausibly exists.** The metal-site field is populated by structural
predictors and enzyme-discovery groups; the variant-effect field is populated by clinical
genetics groups. Different conferences, different journals, different vocabulary. Roughly
40% of PDB structures contain a modelled metal ⚠️, so the annotation base exists.

**Data needed.** MaveDB; UniProt binding-site annotations; PDB/AlphaFold geometry.

**Threat.** Overlaps N2 and may be absorbed by it. Also risks having too few proteins with
both MAVE data *and* annotated metal sites — an n problem to test in Phase 4, not assume.

---

### N4 — MaveDB as an under-mined cross-study resource Grade B

**The gap.** MaveDB holds >7M measurements ✅ contributed by many labs using different assay
readouts (abundance, binding, uptake, growth). Assay choice plausibly determines which
mechanism of damage is visible — Tabet et al. showed LDLR LA2/LA6 variants are damaging
*only* in the presence of excess VLDL, meaning the primary assay is blind to that
mechanism. How often does assay choice determine the answer, across MaveDB?

**Why the gap plausibly exists.** Each dataset is deposited to support one paper. Nobody
owns the cross-dataset comparison.

**Threat.** Cross-DMS comparison methods already exist — `multidms`, and joint modelling of
SARS-CoV-2 spike homologs (bioRxiv 2023.07.31.551037) ✅. Method exists; whether the
*survey* has been run is the open question.

---

### N5 — Ligand and metal modelling quality within one enzyme family in the PDB Grade B

**The gap.** "Structures of metal-containing macromolecules in which metals are misidentified
and/or suboptimally modeled are abundant in the PDB" ⚠️ (CheckMyMetal, *Nat Protoc* 2013 /
*Acta Cryst D* 2017 ✅). Tools to detect this exist. A systematic audit *within a single
biochemically coherent enzyme family* — asking whether the family's mechanistic literature
rests on questionable metal assignments — appears not to have been done family-by-family.

**Data needed.** PDB entries for one family (small — each structure is a few hundred KB),
CheckMyMetal web server (free), PDBe validation reports.

**Laptop verdict.** Excellent fit. Genuinely small data.

**Threat.** Might be a cataloguing exercise rather than a scientific result. Phase 5 will
press hard on "so what?".

---

### N6 — Tdark proteins: what does structure say about proteins the literature ignores? Grade B

**The gap.** IDG's **Tdark** category is defined by information scarcity: fewer than 5
publications, ≤3 GeneRIF annotations, ≤50 commercial antibodies ⚠️. These proteins now have
AlphaFold structures. Structural neighbours can transfer functional hypotheses.

**Why the gap plausibly exists.** By construction — Tdark proteins are ignored *because*
they are ignored. Tdark is enriched for membrane proteins and large families (olfactory
receptors, TFs) ⚠️.

**Threat.** The IDG/Pharos consortium publishes its own analyses and is well resourced.
Requires foldseek, which is Linux-first → WSL2 (available to Daniel).

---

### N7 — One unannotated AlphaFold structural cluster, characterised properly Grade B

**The gap.** 31% of 2.3M AFDB structural clusters lack annotation ⚠️. Precedent exists that
this yields real families: a P-loop NTPase family ("dual-wield NTPases") was mined from
AFDB this way ✅ (PMC10949312).

**Why the gap plausibly exists.** 700,000 unannotated clusters is far more than the field
can process. Each requires manual biochemical reasoning that does not scale.

**Threat.** Cluster *selection* is the whole problem, and doing it well needs judgement he
is still building. Full-scale analysis needs compute he does not have — must downscope to
one cluster. Also risks being unfalsifiable ("here is a protein, we think it might do X").

---

### N8 — Legacy proteomics: data nobody has touched in a decade Grade C→B

**The gap.** Proteomics datasets are rarely reused after 3 years ⚠️, while the search
engines and PTM-detection methods available have improved substantially. The oldest PRIDE
deposits are therefore the most systematically neglected data in biology.

**Why the gap plausibly exists.** Old raw formats, poor metadata, and no career incentive to
reanalyse someone's 2012 dataset.

**Threat — probably fatal.** Raw MS files are frequently 10–100+ GB per dataset. This
collides directly with the ~50 GB storage ceiling and 8 h compute limit. Survives only if
restricted to *processed* supplementary tables rather than raw files. Phase 4 will likely
kill it.

---

### N9 — Metabolomics repository reuse Grade C

**The gap.** Metabolomics reuse is even further behind proteomics. Reanalysis demonstrably
pays: reanalysis of lipidomics data from nine algal species produced **1,437 annotated
lipids, a 40% increase** over the original ⚠️.

**Why the gap plausibly exists.** **70% of MetaboLights / Metabolomics Workbench datasets
have incomplete chromatographic metadata** ⚠️, and raw file formats are not standardised.

**Threat — probably fatal for a beginner.** That 70% metadata-incompleteness figure is not a
minor annoyance; it is the reason the field is under-analysed, and it would consume his
entire timeline. Also, a pan-repository reanalysis resource appeared in *Nat Commun* 2025 ✅,
so the obvious version is being actively taken.

---

### N10 — Taxonomic bias: non-model organisms Grade C

**The gap.** Non-model invertebrates are severely underrepresented in NCBI resources ⚠️;
BLAST-based taxonomic assignment is systematically misleading for them ⚠️.

**Threat.** The bottleneck is missing reference databases, and building one is a large
project requiring assembly-scale compute. Explicitly noted in the literature as
"computationally expensive… hindering accessibility by researchers with limited
computational resources" ⚠️ — i.e. the barrier is precisely Daniel's constraint.

---

### N11 — Bioactivity discordance confined to one narrow target class Grade C

Retained only because the *general* form is dead (see kill table) while a sufficiently
narrow slice might not be. Low expectation. Phase 3 will most likely finish it.

---

### N12 — PubChem BioAssay inactive-compound data Grade C

**The gap.** PubChem archives *inactive* results, which are rarely analysed; there is
precedent for mining consistently-inactive compounds as clean starting points ⚠️.

**Threat.** Assay heterogeneity is severe, and the BioAssay Ontology work suggests
standardisation is itself the open problem. Probably a data-engineering project wearing a
biochemistry costume.

---

## Reading of the landscape

The strongest cluster is **N1–N4**: all sit on MaveDB, all are small-data, all use standard
tools, and all exploit a genuine structural gap — *measurement* data deposited by clinical
and protein-engineering groups, joined to *annotation* data curated by structural
biologists, with few people fluent in both. N1 is currently the most attractive because the
question is biochemical rather than methodological, the data is tiny, and Daniel has real
prior context.

The honest counterweight: N1–N4 are all in the variant-effect field, which is **fast-moving
and well funded**. That is exactly the field that scooped him last time. Phase 3 must be
merciless here, and the MaveDB gate from his own post-mortem applies to all four.

**N5** is the best non-variant-effect option and the best pure-structural-biology fit.
**N6/N7** are the highest-ceiling and highest-variance options.
**N8–N12** are retained for completeness and will most likely die in Phase 4.

---

## Action Items — Daniel must fetch these

I hit a hard block. Per the no-fabrication rule I am not guessing at the contents.

### AI-1 (blocking for N2, N3, N4) — bioRxiv preprint, HTTP 403

**URL:** https://www.biorxiv.org/content/10.1101/2025.07.31.667868v1.full

**Title:** *Why variant effect predictors and multiplexed assays agree and disagree*

**What to do:** open it, and either save the full text to
`C:\Users\danie\Documents\research-project\refs\vep_mave_2025.txt`, or paste back the
**Abstract**, the **Methods** section listing which predictors and which MAVE datasets were
used, and any **figure captions** that mention stratifying by structural or biochemical
category (look for: disulfide, cysteine, metal, binding site, cofactor, catalytic).

**Why it matters:** if this paper already stratifies VEP-vs-MAVE agreement by biochemical
context, then N2 is dead and N1 is wounded. I would rather know now than in week 6.

### AI-2 (non-blocking, useful) — confirm library access works

Try to reach one paywalled paper through your university VPN — e.g. the Landrum & Riniker
*JCIM* 2024 paper at https://pubs.acs.org/doi/10.1021/acs.jcim.4c00049 — and tell me whether
you get the full PDF. This tells me how much I can lean on you for Phase 3 novelty checks.

---

## Provenance log

| Date | Source | Retrieved via | Status |
|---|---|---|---|
| 2026-08-04 | Google/Bing web search × ~17 queries | WebSearch tool | complete |
| 2026-08-04 | PubMed E-utilities × 4 queries | pubmed MCP | 2 returned 0 hits (over-conjunctive query translation — a real PubMed quirk worth knowing) |
| 2026-08-04 | bioRxiv 2025.07.31.667868 | WebFetch | **FAILED — HTTP 403**, escalated to AI-1 |
| 2026-08-04 | Daniel's Obsidian vault, LDLR project note | Read | complete — source of the LA1/2/6 finding |

---

**Next:** Phase 2 — generate 15 candidate projects with named accessions, tools, target
figures and defined null results. Phase 2 does **not** require AI-1 to be resolved; Phase 3
does.
