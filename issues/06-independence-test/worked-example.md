# One run, in full

**Honesty label.** A real run, not an illustration. Nine checks plus one repeat, 30 August 2026, against a synthetic vendor recommendation memo. Three makers crossed with three framings: A = Claude, B = Gemini, C = ChatGPT. Every block went into a brand-new chat and carried a cell id which the model echoed back inside its JSON, so no answer could be mislabelled. Every figure below came out of the tool.

**A note on the record.** The run was executed against the memo denominated in pounds; the published version is in euro. Nothing else changed and no figure depends on it. The ten answers in `run-v3/cells.json` are as returned, with currency symbols and dashes normalised in transcription and no wording altered.

**Two limits, stated up front.** Isolation was *instructed* inside each prompt rather than switched off in the product settings. An instruction asks a model not to retrieve; the setting stops it. Any memory that leaked in is shared context between checks and would push agreement up, which means the independence reported here is if anything flattering. And the matching was **lexical, not model-judged**. The lexical matcher leans toward calling two criticisms the same, which pushes n_eff down. The two limits point in opposite directions.

## The document under test

A recommendation to an investment committee: replace a field service platform, two finalists, a weighted scoring model, and a request to release EUR 310k. Deliberately not this issue, and deliberately not a real company. A document about itself can be accused of being chosen to flatter the argument.

**A reviewer baseline was written and sealed before any check ran**, so the panel could be scored against a named human list rather than against an impression.

## What came back

```
  Checks per document             9
  Mean agreement between them     0.289
  Verdicts                        5 of 9 said MATERIAL_PROBLEMS, 4 said UNSOUND

  EFFECTIVE INDEPENDENT OPINIONS  2.72

  You ran 9 checks and got 2.72 opinions' worth of information.
  6.28 of them were echo.
  Drop any single check and it lands between 2.53 and 2.83.

  WHAT BOUGHT THE INDEPENDENCE      (lower agreement = more bought)
    Changed the framing, held the model   0.427  (9 pairs)
    Changed the model, held the framing   0.230  (9 pairs)
    -> Indistinguishable. Shuffling the pairs at random produces a gap
       this big 5% of the time. Do not read a winner into it.

  THE NOISE FLOOR       (same model, same framing, asked twice)
    It agreed with itself                 0.321
    n_eff if every check were that check  2.52
    -> The panel clears its noise floor by 0.20.

  Distinct problems raised        21
  Raised by only one check        10  (48%)
```

Nine checks, 2.72 opinions. For scale, the published nine-judge panel came to 2.18 and a human panel on the same measure lands between 4.0 and 5.8.

**The noise floor is the number to read second, and here it is brutal.** The same model, same framing, same document, asked twice, agreed with itself at 0.321, which is *more* than the 0.289 the whole nine-way panel managed. Ask one model the same thing nine times and the formula returns 2.52; nine checks across three makers and three framings returned 2.72. The crossing bought 0.20. Nine checks, three makers, three framings, and most of what looked like independence was a model being inconsistent with itself.

**And the two runs of the identical prompt returned different verdicts.** A-neutral said MATERIAL_PROBLEMS. A-neutral#2, same model, same words, fresh chat, said UNSOUND. Nobody who runs one check would ever see that.

## The panel against the sealed baseline

The human baseline named ten problems. The panel found six of them squarely, two partially, missed two, and added one the human had not seen.

| # | Sealed baseline item | Panel |
|---|---|---|
| 1 | Weighted totals do not follow from the table: K 77 and M 76, so the gap is one point, not four | **FOUND**, by eight of nine checks, with the correct figures |
| 2 | The two quotes cover unstated and different terms, so TCO is built on a non-comparison | **FOUND**, seven checks |
| 3 | Weights were set after the demonstrations | **FOUND**, all nine checks |
| 4 | Cultural fit is 15%, undefined, and carries K's largest lead | **FOUND**, five checks |
| 5 | Four references against one, not like for like | **FOUND**, four checks |
| 6 | Both implementation estimates come from the vendors | **FOUND**, seven checks |
| 7 | Data migration is named as a risk and costed nowhere | **PARTIAL**. Several checks note the scope is unseen; none says it is absent from the cost model |
| 8 | No sensitivity analysis on a one-point margin | **PARTIAL**. Raised once, by A-inverted, and as a remedy rather than a finding |
| 9 | The 1 to 5 scale is never defined and eight participants were averaged with no dispersion reported | **MISSED**. No check raised it |
| 10 | "Not attributable to any single criterion" is false; remove cultural fit and M wins | **FOUND**, four checks, but **none of them quantified it** |

**What the panel added.** A-adversarial, alone, checked the calendar: *"From the paper's own date of 24 August 2026 to end of support in June 2027 is at most ten months."* The memo asserts eleven months in three places and uses the urgency to justify deciding this month. Verified: 24 August 2026 to 30 June 2027 is 310 days, 10.2 months. **A factual error in the document, raised by exactly one of nine checks, and absent from the human baseline.**

**What the human had that the panel could not reach.** Item 9 is the one nobody found, and it is the one that undermines every number in the table: without dispersion, a 4 that eight people agreed on is indistinguishable from a 4 that was half 2s and half 5s. Item 10 shows the same gap from the other side. Four checks said removing cultural fit reverses the ranking. **None worked out by how much.** It is 5.9 points to Vendor M. The panel found the direction and stopped; the argument that changes the committee's mind is the size.

## What this run says about the method

**For it.** Ten of 21 distinct problems came from a single check. Take any one check on its own and you lose roughly half the findings, including the only calendar error anyone caught. A majority vote across the nine would have deleted all ten.

**Against it.** 6.28 of the nine checks were echo, the panel barely cleared the noise it makes on its own, and the two blind spots it left are the two that most needed a person: how the scores were built, and how big the reversal is. The panel is good at finding stated things that contradict each other. It did not once ask what was not there.

**Neither axis won.** The literature says framing should do more work than model. On this document the gap between the two axes is inside what random reshuffling produces 5% of the time, so this run cannot tell them apart, and it is reported that way rather than rounded into a claim.

## Reproducing it

`run-v3/cells.json` holds all ten answers as returned. `run-v3/score.py` rebuilds the figures from them. `run-v3/run-sheet-v3.md` holds the ten prompts. The sealed baseline is in `run-v3/reviewer-baseline-SEALED.md`, written before the run and unedited since.

---

The measure here belongs to survey statistics and the findings it rests on are other people's; both are cited in the sources above. What is mine is the assembly, the run, and the reading of it.

Arguments and voice are mine. Claude is used as an editing and scaffolding tool. If others' concepts are used, they are referenced in the sources section.
