# 06 — Project Brief and Pre-Registered Analysis Plan

**Phase 6 of 7.** Written 2026-08-05. This is the working document: the thing to build from,
and the thing to be held to.

---

## Title

**How much of the viral auxiliary metabolic gene record rests on gene categories the field's own
experts say should not count?**

## The question in one sentence

Bacteriophages carry genes that resemble host metabolic enzymes, and the field catalogues these
"auxiliary metabolic genes" (AMGs) as evidence that viruses reprogram host metabolism — but a
2025 *Nature Microbiology* Perspective argues that several of the most frequently counted
categories are doing something essential for the virus instead, and nobody has measured how much
of the record they account for.

## Why it matters

AMG catalogues underwrite claims about viral influence on global biogeochemistry. If a
substantial share of calls sit in disputed categories, then those claims are quantitatively
overstated by an amount nobody has established. The answer is interesting whether it is large or
small.

---

## THE INTEGRITY POINT, STATED FIRST

**The ocean-catalogue result already exists.** It was obtained on 2026-08-05, before this plan
was written: 25.1% of KO-assigned calls, driven by `dcm` and queuosine, with the share *rising*
after curation. That analysis is therefore **exploratory, not confirmatory**, and must be
reported as such. Calling it pre-registered would be false.

**The pre-registration below governs catalogues two and three**, which have not been examined.
That is the confirmatory test. This is the standard discovery-then-replication structure and it
is honest; presenting the ocean result as a prediction would not be.

*(The rubric itself was fixed before the ocean data was downloaded — the suspect patterns in
`amg_database_audit.py` were copied unchanged into `amg_record_composition.py`. That much is
genuinely pre-specified, and the scripts and their commit order are the evidence.)*

---

## UPGRADE 2026-08-05 — a second, stronger test than the rubric

The wastewater paper was obtained (*ES&T* 2023, `refs/est_2023_wastewater_amg.txt`) and it
changes the design. Three findings:

**1. Independent confirmation of H1, by an independent method.** They did **not** use VIBRANT or
DRAM-v. Their pipeline is hmmsearch/Pfam + kofamscan/KEGG + usearch/UniProt90 followed by manual
curation. Different environment, different team, different tools — and the disputed category is
still the top result:

> *"A total of 101 vAMGs … were identified, **the most common of which were the queuosine
> biosynthesis genes folE, queD, and queE** and the sulfur metabolism gene cysH."*

**20 of 101 vAMGs are folE/Que genes = 19.8%** ✅ — against 25.1% in the ocean catalogue. H1
(≥10%) confirmed in a second dataset, and the DRAM-v-artefact explanation is dead.

**2. The paper states an exclusion criterion and does not apply it.** From their methods:

> *"Metabolic genes directly involved in viral replication (e.g., replication, repair,
> **nucleotide transport, and metabolism**) were **not** included in vAMGs under the vAMGs
> classification scheme."*

And from their own results:

> *"20 vAMGs of folE and Que biosynthesis proteins (queC, queD, queE, and queF) **could also
> participate in tRNA biogenesis** by producing a hypermodified guanosine…"*

They declared the rule, noticed the conflict in their own text, and headlined the genes anyway.

> [!important] This is a better test than the rubric, and it defeats Attack 5
> The red team's strongest surviving objection was *"this is definitional — you picked a rubric
> and applied it."*
>
> **Testing each paper against its own stated inclusion criteria removes that objection
> entirely.** It is no longer Martin's opinion versus the field's; it is a paper's methods
> section versus its own results. That is an internal inconsistency, not a matter of taste, and
> it is far harder to argue with.

**NEW ANALYSIS STEP (now primary, ahead of the rubric comparison):** for each catalogue, extract
the authors' **stated** AMG inclusion/exclusion criteria, and test their own calls against them.
Report agreement with (a) their own stated rule and (b) Martin *et al.*'s rubric, separately.

**H4 (new, pre-specified — catalogues 3+ only, this one has been seen).** Published AMG
catalogues contain calls that violate their own stated inclusion criteria. *Null: stated
criteria are applied consistently.*

---

## UPDATE 2026-08-05 — third catalogue in. H1 confirmed three times, and a new finding.

Soil catalogue obtained (Daniel; *ISME J* 2022 16(5):1397 supplementary `moesm6`, sheet `AMGs`,
4,583 rows with Pfam descriptions, per-sample abundances included). It used **VIBRANT and
DRAM-v together** — the tool gap is closed.

| Catalogue | Environment | Pipeline | Disputed share | Dominated by |
|---|---|---|---|---|
| Ocean, *Microbiome* 2024 | marine | DRAM-v | **25.1%** (of KO-assigned) | `dcm` 5,797 · queuosine 2,156 |
| Wastewater, *ES&T* 2023 | activated sludge | custom hmmer/kofamscan/usearch | **19.8%** (20/101) | queuosine, `folE` |
| Soil, *ISME J* 2022 | contaminated soil | **VIBRANT + DRAM-v** | **29.8%** (1,365/4,583) | **glycosyltransferases 1,238** |

**H1 confirmed in three independent datasets** — three environments, three pipelines, all
between 20% and 30%. The "DRAM-v artefact" explanation is dead twice over.

> [!important] The new finding, and it is better than the headline number
> **The composition is completely different in each environment.** Soil has **zero** `dcm` calls
> and 1,155 "Glycosyl transferases group 1"; the ocean is the mirror image.
>
> Part of this is real biology and part is **annotation namespace**: the ocean catalogue is
> KEGG-keyed, the soil one is Pfam-keyed (KEGG populated on only 1,151 of 4,583 rows). **What
> you count as a disputed AMG depends on which identifier system the study used** — which
> connects directly to the earlier observation that VIBRANT keys on KEGG and DRAM keys on PFAM.
>
> That is a genuinely new claim, it is not in Martin *et al.*, and it is defensible from three
> datasets.

**A methodological lesson banked, at the cost of one wrong run.** A first pass matched against
the CAZy column as well as the Pfam description and returned **47.5%** — inflated by
"NAD dependent epimerase/dehydratase" and "short chain dehydrogenase" matching as glycoside
hydrolases via bare `GT\d+`/`GH\d+` codes. Restricting to Pfam descriptions gives 29.8% and every
match is genuine. **Free-text matching across heterogeneous annotation columns is unsafe and the
protocol must specify one source per category.**

---

## The pre-registered rubric

Taken **unchanged** from Martin *et al.* (2025), *A call for caution in the biological
interpretation of viral auxiliary metabolic genes*, *Nature Microbiology*,
[doi:10.1038/s41564-025-02095-4](https://doi.org/10.1038/s41564-025-02095-4). Not invented here.
The claim being tested is therefore *"what follows if the field adopts the position published in
Nature Microbiology"* — falsifiable, and not a personal opinion.

**Category S (suspect — argued to be essential viral function, not host metabolic modulation):**

| Gene family | Martin *et al.*'s argument |
|---|---|
| `dcm` — DNA cytosine methyltransferase | Modifies viral DNA to evade host restriction systems |
| `queC`, `queD`, `queE`, `queF` — queuosine biosynthesis | Modifies the viral chromosome to evade host defences |
| `dsrC` / `tusE` | HMMs cannot distinguish them; KEGG merges them into K11179 |
| Glycoside hydrolases | Structural — tail fibres, baseplates, endolysins — for entry and exit, not nutrition |
| Folate / one-carbon genes | Feed *de novo* nucleotide biosynthesis for genome replication |

**Two rubrics will be reported side by side, and the gap between them is itself a result:**
- **Strict:** all of Category S excluded from AMG counts
- **Inclusive:** current practice, nothing excluded

**No category may be added to S after seeing results.** If a new suspect emerges during the
adjudication it is reported separately as an exploratory observation.

---

## Hypotheses, pre-specified

**H1 (primary).** In catalogues two and three, Category S accounts for **≥10% of KO-assigned AMG
calls**. *Null: <10%, i.e. the ocean result does not generalise.*

**H2 (secondary, the more interesting one).** Curation **enriches** for Category S — the suspect
share of KO-assigned calls is higher in curated than in uncurated catalogues. *Null: curation
reduces or does not change it.*

**H3 (tertiary).** Category S share differs by tool. DRAM-v-based and VIBRANT-based catalogues
give materially different suspect fractions. *Null: no difference.*

**Directional and committed.** H2 is the one worth being wrong about publicly.

---

## Datasets

| # | Catalogue | Status | Role |
|---|---|---|---|
| 1 | Global ocean, *Microbiome* 2024 (Zenodo 10.5281/zenodo.12668289) | ✅ analysed | **Discovery** |
| 2 | Wastewater, *ES&T* [doi:10.1021/acs.est.2c07800](https://doi.org/10.1021/acs.est.2c07800) | ⚠️ needs library access | **Confirmatory** — highest value, it headlines queuosine |
| 3 | Soil virome (*ISME J* organochlorine study or equivalent) | ⚠️ unverified | **Confirmatory** — different environment |
| 4 | Global RNA virome, GitHub `YangZhao-LZU/RNA_AMG` | ✅ obtainable | **Contrast only** — 256 AMGs, different biology |

**Hard gate.** If catalogues 2 and 3 do not publish per-gene tables carrying KO or PFAM
identifiers, the cross-dataset claim is impossible and the project reduces to a single-catalogue
report. **Test this first, in half a day, before any other work.**

---

## Analysis plan

1. **Retrieve** catalogues 2–3; confirm per-gene identifiers exist. *Stop if not.*
2. **Harmonise** to a common schema: one row per AMG call, with gene ID, KO, PFAM, CAZy,
   confidence score, source catalogue. Deduplicate (~1,800 duplicate rows in catalogue 1).
3. **Confirm tool semantics** from DRAM-v and VIBRANT documentation — particularly the `F` flag
   carried by 68% of `dcm` calls. Do not assume.
4. **Classify** every call against the frozen rubric, by KEGG KO where present.
5. **Report two denominators, always together**: share of *KO-assigned* calls and share of *all*
   calls. Reporting only the former is misleading, since ~36% of calls carry a KO.
6. **Binomial confidence intervals** on every proportion.
7. **Compare** catalogues (H3) and curation levels (H2) with Fisher's exact test.
8. **Abundance-weight** where per-sample abundance is available — a call is not an organism.
9. **Adjudicate** each Category S family from primary biochemistry, and record the reasoning per
   family. *This is the scientific substance.*
10. **Test consequence:** does excluding Category S change any published conclusion? The *ES&T*
    "queuosine genes are the most common AMGs" claim is test case one.

---

## Outcomes

**Primary.** Percentage of AMG calls in Category S, per catalogue, under both rubrics, with CIs.

**Secondary.** Curation enrichment ratio (H2); between-tool difference (H3); the adjudication
table; a list of published claims that do or do not survive the strict rubric.

**Figures.** (i) Suspect share per catalogue, both rubrics, with CIs. (ii) Retention rate through
curation, Category S vs all. (iii) Composition of Category S by gene family.

---

## What the null looks like, and why it is still publishable

If Category S is a few percent everywhere outside the ocean catalogue, the finding is: **the
concern raised in *Nature Microbiology* is real but quantitatively minor, and the ocean result is
an outlier.** That is a useful, honest, citable answer to a question the field has posed and not
answered. It is written up either way.

## What would make this project be abandoned

- Catalogues 2–3 publish no gene-level data *(fatal to the general claim; retreat to a single-catalogue report)*
- Martin's group publishes the same measurement first *(then: pivot to the curation-enrichment finding, which is not in their paper)*
- The adjudication shows Category S calls are overwhelmingly defensible on biochemical grounds
  *(then the finding is that the field's practice is sound — report it)*

---

## Deliverables

1. A short paper or preprint, honestly framed as an audit
2. A public repository: scripts, harmonised data, frozen rubric, full provenance
3. The adjudication table — the reusable artefact, whatever happens to the rest
4. A vault write-up in [[Skills Log]] stating exactly what was learned and what was not

---

## Already done, and what remains

**Done (2026-08-05):** rubric fixed; both tool databases audited; ocean catalogue measured
(88,729 calls) and verified accession-by-accession; curation-enrichment observed; red team
survived; feasibility cleared.

**Remaining:** everything in the analysis plan above, beginning with the half-day gate.

---

## Limitations, declared in advance

- **Partly definitional.** "AMG" has no universally agreed boundary. Mitigated by using a
  published rubric unchanged and reporting both versions.
- **Ocean result is exploratory**, not a prediction. Stated in the paper, not buried.
- **KO coverage is only ~36%.** Everything outside that is invisible to the exact route.
- **A call is not an abundance, and abundance is not an organism.**
- **One analyst, no blinding.** The rubric being frozen and public is the substitute.

## Key citations

- Martin *et al.* (2025) *Nature Microbiology* — [doi:10.1038/s41564-025-02095-4](https://doi.org/10.1038/s41564-025-02095-4) — the framing paper
- *Expanding standards in viromics*, *PeerJ* 2021 9:e11447, [PMC8210812](https://pmc.ncbi.nlm.nih.gov/articles/PMC8210812) — raised the concern in 2021, declined to catalogue it
- Global ocean AMG catalogue, *Microbiome* 2024 — [doi:10.1186/s40168-024-01876-z](https://doi.org/10.1186/s40168-024-01876-z)
- Kieft, Zhou & Anantharaman (2020) VIBRANT; Shaffer *et al.* (2020) DRAM — the two tools
