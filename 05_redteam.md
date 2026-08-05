# 05 — Red Team: R4, viral auxiliary metabolic genes

**Phase 5 of 7.** 2026-08-05. The job here is to argue against R4 as a hostile reviewer would,
and to attack **with data** wherever the attack is testable rather than merely stating a worry.
Attacks that fail are as informative as attacks that land.

**Summary: 3 attacks fail on evidence, 3 land, 1 is a standing risk.** None is fatal. Two
change the design.

---

## ATTACK 1 — "Your suspect calls are just low-confidence junk the field already ignores."

*The reviewer's version:* DRAM-v assigns an `auxiliary_score`. If `dcm` calls sit in the weak
tiers, you have discovered that low-confidence calls are low-confidence.

**FAILS.** `dcm` is distributed almost evenly across every confidence tier:

| auxiliary_score | all calls | dcm | dcm share |
|---|---|---|---|
| 1 (highest) | 12,628 | 721 | 5.7% |
| 2 | 42,348 | 2,900 | 6.8% |
| 3 | 33,747 | 2,176 | 6.4% |

There is no tier where `dcm` is rare. It cannot be dismissed as weak calls.

**But one caveat survives and must be carried.** The `amg_flags` field shows 3,941 of 5,797
`dcm` calls flagged `MF` and 1,854 flagged `M`. If `F` denotes proximity to a contig end — a
standard reliability warning — then ~68% of `dcm` calls carry it. ❓ **DRAM-v's flag semantics
must be confirmed from its documentation, not assumed.** If `F` does mean what it appears to,
this is a genuine limitation of the underlying calls and belongs in the results, not hidden.

---

## ATTACK 2 — "Your 'curation makes it worse' claim compares two incomparable sets."

*The reviewer's version:* the permissive and conservative catalogues may be built differently.
If the conservative set is not a subset, the retention comparison is meaningless.

**LARGELY FAILS.** Of 86,914 unique conservative gene identifiers, **86,913 appear in the
permissive set.** One does not. It is effectively a strict subset and the comparison is
like-for-like.

> [!note] My own automated check was wrong, and that is worth recording
> The script tested subset-hood as a binary and printed **"NOT a subset: the trend claim is
> UNSAFE"** on the strength of that single discrepant record out of 86,914. Reported verbatim,
> that would have been a false alarm — an over-strict test producing a confident wrong verdict.
>
> **A binary test on messy data needs a tolerance, and any automated verdict needs eyes on the
> magnitude before it is believed.** Same family of error as the 83-fold artefact, opposite
> direction.

The retention finding therefore stands: **`dcm` retained at 68%, all calls retained at 36%** —
`dcm` survives curation at nearly twice the overall rate.

**A smaller real problem found on the way:** 88,729 rows but 86,914 unique gene identifiers, so
~1,800 rows are duplicates. Trivial to handle, but it must be handled explicitly.

---

## ATTACK 3 — "Nobody actually claims anything about these genes. You're auditing a footnote."

*The reviewer's version, and the sharpest one:* if `dcm` and queuosine genes merely sit in
supplementary tables and no one draws conclusions from them, reclassifying them changes nothing.

**FAILS — and the counter-example is concrete.** *Potential Auxiliary Metabolic Capabilities and
Activities Reveal Biochemical Impacts of Viruses in Municipal Wastewater Treatment Plants*
(*Environmental Science & Technology*,
[doi:10.1021/acs.est.2c07800](https://doi.org/10.1021/acs.est.2c07800)) reports that
**queuosine biosynthesis genes (`folE`, `queD`, `queE`) are the most common viral AMGs** in
those systems ⚠️ — presented as biochemical impacts of viruses on the environment.

That is exactly the interpretation Martin *et al.* argue against: they hold that queuosine genes
are more likely modifying the **viral** chromosome to evade host defences, i.e. an essential
viral function, not host metabolic modulation.

**Published claims do rest on these categories.** The audit has a target.

Supporting point for `dcm`: the phage literature treats phage-encoded DNA methyltransferases as
**epigenetic / anti-restriction and host-tropism** machinery ⚠️ — a replication strategy, not
metabolism. Counting `dcm` as a *metabolic* gene looks like a category error on the field's own
evidence, which strengthens the mechanistic (not merely definitional) case.

---

## ATTACK 4 — "This is one dataset. You have critiqued one paper, not a field." → **LANDS**

The entire result rests on a single ocean catalogue. If the pattern is specific to that
pipeline, the finding is a comment on one publication.

**Design change, mandatory.** At least one further independent catalogue — a different
environment (soil, gut, wastewater) and ideally a VIBRANT-based rather than DRAM-v-based
survey, so the result is not an artefact of one tool. The ES&T wastewater paper above is an
obvious second target, since it already headlines a suspect category.

---

## ATTACK 5 — "This is definitional. You picked a rubric and applied it." → **LANDS, manageable**

True and unavoidable in part: "what counts as an AMG" is partly an argument. A hostile reviewer
can say the 25% figure measures the consequence of one group's opinion.

**Three defences, in order of strength:**
1. **Pre-register Martin *et al.*'s criteria as the rubric**, unchanged, and say so. The claim
   becomes "here is what follows if the field adopts the position published in *Nature
   Microbiology*" — a legitimate and falsifiable statement.
2. **For the two genes that dominate the result, the argument is mechanistic, not definitional.**
   Anti-restriction methylation and viral chromosome modification are established phage biology.
3. **Report the answer under both rubrics** — inclusive and strict — rather than picking one.
   The gap between them *is* a result.

---

## ATTACK 6 — "The headline number took an afternoon. Rule 3 says that is a figure." → **LANDS**

Honest: the 25.1% was obtained in a single sitting. This project's own standing rule says that
makes it a figure, and the project must be the question the figure raises.

**What legitimately fills 8–12 weeks:**
- Extending to ≥2 further catalogues across environments and tools (Attack 4)
- **The adjudication** — going gene family by gene family through the suspect categories and
  arguing from biochemistry whether each is plausibly auxiliary or essential-viral. This is the
  scientific core and no script can do it
- Abundance weighting: a call is not an organism. Per-sample abundance changes the picture
- Testing whether excluding suspect categories changes any **published conclusion** — the
  ES&T "most common AMG" claim is the first test case
- Confirming DRAM-v flag semantics and handling duplicates properly

**Risk if not done:** the project becomes a well-executed short report rather than a study.
Acceptable as an undergraduate output, but it should be planned as the larger thing.

---

## ATTACK 7 — "Martin *et al.* will do this themselves." → **STANDING RISK, unresolvable**

Their Perspective is roughly a year old, they have the field's attention, and they are the
obvious people to run the measurement. Nothing can remove this risk.

**Mitigations:** work in a narrow lane they did not claim (the *curation-enriches-suspects*
finding is not in their paper and is not obvious); publish the analysis openly as it develops;
accept that being scooped on a first undergraduate project is survivable and the skills are not.

---

## Verdict

**R4 survives the red team.** The three attacks that would have been fatal — low-confidence
artefact, incomparable datasets, nobody cares — all fail on evidence. The three that land change
the design rather than the question:

1. Add ≥2 independent catalogues
2. Pre-register the rubric and report both inclusive and strict versions
3. Plan the adjudication as the substance, not the enumeration

**Compared with E1**, R4 has a published framing paper, no equivalent of E1's fatal-ish
"the metal was assigned from what was purified" problem, a larger and better-structured dataset,
and a demonstrated target in the published literature. It should proceed to Phase 4
(feasibility) and Phase 6 (pre-registered plan).

## ATTACK 8 — "Your suspect calls are contig-edge artefacts." → **TESTED, FAILS**

*Added 2026-08-05 after Chunk 1. Raised internally, not by a reviewer — 68% of `dcm` calls carry
DRAM-v's `F` flag, and `F` turns out to mean "within 5,000 bp of a contig end".*

Genes near a contig end have the weakest evidence of viral provenance, so if the disputed
categories were concentrated there, the 25.1% result would be explained away as assembly noise.

**It fails, and it fails in the opposite direction.** Against a baseline nobody had computed:

| Stratum | n | % `F`-flagged |
|---|---|---|
| All AMG calls | 88,729 | 79.1% [78.9–79.4] |
| KO-assigned calls | 31,772 | **75.8%** [75.3–76.3] |
| `dcm` | 5,797 | **68.0%** [66.8–69.2] |
| All suspect categories | 7,969 | 69.9% [68.8–70.9] |

`dcm` sits at contig edges **less** than the average call — non-overlapping intervals, ratio
0.92×. Contig position cannot explain the disputed share in either direction. A confounder
measured and eliminated. Full working: `07_flag_semantics.md`.

**What the check did find** is a limitation of the record rather than a defence of it: 79.1% of
the curated catalogue is within 5 kb of a contig end, rising from 62.8% pre-curation. Declared
in the paper's limitations, not used as evidence.

## Provenance

| Date | Check | Method | Result |
|---|---|---|---|
| 2026-08-05 | dcm confidence distribution | `GlobalAMGs_SOM.xlsx`, Table S5 | even across all tiers — attack fails |
| 2026-08-05 | conservative ⊂ permissive | gene-id set comparison | 86,913/86,914 — attack fails |
| 2026-08-05 | do papers claim these genes? | WebSearch → ES&T wastewater study | queuosine = "most common AMG" — attack fails |
| 2026-08-05 | contig-edge confounder (`F` flag) | `dramv_flag_semantics.py`, Wilson CIs | 68.0% vs 75.8% baseline — attack fails |
