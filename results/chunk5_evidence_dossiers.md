---
tags: [project, research, adjudication, evidence]
---

# Evidence Dossiers

Literature gathered per family so you can judge without doing the searching.
**No verdicts here — that's [[Adjudication Worksheet]].** This note lays out what's known and
the strongest case for each reading, and stops there.

Literature retrieved from **PubMed**. Every citation below was fetched and its abstract read;
nothing is quoted that I have not seen. DOIs link to source.

> [!warning] Read the dossier, then decide — don't let it decide
> Where I've written "the case for X" and "the case for Y", both are meant to be genuinely
> arguable. If one looks obviously right to you, that's your judgement forming, which is the
> point. If one looks obviously right *because of how I've written it*, tell me and I'll rewrite
> it flatter.

**Status: all 35 families covered.** Order is alphabetical within each batch, per the protocol.

---

## `dcm` — DNA cytosine methyltransferase (K00558, K17398)

**What the enzyme does.** Transfers a methyl group to the C5 position of cytosine in DNA.
In bacteria this is the "M" half of restriction–modification: the host methylates its own DNA at
specific motifs, and its restriction endonucleases cleave any DNA lacking that mark.

**The phage-specific evidence — and it is unusually direct.**

According to PubMed, Burke *et al.* (2021, *PNAS*) characterised **phage-encoded TET dioxygenases
found in viral metagenomes** and showed they oxidise 5-methylcytosine. The relevant part for this
family is what the TETs work *on*: the paper reports the phage TETs cluster with, and act on the
methyl groups installed by, *"their genomically cooccurring cytosine C5-methyltransferases"* —
i.e. phage-encoded `dcm` homologues — and that these sit *"within gene clusters specifying complex
cytosine modifications that may be important for DNA packaging and evasion of host restriction."*
[DOI](https://doi.org/10.1073/pnas.2026742118)

So there is direct biochemical work on phage-encoded C5-methyltransferases, and the substrate
described is the **phage's own cytosines**, in a modification cluster.

**The case that it acts on a HOST substrate / sustains host metabolism:**
Methylation is a genuine enzymatic modification of DNA, and DNA methylation in bacteria does have
regulatory roles beyond defence (gene expression, replication timing). If a phage-encoded MTase
methylated *host* DNA it could in principle reprogram host gene expression. **I found no study
demonstrating this for a phage `dcm`** — that absence is itself the finding.

**The case that it acts on a VIRAL substrate / serves a lifecycle step:**
The Burke paper places phage C5-MTases in modification clusters whose described function is
protecting the phage genome. Anti-restriction is the textbook reason a phage carries a
methyltransferase: methylate your own genome in the host's pattern and the host's endonucleases
ignore it. Genome protection is a discrete lifecycle step under the protocol's Part 2.

**Evidence tier available: 2** (biochemical characterisation of the phage-encoded protein and its
modification cluster). Not Tier 1 — no knockout-and-measure experiment surfaced.

---

## `dut` — dUTP diphosphatase (K01520)

**What the enzyme does.** Hydrolyses dUTP to dUMP + PPi. Two jobs at once: it keeps dUTP out of
the nucleotide pool (uracil would otherwise be misincorporated into DNA) and it supplies dUMP,
the substrate for thymidylate synthase. So it sits directly on the path to dTTP.

**Phage-specific evidence.** According to PubMed, Huang *et al.* (2021, *Environ Microbiol*)
catalogued 180 AMGs across 50 roseophage genomes and found seven high-frequency ones — *"trx,
grx, RNR, thyX, DCD, phoH, and mazG"* — reporting that **most are** *"involved in the nucleotide
biosynthesis pathway."* `dUTPase` appears in their *sporadic* AMG set.
[DOI](https://doi.org/10.1111/1462-2920.15412)

**A complication worth knowing about.** Phage dUTPases have a documented role that is not
enzymatic at all. Nyíri *et al.* (2019, *Biomolecules*) and (2024, *Sci Rep*) show
staphylococcal phage dUTPases binding the **Stl master repressor** of pathogenicity islands,
de-repressing island transfer — a signalling/regulatory function distinct from dUTP hydrolysis.
[DOI](https://doi.org/10.3390/biom9090488) ·
[DOI](https://doi.org/10.1038/s41598-024-51260-y)

That doesn't settle your question, but it means "what is a phage dUTPase for?" has at least two
published answers, and neither is host metabolic modulation.

**The case for HOST / sustains host metabolism:**
dUTPase is a housekeeping enzyme of the host's own nucleotide pool. A phage boosting it arguably
raises the cell's overall dNTP supply, which is metabolic modulation in the ordinary sense.

**The case for VIRAL / lifecycle step:**
The pool it protects is the one being drawn on to replicate the **phage** genome, during an
infection that ends in lysis. Under the protocol's Part 2, feeding your own genome replication is
a discrete lifecycle step, not sustaining host metabolism. Martin *et al.* make exactly this
argument for nucleotide-pathway genes generally.

**Evidence tier available: 2–4.** Structural/biochemical work on phage dUTPases exists (Tier 2)
but addresses the Stl interaction rather than the AMG question; the AMG-context evidence is
genomic (Tier 4).

---

## `psbA` (K02703) and `psbD` (K02706) — photosystem II D1 and D2

*(Two worksheet entries; the evidence is shared, so it is presented once.)*

**What they do.** D1 and D2 form the heterodimeric core of the photosystem II reaction centre.
D1 is the most rapidly turned-over protein in the photosynthetic apparatus — it is continually
damaged by light and continually replaced.

**Phage-specific evidence, and this is the strongest in the whole list.**

Sullivan *et al.* (2006, *PLoS Biology*) screened 33 cultured cyanophages plus field samples and
found **88% of phage genomes contain `psbA`, and 50% contain both `psbA` and `psbD`**, describing
them as host-like photosynthesis genes carried *"presumably to augment the host photosynthetic
machinery during infection."* [DOI](https://doi.org/10.1371/journal.pbio.0040234)

Sieradzki *et al.* (2019, *Nature Communications*) went further and measured expression in situ
by metatranscriptomics, reporting that **sometimes more than 50% of all cyanobacterial + viral
`psbA` expression is of viral origin**, and concluding this highlights *"the contribution of
viruses to photosynthesis and oxygen production."*
[DOI](https://doi.org/10.1038/s41467-019-09106-z)

**The case for HOST / sustains host metabolism:**
The gene product is inserted into the **host's** thylakoid membrane, replacing a host subunit
that photodamage is destroying. The measured consequence is that photosynthesis keeps running in
an infected cell. Substrate: host. Consequence: sustaining host metabolism.

**The case for VIRAL / lifecycle step:**
The phage keeps the lights on only because it needs ATP and reducing power to finish replicating
before the cell dies — so ultimately this serves phage replication. **Note that this argument
generalises to almost everything**, which is precisely why the protocol's Part 2 asks whether
the action is a *discrete lifecycle step* rather than whether it ultimately benefits the virus.

**Evidence tier available: 1–2.** Expression measured during real infections in the environment.
This is as good as the evidence in this field gets.

---

## `queuosine` — `queC`, `queD`, `queE`, `queF` and relatives

**What the pathway does.** Builds 7-deazaguanine derivatives. In the classical picture this ends
in queuosine, a hypermodified base inserted into the wobble position of certain tRNAs, tuning
translation. `folE`/GTP cyclohydrolase I supplies the entry-point precursor — **the same step
that feeds folate biosynthesis**, which is why these genes sit at the branch point that moves
your headline by 18 points.

**The phage-specific evidence, which reframes the family.**

According to PubMed, Thiaville *et al.* (2016, *PNAS*) showed that 7-deazaguanine derivatives are
inserted **into DNA, not only tRNA**. They detected modified deoxynucleosides in bacterial DNA
from gene clusters containing preQ₀-synthesis genes, and their transformation experiments
*"strongly suggest a restriction-modification role for the cluster."* Crucially for you, they also
report finding **2′-deoxy-7-formamidino-7-deazaguanosine in the *E. coli* bacteriophage 9g**.
[DOI](https://doi.org/10.1073/pnas.1518570113)

Hutinet *et al.* (2016, *RNA Biology*) summarise the position: seven-deazapurine modifications
*"were thought to be highly specific of tRNAs, but have now been discovered in DNA of phages and
of phylogenetically diverse bacteria"*, and *"the presence of 7-deazapurine in DNA is proposed to
be a protection mechanism against endonucleases."*
[DOI](https://doi.org/10.1080/15476286.2016.1265200)

de Crécy-Lagard *et al.* (2024, *MMBR*) review the field and list among the functions of
deazaguanine modifications *"cellular stress resistance, self-nonself discrimination mechanisms,
and host evasion defenses."* [DOI](https://doi.org/10.1128/mmbr.00199-23)

**The case for HOST / sustains host metabolism:**
Queuosine's established role is tRNA modification, which affects translational fidelity across
the whole cell. The wastewater authors themselves note the genes *"could also participate in tRNA
biogenesis."* If the phage copies feed host tRNA modification, that is genuine host metabolic
modulation.

**The case for VIRAL / lifecycle step:**
The pathway's product has been directly detected **in phage DNA**, and the function attributed to
it in that context is protection from host endonucleases. That makes the substrate viral and the
consequence genome protection — a discrete lifecycle step.

> [!important] The specific question you have to answer here
> The evidence shows this pathway does **both** things in different organisms. So the question is
> not "what can 7-deazaguanine chemistry do?" but **"when a phage carries `queC`/`queD`/`queE`,
> which is it doing?"** Note that a phage carrying the pathway to modify its own DNA needs the
> same enzymes as one feeding host tRNA — the genes do not distinguish the two uses.
>
> That may be a case for **UNRESOLVABLE** — in which case the protocol requires you to name the
> experiment. A plausible one: detect 7-deazaguanine derivatives in the DNA of phages whose
> genomes carry these genes, versus those that don't. Thiaville *et al.* did exactly that for one
> phage; nobody has done it systematically.

**Evidence tier available: 2.** Direct chemical detection of the pathway's product in phage DNA.

---

## `xtmA` / `xtmB` — phage terminase small and large subunit (K07474, K06909)

**What they do.** The terminase holoenzyme is the phage DNA-packaging motor. The large subunit
provides ATPase and nuclease activity; the small subunit recognises the packaging initiation site.
Together they translocate the phage genome into the preformed capsid against enormous internal
pressure. PubMed returns 88 results for phage terminase DNA packaging — this is among the best
characterised machines in phage biology.

**The case for HOST / sustains host metabolism:**
None that I can construct. The substrate is the phage genome; the product is a filled phage head.

**The case for VIRAL / lifecycle step:**
Assembly. It is difficult to name a more purely viral function.

> [!note] Why this is in your list at all
> These are genuine entries in the **soil AMG catalogue**. A DNA-packaging motor was called an
> auxiliary *metabolic* gene. Whatever verdict you reach, that is worth a sentence in the paper.

**Evidence tier available: 1–2**, abundantly.

---

---

# Batch 2 — the cell-surface block, glycoside hydrolases, and `phoH`

## `glycosyltransferase` — plus `galE` `gmd` `manB` `rfbB` `rfbC` `UGDH` `pseB` `glmS` `tagD`

*(One shared evidence base. Each still gets its own verdict — the enzymes differ in how directly
they touch the surface.)*

**What these enzymes do.** They build and interconvert **nucleotide sugars** — UDP-glucose,
UDP-galactose, dTDP-rhamnose, GDP-mannose and relatives — and transfer those sugars onto growing
glycans. Downstream: **O-antigen, LPS, capsule, wall teichoic acid.** That is, the bacterial cell
surface.

- `galE` UDP-glucose 4-epimerase · `UGDH` UDP-glucose 6-dehydrogenase · `gmd` GDP-mannose
  4,6-dehydratase · `rfbB` dTDP-glucose 4,6-dehydratase · `rfbC` O-antigen biosynthesis protein ·
  `manB` phosphomannomutase · `glmS` glutamine–fructose-6-P transaminase (entry to amino sugars) ·
  `pseB` pseudaminic acid pathway · `tagD` teichoic acid pathway
- `glycosyltransferase` — the transfer step itself

**The phage-specific evidence, and it is unusually good here.**

According to PubMed, Mann *et al.* (2015, *J Biol Chem*) state that lysogenic bacteriophages
encode enzymes that modify LPS O-antigen glycans, *"altering the structure of the bacteriophage
receptor and resulting in serotype conversion"*, and demonstrate phage-mediated glucosylation of
an O-antigen experimentally. [DOI](https://doi.org/10.1074/jbc.M115.660803)

Sun *et al.* (2013, *BMC Microbiology*) describe the *Shigella flexneri* system, where *"nearly
all variations between serotypes are due to glucosyl and/or O-acetyl modifications of the common
O unit mediated by glycosyltransferases encoded by serotype-converting bacteriophages."*
[DOI](https://doi.org/10.1186/1471-2180-13-39)

From the other direction, Sumrall *et al.* (2021, *J Bacteriol*) deleted a **host**
glycosyltransferase in *Listeria ivanovii*, removing glucose decoration from wall teichoic acid;
the mutant *"became resistant to phage B025 infection due to an inability of the phage to adsorb
to the bacterial surface."* [DOI](https://doi.org/10.1128/JB.00136-21)

> [!important] This block does not fit the two-part rule cleanly, and you should expect that
> The substrate is unambiguously **host** — phage glycosyltransferases modify the host's own
> O-antigen. Part 1 says host.
>
> But the demonstrated consequence is **serotype conversion — changing the phage receptor.**
> That is neither "sustaining host metabolism" nor obviously one of the listed lifecycle steps
> (entry, genome protection, replication, assembly, egress).
>
> **It is arguably a third thing: modifying the host to control who else can infect it.** For a
> lysogen, excluding competitors is a real fitness function.
>
> Three honest options, and the protocol permits all three:
> 1. read receptor modification as a **lifecycle function** (superinfection exclusion, host-range
>    control) → DOES NOT COUNT
> 2. read it as **genuine host modification** — the host's surface chemistry really is changed,
>    persistently, in a lysogen → COUNTS
> 3. **UNRESOLVABLE**, and name the experiment
>
> Whichever you pick, **say in the argument box that the two-part rule underdetermined it.**
> Chunk 4 showed the field's own rules have exactly this problem; being able to say "and so does
> ours, here, and we noticed" is far stronger than hiding it.

**A distinction worth drawing across the nine.** The evidence above concerns the **transfer**
step — glycosyltransferases acting on the surface. The **precursor** enzymes (`galE`, `UGDH`,
`gmd`, `rfbB`, `manB`, `glmS`) make nucleotide sugars feeding *many* pathways, not only the
surface. Whether the same reasoning carries to them is a real question, not a formality: a phage
carrying `galE` may be feeding surface modification, or something else entirely.

**Evidence tier available: 2** for the transfer step. Likely **5–6** for the individual precursor
enzymes unless you find phage-specific work on them.

---

## `glycoside_hydrolase`

**What they do.** Cleave glycosidic bonds. In phage biology that means **endolysins** (degrade
peptidoglycan from inside to lyse the cell at the end of infection), **virion-associated lysins**
(locally degrade the wall during entry), and **tailspike depolymerases** (chew capsule or
O-antigen to reach the receptor).

**Why this family is the protocol's own worked example.** An endolysin acts on a **host**
substrate — the cell wall — so Part 1 says host. But it is unambiguously viral work: it bursts
the cell open to release progeny. That is exactly why the decision rule has two parts.

**The case for HOST / sustains host metabolism:**
Some glycoside hydrolases are genuine sugar-catabolic enzymes. If a phage-encoded one liberated
usable sugars for the host, that would be host metabolic modulation. **I found no phage-specific
evidence for this reading.** That absence is itself the finding — and under default-COUNTS it
still has to be weighed rather than waved away.

**The case for VIRAL / lifecycle step:**
Entry and egress. Both are discrete lifecycle steps.

> [!note] The Chunk 2 lesson applies directly here
> `PF13385` — *"Concanavalin A-like lectin/glucanases superfamily"* — was excluded from this
> family during the accession review because it is a **fold, not an activity**: concanavalin A
> binds sugars, it does not hydrolyse them. That was **99.4%** of the family's original count.
>
> So you are judging the **123 calls that survived that check**, not the 21,690 that didn't.

**Evidence tier available: 1–2** for endolysins and tailspikes; a very well developed field.

---

## `phoH` — phosphate starvation-inducible protein (K06217)

**What it does.** Part of the **Pho regulon** — the bacterial response to phosphate limitation,
which switches on high-affinity phosphate scavenging when phosphate runs short. `phoH` itself is
an ATP-binding protein whose precise function is not fully resolved.

**Phage-specific evidence.** According to PubMed, Goldsmith *et al.* (2011, *Appl Environ
Microbiol*) found Pho regulon genes in **nearly 40% of marine phage genomes but only 4% of
non-marine phage genomes**, with `phoH` the most prevalent — in 42 of 602 complete phage genomes.
Phage `phoH` sequences *"formed a cluster distinct from those of their bacterial hosts"*, and the
gene is now used as a **signature gene for marine phage diversity**.
[DOI](https://doi.org/10.1128/AEM.05531-11)

Huang *et al.* (2021, *Environ Microbiol*) list `phoH` among the seven high-frequency AMGs shared
across roseophages. [DOI](https://doi.org/10.1111/1462-2920.15412)

**The case for HOST / sustains host metabolism:**
This is about as good as the AMG hypothesis gets outside photosynthesis. The marine/non-marine
split — **40% vs 4%** — is a strong ecological signal: phages carry it **where phosphate is
limiting**. That pattern is hard to explain except by phosphate acquisition mattering to the
infected cell.

**The case for VIRAL / lifecycle step:**
Phage genome replication is phosphate-expensive; a burst of a hundred virions is a large
nucleic-acid demand. Boosting phosphate scavenging could serve the phage's own replication rather
than host metabolism generally. Note too the phylogenetic separation — phage `phoH` forms its own
cluster, consistent with specialisation away from the host function.

**Evidence tier available: 4–5.** Strong comparative genomics and a clear ecological correlation;
no experiment isolating what phage `phoH` does during infection. **That missing experiment is
nameable**, which matters if you land on UNRESOLVABLE: delete or express phage `phoH` and measure
phosphate uptake in infected versus uninfected cells under limitation.

---

---

# Batch 3 — the remaining 16

## `dsrC_tusE` — sulfur relay (K11179)

**The reason this family exists in the rubric.** Martin *et al.* single it out not for its
biology but as an **annotation failure**: DsrC and TusE do different jobs, current HMMs cannot
separate them, and **KEGG has merged them into a single orthology group literally named
`tusE, dsrC`**. One accession, two functions.

**What the two proteins actually do.** According to PubMed, Stockdreher *et al.* (2012, *PLoS
One*) work out the sulfur-transfer chemistry in *Allochromatium vinosum* and state the
relationship directly: **TusE is part of a system for tRNA modification** — TusBCD transfers
sulfur to TusE — and TusE is *"a homolog of another crucial component of the A. vinosum Dsr
system, namely DsrC."* DsrC itself is persulfurated at Cys111 and feeds sulfur to the
**dissimilatory sulfite reductase DsrAB**, i.e. energy metabolism.
[DOI](https://doi.org/10.1371/journal.pone.0040785)

So: same fold, same persulfide chemistry, **two entirely different destinations** — tRNA
thiolation versus dissimilatory sulfur oxidation.

**The case for HOST / sustains host metabolism:**
If the phage copy is a genuine `dsrC`, it feeds dissimilatory sulfur oxidation — host energy
metabolism, and exactly the kind of thing claimed in the biogeochemical literature.

**The case for VIRAL / lifecycle step:**
If it is a `tusE`, it feeds tRNA thiolation — a housekeeping modification with no sulfur-cycling
implication whatever. Note this reading doesn't make it *viral* so much as **not what the
catalogue claims it is**.

> [!important] This family is different from all the others, and the distinction matters
> For every other family you are judging **what a phage does with a gene**. Here you are judging
> whether **anyone can tell which gene it is.** Under a merged KEGG orthology, a call of K11179
> carries no information about which of the two functions is present.
>
> That makes it a strong candidate for **UNRESOLVABLE**, and unusually, the resolving experiment
> is easy to name: **phylogenetic or HMM separation of DsrC from TusE**, then re-annotation of
> the calls. Until someone does that, no catalogue can support a sulfur-cycling claim from this
> accession — and *that* is the finding, whichever way you rule.

**Evidence tier available: 2** for the underlying biochemistry; **effectively 0** for
distinguishing which one the environmental calls actually are.

---

## `folate` — `folE`, `folE2`, `folA`, `folB`, `folD` and relatives

**What the pathway does.** Builds tetrahydrofolate, the universal one-carbon carrier. Its
one-carbon units feed purine synthesis, thymidylate synthesis (via thymidylate synthase),
methionine, and formylmethionyl-tRNA for translation initiation.

**The overlap you already know about.** `folE` / GTP cyclohydrolase I is the first committed step
of folate biosynthesis **and** the entry point to queuosine biosynthesis. `folE2` (`K09007`,
GTP cyclohydrolase IB) is an alternative to it and sits at the same branch. Chunk 2 flagged all
four as **AMBIGUOUS** in the accession list precisely for this reason, and Chunk 4 showed the
wastewater rule cannot resolve it either.

**Cross-reference the queuosine dossier above.** Thiaville *et al.* detected a 7-deazaguanine
derivative in phage DNA; the pathway producing it starts at GTP cyclohydrolase I. So a phage
`folE` may be feeding folate, or feeding DNA modification, and the gene does not say which.
[DOI](https://doi.org/10.1073/pnas.1518570113)

**The case for HOST / sustains host metabolism:**
Folate is a genuine cofactor pathway serving the whole cell. A phage supplementing it is
supplementing host one-carbon metabolism, which is host metabolic modulation in the ordinary
sense.

**The case for VIRAL / lifecycle step:**
Martin *et al.*'s argument is that the one-carbon units feed *de novo* nucleotide biosynthesis for
**phage genome replication** — a discrete lifecycle step. The queuosine evidence adds a second
viral route: genome modification.

> [!caution] This is the 18-percentage-point family
> Wastewater moves **19.5% → 37.7%** on whether `folE`/`queD` count. Whatever you decide here,
> the write-up reports the answer **both ways**. Take your time and make the argument box good —
> this is the paragraph a reviewer will read hardest.

**Evidence tier available: 2** (for the chemistry and the phage-DNA detection); **6** for the
specific question of what a phage `folE` is doing, unless you find better.

---

## `nrdH` — glutaredoxin-like protein, ribonucleotide reductase system

**What it does.** `nrdH` is the redox partner of class Ib ribonucleotide reductase (RNR). RNR
converts ribonucleotides to deoxyribonucleotides — the committed, rate-limiting step of making
DNA precursors from RNA precursors.

**Phage-specific evidence, and it is indirect but telling.** PubMed returns **130 results** for
bacteriophage ribonucleotide reductase — phage-encoded RNRs are common and well studied.

More pointedly, Sakowski *et al.* (2021, *Nature Microbiology*) built a method for capturing
virus–host interactions in situ that *"fuses a **phage marker, the ribonucleotide reductase
gene**, with the host 16S rRNA gene of infected bacterial cells."*
[DOI](https://doi.org/10.1038/s41564-021-00873-4)

**RNR is used as a marker gene for phage.** That is the same status `phoH` has, and it means
phage RNR sequences are distinct enough from host ones to identify a virus. Whatever else that
implies, it is not the signature of a gene the phage picked up incidentally.

Huang *et al.* (2021) also list RNR among the seven high-frequency roseophage AMGs, all of which
they describe as *"involved in the nucleotide biosynthesis pathway."*
[DOI](https://doi.org/10.1111/1462-2920.15412)

**The case for HOST / sustains host metabolism:**
RNR supplies the dNTP pool the whole cell uses. Boosting it raises host biosynthetic capacity.

**The case for VIRAL / lifecycle step:**
The dNTPs are consumed replicating the phage genome. A phage encoding its own RNR is the textbook
example of a virus provisioning **its own** replication rather than the host's, and the fact that
phage RNRs are phylogenetically distinct enough to serve as viral marker genes supports
specialisation for that role.

**Evidence tier available: 4–5.** Abundant comparative genomics; no experiment separating "the
host's dNTP pool" from "the phage's dNTP pool" during infection, because during infection they
are the same pool. **That may be genuinely unresolvable** — and if you say so, that is the
experiment problem to name.

---

## `IMPDH` — IMP dehydrogenase (K00088)

**What it does.** Catalyses the rate-limiting, committed step of **guanine nucleotide**
biosynthesis: IMP → XMP, en route to GMP, GDP, GTP, dGTP.

Same structural argument as `nrdH` and `dut` — it is a nucleotide-supply enzyme, and during
infection the nucleotide pool being drawn down is the one replicating the phage genome. Note that
IMPDH sits in KEGG's **09104 Nucleotide metabolism**, which is the category the wastewater paper's
own rule excludes (Chunk 4).

**No phage-specific functional study surfaced** in the searches run. Treat as **Tier 6** unless
you find otherwise: the argument available is from the chemistry, and **Tier 6 alone cannot rule
a family out**, so the protocol's default applies.

---

## `speD` — S-adenosylmethionine decarboxylase

**What it does.** Decarboxylates SAM to provide the aminopropyl donor for **spermidine**
synthesis. Polyamines are polycations that bind nucleic acids and are required for normal growth.

**Why this one is more interesting than it looks.** Polyamines have a long-standing association
with phage biology — PubMed returns work on phage and polyamines going back to the 1970s.
Spermidine is a structural component of some phage virions, where its positive charge helps
neutralise the packaged genome's phosphate backbone.

**The case for HOST / sustains host metabolism:**
Polyamine synthesis is general host metabolism affecting growth, translation and stress response.

**The case for VIRAL / lifecycle step:**
If spermidine is being made to **condense and neutralise the phage genome during packaging**,
that is assembly — a discrete lifecycle step, and directly parallel to the terminase argument.

**Evidence tier available: 5–6** for the environmental calls. The polyamine-in-virion literature
is real but old and organism-specific; check whether it applies to the phages in these
catalogues before leaning on it.

---

## The eleven with no phage-specific literature

`asnB` · `cgeB` · `hisF` · `HMGCL` · `iscU` · `K07336` · `NAMPT` · `nodU` · `P4HA` · `raxST` ·
`TALDO1`

I searched for phage-specific functional work on each and **found none**. That is not laziness on
the searching and it is not a gap to apologise for — **it is the single most consequential result
in this dossier**, so it is stated plainly rather than buried.

| Family | What the enzyme does | Where it sits |
|---|---|---|
| `asnB` | asparagine synthase (glutamine-hydrolysing) | amino acid metabolism |
| `cgeB` | spore maturation protein | sporulation, cell surface |
| `hisF` | imidazole glycerol phosphate synthase | histidine biosynthesis |
| `HMGCL` | hydroxymethylglutaryl-CoA lyase | ketone body / leucine catabolism |
| `iscU` | Fe-S cluster scaffold | iron–sulfur cluster assembly |
| `K07336` | PKHD-type hydroxylase | uncharacterised 2OG-Fe(II) oxygenase |
| `NAMPT` | nicotinamide phosphoribosyltransferase | NAD salvage |
| `nodU` | carbamoyltransferase | nodulation factor / surface modification |
| `P4HA` | prolyl 4-hydroxylase | collagen-type hydroxylation, 2OG-dependent |
| `raxST` | sulfotransferase | sulfation, surface/signal molecules |
| `TALDO1` | transaldolase | pentose phosphate pathway |

**What the protocol says happens to these.** Only Tier 6 evidence is available — reasoning from
the chemistry. The protocol is explicit that **Tier 6 alone can never move a family out of the
record**. So unless you find literature I missed, every one of these **defaults to COUNTS**.

> [!important] This is a result, and it should go in the paper
> Eleven of 35 families — roughly a third — have **no phage-specific functional evidence at all**.
> Not weak evidence. None.
>
> The field is making claims about viral modulation of host metabolism from gene families where
> nobody has ever tested what the phage-encoded copy does. That finding does not depend on any
> verdict you reach, and it is arguably more robust than the disputed-share number itself,
> because it needs no rubric.
>
> It also connects to the protocol's stated falsification condition: *"nearly everything comes
> out UNRESOLVABLE → the evidence base is too thin for the question, and the honest finding is
> that the AMG record cannot currently be adjudicated."* Watch whether that is where this lands.

**Do still check them yourself.** My searches were systematic but not exhaustive, and a negative
search result is weaker than a positive one. If you find something for any of these, it changes
that family's tier and possibly its verdict — and it makes the "eleven with nothing" claim
stronger, because it will have survived a second search.

---

# All 35 families now have a dossier

**Complete.** Every citation was retrieved from PubMed and its abstract read before being quoted.

**The headline from the gathering, before you judge anything:**

| | families |
|---|---|
| Strong phage-specific evidence (Tier 1–2) | `psbA` `psbD` `dcm` `queuosine` `glycosyltransferase` `glycoside_hydrolase` `xtmA` `xtmB` `dsrC_tusE` |
| Good comparative/ecological evidence (Tier 4–5) | `phoH` `nrdH` `dut` |
| Chemistry only (Tier 6) — **defaults to COUNTS** | the 11 above, plus `IMPDH`, `speD`, and most nucleotide-sugar precursors |

**Roughly a third of the families have no phage-specific functional evidence whatsoever.**

## Related

- [[Adjudication Worksheet]] — where the verdicts go
- [[How To Adjudicate]] — the mechanics
- [[Adjudication Protocol]] — the rules
