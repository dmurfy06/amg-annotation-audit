---
tags: [project, research, adjudication, evidence]
---

# Evidence Dossiers

**One section per family, numbered and ordered to match [[Adjudication Worksheet]] exactly.**
Family 7 here is family 7 there. Work down both together.

**No verdicts.** Each section gives what the enzyme does, the phage-specific literature, and the
strongest case for *each* reading. The decision is yours.

Literature from **PubMed** unless noted; every citation was fetched and its abstract read before
being quoted. Search method and corrections are in the [Appendix](#appendix-c--method-and-corrections).

> [!tip] Shortcut
> Families **1, 2, 12, 13, 15, 16, 19, 21, 27** have no phage-specific evidence and are
> pre-filled in the worksheet. See [Appendix B](#appendix-b--the-evidence-free-families).

---

## 1. `asnB` — asparagine synthase (glutamine-hydrolysing)

**K01953** · EC 6.3.5.4

**What it does.** Amidates aspartate to asparagine, using glutamine as the nitrogen donor.
Standard amino-acid biosynthesis.

**Phage-specific evidence: none found.** → [Appendix B](#appendix-b--the-evidence-free-families)

**One adjacent finding, which is not what you need.** Ito *et al.* (2014, *PLoS One*) disrupted
**host** `asnH` in *Lactobacillus casei* and got **phage-resistant** mutants that had lost normal
peptidoglycan structure. [DOI](https://doi.org/10.1371/journal.pone.0083876) That is a host gene
affecting phage adsorption — same shape as the Sumrall result in §10 — and says nothing about
what a *phage-encoded* `asnB` does.

**Tier available: 6.**

---

## 2. `cgeB` — spore maturation protein CgeB

**K06320**

**What it does.** Involved in spore coat maturation in *Bacillus*; the CgeB family is
glycosyltransferase-like and contributes to the outermost spore layer.

**Phage-specific evidence: none found.** → [Appendix B](#appendix-b--the-evidence-free-families)

**Worth noting when you write it up.** This is a **sporulation** protein appearing in an AMG
catalogue. Whatever it is doing in a phage genome, "auxiliary metabolic gene" is an odd label for
it, and that is worth a clause even under a COUNTS verdict.

**Tier available: 6.**

---

## 3. `dcm` — DNA cytosine methyltransferase

**K00558, K17398** · EC 2.1.1.37

**What it does.** Methylates C5 of cytosine in DNA. In bacteria this is the "M" of
restriction–modification: methylate your own DNA at specific motifs and your restriction
endonucleases spare it.

**Phage-specific evidence — unusually direct.** Burke *et al.* (2021, *PNAS*) characterised
**phage-encoded TET dioxygenases** from viral metagenomes that oxidise 5-methylcytosine. The part
that matters here is what those TETs act on: the methyl groups installed by *"their genomically
cooccurring cytosine C5-methyltransferases"* — phage-encoded `dcm` homologues — sitting *"within
gene clusters specifying complex cytosine modifications that may be important for DNA packaging
and evasion of host restriction."* [DOI](https://doi.org/10.1073/pnas.2026742118)

**Case for HOST.** DNA methylation in bacteria has regulatory roles beyond defence — gene
expression, replication timing. A phage MTase methylating *host* DNA could reprogram host
expression. **No study demonstrating this for a phage `dcm` was found**; that absence is itself
the finding.

**Case for VIRAL.** The substrate described in the only direct work is the phage's own cytosines,
inside a modification cluster whose stated function is genome protection. Anti-restriction is the
textbook reason a phage carries a methyltransferase.

**Tier available: 2.** No knockout-and-measure experiment surfaced.

> [!caution] Not blind. `dcm` → *doesn't count* appears in the protocol's own worked-example table,
> so this verdict cannot be cited as evidence of impartiality. Say so in the write-up.

---

## 4. `dsrC_tusE` — sulfur relay

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

**Tier available: 3–4** for the ecology; **effectively 0** for telling which gene the
environmental calls actually are.

**Resolving experiment, if UNRESOLVABLE:** phylogenetic or HMM separation of DsrC from TusE, then
re-annotation. Until someone does it, no catalogue can support a sulfur-cycling claim from K11179.

---

## 5. `dut` — dUTP diphosphatase

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

**Tier available: 2–4.**

---

## 6. `folate` — folate / one-carbon pathway

**K00287, K00548, K01433, K01491, K01495, K01633, K09007, K13938, K13998, K19645**
Includes `folA`, `folB`, `folD`, `folE` (K01495), `folE2` (K09007), `metH`, `purU`, DHFR-TS.

**What it does.** Builds tetrahydrofolate, the universal one-carbon carrier — feeding purine
synthesis, thymidylate synthesis, methionine, and formylmethionyl-tRNA for translation initiation.

**The overlap you already know about.** `folE`/GTP cyclohydrolase I is the first committed step of
folate biosynthesis **and** the entry point to queuosine biosynthesis (§26). `folE2` is an
alternative at the same branch. All four are flagged **AMBIGUOUS** in the frozen accession list,
and Chunk 4 showed the wastewater paper's own rule cannot resolve them either.

**Cross-reference §26.** Thiaville *et al.* detected a 7-deazaguanine derivative **in phage DNA**;
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

**Tier available: 2** for the chemistry and the phage-DNA detection; **6** for what a phage `folE`
is specifically doing.

---

## 7. `galE` — UDP-glucose 4-epimerase

**K01784** · EC 5.1.3.2

**What it does.** Interconverts UDP-glucose and UDP-galactose. A **precursor** enzyme: its product
feeds surface glycans, but also several other pathways.

**Phage-specific evidence:** none specific to `galE`. See
[Appendix A](#appendix-a--the-nucleotide-sugar-and-cell-surface-literature) for the block
literature, which concerns the **transfer** step rather than precursor supply.

**Case for HOST.** Nucleotide-sugar supply is general host metabolism, feeding more than the
surface.

**Case for VIRAL.** If it is feeding surface modification, the block reasoning in §10 applies.

> [!warning] Don't import §10's verdict automatically
> The demonstrated phage biology in Appendix A is about glycosyltransferases **transferring**
> sugars onto the host surface. `galE` **makes the precursor**, which has many destinations. That
> the block reasoning carries to it is an assumption, not a finding.

**Tier available: 5–6.**

---

## 8. `glmS` — glutamine–fructose-6-phosphate transaminase

**K00820**

**What it does.** The committed entry step to **amino-sugar biosynthesis** — makes glucosamine-
6-phosphate, upstream of UDP-GlcNAc, which feeds peptidoglycan, LPS and teichoic acids.

**Phage-specific evidence:** none specific. See
[Appendix A](#appendix-a--the-nucleotide-sugar-and-cell-surface-literature).

**Case for HOST.** Amino sugars feed the cell wall — the cell's largest structural investment.
This is core host anabolism.

**Case for VIRAL.** As §7: if it is feeding surface modification for receptor control, §10's
reasoning applies. But `glmS` sits further upstream than almost anything else in this block.

**Tier available: 6.**

---

## 9. `glycoside_hydrolase`

**K01179, K01185, K01187, K01190, K01199, K03791** — endoglucanase, lysozyme, α-glucosidase,
β-galactosidase, glucan endo-1,3-β-D-glucosidase, putative chitinase

**What they do.** Cleave glycosidic bonds. In phage biology: **endolysins** (lyse the cell from
inside at the end of infection), **virion-associated lysins** (locally degrade the wall during
entry), **tailspike depolymerases** (chew capsule or O-antigen to reach the receptor).

**Phage-specific evidence — direct and structural.** Yuan & Gao (2016, *Front Microbiol*) did
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

**Tier available: 1–2.**

---

## 10. `glycosyltransferase`

**K00754, K03669, K03814, K07270, K15521** — `bshA`, `mdoH`, `mtgA`, family-25 GT, `mshA`

**What they do.** Transfer sugars onto growing glycans. Downstream: **O-antigen, LPS, capsule,
wall teichoic acid** — the bacterial cell surface.

**Phage-specific evidence — good.** See
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
> Three defensible readings, all permitted:
> 1. receptor modification is a **lifecycle function** (superinfection exclusion / host-range
>    control) → DOES NOT COUNT
> 2. it is **genuine host modification** — the surface chemistry really is changed, persistently
>    → COUNTS
> 3. **UNRESOLVABLE**, and name the experiment
>
> Whichever you choose, **say in the argument box that the rule underdetermined it.** Chunk 4
> showed the field's rules have this problem; "and so does ours, here, and we noticed" is a far
> stronger paper than hiding it.

**Tier available: 2.**

---

## 11. `gmd` — GDP-mannose 4,6-dehydratase

**K01711** · EC 4.2.1.47

**What it does.** First step from GDP-mannose toward GDP-fucose and related deoxy sugars, which
go into O-antigen and capsule.

**Phage-specific evidence:** none specific. See
[Appendix A](#appendix-a--the-nucleotide-sugar-and-cell-surface-literature).

**Case for HOST / VIRAL:** as §7 — a precursor enzyme, so the §10 reasoning is an assumption
rather than a finding. `gmd` is more surface-committed than `galE` (fucose is largely a surface
sugar), which is a point you can make either way.

**Tier available: 5–6.**

---

## 12. `hisF` — imidazole glycerol-phosphate synthase subunit

**K02500** · EC 4.3.2.10

**What it does.** Histidine biosynthesis. Also connects to purine metabolism — the reaction
releases AICAR, which re-enters purine synthesis.

**Phage-specific evidence: none found.** → [Appendix B](#appendix-b--the-evidence-free-families)

**Tier available: 6.**

---

## 13. `HMGCL` — hydroxymethylglutaryl-CoA lyase

**K01640** · EC 4.1.3.4

**What it does.** Cleaves HMG-CoA to acetyl-CoA and acetoacetate. Leucine catabolism and ketone
body formation.

**Phage-specific evidence: none found.** → [Appendix B](#appendix-b--the-evidence-free-families)

**Tier available: 6.**

---

## 14. `IMPDH` — IMP dehydrogenase

**K00088** · EC 1.1.1.205

**What it does.** The rate-limiting committed step of **guanine nucleotide** biosynthesis:
IMP → XMP, en route to GMP/GDP/GTP/dGTP.

**Phage-specific evidence:** no functional study of a phage-encoded IMPDH surfaced. The structural
argument is the same as §5 and §20 — a nucleotide-supply enzyme, where during infection the pool
being drawn down replicates the phage genome.

**Worth knowing:** IMPDH sits in KEGG's **09104 Nucleotide metabolism** — the category the
wastewater paper's own rule excludes (Chunk 4).

**Case for HOST.** Guanine nucleotides serve the whole cell.

**Case for VIRAL.** Feeding phage genome replication; Martin *et al.* make this argument for
nucleotide-pathway genes generally.

**Tier available: 6.** Under the protocol, Tier 6 alone cannot rule it out.

---

## 15. `iscU` — Fe-S cluster scaffold / NifU

**K04488**

**What it does.** Scaffold protein on which iron–sulfur clusters are assembled before delivery to
apo-proteins. Fe-S clusters are cofactors for a very large number of enzymes.

**Phage-specific evidence: none found.** → [Appendix B](#appendix-b--the-evidence-free-families)

> [!warning] Beware the false positive here
> A PubMed search returns one hit, which is about the *E. coli* Hsc66/IscU chaperone and uses
> **phage display as a laboratory method**. "Phage" is the technique, not the biology.

**Tier available: 6.**

---

## 16. `K07336` — PKHD-type hydroxylase

**K07336** · EC 1.14.11.-

**What it does.** An uncharacterised 2OG-Fe(II) oxygenase. **KEGG gives it no gene symbol** — the
family label *is* the accession.

**Phage-specific evidence: none found.** → [Appendix B](#appendix-b--the-evidence-free-families)

> [!important] Worth its own sentence in the paper
> This is counted as an auxiliary **metabolic** gene while being an enzyme **whose substrate
> nobody has identified.** The gap here is more basic than for the other eight: it is not that
> nobody has studied the phage copy, it is that nobody has characterised the enzyme at all.

**Tier available: 6, and arguably less.**

---

## 17. `manB` — phosphomannomutase

**K01840** · EC 5.4.2.8

**What it does.** Mannose-6-P ⇄ mannose-1-P, feeding GDP-mannose and thence surface glycans.
A **precursor** enzyme.

**Phage-specific evidence:** none specific. See
[Appendix A](#appendix-a--the-nucleotide-sugar-and-cell-surface-literature). Same caution as §7.

**Tier available: 5–6.**

---

## 18. `NAMPT` — nicotinamide phosphoribosyltransferase

**K03462** · EC 2.4.2.12

**What it does.** First step of **NAD⁺ salvage**: nicotinamide → nicotinamide mononucleotide,
en route to NAD⁺.

**Phage-specific evidence — Tier 1–2.** Lee, Li & Miller (2017, *J Bacteriol*), *"Vibrio Phage
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

**Tier available: 1–2.**

---

## 19. `nodU` — carbamoyltransferase

**K00612** · EC 2.1.3.-

**What it does.** Transfers a carbamoyl group. In rhizobia, `nodU` carbamoylates the Nod factor —
a secreted signalling glycan. Outside that context the target is generally unknown.

**Phage-specific evidence: none found.** → [Appendix B](#appendix-b--the-evidence-free-families)

**Tier available: 6.**

---

## 20. `nrdH` — glutaredoxin-like protein NrdH

**K06191**

**What it does.** Redox partner of class Ib **ribonucleotide reductase** (RNR). RNR converts
ribonucleotides to deoxyribonucleotides — the committed step in making DNA precursors.

**Phage-specific evidence — indirect but telling.** PubMed returns ~130 results for bacteriophage
ribonucleotide reductase. More pointedly, Sakowski *et al.* (2021, *Nature Microbiology*) built a
method for capturing virus–host interactions that *"fuses a **phage marker, the ribonucleotide
reductase gene**, with the host 16S rRNA gene of infected bacterial cells."*
[DOI](https://doi.org/10.1038/s41564-021-00873-4)

**RNR is used as a marker gene for phage** — the same status `phoH` has (§22). Phage RNRs are
distinct enough from host copies to identify a virus, which is not the signature of an
incidentally acquired gene. Huang *et al.* (2021) also list RNR among the seven high-frequency
roseophage AMGs. [DOI](https://doi.org/10.1111/1462-2920.15412)

**Case for HOST.** RNR supplies the dNTP pool the whole cell uses.

**Case for VIRAL.** Those dNTPs replicate the phage genome; a phage encoding its own RNR is the
textbook case of provisioning its own replication, and the phylogenetic distinctness supports
specialisation.

**Tier available: 4–5.** No experiment separates "the host's dNTP pool" from "the phage's" during
infection, **because during infection they are the same pool** — which may make this genuinely
unresolvable. If you go that way, that is the experiment problem to name.

---

## 21. `P4HA` — prolyl 4-hydroxylase

**K00472** · EC 1.14.11.2

**What it does.** 2OG-dependent hydroxylation of proline residues in peptide linkage, giving
4-hydroxyproline — a structural modification best known from collagen.

**Phage-specific evidence: none verified.** → [Appendix B](#appendix-b--the-evidence-free-families)

> [!warning] PENDING — a live lead worth 15 minutes of your library access
> A web source asserted that prolyl-4-hydroxylase appears in **megaphage virion proteomics**
> (*npj Viruses* 2025) and that P4HA is among the most abundant AMGs in marine viromes.
> **I could not verify either** — the article sits behind a login wall and PubMed did not return
> it. A separate paper on "viral prolyl-4-hydroxylase" concerns a **eukaryotic algal virus**, not
> a phage.
>
> **If you can reach that paper and prolyl 4-hydroxylase is in its virion proteomics table, this
> family leaves the evidence-free group** and probably becomes a structural verdict on the same
> logic as §9.

**Tier available: 6 pending that check.**

---

## 22. `phoH` — phosphate starvation-inducible protein

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

**Tier available: 4–5.** **Resolving experiment:** delete or express phage `phoH` and measure
phosphate uptake in infected versus uninfected cells under limitation.

---

## 23. `psbA` — photosystem II D1 protein

**K02703** · EC 1.10.3.9

**What it does.** D1 is half the heterodimeric core of the photosystem II reaction centre, and the
most rapidly turned-over protein in the photosynthetic apparatus — continually photodamaged and
continually replaced.

**Phage-specific evidence — the strongest in the list.** Sullivan *et al.* (2006, *PLoS Biology*)
screened 33 cultured cyanophages plus field samples: **88% of phage genomes contain `psbA`**,
carried *"presumably to augment the host photosynthetic machinery during infection."*
[DOI](https://doi.org/10.1371/journal.pbio.0040234)

Sieradzki *et al.* (2019, *Nature Communications*) measured expression in situ by
metatranscriptomics: **sometimes more than 50% of all cyanobacterial + viral `psbA` expression is
of viral origin**, highlighting *"the contribution of viruses to photosynthesis and oxygen
production."* [DOI](https://doi.org/10.1038/s41467-019-09106-z)

Lindell *et al.* (2007, *Nature*) show `psbA` transcribed **together with phage DNA replication
genes**, in a cluster with `hli`, `talC` and `nrd`, described as *"a functional unit involved in
energy and deoxynucleotide production for phage replication."*
[DOI](https://doi.org/10.1038/nature06130)

**Case for HOST.** Inserted into the **host's** thylakoid membrane, replacing a host subunit
photodamage is destroying; the measured consequence is that photosynthesis keeps running.

**Case for VIRAL.** Lindell places it in the replication module — the lights stay on so the phage
can finish. **Note this argument generalises to almost everything**, which is why Part 2 asks
about *discrete lifecycle steps* rather than ultimate benefit.

**Tier available: 1–2.**

> [!caution] Not blind. `psbA` → COUNTS appears in the protocol's worked-example table.

---

## 24. `psbD` — photosystem II D2 protein

**K02706** · EC 1.10.3.9

**What it does.** The other half of the PSII reaction-centre core. Pairs with D1.

**Phage-specific evidence.** Sullivan *et al.* (2006): **50% of cyanophage genomes carry both
`psbA` and `psbD`**, and *"nearly all of the phages that encoded both psbA and psbD had broad host
ranges."* They speculate that carrying `psbD` too *"may reflect constraints on coupling of viral-
and host-encoded PsbA-PsbD in the photosynthetic reaction center across divergent hosts."*
[DOI](https://doi.org/10.1371/journal.pbio.0040234)

**Case for HOST / VIRAL:** as §23.

> [!tip] Judge this separately from `psbA`, and the host-range point is why
> `psbD` is carried by **half** as many phages as `psbA`, and its presence correlates with broad
> host range. That is a genuine difference between the two, and it is evidence about *why* a
> phage carries the pair rather than just D1 — which bears on whether this is host-directed
> function or compatibility engineering.

**Tier available: 2.**

---

## 25. `pseB` — UDP-N-acetylglucosamine 4,6-dehydratase

**K15894**

**What it does.** First step of **pseudaminic acid** biosynthesis — a sialic-acid-like sugar used
in surface glycans and flagellar glycosylation.

**Phage-specific evidence:** none specific. See
[Appendix A](#appendix-a--the-nucleotide-sugar-and-cell-surface-literature).

**A point worth making either way.** Pseudaminic acid is a **surface-committed** sugar with few
other destinations — so unlike `galE` or `manB`, the "it feeds many pathways" defence is weaker
here. That cuts toward surface modification being the actual purpose.

**Tier available: 5–6.**

---

## 26. `queuosine` — `queC`, `queD`, `queE`, `queF`

**K01737, K06879, K06920, K09457, K10026**

**What the pathway does.** Builds 7-deazaguanine derivatives. Classically it ends in queuosine, a
hypermodified base at the wobble position of certain tRNAs. **`folE` supplies the entry precursor
— the same step that feeds folate biosynthesis** (§6), which is why these sit at the branch point
that moves the headline by 18 points.

**Phage-specific evidence — reframes the family.** Thiaville *et al.* (2016, *PNAS*) showed
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
> That may be a genuine **UNRESOLVABLE**. **Resolving experiment:** detect 7-deazaguanine
> derivatives in the DNA of phages carrying these genes versus those that don't. Thiaville did it
> for one phage; nobody has done it systematically.

**Tier available: 2.**

---

## 27. `raxST` — sulfotransferase

**K13472**

**What it does.** Transfers sulfate to an acceptor. In *Xanthomonas*, RaxST sulfates a secreted
peptide involved in plant immune recognition. Outside that, the target is generally unknown.

**Phage-specific evidence: none found.** → [Appendix B](#appendix-b--the-evidence-free-families)

> [!warning] Beware the false positives here
> "Bacteriophage sulfotransferase" returns hits that are a **mouse liver study** (whose keyword
> list includes *"bacteriophage P1 cyclization recombinase"* — Cre-lox) and a **cancer
> autoantibody study using phage microarrays**. Method, not biology.

**Tier available: 6.**

---

## 28. `rfbB` — dTDP-glucose 4,6-dehydratase

**K01710** · EC 4.2.1.46

**What it does.** Second step of the dTDP-L-rhamnose pathway. Rhamnose is a **major O-antigen
sugar**.

**Phage-specific evidence:** none specific. See
[Appendix A](#appendix-a--the-nucleotide-sugar-and-cell-surface-literature).

**As with `pseB` (§25),** dTDP-rhamnose is strongly surface-committed, so the "feeds many
pathways" defence is weaker than for `galE`.

**Tier available: 5–6.**

---

## 29. `rfbC` — O-antigen biosynthesis protein

**K20444** · EC 2.4.1.-

**What it does.** KEGG's own description names it **O-antigen biosynthesis**. Of the whole
nucleotide-sugar block, this is the most explicitly surface-dedicated.

**Phage-specific evidence:** the block literature in
[Appendix A](#appendix-a--the-nucleotide-sugar-and-cell-surface-literature) applies most directly
here — Mann *et al.* and Sun *et al.* are specifically about phage modification of O-antigen.

**Case for HOST / VIRAL:** as §10, and with less of the precursor-ambiguity caveat. If you reach
different verdicts for §10 and §29, be sure you can say why.

**Tier available: 2** (via the block literature, which is about this exact process).

---

## 30. `speD` — S-adenosylmethionine decarboxylase

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
terminase argument (§34–35).

**Tier available: 5–6.** The polyamine-in-virion literature is real but old and organism-specific;
check whether it applies to the phages in these catalogues before leaning on it.

---

## 31. `tagD` — glycerol-3-phosphate cytidylyltransferase

**K00980** · EC 2.7.7.39

**What it does.** Makes CDP-glycerol, the donor for **wall teichoic acid** — a major Gram-positive
surface polymer.

**Phage-specific evidence:** none specific, but see the Sumrall result in
[Appendix A](#appendix-a--the-nucleotide-sugar-and-cell-surface-literature): removing glucose
decoration from **wall teichoic acid** made *Listeria* **resistant to phage** by preventing
adsorption. That is the same polymer `tagD` feeds.

**Case for HOST.** Teichoic acid is core cell-wall biosynthesis.

**Case for VIRAL.** WTA glycosylation *is* the phage receptor in Gram-positives, so §10's
receptor-control reasoning applies here more directly than to most of the block.

**Tier available: 5–6.**

---

## 32. `TALDO1` — transaldolase

**K00616** · EC 2.2.1.2

**What it does.** Reversible carbon-shuffling step of the **non-oxidative pentose phosphate
pathway**, linking PPP to glycolysis. The PPP makes **NADPH** and **ribose 5-phosphate** — the
sugar backbone of nucleotides.

**Phage-specific evidence — Tier 1–2, and among the best here.** Thompson *et al.* (2011, *PNAS*),
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

**Tier available: 1–2.**

---

## 33. `UGDH` — UDP-glucose 6-dehydrogenase

**K00012** · EC 1.1.1.22

**What it does.** Oxidises UDP-glucose to UDP-glucuronate, feeding capsule and other acidic
surface polysaccharides.

**Phage-specific evidence:** none specific. See
[Appendix A](#appendix-a--the-nucleotide-sugar-and-cell-surface-literature).

**As with `pseB` and `rfbB`,** UDP-glucuronate is fairly surface-committed.

**Tier available: 5–6.**

---

## 34. `xtmA` — phage terminase small subunit

**K07474**

**What it does.** Recognises the packaging initiation site on the phage genome and regulates the
large subunit. Part of the DNA-packaging motor.

**Case for HOST.** None that can be constructed. The substrate is the phage genome.

**Case for VIRAL.** Assembly.

> [!note] Why it is in your list at all
> This is a genuine entry in the **soil AMG catalogue**. A DNA-packaging motor subunit was called
> an auxiliary *metabolic* gene. Worth a sentence in the paper whatever the verdict.

**Tier available: 1–2, abundantly.** PubMed returns ~88 results for phage terminase DNA packaging.

> [!caution] Not blind — this note previously identified `xtmA`/`xtmB` as the negative controls.

---

## 35. `xtmB` — phage terminase large subunit

**K06909**

**What it does.** The ATPase and nuclease of the packaging motor; translocates the genome into the
preformed capsid against enormous internal pressure. Among the best-characterised machines in
phage biology.

**Case for HOST / VIRAL:** as §34.

**Tier available: 1–2, abundantly.**

---
---

# Appendix A — the nucleotide-sugar and cell-surface literature

Shared evidence for §7 `galE`, §8 `glmS`, §10 `glycosyltransferase`, §11 `gmd`, §17 `manB`,
§25 `pseB`, §28 `rfbB`, §29 `rfbC`, §31 `tagD`, §33 `UGDH`.

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

# Appendix B — the evidence-free families

**§1 `asnB` · §2 `cgeB` · §12 `hisF` · §13 `HMGCL` · §15 `iscU` · §16 `K07336` · §19 `nodU` ·
§21 `P4HA` · §27 `raxST`**

No phage-specific functional evidence found for any of these after three independent search
strategies. **These nine are pre-filled in the worksheet** with the protocol's mechanical default.

## Verdict: COUNTS, not UNRESOLVABLE

Both are permitted — the missing experiment *is* nameable. But COUNTS is right, for three reasons.

**1. UNRESOLVABLE would conflate two different situations.** §26 `queuosine` has evidence
pointing **both ways** — genuinely undecidable. §12 `hisF` has **no evidence at all**. Same label,
two incompatible meanings, in the project's most reusable artefact. Keep UNRESOLVABLE for *"the
evidence conflicts."*

**2. COUNTS is the conservative direction, and this is where it matters most.** The
maximally-strict rule excludes UNRESOLVABLE families too — so marking nine that way would
**inflate the disputed share on the basis of nobody having done an experiment.** That is using
ignorance to support your own hypothesis: the most attackable move available, avoidable at no cost.

**3. The finding does not need the verdict.** "No phage-specific evidence exists for these
families" is a **separate measurement** that depends on no rubric and nobody's agreement — which
makes it *more* durable than the disputed share, not less. Report it as its own quantity.

> [!important] Two independent findings instead of one
> 1. **X% of calls sit in categories the field's own experts dispute** — depends on the rubric
> 2. **Y% sit in families with no phage-specific evidence at all** — depends on nothing
>
> The second cannot be argued away by rejecting Martin *et al.*

## Draft paragraph for the paper

Percentages filled in after the verdicts close and the sealed counts open.

> Of the 35 gene families adjudicated, nine — accounting for **[X]%** of KO-assigned calls — had
> no phage-specific functional evidence that we were able to identify. For these families we found
> no study characterising the phage-encoded protein, determining its substrate, or measuring its
> expression during infection, and none of the three source catalogues discussed them in their
> text. Searches were conducted in three independent passes: thematic queries, per-gene queries,
> and targeted preprint and web searching, with all candidate hits verified against primary
> records before inclusion. Two families initially assigned to this group (transaldolase and
> nicotinamide phosphoribosyltransferase) were removed following the second pass, and one further
> lead remains unresolved; we therefore report this as a **lower bound on the evidence available**,
> not a demonstration of its absence.
>
> We do not treat this as grounds for exclusion. Under our pre-registered protocol, absence of
> evidence defaults to inclusion, and these families are counted as auxiliary metabolic genes
> throughout. We report the observation separately because it bears on a different question: for
> approximately a quarter of the families contributing to these catalogues, the AMG designation
> rests on sequence similarity to a characterised host enzyme and on nothing else.

> [!tip] The sentence to avoid
> *"Nobody has ever studied these genes."* You don't know that. What you know is that three
> search strategies found nothing and the catalogue papers don't discuss them. Narrower, true,
> and nobody can knock it down.

## Also checked: the catalogue papers themselves

The full text of all three catalogue papers was searched for each gene symbol and enzyme name.
**Zero mentions.** But state this carefully — these genes sit in supplementary tables of tens of
thousands of rows, and **papers do not discuss every gene they count.** The defensible claim is
the narrow one: for these families the entire evidentiary basis is a database match.

---

# Appendix C — method and corrections

**Searches run.** Three passes: (1) thematic PubMed queries by biological topic; (2) per-gene
PubMed queries using gene symbol, enzyme name and reaction; (3) targeted web and preprint
searching, with every promising hit verified through PubMed before use. The bioRxiv tool available
here browses by date and category only — **it has no keyword search** — so preprint coverage came
via web search.

**Corrections made, recorded rather than quietly fixed:**

| # | What was claimed | What was true |
|---|---|---|
| 1 | *"I searched each of the eleven and found none"* | I had run **thematic** searches and inferred absence. Not a per-gene search. |
| 2 | `TALDO1` has no evidence | **Tier 1–2.** Thompson 2011 *PNAS*, Lindell 2007 *Nature*. See §32. |
| 3 | `NAMPT` has no evidence | **Tier 1–2.** Lee 2017 *J Bacteriol*. See §18. |
| 4 | The negative controls are blind | **They are not.** All four controls are named in the protocol or in [[How To Adjudicate]]. |

**False positives to watch for.** "Phage" appears in thousands of papers as a *tool*:
**phage display** (caught in §15 `iscU`), **phage microarrays** and **Cre-lox from phage P1**
(caught in §27 `raxST`), and a substring match inside the word "di**scu**ssion" (caught in the
catalogue-paper search). Check that a hit concerns a phage-*encoded* gene before counting it.

**Two corrections came from Daniel asking for a re-check.** Both times the check was justified.
A negative claim needs more evidence than a positive one, not less.

## Related

- [[Adjudication Worksheet]] — where the verdicts go
- [[How To Adjudicate]] — the mechanics
- [[Adjudication Protocol]] — the rules
