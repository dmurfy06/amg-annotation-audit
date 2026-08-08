# Adjudicating the viral auxiliary metabolic gene record: disputed families cancel in comparisons and persist in descriptions

**Daniel Murphy**
*Undergraduate, Biochemistry. Independent research.*

**Status:** draft, 8 August 2026. Numbers are final; prose is not.
All analysis code and intermediate results: https://github.com/dmurfy06/amg-annotation-audit

---

## Abstract

Viruses of bacteria carry genes that resemble host metabolic enzymes. These are routinely
catalogued as auxiliary metabolic genes (AMGs) and read as evidence that viruses reprogram
host metabolism. A 2025 commentary argued that several of the most frequently counted
categories are more plausibly performing viral functions — genome protection, nucleotide
provisioning, receptor modification — and named specific suspects without quantifying them.
We quantify them.

We harmonised three published AMG catalogues spanning ocean, soil and wastewater
(93,413 calls, three annotation pipelines, three independent research groups), matched gene
families by database accession rather than free text, and adjudicated 35 gene families
against a pre-registered two-part rule with a six-tier evidence hierarchy. The rule was
deliberately biased against our own hypothesis: families default to counting, and chemical
plausibility alone can never rule one out.

Twenty-eight of 35 families survive adjudication. Four are ruled out and three are
unresolvable. **Eight of 35 have no phage-specific experimental evidence of any kind**, yet
support published claims. Under the strictest pre-registered rule, 28.5% of the curated
ocean AMG record, 11.9% of soil and 37.7% of wastewater falls in families that do not
support the inference drawn from them — but this figure is carried almost entirely by
families that are *unresolvable* rather than refuted, and in the ocean the strict-rule
result reduces to a single family (`dcm`, 99.6% of excluded calls).

Testing the consequence on published claims, the effect is strongly claim-dependent. A
wastewater catalogue's headline compositional claim does not survive: the genes it names as
most common are the disputed family. An ocean prevalence estimate moves modestly (19% to
16.9%). A soil comparative claim across a contamination gradient is entirely unaffected.
**Disputed families cancel in comparisons and persist in descriptions.** Comparative AMG
claims are largely robust; the more specific a descriptive claim, the more of it rests on
families the current evidence cannot adjudicate.

None of the three catalogues did anything the field would regard as incorrect. They applied
the standard category. The problem is in the category.

---

## 1. Introduction

Bacteriophages carry genes with unmistakable homology to bacterial metabolic enzymes. The
canonical example is `psbA`, the photosystem II reaction centre protein, carried and
expressed by marine cyanophages during infection [CITE: Mann 2003 / Lindell 2005 — verify].
Such genes are interpreted as **auxiliary metabolic genes**: virus-encoded functions that
sustain or redirect host metabolism through infection, with consequences that scale to
biogeochemical cycling.

For `psbA` the interpretation is well supported. A phage that keeps photosynthesis running
in a cell it is consuming is doing something the host would recognise as its own metabolism,
and the fitness rationale — maintaining the energy supply the phage is drawing on — is clear.

The inference has since been generalised well beyond that case. Annotation pipelines assign
AMG status semi-automatically; catalogues are published at the scale of tens of thousands of
calls; and those counts underwrite claims about viral contributions to carbon, nitrogen,
sulfur and phosphorus cycling across every sampled environment. The category has become
infrastructure.

Martin *et al.* (2025, *Nature Microbiology*, doi:10.1038/s41564-025-02095-4) argue that a
substantial part of what the infrastructure has accumulated is misread. Several of the most
frequently counted families have direct, well-documented viral functions:

- **DNA cytosine methyltransferases** (`dcm`) modify the phage's own genome, evading host
  restriction — genome protection, not host metabolism.
- **Queuosine biosynthesis** enzymes make 7-deazaguanine derivatives that have been detected
  *in phage DNA*, where the attributed function is protection from host endonucleases
  (Thiaville *et al.* 2016, doi:10.1073/pnas.1518570113; Hutinet *et al.* 2016,
  doi:10.1080/15476286.2016.1265200).
- **Glycoside hydrolases** include virion-associated lysins that breach the cell wall during
  entry; one was found bound to the phage baseplate and proposed to facilitate genome
  injection (Yuan & Gao 2016, doi:10.3389/fmicb.2016.00745).
- **Folate and one-carbon** enzymes feed nucleotide biosynthesis, which during infection is
  supplying the phage genome.

The general form of the objection is that a gene can act on a host molecule and still be
performing a discrete step of the viral lifecycle rather than sustaining host metabolism —
and that the AMG category, as applied, does not distinguish the two.

Martin *et al.* name the suspects. They do not count them, and a 2021 standards paper raising
the same concern explicitly declined to catalogue it [CITE: PeerJ 2021 — verify]. **How much
of the AMG record actually rests on contested families has never been measured.**

That is the gap. It matters because the answer is not obvious in either direction: the
contested families could be a rounding error, or they could be most of the record, and the
published literature is compatible with both. It also matters that the question is answerable
without new experiments — the catalogues, the annotations and the primary phage literature
are all public.

This study asks three questions in order:

1. **How much of the published record sits in contested families?** We harmonise three
   independent catalogues and match families by database accession rather than free text
   (§2.2, §3.1).
2. **Do the catalogues apply their own stated inclusion criteria?** This is deliberately
   independent of Martin *et al.*'s rubric, and so cannot be dismissed as choosing a
   convenient standard (§3.2).
3. **Which families withstand scrutiny on the published evidence, and does removing the rest
   change anything anyone has claimed?** (§3.3–3.6).

The third question is the one that determines whether any of this matters. A labelling
problem that changes no published conclusion is a curiosity; one that changes conclusions
selectively, in a predictable direction, is a methodological finding. We find the latter.

> **A note on what this study is and is not.** Every verdict here is a judgement about the
> most parsimonious reading of a gene *family* on currently published evidence. It is
> defeasible, it is not a claim about any individual gene call, and it is not a claim that
> anyone's annotation is incorrect. The protocol was pre-registered, deliberately biased
> against the hypothesis motivating the study, and its abundance data sealed before any
> verdict existed, precisely because the author had an obvious interest in a particular
> answer.

---

## 2. Methods

### 2.1 Catalogues

Three published AMG catalogues, chosen for independence of environment, pipeline and
research group:

| Catalogue | Environment | Pipeline | Calls | KO-assigned |
|---|---|---|---|---|
| Microbiome 2024 | Global ocean (*Tara*) | DRAM-v | 88,729 | 31,772 |
| ISME J 2022 | Soil, organochlorine gradient | VIBRANT + DRAM-v | 4,583 | 1,151 |
| ES&T 2023 | Wastewater activated sludge | kofamscan + hmmsearch | 101 | 77 |

The ocean catalogue is additionally available pre-curation (255,859 calls), which permits a
direct test of whether curation enriches or depletes contested families.

### 2.2 Accession-based family matching (Amendment 1)

Gene families were initially identified by text-matching annotation descriptions. **This was
wrong and the results it produced are void.** Databases spell the same function differently
("glycosyltransferase" vs "Glycosyl transferases group 1"), so text matching under-counted
by up to ninefold in the soil catalogue.

All matching is now by **database accession** (KEGG KO, Pfam PF), which cannot be misspelled.
The frozen accession list is `data/family_accessions.tsv`. Every accession was reviewed by
hand and carries a status:

- **INCLUDED** (72) — the accession denotes the family's activity.
- **AMBIGUOUS** (6) — `folE`, `folE2`, `queD` and relatives sit at the branch point shared by
  folate and queuosine biosynthesis. Reported both ways throughout; this single ambiguity
  moves the wastewater result by 18 percentage points.
- **EXCLUDED** (2) — matched in error and removed.

The two exclusions matter enough to state explicitly:

- **`PF13385`** — "Concanavalin A-like lectin/glucanases superfamily" — is a **structural
  fold, not an activity**. Concanavalin A binds sugars; it does not hydrolyse them. This
  accession alone was 21,567 of the glycoside hydrolase family's 21,690 calls (99.4%), matched
  solely on the substring "glucanases".
- **`K14652`** (`ribBA`) is GTP cyclohydrolase **II** — riboflavin biosynthesis. Folate and
  queuosine use GTP cyclohydrolase **I**. Matched on the shared string "GTP cyclohydrolase".

Both errors inflated our own hypothesis. Removing them reduced the headline. We report this
because the direction is informative: the largest single correction in this study made the
result smaller.

### 2.3 The adjudication rule (pre-registered)

Full protocol: `08_adjudication_protocol.md`, committed before any verdict existed.

A family **counts** as an AMG only if **both**:

1. **Substrate** — the gene product acts on a **host** molecule; and
2. **Consequence** — the effect is to **sustain or redirect host metabolism**, rather than to
   serve a discrete step of the viral lifecycle (entry, genome protection, replication,
   assembly, egress).

Three design choices deliberately bias the protocol *against* the hypothesis this study
exists to test:

- **The default verdict is COUNTS.** A family leaves the record only on positive evidence.
- **Tier 6 evidence (chemical plausibility alone) can never rule a family out.** Tier 6 is
  essentially what Martin *et al.* offer; permitting it to decide would restate their argument
  rather than test it.
- **UNRESOLVABLE requires naming the experiment that would settle it.** A family with no
  evidence at all is *unresearched*, not unresolvable, and defaults to COUNTS. Collapsing
  those two states would inflate the disputed share on the basis of nobody having done an
  experiment — the exact information loss this paper criticises.

**Evidence tiers.** 1: gene knocked out of a phage and effect measured. 2: the phage's own
protein purified or structured and substrate shown. 3: expression timing across infection.
4: consistent genomic context among structural/replication genes. 5: informative divergence
from host copies. 6: chemistry alone.

**Family selection.** A family was adjudicated if it accounted for ≥1% of KO-assigned AMG
calls *and* ≥10 calls in any catalogue, or was named by Martin *et al.* The ≥10 floor
(Amendment 2) prevents the percentage threshold from becoming degenerate in the 77-call
wastewater catalogue; it removes 18 families accounting for 3.1 percentage points, which are
counted in aggregate as COUNTS. No control was removed by this amendment.

**Controls.** `psbA`/`psbD` must return COUNTS; `xtmA`/`xtmB`/`dcm` must return DOES NOT
COUNT. All five returned correctly. **These controls are not blind** — the protocol names
them — so they test whether the rule, faithfully applied, reproduces distinctions the field
already accepts. They do not test rater impartiality, and we do not claim they do.

**Sealed counts.** Per-family abundance was computed and committed to
`data/adjudication_counts_SEALED.tsv` *before any verdict existed*, and opened only after all
35 verdicts were recorded and the controls checked. No verdict can have been fitted to the
counts it would move.

### 2.4 Reporting rules (pre-registered)

The disputed share is reported under four rules, always together:

| Rule | Treatment |
|---|---|
| **Inclusive** | Current field practice; nothing excluded |
| **Strict** | DOES NOT COUNT excluded; UNRESOLVABLE retained |
| **Maximally strict** | DOES NOT COUNT *and* UNRESOLVABLE excluded |
| **Confidence-limited** | Only high-confidence DOES NOT COUNT excluded |

All proportions carry Wilson score intervals. The spread between rules is a headline result,
not a footnote: no reader has to accept our verdicts to use our numbers.

### 2.5 Rater independence — a limitation stated in the methods, not the discussion

The first adjudication pass was produced with AI assistance (Claude, Anthropic). A second
pass was then conducted by the author on the 12 families where evidentiary judgement was
actually required; the remaining 23 were resolved mechanically by the protocol (no Tier 1–5
evidence exists, so the family cannot be ruled out), where two raters must agree by
construction and measuring agreement would inflate the figure while testing nothing.

The second pass worked from evidence extracts with all verdicts, tier assessments and
resolving experiments programmatically removed (build script and leak checks:
`scripts/build_blind_concordance_sheet.py`).

**Agreement: 12/12 verdict, 12/12 confidence, 11/12 evidence tier.**

**Independence could not be verified.** The first-pass file remained accessible to the second
rater during rating, contrary to protocol. Text-similarity analysis does not indicate
copying — every content word in the second rater's free text appears in the supplied evidence
extracts, which is sufficient to explain the overlap, and the single tier disagreement is not
consistent with transcription. We nonetheless report this as a **rubric-application check
with independence unverified**, and **do not present κ as an inter-rater reliability
statistic for this study.** A genuine reliability figure requires a second human rater
working from the blind materials alone, and we did not obtain one.

---

## 3. Results

### 3.1 A DRAM-v flag that looked like a fatal objection, and was not

68% of `dcm` calls — the largest contested family — carry DRAM-v's `F` flag. We established
from the DRAM-v source (`annotate_vgfs.py::get_metabolic_flags`, `length_from_end=5000`) that
`F` means *the gene lies within 5,000 bp of a contig end*: a positional property, not a
biological one, and a plausible marker of unreliable assembly.

The obvious objection is that contested families are assembly artefacts. They are not.

| Stratum | n | % F-flagged [95% CI] |
|---|---|---|
| **Baseline — all AMG calls** | 88,729 | **79.1% [78.9–79.4]** |
| Baseline — KO-assigned only | 31,772 | 75.8% [75.3–76.3] |
| `dcm` | 5,797 | 68.0% [66.8–69.2] |
| Queuosine biosynthesis | 2,156 | 74.8% [72.9–76.6] |
| **All contested families combined** | 7,969 | **69.9% [68.8–70.9]** |

Contested families are **better** placed than the catalogue average, with non-overlapping
intervals. A proportion without its denominator is not a finding; computing the baseline
converted a threat into a ruled-out confounder.

Two further flags are worth reporting: `V` (viral replication/structure category) and `T`
(transposon) occur **zero times** in the curated catalogue, confirming the published
exclusions were applied.

### 3.2 The catalogues mostly cannot break their own rules

We tested each catalogue against **its own stated inclusion criteria**, using its own
annotation database. Martin *et al.* are not used in this analysis at all. This defeats the
objection that we simply selected a rubric that produces the answer we wanted.

**Ocean — the rule is enforceable, and enforced.** The catalogue states it excludes AMGs on
contigs carrying lipopolysaccharide-island genes including glycosyltransferases. Between the
permissive and conservative releases, glycosyltransferase calls fall from **30,483 to 2**
(99.993% removed) and all 762 transposon-flagged calls are removed. This is a **negative
result** for our pre-registered hypothesis, and it is what makes the positive result credible:
the test can pass.

**Wastewater — the rule cannot be applied deterministically.** The catalogue states that genes
"directly involved in viral replication (e.g., replication, repair, nucleotide transport, and
metabolism) were not included". Using the authors' own KEGG annotation, **13.0% [7.2–22.3] of
KO-assigned calls sit in a category the rule excludes** — but **0.0% [0.0–4.8] sit in such a
category exclusively.** Every one is dual-classified: `purA` is both nucleotide metabolism
(excluded) and amino acid metabolism (permitted); `prsA` is both nucleotide (excluded) and
carbohydrate metabolism (permitted), and the authors present it as a carbon gene.

A rule that does not decide is not being enforced. It is being interpreted case by case,
invisibly, and no reader can reconstruct which reading was applied to which gene.

**Soil — the rule is not mechanically testable.** "Proteins involved in nutrient
transformation and pollutant degradation were defined as auxiliary metabolic genes" is a
positive definition in ordinary English. Deciding whether cell-surface polysaccharide
biosynthesis counts as "nutrient transformation" requires our judgement, so this is not an
internal-inconsistency result and we do not claim it as one.

> **A pre-registered prediction that failed.** We predicted the queuosine genes would violate
> the wastewater rule, since the authors themselves note those genes "could also participate
> in tRNA biogenesis". They do not trip the test: KEGG files queuosine biosynthesis under
> **folate biosynthesis (09108, cofactors and vitamins)**, not nucleotide metabolism. The genes
> that trip it are `purA` and `prsA`, and neither trips it cleanly. Reported as a failed
> prediction rather than quietly dropped.

**So: of three catalogues, one states a rule it can and does enforce, one states a rule that
cannot be enforced, and one states no mechanically testable rule at all.** AMG inclusion
criteria are mostly not the kind of thing anyone can check — which is precisely why the
record drifts.

### 3.3 Adjudication: most families survive

Of 35 families adjudicated:

| Verdict | n | Families |
|---|---|---|
| **COUNTS** | 28 | incl. `psbA`, `psbD`, `phoH`, `TALDO1`, `nrdH`, `dut`, `NAMPT`, all nucleotide-sugar precursors |
| **DOES NOT COUNT** | 4 | `dcm`, `glycoside_hydrolase`, `xtmA`, `xtmB` |
| **UNRESOLVABLE** | 3 | `dsrC_tusE`, `folate`, `queuosine` |

**The headline finding is not that the record is full of miscounted genes.** Four families in
35 are ruled out, three of which are protocol controls or near-zero in abundance. The
adjudication mostly *vindicates* the field's assignments at the family level.

**Eight of the 35 families have no phage-specific experimental evidence of any kind.** Nobody
has tested what the phage version of those genes does, in any system. Published claims rest
on them regardless. This is independent of any verdict and, we suggest, the most immediately
actionable result here: it is a research agenda, not a criticism.

`dsrC_tusE` deserves specific mention because it is an annotation failure rather than a
biological one. KEGG merges two functionally distinct proteins into one orthology group
literally named `tusE, dsrC` — one feeds tRNA thiolation, the other dissimilatory sulfite
reduction. Nothing in environmental data distinguishes them. The field's strongest
phage-sulfur paper writes `dsrC/tusE`, with a slash, inheriting the ambiguity in its own
notation.

### 3.4 The disputed share, and what carries it

| Rule | Ocean (curated) | Soil | Wastewater |
|---|---|---|---|
| Inclusive | 0% | 0% | 0% |
| **Strict** | **18.31% [17.89–18.74]** | 0.87% [0.47–1.59] | 0.00% [0.00–4.75] |
| **Maximally strict** | **28.47% [27.98–28.97]** | 11.90% [10.16–13.90] | **37.66% [27.67–48.83]** |
| Confidence-limited | 18.31% | 0.87% | 0.00% |

Two features of this table matter more than the point estimates.

**The confidence-limited rule is degenerate.** All four DOES NOT COUNT verdicts were recorded
at high confidence, making it identical to strict. A pre-registered analysis that turns out
degenerate is still reported; its degeneracy is a fact about the evidence base.

**The ocean strict result is one gene family.** `dcm` supplies **5,797 of 5,818 excluded ocean
calls (99.6%)**. Leave-one-out across all 35 families:

| Family held as COUNTS | Ocean strict becomes | Swing |
|---|---|---|
| `dcm` | **0.07%** | **18.25 pp** |
| `glycoside_hydrolase` | 18.25% | 0.07 pp |
| `xtmA`, `xtmB` | 18.31% | 0.00 pp |

Removing `dcm` collapses the strict result from 18.31% to 0.07%. Moreover, `dcm` is one of the
protocol's pre-specified worked examples: its verdict was fixed when the rules were written,
not when the evidence was weighed. **The ocean strict figure is therefore not an output of the
adjudication in the way the maximally-strict figure is**, and we do not present it as one.

The defensible headline is the maximally-strict row, where the load is distributed — `dcm`
18.25 pp, `queuosine` 6.79 pp, `folate` 3.35 pp — and where the families doing the work are
**unresolvable rather than refuted**. The honest statement of this study's central result is:

> The disputed mass of the AMG record sits in families that the current evidence base cannot
> adjudicate in either direction.

### 3.5 Abundance weighting covers only 5% of the record

The pre-registration commits to reporting call-weighted and abundance-weighted shares wherever
per-sample abundance exists. It exists for soil (9 samples, relative abundance) and wastewater
(RPKM per genome). **It does not exist for the ocean catalogue**, which publishes annotations
without the abundance table behind them — 88,729 of 93,413 calls, and the catalogue carrying
the strict-rule result. Abundance weighting is therefore impossible for 95% of this study.

Where it is possible, two analytical traps must be avoided, both of which produced incorrect
results in our first attempt:

**Abundance is published per virus, not per gene.** A virus carrying 27 AMGs repeats its
abundance on 27 rows. Naive summation over calls double-counts, and unevenly — it inflates
whichever group sits on gene-dense genomes. This artefact alone produced an apparent
strict-rule depletion of 0.58×, which **disappears entirely (0.99–1.01×) when each virus is
counted once.** There was no effect.

**Aggregate ratios are not family properties.** Under the maximally-strict rule the
abundance-weighted share genuinely is lower than the call-weighted share (soil 0.47–0.49×,
wastewater 0.36–0.37×). But the viruses carrying `folate` and `queuosine` sit at **0.92× and
0.90× of the overall median abundance** — that is, entirely typical. The aggregate gap is
driven by the heavy right skew of viral abundance: a small number of very abundant viruses
happen to carry nothing disputed, out of 539.

We therefore state only the narrow result: **abundance weighting lowers the disputed share in
both catalogues where it can be computed, but the families driving the dispute are carried by
viruses of ordinary abundance.** The stronger and more interesting claim — that disputed genes
sit preferentially on rare viruses — is not supported.

Direction of effect, declared: this cuts against our hypothesis.

### 3.6 Does any of this change a published claim?

One claim was taken from each catalogue's own abstract. All three were fixed before any was
recomputed.

**Wastewater — the claim does not survive.** The abstract states that of 101 vAMGs, "the most
common of which were the queuosine biosynthesis genes `folE`, `queD`, and `queE` and the sulfur
metabolism gene `cysH`". Those genes *are* the disputed family. Under the maximally-strict rule
**29 of 101 vAMGs (28.7%) are removed**, the named genes disappear entirely, and `cysH` inherits
the top of the list. We note additionally that the claim holds only in aggregate: no single
queuosine gene exceeds `cysH`'s 12 calls; the pathway reaches 27 only when its genes are summed.

**Ocean — the claim moves modestly.** "We estimate that ~19% of ocean virus populations carry
at least one AMG" becomes **17.4% (strict)** or **16.9% (maximally strict)**, a relative fall of
about 11%. Of 60,471 virus contigs carrying at least one AMG call, **4,945 qualify on the
strength of `dcm` alone.**

**Soil — the claim is unaffected.** "The diversity and relative abundance of AMGs significantly
increased along with the severity of pesticide contamination" holds under every rule:

| Rule | Abundance Heavy/Clean | Richness Heavy/Clean |
|---|---|---|
| As published | 1.25× | 2.54× |
| Strict | 1.25× | 2.54× |
| Maximally strict | 1.25× | 2.55× |

**The pattern is the result.** Disputed families are a roughly constant fraction across a
gradient, so they **cancel in comparisons** and **persist in descriptions**. A study asking
*"does AMG content differ between conditions?"* is largely robust to everything in this paper.
A study asking *"what are these viruses doing?"* is answering with families the evidence
cannot resolve — and the more specific the answer, the more of it rests on them.

Every recomputation reduces the published figure. None of the three claims is strengthened.

---

## 4. Discussion

### 4.1 The record is not broken, but it is unevenly load-bearing

Twenty-eight of 35 families survive adjudication under a protocol explicitly designed to make
exclusion difficult. Anyone expecting this study to show that the AMG literature is largely
artefact should read that as the primary result. At the level of families, the field's
assignments mostly hold.

What does not hold is the assumption that the record is uniformly reliable. Its exposure is
concentrated in a small number of families that happen to be very abundant, and — importantly —
those families are mostly **unresolvable rather than refuted**. `folate` and `queuosine` carry
the maximally-strict result in every catalogue. Neither can currently be assigned in either
direction: the queuosine pathway demonstrably serves tRNA modification *and* has been detected
modifying phage DNA, and the same enzymes do both. `folE` sits at the branch point feeding both
pathways, and which branch it feeds moves the wastewater result by 18 percentage points.

This is a different and more tractable problem than "the record is wrong". It localises the
uncertainty to a handful of specific, nameable biochemical questions.

### 4.2 Why the effect is claim-dependent, and how to use that

The most useful generalisation this study supports is structural rather than numerical:

> **Disputed families cancel in comparisons and persist in descriptions.**

The mechanism is straightforward. Contested families occur at a roughly constant rate across
the conditions a study compares, so they appear in both numerator and denominator of a ratio
and largely drop out. The soil contamination gradient is unchanged to two decimal places under
every rule. But those same families remain in any statement about what the record *is* — what
the most common vAMG is, what fraction of viruses carry one, which pathways viruses target —
because there is no second term for them to cancel against.

This gives readers a usable heuristic. A study comparing AMG content between treatments, sites,
depths or timepoints is largely robust to everything in this paper. A study describing what
viruses in an environment are doing is not, and the more specific the description, the less
robust it is. The wastewater case is the limiting example: a claim naming the queuosine genes
as the most common vAMGs cannot survive those genes being contested, because the claim's
subject and the contested family are the same object.

### 4.3 The criteria problem is upstream of the counting problem

Section 3.2 is, on reflection, the more uncomfortable result. Of three catalogues, one states a
mechanical exclusion and enforces it almost perfectly; one states an exclusion that **cannot be
applied deterministically**, because in the authors' own annotation database the same gene
simultaneously satisfies and violates it depending on which KEGG category one reads; and one
states its criterion in ordinary English, which cannot be checked at all without importing the
checker's judgement.

A rule that does not decide is not being enforced — it is being interpreted, case by case,
invisibly, and no reader can reconstruct which reading was applied to which gene. This is not
a failure of care by any author. It is a convention that has never required inclusion criteria
to be machine-checkable, and the drift documented in this paper is what that convention
produces at scale.

We think this is the finding with the clearest remedy, and it does not depend on accepting a
single one of our verdicts.

### 4.4 Eight families, no evidence

Eight of 35 families have **no phage-specific experimental evidence of any kind**. Not weak
evidence: none. Nobody has tested what the phage copy of those genes does, in any system, and
published claims rest on them anyway.

Under our protocol these families default to COUNTS, because a family with no evidence is
*unresearched*, not unresolvable, and we refuse to let absence of evidence inflate the disputed
share. That is the conservative choice and it works against our own hypothesis. But it should
not obscure what the number means: for roughly a quarter of the families examined, the
question this entire literature turns on has never been asked experimentally.

Each unresolvable verdict in this study names the specific experiment that would settle it
(Appendix A). We suggest that list is the most immediately actionable output here.

### 4.5 What we are not claiming

Not that the annotations are wrong: these sequences really do encode glycosyltransferases and
methyltransferases. We challenge the **inference drawn from the annotation**, not the
identification — the misannotation is not in the database, it is in the sentence written
afterwards.

Not that any author was careless. Section 3.2 shows one team applying its own stated exclusions
to 99.993%. People following reasonable rules can still produce a record that overstates,
because the rules underdetermine.

Not anything about any individual gene call. We cannot know what one phage in one water sample
was doing with its copy of `galE`. These are claims about the most parsimonious reading of a
family, applied to every call in it.

And emphatically not that AMGs are not real. `psbA` is real, `phoH`'s distribution (present in
~40% of marine phage genomes and 4% of non-marine ones; Goldsmith *et al.* 2011,
doi:10.1128/AEM.05531-11) is about as good as ecological evidence gets, and transaldolase
measurably doubles the host NADPH/NADP ratio (Thompson *et al.* 2011,
doi:10.1073/pnas.1102164108). The question is only how much of the record rests on families
that do not support the claim drawn from them.

### 4.6 On `dcm`, and on reporting one's own fragilities

That a single family supplies 99.6% of the ocean strict-rule result is a fragility, and we
report it as one rather than leaving it for a reviewer. It is also informative in two ways.
First, `dcm` is the least contested case in the whole record — a restriction–modification
function nobody seriously argues is host metabolism — so the exposure is concentrated in the
clearest case rather than a marginal one. Second, `dcm`'s verdict was fixed by the protocol as
a worked example *before* any evidence was weighed, which means the ocean strict figure is
substantially a restatement of the protocol rather than a finding produced by applying it. We
therefore rest nothing on it.

### 4.7 What the field could do

1. **Report AMG counts under more than one rule.** The spread between inclusive and maximally
   strict reaches 28.5 percentage points within a single catalogue. A single number conceals a
   choice that a reader cannot see or reverse.
2. **State inclusion criteria mechanically enough to be checked.** If a criterion cannot be
   applied deterministically using the annotation database the study itself used, it is not
   functioning as a criterion.
3. **Report the namespace and the unit.** KEGG and Pfam disagree by up to threefold on the same
   catalogue, and in opposite directions in different environments; genes and calls are not
   interchangeable.
4. **Do the named experiments.** Three unresolvable families, three specified experiments, and
   eight families with no phage-specific evidence at all.

### 4.8 A note on method

Three headline numbers in this study were killed by checks built into it beforehand: a family
that turned out to be 99.4% a protein *fold* rather than an activity; an apparent abundance
depletion that was per-virus values summed over per-gene rows; and an inter-rater agreement
figure whose independence could not be verified. Each was caught by something set up in
advance — a frozen accession list with a status column, a pre-registered commitment to report
both weightings, a sealed counts file, a routine text comparison.

We report them because a study arguing that a field's conventions permit undetected drift is
obliged to demonstrate that its own conventions detect it.

## 5. Limitations

1. **Independence of the second adjudication pass is unverified** (§2.5). No inter-rater
   reliability statistic is claimed.
2. **No control in this study is blind.** The protocol names all five.
3. **Abundance weighting covers 5% of the record** (§3.5).
4. **35 families, not all families.** 18 further families were removed by Amendment 2 and
   counted in aggregate as COUNTS, accounting for 3.1 percentage points.
5. **Family-level verdicts are applied to every call in the family.** No claim is made about
   any individual gene call, which cannot be adjudicated from catalogue data.
6. **Adjudication is defeasible.** Verdicts reflect the best reading of current evidence, not
   settled fact — which is why confidence is recorded separately and why Tier 6 alone cannot
   rule a family out.

## 6. Data and code availability

All code, intermediate results, the frozen accession list, the pre-registered protocol with
amendments, the sealed abundance counts with their commit history, and both adjudication
passes: **https://github.com/dmurfy06/amg-annotation-audit**

Source catalogues are the published supplementary files of the three cited studies and are not
redistributed here.

## 7. Acknowledgements

Analysis code was written with Claude (Anthropic), and the first adjudication pass was
AI-produced; see §2.5 for what that means for the reliability claims in this paper. Scientific
judgement, verdicts, and all decisions about what to report are the author's.

---

## Appendix A — the 35 adjudicated families

**Complete: `manuscript/appendix_a_families.md`.** Verdict, evidence tier, confidence,
per-catalogue counts, basis for inclusion and full accession list for all 35 families, plus
the named resolving experiment for each unresolvable verdict. Generated directly from the
adjudication record by `scripts/build_appendix_a.py` rather than transcribed, so it cannot
drift from the underlying verdicts.

## Figures

Built by `scripts/build_figures.py` from the sealed counts and the adjudication record
(Figures 1, 2, 4) and from the chunk 7 outputs (Figure 3), so no value is transcribed by hand.
PNG and vector PDF in `manuscript/figures/`. Palette is Okabe–Ito and legible in greyscale.

**Figure 1 — Excluded share depends on which pre-registered rule is applied.**
`fig1_four_rule_spread` · cited in §3.4
Excluded share of the KO-assigned AMG record under three of the four pre-registered rules, for
each catalogue, with Wilson 95% intervals. The confidence-limited rule is identical to strict —
all four DOES NOT COUNT verdicts were recorded at high confidence — and is not plotted
separately. *The spread between rules is the result; no single bar is the headline.*

**Figure 2 — One family carries the strict result; the maximally-strict result is distributed.**
`fig2_leave_one_out` · cited in §3.4
Leave-one-out for the ocean catalogue: each bar is the excluded share when that family alone is
held at COUNTS, against the dashed baseline. Under the strict rule, removing `dcm` collapses the
result from 18.31% to 0.07%. Under the maximally-strict rule the load is distributed across
`dcm`, `queuosine` and `folate`. `dcm` is highlighted because it is also a protocol worked
example, so its verdict was fixed before evidence was weighed.

**Figure 3 — Disputed families cancel in comparisons and persist in descriptions.**
`fig3_published_claims` · cited in §3.6 · **the paper's key figure**
One claim from each catalogue's own abstract, all three fixed before any was recomputed.
*Left:* the wastewater catalogue's 101 vAMGs, with the queuosine-pathway genes its abstract
names as most common highlighted — under the maximally-strict rule those genes disappear and
29 vAMGs go with them. *Centre:* the ocean prevalence estimate falls from 19% to 16.9%.
*Right:* the soil contamination gradient is unchanged under every rule, for both abundance and
richness.

**Figure 4 — Half the adjudicated families rest on chemical plausibility alone.**
`fig4_evidence_tiers` · cited in §3.3
Highest tier of phage-specific evidence found for each of the 35 families, stacked by verdict.
Seventeen families reach only Tier 6, where the protocol forbids ruling a family out, so they
default to counting. Eight have no phage-specific evidence of any kind. Tiers are from the
first-pass record; the second pass disagreed on one family (`rfbC`, Tier 2 vs 6; §2.5).
