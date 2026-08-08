---
tags: [project, research, adjudication, parallel-rater]
---

# Parallel Adjudication — Rater C

**A second, independent set of verdicts for all 35 families**, produced without reference to any
verdict recorded elsewhere and without opening `adjudication_counts_SEALED.tsv`.

**This is not the record.** [[Adjudication Worksheet]] is the record. This file exists to be
compared against it — two raters, concordance reported, disagreements examined. See
[the note at the end](#what-this-is-and-what-it-is-not) before using any of it.

Rules applied exactly as written in [[Adjudication Protocol]]:

- **Counts as an AMG only if BOTH** the substrate is host **and** the consequence is sustaining or
  redirecting host metabolism, rather than a discrete lifecycle step
- **Default is COUNTS.** Positive Tier 1–5 evidence is required to move a family out
- **Tier 6 alone can never rule a family out**
- **UNRESOLVABLE** requires the evidence to genuinely conflict *and* a nameable resolving
  experiment — not merely an absence of evidence

---

## 1. `asnB` — asparagine synthase (glutamine-hydrolysing) · K01953

| | |
|---|---|
| **Part 1 — substrate** | Undetermined — no evidence either way |
| **Part 2 — consequence** | Undetermined |
| **Evidence tier** | 6 |
| **Citations** | KEGG K01953. No phage-specific study found. |
| **VERDICT** | **COUNTS** |
| **Confidence** | low |
| **Resolving experiment** | Express the phage-encoded enzyme; confirm activity; test whether asparagine limitation alters burst size |

**Argument.** Asparagine synthase is ordinary amino-acid anabolism with no obvious viral
application. No study has examined a phage-encoded copy. Only Tier 6 reasoning is available,
which under the protocol cannot move a family out. Defaults to COUNTS at low confidence.

---

## 2. `cgeB` — spore maturation protein · K06320

| | |
|---|---|
| **Part 1 — substrate** | Undetermined |
| **Part 2 — consequence** | Undetermined |
| **Evidence tier** | 6 |
| **Citations** | KEGG K06320. No phage-specific study found. |
| **VERDICT** | **COUNTS** |
| **Confidence** | low |
| **Resolving experiment** | Determine whether the protein localises to the virion or the host cell surface |

**Argument.** A sporulation-associated, glycosyltransferase-like protein contributing to the
outer spore layer. Nothing links the phage-encoded copy to either host metabolism or a viral
lifecycle step. Defaults to COUNTS. Worth noting separately that "auxiliary **metabolic** gene"
is a strained label for a spore-coat protein, but that observation is not a verdict.

---

## 3. `dcm` — DNA cytosine methyltransferase · K00558, K17398

| | |
|---|---|
| **Part 1 — substrate** | **Viral** — the phage's own cytosines |
| **Part 2 — consequence** | **Genome protection** — a discrete lifecycle step |
| **Evidence tier** | 2 |
| **Citations** | Burke *et al.* 2021 *PNAS* [DOI](https://doi.org/10.1073/pnas.2026742118) |
| **VERDICT** | **DOES NOT COUNT** |
| **Confidence** | high |
| **Resolving experiment** | — |

**Argument.** The only direct work on phage-encoded C5-methyltransferases places them inside
modification clusters whose described function is *"DNA packaging and evasion of host
restriction"*, acting on the phage's own cytosines. Anti-restriction is the standard reason a
phage carries a methyltransferase: methylate your genome in the host's pattern and the host's
endonucleases spare it. Both parts of the rule point viral. No study shows a phage `dcm`
methylating host DNA. Tier 2 is sufficient to move a family out.

*Not blind — this family's expected verdict appears in the protocol's worked-example table.*

---

## 4. `dsrC_tusE` — sulfur relay · K11179

| | |
|---|---|
| **Part 1 — substrate** | **Cannot be determined from the accession** |
| **Part 2 — consequence** | Host energy metabolism *or* tRNA thiolation, depending which gene it is |
| **Evidence tier** | 3–4 (ecology); effectively 0 for gene identity |
| **Citations** | Stockdreher *et al.* 2012 *PLoS One* [DOI](https://doi.org/10.1371/journal.pone.0040785) · Kieft *et al.* 2021 *Nat Commun* [DOI](https://doi.org/10.1038/s41467-021-23698-5) |
| **VERDICT** | **UNRESOLVABLE** |
| **Confidence** | high (in the unresolvability) |
| **Resolving experiment** | Phylogenetic or HMM separation of DsrC from TusE, then re-annotation of the environmental calls |

**Argument.** This family is unlike any other in the list: the question is not what a phage does
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

## 5. `dut` — dUTP diphosphatase · K01520

| | |
|---|---|
| **Part 1 — substrate** | Shared nucleotide pool — not separable |
| **Part 2 — consequence** | Arguably replication; not demonstrated |
| **Evidence tier** | 4 |
| **Citations** | Huang *et al.* 2021 *Environ Microbiol* [DOI](https://doi.org/10.1111/1462-2920.15412) · Nyíri *et al.* 2019 [DOI](https://doi.org/10.3390/biom9090488) |
| **VERDICT** | **COUNTS** |
| **Confidence** | low |
| **Resolving experiment** | Isotopically track dUMP produced by phage dUTPase into phage versus host DNA during infection |

**Argument.** The intuition here is strong — a phage dUTPase is *obviously* about phage DNA — but
intuition is Tier 6, and the protocol explicitly forbids Tier 6 alone from moving a family out.
The available Tier 2 work on phage dUTPases concerns their **non-enzymatic** binding to the Stl
repressor, a different function entirely; the Tier 4 evidence places dUTPase in nucleotide-pathway
AMG sets, which describes the pathway rather than showing who benefits. dUTPase also protects the
pool it draws on, and during infection host and phage draw on the same pool.

No positive Tier 1–5 evidence that the dUTPase function is viral-directed. **Defaults to COUNTS,
and I record my discomfort with that**: this is the protocol being deliberately hard to satisfy,
working as designed.

---

## 6. `folate` — folate / one-carbon pathway · 10 accessions incl. `folE`, `folE2`

| | |
|---|---|
| **Part 1 — substrate** | GTP → shared; product routes to host cofactor **or** phage DNA |
| **Part 2 — consequence** | Genuinely both |
| **Evidence tier** | 2 |
| **Citations** | Thiaville *et al.* 2016 *PNAS* [DOI](https://doi.org/10.1073/pnas.1518570113) |
| **VERDICT** | **UNRESOLVABLE** |
| **Confidence** | high (in the unresolvability) |
| **Resolving experiment** | Metabolic flux from `folE` in infected cells: does the pterin output go to tetrahydrofolate or to 7-deazaguanine? |

**Argument.** `folE`/GTP cyclohydrolase I is the first committed step of folate biosynthesis
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

## 7. `galE` — UDP-glucose 4-epimerase · K01784

| | |
|---|---|
| **Part 1 — substrate** | Host nucleotide-sugar pool |
| **Part 2 — consequence** | Not determined — feeds many pathways |
| **Evidence tier** | 6 |
| **Citations** | KEGG K01784. Block literature (Appendix A of [[Evidence Dossiers]]) concerns the transfer step, not precursor supply. |
| **VERDICT** | **COUNTS** |
| **Confidence** | low |
| **Resolving experiment** | Determine the destination of UDP-galactose produced by the phage enzyme — surface glycan or elsewhere |

**Argument.** A precursor enzyme whose product feeds surface glycans among other destinations.
The demonstrated phage biology in this block concerns glycosyltransferases **transferring** sugars
onto the host surface; `galE` merely supplies building blocks. Extending that reasoning to the
precursor is an assumption, not a finding. No phage-specific evidence. Defaults to COUNTS.

---

## 8. `glmS` — glutamine–fructose-6-phosphate transaminase · K00820

| | |
|---|---|
| **Part 1 — substrate** | Host central metabolism |
| **Part 2 — consequence** | Not determined |
| **Evidence tier** | 6 |
| **Citations** | KEGG K00820. No phage-specific study found. |
| **VERDICT** | **COUNTS** |
| **Confidence** | low |
| **Resolving experiment** | As §7, for glucosamine-6-phosphate |

**Argument.** The committed entry to amino-sugar biosynthesis, sitting further upstream than
almost anything else in this block — its product feeds peptidoglycan, LPS and teichoic acids,
i.e. most of the cell envelope. The further upstream an enzyme sits, the weaker any claim that it
serves one specific downstream purpose. Defaults to COUNTS.

---

## 9. `glycoside_hydrolase` · 6 accessions

| | |
|---|---|
| **Part 1 — substrate** | **Host** — cell wall peptidoglycan |
| **Part 2 — consequence** | **Entry / egress** — discrete lifecycle steps |
| **Evidence tier** | 1–2 |
| **Citations** | Yuan & Gao 2016 *Front Microbiol* [DOI](https://doi.org/10.3389/fmicb.2016.00745) |
| **VERDICT** | **DOES NOT COUNT** |
| **Confidence** | high |
| **Resolving experiment** | — |

**Argument.** This is the family the two-part rule was designed for. The substrate is a host
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

## 10. `glycosyltransferase` · 5 accessions

| | |
|---|---|
| **Part 1 — substrate** | **Host** — O-antigen, LPS, teichoic acid |
| **Part 2 — consequence** | **Rule underdetermines** — see argument |
| **Evidence tier** | 2 |
| **Citations** | Mann *et al.* 2015 *JBC* [DOI](https://doi.org/10.1074/jbc.M115.660803) · Sun *et al.* 2013 [DOI](https://doi.org/10.1186/1471-2180-13-39) · Sumrall *et al.* 2021 [DOI](https://doi.org/10.1128/JB.00136-21) |
| **VERDICT** | **COUNTS** |
| **Confidence** | low |
| **Resolving experiment** | Determine whether phage-mediated serotype conversion alters host metabolic flux beyond the glycan itself |

**Argument, and this one needs stating carefully.** Phage-encoded glycosyltransferases
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

## 11. `gmd` — GDP-mannose 4,6-dehydratase · K01711

| | |
|---|---|
| **Part 1 — substrate** | Host nucleotide-sugar pool |
| **Part 2 — consequence** | Not determined |
| **Evidence tier** | 6 |
| **Citations** | KEGG K01711. Block literature concerns the transfer step. |
| **VERDICT** | **COUNTS** |
| **Confidence** | low |
| **Resolving experiment** | As §7, for GDP-fucose |

**Argument.** A precursor enzyme, though more surface-committed than `galE` since fucose is
largely a surface sugar. That tilt is worth noting but is not evidence. Defaults to COUNTS.

---

## 12. `hisF` — imidazole glycerol-phosphate synthase · K02500

| | |
|---|---|
| **Part 1 — substrate** | Undetermined |
| **Part 2 — consequence** | Undetermined |
| **Evidence tier** | 6 |
| **Citations** | KEGG K02500. No phage-specific study found. |
| **VERDICT** | **COUNTS** |
| **Confidence** | low |
| **Resolving experiment** | Complementation of a histidine auxotroph by the phage copy; histidine flux in infected cells |

**Argument.** Histidine biosynthesis, with a side-connection to purine metabolism via released
AICAR. Nothing phage-specific. Defaults to COUNTS.

---

## 13. `HMGCL` — hydroxymethylglutaryl-CoA lyase · K01640

| | |
|---|---|
| **Part 1 — substrate** | Undetermined |
| **Part 2 — consequence** | Undetermined |
| **Evidence tier** | 6 |
| **Citations** | KEGG K01640. No phage-specific study found. |
| **VERDICT** | **COUNTS** |
| **Confidence** | low |
| **Resolving experiment** | Determine the substrate of the phage enzyme; test whether infection alters host leucine/ketone catabolism |

**Argument.** Leucine catabolism and ketone body formation. No phage connection in the
literature. Defaults to COUNTS.

---

## 14. `IMPDH` — IMP dehydrogenase · K00088

| | |
|---|---|
| **Part 1 — substrate** | Shared nucleotide pool |
| **Part 2 — consequence** | Arguably replication; not demonstrated |
| **Evidence tier** | 6 |
| **Citations** | KEGG K00088. No functional study of a phage-encoded IMPDH found. |
| **VERDICT** | **COUNTS** |
| **Confidence** | low |
| **Resolving experiment** | As §5 — track guanine nucleotides produced by the phage enzyme into phage versus host DNA |

**Argument.** The rate-limiting step of guanine nucleotide biosynthesis, and structurally the
same problem as `dut` and `nrdH`: during infection host and phage draw on one pool. The
mechanistic case that this serves phage replication is Tier 6, which cannot rule a family out.
Defaults to COUNTS.

Worth recording that KEGG places IMPDH in **09104 Nucleotide metabolism** — the category the
wastewater paper's own methods exclude, which is a Chunk 4 point rather than a verdict.

---

## 15. `iscU` — Fe-S cluster scaffold · K04488

| | |
|---|---|
| **Part 1 — substrate** | Undetermined |
| **Part 2 — consequence** | Undetermined |
| **Evidence tier** | 6 |
| **Citations** | KEGG K04488. No phage-specific study found. |
| **VERDICT** | **COUNTS** |
| **Confidence** | low |
| **Resolving experiment** | Test Fe-S assembly by the phage protein and identify which apo-proteins it loads — host or phage |

**Argument.** Scaffold for iron–sulfur cluster assembly, delivering cofactors to a large number
of enzymes. Nothing phage-specific. The one apparent hit in the literature uses **phage display
as a method** and is not about phage biology. Defaults to COUNTS.

---

## 16. `K07336` — PKHD-type hydroxylase · K07336

| | |
|---|---|
| **Part 1 — substrate** | **Unknown — the enzyme itself is uncharacterised** |
| **Part 2 — consequence** | Unknown |
| **Evidence tier** | 6, and arguably less |
| **Citations** | KEGG K07336. No gene symbol assigned. No phage-specific study found. |
| **VERDICT** | **COUNTS** |
| **Confidence** | low |
| **Resolving experiment** | **Determine the substrate at all** |

**Argument.** An uncharacterised 2OG-Fe(II) oxygenase to which KEGG assigns no gene symbol. The
gap here is more basic than elsewhere: it is not that nobody has studied the phage copy, it is
that nobody has characterised the enzyme. Defaults to COUNTS, and I would flag this family in the
write-up as the clearest single instance of a call resting on nothing but sequence similarity.

---

## 17. `manB` — phosphomannomutase · K01840

| | |
|---|---|
| **Part 1 — substrate** | Host central metabolism |
| **Part 2 — consequence** | Not determined |
| **Evidence tier** | 6 |
| **Citations** | KEGG K01840. Block literature concerns the transfer step. |
| **VERDICT** | **COUNTS** |
| **Confidence** | low |
| **Resolving experiment** | As §7, for GDP-mannose |

**Argument.** Precursor enzyme feeding GDP-mannose, which has surface and non-surface
destinations. Same reasoning as §7. Defaults to COUNTS.

---

## 18. `NAMPT` — nicotinamide phosphoribosyltransferase · K03462

| | |
|---|---|
| **Part 1 — substrate** | Shared cofactor pool (NAD⁺) |
| **Part 2 — consequence** | Authors propose phage-directed use; not demonstrated as such |
| **Evidence tier** | 1–2 |
| **Citations** | Lee, Li & Miller 2017 *J Bacteriol* [DOI](https://doi.org/10.1128/JB.00855-16) |
| **VERDICT** | **COUNTS** |
| **Confidence** | low |
| **Resolving experiment** | Determine whether NAD⁺ produced by the phage pathway is preferentially consumed by phage-directed ADP-ribosylation versus general host metabolism |

**Argument.** This is the hardest COUNTS in the set, and the reasoning matters.

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

## 19. `nodU` — carbamoyltransferase · K00612

| | |
|---|---|
| **Part 1 — substrate** | Undetermined |
| **Part 2 — consequence** | Undetermined |
| **Evidence tier** | 6 |
| **Citations** | KEGG K00612. No phage-specific study found. |
| **VERDICT** | **COUNTS** |
| **Confidence** | low |
| **Resolving experiment** | Identify the carbamoylation target — host surface polysaccharide, or a phage structural protein |

**Argument.** In rhizobia `nodU` carbamoylates a secreted signalling glycan; outside that context
the target is generally unknown. Both a host-surface and a phage-structural target are plausible,
but neither is evidenced. Defaults to COUNTS.

---

## 20. `nrdH` — glutaredoxin-like protein NrdH · K06191

| | |
|---|---|
| **Part 1 — substrate** | Shared — ribonucleotide pool |
| **Part 2 — consequence** | Not separable during infection |
| **Evidence tier** | 4–5 |
| **Citations** | Sakowski *et al.* 2021 *Nat Microbiol* [DOI](https://doi.org/10.1038/s41564-021-00873-4) · Huang *et al.* 2021 [DOI](https://doi.org/10.1111/1462-2920.15412) |
| **VERDICT** | **COUNTS** |
| **Confidence** | low |
| **Resolving experiment** | Separate the phage and host dNTP pools during infection — which may not be experimentally possible, and if so this family becomes genuinely undecidable |

**Argument.** Redox partner of class Ib ribonucleotide reductase. The Tier 5 signal is real and
interesting: phage RNRs are phylogenetically distinct enough from host copies to serve as a
**viral marker gene**, which argues against incidental acquisition and for specialisation. But
specialisation *for what* is not shown.

The deeper problem is that during lytic infection there is only one dNTP pool, so "does this
serve the host or the phage" may not be a well-formed question experimentally. I have not marked
this UNRESOLVABLE, because the evidence does not conflict — it simply does not reach. Under the
protocol that is unresearched, not unresolvable. Defaults to COUNTS.

---

## 21. `P4HA` — prolyl 4-hydroxylase · K00472

| | |
|---|---|
| **Part 1 — substrate** | Undetermined |
| **Part 2 — consequence** | Undetermined |
| **Evidence tier** | 6 (pending verification of one lead) |
| **Citations** | KEGG K00472. No **verified** phage-specific study. |
| **VERDICT** | **COUNTS** |
| **Confidence** | low |
| **Resolving experiment** | Check megaphage virion proteomics for the protein; determine whether the hydroxylation target is a phage structural protein |

**Argument.** 2OG-dependent proline hydroxylation, a structural modification. An unverified lead
suggests prolyl-4-hydroxylase appears in megaphage virion proteomics; I could not confirm it, and
a related paper on "viral prolyl-4-hydroxylase" concerns a eukaryotic algal virus rather than a
phage. **On verified evidence this is Tier 6 and defaults to COUNTS** — but if the virion
proteomics confirms, this becomes a structural verdict on §9's logic and the verdict should be
revisited.

---

## 22. `phoH` — phosphate starvation-inducible protein · K06217

| | |
|---|---|
| **Part 1 — substrate** | **Host** — phosphate acquisition machinery |
| **Part 2 — consequence** | **Sustains host phosphate scavenging** under limitation |
| **Evidence tier** | 4–5 |
| **Citations** | Goldsmith *et al.* 2011 *AEM* [DOI](https://doi.org/10.1128/AEM.05531-11) · Huang *et al.* 2021 [DOI](https://doi.org/10.1111/1462-2920.15412) |
| **VERDICT** | **COUNTS** |
| **Confidence** | moderate |
| **Resolving experiment** | Delete or express phage `phoH` and measure phosphate uptake in infected versus uninfected cells under limitation |

**Argument.** Unlike most COUNTS verdicts here, this one is **supported** rather than merely
defaulted. Pho regulon genes appear in ~40% of marine phage genomes against 4% of non-marine ones
— phages carry this **where phosphate is limiting**. That ecological correlation is difficult to
explain except by phosphate acquisition mattering in the infected cell, and phosphate acquisition
is host machinery doing host work.

The counter-argument — that phage replication is itself phosphate-expensive — is real but does not
displace the substrate, which remains the host's uptake system. The phylogenetic distinctness of
phage `phoH` is a caution against assuming the host function is preserved intact, hence moderate
rather than high confidence.

---

## 23. `psbA` — photosystem II D1 · K02703

| | |
|---|---|
| **Part 1 — substrate** | **Host** — the host's thylakoid membrane |
| **Part 2 — consequence** | **Sustains host photosynthesis**, measured |
| **Evidence tier** | 1–2 |
| **Citations** | Sullivan *et al.* 2006 *PLoS Biol* [DOI](https://doi.org/10.1371/journal.pbio.0040234) · Sieradzki *et al.* 2019 *Nat Commun* [DOI](https://doi.org/10.1038/s41467-019-09106-z) · Lindell *et al.* 2007 *Nature* [DOI](https://doi.org/10.1038/nature06130) |
| **VERDICT** | **COUNTS** |
| **Confidence** | high |
| **Resolving experiment** | — |

**Argument.** The phage protein is inserted into the **host's** photosystem, replacing a host
subunit that photodamage continually destroys, and the measured consequence is that host
photosynthesis keeps running during infection — with more than half of all `psbA` expression
viral in some samples. Both parts point host.

The objection that the phage does this only to finish replicating is true and **generalises to
everything a phage does**, which is precisely why Part 2 asks about discrete lifecycle steps
rather than ultimate benefit. Maintaining a functioning host photosystem is not one of entry,
genome protection, replication, assembly or egress.

*Not blind — expected verdict appears in the protocol's worked-example table.*

---

## 24. `psbD` — photosystem II D2 · K02706

| | |
|---|---|
| **Part 1 — substrate** | **Host** thylakoid |
| **Part 2 — consequence** | **Sustains host photosynthesis** |
| **Evidence tier** | 2 |
| **Citations** | Sullivan *et al.* 2006 [DOI](https://doi.org/10.1371/journal.pbio.0040234) |
| **VERDICT** | **COUNTS** |
| **Confidence** | high |
| **Resolving experiment** | — |

**Argument.** Same reasoning as §23, and judged separately rather than inherited. The
distinguishing fact is that `psbD` occurs in about half as many phages as `psbA` and its presence
correlates with **broad host range**, which Sullivan *et al.* attribute to constraints on coupling
viral and host PsbA–PsbD across divergent hosts. That is compatibility engineering in service of
the same host-directed function, not a different function — so the verdict follows `psbA`, with
slightly lower evidentiary depth.

---

## 25. `pseB` — UDP-GlcNAc 4,6-dehydratase · K15894

| | |
|---|---|
| **Part 1 — substrate** | Host nucleotide-sugar pool |
| **Part 2 — consequence** | Not determined |
| **Evidence tier** | 6 |
| **Citations** | KEGG K15894. No phage-specific study found. |
| **VERDICT** | **COUNTS** |
| **Confidence** | low |
| **Resolving experiment** | As §7, for pseudaminic acid |

**Argument.** First step to pseudaminic acid, a surface-committed sugar with few destinations
outside surface glycans and flagellar glycosylation. That commitment weakens the "feeds many
pathways" defence relative to `galE` — but a strong prior about destination is still not evidence
about consequence. Defaults to COUNTS.

---

## 26. `queuosine` — `queC`, `queD`, `queE`, `queF` · 5 accessions

| | |
|---|---|
| **Part 1 — substrate** | **Both demonstrated** — tRNA (host) and phage DNA (viral) |
| **Part 2 — consequence** | Translation fidelity *or* genome protection |
| **Evidence tier** | 2 |
| **Citations** | Thiaville *et al.* 2016 *PNAS* [DOI](https://doi.org/10.1073/pnas.1518570113) · Hutinet *et al.* 2016 *RNA Biol* [DOI](https://doi.org/10.1080/15476286.2016.1265200) · de Crécy-Lagard *et al.* 2024 *MMBR* [DOI](https://doi.org/10.1128/mmbr.00199-23) |
| **VERDICT** | **UNRESOLVABLE** |
| **Confidence** | high (in the unresolvability) |
| **Resolving experiment** | Systematic detection of 7-deazaguanine derivatives in the DNA of phages carrying these genes versus those lacking them. Done for a single phage; never done systematically |

**Argument.** This is the case UNRESOLVABLE exists for. The pathway demonstrably does **both
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

## 27. `raxST` — sulfotransferase · K13472

| | |
|---|---|
| **Part 1 — substrate** | Undetermined |
| **Part 2 — consequence** | Undetermined |
| **Evidence tier** | 6 |
| **Citations** | KEGG K13472. No phage-specific study found. |
| **VERDICT** | **COUNTS** |
| **Confidence** | low |
| **Resolving experiment** | Identify the sulfation target |

**Argument.** In *Xanthomonas*, RaxST sulfates a secreted peptide involved in plant immune
recognition; elsewhere the target is generally unknown. Apparent literature hits are false
positives — a mouse liver study mentioning Cre-lox from phage P1, and a cancer study using phage
microarrays. Defaults to COUNTS.

---

## 28. `rfbB` — dTDP-glucose 4,6-dehydratase · K01710

| | |
|---|---|
| **Part 1 — substrate** | Host nucleotide-sugar pool |
| **Part 2 — consequence** | Not determined |
| **Evidence tier** | 6 |
| **Citations** | KEGG K01710. Block literature concerns the transfer step. |
| **VERDICT** | **COUNTS** |
| **Confidence** | low |
| **Resolving experiment** | As §7, for dTDP-rhamnose |

**Argument.** Second step of the dTDP-L-rhamnose pathway; rhamnose is a major O-antigen sugar, so
this is surface-committed like `pseB`. Same reasoning: strong prior about destination, no evidence
about consequence. Defaults to COUNTS.

---

## 29. `rfbC` — O-antigen biosynthesis protein · K20444

| | |
|---|---|
| **Part 1 — substrate** | **Host** — O-antigen |
| **Part 2 — consequence** | **Rule underdetermines**, as §10 |
| **Evidence tier** | 2 (via the block literature, which is about this exact process) |
| **Citations** | Mann *et al.* 2015 [DOI](https://doi.org/10.1074/jbc.M115.660803) · Sun *et al.* 2013 [DOI](https://doi.org/10.1186/1471-2180-13-39) |
| **VERDICT** | **COUNTS** |
| **Confidence** | low |
| **Resolving experiment** | As §10 |

**Argument.** KEGG names this **O-antigen biosynthesis** directly, and its EC number (2.4.1.-)
makes it a glycosyltransferase — so the Mann and Sun evidence about phage-mediated O-antigen
modification applies here more squarely than to any precursor enzyme.

That means the verdict must match §10, and for the same reason: Part 1 is host, but serotype
conversion is neither host metabolic modulation nor an enumerated lifecycle step, so the rule
underdetermines and the conservative default applies. **If §10 and §29 ever receive different
verdicts, that inconsistency needs explaining** — I have kept them aligned deliberately.

---

## 30. `speD` — S-adenosylmethionine decarboxylase · K01611

| | |
|---|---|
| **Part 1 — substrate** | Host SAM pool |
| **Part 2 — consequence** | Not determined; virion packaging is plausible but not shown for these phages |
| **Evidence tier** | 5–6 |
| **Citations** | KEGG K01611. Phage–polyamine literature exists but is old and organism-specific. |
| **VERDICT** | **COUNTS** |
| **Confidence** | low |
| **Resolving experiment** | Determine whether spermidine produced during infection is packaged into virions or remains in the host cytoplasm |

**Argument.** Supplies the aminopropyl donor for spermidine. Spermidine is a structural component
of some phage virions, where its charge helps neutralise the packaged genome — which, if it
applied here, would make this assembly and parallel the terminase argument. But that literature is
decades old and organism-specific, and nothing connects it to the phages in these catalogues.
Defaults to COUNTS.

---

## 31. `tagD` — glycerol-3-phosphate cytidylyltransferase · K00980

| | |
|---|---|
| **Part 1 — substrate** | Host — teichoic acid backbone |
| **Part 2 — consequence** | Not determined |
| **Evidence tier** | 6 |
| **Citations** | KEGG K00980. Sumrall *et al.* 2021 concerns WTA **decoration**, not backbone synthesis. [DOI](https://doi.org/10.1128/JB.00136-21) |
| **VERDICT** | **COUNTS** |
| **Confidence** | low |
| **Resolving experiment** | As §7, for CDP-glycerol |

**Argument.** Makes CDP-glycerol, the wall teichoic acid backbone donor. WTA **glycosylation** is
demonstrably the phage receptor in Gram-positives, but `tagD` builds the polymer, not the sugar
decoration that the receptor work concerns. The distinction matters and I have not elided it.
Defaults to COUNTS.

---

## 32. `TALDO1` — transaldolase · K00616

| | |
|---|---|
| **Part 1 — substrate** | **Host** — pentose phosphate pathway intermediates |
| **Part 2 — consequence** | **Host carbon flux measurably redirected** — NADPH/NADP doubles |
| **Evidence tier** | 1–2 |
| **Citations** | Thompson *et al.* 2011 *PNAS* [DOI](https://doi.org/10.1073/pnas.1102164108) · Lindell *et al.* 2007 *Nature* [DOI](https://doi.org/10.1038/nature06130) |
| **VERDICT** | **COUNTS** |
| **Confidence** | moderate |
| **Resolving experiment** | — |

**Argument, and this is the most interesting verdict in the set.**

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

## 33. `UGDH` — UDP-glucose 6-dehydrogenase · K00012

| | |
|---|---|
| **Part 1 — substrate** | Host nucleotide-sugar pool |
| **Part 2 — consequence** | Not determined |
| **Evidence tier** | 6 |
| **Citations** | KEGG K00012. Block literature concerns the transfer step. |
| **VERDICT** | **COUNTS** |
| **Confidence** | low |
| **Resolving experiment** | As §7, for UDP-glucuronate |

**Argument.** Oxidises UDP-glucose to UDP-glucuronate, feeding capsule and acidic surface
polysaccharides. Surface-committed but a precursor. Same reasoning as §25 and §28. Defaults to
COUNTS.

---

## 34. `xtmA` — phage terminase small subunit · K07474

| | |
|---|---|
| **Part 1 — substrate** | **Viral** — the phage genome |
| **Part 2 — consequence** | **Assembly** — a discrete lifecycle step |
| **Evidence tier** | 1–2 |
| **Citations** | Extensive; ~88 PubMed results for phage terminase DNA packaging |
| **VERDICT** | **DOES NOT COUNT** |
| **Confidence** | high |
| **Resolving experiment** | — |

**Argument.** The small subunit recognises the packaging initiation site on the phage genome and
regulates the large subunit. The substrate is phage DNA; the consequence is genome packaging.
No host-directed reading is constructible.

That this appears in an AMG catalogue at all is worth a sentence in the paper.

---

## 35. `xtmB` — phage terminase large subunit · K06909

| | |
|---|---|
| **Part 1 — substrate** | **Viral** — the phage genome |
| **Part 2 — consequence** | **Assembly** |
| **Evidence tier** | 1–2 |
| **Citations** | As §34 |
| **VERDICT** | **DOES NOT COUNT** |
| **Confidence** | high |
| **Resolving experiment** | — |

**Argument.** The ATPase and nuclease of the packaging motor, translocating the genome into the
capsid against internal pressure. As §34.

---
---

# Tally

| Verdict | n | Families |
|---|---|---|
| **COUNTS** | **28** | `asnB` `cgeB` `dut` `galE` `glmS` `glycosyltransferase` `gmd` `hisF` `HMGCL` `IMPDH` `iscU` `K07336` `manB` `NAMPT` `nodU` `nrdH` `P4HA` `phoH` `psbA` `psbD` `pseB` `raxST` `rfbB` `rfbC` `speD` `tagD` `TALDO1` `UGDH` |
| **DOES NOT COUNT** | **4** | `dcm` `glycoside_hydrolase` `xtmA` `xtmB` |
| **UNRESOLVABLE** | **3** | `dsrC_tusE` `folate` `queuosine` |

## Control check

| Control | Required | Obtained | |
|---|---|---|---|
| `psbA` | COUNTS | COUNTS | ✅ |
| `psbD` | COUNTS | COUNTS | ✅ |
| `xtmA` | DOES NOT COUNT | DOES NOT COUNT | ✅ |
| `xtmB` | DOES NOT COUNT | DOES NOT COUNT | ✅ |

**All four controls pass.** The rule, applied faithfully, separates a photosystem subunit from a
DNA-packaging motor — which is the distinction it was built to capture.

## Observations from doing it

**Only two families were ruled out on their own merits.** `xtmA` and `xtmB` are the negative
controls, so the substantive exclusions are `dcm` and `glycoside_hydrolase`. Both have Tier 1–2
evidence; nothing else did, in the direction required.

**The protocol is hard to satisfy, and that is visible in the results.** Several families where
the mechanistic intuition is strong — `dut`, `IMPDH`, `nrdH` — default to COUNTS because
intuition is Tier 6 and Tier 6 cannot rule a family out. I recorded discomfort with `dut`
specifically. That is the protocol working as designed, and it means the disputed share this
produces is a **floor**, not an estimate.

**The rule failed to classify two families**, `glycosyltransferase` and `rfbC`. Serotype
conversion is neither host metabolic modulation nor one of the five enumerated lifecycle steps.
The conservative default was applied and the failure recorded rather than resolved by preference.
This should be stated in the paper — Chunk 4 found the field's criteria have the same defect.

**`TALDO1` is the sharpest case and I would draw attention to it.** A phage enzyme that
measurably doubles the host NADPH/NADP ratio, for a purpose the authors describe as feeding phage
replication. It counts, because the rule asks about consequence rather than purpose — but a
reasonable person applying the same rule could weigh it differently, and that is exactly why the
category is contested.

**The three UNRESOLVABLEs are all the same underlying problem**: a gene whose product has two
documented destinations, where the sequence does not say which. `dsrC/tusE` cannot even be
identified; `folE` sits at a branch point; queuosine enzymes serve tRNA and DNA alike. All three
have nameable resolving experiments, none of which has been done.

---
---

# What this is, and what it is not

**This is a second rater, not the record.** [[Adjudication Worksheet]] holds the verdicts of
record. This file was produced independently, blind to the sealed counts, and without consulting
any verdict already entered there.

**It was generated by Claude.** That fact has to appear in the write-up. A parallel adjudication
is only worth something if its provenance is stated — as a methodological feature, not a
disclosure buried in supplementary material.

## Why a second rater is worth having

Adjudication by a single unblinded person is the project's weakest methodological point, and it
was flagged as such in `06_project_brief.md` from the start (*"One analyst, no blinding"*). Two
independent raters addresses that directly:

- **Where the raters agree**, the verdict is more than one person's reading
- **Where they disagree**, the disagreement locates exactly where judgement is load-bearing — and
  those families are the ones the paper should discuss at length
- **Concordance is reportable.** "Two independent adjudications agreed on N of 35 families" is a
  quantitative statement about the robustness of the rubric, which no single adjudication can make

## How to use it without it contaminating your own verdicts

**If you have not yet judged a family, judge it before reading this file's entry for it.** Reading
first turns a second rater into an anchor and destroys the only thing that makes it valuable.

Then compare, and for each disagreement decide which reading you find better — recording *why*.
Your verdict remains the one of record; this one is evidence about how stable it is.

## Concordance with the record so far

**One family has been independently judged in both.**

| Family | Worksheet | This file | |
|---|---|---|---|
| `dcm` | DOES NOT COUNT, Tier 2, Burke *et al.*, high confidence | DOES NOT COUNT, Tier 2, Burke *et al.*, high confidence | **agree** |

Same verdict, same tier, same citation, same confidence, reached separately.

**1 of 1 concordant.** That is a sample of one and proves nothing on its own — but it is the
right start, and it is the biggest family in the ocean catalogue, so agreement there matters more
than agreement on a small one.

## Related

- [[Adjudication Worksheet]] — the verdicts of record
- [[Evidence Dossiers]] — the literature these verdicts rest on
- [[Adjudication Protocol]] — the rules
- [[How To Adjudicate]] — the mechanics
