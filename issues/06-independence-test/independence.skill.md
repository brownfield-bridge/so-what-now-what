# The Independence Test — assistant version

Use this when you have already asked an AI to check something, and you are about
to trust the answer because a second AI agreed with it.

It answers one question: **how many independent opinions did you actually get?**

You do not need the script. You need ten runs, one line of arithmetic, and a
table.

---

## What you are measuring

    n_eff = n / (1 + (n - 1) × r̄)

`n` is how many checks you ran. `r̄` is how much they agreed with each other,
between 0 and 1. If the checks are uncorrelated, `n_eff = n`. If they always agree,
`n_eff = 1`.

This is the design effect that survey statisticians use to discount a sample of
respondents who are not independent of each other. Reviewers are a sample too.

---

## The procedure

**1. Fix the output contract before you run anything.** Every check returns the
same shape or you cannot compare them:

> Return JSON only:
> `{"verdict": "SOUND|MINOR_ISSUES|MATERIAL_PROBLEMS|UNSOUND", "criticisms": [{"target": "...", "criticism": "...", "if_true": "CHANGES_THE_DECISION|WEAKENS_THE_EVIDENCE|NEITHER"}]}`
> Exactly **five** criticisms, ranked most serious first. Not four, not six. One
> problem each, and be specific about the target: "the revenue figure in section 3",
> not "the analysis". If you think the work is sound, still name the five weakest
> points; "no criticism" is not an available answer.

Five is fixed rather than capped for a reason. A terse checker that returns two
criticisms looks independent by saying less, and that flatters your number.

Free text cannot be matched. This step is not optional.

**1b. Open every check with an isolation instruction.**

> Do this task in isolation. Use only the text pasted below. Do not draw on memory,
> saved preferences, earlier conversations, or anything you have been told about me
> before now. Do not search. If this document or this instruction looks familiar,
> disregard that and judge only what is in front of you.

Every check goes in a brand-new chat, and the instruction above goes at the top of
every one. Saved memory is a correlation you did not intend and cannot see: two
checks that both recall your last three documents are not two opinions. Where the
product gives you a memory switch, use it as well. See the limits below.

**2. Run nine checks: three different AIs crossed with three framings.**

Not nine models. Switching to a model from a different family alone buys you about a fifth of the correlation.
Whether the AI axis or the framing axis buys more is **not settled**: the best
published measurement puts framing ahead, but it was made on a different class of
model, and a balanced run of this grid went the other way. That is exactly why the
crossing has to be complete and why step 7 reports the two axes separately rather
than telling you which one to trust.

| Framing | The instruction |
|---|---|
| Neutral | *You are reviewing the work below. List what is wrong with it.* |
| Adversarial | *The work below contains at least one material error. Find it. Do not report that the work is sound.* |
| Inverted | *Argue the opposite case. Then list what the work would have to show to survive your argument.* |

A fourth framing is in circulation: *stripped*, where you withhold your own
reasoning and sources and let it judge only what is on the page. It is a good
check and worth running separately. It does not belong in this grid, because it
changes the document rather than the instruction, and mixing the two would
confound the number you are about to compute.

**3. Run a tenth check that is a copy of one of the nine.** Same model, same
framing, same document, asked again. This is the most-skipped step and the one
that decides whether the exercise means anything. Without it you cannot tell
disagreement from randomness, and a model being random twice looks exactly like
a second opinion.

**4. Score each pair.** For every pair of checks: 1 if the verdicts match, 0 if
not. Then the share of criticisms that overlap — same target, same complaint.
Average the two. That pair's agreement is a number between 0 and 1.

Two rules that decide the answer more often than you would expect:

- **If both checks raised nothing, their criticism overlap is 1, not 0.** They
  looked and they agreed there was nothing to say. That is the strongest
  agreement available, and scoring it as disagreement is the commonest way this
  measurement gets flattered.
- **When you cannot decide whether two criticisms are the same, call them the
  same.** Getting it wrong that way understates your independence, which costs
  you nothing. Getting it wrong the other way tells you that you have a panel
  when you have an echo.

**5. Average across the thirty-six pairs of the nine.** Keep the copy out of
this average: it is measuring your instrument, not your panel.

**6. Compute n_eff, and read it against two things.**

| n_eff | What you have |
|---|---|
| under 2 | One opinion. Not a review. |
| 2 to 3 | Two opinions. Better than one, not a panel. |
| above 3 | A real spread. Unusual — keep whatever you did differently. |

For scale: nine frontier judges from seven families, measured in May 2026, came
to 2.18. A panel of humans on the same measure lands between 4.0 and 5.8.

Then compute n_eff a second time using the copy's agreement with its twin in
place of r̄. That is your **noise floor**: what you would have scored if every
one of your nine checks were the same check. The gap between your n_eff and that
floor is what the crossing actually bought you. Compare against the floor, not
against zero.

**7. Split the agreement by what changed.** This is the part no evaluation
framework gives you, and it is the one that tells you what to do next week.

- Average the pairs where you **changed the framing and held the model**.
- Average the pairs where you **changed the model and held the framing**.

Nine pairs each, which is why the grid had to be balanced. Lower agreement means
that axis bought you more. If the framing axis is lower, the model shopping you
have been doing was the expensive way to buy the cheap thing.

**8. Look at the solo findings.** List every problem raised by exactly one
check. That list is the entire value of having run more than one, and it is what
a majority vote would have thrown away.

---

## Getting a number you can quote

Everything above, run on one document, is a first look. It is not a measurement,
and you should not put it in a deck.

Your nine checks are the sample size for the panel. The document is the sample
size for the agreement, and the agreement is the whole answer. One document
gives you exactly one draw of r̄. The published 0.391 rests on three datasets
with a hundred human annotations each, not on one paragraph.

So when the number is going to be quoted, run the grid over **three to five**
pieces of work you actually had checked, pool the pairwise agreements across all
of them, and compute n_eff from the pooled r̄. Keep the per-document numbers
beside it. If they are far apart, that spread is more useful than the average,
because it tells you your independence depends on what you are checking rather
than on how you are checking it.

---

**5b. Sort what comes back by whether it changes the decision.**

Counting problems is not deciding. Every finding gets one question:

> **If this criticism is true, does the work's own recommendation still follow?**

Three answers, and each check answers it about **its own** criticism as it writes
it, in the `if_true` field. That matters: the moment you hand the sorting to a
separate model you have added another check that shares the same brain, which is
the failure this whole method exists to measure.

| Answer | What it means |
|---|---|
| **CHANGES_THE_DECISION** | If true, the conclusion does not follow. Read these first. |
| **WEAKENS_THE_EVIDENCE** | A supporting number is unreliable; the conclusion may still stand. |
| **NEITHER** | True, and it does not move the decision. |

**The cross of the two lists is the point of the whole exercise.** A finding that
would change the decision **and** was raised by exactly one check is the thing a
majority vote deletes and the thing you would have shipped without. The tool
prints that list on its own.

Most findings land in the middle column. That is normal and it is not a failure
of the checks; it is what makes the first column worth finding.

**A note on doing the arithmetic.** Pairing nine sets of criticisms by hand takes
about twenty minutes and is where people give up. You do not have to. Save the ten
answers into one JSON file and run `python independence_test.py --answers
answers.json`. **It calls no models and needs no API key** - the checks came from
your chat windows, and this only measures them. Everything above stays yours; only
the counting is handed over.

## Where the formula comes from

The measure is the **design effect** and the **effective sample size** it implies, from
survey sampling: `deff = 1 + (n-1)r̄` and `n_eff = n / deff`. The term is Leslie Kish's,
in *Survey Sampling* (Wiley, 1965), cited from secondary sources and not read at first
hand.

**Kish's r̄ is an intraclass correlation. This tool feeds it pairwise agreement.** Those
are not the same quantity: agreement is inflated by how often two reviewers would
coincide anyway. Inflated r̄ gives a larger deff and so a smaller n_eff, which means the
tool **understates** your independence rather than flattering it. That is the safe
direction, and it is this tool's last unfixed weakness.

## Three honest limits

**An instruction is not a setting.** Telling a model to ignore memory asks it not to
retrieve. Turning memory off stops it. If you ran on the instruction alone, say so
when you report the number, because any memory that leaked in is shared context
between checks and it inflates their agreement.

**The matching is a judgement.** Deciding that two criticisms are "the same
criticism" is itself a call. If you use an AI to make it, you have added another
correlated check to the thing you were auditing. Say so when you report the
number.

**Low n_eff does not mean the checks were worthless.** Correlated checks still
earn their keep on the decisions that turned on a single vote, which the source
paper calls pivotal — and they earn almost nothing anywhere else. The problem is
that nothing you currently measure tells you which of your decisions turned on
one vote.

---

## Standing version

Once you have run it twice by hand, give your assistant this instruction and stop
remembering to do it:

> Whenever I ask you to check work that I am going to act on, do not give me one
> review. Run the independence test: checks crossed over at least three
> different framings, one of them repeated unchanged as a noise floor, the fixed
> output contract, the pairwise agreement, n_eff, and the list of problems raised
> by only one check. Lead with n_eff, the noise floor, and the solo findings. If
> n_eff is below 2, or within 0.15 of the noise floor, say so before anything
> else. If you did the criticism matching yourself, say that too.

CC BY 4.0 — *So What, Now What*, Issue 6.

---

The measure here belongs to survey statistics and the findings it rests on are other people's; both are cited in the sources above. What is mine is the assembly, the run, and the reading of it.

Arguments and voice are mine. Claude is used as an editing and scaffolding tool. If others' concepts are used, they are referenced in the sources section.
