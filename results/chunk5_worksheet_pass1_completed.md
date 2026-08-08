---
tags: [project, research, adjudication, active]
---

# Chunk 5 — Adjudication Worksheet

> [!tip] Work in this file. It lives in the vault so you can use Obsidian.
> When you're done (or at any checkpoint), Claude copies it back into the repo as the record.
> The repo original is `C:\ProjectAuxiliary
esults\chunk5_worksheet.md` — **don't edit that one**,
> it'll be overwritten by this.

> [!note] Nine entries are PRE-FILLED
> `asnB` `cgeB` `hisF` `HMGCL` `iscU` `K07336` `nodU` `raxST` `P4HA` — the families with no
> phage-specific evidence. Each carries the protocol's **mechanical default**: no Tier 1–5
> evidence means the family cannot be ruled out, so COUNTS applies automatically. That is rule
> application, not judgement.
>
> **What you still have to decide for those nine:** whether you accept the evidence really is
> absent. Re-search a couple if you want — two of my earlier "no evidence" calls turned out
> wrong. `P4HA` additionally needs a library check that could change its verdict.
>
> **26 families are blank and are yours.**

**Per family: ~30–45 min.** 35 families ≈ 18–26 hours ≈ 3–4 weeks part-time.
See [[Adjudication Protocol]] for the rules and [[How To Adjudicate]] for the step-by-step.


**35 families**, frozen by the rule in `08_adjudication_protocol.md` and ordered **alphabetically** so the big families cannot anchor the run.

> [!warning] This worksheet deliberately contains NO call counts.
> Abundance is in `data/adjudication_counts_SEALED.tsv`. **Do not open it until every
> verdict below is written.** Knowing that a family is worth 5,000 calls while deciding
> whether it counts is exactly the bias the protocol exists to prevent.

## The rule, for reference

**Counts as an AMG only if BOTH:** the product acts on a **host** molecule, **and** the
effect is to **sustain or redirect host metabolism** — not to serve a discrete step of
the viral lifecycle (entry, genome protection, replication, assembly, egress).

Default verdict is **COUNTS**. A family only leaves the record on positive Tier 1–5
evidence. Tier 6 (chemistry alone) can never move a family out by itself.

**UNRESOLVABLE must name the experiment that would resolve it** — otherwise the family
is unresearched, not unresolvable, and defaults to COUNTS.

---

## 1. `asnB`


- **K01953** — asnB, ASNS; asparagine synthase (glutamine-hydrolysing) [EC:6.3.5.4]

*Included because: >=1% and >=10 calls in soil*

> [!note] PRE-FILLED by Claude — review and edit. This is the protocol's mechanical default,
> not a judgement: with no Tier 1–5 evidence the protocol forbids ruling the family out, so
> COUNTS applies automatically. **Your judgement here is whether you accept that the evidence
> is genuinely absent** — i.e. whether my searching held up.

| | |
|---|---|
| **Part 1 — substrate** | UNDETERMINED — no evidence either way |
| **Part 2 — consequence** | UNDETERMINED — no evidence either way |
| **Evidence tier** | 6 (chemistry only; no Tier 1–5 available) |
| **Citations** | KEGG/EcoCyc for the reaction. No phage-specific study found. |
| **VERDICT** | **COUNTS** |
| **Confidence** | low |
| **Resolving experiment** | Express the phage-encoded enzyme; confirm asparagine synthase activity; test whether asparagine limitation alters burst size |

**Argument:**

No phage-specific functional evidence identified after three independent search strategies (thematic PubMed, per-gene PubMed, targeted preprint/web), and the gene is not discussed in any of the three source catalogue papers. Only Tier 6 evidence is available, which under the protocol cannot move a family out of the record. Defaults to COUNTS at low confidence. Flagged as **evidence-free** for separate reporting.

---

## 2. `cgeB`

- **K06320** — cgeB; spore maturation protein CgeB

*Included because: >=1% and >=10 calls in soil*

> [!note] PRE-FILLED by Claude — review and edit. This is the protocol's mechanical default,
> not a judgement: with no Tier 1–5 evidence the protocol forbids ruling the family out, so
> COUNTS applies automatically. **Your judgement here is whether you accept that the evidence
> is genuinely absent** — i.e. whether my searching held up.

| | |
|---|---|
| **Part 1 — substrate** | UNDETERMINED — no evidence either way |
| **Part 2 — consequence** | UNDETERMINED — no evidence either way |
| **Evidence tier** | 6 (chemistry only; no Tier 1–5 available) |
| **Citations** | KEGG/EcoCyc for the reaction. No phage-specific study found. |
| **VERDICT** | **COUNTS** |
| **Confidence** | low |
| **Resolving experiment** | Determine whether the protein localises to the virion or to the host cell surface |

**Argument:**

No phage-specific functional evidence identified after three independent search strategies (thematic PubMed, per-gene PubMed, targeted preprint/web), and the gene is not discussed in any of the three source catalogue papers. Only Tier 6 evidence is available, which under the protocol cannot move a family out of the record. Defaults to COUNTS at low confidence. Flagged as **evidence-free** for separate reporting.

---

## 3. `dcm`

- **K00558** — DNMT1, dcm; DNA (cytosine-5)-methyltransferase 1 [EC:2.1.1.37]
- **K17398** — DNMT3A; DNA (cytosine-5)-methyltransferase 3A [EC:2.1.1.37]

*Included because: >=1% and >=10 calls in ocean_conservative; named by Martin et al.*

|                                            |                                                                           |
| ------------------------------------------ | ------------------------------------------------------------------------- |
| **Part 1 — substrate**                     | **Viral** — the phage's own cytosines                                     |
| **Part 2 — consequence**                   | **Genome protection** — a discrete lifecycle step                         |
| **Evidence tier**                          | 2                                                                         |
| **Citations**                              | Burke *et al.* 2021 *PNAS* [DOI](https://doi.org/10.1073/pnas.2026742118) |
| **VERDICT**                                | DOES NOT COUNT                                                            |
| **Confidence**                             | high                                                                      |
| **If unresolvable — resolving experiment** | -                                                                         |

**Argument (half a page):** The only direct work on phage-encoded C5-methyltransferases places them inside modification clusters whose described function is *"DNA packaging and evasion of host
restriction"*, acting on the phage's own cytosines. Anti-restriction is the standard reason a
phage carries a methyltransferase: methylate your genome in the host's pattern and the host's
endonucleases spare it. Both parts of the rule point viral. No study shows a phage `dcm`
methylating host DNA. Tier 2 is sufficient to move a family out.


---

## 4. `dsrC_tusE`

- **K11179** — tusE, dsrC; tRNA 2-thiouridine synthesizing protein E [EC:2.8.1.-]

*Included because: named by Martin et al.*

|                                            |                                                                                                                                                                               |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Part 1 — substrate**                     | **Cannot be determined from the accession**                                                                                                                                   |
| **Part 2 — consequence**                   | Host energy metabolism *or* tRNA thiolation, depending which gene it is                                                                                                       |
| **Evidence tier**                          | 3–4 (ecology); effectively 0 for gene identity                                                                                                                                |
| **Citations**                              | Stockdreher *et al.* 2012 *PLoS One* [DOI](https://doi.org/10.1371/journal.pone.0040785) · Kieft *et al.* 2021 *Nat Commun* [DOI](https://doi.org/10.1038/s41467-021-23698-5) |
| **VERDICT**                                | UNRESOLVABLE                                                                                                                                                                  |
| **Confidence**                             | high (in the unresolvability)<br>                                                                                                                                             |
| **If unresolvable — resolving experiment** |  **phylogenetic or HMM separation of DsrC from TusE**, then re-annotation of  <br>the calls                                                                                   |

**Argument (half a page):** This family is unlike any other in the list: the question is not what a phage does
with the gene, but whether anyone can tell **which gene it is**. DsrC and TusE share a fold and
the same persulfide chemistry but have entirely different destinations — DsrC feeds dissimilatory
sulfite reductase (energy metabolism), TusE feeds tRNA thiolation (housekeeping). KEGG merges
both into a single orthology group.

Kieft *et al.* make a substantial case that phage sulfur AMGs are real and selectively retained,
with expression profiles and a response to sulfur gradients — genuinely the strongest pro-AMG
evidence for any family here. But they write the gene as **`dsrC/tusE`**, with a slash. The
field's strongest phage-sulfur paper inherits the identical ambiguity in its own notation.

The evidence does not conflict about the biology; it conflicts about **which biology is present**.
That is undecidable from a merged accession, and the resolving experiment is unusually easy to
name. UNRESOLVABLE.


---

## 5. `dut`

- **K01520** — dut, DUT; dUTP diphosphatase [EC:3.6.1.23]

*Included because: >=1% and >=10 calls in ocean_conservative*

|                                            |                                                                                                                                                         |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Part 1 — substrate**                     | Shared nucleotide pool — not separable                                                                                                                  |
| **Part 2 — consequence**                   | Arguably replication; not demonstrated                                                                                                                  |
| **Evidence tier**                          | 4                                                                                                                                                       |
| **Citations**                              | Huang *et al.* 2021 *Environ Microbiol* [DOI](https://doi.org/10.1111/1462-2920.15412) · Nyíri *et al.* 2019 [DOI](https://doi.org/10.3390/biom9090488) |
| **VERDICT**                                | **COUNTS**                                                                                                                                              |
| **Confidence**                             | low                                                                                                                                                     |
| **If unresolvable — resolving experiment** | Isotopically track dUMP produced by phage dUTPase into phage versus host DNA during infection                                                           |

**Argument (half a page): The intuition here is strong — a phage dUTPase is *obviously* about phage DNA — but
intuition is Tier 6, and the protocol explicitly forbids Tier 6 alone from moving a family out.
The available Tier 2 work on phage dUTPases concerns their **non-enzymatic** binding to the Stl
repressor, a different function entirely; the Tier 4 evidence places dUTPase in nucleotide-pathway
AMG sets, which describes the pathway rather than showing who benefits. dUTPase also protects the
pool it draws on, and during infection host and phage draw on the same pool.

No positive Tier 1–5 evidence that the dUTPase function is viral-directed. **Defaults to COUNTS,
and I record my discomfort with that**: this is the protocol being deliberately hard to satisfy,
working as designed.


---

## 6. `folate`

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

|                                            |                                                                                                                   |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| **Part 1 — substrate**                     | GTP → shared; product routes to host cofactor **or** phage DNA                                                    |
| **Part 2 — consequence**                   | Genuinely both                                                                                                    |
| **Evidence tier**                          | 2                                                                                                                 |
| **Citations**                              | Thiaville *et al.* 2016 *PNAS* [DOI](https://doi.org/10.1073/pnas.1518570113)                                     |
| **VERDICT**                                | **UNRESOLVABLE**                                                                                                  |
| **Confidence**                             | high (in the unresolvability)                                                                                     |
| **If unresolvable — resolving experiment** | Metabolic flux from `folE` in infected cells: does the pterin output go to tetrahydrofolate or to 7-deazaguanine? |

**Argument (half a page):** `folE`/GTP cyclohydrolase I is the first committed step of folate biosynthesis
**and** the entry point to queuosine biosynthesis; `folE2` sits at the same branch. The folate
route is host cofactor metabolism. The queuosine route leads, on Thiaville's evidence, to
7-deazaguanine derivatives detected in phage DNA.

Both destinations are real and documented. The gene does not say which one the flux takes, and
neither does the annotation. This is the definition of undecidable-on-current-evidence, and the
resolving experiment is a flux measurement nobody has done.

Note the accession list also contains unambiguously host-directed folate enzymes (`folA`, `folD`,
`metH`). **The family is heterogeneous**, which is itself an argument for reporting it separately
rather than as a single verdict — flagged for the write-up.


---

## 7. `galE`

- **K01784** — galE, GALE; UDP-glucose 4-epimerase [EC:5.1.3.2]

*Included because: >=1% and >=10 calls in ocean_conservative, soil*

|                                            |                                                                                                                       |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| **Part 1 — substrate**                     | Host nucleotide-sugar pool                                                                                            |
| **Part 2 — consequence**                   | Not determined — feeds many pathways                                                                                  |
| **Evidence tier**                          | 6                                                                                                                     |
| **Citations**                              | KEGG K01784. Block literature (Appendix A of [[Evidence Dossiers]]) concerns the transfer step, not precursor supply. |
| **VERDICT**                                | COUNTS                                                                                                                |
| **Confidence**                             | low                                                                                                                   |
| **If unresolvable — resolving experiment** | Determine the destination of UDP-galactose produced by the phage enzyme — surface glycan or elsewhere                 |

**Argument (half a page): ** A precursor enzyme whose product feeds surface glycans among other destinations.
The demonstrated phage biology in this block concerns glycosyltransferases **transferring** sugars
onto the host surface; `galE` merely supplies building blocks. Extending that reasoning to the
precursor is an assumption, not a finding. No phage-specific evidence. Defaults to COUNTS.


---

## 8. `glmS`

- **K00820** — glmS, GFPT; glutamine---fructose-6-phosphate transaminase (isomerizing) [EC:2.6.1.16]

*Included because: >=1% and >=10 calls in soil*

|                                            |                                             |
| ------------------------------------------ | ------------------------------------------- |
| **Part 1 — substrate**                     | Host central metabolism                     |
| **Part 2 — consequence**                   | Not determined                              |
| **Evidence tier**                          | 6                                           |
| **Citations**                              | KEGG K00820. No phage-specific study found. |
| **VERDICT**                                | COUNTS                                      |
| **Confidence**                             | high                                        |
| **If unresolvable — resolving experiment** | As §7, for glucosamine-6-phosphate          |

**Argument (half a page): ** The committed entry to amino-sugar biosynthesis, sitting further upstream than
almost anything else in this block — its product feeds peptidoglycan, LPS and teichoic acids,
i.e. most of the cell envelope. The further upstream an enzyme sits, the weaker any claim that it
serves one specific downstream purpose. Defaults to COUNTS.


---

## 9. `glycoside_hydrolase`

- **K01179** — E3.2.1.4; endoglucanase [EC:3.2.1.4]
- **K01185** — E3.2.1.17; lysozyme [EC:3.2.1.17]
- **K01187** — malZ; alpha-glucosidase [EC:3.2.1.20]
- **K01190** — lacZ; beta-galactosidase [EC:3.2.1.23]
- **K01199** — EGLC; glucan endo-1,3-beta-D-glucosidase [EC:3.2.1.39]
- **K03791** — K03791; putative chitinase

*Included because: named by Martin et al.*

|                                            |                                                                                   |
| ------------------------------------------ | --------------------------------------------------------------------------------- |
| **Part 1 — substrate**                     | **Host** — cell wall peptidoglycan                                                |
| **Part 2 — consequence**                   | **Entry / egress** — discrete lifecycle steps                                     |
| **Evidence tier**                          | 1-2                                                                               |
| **Citations**                              | Yuan & Gao 2016 *Front Microbiol* [DOI](https://doi.org/10.3389/fmicb.2016.00745) |
| **VERDICT**                                | DOES NOT COUNT                                                                    |
| **Confidence**                             | high                                                                              |
| **If unresolvable — resolving experiment** | -                                                                                 |

**Argument (half a page):** ** This is the family the two-part rule was designed for. The substrate is a host
molecule, so Part 1 alone would let it count — but structural proteomics of a *Bacillus* jumbo
phage found a glycoside hydrolase **physically in the virion, interacting with the baseplate
protein**, with lytic activity against the host, proposed to *"facilitate the injection of the
phage genome during infection by forming pores on the bacterial cell wall."*

That is entry: a discrete lifecycle step. Endolysins do the same at egress. Nothing in the phage
literature supports the alternative reading, in which a phage-encoded glycoside hydrolase
liberates usable sugars for host metabolism.

Note this verdict applies to the **123 calls** surviving the `PF13385` exclusion, not the 21,690
before it.


---

## 10. `glycosyltransferase`

- **K00754** — bshA; L-malate glycosyltransferase [EC:2.4.1.-]
- **K03669** — mdoH; membrane glycosyltransferase [EC:2.4.1.-]
- **K03814** — mtgA; peptidoglycan glycosyltransferase [EC:2.4.99.28]
- **K07270** — K07270; glycosyl transferase, family 25
- **K15521** — mshA; D-inositol-3-phosphate glycosyltransferase [EC:2.4.1.250]

*Included because: >=1% and >=10 calls in soil; named by Martin et al.*

|                                            |                                                                                                                                                                                                               |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Part 1 — substrate**                     | **Host** — O-antigen, LPS, teichoic acid                                                                                                                                                                      |
| **Part 2 — consequence**                   | **Rule underdetermines** - see argument                                                                                                                                                                       |
| **Evidence tier**                          | 2                                                                                                                                                                                                             |
| **Citations**                              | Mann *et al.* 2015 *JBC* [DOI](https://doi.org/10.1074/jbc.M115.660803) · Sun *et al.* 2013 [DOI](https://doi.org/10.1186/1471-2180-13-39) · Sumrall *et al.* 2021 [DOI](https://doi.org/10.1128/JB.00136-21) |
| **VERDICT**                                | COUNTS                                                                                                                                                                                                        |
| **Confidence**                             | low                                                                                                                                                                                                           |
| **If unresolvable — resolving experiment** | Determine whether phage-mediated serotype conversion alters host metabolic flux beyond the glycan itself                                                                                                      |

**Argument (half a page): ** Phage-encoded glycosyltransferases
demonstrably modify the **host's** O-antigen, producing serotype conversion — which changes the
phage receptor. Part 1 is unambiguously host.

Part 2 is where the rule fails. Serotype conversion is **not** sustaining or redirecting host
metabolism in the sense the field's claim requires — the host's central metabolism is unchanged,
only its surface decoration. But nor is it one of the five listed lifecycle steps: it is
superinfection exclusion and host-range control, which the rule does not enumerate.

**The protocol has no category for "the rule cannot classify this."** Given that, and given the
default, the conservative reading applies: COUNTS, at low confidence, with the underdetermination
recorded explicitly rather than resolved by preference. Chunk 4 found the field's own criteria
have exactly this defect; ours does too, and saying so is stronger than hiding it.


---

## 11. `gmd`

- **K01711** — gmd, GMDS; GDPmannose 4,6-dehydratase [EC:4.2.1.47]

*Included because: >=1% and >=10 calls in ocean_conservative, soil*

|                                            |                                                           |
| ------------------------------------------ | --------------------------------------------------------- |
| **Part 1 — substrate**                     | Host nucleotide-sugar pool                                |
| **Part 2 — consequence**                   | Not determined                                            |
| **Evidence tier**                          | 6                                                         |
| **Citations**                              | KEGG K01711. Block literature concerns the transfer step. |
| **VERDICT**                                | COUNTS                                                    |
| **Confidence**                             | low                                                       |
| **If unresolvable — resolving experiment** | As §7, for GDP-fucose                                     |

**Argument (half a page): ** A precursor enzyme, though more surface-committed than `galE` since fucose is
largely a surface sugar. That tilt is worth noting but is not evidence. Defaults to COUNTS.


---

## 12. `hisF`

- **K02500** — hisF; imidazole glycerol-phosphate synthase subunit HisF [EC:4.3.2.10]

*Included because: >=1% and >=10 calls in soil*

> [!note] PRE-FILLED by Claude — review and edit. This is the protocol's mechanical default,
> not a judgement: with no Tier 1–5 evidence the protocol forbids ruling the family out, so
> COUNTS applies automatically. **Your judgement here is whether you accept that the evidence
> is genuinely absent** — i.e. whether my searching held up.

| | |
|---|---|
| **Part 1 — substrate** | UNDETERMINED — no evidence either way |
| **Part 2 — consequence** | UNDETERMINED — no evidence either way |
| **Evidence tier** | 6 (chemistry only; no Tier 1–5 available) |
| **Citations** | KEGG/EcoCyc for the reaction. No phage-specific study found. |
| **VERDICT** | **COUNTS** |
| **Confidence** | low |
| **Resolving experiment** | Test whether the phage copy complements a histidine auxotroph; measure histidine flux in infected cells |

**Argument:**

No phage-specific functional evidence identified after three independent search strategies (thematic PubMed, per-gene PubMed, targeted preprint/web), and the gene is not discussed in any of the three source catalogue papers. Only Tier 6 evidence is available, which under the protocol cannot move a family out of the record. Defaults to COUNTS at low confidence. Flagged as **evidence-free** for separate reporting.

---

## 13. `HMGCL`

- **K01640** — HMGCL, hmgL; hydroxymethylglutaryl-CoA lyase [EC:4.1.3.4]

*Included because: >=1% and >=10 calls in ocean_conservative*

|                          |                                                                                                           |
| ------------------------ | --------------------------------------------------------------------------------------------------------- |
| **Part 1 — substrate**   | UNDETERMINED — no evidence either way                                                                     |
| **Part 2 — consequence** | UNDETERMINED — no evidence either way                                                                     |
| **Evidence tier**        | 6 (chemistry only; no Tier 1–5 available)                                                                 |
| **Citations**            | KEGG/EcoCyc for the reaction. No phage-specific study found.                                              |
| **VERDICT**              | **COUNTS**                                                                                                |
| **Confidence**           | low                                                                                                       |
| **Resolving experiment** | Determine the substrate of the phage enzyme; test whether infection alters host leucine/ketone catabolism |

**Argument:**

No phage-specific functional evidence identified after three independent search strategies (thematic PubMed, per-gene PubMed, targeted preprint/web), and the gene is not discussed in any of the three source catalogue papers. Only Tier 6 evidence is available, which under the protocol cannot move a family out of the record. Defaults to COUNTS at low confidence. Flagged as **evidence-free** for separate reporting.

---

## 14. `IMPDH`

- **K00088** — IMPDH, guaB; IMP dehydrogenase [EC:1.1.1.205]

*Included because: >=1% and >=10 calls in ocean_conservative*

|                                            |                                                                                           |
| ------------------------------------------ | ----------------------------------------------------------------------------------------- |
| **Part 1 — substrate**                     | Shared nucleotide pool                                                                    |
| **Part 2 — consequence**                   | Arguably replication; not demonstrated                                                    |
| **Evidence tier**                          | 6                                                                                         |
| **Citations**                              | KEGG K00088. No functional study of a phage-encoded IMPDH found.                          |
| **VERDICT**                                | COUNTS                                                                                    |
| **Confidence**                             | low                                                                                       |
| **If unresolvable — resolving experiment** | As §5 — track guanine nucleotides produced by the phage enzyme into phage versus host DNA |

**Argument (half a page): ** The rate-limiting step of guanine nucleotide biosynthesis, and structurally the
same problem as `dut` and `nrdH`: during infection host and phage draw on one pool. The
mechanistic case that this serves phage replication is Tier 6, which cannot rule a family out.
Defaults to COUNTS.

Worth recording that KEGG places IMPDH in **09104 Nucleotide metabolism** — the category the
wastewater paper's own methods exclude, which is a Chunk 4 point rather than a verdict.


---

## 15. `iscU`

- **K04488** — iscU, nifU; nitrogen fixation protein NifU and related proteins

*Included because: >=1% and >=10 calls in ocean_conservative*

> [!note] PRE-FILLED by Claude — review and edit. This is the protocol's mechanical default,
> not a judgement: with no Tier 1–5 evidence the protocol forbids ruling the family out, so
> COUNTS applies automatically. **Your judgement here is whether you accept that the evidence
> is genuinely absent** — i.e. whether my searching held up.

| | |
|---|---|
| **Part 1 — substrate** | UNDETERMINED — no evidence either way |
| **Part 2 — consequence** | UNDETERMINED — no evidence either way |
| **Evidence tier** | 6 (chemistry only; no Tier 1–5 available) |
| **Citations** | KEGG/EcoCyc for the reaction. No phage-specific study found. |
| **VERDICT** | **COUNTS** |
| **Confidence** | low |
| **Resolving experiment** | Test Fe-S cluster assembly by the phage protein, and identify which apo-proteins it loads — host or phage |

**Argument:**

No phage-specific functional evidence identified after three independent search strategies (thematic PubMed, per-gene PubMed, targeted preprint/web), and the gene is not discussed in any of the three source catalogue papers. Only Tier 6 evidence is available, which under the protocol cannot move a family out of the record. Defaults to COUNTS at low confidence. Flagged as **evidence-free** for separate reporting.

---

## 16. `K07336`

- **K07336** — K07336; PKHD-type hydroxylase [EC:1.14.11.-]

*Included because: >=1% and >=10 calls in ocean_conservative*

> [!note] PRE-FILLED by Claude — review and edit. This is the protocol's mechanical default,
> not a judgement: with no Tier 1–5 evidence the protocol forbids ruling the family out, so
> COUNTS applies automatically. **Your judgement here is whether you accept that the evidence
> is genuinely absent** — i.e. whether my searching held up.

| | |
|---|---|
| **Part 1 — substrate** | UNDETERMINED — no evidence either way |
| **Part 2 — consequence** | UNDETERMINED — no evidence either way |
| **Evidence tier** | 6 (chemistry only; no Tier 1–5 available) |
| **Citations** | KEGG/EcoCyc for the reaction. No phage-specific study found. |
| **VERDICT** | **COUNTS** |
| **Confidence** | low |
| **Resolving experiment** | **Determine the substrate at all.** Uncharacterised 2OG-Fe(II) oxygenase; the gap is more basic than for the others |

**Argument:**

No phage-specific functional evidence identified after three independent search strategies (thematic PubMed, per-gene PubMed, targeted preprint/web), and the gene is not discussed in any of the three source catalogue papers. Only Tier 6 evidence is available, which under the protocol cannot move a family out of the record. Defaults to COUNTS at low confidence. Flagged as **evidence-free** for separate reporting.

---

## 17. `manB`

- **K01840** — manB; phosphomannomutase [EC:5.4.2.8]

*Included because: >=1% and >=10 calls in ocean_conservative*

|                                            |                                                           |
| ------------------------------------------ | --------------------------------------------------------- |
| **Part 1 — substrate**                     | Host central metabolism                                   |
| **Part 2 — consequence**                   | Not determined                                            |
| **Evidence tier**                          | 6                                                         |
| **Citations**                              | KEGG K01840. Block literature concerns the transfer step. |
| **VERDICT**                                | COUNTS                                                    |
| **Confidence**                             | low                                                       |
| **If unresolvable — resolving experiment** | As §7, for GDP-mannose                                    |

**Argument (half a page):**  Precursor enzyme feeding GDP-mannose, which has surface and non-surface
destinations. Same reasoning as §7. Defaults to COUNTS.


---

## 18. `NAMPT`

- **K03462** — NAMPT; nicotinamide phosphoribosyltransferase [EC:2.4.2.12]

*Included because: >=1% and >=10 calls in soil*

|                                            |                                                                                                                                                   |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Part 1 — substrate**                     | Shared cofactor pool (NAD⁺)                                                                                                                       |
| **Part 2 — consequence**                   | Authors propose phage-directed use; not demonstrated as such                                                                                      |
| **Evidence tier**                          | 1–2                                                                                                                                               |
| **Citations**                              | Lee, Li & Miller 2017 *J Bacteriol* [DOI](https://doi.org/10.1128/JB.00855-16)                                                                    |
| **VERDICT**                                | COUNTS                                                                                                                                            |
| **Confidence**                             | low                                                                                                                                               |
| **If unresolvable — resolving experiment** | Determine whether NAD⁺ produced by the phage pathway is preferentially consumed by phage-directed ADP-ribosylation versus general host metabolism |

**Argument (half a page):** This is the hardest COUNTS in the set, and the reasoning matters.

The evidence is genuinely Tier 1–2: the phage enzyme was purified, shown active, and
**complements an *E. coli* mutant**; transcription was measured during the early and delayed-early
period of infection. But what that establishes is that the enzyme **works and is expressed** — not
who consumes the product. The authors' interpretation (DNA precursor synthesis and
ADP-ribosylation of phage transcription/translation machinery) is a reading of T4-type biology
generally, not a measurement in this system, and their own framing calls it a *"metabolic resource
control point"*, which reads host-directed.

NAD⁺ is a universal cofactor and the pool is shared. Tier 1–2 evidence of activity is not Tier 1–5
evidence that the **consequence** is viral. Defaults to COUNTS at low confidence.

---

## 19. `nodU`

- **K00612** — nodU; carbamoyltransferase [EC:2.1.3.-]

*Included because: >=1% and >=10 calls in ocean_conservative*

> [!note] PRE-FILLED by Claude — review and edit. This is the protocol's mechanical default,
> not a judgement: with no Tier 1–5 evidence the protocol forbids ruling the family out, so
> COUNTS applies automatically. **Your judgement here is whether you accept that the evidence
> is genuinely absent** — i.e. whether my searching held up.

| | |
|---|---|
| **Part 1 — substrate** | UNDETERMINED — no evidence either way |
| **Part 2 — consequence** | UNDETERMINED — no evidence either way |
| **Evidence tier** | 6 (chemistry only; no Tier 1–5 available) |
| **Citations** | KEGG/EcoCyc for the reaction. No phage-specific study found. |
| **VERDICT** | **COUNTS** |
| **Confidence** | low |
| **Resolving experiment** | Identify the carbamoylation target — host surface polysaccharide, or a phage structural protein |

**Argument:**

No phage-specific functional evidence identified after three independent search strategies (thematic PubMed, per-gene PubMed, targeted preprint/web), and the gene is not discussed in any of the three source catalogue papers. Only Tier 6 evidence is available, which under the protocol cannot move a family out of the record. Defaults to COUNTS at low confidence. Flagged as **evidence-free** for separate reporting.

---

## 20. `nrdH`

- **K06191** — nrdH; glutaredoxin-like protein NrdH

*Included because: >=1% and >=10 calls in soil*

|                                            |                                                                                                                                                               |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Part 1 — substrate**                     | Shared — ribonucleotide pool                                                                                                                                  |
| **Part 2 — consequence**                   | Not separable during infection                                                                                                                                |
| **Evidence tier**                          | 4-5                                                                                                                                                           |
| **Citations**                              | Sakowski *et al.* 2021 *Nat Microbiol* [DOI](https://doi.org/10.1038/s41564-021-00873-4) · Huang *et al.* 2021 [DOI](https://doi.org/10.1111/1462-2920.15412) |
| **VERDICT**                                | COUNTS                                                                                                                                                        |
| **Confidence**                             | low                                                                                                                                                           |
| **If unresolvable — resolving experiment** | Separate the phage and host dNTP pools during infection — which may not be experimentally possible, and if so this family becomes genuinely undecidable       |

**Argument (half a page):** Redox partner of class Ib ribonucleotide reductase. The Tier 5 signal is real and
interesting: phage RNRs are phylogenetically distinct enough from host copies to serve as a
**viral marker gene**, which argues against incidental acquisition and for specialisation. But
specialisation *for what* is not shown.

The deeper problem is that during lytic infection there is only one dNTP pool, so "does this
serve the host or the phage" may not be a well-formed question experimentally. I have not marked
this UNRESOLVABLE, because the evidence does not conflict — it simply does not reach. Under the
protocol that is unresearched, not unresolvable. Defaults to COUNTS.


---

## 21. `P4HA`

- **K00472** — P4HA; prolyl 4-hydroxylase [EC:1.14.11.2]

*Included because: >=1% and >=10 calls in ocean_conservative*


> [!warning] PENDING — do the library check before accepting this
> A lead suggests prolyl 4-hydroxylase appears in megaphage virion proteomics (*npj Viruses* 2025), which I could not verify behind a login wall. **If it does, this becomes a structural verdict and leaves the evidence-free group.** ~15 minutes.

|                          |                                                                                                                           |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| **Part 1 — substrate**   | Undetermined — phage structural protein, host ribosomal protein, or free proline                                          |
| **Part 2 — consequence** | Undetermined; contingent on Part 1                                                                                        |
| **Evidence tier**        | 5 (was 6 — virion presence now verified)                                                                                  |
| **Citations**            | KEGG K00472 · Buchan _et al._ 2025 _npj Viruses_ [DOI](https://doi.org/10.1038/s44298-025-00150-9)                        |
| **VERDICT**              | **COUNTS**                                                                                                                |
| **Confidence**           | low                                                                                                                       |
| **Resolving experiment** | Foldseek ps183 model — vP4H vs YcfD ribosomal-oxygenase clade; scan phage G ORFs for (Gly-X-Y)ₙ in tail fiber / baseplate |

**Argument:**

**Argument:** 2OG-dependent proline hydroxylation, a structural modification. The lead is now verified: Buchan _et al._ detect ps183/gp281 by LC-MS/MS in purified phage G virions — a genuine phage, not the algal virus that muddied the earlier search. But the authors file it under translation and amino-acid metabolism, not among their 16 detected structural proteins, and phage G packages many enzymes as cargo (RNR, DNA pol, gyrase). At 104/668 ORFs detected, packaging alone is weak evidence.

§9's trigger has two clauses — virion presence _and_ a phage structural hydroxylation target — and only the first is met. The Argument as previously written flipped on the first clause alone, which contradicts the row above it. Substrate remains unknown, so COUNTS stands and the resolving experiment narrows to substrate identification.

---

## 22. `phoH`

- **K06217** — phoH, phoL; phosphate starvation-inducible protein PhoH and related proteins

*Included because: >=1% and >=10 calls in ocean_conservative*

|                                            |                                                                                                                                                |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Part 1 — substrate**                     | **Host** — phosphate acquisition machinery                                                                                                     |
| **Part 2 — consequence**                   | **Sustains host phosphate scavenging** under limitation                                                                                        |
| **Evidence tier**                          | 4-5                                                                                                                                            |
| **Citations**                              | Goldsmith *et al.* 2011 *AEM* [DOI](https://doi.org/10.1128/AEM.05531-11) · Huang *et al.* 2021 [DOI](https://doi.org/10.1111/1462-2920.15412) |
| **VERDICT**                                | COUNTS                                                                                                                                         |
| **Confidence**                             | moderate                                                                                                                                       |
| **If unresolvable — resolving experiment** | Delete or express phage `phoH` and measure phosphate uptake in infected versus uninfected cells under limitation                               |

**Argument (half a page):** Unlike most COUNTS verdicts here, this one is **supported** rather than merely
defaulted. Pho regulon genes appear in ~40% of marine phage genomes against 4% of non-marine ones
— phages carry this **where phosphate is limiting**. That ecological correlation is difficult to
explain except by phosphate acquisition mattering in the infected cell, and phosphate acquisition
is host machinery doing host work.

The counter-argument — that phage replication is itself phosphate-expensive — is real but does not
displace the substrate, which remains the host's uptake system. The phylogenetic distinctness of
phage `phoH` is a caution against assuming the host function is preserved intact, hence moderate
rather than high confidence.


---

## 23. `psbA`

- **K02703** — psbA; photosystem II P680 reaction center D1 protein [EC:1.10.3.9]

*Included because: control*

|                                            |                                                                                                                                                                                                                                                             |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Part 1 — substrate**                     | **Host** — the host's thylakoid membrane                                                                                                                                                                                                                    |
| **Part 2 — consequence**                   | **Sustains host photosynthesis**, measured                                                                                                                                                                                                                  |
| **Evidence tier**                          | 1-2                                                                                                                                                                                                                                                         |
| **Citations**                              | Sullivan *et al.* 2006 *PLoS Biol* [DOI](https://doi.org/10.1371/journal.pbio.0040234) · Sieradzki *et al.* 2019 *Nat Commun* [DOI](https://doi.org/10.1038/s41467-019-09106-z) · Lindell *et al.* 2007 *Nature* [DOI](https://doi.org/10.1038/nature06130) |
| **VERDICT**                                | COUNTS                                                                                                                                                                                                                                                      |
| **Confidence**                             | high                                                                                                                                                                                                                                                        |
| **If unresolvable — resolving experiment** | -                                                                                                                                                                                                                                                           |

**Argument (half a page):** The phage protein is inserted into the **host's** photosystem, replacing a host
subunit that photodamage continually destroys, and the measured consequence is that host
photosynthesis keeps running during infection — with more than half of all `psbA` expression
viral in some samples. Both parts point host.

The objection that the phage does this only to finish replicating is true and **generalises to
everything a phage does**, which is precisely why Part 2 asks about discrete lifecycle steps
rather than ultimate benefit. Maintaining a functioning host photosystem is not one of entry,
genome protection, replication, assembly or egress.


---

## 24. `psbD`

- **K02706** — psbD; photosystem II P680 reaction center D2 protein [EC:1.10.3.9]

*Included because: control*

|                                            |                                                                            |
| ------------------------------------------ | -------------------------------------------------------------------------- |
| **Part 1 — substrate**                     | **Host** thylakoid                                                         |
| **Part 2 — consequence**                   | **Sustains host photosynthesis**                                           |
| **Evidence tier**                          | 2                                                                          |
| **Citations**                              | Sullivan *et al.* 2006 [DOI](https://doi.org/10.1371/journal.pbio.0040234) |
| **VERDICT**                                | COUNTS                                                                     |
| **Confidence**                             | high                                                                       |
| **If unresolvable — resolving experiment** | -                                                                          |

**Argument (half a page):** Same reasoning as §23, and judged separately rather than inherited. The
distinguishing fact is that `psbD` occurs in about half as many phages as `psbA` and its presence
correlates with **broad host range**, which Sullivan *et al.* attribute to constraints on coupling
viral and host PsbA–PsbD across divergent hosts. That is compatibility engineering in service of
the same host-directed function, not a different function — so the verdict follows `psbA`, with
slightly lower evidentiary depth.


---

## 25. `pseB`

- **K15894** — pseB, fnlA, wbjB; UDP-N-acetylglucosamine 4,6-dehydratase [EC:4.2.1.115]

*Included because: >=1% and >=10 calls in soil*

|                                            |                                             |
| ------------------------------------------ | ------------------------------------------- |
| **Part 1 — substrate**                     | Host nucleotide-sugar pool                  |
| **Part 2 — consequence**                   | Not determined                              |
| **Evidence tier**                          | 6                                           |
| **Citations**                              | KEGG K15894. No phage-specific study found. |
| **VERDICT**                                | COUNTS                                      |
| **Confidence**                             | low                                         |
| **If unresolvable — resolving experiment** | As §7, for pseudaminic acid                 |

**Argument (half a page):** First step to pseudaminic acid, a surface-committed sugar with few destinations
outside surface glycans and flagellar glycosylation. That commitment weakens the "feeds many
pathways" defence relative to `galE` — but a strong prior about destination is still not evidence
about consequence. Defaults to COUNTS.


---

## 26. `queuosine`

- **K01737** — queD, ptpS, PTS; 6-pyruvoyltetrahydropterin/6-carboxytetrahydropterin synthase [EC:4.2.3.12 4.1.2.50]
- **K06879** — queF; 7-cyano-7-deazaguanine reductase [EC:1.7.1.13]
- **K06920** — queC; 7-cyano-7-deazaguanine synthase [EC:6.3.4.20]
- **K09457** — queF; 7-cyano-7-deazaguanine reductase [EC:1.7.1.13]
- **K10026** — queE; 7-carboxy-7-deazaguanine synthase [EC:4.3.99.3]

*Included because: >=1% and >=10 calls in ocean_conservative, soil; named by Martin et al.*

|                                            |                                                                                                                                                                                                                                                           |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Part 1 — substrate**                     | **Both demonstrated** — tRNA (host) and phage DNA (viral)                                                                                                                                                                                                 |
| **Part 2 — consequence**                   | Translation fidelity *or* genome protection                                                                                                                                                                                                               |
| **Evidence tier**                          | 2                                                                                                                                                                                                                                                         |
| **Citations**                              | Thiaville *et al.* 2016 *PNAS* [DOI](https://doi.org/10.1073/pnas.1518570113) · Hutinet *et al.* 2016 *RNA Biol* [DOI](https://doi.org/10.1080/15476286.2016.1265200) · de Crécy-Lagard *et al.* 2024 *MMBR* [DOI](https://doi.org/10.1128/mmbr.00199-23) |
| **VERDICT**                                | UNRESOLVABLE                                                                                                                                                                                                                                              |
| **Confidence**                             | high (in the unresolvability)                                                                                                                                                                                                                             |
| **If unresolvable — resolving experiment** | Systematic detection of 7-deazaguanine derivatives in the DNA of phages carrying these genes versus those lacking them. Done for a single phage; never done systematically                                                                                |

**Argument (half a page):** This is the case UNRESOLVABLE exists for. The pathway demonstrably does **both
things** — queuosine goes into tRNA in some organisms, and 7-deazaguanine derivatives have been
chemically detected **in the DNA of *E. coli* phage 9g**, where the attributed function is
protection against endonucleases.

Critically, **the genes do not distinguish the two uses**: a phage modifying its own DNA needs the
same enzymes as one feeding host tRNA modification. The evidence conflicts, it conflicts at the
same tier, and there is a clean experiment that would settle it which nobody has run.

Marking this DOES NOT COUNT would be adopting Martin *et al.*'s reading on Tier 6 grounds, which
the protocol forbids. Marking it COUNTS would ignore direct chemical evidence of the product in
phage DNA. Neither is honest.


---

## 27. `raxST`

- **K13472** — raxST; sulfotransferase

*Included because: >=1% and >=10 calls in ocean_conservative*


| | |
|---|---|
| **Part 1 — substrate** | UNDETERMINED — no evidence either way |
| **Part 2 — consequence** | UNDETERMINED — no evidence either way |
| **Evidence tier** | 6 (chemistry only; no Tier 1–5 available) |
| **Citations** | KEGG/EcoCyc for the reaction. No phage-specific study found. |
| **VERDICT** | **COUNTS** |
| **Confidence** | low |
| **Resolving experiment** | Identify the sulfation target |

**Argument:**

No phage-specific functional evidence identified after three independent search strategies (thematic PubMed, per-gene PubMed, targeted preprint/web), and the gene is not discussed in any of the three source catalogue papers. Only Tier 6 evidence is available, which under the protocol cannot move a family out of the record. Defaults to COUNTS at low confidence. Flagged as **evidence-free** for separate reporting.

---

## 28. `rfbB`

- **K01710** — rfbB, rmlB, rffG; dTDP-glucose 4,6-dehydratase [EC:4.2.1.46]

*Included because: >=1% and >=10 calls in soil*

|                                            |                                                           |
| ------------------------------------------ | --------------------------------------------------------- |
| **Part 1 — substrate**                     | Host nucleotide-sugar pool                                |
| **Part 2 — consequence**                   | Not determined                                            |
| **Evidence tier**                          | 6                                                         |
| **Citations**                              | KEGG K01710. Block literature concerns the transfer step. |
| **VERDICT**                                | COUNTS                                                    |
| **Confidence**                             | low                                                       |
| **If unresolvable — resolving experiment** | As §7, for dTDP-rhamnose                                  |

**Argument (half a page):** Second step of the dTDP-L-rhamnose pathway; rhamnose is a major O-antigen sugar, so
this is surface-committed like `pseB`. Same reasoning: strong prior about destination, no evidence
about consequence. Defaults to COUNTS.


---

## 29. `rfbC`

- **K20444** — rfbC; O-antigen biosynthesis protein [EC:2.4.1.-]

*Included because: >=1% and >=10 calls in soil*

|                                            |                                                                                                                                      |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Part 1 — substrate**                     | **Host** — O-antigen                                                                                                                 |
| **Part 2 — consequence**                   | **Rule underdetermines**, as §10                                                                                                     |
| **Evidence tier**                          | 2 (via the block literature, which is about this exact process)                                                                      |
| **Citations**                              | Mann *et al.* 2015 [DOI](https://doi.org/10.1074/jbc.M115.660803) · Sun *et al.* 2013 [DOI](https://doi.org/10.1186/1471-2180-13-39) |
| **VERDICT**                                | COUNTS                                                                                                                               |
| **Confidence**                             | low                                                                                                                                  |
| **If unresolvable — resolving experiment** | As §10                                                                                                                               |

**Argument (half a page):** KEGG names this **O-antigen biosynthesis** directly, and its EC number (2.4.1.-)
makes it a glycosyltransferase — so the Mann and Sun evidence about phage-mediated O-antigen
modification applies here more squarely than to any precursor enzyme.

That means the verdict must match §10, and for the same reason: Part 1 is host, but serotype
conversion is neither host metabolic modulation nor an enumerated lifecycle step, so the rule
underdetermines and the conservative default applies. **If §10 and §29 ever receive different
verdicts, that inconsistency needs explaining** — I have kept them aligned deliberately.


---

## 30. `speD`

- **K01611** — speD, AMD1; S-adenosylmethionine decarboxylase [EC:4.1.1.50]

*Included because: >=1% and >=10 calls in ocean_conservative*

|                                            |                                                                                                                  |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| **Part 1 — substrate**                     | Host SAM pool                                                                                                    |
| **Part 2 — consequence**                   | Not determined; virion packaging is plausible but not shown for these phages                                     |
| **Evidence tier**                          | 5-6                                                                                                              |
| **Citations**                              | KEGG K01611. Phage–polyamine literature exists but is old and organism-specific.                                 |
| **VERDICT**                                | COUNTS                                                                                                           |
| **Confidence**                             | low                                                                                                              |
| **If unresolvable — resolving experiment** | Determine whether spermidine produced during infection is packaged into virions or remains in the host cytoplasm |

**Argument (half a page):** Supplies the aminopropyl donor for spermidine. Spermidine is a structural component
of some phage virions, where its charge helps neutralise the packaged genome — which, if it
applied here, would make this assembly and parallel the terminase argument. But that literature is
decades old and organism-specific, and nothing connects it to the phages in these catalogues.
Defaults to COUNTS.


---

## 31. `tagD`

- **K00980** — tagD; glycerol-3-phosphate cytidylyltransferase [EC:2.7.7.39]

*Included because: >=1% and >=10 calls in ocean_conservative*

|                                            |                                                                                                                                    |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Part 1 — substrate**                     | Host — teichoic acid backbone                                                                                                      |
| **Part 2 — consequence**                   | Not determined                                                                                                                     |
| **Evidence tier**                          | 6                                                                                                                                  |
| **Citations**                              | KEGG K00980. Sumrall *et al.* 2021 concerns WTA **decoration**, not backbone synthesis. [DOI](https://doi.org/10.1128/JB.00136-21) |
| **VERDICT**                                | COUNTS                                                                                                                             |
| **Confidence**                             | low                                                                                                                                |
| **If unresolvable — resolving experiment** | As §7, for CDP-glycerol                                                                                                            |

**Argument (half a page):** Makes CDP-glycerol, the wall teichoic acid backbone donor. WTA **glycosylation** is
demonstrably the phage receptor in Gram-positives, but `tagD` builds the polymer, not the sugar
decoration that the receptor work concerns. The distinction matters and I have not elided it.
Defaults to COUNTS.


---

## 32. `TALDO1`

- **K00616** — TALDO1, talB, talA; transaldolase [EC:2.2.1.2]

*Included because: >=1% and >=10 calls in ocean_conservative*

|                                            |                                                                                                                                                          |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Part 1 — substrate**                     | **Host** — pentose phosphate pathway intermediates                                                                                                       |
| **Part 2 — consequence**                   | **Host carbon flux measurably redirected** — NADPH/NADP doubles                                                                                          |
| **Evidence tier**                          | 1-2                                                                                                                                                      |
| **Citations**                              | Thompson *et al.* 2011 *PNAS* [DOI](https://doi.org/10.1073/pnas.1102164108) · Lindell *et al.* 2007 *Nature* [DOI](https://doi.org/10.1038/nature06130) |
| **VERDICT**                                | COUNTS                                                                                                                                                   |
| **Confidence**                             | moderate                                                                                                                                                 |
| **If unresolvable — resolving experiment** | -                                                                                                                                                        |

**Argument (half a page):** 
The phage enzyme was purified and shown functional; it is the most prevalent PPP gene in
cyanophages; and **the host NADPH/NADP ratio doubles in infected cells.** That is a measured
change in host metabolic state caused by a phage enzyme acting on host metabolites. Part 1 host,
Part 2 host.

The authors themselves say the redirected output *"fuels deoxynucleotide biosynthesis for phage
replication"*, and Lindell shows `talC` co-transcribed with the replication module. **So the
purpose is viral.** But the protocol's Part 2 asks about the **consequence**, not the purpose —
deliberately, because purpose-based reasoning rules out everything including `psbA`.

The consequence is that host carbon flux is redirected, measurably. It counts. Confidence is
moderate rather than high because the purpose/consequence distinction is doing real work here and
a reasonable person applying the same rule could weigh it differently.

**This family is the clearest illustration in the whole set of why the AMG category is contested**
— and it should be discussed in the paper regardless of verdict.


---

## 33. `UGDH`

- **K00012** — UGDH, ugd; UDPglucose 6-dehydrogenase [EC:1.1.1.22]

*Included because: >=1% and >=10 calls in ocean_conservative, soil*

|                                            |                                                           |
| ------------------------------------------ | --------------------------------------------------------- |
| **Part 1 — substrate**                     | Host nucleotide-sugar pool                                |
| **Part 2 — consequence**                   | Not determined                                            |
| **Evidence tier**                          | 6                                                         |
| **Citations**                              | KEGG K00012. Block literature concerns the transfer step. |
| **VERDICT**                                | COUNTS                                                    |
| **Confidence**                             | low                                                       |
| **If unresolvable — resolving experiment** | As §7, for UDP-glucuronate                                |

**Argument (half a page):** Oxidises UDP-glucose to UDP-glucuronate, feeding capsule and acidic surface
polysaccharides. Surface-committed but a precursor. Same reasoning as §25 and §28. Defaults to
COUNTS.


---

## 34. `xtmA`

- **K07474** — xtmA; phage terminase small subunit

*Included because: control*

|                                            |                                                                 |
| ------------------------------------------ | --------------------------------------------------------------- |
| **Part 1 — substrate**                     | **Viral** — the phage genome                                    |
| **Part 2 — consequence**                   | **Assembly** — a discrete lifecycle step                        |
| **Evidence tier**                          | 1-2                                                             |
| **Citations**                              | Extensive; ~88 PubMed results for phage terminase DNA packaging |
| **VERDICT**                                | DOES NOT COUNT                                                  |
| **Confidence**                             | high                                                            |
| **If unresolvable — resolving experiment** | -                                                               |

**Argument (half a page):** The small subunit recognises the packaging initiation site on the phage genome and
regulates the large subunit. The substrate is phage DNA; the consequence is genome packaging.
No host-directed reading is constructible.



---

## 35. `xtmB`

- **K06909** — xtmB; phage terminase large subunit

*Included because: control*

|                                            |                              |
| ------------------------------------------ | ---------------------------- |
| **Part 1 — substrate**                     | **Viral** — the phage genome |
| **Part 2 — consequence**                   | Assembly                     |
| **Evidence tier**                          | 1–2                          |
| **Citations**                              | As §34                       |
| **VERDICT**                                | **DOES NOT COUNT**           |
| **Confidence**                             | high                         |
| **If unresolvable — resolving experiment** | -                            |

**Argument (half a page):**  The ATPase and nuclease of the packaging motor, translocating the genome into the
capsid against internal pressure. As §34.


---
