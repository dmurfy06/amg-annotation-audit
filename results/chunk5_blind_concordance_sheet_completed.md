---
tags: [project, research, adjudication, concordance, active]
---

# Blind Concordance Sheet — 12 judgement families

**This is the only adjudication file left in the vault. That is deliberate.**
The completed worksheet and the evidence dossiers have been moved into the repo so nothing
can leak in while you work.

> [!danger] Don't go looking for the earlier verdicts
> The entire value of this exercise is that you reach your answers without seeing anyone
> else's. Read them first and you are not a second rater, you are an echo — and the
> concordance number becomes worthless with no way for anyone to tell.

## What this is

Twelve families. Every one is a case where evidence **was** found and had to be weighed —
the only places two raters applying the same rule could legitimately diverge. The other 23
families were decided mechanically by the protocol (no Tier 1–5 evidence, so the family
cannot be ruled out, so it stays in), and two raters must agree on those by construction.
Measuring agreement there would inflate the number while testing nothing.

**You are not writing arguments.** This is standard inter-rater practice: apply the rubric,
record the code. Three fields per family, plus a resolving experiment if you say the evidence
can't settle it. **A note is only needed if something surprised you.**

Roughly **4–6 hours**. Two sittings is a good rate. Stop when you're tired — a verdict
written badly at 1am is worse than no verdict.

## The rule, for reference

**Counts as an AMG only if BOTH:** the product acts on a **host** molecule, **and** the
effect is to **sustain or redirect host metabolism** — not to serve a discrete step of the
viral lifecycle (entry, genome protection, replication, assembly, egress).

**Default is COUNTS.** A family only leaves the record on positive Tier 1–5 evidence.
Tier 6 (chemistry alone) can never move a family out by itself — that would restate the
Martin *et al.* argument rather than test it.

**UNRESOLVABLE requires naming the experiment that would settle it.** If you can't name one,
the family is *unresearched*, not unresolvable, and defaults to COUNTS. Keep UNRESOLVABLE for
"the evidence conflicts", never for "there is no evidence".

| Tier | What it looks like |
|---|---|
| **1** | The gene was knocked out of a phage and the effect measured |
| **2** | The **phage's own** protein was purified or structured and its substrate shown |
| **3** | Expression timing across infection (early / middle / late) |
| **4** | The gene sits consistently among structural or replication genes |
| **5** | The phage copy has diverged from host copies in a telling way |
| **6** | Chemistry alone — *"this enzyme does X, so presumably…"* |

> [!note] What was removed from the evidence below, and why
> These extracts are the dossiers minus three things: any passage naming a verdict, my
> "tier available" assessments, and the pre-named resolving experiments. You assign the tier
> yourself, which makes tier agreement a real measurement rather than a copied one.
>
> **The case for HOST and the case for VIRAL are kept in full for every family**, along with
> every citation. Five families needed hand-written edits because a blunt strip took evidence
> with it — `dsrC_tusE`, `nrdH`, `queuosine`, `rfbC`, `glycosyltransferase`. Those edits are
> in `scripts/build_blind_concordance_sheet.py` if you want to audit them.

---

## 1. `dsrC_tusE`

- **K11179** — tusE, dsrC; tRNA 2-thiouridine synthesizing protein E [EC:2.8.1.-]

*Included because: named by Martin et al.*

### Evidence

**K11179** · EC 2.8.1.-

**Why this family is in the rubric.** Martin *et al.* single it out as an **annotation failure**,
not a biological one: DsrC and TusE do different jobs, HMMs cannot separate them, and **KEGG has
merged them into one orthology group literally named `tusE, dsrC`.**

**The two proteins.** Stockdreher *et al.* (2012, *PLoS One*) work out the chemistry and state the
relationship: **TusE is part of a tRNA-modification system** — TusBCD transfers sulfur to TusE —
and TusE is *"a homolog of another crucial component of the A. vinosum Dsr system, namely DsrC."*
DsrC is persulfurated at Cys111 and feeds sulfur to **dissimilatory sulfite reductase DsrAB**,
i.e. energy metabolism. [DOI](https://doi.org/10.1371/journal.pone.0040785)

Same fold, same persulfide chemistry, **two entirely different destinations.**

**Case for HOST — and this is stronger than it first looked.** Kieft *et al.* (2021, *Nature
Communications*) identified **191 phages across twelve environments encoding 227 AMGs** for sulfur
and thiosulfate oxidation — listing *"dsrA, dsrC/tusE, soxC, soxD and soxYZ"*. They report
*"evidence for retention of AMGs during niche-differentiation… auxiliary metabolism imparts
measurable fitness benefits to phages"*, expression profiles suggesting *"significant
contributions by phages to sulfur and thiosulfate oxidation in freshwater lakes and oceans"*, and
a response to sulfur gradients in hydrothermal systems.
[DOI](https://doi.org/10.1038/s41467-021-23698-5)

**Case for VIRAL / not-what-it-claims.** If the phage copy is a `tusE`, it feeds tRNA thiolation —
housekeeping, with no sulfur-cycling implication at all.

> [!important] Two things to notice, and the second is sharper
> **First**, Kieft *et al.* is the strongest pro-AMG case for any family in this list.
>
> **Second — the authors themselves write `dsrC/tusE`, with a slash.** The field's strongest
> phage-sulfur paper inherits the exact ambiguity Martin complains about, and says so in its own
> notation. Also worth knowing: first author **Kristopher Kieft is the author of VIBRANT**, one of
> the two tools audited in Chunk 1. Not a criticism — context.

**Note.** Nothing in the environmental data tells you which of the two genes a given call actually is.

### Your call

| Field                                                      | Your answer                                              |
| ---------------------------------------------------------- | -------------------------------------------------------- |
| **VERDICT** — COUNTS / DOES NOT COUNT / UNRESOLVABLE       | UNRESOLVABLE                                             |
| **Evidence tier** — 1 to 6                                 | 3 on ecology 0 on genetics                               |
| **Confidence** — low / moderate / high                     | high                                                     |
| **Resolving experiment** — *required only if UNRESOLVABLE* | seperation of dsrc from tuse then reannotation of calls  |
| **Note** — *optional; only if something surprised you*     |                                                          |

---

## 2. `dut`

- **K01520** — dut, DUT; dUTP diphosphatase [EC:3.6.1.23]

*Included because: >=1% and >=10 calls in ocean_conservative*

### Evidence

**K01520** · EC 3.6.1.23

**What it does.** Hydrolyses dUTP → dUMP + PPi. Two jobs: keeps dUTP out of the pool so uracil
isn't misincorporated into DNA, and supplies dUMP for thymidylate synthase. Sits directly on the
path to dTTP.

**Phage-specific evidence.** Huang *et al.* (2021, *Environ Microbiol*) catalogued 180 AMGs across
50 roseophage genomes; seven high-frequency ones (*"trx, grx, RNR, thyX, DCD, phoH, and mazG"*)
are **mostly** *"involved in the nucleotide biosynthesis pathway."* `dUTPase` is in their
*sporadic* set. [DOI](https://doi.org/10.1111/1462-2920.15412)

**A complication.** Phage dUTPases have a documented **non-enzymatic** role: Nyíri *et al.* (2019,
*Biomolecules*; 2024, *Sci Rep*) show staphylococcal phage dUTPases binding the **Stl master
repressor**, de-repressing pathogenicity-island transfer.
[DOI](https://doi.org/10.3390/biom9090488) · [DOI](https://doi.org/10.1038/s41598-024-51260-y)
So "what is a phage dUTPase for?" already has two published answers, neither host metabolism.

**Case for HOST.** A housekeeping enzyme of the host's own nucleotide pool; boosting it raises the
cell's dNTP supply.

**Case for VIRAL.** That pool is being drawn down to replicate the **phage** genome, in an
infection ending in lysis. Feeding your own replication is a discrete lifecycle step.

### Your call

| Field                                                      | Your answer                                                      |
| ---------------------------------------------------------- | ---------------------------------------------------------------- |
| **VERDICT** — COUNTS / DOES NOT COUNT / UNRESOLVABLE       | counts                                                           |
| **Evidence tier** — 1 to 6                                 | 4                                                                |
| **Confidence** — low / moderate / high                     | low                                                              |
| **Resolving experiment** — *required only if UNRESOLVABLE* | track dUMP produced into phage versus host DNA afteer infection  |
| **Note** — *optional; only if something surprised you*     |                                                                  |

---

## 3. `folate`

- **K00287** — DHFR, folA; dihydrofolate reductase [EC:1.5.1.3]
- **K00548** — metH, MTR; 5-methyltetrahydrofolate--homocysteine methyltransferase [EC:2.1.1.13]
- **K01433** — purU; formyltetrahydrofolate deformylase [EC:3.5.1.10]
- **K01491** — folD; methylenetetrahydrofolate dehydrogenase (NADP+) / methenyltetrahydrofolate cyclohydrolase [EC:1.5.1.5 3.5.4.9]
- **K01495** — GCH1, folE; GTP cyclohydrolase IA [EC:3.5.4.16]
- **K01633** — folB; 7,8-dihydroneopterin aldolase/epimerase/oxygenase [EC:4.1.2.25 5.1.99.8 1.13.11.81]
- **K09007** — folE2; GTP cyclohydrolase IB [EC:3.5.4.16]
- **K13938** — folM; dihydromonapterin reductase / dihydrofolate reductase [EC:1.5.1.50 1.5.1.3]
- **K13998** — DHFR-TS; dihydrofolate reductase / thymidylate synthase [EC:1.5.1.3 2.1.1.45]
- **K19645** — dfrB, dfr2; dihydrofolate reductase (trimethoprim resistance protein) [EC:1.5.1.3]

*Included because: >=1% and >=10 calls in ocean_conservative, soil; named by Martin et al.*

### Evidence

**K00287, K00548, K01433, K01491, K01495, K01633, K09007, K13938, K13998, K19645**
Includes `folA`, `folB`, `folD`, `folE` (K01495), `folE2` (K09007), `metH`, `purU`, DHFR-TS.

**What it does.** Builds tetrahydrofolate, the universal one-carbon carrier — feeding purine
synthesis, thymidylate synthesis, methionine, and formylmethionyl-tRNA for translation initiation.

**The overlap you already know about.** `folE`/GTP cyclohydrolase I is the first committed step of
folate biosynthesis **and** the entry point to queuosine biosynthesis (`queuosine`). `folE2` is an
alternative at the same branch. All four are flagged **AMBIGUOUS** in the frozen accession list,
and Chunk 4 showed the wastewater paper's own rule cannot resolve them either.

**Cross-reference `queuosine`.** Thiaville *et al.* detected a 7-deazaguanine derivative **in phage DNA**;
the pathway making it starts at GTP cyclohydrolase I.
[DOI](https://doi.org/10.1073/pnas.1518570113)

**Case for HOST.** Folate is a genuine cofactor pathway serving the whole cell; supplementing it
is host metabolic modulation in the ordinary sense.

**Case for VIRAL.** Martin *et al.*'s argument: the one-carbon units feed *de novo* nucleotide
biosynthesis for **phage genome replication**. The queuosine evidence adds a second viral route —
genome modification.

> [!caution] This is the 18-percentage-point family
> Wastewater runs **19.5% → 37.7%** on whether `folE`/`queD` count. The write-up reports it both
> ways regardless. Make this argument box your best one — it is the paragraph a reviewer reads
> hardest.

### Your call

| Field                                                      | Your answer                                                                             |
| ---------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **VERDICT** — COUNTS / DOES NOT COUNT / UNRESOLVABLE       | UNRESOLVABLE                                                                            |
| **Evidence tier** — 1 to 6                                 | 2                                                                                       |
| **Confidence** — low / moderate / high                     | high (in the unresolvability)                                                           |
| **Resolving experiment** — *required only if UNRESOLVABLE* | metabolic flux from folE. See if pterin output is to tetrahydrofolate or deazaguanine   |
| **Note** — *optional; only if something surprised you*     |                                                                                         |

---

## 4. `glycoside_hydrolase`

- **K01179** — E3.2.1.4; endoglucanase [EC:3.2.1.4]
- **K01185** — E3.2.1.17; lysozyme [EC:3.2.1.17]
- **K01187** — malZ; alpha-glucosidase [EC:3.2.1.20]
- **K01190** — lacZ; beta-galactosidase [EC:3.2.1.23]
- **K01199** — EGLC; glucan endo-1,3-beta-D-glucosidase [EC:3.2.1.39]
- **K03791** — K03791; putative chitinase

*Included because: named by Martin et al.*

### Evidence

**K01179, K01185, K01187, K01190, K01199, K03791** — endoglucanase, lysozyme, α-glucosidase,
β-galactosidase, glucan endo-1,3-β-D-glucosidase, putative chitinase

**What they do.** Cleave glycosidic bonds. In phage biology: **endolysins** (lyse the cell from
inside at the end of infection), **virion-associated lysins** (locally degrade the wall during
entry), **tailspike depolymerases** (chew capsule or O-antigen to reach the receptor).

**Phage-specific evidence.** Yuan & Gao (2016, *Front Microbiol*) did
**structural proteome analysis** on a *Bacillus* jumbo phage and identified 23 virion proteins
including a glycoside hydrolase, Gp255, which:

- *"was identified as phage virion component and was found to **interact with the phage baseplate
  protein**"*
- shows lytic activity against the host strain
- was *"the **first functional individual structural glycoside hydrolase in phage virion**"*
- *"might **facilitate the injection of the phage genome during infection** by forming pores on
  the bacterial cell wall."*

[DOI](https://doi.org/10.3389/fmicb.2016.00745)

**Case for HOST.** Some glycoside hydrolases are genuine sugar-catabolic enzymes; one liberating
usable sugars for the host would be host metabolic modulation. **No phage-specific evidence for
this reading was found.**

**Case for VIRAL.** A glycoside hydrolase physically in the virion, bound to the baseplate,
breaching the wall for genome entry. Substrate host, consequence entry — a discrete lifecycle step.

> [!note] You are judging 123 calls, not 21,690
> `PF13385` — *"Concanavalin A-like lectin/glucanases superfamily"* — was struck from this family
> during the accession review because it is a **fold, not an activity**. It was 99.4% of the
> original count.

### Your call

| Field                                                      | Your answer    |
| ---------------------------------------------------------- | -------------- |
| **VERDICT** — COUNTS / DOES NOT COUNT / UNRESOLVABLE       | does not count |
| **Evidence tier** — 1 to 6                                 | 1              |
| **Confidence** — low / moderate / high                     | high           |
| **Resolving experiment** — *required only if UNRESOLVABLE* |                |
| **Note** — *optional; only if something surprised you*     |                |

---

## 5. `glycosyltransferase`

- **K00754** — bshA; L-malate glycosyltransferase [EC:2.4.1.-]
- **K03669** — mdoH; membrane glycosyltransferase [EC:2.4.1.-]
- **K03814** — mtgA; peptidoglycan glycosyltransferase [EC:2.4.99.28]
- **K07270** — K07270; glycosyl transferase, family 25
- **K15521** — mshA; D-inositol-3-phosphate glycosyltransferase [EC:2.4.1.250]

*Included because: >=1% and >=10 calls in soil; named by Martin et al.*

### Evidence

**K00754, K03669, K03814, K07270, K15521** — `bshA`, `mdoH`, `mtgA`, family-25 GT, `mshA`

**What they do.** Transfer sugars onto growing glycans. Downstream: **O-antigen, LPS, capsule,
wall teichoic acid** — the bacterial cell surface.

**Phage-specific evidence.** See
[Appendix A](#appendix-a--the-nucleotide-sugar-and-cell-surface-literature) in full. In short:
phage-encoded glycosyltransferases demonstrably modify the **host's** O-antigen, and the
demonstrated consequence is **serotype conversion — changing the phage receptor.**

> [!important] This family breaks the two-part rule, and you should expect that
> Substrate is unambiguously **host**. But the consequence — receptor modification — is neither
> "sustaining host metabolism" nor obviously one of the listed lifecycle steps.
>
> **It is arguably a third thing: modifying the host to control who else can infect it.** For a
> lysogen, excluding competitors is a real fitness function.
>
> The protocol has no category for "the rule cannot classify this." Whatever you decide,
> record in the Note field that the rule underdetermined it.

### Your call

| Field                                                      | Your answer                                                                        |
| ---------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **VERDICT** — COUNTS / DOES NOT COUNT / UNRESOLVABLE       | counts                                                                             |
| **Evidence tier** — 1 to 6                                 | 2                                                                                  |
| **Confidence** — low / moderate / high                     | low                                                                                |
| **Resolving experiment** — *required only if UNRESOLVABLE* | does phage mediated serotype conversion alter metabolic flux in host after glycan  |
| **Note** — *optional; only if something surprised you*     |                                                                                    |

---

## 6. `NAMPT`

- **K03462** — NAMPT; nicotinamide phosphoribosyltransferase [EC:2.4.2.12]

*Included because: >=1% and >=10 calls in soil*

### Evidence

**K03462** · EC 2.4.2.12

**What it does.** First step of **NAD⁺ salvage**: nicotinamide → nicotinamide mononucleotide,
en route to NAD⁺.

**Phage-specific evidence.** Lee, Li & Miller (2017, *J Bacteriol*), *"Vibrio Phage
KVP40 Encodes a Functional NAD⁺ Salvage Pathway"*: KVP40 has five pyridine-nucleotide genes, two
sufficient for salvage. They cloned, expressed and purified them; **KVP40 NadV NAmPRTase is
active**, and a clone **complements an *E. coli* mutant** defective in both bacterial NAD
pathways. RT-qPCR and enzyme assays of infected cells showed transcription **during the early and
delayed-early period of infection**, alongside other nucleotide-precursor genes.
[DOI](https://doi.org/10.1128/JB.00855-16)

They conclude NAD⁺ biosynthesis is *"another important metabolic resource control point by large,
rapidly replicating dsDNA bacteriophages"*, noting T4-type phages use NADH/NADPH for DNA precursor
synthesis and NAD⁺ for **ADP-ribosylation of proteins transcribing and translating the phage
genome**.

Independently, Huang *et al.* (2022, *ACS Synth Biol*) used the KVP40 enzyme as a biocatalyst,
finding it *"has the best catalytic activity"* for producing NMN — confirming it is genuinely
functional. [DOI](https://doi.org/10.1021/acssynbio.2c00100)

**Case for HOST.** NAD⁺ is a universal cofactor; a phage salvage pathway raises its availability
in the infected cell — "metabolic resource control", in the authors' phrase.

**Case for VIRAL.** The stated uses are DNA precursor synthesis and ADP-ribosylation of the
phage's own machinery, expressed in the phage's own metabolic window rather than as a sustained
host programme.

### Your call

| Field                                                      | Your answer                                                                                |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **VERDICT** — COUNTS / DOES NOT COUNT / UNRESOLVABLE       | counts                                                                                     |
| **Evidence tier** — 1 to 6                                 | 2                                                                                          |
| **Confidence** — low / moderate / high                     | low                                                                                        |
| **Resolving experiment** — *required only if UNRESOLVABLE* | see if nad+ produced by pathway is taken up by phagre adp ribosylation or host metabolism  |
| **Note** — *optional; only if something surprised you*     |                                                                                            |

---

## 7. `nrdH`

- **K06191** — nrdH; glutaredoxin-like protein NrdH

*Included because: >=1% and >=10 calls in soil*

### Evidence

**K06191**

**What it does.** Redox partner of class Ib **ribonucleotide reductase** (RNR). RNR converts
ribonucleotides to deoxyribonucleotides — the committed step in making DNA precursors.

**Phage-specific evidence.** PubMed returns ~130 results for bacteriophage
ribonucleotide reductase. More pointedly, Sakowski *et al.* (2021, *Nature Microbiology*) built a
method for capturing virus–host interactions that *"fuses a **phage marker, the ribonucleotide
reductase gene**, with the host 16S rRNA gene of infected bacterial cells."*
[DOI](https://doi.org/10.1038/s41564-021-00873-4)

**RNR is used as a marker gene for phage** — the same status `phoH` has. Phage RNRs are
distinct enough from host copies to identify a virus, which is not the signature of an
incidentally acquired gene. Huang *et al.* (2021) also list RNR among the seven high-frequency
roseophage AMGs. [DOI](https://doi.org/10.1111/1462-2920.15412)

**Case for HOST.** RNR supplies the dNTP pool the whole cell uses.

**Case for VIRAL.** Those dNTPs replicate the phage genome; a phage encoding its own RNR is the
textbook case of provisioning its own replication, and the phylogenetic distinctness supports
specialisation.

**A complication.** No experiment separates "the host's dNTP pool" from "the phage's" during infection, **because during infection they are the same pool.**

### Your call

| Field                                                      | Your answer                                    |
| ---------------------------------------------------------- | ---------------------------------------------- |
| **VERDICT** — COUNTS / DOES NOT COUNT / UNRESOLVABLE       | counts                                         |
| **Evidence tier** — 1 to 6                                 | 4-5                                            |
| **Confidence** — low / moderate / high                     | low                                            |
| **Resolving experiment** — *required only if UNRESOLVABLE* | seperate pahge and host dNTP during infection  |
| **Note** — *optional; only if something surprised you*     |                                                |

---

## 8. `phoH`

- **K06217** — phoH, phoL; phosphate starvation-inducible protein PhoH and related proteins

*Included because: >=1% and >=10 calls in ocean_conservative*

### Evidence

**K06217**

**What it does.** Part of the **Pho regulon**, the response to phosphate limitation that switches
on high-affinity phosphate scavenging. `phoH` is an ATP-binding protein of not-fully-resolved
function.

**Phage-specific evidence.** Goldsmith *et al.* (2011, *Appl Environ Microbiol*) found Pho regulon
genes in **~40% of marine phage genomes but only 4% of non-marine ones**, `phoH` most prevalent —
in 42 of 602 complete phage genomes. Phage `phoH` sequences *"formed a cluster distinct from those
of their bacterial hosts"*, and the gene is now a **signature gene for marine phage diversity**.
[DOI](https://doi.org/10.1128/AEM.05531-11) Huang *et al.* (2021) list it among the seven
high-frequency roseophage AMGs. [DOI](https://doi.org/10.1111/1462-2920.15412)

**Case for HOST.** About as good as the AMG hypothesis gets outside photosynthesis: the 40%-vs-4%
split says phages carry it **where phosphate is limiting**, which is hard to explain except by
phosphate acquisition mattering to the infected cell.

**Case for VIRAL.** Phage replication is phosphate-expensive — a hundred-virion burst is a large
nucleic-acid demand. And the phylogenetic separation is consistent with specialisation away from
the host function.

### Your call

| Field                                                      | Your answer                                                                       |
| ---------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **VERDICT** — COUNTS / DOES NOT COUNT / UNRESOLVABLE       | counts                                                                            |
| **Evidence tier** — 1 to 6                                 | 4                                                                                 |
| **Confidence** — low / moderate / high                     | medium                                                                            |
| **Resolving experiment** — *required only if UNRESOLVABLE* | deltee pjage phoH and look at phosphaye uptake in a normal cell vs infected cell  |
| **Note** — *optional; only if something surprised you*     |                                                                                   |

---

## 9. `queuosine`

- **K01737** — queD, ptpS, PTS; 6-pyruvoyltetrahydropterin/6-carboxytetrahydropterin synthase [EC:4.2.3.12 4.1.2.50]
- **K06879** — queF; 7-cyano-7-deazaguanine reductase [EC:1.7.1.13]
- **K06920** — queC; 7-cyano-7-deazaguanine synthase [EC:6.3.4.20]
- **K09457** — queF; 7-cyano-7-deazaguanine reductase [EC:1.7.1.13]
- **K10026** — queE; 7-carboxy-7-deazaguanine synthase [EC:4.3.99.3]

*Included because: >=1% and >=10 calls in ocean_conservative, soil; named by Martin et al.*

### Evidence

**K01737, K06879, K06920, K09457, K10026**

**What the pathway does.** Builds 7-deazaguanine derivatives. Classically it ends in queuosine, a
hypermodified base at the wobble position of certain tRNAs. **`folE` supplies the entry precursor
— the same step that feeds folate biosynthesis** (another family), which is why these sit at the branch point
that moves the headline by 18 points.

**Phage-specific evidence.** Thiaville *et al.* (2016, *PNAS*) showed
7-deazaguanine derivatives are inserted **into DNA, not only tRNA**; transformation assays
*"strongly suggest a restriction-modification role for the cluster"*; and they detected
**2′-deoxy-7-formamidino-7-deazaguanosine in *E. coli* bacteriophage 9g.**
[DOI](https://doi.org/10.1073/pnas.1518570113)

Hutinet *et al.* (2016, *RNA Biology*): the modifications *"were thought to be highly specific of
tRNAs, but have now been discovered in DNA of phages"*, and are *"proposed to be a protection
mechanism against endonucleases."* [DOI](https://doi.org/10.1080/15476286.2016.1265200)

de Crécy-Lagard *et al.* (2024, *MMBR*) list among their functions *"cellular stress resistance,
self-nonself discrimination mechanisms, and host evasion defenses."*
[DOI](https://doi.org/10.1128/mmbr.00199-23)

**Case for HOST.** Queuosine's established role is tRNA modification, affecting translational
fidelity cell-wide. The wastewater authors themselves note the genes *"could also participate in
tRNA biogenesis."*

**Case for VIRAL.** The product has been **detected in phage DNA**, with the attributed function
being protection from host endonucleases — viral substrate, genome protection.

> [!important] The specific question here
> The pathway demonstrably does **both**, in different organisms, and **the genes do not
> distinguish the two uses** — a phage modifying its own DNA needs the same enzymes as one
> feeding host tRNA.
>
> Thiaville's chemical detection was done for a single phage; nobody has repeated it
> systematically.

### Your call

| Field                                                      | Your answer                                                                        |
| ---------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **VERDICT** — COUNTS / DOES NOT COUNT / UNRESOLVABLE       | unresolvalbe                                                                       |
| **Evidence tier** — 1 to 6                                 | 2                                                                                  |
| **Confidence** — low / moderate / high                     | high in unresolvability                                                            |
| **Resolving experiment** — *required only if UNRESOLVABLE* | systematic detection of deazaguianine derivatives in phage dna carry genes vs not  |
| **Note** — *optional; only if something surprised you*     |                                                                                    |

---

## 10. `rfbC`

- **K20444** — rfbC; O-antigen biosynthesis protein [EC:2.4.1.-]

*Included because: >=1% and >=10 calls in soil*

### Evidence

**K20444** · EC 2.4.1.-

**What it does.** KEGG's own description names it **O-antigen biosynthesis**. Of the whole
nucleotide-sugar block, this is the most explicitly surface-dedicated.

**Phage-specific evidence.** The block literature in
[Appendix A](#appendix-a--the-nucleotide-sugar-and-cell-surface-literature) applies most directly
here — Mann *et al.* and Sun *et al.* are specifically about phage modification of O-antigen.

**Case for HOST / VIRAL:** as for `glycosyltransferase` above, and with less of the
precursor-ambiguity caveat.

### Your call

| Field                                                      | Your answer                                             |
| ---------------------------------------------------------- | ------------------------------------------------------- |
| **VERDICT** — COUNTS / DOES NOT COUNT / UNRESOLVABLE       | counts                                                  |
| **Evidence tier** — 1 to 6                                 | 6                                                       |
| **Confidence** — low / moderate / high                     | low                                                     |
| **Resolving experiment** — *required only if UNRESOLVABLE* | find destination of dTDP-rhamnose made by pahge enzyme  |
| **Note** — *optional; only if something surprised you*     |                                                         |

---

## 11. `speD`

- **K01611** — speD, AMD1; S-adenosylmethionine decarboxylase [EC:4.1.1.50]

*Included because: >=1% and >=10 calls in ocean_conservative*

### Evidence

**K01611** · EC 4.1.1.50

**What it does.** Decarboxylates SAM to supply the aminopropyl donor for **spermidine** synthesis.
Polyamines are polycations that bind nucleic acids and are needed for normal growth.

**Phage-specific evidence.** PubMed returns work on phage and polyamines going back to the 1970s.
Spermidine is a structural component of some phage virions, where its positive charge helps
neutralise the packaged genome's phosphate backbone.

**Case for HOST.** Polyamine synthesis is general host metabolism — growth, translation, stress
response.

**Case for VIRAL.** If spermidine is being made to **condense and neutralise the phage genome
during packaging**, that is assembly — a discrete lifecycle step, directly parallel to the
terminase argument (another family–35).

### Your call

| Field                                                      | Your answer                                                                       |
| ---------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **VERDICT** — COUNTS / DOES NOT COUNT / UNRESOLVABLE       | counts                                                                            |
| **Evidence tier** — 1 to 6                                 | 5                                                                                 |
| **Confidence** — low / moderate / high                     | low                                                                               |
| **Resolving experiment** — *required only if UNRESOLVABLE* | see if spermidine made during infecition is made into virions or remains on host  |
| **Note** — *optional; only if something surprised you*     |                                                                                   |

---

## 12. `TALDO1`

- **K00616** — TALDO1, talB, talA; transaldolase [EC:2.2.1.2]

*Included because: >=1% and >=10 calls in ocean_conservative*

### Evidence

**K00616** · EC 2.2.1.2

**What it does.** Reversible carbon-shuffling step of the **non-oxidative pentose phosphate
pathway**, linking PPP to glycolysis. The PPP makes **NADPH** and **ribose 5-phosphate** — the
sugar backbone of nucleotides.

**Phage-specific evidence.** Thompson *et al.* (2011, *PNAS*),
*"Phage auxiliary metabolic genes and the redirection of cyanobacterial host carbon metabolism"*:

- cyanophages carry and express **CP12, a Calvin cycle inhibitor**, whose host homologue *"directs
  carbon flux from the Calvin cycle to the pentose phosphate pathway"*
- **phage transaldolase was purified to homogeneity from several strains and shown to be
  functional in vitro**; it is *"the most prevalent PPP gene in cyanophages"*
- phage transaldolase has k_cat/K_m only **~one third** of the host enzyme
- **the host NADPH/NADP ratio increased two-fold in infected cells**
- their proposal: *"phage-augmented NADPH production fuels deoxynucleotide biosynthesis for phage
  replication"*

[DOI](https://doi.org/10.1073/pnas.1102164108)

Lindell *et al.* (2007, *Nature*): `talC` is transcribed **together with phage DNA replication
genes**. [DOI](https://doi.org/10.1038/nature06130) Huang *et al.* (2015, *PLoS One*) find `talC`
at a conserved locus across cyanopodoviruses, in the position `thyX` occupies in other clades.
[DOI](https://doi.org/10.1371/journal.pone.0142962)

**Case for HOST.** A phage enzyme measurably shifts host carbon flux and **doubles the host
NADPH/NADP ratio**. If anything here is host metabolic modulation, this is.

**Case for VIRAL.** The authors themselves say the redirected output fuels **phage** dNTP
synthesis, and Lindell shows it co-transcribed with the replication module.

> [!important] The cleanest statement of the project's central tension
> `psbA` keeps host machinery running. A terminase is purely viral. **Transaldolase is a phage
> enzyme that demonstrably changes host metabolic flux, for a purpose that is entirely viral** —
> stated as such by the authors, in a paper whose title calls it an AMG.
>
> Both readings are defensible on the published evidence. This may be the best example in the
> paper of why the category is contested. Give it time.

### Your call

| Field                                                      | Your answer |
| ---------------------------------------------------------- | ----------- |
| **VERDICT** — COUNTS / DOES NOT COUNT / UNRESOLVABLE       | counts      |
| **Evidence tier** — 1 to 6                                 | 1-2         |
| **Confidence** — low / moderate / high                     | moderate    |
| **Resolving experiment** — *required only if UNRESOLVABLE* | -           |
| **Note** — *optional; only if something surprised you*     |             |

---

## Appendix A — the nucleotide-sugar and cell-surface literature
Shared evidence for `galE` `galE`, `glmS` `glmS`, `glycosyltransferase` `glycosyltransferase`, `gmd` `gmd`, `manB` `manB`,
`pseB` `pseB`, `rfbB` `rfbB`, `rfbC` `rfbC`, `tagD` `tagD`, `UGDH` `UGDH`.

**Phage-encoded glycosyltransferases modify the host's O-antigen.** Mann *et al.* (2015, *J Biol
Chem*): lysogenic bacteriophages encode enzymes that modify LPS O-antigen glycans, *"altering the
structure of the bacteriophage receptor and resulting in serotype conversion"*, demonstrated
experimentally. [DOI](https://doi.org/10.1074/jbc.M115.660803)

**The *Shigella* system.** Sun *et al.* (2013, *BMC Microbiology*): *"nearly all variations between
serotypes are due to glucosyl and/or O-acetyl modifications of the common O unit mediated by
glycosyltransferases encoded by serotype-converting bacteriophages."*
[DOI](https://doi.org/10.1186/1471-2180-13-39)

**Surface glycosylation *is* the phage receptor.** Sumrall *et al.* (2021, *J Bacteriol*) deleted
a **host** glycosyltransferase in *Listeria ivanovii*, removing glucose decoration from wall
teichoic acid; the mutant *"became resistant to phage B025 infection due to an inability of the
phage to adsorb to the bacterial surface."* [DOI](https://doi.org/10.1128/JB.00136-21)

> [!warning] What this literature does and does not cover
> It concerns the **transfer** step — glycosyltransferases acting on the surface. The **precursor**
> enzymes (`galE`, `UGDH`, `gmd`, `rfbB`, `manB`, `glmS`) make nucleotide sugars feeding *many*
> pathways. That the same reasoning carries to them is **an assumption, not a finding** — and how
> surface-committed each precursor is (`pseB`, `rfbB`, `rfbC`, `tagD` more so; `galE`, `manB`,
> `glmS` less so) is a real distinction you can use.

---

## When you're done

Tell Claude. Then, and only then:

1. Your verdicts are compared against the first pass — **agreement on all three fields**
2. The four controls are checked (`psbA`/`psbD` → COUNTS, `xtmA`/`xtmB` → DOES NOT COUNT)
3. **The sealed counts are opened** for the first time
4. The disputed share is recomputed under your verdicts, four ways

> [!important] Disagreements are the valuable output, not the failures
> A family where two raters applying the same written rule reach different answers is a
> family where judgement is load-bearing. Those are exactly the ones the paper should
> discuss at length — and you can't find them without this step.

## Related

- [[Adjudication Protocol]] — the rules and why they're shaped that way
- [[How To Adjudicate]] — the longer mechanics
- [[Where We Are]] · [[Project Auxiliary MOC]]
