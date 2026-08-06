# 10 — Each catalogue against its own stated criteria (Chunk 4)

**Run 2026-08-05.** Script: `chunk4_own_criteria.py` · Output: `results/chunk4_own_criteria.txt`
Paper texts: `refs/microbiome_2024_ocean_amg.txt`, `refs/isme_2022_soil_amg.txt`,
`refs/est_2023_wastewater_amg.txt`.

**Martin *et al.* are not used anywhere in this analysis.** That is the point of it.

---

## Why this was supposed to be the primary analysis

Every other form of the argument can be dismissed as definitional — *"you picked a rubric and
applied it."* Testing a paper against **its own methods section**, using **its own annotation
database**, removes that objection entirely. It stops being anyone's opinion and becomes an
internal inconsistency.

For that to be worth anything, the test has to be able to come out either way. **It does — and
it did.**

## The three rules, quoted from their own methods

| Catalogue | Stated rule | Testable mechanically? |
|---|---|---|
| **Ocean**, *Microbiome* 2024 | *"AMGs were excluded if they were found on contigs carrying genes encoding transposons, lipopolysaccharide islands (**glycosyltransferase**, nucleotidyl transferase, carbohydrate kinases, and nucleotide sugar epimerase), endonucleases, integrases, or plasmid stability genes."* | **Yes** |
| **Wastewater**, *ES&T* 2023 | *"Metabolic genes directly involved in viral replication (e.g., replication, repair, **nucleotide transport, and metabolism**) were not included in vAMGs."* | **Yes**, via KEGG |
| **Soil**, *ISME J* 2022 | *"Proteins involved in **nutrient transformation and pollutant degradation** were defined as auxiliary metabolic genes."* | **No** — ordinary English |

---

## Result 1 — the ocean catalogue applies its rule. Almost perfectly.

| | permissive | conservative | |
|---|---|---|---|
| glycosyltransferase calls | 30,483 | **2** | 99.993% removed |
| transposon-flagged calls | 762 | **0** | removed entirely |
| auxiliary score | ≤3 | ≤3 | respected |

**This is a negative result for H4, and it is the most important thing in the chunk.** It proves
the test discriminates. Had every catalogue "violated its own criteria", the obvious reading
would be that the test was rigged. It is not: a paper that states a mechanical rule can enforce
it, and this one did.

It also retires an earlier worry: the ocean catalogue's near-total absence of glycosyltransferases
is not a namespace artefact. **It is the authors deliberately excluding them, exactly as their
methods say.**

## Result 2 — the wastewater rule cannot be applied at all

| | calls | share of KO-assigned |
|---|---|---|
| In a KEGG category their rule excludes | 10 | 13.0% [7.2–22.3] |
| **Exclusively so — a clean violation** | **0** | **0.0% [0.0–4.8]** |

Both offending KOs are **dual-classified by KEGG**:

| KO | Gene | KEGG categories |
|---|---|---|
| `K01939` (8 calls) | adenylosuccinate synthase, `purA` | **09104 Nucleotide metabolism** · 09105 Amino acid metabolism |
| `K00948` (2 calls) | ribose-phosphate pyrophosphokinase, `prsA` | 09101 Carbohydrate metabolism · **09104 Nucleotide metabolism** |

> [!warning] The headline did not survive contact with the data, and it should not have
> "13% of their calls violate their own stated rule" was the number this chunk was expected to
> produce. It is arithmetically true and **substantively misleading**.
>
> Every one of those genes also sits in a category the rule *permits*. The authors could read
> `purA` as amino acid metabolism and `prsA` as carbohydrate metabolism — and they do exactly
> that, presenting `prsA` in the abstract as a **carbon** metabolism gene. **Zero calls are
> exclusively in an excluded category.**
>
> Fourth artefact caught by Rule 5, and the first one caught *before* it reached Daniel.

### What survives is better than the gotcha

**The wastewater paper's stated exclusion criterion cannot be applied deterministically.** Using
the authors' own annotation database, the same gene can satisfy and violate their rule at once,
depending on which of KEGG's categories you read.

A rule that does not decide is not being *enforced*. It is being **interpreted, case by case,
invisibly** — and no reader can reconstruct which reading was used for which gene.

That is a finding about the state of AMG methodology, not an accusation about these authors. It
is also more durable: it cannot be rebutted by saying "we meant the other category", because
that rebuttal *is* the finding.

## Result 3 — soil is not testable without our judgement, so it is not tested

Their definition is *"nutrient transformation and pollutant degradation"*. Their catalogue is
**27.0%** glycosyltransferases [25.7–28.3] — Glycosyl transferases group 1, cell-surface
polysaccharide biosynthesis.

Deciding whether that counts as "nutrient transformation" is a biochemical judgement, and it is
**ours**. Claiming it as an internal inconsistency would smuggle back exactly the definitional
objection this chunk exists to avoid. It goes to the Chunk 5 adjudication like any other question.

---

## The pre-registered expectation failed

**H4 predicted the queuosine genes would be the violation** — the authors themselves note those
genes *"could also participate in tRNA biogenesis"*, and they headline them as the most common
vAMGs.

**They do not trip the test.** KEGG files queuosine biosynthesis under **folate biosynthesis
(09108, cofactors and vitamins)**, not nucleotide metabolism. Under the authors' own annotation
database, queuosine genes are cofactor metabolism and pass their filter cleanly.

This is recorded as a failed prediction, not quietly dropped. It also sharpens the real question:
**the dispute over queuosine is not about whether a rule was broken — it is about whether KEGG's
placement of that pathway is biologically the right one.** That is squarely Chunk 5.

## Consequences

- **H4 is not supported in the form it was written.** No catalogue tested here demonstrably
  breaks its own mechanical rule. Report it that way.
- **The replacement claim is stronger and is what the paper should argue**: of three catalogues,
  one states an enforceable rule and enforces it, one states a rule that cannot be enforced, and
  one states no testable rule at all. **AMG inclusion criteria are mostly not the kind of thing
  that can be checked** — which is precisely why the record drifts.
- The `05_redteam.md` "definitional" attack is now answered in a new way: not *"the papers break
  their own rules"* but *"the rules mostly cannot be broken, because they do not decide anything."*
- Every quotation above is from the papers' own methods, with the text files in `refs/`.
