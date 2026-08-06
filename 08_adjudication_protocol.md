# 08 — Adjudication Protocol (Chunk 3)

**Written 2026-08-05, before any gene family has been adjudicated.**
This document fixes the rules for Chunk 5 — the scientific core of the project — *before* the
biochemistry is read. Once published it is append-only: see [Amendments](#amendments).

---

## Why this document exists, stated honestly

`06_project_brief.md` pre-registered H1 for "catalogues two and three, which have not been
examined." **They were examined the same day.** Wastewater (19.8%) and soil (29.8%) are both
measured. So the H1 pre-registration is spent, and **all three catalogue measurements are
exploratory**. They will be reported as such. Freezing the gene-family rubric now would be
closing a door that is already open.

**What is genuinely unspent is the adjudication.** Not one gene family has been judged. That is
where bias would actually bite: the verdicts will be reached by one undergraduate, unblinded to
the fact that `dcm` alone is 5,797 calls and that ruling it "does not count" moves the headline
number more than every other decision combined.

This protocol exists to make those verdicts something other than a preference.

> [!important] The protocol is deliberately biased **against** this project's own hypothesis
> The default verdict is **COUNTS** — current field practice. A family only leaves the AMG
> record if positive evidence pushes it out. Ambiguity therefore *protects* the field's numbers
> and *shrinks* the disputed share.
>
> This is the right direction. A project arguing the record is inflated should make deflating
> it hard. If the disputed share survives a protocol built to suppress it, the finding is real.

---

## The question being adjudicated

For each gene family, the question is **not** "is this gene essential to the virus?" — nearly
everything a phage carries is ultimately for the virus, so that test rules out everything and
decides nothing.

The question is the one the field's own claim rests on:

> **Does a phage carrying this gene support the claim that the virus modulates its host's
> metabolism?**

## The decision rule — two parts, both must point the same way

**Part 1 — SUBSTRATE.** Does the gene product act on a **host** molecule, structure or pathway,
or on a **viral** one?

**Part 2 — CONSEQUENCE.** Does the action **sustain or redirect host metabolism during
infection**, or does it serve a **discrete step of the viral lifecycle** — entry, genome
protection, replication, assembly, or egress?

**A family counts as an AMG only if Part 1 = host AND Part 2 = host metabolism.**

Worked examples of the rule's behaviour, stated now so it cannot be bent later:

| Family | Part 1 substrate | Part 2 consequence | Verdict under this rule |
|---|---|---|---|
| `psbA` — photosystem II D1 | host (host thylakoid) | sustains host photosynthesis during infection | **COUNTS** |
| `dcm` — DNA methyltransferase | viral (own genome) | genome protection | does not count |
| endolysin | host (cell wall) | egress — a discrete lifecycle step | does not count |
| tail-fibre glycoside hydrolase | host (cell wall) | entry — a discrete lifecycle step | does not count |
| folate / one-carbon | viral (own nucleotide pool) | replication | does not count |

The endolysin row is the important one. It shows why Part 1 alone is not enough: a gene can act
on a host substrate and still be doing plainly viral work. Any rule that cannot separate an
endolysin from `psbA` has failed to capture the distinction the field itself draws.

---

## Evidence hierarchy

Verdicts cite the **highest tier of evidence available**, and the tier is recorded with the
verdict. Lower tiers cannot overturn a higher one; they can only decide a family where no higher
tier exists.

| Tier | Evidence | Weight |
|---|---|---|
| **1** | Experiment in a phage context — knockout, complementation, or direct measurement of host metabolism during infection | decisive |
| **2** | Biochemical or structural characterisation of the **phage-encoded** protein itself (purified enzyme's actual substrate; cryo-EM placing it in a virion) | strong |
| **3** | Expression timing across the infection cycle (early / middle / late) | moderate |
| **4** | Genomic context — consistent linkage to structural, replication or defence modules across phage genomes | moderate |
| **5** | Sequence divergence from host homologues indicating viral specialisation | weak |
| **6** | Mechanistic inference from the enzyme's known chemistry alone | weakest — this is mostly what Martin *et al.* offer |

> [!warning] Tier 6 alone can never move a family out of the record
> A family may only be ruled **DOES NOT COUNT** on Tier 6 evidence if no Tier 1–5 evidence
> exists for it *and* the verdict is additionally recorded as **low-confidence**. Martin *et
> al.*'s Perspective is largely Tier 6 argument. Adopting their conclusions without independent
> evidence would make this project a restatement of theirs, not a test of it.

---

## Verdicts

Exactly one of three, per family:

**COUNTS** — Part 1 and Part 2 both indicate host metabolic modulation. Also the **default**
where evidence is absent or balanced.

**DOES NOT COUNT** — positive evidence at Tier 1–5 that the substrate or the consequence is
viral. Requires a named, cited piece of evidence. "It seems obvious" is not a verdict.

**UNRESOLVABLE** — genuinely undecidable on current evidence.

### The guard on UNRESOLVABLE

"Unresolvable" is the obvious escape hatch for a family whose answer is inconvenient. So:

> Every UNRESOLVABLE verdict **must name the specific experiment or observation that would
> resolve it.** If the missing evidence cannot be named, the family is not unresolvable — it is
> unresearched, and the verdict defaults to **COUNTS**.

This makes each unresolvable falsifiable and turns the unresolvable set into a research agenda
rather than a shrug. It is also the most citable part of the output.

---

## Procedure — how verdicts are actually reached

1. **Adjudicate blind to call counts.** The family list is worked in a pre-set order (below).
   Call counts are *not* consulted while judging. Verdicts are joined to counts only after every
   family is closed. `dcm` and queuosine counts are already known and cannot be unknown — those
   are handled by the seen/unseen split below.
2. **Fixed order: alphabetical by gene-family label.** Not by abundance, not by interest. This
   prevents the high-impact families being decided first and setting an anchor.
3. **One family, one written record**, before moving on. Each entry carries: the two-part
   determination, the evidence tier, the citations, the verdict, the confidence, and — where
   unresolvable — the resolving experiment.
4. **No revisiting a closed verdict after seeing its call count.** If a verdict must change,
   it is amended openly with a date and a reason (see Amendments), never silently.
5. **Verdicts are recorded before any figure is drawn.**

### Seen vs unseen families — declared, not hidden

`dcm`, the queuosine genes, glycoside hydrolases, folate genes and `dsrC`/`tusE` were named by
Martin *et al.* and their call counts are already known. Their verdicts are therefore
**protocol-guided but not blind**, and will be labelled so in the output.

Every other family enters blind. The paper reports the disputed share **twice**: once over all
families, once over blind-only families. If the two differ materially, that difference is itself
reported — it is a measurement of how much knowing the counts changed the answer.

---

## Controls — the protocol must be shown to work in both directions

A protocol that rules everything "does not count" is worthless. Controls are adjudicated
**inside the normal alphabetical run, unlabelled**, and checked only at the end.

**Positive controls** — families the field treats as canonical, experimentally supported AMGs,
chosen because Tier 1 evidence exists and they are not disputed by Martin *et al.* `psbA` and
`psbD` (photosystem II core proteins in cyanophages) are the anchor cases. **These must come out
COUNTS.** If the protocol rules `psbA` out of the AMG record, the protocol is broken and must be
revised and re-run before any real verdict is used.

**Negative controls** — families present in an AMG database whose viral-lifecycle role is
uncontested. **These must come out DOES NOT COUNT.**

**Failure of any control invalidates the run.** Say so in the paper either way.

---

## Which families get adjudicated

Fixed now, so the list cannot be trimmed to taste later. A family is included if it meets **any**
of:

1. It accounts for **≥1% of KO-assigned AMG calls** in any of the three catalogues; **or**
2. It is **named by Martin *et al.* (2025)**; **or**
3. It is designated a positive or negative **control**.

Expected size ~15–25 families. The list is generated by script from the harmonised catalogues
(Chunk 2) and **frozen before adjudication begins** — a family cannot be added or dropped
afterwards. Families falling below threshold are counted in aggregate as "not adjudicated" and
their share of the record is reported, so the unexamined remainder is visible.

---

## Analyses committed to in advance

The disputed share is reported under **four** rules, always together, never one alone:

| Rule | Treatment of verdicts |
|---|---|
| **Inclusive** | current field practice — nothing excluded |
| **Strict** | DOES NOT COUNT excluded; UNRESOLVABLE retained |
| **Maximally strict** | DOES NOT COUNT *and* UNRESOLVABLE excluded |
| **Confidence-limited** | only high-confidence DOES NOT COUNT excluded |

The spread between them is a headline result, not a footnote. Every proportion carries a
binomial (Wilson) confidence interval. Where per-sample abundance exists, both call-weighted and
abundance-weighted versions are reported.

## What would falsify this protocol

Stated in advance, so it cannot be explained away:

- **A control fails.** Protocol broken; revise and re-run.
- **Nearly everything comes out UNRESOLVABLE.** The evidence base is too thin for the question,
  and the honest finding is that the AMG record cannot currently be adjudicated at all — which
  is publishable and is *also* a criticism of the field.
- **Nearly everything comes out COUNTS.** The field's practice is sound, Martin *et al.*'s
  concern is quantitatively minor, and that is the result. Written up as such.
- **Blind and non-blind families give materially different disputed shares.** Knowing the counts
  influenced the verdicts; the non-blind verdicts are then reported as unreliable.

## Amendments

This file is **append-only** once published. Any change is added below with a date, the reason,
and what it replaces. The original text is never edited or deleted. A protocol that can be
quietly rewritten is not a protocol.

---

### Amendment 1 — 2026-08-05. Family membership is defined by accession, not by text matching.

**Approved by Daniel 2026-08-05. Committed before the affected numbers were recomputed.**

**What this replaces.** Nothing in the *rubric*: the six gene families are unchanged, and no
family is added or removed. What changes is **how a call is determined to belong to one** —
previously by regular expressions over free-text gene descriptions, now by membership of an
explicit list of KEGG KO and Pfam accessions.

**Why.** Chunk 2 (`09_chunk2_harmonisation.md`) showed free-text matching failing three
different ways in a single sitting, each silently:

| Failure | Example | Effect |
|---|---|---|
| **Over-match** | bare `GT\d+`/`GH\d+` against the CAZy column caught "NAD dependent epimerase/dehydratase" | inflated soil to 47.5% |
| **Under-match** | Pfam writes `Glycosyl transferases group 1` and `methylase`; the rubric looked for `glycosyltransferase` and `methyltransferase` | soil 3.4% against a true 30.3%; `dcm` found 0 of 5,277 |
| **Cross-family leakage** | `pterin` in a folate pattern caught `queD`, a queuosine gene | thousands of calls attributed to the wrong family |

None of these raise an error. A regex that matches nothing looks exactly like a category that
is genuinely absent.

**Why accessions fix it.** `K00558` and `PF00145` are stable, unambiguous, and mean the same
thing in every catalogue and every paper. They cannot be misspelled, cannot leak between
categories, and — decisively — **a reviewer can check the entire membership list by reading it**,
without running any code. That is not possible for a regex applied to 349,171 rows.

**Procedure, fixed now.**

1. A candidate accession list is generated **by script** from the observed data and written to
   `data/family_accessions.tsv`, with every accession carrying its official KEGG/Pfam
   description and the number of calls it accounts for in each catalogue.
2. The list is **reviewed accession by accession** and frozen before any disputed share is
   recomputed. Generation is mechanical; inclusion is a judgement, and it is recorded as one.
3. Any accession whose family assignment is genuinely ambiguous is marked **`AMBIGUOUS`** rather
   than being forced into one family. The headline is then reported **both** with and without the
   ambiguous set, and the gap between the two is a declared result.
4. Accessions may **not** be added or removed after the disputed share has been recomputed. A
   later change requires a further amendment here.

**The known ambiguous case, named in advance.** `folE` / GTP cyclohydrolase I (KEGG `K01495`,
Pfam `PF01227`) is the first committed step of **both** folate and queuosine biosynthesis. The
*ES&T* wastewater paper counts it as a queuosine gene. Under text matching it was silently
counted as folate in Pfam and as nothing at all in KEGG. It is marked `AMBIGUOUS` and its effect
is reported separately. The same applies to `queD` / 6-pyruvoyl tetrahydropterin synthase.

**What this does not do.** It does not decide whether a family *counts* as an AMG — that remains
the Chunk 5 adjudication, governed by the two-part rule above and unchanged. This amendment only
fixes which calls belong to which family, so that the adjudication's verdicts can be applied to
a defined set rather than to whatever a regex happened to catch.

**Direction of effect, declared.** Correcting the under-match **raises** the disputed share,
which favours this project's own hypothesis. That is precisely why the defect, the correction,
and both sets of numbers are reported together — see `09_chunk2_harmonisation.md`.
