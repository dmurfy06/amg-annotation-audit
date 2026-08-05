# 03 — Novelty Audit (in progress)

**Phase 3 of 7.** Started 2026-08-04. Goal: actively prove each candidate has already been
done. Verdicts: **DEAD** (with the citation that kills it) · **WOUNDED** (partly done — state
what remains) · **ALIVE** (no evidence found, with the searches listed so the effort is
judgeable).

**Audited: 15 of 15. Phase 3 complete.**

**Result: 10 DEAD, 3 WOUNDED, 1 ALIVE-but-undifferentiated, 1 ALIVE and strengthened.**

---

## A1 — "Has enzyme misannotation got worse?" → **DEAD**

**Killed by:** Rembeza E & Engqvist MKM (2021), *Experimental and computational investigation
of enzyme functional annotations uncovers misannotation in the EC 1.1.3.15 enzyme class*,
*PLoS Computational Biology* 17(9):e1009446. PMID 34555022,
[doi:10.1371/journal.pcbi.1009446](https://doi.org/10.1371/journal.pcbi.1009446).
Retrieved via PubMed. ✅

**Why it is fatal.** Their abstract states they *"performed a computational analysis of
annotations to all enzyme classes in the BRENDA database, and showed that nearly **18% of all
sequences** are annotated to an enzyme class while sharing no similarity or domain architecture
to experimentally characterised representatives."* They also *"showed that misannotation in the
enzyme class increased over time."*

That is A1's question — database-wide misannotation, re-measured, plus the increase-over-time
claim — answered in 2021. The premise that nobody has re-measured since Schnoes is false.

**A second, independent problem.** The **SFLD** (Structure–Function Linkage Database), which
supplied Schnoes' gold standard of 14,902 sequences, has been **static and unmaintained since
April 2019** ⚠️. A 2026 misannotation measurement needs a 2026 gold standard; the original one
is frozen. So even the narrow "replicate Schnoes exactly on UniProt" version is
methodologically awkward, not merely derivative.

**Correction to the record.** In `02_candidates.md` v2 I attributed "~3% misannotated in 2005"
to Schnoes. That is wrong. The paper reports Swiss-Prot near 0%, and GenBank NR / TrEMBL /
KEGG averaging **5–63%** across six superfamilies, with **>80% in 10 of the 37 families**.
Database snapshots were taken **17 February 2006**. Verified by direct fetch of
[PMC2781113](https://pmc.ncbi.nlm.nih.gov/articles/PMC2781113/) ✅. The 3% figure came from a
later paper citing Schnoes about something narrower.

> [!note] What went wrong in my own process
> I ranked A1 first on the strength of a search snippet saying the rate is "**likely** much
> higher" — treating absence of evidence in my searches as evidence of absence. I did not
> search the *citing* literature before ranking it. The correct order is: find the landmark
> paper, then read what cites it, **then** decide whether the question is open.

**Searches run:** "misannotation rate protein function databases re-measured since Schnoes";
"annotation error rate / annotation quality protein databases increased over time 2024 2025";
PubMed `misannotation` 2015–2026 (403 hits, top 30 inspected); UniProt 2025 release paper.

---

## A2 — Orphan enzyme census → **ALIVE**, and reframed into something better

**No post-2014 census found.** Repeated searches return only:
- Lespinet & Labedan (2005/2006), *A survey of orphan enzyme activities*, BMC Bioinformatics ✅
- ORENZA web resource (2006) ✅
- Sorokina *et al.* (2014), *Profiling the orphan enzymes*, *Biology Direct* ✅
- Ramkissoon *et al.* (2014), *Finding Sequences for over 270 Orphan Enzymes*, *PLOS ONE* ✅
- DeepES (2025), *Bioinformatics* btaf053 ✅ — a **method**, not a census

**DATA CHECK ✅ PASSED — decisively, today.** `scripts/orphan_enzyme_census.py` parses the
ENZYME nomenclature flat file, where each EC entry carries `DR` lines listing UniProtKB
cross-references. An entry with no `DR` line has no associated sequence.

```
Total EC entries in file        : 8,456
Transferred / deleted (excluded): 1,491
Retained EC entries             : 6,965
...with NO UniProt cross-ref    : 1,181
ORPHAN FRACTION                 : 17.0%
```

Against the published series: **36.8% (2006) → ~22% (2014) → 17.0% (2026)**.

Orphan rate varies by class — hydrolases **19.2%**, oxidoreductases 18.0%, transferases 17.4%,
ligases 13.3%, isomerases 13.1%, lyases 12.5%, translocases 10.2%.

> [!warning] The census alone is NOT a project
> A ~100-line script answered it in three minutes. One number and a bar chart is a figure, not
> a piece of research. If this proceeds as "count the orphans", Phase 5 will destroy it.

### The question the script actually surfaced

**1,491 of 8,456 EC entries are transferred or deleted.** So the orphan fraction has two ways
to fall:

1. **Real progress** — an orphan gets a sequence assigned, and is solved.
2. **Attrition** — an orphan gets *deleted or transferred* out of the EC classification, and
   silently stops being counted.

Everyone cites the falling orphan fraction as progress. **Nobody appears to have checked which
mechanism it is.**

**Reframed question.** Is the twenty-year decline in orphan enzymes driven by orphans being
*solved*, or by orphans being *retired from the classification*?

**Hypothesis (pre-specified).** Orphan EC entries are enriched among transferred/deleted
entries relative to non-orphan entries — i.e. a measurable share of the apparent progress is
bookkeeping rather than discovery.

**Why this is a real project and the census is not:** it tests an assumption the field repeats
without checking, it has a clean null (orphans and non-orphans are retired at the same rate →
the decline is genuine progress), it needs historical ENZYME releases rather than one file, and
the answer is interesting **either way**.

### UPDATE 2026-08-05 — the reframe is also largely done. **A2 → WOUNDED, badly**

The blocking data check **passed**: historical snapshots are unnecessary because ExplorEnz's
SQL dump carries a `hist` table with `action` ('created' / 'transferred') and a free-text
`history` field giving years — e.g. `'1.1.1.5','transferred',...,'created 1961, modified 1976,
deleted 2010'`. So creation and deletion dates are recoverable per EC. ✅

**But then reading the full text of Sorokina *et al.* killed most of the value.** Retrieved via
PubMed Central, PMC4084501; local copy `refs/sorokina_2014_orphan_enzymes.txt`.

What they already did:

| Their result | Effect on A2 |
|---|---|
| Orphan fraction **22.4%** — 1,143 of 5,096 EC numbers with no UniProt protein (Feb 2013) | The census is theirs. My 17.0% merely updates their number |
| Per-class orphan rates: class 1 = 25%, 2 = 26%, 3 = 19%, 4 = 19%, 5 = 15%, 6 = 13% | The per-class breakdown is theirs too |
| **Figure 2: "Snapshot of EC number status by year of creation… proportion of nowadays active entries in red and transferred/deleted entries in pink"** | **This is the retirement analysis.** Already plotted |
| Second panel: "EC entry modifications over years: creation (yellow), transfer (light red), deletion (dark red)" | Also already plotted |
| Figure 3: heatmap of activity-discovery year vs EC-creation year | The lag analysis is theirs |
| vs Karp 2003: −294 orphan entries while +1,360 EC entries added | The trend framing is theirs |

**The one sliver that may remain.** They state: *"Only valid and complete EC entries were
considered without taking into account deleted or transferred entries."* So their **orphan**
count excludes retired entries, and Figure 2 covers **all** EC entries, not orphans
specifically. The precise cross — *are orphans retired at a higher rate than non-orphans?* —
is not visibly done.

**But that is a thin distinction and I am not going to pretend otherwise.** They hold both
variables, the figures sit adjacent, it may well be in Additional file Figure S1.1 / Table
S2.1 (unchecked ❓), and a reviewer would reasonably say the 2014 review covers the territory.
As a first project it would be a small increment on someone else's review.

**Also unresolved:** my 17.0% and their 22.4% use different methods — ENZYME `DR` lines versus
IntEnz + UniProt — so the two are not directly comparable without harmonising. That work would
have to be done before any trend claim.

**Verdict: WOUNDED, badly. Not recommended.** Kept on the list only pending a check of their
supplementary material, which would decide between "small increment" and "fully done".

---

## C1 — Cross-study disagreement in GEO → **WOUNDED**

**Why.** The general finding is established: *"The cross-study concordance of differential
expression results is remarkably low"* ⚠️, and *"reproducibility of differential-expression was
associated with differential-expression strength"* ⚠️ — which is essentially the hypothesis
C1 pre-specified. Cross-dataset perturbation benchmarking compendia also exist.

**What may remain.** Concordance for one specific, well-defined condition, and whether
disagreement is predicted by *study design* variables rather than effect size. Derivative, and
it would need a sharper angle to be worth doing.

**Retained but demoted.** Not dead; not currently competitive with A2.

---

## E1 — SOD metal assignment → **ALIVE**, and the only candidate that improved under scrutiny

**No family-specific audit found.** Searches for SOD combined with MetalPDB, MESPEUS,
CheckMyMetal and metal-misassignment terms returned only SOD structural/mechanistic biology,
not database audits.

**CheckMyMetal 2024 checked directly** ([PMC11364027](https://pmc.ncbi.nlm.nih.gov/articles/PMC11364027/)) ✅.
Their analysis is organised by **metal type, resolution, technique and molecular weight** —
there is **no breakdown by enzyme family, EC number or protein class**, SOD is not mentioned,
and Cu-vs-Zn discrimination is not discussed. The family-level question is untouched.

**MetalPDB queried directly, not read about** ✅ — the discipline that killed A1. It returns
metal identity, ligands, geometry and coordination number, but **no quality or validation
flags**. So MetalPDB is a *data source* for E1, not a competitor. Geometry arrives
pre-computed by an established citable tool, which satisfies the no-reimplementation rule.

**MESPEUS still unqueried ❓** — the one outstanding novelty check.

### The premise was wrong, and the corrected version is better

`scripts/sod_metal_sites.py` pulled 1,531 sites / 341 PDB entries / 1,757 metal atoms /
92 UniProt accessions. Zn 685, Cu 431, Mn 287, Fe 200, Ni 74, plus 80 non-catalytic atoms
(Na 32, Cd 15, Ca 14, Pt 9, K 5, Co 3, U 2).

| Framing | Status |
|---|---|
| **Cu vs Zn** — the original premise | **Wrong.** They are cleanly separable by ligand set: Cu mean 0.01 Asp, Zn mean 0.88 Asp |
| **Mn vs Fe** — not originally considered | **The real problem.** Identical dominant signature `1ASP+3HIS+1HOH`, near-identical coordination-number distributions, same Pfam domains, one electron apart (Z=25 vs 26) |

Cambialistic SODs confirm the ambiguity is biologically real: 1QNN models a 3:1 Fe/Mn mixture,
and *P. shermanii* shows no obvious structural difference between the two forms ⚠️.

### The result that makes this a project

`scripts/sod_metal_disagreement.py` asks whether **independent depositions of the same protein
(same UniProt accession) assign different metals**. Cu+Zn co-occurrence is treated as expected,
not as conflict.

```
proteins with catalytic metals   : 92
proteins with >=2 PDB entries    : 41
DEPOSITIONS DISAGREE ON THE METAL: 11   (27% of multi-entry proteins)
   of those, Fe/Mn disagreements : 10
```

| Protein | Organism | Split |
|---|---|---|
| P00448 | *E. coli* | **Mn in 11 entries, Fe in 1** (1mmm) |
| G0RQS7 | *T. reesei* | Mn 5, Fe 2 |
| P80293 | *P. freudenreichii shermanii* | Fe 5, Mn 1 (1ar4) |
| P9WGE7 | *M. tuberculosis* | Fe 4, Mn 1 (1gn4) |
| Q9RUV2 | *D. radiodurans* | Mn 4, Fe 1 (1y67) |
| P00447 | *S. cerevisiae* | Mn 4, Fe 1 (3rn4) |
| P19665 | *P. gingivalis* | Fe 2, Mn 1 |
| Q186I6 | *C. difficile* 630 | Fe 2, Mn 1 |
| Q9Y8H8 | *A. pernix* K1 | Mn 1, Fe 1 |
| O15904 | *B. bovis* | **Zn 1, Fe 1** |
| W8UU58 | *S. aureus* | Mn 1, Fe 1 |

**Sharpened question.** Across the SOD structural record, how much metal-identity disagreement
is *deliberate biology* (cambialism, metal-substitution experiments) versus *assignment
error* — and can the deposited evidence distinguish them?

*P. shermanii*, *P. gingivalis* and *A. pernix* are known cambialistic SODs, so their splits are
expected. *E. coli* MnSOD is a textbook manganese enzyme with eleven structures saying Mn and
one saying Fe. Separating those two categories is the work.

> [!warning] Red team, stated now rather than discovered in Phase 5
> In this family the modelled metal is often assigned from **which protein was purified**, not
> from the density. So "misassignment" may be the wrong frame entirely. The defensible version
> is the narrow one already tested — *independent redeterminations of the same protein
> disagreeing* — not a claim that the density was misread.

> [!caution] A cautionary precedent that applies directly
> A published analysis of zinc coordination patterns (Yao *et al.* 2015) was subsequently shown
> to "violate/ignore chemical and crystallographic knowledge" ⚠️ — i.e. a database-scale metal
> coordination study went wrong by trusting deposited sites uncritically. Any E1 protocol must
> filter on resolution and validation metrics *before* counting, and say so up front.

**DATA CHECK ✅** remains the strongest on the list: 523 entries at EC 1.15.1.1 by direct RCSB
query; 1,531 annotated sites by direct MetalPDB query.

---

## The sweep — remaining eleven candidates

Run 2026-08-05. Each was attacked with the question *"who has already done this, at larger
scale?"* Ten of eleven had an answer.

---

### A3 — Pseudoenzymes outside the kinases → **DEAD**

**Killed by:** Ribeiro AJM, Tyzack JD, Borkakoti N & Thornton JM (2019), *Identifying
pseudoenzymes using functional annotation: pitfalls of common practice*, *FEBS J*
287(19):4128–4140. PMID 31733177, [doi:10.1111/febs.15142](https://doi.org/10.1111/febs.15142).
Abstract retrieved via PubMed ✅.

This is A3's exact question, exact data source and exact method. From their abstract: they
*"analyse current knowledge related to pseudoenzymes **across a large number of enzymes
families**"*, using *"UniProtKB as the source for functional annotation and **M-CSA … for
information on the catalytic residues**"*, and *"After identifying pseudoenzymes related to
enzymes in M-CSA, we were able to comment on **their prevalence across enzyme families**"*.

**It is worse than merely prior.** They explicitly went looking beyond the pseudokinases —
A3's stated gap — and their conclusion *"challenge[s] two common ideas… that pseudoenzymes are
ubiquitous across enzyme families and that **mutations in the catalytic residues of enzyme
homologues are always a good indication of lack of activity**"*. That second clause destroys
A3's *method*, not just its novelty. Thornton's group built M-CSA; they audited its use for
this purpose and found it unreliable.

**Also note:** the 5–10% figure A3 was built on already comes from a kingdom-wide analysis
across prokaryotes, archaea and eukaryotes ⚠️ — so it was never kinase-specific in the first
place. A3's premise was false as written.

---

### A4 — How stable are EC annotations? → **DEAD**

**Killed by:** *ENZYMAP: Exploiting Protein Annotation for Modeling and Predicting EC Number
Changes in UniProt/Swiss-Prot*, *PLOS ONE* 9(2):e89162 (2014),
[PMC3929618](https://pmc.ncbi.nlm.nih.gov/articles/PMC3929618/),
[doi:10.1371/journal.pone.0089162](https://doi.org/10.1371/journal.pone.0089162) ✅.

The title alone is fatal. Reported to have analysed **44 major releases**, **18,727,155 EC
pairs**, of which **55,908 changed** ⚠️ *(figures from search snippet, unverified — but the
kill does not depend on them)*. They also modelled severity by position in the EC hierarchy
and built a supervised predictor of future changes.

A4 asked "how often does EC annotation change between releases, and are some classes
systematically unstable?" That was measured twelve years ago, and then exceeded.

---

### B1 — Cofactor supply vs dependence, beyond B12 → **DEAD**

**Killed by:** Rodionov DA *et al.* (2019), *Micronutrient Requirements and Sharing
Capabilities of the Human Gut Microbiome*, *Front Microbiol* 10:1316. PMID 31275260,
[PMC6593275](https://pmc.ncbi.nlm.nih.gov/articles/PMC6593275/) ✅.

They performed *"a subsystems-based reconstruction of **biogenesis, salvage and uptake** for
**eight B vitamins** (B1, B2, B3, B5, B6, B7, B9, B12) and queuosine over a reference set of
**2,228 bacterial genomes** representing 690 cultured species"*, with prototroph/auxotroph
cross-feeding analysis.

That is B1's analysis, for B1's exact cofactor list, at a scale a laptop cannot match — and it
includes **salvage and uptake**, a dimension B1 did not even propose. Reinforced by
Magnúsdóttir *et al.* (2015), *Systematic genome assessment of B-vitamin biosynthesis suggests
co-operation among gut microbes*, PMID 25941533 ✅ (256 gut bacteria, eight B vitamins).

---

### B2 — Pathway completeness in an understudied clade → **DEAD, with B1**

B2 was defined as "narrow version of B1". Once the general analysis is a published subsystems
reconstruction, the narrow version becomes *running somebody else's established protocol on a
clade they happened not to cover*. That is the weakest novelty class on the brief's own list —
it is not an unasked question, it is an unfilled cell in someone else's table.

**Conceivable rescue:** Rodionov *et al.* is human-gut-only, so a non-gut clade is technically
uncovered. Not pursued — the ceiling is too low to be worth the weeks.

---

### B3 — Gut CAZyme repertoires vs host diet → **DEAD** (as predicted on arrival)

**Killed by:** *Global Profiling of Carbohydrate Active Enzymes in Human Gut Microbiome*,
*PLOS ONE* 10(11):e0142038 (2015), PMID 26544883,
[PMC4636310](https://pmc.ncbi.nlm.nih.gov/articles/PMC4636310/) ✅ — three **"CAZotypes"** with
*"distinct taxonomic drivers and probable dietary basis"*, with French/American populations on
CAZotype-2 and rural Malawi/Venezuela on CAZotype-3.

Further buried by Cayman (*Nature Microbiology* 2026,
[s41564-026-02318-2](https://www.nature.com/articles/s41564-026-02318-2)) ⚠️, a dedicated
large-scale CAZyme-repertoire analysis tool, and by published income-setting contrasts in
fibre-degrading CAZyme enrichment.

---

### C2 — What is different about understudied genes? → **DEAD**

**Killed by:** Stoeger T, Gerlach M, Morimoto RI & Nunes Amaral LA (2018), *Large-scale
investigation of the reasons why potentially important genes are ignored*, *PLOS Biology*
16(9):e2006643. PMID 30226837, [PMC6143198](https://pmc.ncbi.nlm.nih.gov/articles/PMC6143198/),
[doi:10.1371/journal.pbio.2006643](https://doi.org/10.1371/journal.pbio.2006643). Abstract
retrieved via PubMed ✅.

C2 asked whether "understudied" is predictable from expression pattern — *are we ignoring these
genes for a reason, or by historical accident?* Their abstract: *"differences in attention can
be explained, to a large extent, exclusively from a small set of identifiable chemical,
physical, and biological properties of genes"*, and these features *"allow us to accurately
predict the number of publications on individual human genes, the year of their first report,
the levels of funding awarded by the NIH, and the development of drugs"*.

The question is answered, and answered more completely than C2 posed it. A follow-up also
exists (*eLife* 93429, understudied genes lost in a "leaky pipeline") ⚠️.

---

### C3 — mRNA–protein discordance in an unexamined tissue → **DEAD** (as predicted)

**Killed by:** Jiang L *et al.* (2020), *A Quantitative Proteome Map of the Human Body*, *Cell*
183(1):269–283 ⚠️ — **12,627 genes across 32 normal human tissues**, 201 GTEx samples. They
identified 1,012 genes correlated across all tissues and examined genes *"concordantly and
discordantly expressed **for each tissue**"*.

Per-tissue discordance is the whole of C3, already done across 32 tissues. The kidney-specific
follow-up that already existed ✅ was the warning sign; this is the kill.

---

### D1 — Resistance-gene co-occurrence in one species → **DEAD**

Co-occurrence is not the unexplored complement to prevalence that D1 assumed. Found:
- Co-occurrence of β-lactam and aminoglycoside determinants among **clinical *and*
  environmental** isolates of *K. pneumoniae* and *E. coli*,
  [PMC9416466](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9416466/) ⚠️ — that is D1's
  clinical-vs-other-source contrast, in D1's species
- *Global Footprint of the Multidrug Resistance Island Ec17R and **Resistance Gene
  Co-Occurrence** in Pathogenic* E. coli *Isolates*, bioRxiv 2025 ⚠️
- *Clusters of Antibiotic Resistance Genes Enriched Together Stay Together*, *mBio* ⚠️
- The 639,087-genome NCBI Pathogen Detection study covering **food and human sources**,
  [PMC11051753](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11051753/) ⚠️, plus a
  2015–2025 foodborne co-resistance analysis identifying principal axes of co-resistance ⚠️

The prevalence/co-occurrence distinction Phase 2 flagged as the thing to protect does not hold.

---

### D2 — Are resistance genes annotated consistently across databases? → **DEAD**

The Jaccard indices are already published: *"highest concordance between AMRFinderPlus and
MEGARES (J=0.66), followed by CARD–MEGARES (J=0.59) and AMRFinderPlus–CARD (J=0.56)… mean
Jaccard similarity ≈0.21"* ⚠️. A head-to-head on MRSA isolates gives per-database gene counts
and even per-database *mecA* detection rates (82.2% / 98.1% / 100%) ⚠️.

Recent and ongoing: *A Systematic Benchmark of Antibiotic Resistance Gene Detection Tools*
(bioRxiv 2026) and *The elusive resistome: a global comparison reveals large discrepancies
among detection pipelines* (bioRxiv 2026) ⚠️. This is an active, crowded benchmarking area.

---

### E2 — Catalytic vs structural zinc in alcohol dehydrogenase → **ALIVE, but undifferentiated**

**No database audit found** comparing modelling or validation quality between the two site
types. The *biochemical* distinction is textbook — catalytic sites take three protein ligands
plus solvent/substrate, structural sites take four protein ligands, usually Cys, from a local
chain segment ⚠️ — but that is the premise, not the result.

**Why it is not being promoted.** It is the same field, same method and same failure mode as
E1. Running both would not be two projects, it would be one project with two chapters — and if
a metal-site audit paper appears, both die together. Retained as E1's **backup**, not as a
diversifying alternative.

**DATA CHECK ✅.** 237 entries at EC 1.1.1.1, 201 with ZN.

---

### F1 — Targets whose only bioactivity data is in patents → **WOUNDED**

**The 154 figure is verified ✅** by direct fetch of the ChEMBL 2023 paper (*NAR*
52(D1):D1180): since release 24 they added *"381 new patents… containing 99948 bioactivity
values against 1322 targets. For **154 of these targets, patents are currently the only source
of bioactivity data**."*

**The good news:** that paper does **not** characterise the 154 — no breakdown by protein
family, no therapeutic-area analysis, no patent-vs-literature chemistry comparison ✅. So the
descriptive question is genuinely unanswered by the source.

**The bad news, two ways:**
1. The chemistry half is done. Patent-derived and ChEMBL-derived compounds *"formed distinct,
   minimally overlapping clusters in chemical space across all 15 targets analyzed"* ⚠️.
2. The curation was done *"in collaboration with the **Illuminating the Druggable Genome**
   project"* — an entire NIH programme whose purpose is characterising understudied targets,
   with Pharos as its front end. The odds that nobody at IDG has profiled these 154 are poor.
   **Unchecked ❓** and it is the deciding test.

**And the shape is wrong.** "What kind of targets are these 154?" is descriptive — a table and
a bar chart, answerable in an afternoon. That is the A2 trap again: a figure, not a project.

---

## Standings — final

| Candidate | Field | Verdict | Killed by / status |
|---|---|---|---|
| **E1** SOD metal assignment | Structural | **ALIVE** ⭐ | Strengthened under scrutiny; 27% of multi-entry SOD proteins disagree with themselves |
| E2 catalytic vs structural Zn | Structural | ALIVE | No audit found — but same field, same failure mode as E1. Backup, not alternative |
| F1 patent-only ChEMBL targets | Chemoinformatics | WOUNDED | 154 verified and uncharacterised, but IDG/Pharos unchecked and the shape is descriptive |
| C1 GEO disagreement | Transcriptomics | WOUNDED | General result published |
| A2 orphan enzymes | Enzymology | WOUNDED badly | Sorokina *et al.* 2014 Figure 2 |
| A1 misannotation re-measured | Enzymology | **DEAD** | Rembeza & Engqvist 2021 |
| A3 pseudoenzymes | Enzymology | **DEAD** | Ribeiro *et al.* 2019 — question *and* method |
| A4 EC annotation stability | Enzymology | **DEAD** | ENZYMAP 2014 |
| B1 cofactor supply–demand | Comparative metabolism | **DEAD** | Rodionov *et al.* 2019 |
| B2 clade pathway completeness | Comparative metabolism | **DEAD** | Dies with B1 |
| B3 CAZymes vs diet | Comparative metabolism | **DEAD** | CAZotypes 2015; Cayman 2026 |
| C2 understudied genes | Transcriptomics | **DEAD** | Stoeger *et al.* 2018 |
| C3 mRNA–protein discordance | Omics | **DEAD** | Jiang *et al.* 2020, 32 tissues |
| D1 AMR co-occurrence | Microbiology | **DEAD** | Multiple; clinical-vs-source contrast done |
| D2 AMR database concordance | Microbiology | **DEAD** | Jaccard indices published; crowded field |

## What the pattern says

Every one of the ten fresh kills died the same way: **an established group had already run the
question at a scale a laptop cannot reach.** Rodionov had 2,228 genomes. Jiang had 32 tissues.
Stoeger had the whole human gene set. Thornton's group built the database A3 wanted to use.

The survivors survive for the opposite reason — they are narrow enough that no funded group
bothered. That is direct evidence for the "extremely niche is ideal" rule set in Phase 0, and
against the instinct to pick a question that sounds important.

> [!warning] An honest problem, flagged rather than buried
> The field diversity deliberately built into v2 has collapsed. Not through anchoring this time
> — the searches were adversarial and the kills are cited — but because the broader candidates
> were the ones big groups had already done. **The two survivors are both structural metal
> work**, which is the concentration Daniel objected to in v1. That is a real trade-off between
> *strongest on evidence* and *diverse by design*, and it is his call, not mine.

---

## Provenance

| Date | Source | Method | Status |
|---|---|---|---|
| 2026-08-04 | Schnoes *et al.* 2009, PMC2781113 | WebFetch | ✅ verified rates, method, 2006 snapshot |
| 2026-08-04 | PubMed `misannotation`, 403 hits | pubmed MCP, top 30 metadata | ✅ found the killer |
| 2026-08-04 | ENZYME flat file, expasy.org | `scripts/orphan_enzyme_census.py` | ✅ 8,456 entries parsed |
| 2026-08-04 | ~6 further web searches, varied vocabulary | WebSearch | ✅ |
| 2026-08-05 | Sorokina *et al.* 2014, PMC4084501 | pubmed MCP full text | ✅ wounded A2 |
| 2026-08-05 | CheckMyMetal 2024, PMC11364027 | full text | ✅ no family breakdown — helps E1 |
| 2026-08-05 | MetalPDB API, EC 1.15.1.1 | `scripts/sod_metal_sites.py` | ✅ 1,531 sites cached |
| 2026-08-05 | same cache, per-UniProt grouping | `scripts/sod_metal_disagreement.py` | ✅ 11/41 disagree |
| 2026-08-05 | Ribeiro *et al.* 2019, PMID 31733177 | pubmed MCP metadata | ✅ killed A3 (Wiley paywalled, 402) |
| 2026-08-05 | Stoeger *et al.* 2018, PMID 30226837 | pubmed MCP metadata | ✅ killed C2 |
| 2026-08-05 | ChEMBL 2023, *NAR* 52(D1):D1180 | WebFetch | ✅ verified the 154 figure |
| 2026-08-05 | 8 adversarial searches, one per candidate | WebSearch | ✅ killed A4, B1, B3, C3, D1, D2 |
