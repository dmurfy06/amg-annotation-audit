# 07 — DRAM-v flag semantics (Chunk 1)

**Run 2026-08-05.** Closes the standing "do not guess what `F` means" item.
Script: `scripts/dramv_flag_semantics.py` · Output: `results/chunk1_flag_semantics_output.txt`

**Source provenance.** Every line number below refers to source **pinned to a specific commit**,
so the citations cannot drift when either project next commits:

| Project | Commit | Licence |
|---|---|---|
| `WrightonLabCSU/DRAM` | `fe61d759303f30db058d5d505c448b28e41b03f1` | GPL-3.0 |
| `AnantharamanLab/VIBRANT` | `a718fba5b3b514d7999634ba5ba0a1e8652a9e51` | GPL-3.0 |

The source is **not redistributed in this repository**. Reproduce it with:

```bash
.venv/Scripts/python.exe scripts/fetch_reference_data.py
```

**Reproducibility checked 2026-08-05.** The whole analysis was re-run from freshly fetched
sources: every figure below is identical. The single difference across the entire output was the
KEGG orthology count, 28,394 → 28,396 — KEGG is a living database and gained two entries. No
result depends on it, but it is a reminder that **KEGG has no version number in its REST
response**, so the retrieval date is the only provenance available and must be reported.

---

## The answer

**`F` = the gene lies within 5,000 bases of a contig end.** Positional. It says nothing about
the gene's biology — only about where the assembler stopped.

From `annotate_vgfs.py::get_metabolic_flags`, `length_from_end=5000`:

```python
# within 5 kb of end of contig
if (int(row['start_position']) < length_from_end) or \
   (int(row['end_position']) > (scaffold_length_dict[row['scaffold']] - length_from_end)):
    flags += 'F'
```

The wiki agrees: *"The near contig end flag (F) is given when the gene is within 5000 bases of
the end of a contig."* Code and documentation match on this one.

**DRAM-v keeps F-flagged genes by default** — `--remove_fs` defaults to `False`
(`scripts/DRAM-v.py` line 88, `summarize_vgfs.py::filter_to_amgs` line 58).

## The complete flag set, from source

| | Meaning | Assigned when |
|---|---|---|
| `V` | viral | VOGDB category `Xr` or `Xs` (replication/structure) |
| `M` | metabolic | identifier present in DRAM's distillate |
| `K` | known AMG | identifier from a previously reported AMG |
| `E` | verified | as `K`, and experimentally verified to affect host metabolism |
| `A` | attachment | CAZy identifier used for host attachment/entry |
| `P` | peptidase | MEROPS identifier typical of viral peptidases — **undocumented** |
| `T` | transposon | a transposon occurs somewhere on the contig |
| `F` | near contig end | gene within 5,000 bp of either end |
| `B` | three in a row | three consecutive genes all carry `M` |
| `J` | — | **never assigned**; the line that would set it is commented out |

**Auxiliary score** (1 = most confident viral) is set from VirSorter categories on each flank:
hallmark both sides → 1; hallmark + viral-like → 2; viral-like both sides → 3; one side only → 4;
no viral-like/hallmark on the contig, **or gene at a contig end** → 5.

---

## THE CHECK — and it reverses the assumption

The project had been carrying "68% of `dcm` calls carry an `F` flag" as a worry. The number is
correct. **The interpretation was wrong, because it was never compared to a baseline.**

Conservative (curated) ocean catalogue, 88,729 calls, Wilson 95% intervals:

| Stratum | n | % `F`-flagged |
|---|---|---|
| **Baseline — all AMG calls** | 88,729 | **79.1%** [78.9–79.4] |
| **Baseline — KO-assigned only** | 31,772 | **75.8%** [75.3–76.3] |
| `dcm` | 5,797 | **68.0%** [66.8–69.2] |
| queuosine `queC/D/E/F` | 2,156 | 74.8% [72.9–76.6] |
| All suspect categories combined | 7,969 | 69.9% [68.8–70.9] |

> [!important] `dcm` is *less* likely to sit near a contig end than the average call
> 68.0% [66.8–69.2] against a KO-assigned baseline of 75.8% [75.3–76.3] — **non-overlapping
> intervals**. The suspect-to-baseline ratio is **0.92×**.
>
> The worry was not merely unsupported. It pointed the wrong way.

**This is the third artefact caught by Rule 5**, after the "83-fold" tool difference and the
"47.5%" suspect share. All three looked alarming, none survived a baseline.

### Why this strengthens the main result rather than weakening it

"Your suspect calls are contig-edge junk" was an available attack on the 25.1% finding. It is
now **measured and dead**: suspect and non-suspect calls are near-identically edge-distributed
(0.92×), so contig position cannot explain the disputed share — in either direction.
A confounder has been ruled out, not discovered. Add this to `05_redteam.md`.

### What replaces it, and it is larger

**79.1% of the curated ocean AMG catalogue is within 5 kb of a contig end** — and curation
*raises* that share, 62.8% → 79.1%.

F-rate climbs steeply as auxiliary score worsens (conservative table):

| Auxiliary score | calls | % `F`-flagged |
|---|---|---|
| 1 (most confident) | 12,628 | 57.9% |
| 2 | 42,348 | 78.5% |
| 3 (least confident kept) | 33,747 | 87.8% |

This is a **general property of the catalogue, not of the disputed categories** — so it belongs
in the paper as a limitation of the record, not as evidence for the thesis. Stated plainly: four
in five AMG calls come from genes at the edge of an assembly, where viral provenance is least
certain, and the tool retains them by default.

---

## Filter reconstruction — which DRAM-v settings the ocean authors ran

Their table shows `V`, `A`, `P` at **zero** and a maximum auxiliary score of **3**. That is
exactly the DRAM-v default filter, so no bespoke settings need to be assumed:

```python
filter_to_amgs(max_aux=3, remove_transposons=False, remove_fs=False)   # CLI defaults
    M present, and V absent, and A absent, and P absent, and auxiliary_score <= 3
```

**Why `B` is zero in both tables** — a structural consequence, not an accident. A `B` flag forces
`auxiliary_score = 4`, and the default filter keeps only `<= 3`. **`B` can never appear in a
default DRAM-v AMG output.** The data confirms it: 0 of 344,588 calls across both tables.

Minor data-quality notes: one conservative row has `" "` in `amg_flags`; six have a blank
auxiliary score.

---

## Three places DRAM's documentation and code disagree

Worth recording — this is H4's shape (stated criteria vs actual behaviour) applied to the *tool*
rather than to a paper.

1. **`T` flag.** The wiki says a potential AMG must have *"not been assigned an A, V or T flag"*.
   But `--remove_transposons` defaults to `False` at the CLI, so **T-flagged genes are retained
   by default**. (The *function* default is `True`; the CLI never uses it.) Consistent with the
   data: 762 T-flagged calls survive into the permissive catalogue.
2. **`P` flag is undocumented.** It appears in neither the wiki's flag list nor its description
   of the default filter, yet it is hard-coded into `filter_to_amgs` and **cannot be switched
   off by the user**. An undocumented, non-optional exclusion criterion.
3. **`B` flag definition.** The wiki says B requires three M genes *"and not the viral or viral
   attachment and entry flags"*. The code checks only for `M` on three consecutive genes; V and A
   are not consulted. The source carries its own `# this needs to be fixed` comment nearby.

---

## The VIBRANT half of Chunk 1 — and the tools are not comparable in kind

VIBRANT has **no equivalent of `amg_flags` and no auxiliary score.** Its AMG call is a single
membership test, from `scripts/VIBRANT_annotation.py` line 1732:

```python
if annotations[n+2] in AMG_list:
    AMG = 'AMG'
```

`AMG_list` is `VIBRANT_AMGs.tsv` — a flat list of **2,834 KEGG KOs**, no columns, no scores.
If the KO is on the list, the gene is an AMG. There is no contig-position test, no flanking-gene
context, no confidence tier, and no user-adjustable threshold.

> [!important] The two tools decide differently in kind, not merely in degree
> **DRAM-v's call is contextual** — `M` present, `V`/`A`/`P` absent, auxiliary score ≤ 3 from
> VirSorter categories on both flanks. Where the gene sits on the contig changes the answer.
>
> **VIBRANT's call is categorical** — KO membership, and nothing else.
>
> So for VIBRANT, **the disputed share of the record is fixed entirely by database composition**.
> `dcm` = K00558 is on the list (verified in `data/VIBRANT_AMGs.tsv`), as are the queuosine KOs.
> **There is no mechanism by which VIBRANT could ever filter out a disputed category** — no
> confidence tier exists for a curator to raise. Whatever is in the file becomes a call.

This sharpens **H3** from "the tools give different suspect fractions" to a mechanistic
prediction: VIBRANT-based catalogues should track the 1.9%-of-database figure scaled by how often
those KOs are hit, with no confidence-related attenuation, whereas DRAM-v-based catalogues carry
a filter that *can* move the number — and, per the curation finding, moves it **upwards**.

It also explains the namespace result already recorded: VIBRANT decides on KEGG KO, DRAM decides
largely on PFAM, so the two cannot even be asked the same question about the same gene.

## Consequences for the analysis plan

- Brief step 3 (**confirm tool semantics**) is **done** for both tools. No assumption remains.
- **H3 gets a mechanism**, not just a comparison — see the VIBRANT section above.
- Do **not** filter on `F`. It is not a quality flag and it is not category-specific.
- Report the 79.1% edge fraction as a **declared limitation of the record**, with the
  auxiliary-score breakdown. It is honest, it is new, and it is not a result about the thesis.
- Add the ruled-out confounder to `05_redteam.md` as an attack that was tested and failed.
- Carry the three doc/code discrepancies into the write-up's methods discussion.
