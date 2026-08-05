# 02b — Candidates, reopened without structural biology or metals

**Phase 2b.** Started 2026-08-05, after Phase 3 left only metal/structural survivors (E1, E2)
and Daniel asked for a search **excluding that territory**, open to anything in life science,
at E1's scale.

**The brief for this round.** Same size as E1 — one bounded dataset, small enough to finish,
narrow enough that no funded group bothered. No metals, no structural biology.

**Verification key:** ✅ verified by direct query · ⚠️ from a search snippet, needs checking ·
❓ unchecked.

---

## What Phase 3 taught, applied as search rules

Every one of the ten Phase 3 kills died the same way: **a funded group had already run the
question at a scale a laptop cannot reach.** So this round explicitly avoided:

- anything that *sounds* important (that is what attracts the group with 2,228 genomes)
- machine-learning-adjacent benchmarking (fast-moving, crowded, three papers a year)
- questions answerable by scaling up rather than by reading

and explicitly favoured: old, stable, curated resources; unglamorous questions; work whose
substance is **domain reading and adjudication** rather than modelling.

---

# R1 — Do curated biochemical databases still rest on retracted evidence? → **DEAD**

**The question.** MIBiG, M-CSA and DrugAge all advertise themselves as holding
*experimentally validated* knowledge, and each entry cites the primary literature that
validates it. Some of that literature has since been retracted. Do the annotations survive?

**Why it looked good.** Retraction *citation* is heavily studied — 57% of citations to
retracted infectious-disease papers occur after retraction ⚠️, the VITALITY study covers
trials, and there is work on retracted papers persisting on Wikipedia ⚠️. But the literature
explicitly notes that *"further work is needed to determine how retraction metadata
propagates"* ⚠️, and searches for retraction handling in UniProt/ChEMBL/BRENDA returned
nothing. Unglamorous, mechanical, nobody's incentive.

**DATA CHECK ✅ — FAILED, decisively, in one sitting.**
`scripts/check_retraction_feasibility.py`. Retraction status taken from **PubMed's own
`Retracted Publication[Publication Type]` flag** — a citable source needing no personal data
in a query string. All 33,627 records retrieved (100% coverage, partitioned by publication
year because esearch will not page past position 10,000).

| Resource | Entries with PMIDs | Unique PMIDs cited | Retracted | Affected entries |
|---|---|---|---|---|
| MIBiG 4.0 | 2,541 | 3,373 | **0** | 0 |
| DrugAge | 1,335 | 664 | **0** | 0 |
| M-CSA | 1,000 | 4,716 | **1** (PMID 10932255) | 1 (entry 626) |

**One hit in 8,753 cited references.** There is no project here.

> [!note] Why the null is real rather than a bug, and what it means
> Retractions concentrate in clinical research and in paper mills — note the **7,014 in 2022
> alone**, largely mass retractions. These databases cite classical experimental biochemistry,
> natural-product chemistry and enzymology, which barely intersects that corpus.
>
> So the honest finding is: **the curated biochemical core is essentially uncontaminated by
> retracted literature.** That is worth one paragraph and one table. It is not worth eight
> weeks, and pretending otherwise would fail the rule that killed the orphan-enzyme census.

**Could it be rescued by scale?** Running the same intersection over all of Swiss-Prot would
find hundreds of hits — but that makes it bigger, more likely already done, and removes the
thing that made it attractive (a handful of cases you can actually adjudicate). Not pursued.

---

# The rest of the slate — generated, not yet tested

**Status: none of these has passed a data check.** They are recorded so the reasoning is
auditable, not because they are recommended. Ranked by how much of the question survives what
is already known.

---

### R2 — The measurement noise floor under antimicrobial peptide activity

**Question.** DBAASP holds ~105,547 MIC measurements over 16,408 peptides and 5,630 strains ⚠️.
When the *same* peptide is tested against the *same* strain by different groups, how far apart
are the answers — and is that spread larger than the error of the models being trained on it?

**The template exists and is published.** Kroll *et al.* did exactly this for enzyme turnover
numbers: *"a single measurement deviates on average 3.3-fold from the geometric mean of all
available measurements for the same enzyme-reaction pair, while predicted kcat values deviate
5.1-fold"* ⚠️ — i.e. the predictors sit at or below the experimental noise ceiling. That
analysis has not obviously been run for AMPs.

**Threats, and they are serious.** Three benchmarking papers appeared in 2026 alone —
BATTLE-AMP, QMAP and AMPBench-MT ⚠️ — plus a 2022 *Briefings in Bioinformatics* paper on
biased negative-data selection. A field with three benchmarks a year is one where somebody
computes the noise ceiling next, if they have not already put it in a supplementary figure.

**DATA SHAPE ✅ — CONFIRMED, and it is better than expected.** Daniel supplied the API schema.
Each peptide carries a `targetActivities` array in which **every individual measurement has its
own `reference`**, alongside the assay conditions:

```
targetActivities[]: targetSpecies, activityMeasureGroup (MIC/MIC50/…),
                    concentration, unit, ph, ionicStrength, saltType,
                    medium, cfu, cfuGroup, note, reference
```

So the same peptide × same species can be traced to *different papers*, **and** the recorded
conditions are available as explanatory variables. That upgrades the question from "how noisy
is it?" to the sharper: **is the disagreement explained by the recorded assay conditions —
salt, medium, inoculum — or is it unexplained?** Clean null, interesting either way.

**ACCESS ❌ STILL BLOCKED.** Every endpoint tried returns HTTP 200 with `Content-Length: 0`
(headers show a Spring Security stack; not user-agent filtering — a browser UA behaves
identically). The schema proves the API exists; the working URL is still unknown.

**Threat assessment has worsened, though.** Given what the *npj Aging* team did to DrugAge
(see R6), a field with **three benchmark papers in 2026** is not somewhere to expect an
unoccupied question. R2's expected value is now low even if access is solved.

---

### R3 — How much phage–host interaction data is actually experimental?

**Question.** Models predicting which bacterium a phage infects are trained on interaction
databases. But *"host range datasets used to feed machine learning models are often inferred
from predictions and do not always represent lab-confirmed interactions"* ⚠️. What fraction is
experimentally confirmed — and does model ranking change when you restrict to the confirmed
subset?

**Why it fits Daniel specifically.** This is the [[LDLR VUS Project]] lesson stated as a
research question: *benchmarking against database labels rather than measurements can certify a
model that does not track reality.* He has already been burned by exactly this.

**A gold standard exists.** The **Viral Host Range database** (Lamy-Besnier *et al.*,
*Bioinformatics* 2021, 37(17):2798) records *experimental* host range specifically ⚠️, with
source code on the Institut Pasteur GitLab. So the confirmed-only subset is obtainable
separately from the mixed training corpora.

**Threat.** *"From genomic signals to prediction tools: a critical feature analysis and
rigorous benchmark for phage–host prediction"*, *Brief Bioinform* 2025, 26(6):bbaf626 ⚠️ —
must be read in full before this goes further. Figures, not abstract.

**DATA CHECK ❓.**

---

### R4 — How much of the viral AMG record rests on categories the field's own experts doubt? → **ALIVE, and the strongest candidate Phase 2b has produced**

**The framing paper, read in full.** Martin *et al.* (2025), *A call for caution in the
biological interpretation of viral auxiliary metabolic genes*, ***Nature Microbiology***.
PMID 40866482, [doi:10.1038/s41564-025-02095-4](https://doi.org/10.1038/s41564-025-02095-4).
Open-repository copy fetched; local text `refs/martin_2025_avg_caution.txt` ✅.

They argue the rush to catalogue AMGs has produced *"an epidemic of misannotation"*, and they
**name the suspects explicitly**:

> *"Two genes that seem inappropriately included in current AMG annotation databases of both
> VIBRANT and DRAM-v are **dcm** and **queC**."*

plus `queDEF`, glycoside hydrolases (*"we encourage researchers to carefully consider what
claims are supported by a GH annotation from a CAZyme-focused database like dbCAN2"*), folate
biosynthesis genes, and the DsrC/TusE pair — which *"current HMMs do not distinguish"* despite
completely distinct functions.

**They quantify nothing.** No rate, no count, no survey. The paper is a Perspective: argument,
examples, and a proposed framework.

**NOVELTY CHECK ✅ — survived the strongest available threat.** *Expanding standards in
viromics*, *PeerJ* 2021 9:e11447, [PMC8210812](https://pmc.ncbi.nlm.nih.gov/articles/PMC8210812)
evaluates AMG curation — but it tests **whether the tools correctly flag genes on viral
contigs**, not whether the gene categories in the AMG databases belong there. It raises the
same worry and explicitly declines to resolve it: *"some genes currently described in the
literature as AMGs might not be legitimate AMGs"* — **without systematically cataloguing which
ones.**

> [!important] Two independent papers, four years apart, say the same thing and neither counts
> 2021 (*PeerJ*): "some of these probably aren't AMGs" — not catalogued.
> 2025 (*Nature Microbiology*): names them — not counted.
> That is about as clean a gap signal as this project has found.

**DATA CHECK ✅ PASSED — total data footprint ~44 KB.** `scripts/amg_database_audit.py`.
The AMG definitions of both standard tools are public, machine-readable and tiny.

```
VIBRANT AMG database : 2,826 KEGG KO accessions
DRAM AMG database    :   279 rows (257 PFAM-keyed, only 37 with a KO)
```

**Every named suspect is present in VIBRANT's database**, verified by joining to the KEGG
orthology list rather than guessing accessions:

| Martin *et al.* suspect | KOs in VIBRANT | example |
|---|---|---|
| `dcm` DNA cytosine methyltransferase | 1 | K00558 |
| `queC/D/E/F` queuosine biosynthesis | 5 | K06920 `queC` |
| `dsrC` / `tusE` | 1 | **K11179 `tusE, dsrC`** |
| folate / one-carbon | 23 | K00287 `folA` |
| glycoside hydrolases | 17 | K01183 chitinase |
| glycosyltransferases | 6 | K04478 `sgtB` |
| **total** | **53 (1.9% of the database)** | |

> [!note] K11179 is the whole argument in one accession
> Martin *et al.* say DsrC and TusE do completely different things but HMMs cannot tell them
> apart. **KEGG has merged them into a single orthology group, named `tusE, dsrC`** — so the
> annotation system is structurally incapable of making the distinction they say matters, and
> that entry sits in the AMG list.

**A second, unlooked-for finding.** DRAM ships `verified` and `reference` columns in its AMG
database and answers the provenance question about itself:

```
verified = TRUE  :  17
verified = FALSE : 262   (94% of its own AMG database)
references       : 231 of 279 entries trace to a single paper (Roux et al. 2016)
```

**An error I caught before reporting it.** A first pass compared "AMG entry counts" between the
two tools and produced an arresting 83-fold difference. That was **an artefact of namespace
mismatch** — VIBRANT keys on KEGG KO, DRAM keys on PFAM, and 242 of DRAM's 279 rows carry no KO
at all. The figure is withdrawn. What survives is the more interesting statement: **the field's
two standard AMG tools do not share an identifier system**, so their outputs are not directly
comparable.

### Where the project actually is

1.9% of database *entries* is not an epidemic. **But database composition is not record
composition** — one abundant glycoside hydrolase KO may be called thousands of times while
hundreds of obscure KOs are never hit. So the real question is:

> **What fraction of AMG calls in published catalogues fall into the categories Martin *et al.*
> say should not count — and does excluding them change any published conclusion?**

**Why this is a project and not a figure.** The enumeration above took an hour. The work is the
**adjudication**: deciding, gene family by gene family, whether an enzyme is plausibly auxiliary
(manipulating host metabolism) or essential to viral replication. That is metabolic
biochemistry — nucleotide biosynthesis, one-carbon pools, cofactor chemistry, cell-surface
polysaccharides — and it is the part no script can do.

**Honest weaknesses, stated now.**
- *Partly definitional.* "What counts as an AMG" is an argument, not only a measurement. The
  defence is to adopt **Martin et al.'s stated criteria as a pre-registered rubric** rather than
  inventing one — the analysis then measures the consequence of an authoritative published
  position, not a personal opinion.
- *Timing risk.* The Perspective is ~1 year old. Its own authors are the obvious people to run
  this, and they have the field's attention.
### The outstanding data check, run — and the answer is large

**Source.** *Virus-encoded auxiliary metabolic genes throughout the global oceans*, *Microbiome*
2024, [doi:10.1186/s40168-024-01876-z](https://doi.org/10.1186/s40168-024-01876-z);
supplementary workbook from Zenodo [10.5281/zenodo.12668289](https://doi.org/10.5281/zenodo.12668289),
`GlobalAMGs_SOM.xlsx`, 114 MB ✅. Raw DRAM-v output, one row per AMG call.
`scripts/amg_record_composition.py`. Suspect patterns copied **unchanged** from the earlier
script, which was written before this file was downloaded — the rubric was not tuned to the
result.

| | Permissive (pre-curation) | **Conservative (their curated catalogue)** |
|---|---|---|
| AMG calls | 255,859 | **88,729** |
| with a KEGG KO | 99,822 (39.0%) | 31,772 (35.8%) |
| **calls in a Martin-named suspect category** | 13,358 | **7,969** |
| **as % of KO-assigned calls** | 13.4% | **25.1%** |
| as % of all calls | 5.2% | 9.0% |

**A quarter of all KO-assigned AMG calls in the curated catalogue fall into categories the
field's own experts say should probably not count.**

**And essentially all of it is the two genes Martin *et al.* named explicitly:**

| | calls | verified accessions |
|---|---|---|
| `dcm` DNA cytosine methyltransferase | **5,797** | all K00558 ✅ |
| queuosine biosynthesis | **2,156** | K01737 `queD` (1,206), K06920 `queC` (626), K06879/K09457 `queF` (324) ✅ |
| everything else | 16 | — |

Their sentence was: *"Two genes that seem inappropriately included in current AMG annotation
databases of both VIBRANT and DRAM-v are **dcm** and **queC**."* Those two account for
**7,953 of 7,969** suspect calls.

> [!important] The unexpected result — curation makes it worse, not better
> Going from the permissive to the conservative catalogue, the suspect share of KO-assigned
> calls **rises from 13.4% to 25.1%**.
>
> Retention rates explain it. Overall KO-assigned calls: 99,822 → 31,772 (**32% retained**).
> `dcm`: 8,543 → 5,797 (**68% retained**) — more than double the overall rate.
>
> Curation strips low-confidence and unannotated calls, and `dcm` is a confident, unambiguous
> KEGG hit. **The conservatism intended to raise quality preferentially preserves exactly the
> category under dispute.** That is a specific, checkable, and slightly uncomfortable claim.

**Verification done, not assumed.** Every `dcm` call was confirmed to be K00558, and the
underlying `kegg_hit` strings read *"cytosine-specific methyltransferase"*, *"DNA-cytosine
methyltransferase"*. No regex false positives. This check was run precisely because the
previous headline number in this project turned out to be an artefact.

**Caveats that must be carried forward.**
- Only ~36% of calls carry a KO at all, so **"25.1% of KO-assigned" is not "25.1% of the
  record"** — as a share of all calls it is 9.0%. Both numbers must always be reported together.
- The free-text matching route gives much smaller numbers (1.1%) and is indicative only. The
  two routes must not be merged.
- Whether the authors themselves treat `dcm` as a headline AMG, or merely list it, needs
  checking against their text ❓. A reviewer will ask.

**Verdict: DATA CHECK ✅ PASSED, decisively. R4 is the recommended candidate** and should go
into Phase 4 (feasibility) and Phase 5 (red team) ahead of E1.

---

### R3 — How much phage–host interaction data is actually experimental? → **ALIVE, awkward**

**NOVELTY CHECK ✅ — the gap is stated by the people best placed to close it.** The most
rigorous benchmark in the field (*Brief Bioinform* 2025, 26(6):bbaf626 — 27 tools, two purpose-
built datasets) **does not distinguish experimentally confirmed from computationally inferred
host assignments**, and says so: their framework *"is constrained by public databases that
document one-to-one virus–host associations"* ✅. They did not restrict testing to validated
interactions.

**DATA CHECK ⚠️ — awkward.** The Viral Host Range database (Lamy-Besnier *et al.*,
*Bioinformatics* 2021) is **live** — most recent entry 27 May 2026 ✅ — but has **no documented
bulk download or API**, and its TLS certificate fails validation from a plain Python client.
Extraction would be laborious.

**Standing:** genuinely open, but R4 is better on every axis — smaller data, cleaner access, a
sharper framing citation, and more biochemistry.

---

### R5 — What does transporter substrate annotation actually rest on?

**Question.** *"~30% of the 446 human SLCs were still functionally orphan and lacked known
substrates"* ⚠️, and in GO *"the vast majority [of entries have] only electronic evidence and
[are] not manually curated"* ⚠️. A 2024 paper is titled *Transporter annotations are holding up
progress in metabolic modeling* ⚠️. Meanwhile SPOT and similar models predict transporter
substrates — trained on what?

**Attraction.** Evidence codes are machine-readable, so the audit is one query. **That is also
the problem** — if one query answers it, it is a figure. The project would have to be the
adjudication of a chosen subset.

**Note.** SLC structural classification was already killed in Phase 1 (Ferrada &
Superti-Furga 2022). This is a different question about the same family — which is a caution,
not a disqualification.

**DATA CHECK ❓.**

---

### R6 — Do published lifespan-extension claims survive multi-laboratory testing? → **DEAD**

**Killed by:** Parish A, **Ioannidis JPA**, Zhang K, Barardo D, Swindell WR & de Magalhães JP
(2025), *Reporting quality, effect sizes, and biases for aging interventions: a methodological
appraisal of the DrugAge database*, *npj Aging* 11:96,
[doi:10.1038/s41514-025-00287-0](https://doi.org/10.1038/s41514-025-00287-0). Full text
fetched by Daniel; local copy `refs/drugage_appraisal_2025.txt` ✅.

**They did all of it, and then some.** 667 studies / 720 experiments:

| Their analysis | Effect on R6 |
|---|---|
| CAMARADES quality scoring across 8 components — randomization 19.9%, blinded intervention 4.0%, sample-size calculation 6.0% | The quality audit is theirs |
| Random-effects meta-analysis of standardised mean differences: 0.57 (95% CI 0.48–0.66), **I² = 95%** | The effect-size synthesis is theirs |
| **35 compounds tested in both mammals and non-mammals.** Of 21 significant in non-mammals, **only 7 were also significant in mammals**; 2 showed a significant *decrease* (quercetin, butylated hydroxytoluene) | **This is the replication-concordance question.** Already answered |
| Absolute percent error between non-mammal and mammal effects: **83% (IQR 49–164%)**; no significant correlation between them (r = 0.26, p = 0.10) | The discordance is quantified |
| Publication bias: **Egger's Z = 11.3, p < 0.0001**; test of excess significance χ² = 14.0, p < 0.0001 (546 significant observed vs 499 expected) | The bias probe is theirs |
| Trends over time in every component | Also theirs |

**Note the author list.** Ioannidis wrote *Why Most Published Research Findings Are False* and
runs Stanford's meta-research centre. This is a professional meta-research team working the
exact territory R6 proposed to enter, with the exact database, published within the last year.

**Read this as a general warning, not just one kill.** "Audit the evidence quality of database
X" is not an unoccupied niche — it is a discipline with its own methods (CAMARADES), its own
journals and its own experts. Any future candidate of that shape must first check whether a
meta-research group has already been through it.

*(Previous verdict, retained for the record: WOUNDED before testing, because CITP deliberately
de-prioritised compounds already in DrugAge, so the overlap was small by design.)*

### R6 — original framing, superseded

**Question.** DrugAge holds 3,423 lifespan experiments from 680 studies ⚠️. The
**Caenorhabditis Intervention Testing Program** re-tests compounds across three labs, multiple
strains and two species — >75 compounds, >725,000 animal assays, 891 trials as of Dec 2024 ⚠️.
Of the published claims CITP re-tested, how many held?

**Why it is wounded already.** CITP *"used the DrugAge database to de-prioritize compounds that
had already been published to extend C. elegans lifespan, to avoid duplicative research
efforts"* ⚠️. **The overlap is small by design.** The comparison is gutted before it starts —
a data check failing in advance.

**What might remain.** CITP has published outright negatives (tamibarotene and bakuchiol do not
extend lifespan ⚠️). The overlap set may be ~10–20 compounds — E1-sized. But it is a biased
sample and would have to be presented as a case series, not a rate.

**Also outstanding:** *npj Aging* 2025 published *Reporting quality, effect sizes, and biases
for aging interventions: a methodological appraisal of the DrugAge database* ❓ — **paywalled,
fetch blocked by a Nature IDP redirect.** Must be read before R6 goes anywhere.

---

### R7 — How far apart are reported enzyme optima? → **partly done**

BRENDA holds pH and temperature optima from many independent studies. Reported: **96 enzymes
have T_opt standard deviations greater than 5°C** ⚠️ — so somebody has already quantified the
spread, and Seq2Topt already predicts T_opt ⚠️. Retained only to record that it was considered.

---

### R8 — Re-examining horizontal gene transfer claims in an untouched clade → **not recommended**

The re-examination has been done for plants (**only 29.3% of previously reported interkingdom
HGT cases survived reanalysis** ⚠️) and for the human genome ⚠️. Extending it to a clade nobody
covered is the *unfilled-cell-in-someone-else's-table* pattern — the weakest novelty class on
the brief's own list. Recorded and set aside.

---

## Dead on arrival this round

| Direction | Killed by |
|---|---|
| Thermodynamic (Haldane) consistency audit of enzyme kinetics | *Auditing Haldane Consistency in Reversible Enzyme Kinetics*, arXiv 2607.02784 ⚠️ |
| Contradictions in glycan NMR assignments | CSDB remediation: 244 publications, **272 provable contradictions** already catalogued ⚠️ |
| Mass/charge balance errors in pathway databases | Standard QC — MetRxn, MNXref, BKM-react, memote ⚠️ |
| Tox21/ToxCast replicate reproducibility | Computed in-house: 17/30 assays grade A, <2-fold AC50 spread ⚠️ |
| Cross-database subcellular localisation disagreement | Quantified; plus CAPSUL and a *Nat Methods* 2026 benchmark ⚠️ |
| Model organism database curation accuracy | Measured: 10 errors in 633 validated facts (1.58%) ⚠️ |
| AMR database concordance | Already dead in Phase 3 |

---

> [!warning] A shape monoculture, caught before it became another anchoring failure
> R1–R5 and R7 are **all data-quality / provenance / disagreement questions.** That is the same
> mistake as v1's metal concentration, on a different axis: one idea wearing six hats. If the
> "audit the record" shape turns out to be crowded — and the Haldane, glycan-NMR and AMR
> results suggest it is being actively worked — most of this list dies together.
>
> **Any continuation of Phase 2b must deliberately generate candidates of other shapes**:
> comparative questions across a clade, an assumption inside a widely used protocol, a known
> method applied to an untouched dataset. Noted here rather than discovered later.

## Provenance

| Date | Source | Method | Status |
|---|---|---|---|
| 2026-08-05 | ~30 exploratory web searches across 12 life-science areas | WebSearch | ✅ |
| 2026-08-05 | MIBiG 4.0, DrugAge, M-CSA | direct download / API | ✅ all live, <1 MB each |
| 2026-08-05 | PubMed `Retracted Publication[pt]`, 33,627 records | E-utilities, year-partitioned | ✅ 100% retrieved |
| 2026-08-05 | intersection of the above | `scripts/check_retraction_feasibility.py` | ✅ **R1 dead** |
| 2026-08-05 | DBAASP REST API | direct query | ❌ 200 with empty body, endpoint unknown |
| 2026-08-05 | *npj Aging* DrugAge appraisal | WebFetch | ❌ blocked by Nature IDP redirect |
