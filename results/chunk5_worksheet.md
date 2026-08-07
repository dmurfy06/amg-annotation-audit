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

|                                            |                               |
| ------------------------------------------ | ----------------------------- |
| **Part 1 — substrate**                     | viral                         |
| **Part 2 — consequence**                   | discrete lifecycle step       |
| **Evidence tier**                          | 2                             |
| **Citations**                              | Burke *et al.* (2021, *PNAS*) |
| **VERDICT**                                | DOES NOT COUNT                |
| **Confidence**                             | high                          |
| **If unresolvable — resolving experiment** |                               |

**Argument (half a page):**  The Burke paper places phage C5-MTases in modification clusters whose described function is
protecting the phage genome. Anti-restriction is the textbook reason a phage carries a
methyltransferase: methylate your own genome in the host's pattern and the host's endonucleases
ignore it. Genome protection is a discrete lifecycle step under the protocol's Part 2.


---

## 4. `dsrC_tusE`

- **K11179** — tusE, dsrC; tRNA 2-thiouridine synthesizing protein E [EC:2.8.1.-]

*Included because: named by Martin et al.*

| | |
|---|---|
| **Part 1 — substrate** | host / viral — *what does the product act on?* |
| **Part 2 — consequence** | sustains host metabolism / discrete lifecycle step |
| **Evidence tier** | 1–6 (see protocol) |
| **Citations** | |
| **VERDICT** | COUNTS / DOES NOT COUNT / UNRESOLVABLE |
| **Confidence** | high / low |
| **If unresolvable — resolving experiment** | |

**Argument (half a page):**


---

## 5. `dut`

- **K01520** — dut, DUT; dUTP diphosphatase [EC:3.6.1.23]

*Included because: >=1% and >=10 calls in ocean_conservative*

| | |
|---|---|
| **Part 1 — substrate** | host / viral — *what does the product act on?* |
| **Part 2 — consequence** | sustains host metabolism / discrete lifecycle step |
| **Evidence tier** | 1–6 (see protocol) |
| **Citations** | |
| **VERDICT** | COUNTS / DOES NOT COUNT / UNRESOLVABLE |
| **Confidence** | high / low |
| **If unresolvable — resolving experiment** | |

**Argument (half a page):**


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

| | |
|---|---|
| **Part 1 — substrate** | host / viral — *what does the product act on?* |
| **Part 2 — consequence** | sustains host metabolism / discrete lifecycle step |
| **Evidence tier** | 1–6 (see protocol) |
| **Citations** | |
| **VERDICT** | COUNTS / DOES NOT COUNT / UNRESOLVABLE |
| **Confidence** | high / low |
| **If unresolvable — resolving experiment** | |

**Argument (half a page):**


---

## 7. `galE`

- **K01784** — galE, GALE; UDP-glucose 4-epimerase [EC:5.1.3.2]

*Included because: >=1% and >=10 calls in ocean_conservative, soil*

| | |
|---|---|
| **Part 1 — substrate** | host / viral — *what does the product act on?* |
| **Part 2 — consequence** | sustains host metabolism / discrete lifecycle step |
| **Evidence tier** | 1–6 (see protocol) |
| **Citations** | |
| **VERDICT** | COUNTS / DOES NOT COUNT / UNRESOLVABLE |
| **Confidence** | high / low |
| **If unresolvable — resolving experiment** | |

**Argument (half a page):**


---

## 8. `glmS`

- **K00820** — glmS, GFPT; glutamine---fructose-6-phosphate transaminase (isomerizing) [EC:2.6.1.16]

*Included because: >=1% and >=10 calls in soil*

| | |
|---|---|
| **Part 1 — substrate** | host / viral — *what does the product act on?* |
| **Part 2 — consequence** | sustains host metabolism / discrete lifecycle step |
| **Evidence tier** | 1–6 (see protocol) |
| **Citations** | |
| **VERDICT** | COUNTS / DOES NOT COUNT / UNRESOLVABLE |
| **Confidence** | high / low |
| **If unresolvable — resolving experiment** | |

**Argument (half a page):**


---

## 9. `glycoside_hydrolase`

- **K01179** — E3.2.1.4; endoglucanase [EC:3.2.1.4]
- **K01185** — E3.2.1.17; lysozyme [EC:3.2.1.17]
- **K01187** — malZ; alpha-glucosidase [EC:3.2.1.20]
- **K01190** — lacZ; beta-galactosidase [EC:3.2.1.23]
- **K01199** — EGLC; glucan endo-1,3-beta-D-glucosidase [EC:3.2.1.39]
- **K03791** — K03791; putative chitinase

*Included because: named by Martin et al.*

| | |
|---|---|
| **Part 1 — substrate** | host / viral — *what does the product act on?* |
| **Part 2 — consequence** | sustains host metabolism / discrete lifecycle step |
| **Evidence tier** | 1–6 (see protocol) |
| **Citations** | |
| **VERDICT** | COUNTS / DOES NOT COUNT / UNRESOLVABLE |
| **Confidence** | high / low |
| **If unresolvable — resolving experiment** | |

**Argument (half a page):**


---

## 10. `glycosyltransferase`

- **K00754** — bshA; L-malate glycosyltransferase [EC:2.4.1.-]
- **K03669** — mdoH; membrane glycosyltransferase [EC:2.4.1.-]
- **K03814** — mtgA; peptidoglycan glycosyltransferase [EC:2.4.99.28]
- **K07270** — K07270; glycosyl transferase, family 25
- **K15521** — mshA; D-inositol-3-phosphate glycosyltransferase [EC:2.4.1.250]

*Included because: >=1% and >=10 calls in soil; named by Martin et al.*

| | |
|---|---|
| **Part 1 — substrate** | host / viral — *what does the product act on?* |
| **Part 2 — consequence** | sustains host metabolism / discrete lifecycle step |
| **Evidence tier** | 1–6 (see protocol) |
| **Citations** | |
| **VERDICT** | COUNTS / DOES NOT COUNT / UNRESOLVABLE |
| **Confidence** | high / low |
| **If unresolvable — resolving experiment** | |

**Argument (half a page):**


---

## 11. `gmd`

- **K01711** — gmd, GMDS; GDPmannose 4,6-dehydratase [EC:4.2.1.47]

*Included because: >=1% and >=10 calls in ocean_conservative, soil*

| | |
|---|---|
| **Part 1 — substrate** | host / viral — *what does the product act on?* |
| **Part 2 — consequence** | sustains host metabolism / discrete lifecycle step |
| **Evidence tier** | 1–6 (see protocol) |
| **Citations** | |
| **VERDICT** | COUNTS / DOES NOT COUNT / UNRESOLVABLE |
| **Confidence** | high / low |
| **If unresolvable — resolving experiment** | |

**Argument (half a page):**


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
| **Resolving experiment** | Determine the substrate of the phage enzyme; test whether infection alters host leucine/ketone catabolism |

**Argument:**

No phage-specific functional evidence identified after three independent search strategies (thematic PubMed, per-gene PubMed, targeted preprint/web), and the gene is not discussed in any of the three source catalogue papers. Only Tier 6 evidence is available, which under the protocol cannot move a family out of the record. Defaults to COUNTS at low confidence. Flagged as **evidence-free** for separate reporting.

---

## 14. `IMPDH`

- **K00088** — IMPDH, guaB; IMP dehydrogenase [EC:1.1.1.205]

*Included because: >=1% and >=10 calls in ocean_conservative*

| | |
|---|---|
| **Part 1 — substrate** | host / viral — *what does the product act on?* |
| **Part 2 — consequence** | sustains host metabolism / discrete lifecycle step |
| **Evidence tier** | 1–6 (see protocol) |
| **Citations** | |
| **VERDICT** | COUNTS / DOES NOT COUNT / UNRESOLVABLE |
| **Confidence** | high / low |
| **If unresolvable — resolving experiment** | |

**Argument (half a page):**


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

| | |
|---|---|
| **Part 1 — substrate** | host / viral — *what does the product act on?* |
| **Part 2 — consequence** | sustains host metabolism / discrete lifecycle step |
| **Evidence tier** | 1–6 (see protocol) |
| **Citations** | |
| **VERDICT** | COUNTS / DOES NOT COUNT / UNRESOLVABLE |
| **Confidence** | high / low |
| **If unresolvable — resolving experiment** | |

**Argument (half a page):**


---

## 18. `NAMPT`

- **K03462** — NAMPT; nicotinamide phosphoribosyltransferase [EC:2.4.2.12]

*Included because: >=1% and >=10 calls in soil*

| | |
|---|---|
| **Part 1 — substrate** | host / viral — *what does the product act on?* |
| **Part 2 — consequence** | sustains host metabolism / discrete lifecycle step |
| **Evidence tier** | 1–6 (see protocol) |
| **Citations** | |
| **VERDICT** | COUNTS / DOES NOT COUNT / UNRESOLVABLE |
| **Confidence** | high / low |
| **If unresolvable — resolving experiment** | |

**Argument (half a page):**


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

| | |
|---|---|
| **Part 1 — substrate** | host / viral — *what does the product act on?* |
| **Part 2 — consequence** | sustains host metabolism / discrete lifecycle step |
| **Evidence tier** | 1–6 (see protocol) |
| **Citations** | |
| **VERDICT** | COUNTS / DOES NOT COUNT / UNRESOLVABLE |
| **Confidence** | high / low |
| **If unresolvable — resolving experiment** | |

**Argument (half a page):**


---

## 21. `P4HA`

- **K00472** — P4HA; prolyl 4-hydroxylase [EC:1.14.11.2]

*Included because: >=1% and >=10 calls in ocean_conservative*

> [!note] PRE-FILLED by Claude — review and edit. This is the protocol's mechanical default,
> not a judgement: with no Tier 1–5 evidence the protocol forbids ruling the family out, so
> COUNTS applies automatically. **Your judgement here is whether you accept that the evidence
> is genuinely absent** — i.e. whether my searching held up.

> [!warning] PENDING — do the library check before accepting this
> A lead suggests prolyl 4-hydroxylase appears in megaphage virion proteomics (*npj Viruses* 2025), which I could not verify behind a login wall. **If it does, this becomes a structural verdict and leaves the evidence-free group.** ~15 minutes.

| | |
|---|---|
| **Part 1 — substrate** | UNDETERMINED — no evidence either way |
| **Part 2 — consequence** | UNDETERMINED — no evidence either way |
| **Evidence tier** | 6 (chemistry only; no Tier 1–5 available) |
| **Citations** | KEGG/EcoCyc for the reaction. No phage-specific study found. |
| **VERDICT** | **COUNTS** |
| **Confidence** | low |
| **Resolving experiment** | Check virion proteomics for the protein (see the megaphage lead in [[Evidence Dossiers]]); determine whether the hydroxylation target is a phage structural protein |

**Argument:**

No phage-specific functional evidence identified after three independent search strategies (thematic PubMed, per-gene PubMed, targeted preprint/web), and the gene is not discussed in any of the three source catalogue papers. Only Tier 6 evidence is available, which under the protocol cannot move a family out of the record. Defaults to COUNTS at low confidence. Flagged as **evidence-free** for separate reporting.

---

## 22. `phoH`

- **K06217** — phoH, phoL; phosphate starvation-inducible protein PhoH and related proteins

*Included because: >=1% and >=10 calls in ocean_conservative*

| | |
|---|---|
| **Part 1 — substrate** | host / viral — *what does the product act on?* |
| **Part 2 — consequence** | sustains host metabolism / discrete lifecycle step |
| **Evidence tier** | 1–6 (see protocol) |
| **Citations** | |
| **VERDICT** | COUNTS / DOES NOT COUNT / UNRESOLVABLE |
| **Confidence** | high / low |
| **If unresolvable — resolving experiment** | |

**Argument (half a page):**


---

## 23. `psbA`

- **K02703** — psbA; photosystem II P680 reaction center D1 protein [EC:1.10.3.9]

*Included because: control*

| | |
|---|---|
| **Part 1 — substrate** | host / viral — *what does the product act on?* |
| **Part 2 — consequence** | sustains host metabolism / discrete lifecycle step |
| **Evidence tier** | 1–6 (see protocol) |
| **Citations** | |
| **VERDICT** | COUNTS / DOES NOT COUNT / UNRESOLVABLE |
| **Confidence** | high / low |
| **If unresolvable — resolving experiment** | |

**Argument (half a page):**


---

## 24. `psbD`

- **K02706** — psbD; photosystem II P680 reaction center D2 protein [EC:1.10.3.9]

*Included because: control*

| | |
|---|---|
| **Part 1 — substrate** | host / viral — *what does the product act on?* |
| **Part 2 — consequence** | sustains host metabolism / discrete lifecycle step |
| **Evidence tier** | 1–6 (see protocol) |
| **Citations** | |
| **VERDICT** | COUNTS / DOES NOT COUNT / UNRESOLVABLE |
| **Confidence** | high / low |
| **If unresolvable — resolving experiment** | |

**Argument (half a page):**


---

## 25. `pseB`

- **K15894** — pseB, fnlA, wbjB; UDP-N-acetylglucosamine 4,6-dehydratase [EC:4.2.1.115]

*Included because: >=1% and >=10 calls in soil*

| | |
|---|---|
| **Part 1 — substrate** | host / viral — *what does the product act on?* |
| **Part 2 — consequence** | sustains host metabolism / discrete lifecycle step |
| **Evidence tier** | 1–6 (see protocol) |
| **Citations** | |
| **VERDICT** | COUNTS / DOES NOT COUNT / UNRESOLVABLE |
| **Confidence** | high / low |
| **If unresolvable — resolving experiment** | |

**Argument (half a page):**


---

## 26. `queuosine`

- **K01737** — queD, ptpS, PTS; 6-pyruvoyltetrahydropterin/6-carboxytetrahydropterin synthase [EC:4.2.3.12 4.1.2.50]
- **K06879** — queF; 7-cyano-7-deazaguanine reductase [EC:1.7.1.13]
- **K06920** — queC; 7-cyano-7-deazaguanine synthase [EC:6.3.4.20]
- **K09457** — queF; 7-cyano-7-deazaguanine reductase [EC:1.7.1.13]
- **K10026** — queE; 7-carboxy-7-deazaguanine synthase [EC:4.3.99.3]

*Included because: >=1% and >=10 calls in ocean_conservative, soil; named by Martin et al.*

| | |
|---|---|
| **Part 1 — substrate** | host / viral — *what does the product act on?* |
| **Part 2 — consequence** | sustains host metabolism / discrete lifecycle step |
| **Evidence tier** | 1–6 (see protocol) |
| **Citations** | |
| **VERDICT** | COUNTS / DOES NOT COUNT / UNRESOLVABLE |
| **Confidence** | high / low |
| **If unresolvable — resolving experiment** | |

**Argument (half a page):**


---

## 27. `raxST`

- **K13472** — raxST; sulfotransferase

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
| **Resolving experiment** | Identify the sulfation target |

**Argument:**

No phage-specific functional evidence identified after three independent search strategies (thematic PubMed, per-gene PubMed, targeted preprint/web), and the gene is not discussed in any of the three source catalogue papers. Only Tier 6 evidence is available, which under the protocol cannot move a family out of the record. Defaults to COUNTS at low confidence. Flagged as **evidence-free** for separate reporting.

---

## 28. `rfbB`

- **K01710** — rfbB, rmlB, rffG; dTDP-glucose 4,6-dehydratase [EC:4.2.1.46]

*Included because: >=1% and >=10 calls in soil*

| | |
|---|---|
| **Part 1 — substrate** | host / viral — *what does the product act on?* |
| **Part 2 — consequence** | sustains host metabolism / discrete lifecycle step |
| **Evidence tier** | 1–6 (see protocol) |
| **Citations** | |
| **VERDICT** | COUNTS / DOES NOT COUNT / UNRESOLVABLE |
| **Confidence** | high / low |
| **If unresolvable — resolving experiment** | |

**Argument (half a page):**


---

## 29. `rfbC`

- **K20444** — rfbC; O-antigen biosynthesis protein [EC:2.4.1.-]

*Included because: >=1% and >=10 calls in soil*

| | |
|---|---|
| **Part 1 — substrate** | host / viral — *what does the product act on?* |
| **Part 2 — consequence** | sustains host metabolism / discrete lifecycle step |
| **Evidence tier** | 1–6 (see protocol) |
| **Citations** | |
| **VERDICT** | COUNTS / DOES NOT COUNT / UNRESOLVABLE |
| **Confidence** | high / low |
| **If unresolvable — resolving experiment** | |

**Argument (half a page):**


---

## 30. `speD`

- **K01611** — speD, AMD1; S-adenosylmethionine decarboxylase [EC:4.1.1.50]

*Included because: >=1% and >=10 calls in ocean_conservative*

| | |
|---|---|
| **Part 1 — substrate** | host / viral — *what does the product act on?* |
| **Part 2 — consequence** | sustains host metabolism / discrete lifecycle step |
| **Evidence tier** | 1–6 (see protocol) |
| **Citations** | |
| **VERDICT** | COUNTS / DOES NOT COUNT / UNRESOLVABLE |
| **Confidence** | high / low |
| **If unresolvable — resolving experiment** | |

**Argument (half a page):**


---

## 31. `tagD`

- **K00980** — tagD; glycerol-3-phosphate cytidylyltransferase [EC:2.7.7.39]

*Included because: >=1% and >=10 calls in ocean_conservative*

| | |
|---|---|
| **Part 1 — substrate** | host / viral — *what does the product act on?* |
| **Part 2 — consequence** | sustains host metabolism / discrete lifecycle step |
| **Evidence tier** | 1–6 (see protocol) |
| **Citations** | |
| **VERDICT** | COUNTS / DOES NOT COUNT / UNRESOLVABLE |
| **Confidence** | high / low |
| **If unresolvable — resolving experiment** | |

**Argument (half a page):**


---

## 32. `TALDO1`

- **K00616** — TALDO1, talB, talA; transaldolase [EC:2.2.1.2]

*Included because: >=1% and >=10 calls in ocean_conservative*

| | |
|---|---|
| **Part 1 — substrate** | host / viral — *what does the product act on?* |
| **Part 2 — consequence** | sustains host metabolism / discrete lifecycle step |
| **Evidence tier** | 1–6 (see protocol) |
| **Citations** | |
| **VERDICT** | COUNTS / DOES NOT COUNT / UNRESOLVABLE |
| **Confidence** | high / low |
| **If unresolvable — resolving experiment** | |

**Argument (half a page):**


---

## 33. `UGDH`

- **K00012** — UGDH, ugd; UDPglucose 6-dehydrogenase [EC:1.1.1.22]

*Included because: >=1% and >=10 calls in ocean_conservative, soil*

| | |
|---|---|
| **Part 1 — substrate** | host / viral — *what does the product act on?* |
| **Part 2 — consequence** | sustains host metabolism / discrete lifecycle step |
| **Evidence tier** | 1–6 (see protocol) |
| **Citations** | |
| **VERDICT** | COUNTS / DOES NOT COUNT / UNRESOLVABLE |
| **Confidence** | high / low |
| **If unresolvable — resolving experiment** | |

**Argument (half a page):**


---

## 34. `xtmA`

- **K07474** — xtmA; phage terminase small subunit

*Included because: control*

| | |
|---|---|
| **Part 1 — substrate** | host / viral — *what does the product act on?* |
| **Part 2 — consequence** | sustains host metabolism / discrete lifecycle step |
| **Evidence tier** | 1–6 (see protocol) |
| **Citations** | |
| **VERDICT** | COUNTS / DOES NOT COUNT / UNRESOLVABLE |
| **Confidence** | high / low |
| **If unresolvable — resolving experiment** | |

**Argument (half a page):**


---

## 35. `xtmB`

- **K06909** — xtmB; phage terminase large subunit

*Included because: control*

| | |
|---|---|
| **Part 1 — substrate** | host / viral — *what does the product act on?* |
| **Part 2 — consequence** | sustains host metabolism / discrete lifecycle step |
| **Evidence tier** | 1–6 (see protocol) |
| **Citations** | |
| **VERDICT** | COUNTS / DOES NOT COUNT / UNRESOLVABLE |
| **Confidence** | high / low |
| **If unresolvable — resolving experiment** | |

**Argument (half a page):**


---
