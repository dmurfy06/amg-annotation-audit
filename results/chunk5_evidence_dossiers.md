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

**Status: 18 of 35 complete.** Doing these properly takes real searching; the rest follow in
later batches. Order is alphabetical within each batch, per the protocol.

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

## Still to do — 17 families

`asnB` · `cgeB` · `dsrC_tusE` · `folate` · `hisF` · `HMGCL` · `IMPDH` · `iscU` · `K07336` ·
`NAMPT` · `nodU` · `nrdH` · `P4HA` · `raxST` · `speD` · `TALDO1`

Mostly single enzymes with little obvious phage literature, plus `folate` and `dsrC_tusE`, which
are disputed families and will get full treatment.

## Related

- [[Adjudication Worksheet]] — where the verdicts go
- [[How To Adjudicate]] — the mechanics
- [[Adjudication Protocol]] — the rules
