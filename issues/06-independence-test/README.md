# The Independence Test

**You ran nine checks. How many opinions did you get?**

When you ask a second AI to check the first one's work, you assume you are buying
a second opinion. You are usually buying an echo. Nine frontier judges from seven
different model families carry roughly **2.18 independent votes' worth** of
information. A panel of humans reviewing the same work gets 4.0 to 5.8.

**Two things come out of this, and they answer different questions.**

The **score** is about your checking, not about your document. Nine checks are worth about two
opinions. We got 2.72 in August and 2.12 in September on the same document, which never changed a
word. Learn that once and discount AI agreeing with AI from then on.

The **findings** are about your document, and you get fresh ones every time. One check gives you
five criticisms. Nine gave us twenty-one, and ten of those came from a single check. Those ten are
what a majority vote deletes.

**Run it once to stop trusting agreement. Keep running it because nine checks see four times what
one check sees.**

## What it does that nothing else does

Evaluation frameworks — promptfoo, DeepEval, Langfuse, Braintrust — will run a
multi-judge jury and take a majority vote. Some will calibrate the judges against
human labels. **None of them audits whether the jury is one opinion wearing nine
hats.** Meanwhile a product category has grown up selling multi-model *agreement*
as a confidence score, which is the fallacy this tool exists to expose.

The metric is in the literature. The plumbing is in the eval frameworks. Nobody
had put them together in something you can run on a Sunday.

## How to run it

**You run the checks. This does the arithmetic.** There is no path here that calls
the models for you, by design.

**1. The ten blocks.** Open `prompts.md` and paste each block into a fresh chat,
across three different AIs. Nine checks plus one deliberate repeat. Every block
carries its own cell id and its own isolation instruction, so you do not have to
toggle memory settings ten times. If you would rather an assistant walked you
through it, `independence.skill.md` is the same procedure written for that.

**2. The arithmetic.** Save the ten answers into one JSON file and hand them over.
**No API keys, no accounts, no cost.**

```bash
python independence_test.py --answers answers.json --doc "board paper"
python independence_test.py --verify        # reproduces the published figures
```

`answers.json` is a list of the ten blobs exactly as the models returned them.
Family, framing and the repeat are read from each `cell_id`, so `A-neutral`,
`C-inverted` and `A-neutral#2` all work. If two answers claim the same id the
script stops and names it rather than quietly averaging them.

**Standard library only. Python 3.8 or later. Nothing to install.**

### What was cut, and why it is worth saying

An earlier version could call the three model APIs for you. It is gone. It needed
three keys and three SDKs, it hardcoded model names that go stale within months,
and **it had never actually been run.** One tested path is worth more than two
paths where one of them is a promise.

## What comes back

This is the real output of the run that ships in `run-v3/`, not an illustration.
Run `python3 independence_test.py --answers run-v3/cells.json` and you get it back.

```
  EFFECTIVE INDEPENDENT OPINIONS  2.72

  You ran 9 checks and got 2.72 opinions' worth of
  information. 6.28 of them were echo.
  Drop any single check and it lands between 2.53 and 2.83.
  One document. Read this as indicative. See --help on why.

  WHAT BOUGHT THE INDEPENDENCE      (lower agreement = more bought)
    Changed the framing, held the model   0.427  (9 pairs)
    Changed the model, held the framing   0.23   (9 pairs)
    -> Indistinguishable. Shuffling the pairs at random produces a
       gap this big 5% of the time, so this run cannot tell the
       two axes apart. Do not read a winner into it.

  THE NOISE FLOOR       (same model, same framing, asked twice)
    It agreed with itself                 0.321
    n_eff if every check were that check  2.52
    -> Your panel clears its noise floor by 0.20. That gap,
       not n_eff itself, is what the crossing actually bought.

  Distinct problems raised        21
  Raised by only one check        10  (48%)
```

That block is the diagnosis. The next one is the point of running it at all.

## What you actually get

Every paste block asks each check one more question about **its own** criticism,
in the `if_true` field: *if this criticism is true, does the work's own
recommendation still follow?* Three answers are allowed.

| Answer | What it means |
|---|---|
| **CHANGES_THE_DECISION** | If true, the conclusion does not follow. Read these first. |
| **WEAKENS_THE_EVIDENCE** | A supporting number is unreliable; the conclusion may still stand. |
| **NEITHER** | True, and it does not move the decision. |

Each check answers it about its own finding, as it writes it. That is deliberate.
Hand the sorting to a separate model and you have added another reviewer with the
same brain, which is the failure this whole method exists to measure.

The tool then crosses that against the solo list and prints what falls in both. This is the
real output of `run-v4/`, not an illustration:

```
  WHAT WOULD CHANGE THE DECISION    (each check's own call on its own
                                     criticism, not a fourth model's)
    Findings that change the decision     8
      of those, raised by one check only  0
    Findings that only weaken evidence    5

    Read these first. Each means the recommendation does not follow:
      - [The weighted totals of 78 and 74 in the section 3 scoring table] The
        arithmetic is wrong: the stated weights and scores produce 77 for Vendor K
        and 76 for Vendor M, so the real margin is one point, not four.
      - [The claim that the margin 'is not attributable to any single criterion']
        Removing the single subjective criterion 'Cultural fit and partnership'
        reverses the ranking in Vendor M's favour.
      ...
```

**Note the zero.** On that run every decisive finding was raised by more than one check, so the
cross is empty and the tool says so rather than manufacturing a list. A document with three
unmissable errors does not need nine checks to find them. Run it on a subtler one and the cross
fills up: in `run-v3/`, ten of twenty-one problems came from a single check.

**A finding that would change the decision and that exactly one check raised is
the thing a majority vote deletes and the thing you would have shipped without.**
That short list is what you are running this for. Most findings land in the middle
row instead, which is normal, and it is what makes the first row worth finding.

**Three runs ship, and they disagree.** `run-v3/` is the run the newsletter cites; it predates the
`if_true` field, so scoring it prints *"Not available"* for this block. `run-v4/` is the same
document run again five days later, and it carries the field. It also came back markedly more
converged: nine checks worth 2.12 opinions rather than 2.72, mean agreement 0.406 rather than 0.289.
`run-v5/` then ruled out the obvious explanation: with memory off the repeat agreed with itself
perfectly and three checks scored 1.63, lower still. The tool was consistent across all three. What
it was measuring was not. Both run READMEs say what we can and cannot claim from that.

## Three things that decide whether the number is real

**Turn memory off, or use a document the account has not seen.** Isolation is instructed inside
every block, and an instruction only asks a model not to retrieve; the setting stops it. This bites
hardest on a re-run: our own `run-v4/` put the same document through the same accounts five days
after `run-v3/`, memory on, and the noise floor doubled from 0.321 to 0.75. A model that remembers
last week's answer agrees with itself for a reason that is not independence, and your panel scores
worse than it deserves.

**The noise floor.** One of the nine cells is run twice, unchanged (`--no-replicate`
turns it off). Without it you cannot tell disagreement from randomness, and a
model being random twice reads as a second opinion. Read n_eff against the floor,
not against zero.

**How many documents, not how many checks.** Nine checks on one document is a
first look. The nine checks are your sample size for the panel; the document is
your sample size for the agreement, and the agreement is the whole answer. Pass
three to five files and the tool pools the pairwise agreements across them and
shows each document's own number beside the pooled one. If those are far apart,
that spread is the finding.

**The jackknife.** The report also drops each check in turn and tells you where
n_eff lands without it. A number that moves a lot when one check leaves was never
a measurement.

## The number

    n_eff = n / (1 + (n − 1) × r̄)

The design effect, borrowed from survey statistics. Reviewers are a sample too.

## Keep the crossing balanced

The ten blocks in `prompts.md` are a **balanced** crossing: three model families × three
framings (neutral, adversarial, inverted), plus one repeat. Balanced is not decoration. It is
what gives you nine framing-axis pairs and nine model-axis pairs, so the second
block of the output is a comparison rather than an impression. Drop a cell and
that comparison stops meaning anything.

The crossing matters more than the model list. Measured cross-family and
within-family correlation differ by only about 0.14, so **switching model buys
you about a fifth of the correlation. Switching what you ask it to be buys
more.** The output now lets you check whether that holds on your document
instead of taking it from the paper.

A fourth framing, *stripped* (withhold your reasoning and sources, judge only
what is on the page), is defined in the script and worth running on its own. It
is deliberately not in the grid: it varies the document rather than the
instruction, so including it would confound the axis the second block measures.

## Two honest limits, stated in the tool's own output

1. **The matcher is a judgement.** Deciding two criticisms are the same
   criticism is a call, and a lexical matcher will get some of them wrong. What
   matters is which way. A missed match makes two identical criticisms look like
   two opinions and flatters you; a false match costs you a little credit and
   nothing else. The thresholds lean toward the false match on purpose, and the
   report says so. `--matcher llm` clusters every criticism in a single call
   instead, which handles paraphrase far better and puts a model inside your
   audit. The report then names the model that did it, because that is the
   thing you would otherwise forget to mention.
2. **A low `n_eff` does not mean the checks were worthless.** Correlated checks
   still pay on the decisions that turned on a single vote, and pay almost
   nothing elsewhere. The paper calls those pivotal. The trouble is that nothing
   you currently measure tells you which of your decisions turned on one vote.

## What is in here

    prompts.md              The ten blocks to paste. Start here if you have a browser and nothing else.
    independence.skill.md   The same procedure written for an assistant to run with you.
    independence_test.py    Does the arithmetic. --answers takes the ten JSON blobs you got back.
                            Standard library only. No API key, no install, no account.
    run-v3/                 The run behind the newsletter, in full: every answer as it came back
                            (cells.json), the scored result, the sheet that produced it with the
                            document included, and the human review that was written and sealed
                            before any of it ran.
    run-v4/                 The same document run again on 4 September, five days later, with the
                            if_true field the older run predates. More converged: 2.12 opinions
                            from nine checks, not 2.72. Its README does not explain that away.
    run-v5/                 Four cells, 4 September, memory OFF: Claude incognito, Gemini and
                            ChatGPT temporary chats. Run to test whether v4's convergence was the
                            models recalling the document. It was not: with memory off the repeat
                            agreed with itself PERFECTLY, 1.00. Three checks scored 1.63.
    run-2026-08-29-v1-void/ VOID, and kept on purpose. The first attempt put two prompts into the
                            same chat, so the second answer was the first one repeated. It is here
                            because the failure is the most likely one you will make, and because a
                            kit that only shows its clean runs is doing the thing this issue is about.
                            The script now stops and names the cell if two answers claim the same id.

## Sources

- Nine judges, two effective votes — correlated errors in LLM evaluation panels, arXiv:2605.29800
- Correlated errors across 350+ LLMs, ICML 2025, arXiv:2506.07962
- Dependence-aware aggregation for LLM-as-a-judge, ICML 2026, arXiv:2601.22336
- Family bias in model ensembles, arXiv:2603.17111
- Where verification actually helps — pivotal queries and the one-vote margin, arXiv:2608.06940

CC BY 4.0 — *So What, Now What*, Issue 6.

---

The measure here belongs to survey statistics and the findings it rests on are other people's; both are cited in the sources above. What is mine is the assembly, the run, and the reading of it.

Arguments and voice are mine. Claude is used as an editing and scaffolding tool. If others' concepts are used, they are referenced in the sources section.
