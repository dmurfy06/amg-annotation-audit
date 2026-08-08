# Chunk 5 — second-pass concordance on the 12 judgement families

**Date:** 8 August 2026
**First pass:** `chunk5_worksheet_pass1_completed.md` (AI-produced, 35 families)
**Second pass:** `chunk5_blind_concordance_sheet_completed.md` (Daniel Murphy, 12 families)

## Why only 12 families

The first pass covers 35 families, but only 12 involved evidentiary judgement. The other
23 were decided mechanically by the protocol: no Tier 1–5 evidence exists, so the family
cannot be ruled out, so it stays in. Two raters applying the rubric must agree on those by
construction, and including them would inflate the agreement figure while testing nothing.

Concordance was therefore assessed on all families where the protocol required evidence to
be weighed, rather than on families resolved by mechanical default.

**A property of the design worth stating:** at the time the 12 families were selected and
rated, `data/adjudication_counts_SEALED.tsv` was still sealed. Neither rater knew which
families carried abundance weight, so the sample cannot have been chosen to flatter the
headline. Evidence tier was the only available stratifier.

## Results

| Field | Agreement | 95% CI |
|---|---|---|
| Verdict | **12 / 12** | [75.8 – 100] |
| Confidence | **12 / 12** | [75.8 – 100] |
| Evidence tier | **11 / 12** | [69.9 – 98.9] |

Cohen's κ for verdict = 1.00 (chance agreement P_e = 0.51 given marginals of 8 COUNTS,
3 UNRESOLVABLE, 1 DOES NOT COUNT).

Tier was scored as agreement if the two answers overlap, since both raters were permitted
to give ranges (e.g. "1–2"). Exact matches: 5. Overlapping: 6. Disagreement: 1.

| Family | Pass 1 verdict | Pass 2 verdict | Pass 1 tier | Pass 2 tier | Confidence |
|---|---|---|---|---|---|
| `dsrC_tusE` | UNRESOLVABLE | UNRESOLVABLE | 3–4 ecology, 0 identity | 3 ecology, 0 genetics | high / high |
| `dut` | COUNTS | COUNTS | 4 | 4 | low / low |
| `folate` | UNRESOLVABLE | UNRESOLVABLE | 2 | 2 | high / high |
| `glycoside_hydrolase` | DOES NOT COUNT | DOES NOT COUNT | 1–2 | 1 | high / high |
| `glycosyltransferase` | COUNTS | COUNTS | 2 | 2 | low / low |
| `NAMPT` | COUNTS | COUNTS | 1–2 | 2 | low / low |
| `nrdH` | COUNTS | COUNTS | 4–5 | 4–5 | low / low |
| `phoH` | COUNTS | COUNTS | 4–5 | 4 | moderate / moderate |
| `queuosine` | UNRESOLVABLE | UNRESOLVABLE | 2 | 2 | high / high |
| **`rfbC`** | COUNTS | COUNTS | **2** | **6** | low / low |
| `speD` | COUNTS | COUNTS | 5–6 | 5 | low / low |
| `TALDO1` | COUNTS | COUNTS | 1–2 | 1–2 | moderate / moderate |

## The one disagreement, and why it favours pass 2

`rfbC`, four tiers apart. Pass 1 assigned **Tier 2** on the strength of the shared
nucleotide-sugar block literature (Mann *et al.* 2015; Sun *et al.* 2013), which
demonstrates phage-encoded glycosyltransferases modifying host O-antigen.

Pass 2 assigned **Tier 6** — chemistry alone.

Pass 2 is better reasoned. That literature concerns the **transfer** step. `rfbC` is a
precursor enzyme in dTDP-rhamnose synthesis, not a transferase, and the block's own
caveat states that extending the transfer evidence to precursor enzymes is "an assumption,
not a finding". Tier 2 imports evidence about a different enzyme class.

The verdict is unchanged (COUNTS under both), so the headline is unaffected. But the tier
matters for the write-up: under the protocol, Tier 6 alone can never rule a family out, so
a Tier 6 `rfbC` is a family the evidence base cannot currently adjudicate at all.

Pass 2's resolving experiment — *determine the destination of the dTDP-rhamnose produced
by the phage enzyme* — is the only one of the twelve that is not derivable from the
evidence supplied in the blind sheet, and it targets exactly the precursor/transfer gap.

## Independence — what can and cannot be claimed

**Stated plainly for the methods section: independence of the second pass cannot be
verified, and no inter-rater reliability claim should rest on it.**

The blind sheet was constructed by stripping three things from the evidence dossiers: any
passage naming a verdict, the first pass's tier assessments, and the pre-named resolving
experiments. Zero leaks were verified programmatically at build time
(`scripts/build_blind_concordance_sheet.py`).

However, the first-pass worksheet and the evidence dossiers **remained present in the
rater's Obsidian vault** throughout the second pass; the intended deletion was not carried
out. The rater states he did not open them.

Text forensics were run and **do not indicate copying**:

- free-text resolving experiments are 43–75% similar to pass 1, but **every content word
  in all eight is present in the blind sheet itself**, so the shared source is sufficient
  to explain the overlap;
- `nrdH` scores lowest (42.9%) precisely because the blind sheet stated its resolving
  point in different words;
- the `rfbC` tier disagreement and its novel resolving experiment are not consistent with
  transcription.

This is the opposite pattern to the one that invalidated the first pass, where 27 of 35
families shared verbatim runs of 120+ characters with a parallel adjudication and **none**
of those runs appeared in the dossiers.

**Recommended methods wording:** report this as a second-pass rubric-application check
with independence stated as unverified, note n = 12, and do not present κ as an
inter-rater reliability statistic for the study. A genuine IRR figure would require a
second human rater working from the blind sheet alone.

## Controls

All four pass, plus the protocol's worked example:

| Control | Required | Pass 1 |
|---|---|---|
| `psbA` | COUNTS | COUNTS ✓ |
| `psbD` | COUNTS | COUNTS ✓ |
| `xtmA` | DOES NOT COUNT | DOES NOT COUNT ✓ |
| `xtmB` | DOES NOT COUNT | DOES NOT COUNT ✓ |
| `dcm` | DOES NOT COUNT | DOES NOT COUNT ✓ |

**The controls are not blind** — the protocol and `How To Adjudicate` name all of them.
They test whether the rule, faithfully applied, produces the right answer. They do not
test rater impartiality, and the write-up must not claim they do.

## Gates cleared

Both pre-registered conditions for opening `data/adjudication_counts_SEALED.tsv` were met
on 8 August 2026: verdicts complete for all 35 families, concordance computed, all
controls correct. The seal was opened after this file was written.

Results follow in `chunk5_sensitivity.txt` and `chunk6_abundance.txt`.
