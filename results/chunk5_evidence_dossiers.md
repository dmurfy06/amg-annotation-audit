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

**Status: 7 of 35 complete.** Doing these properly takes real searching; the rest follow in
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

## Still to do — 28 families

`asnB` · `cgeB` · `dsrC_tusE` · `folate` · `galE` · `glmS` · `glycoside_hydrolase` ·
`glycosyltransferase` · `gmd` · `hisF` · `HMGCL` · `IMPDH` · `iscU` · `K07336` · `manB` ·
`NAMPT` · `nodU` · `nrdH` · `P4HA` · `phoH` · `pseB` · `raxST` · `rfbB` · `rfbC` · `speD` ·
`tagD` · `TALDO1` · `UGDH`

The ~10 nucleotide-sugar and cell-surface families (`galE`, `gmd`, `manB`, `rfbB`, `rfbC`,
`UGDH`, `pseB`, `glmS`, `tagD`) share a literature and will be done as one batch with individual
sections, which is why they aren't done yet — doing them singly would duplicate a lot of reading.

## Related

- [[Adjudication Worksheet]] — where the verdicts go
- [[How To Adjudicate]] — the mechanics
- [[Adjudication Protocol]] — the rules
