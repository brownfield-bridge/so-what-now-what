# The AI review recommended a supplier. Nobody had seen its full terms.

**So What, Now What - Issue 8 · Saturday 3 October 2026**

Two skills for choosing a supplier you cannot replace quickly. **First, Anthropic's own `/vendor-review`** gives you a fast, good first look at the bids. **Then the Sourcing Read**, in this folder, does what that review does not:
- checks the review against the bids' own words;
- keeps the decision with the person signing;
- drafts the clarification letters and the schedule of commitments for the contract;
- after award, follows whether the claims that won the work held.

---

## Start here

**Take one sentence that helped a supplier win, and answer four questions:**

1. What exactly did they commit to do?
2. Under what conditions, and by when?
3. What record, one that you control, would show whether they did it?
4. Where is that commitment written into the signed agreement?

If you cannot answer the fourth, find out before you rely on it. That is the whole method in miniature. The rest of this folder does it for every clause.

## What's here

- [**`sourcing-read.skill.md`**](sourcing-read.skill.md) - the guided read, in eight stages, to run after `/vendor-review`. Save it as a skill in your assistant, or paste it into a chat as a prompt.
- [**`standing-checklist.md`**](standing-checklist.md) - twelve core decisions a sourcing document either makes or leaves to chance, and the full list of forty-seven behind them.
- [**`sourcing-read-workbook.xlsx`**](sourcing-read-workbook.xlsx) - the record: your weights with the date you set them, the evidence rows with their quotes and exceptions, the counts, the register. This is the one file to keep.
- [**`SOURCES.md`**](SOURCES.md) - what the method draws on, and what was checked when.
- [**`worked-example/bid-pack.md`**](worked-example/bid-pack.md) - a fictional request for quotation and four responses to it.
- [**`worked-example/vendor-review-run.md`**](worked-example/vendor-review-run.md) - what `/vendor-review` produced on the same bids, unedited apart from dash style.
- [**`worked-example/review-check-one-instruction.md`**](worked-example/review-check-one-instruction.md) - the review checked by a second session with one instruction: 40 flags, every quote confirmed.
- [**`worked-example/test-1-adjudication.md`**](worked-example/test-1-adjudication.md) - the 40 flags judged by another Claude session instructed to challenge each one: 11 upheld, 19 in part, 10 rejected, 4 potentially material. Its verdicts are provisional.
- [**`worked-example/test-2-refusals-and-silences.md`**](worked-example/test-2-refusals-and-silences.md) - whether one sentence keeps a plain refusal apart from a non-answer, scored against a rule fixed before the run. It does.
- [**`worked-example/ledger.csv`**](worked-example/ledger.csv) - all 142 findings, each with its clause, category, commitment key, verbatim quote and any condition or exception.
- [**`worked-example/run-output.md`**](worked-example/run-output.md) - the full run: the checklist marks, the relief list, the check of the AI review, the four readings, the difference pass, the clarification letter, the schedule of commitments, and the register with the pre-mortem behind its odds.
- [**`worked-example/verify_ledger.py`**](worked-example/verify_ledger.py) - rebuilds the ledger and checks every quote and every count.
- [**`assets/`**](assets) - the cover card and the review-against-bid image from the LinkedIn edition, with the image's HTML source.

## How to run it

1. Install `/vendor-review`. In Claude Cowork, add the Operations plugin from claude.com/plugins. In Claude Code:

```
claude plugin marketplace add anthropics/knowledge-work-plugins
claude plugin install operations@knowledge-work-plugins
```

   Checked on 29 September 2026 against version 1.3.0. Anthropic can change it.
2. Read the worked example: `worked-example/vendor-review-run.md` is the review, and `worked-example/run-output.md` shows what each stage of the Sourcing Read adds to it.
3. Check it yourself:

```
cd worked-example
python verify_ledger.py
```

The script checks **quotation accuracy and arithmetic**: each of the 142 finding quotes, each recorded condition or exception, and each quote behind the checklist marks, the relief list, both checks of the AI review, the clarification letter, the register and its pre-mortem appears word for word where it is cited, and every count is computed rather than typed. If a quote were invented, it would stop and say which.

**It does not check whether a finding or a mark is right, or whether anything was missed.** A quote can be accurate and the reading incomplete. That review is yours, and the `condition_or_exception` column shows where the exceptions sit.

4. On your own tender: run `/vendor-review`, then `sourcing-read.skill.md`. Start with your own request, before any bid.

## Before you use it on a real tender

Bid documents contain supplier pricing your own request probably obliges you to keep confidential, and usually named CVs, which are personal data. **Use the environment your organisation has approved for that material.** If you are not sure one exists, run the read on the worked example first, and ask.

## What it does not do

It does not rank, price or recommend a supplier. It does not replace your procurement process or the people who run it; it is something to bring to them. It cannot tell you the losing bids were worse. It does not tell you to stay or walk. It does not decide what is enforceable.

The short prompt checks the review's claims. It will not look for a requirement that neither the review nor any bid mentions, and it can compare against your request only if you give it the request with the bids. Stages 1 and 2 start from your request for that reason.

## Change four things to make it yours

The unit of service in your category. What a supplier there would be most relieved you did not ask. The standard conditions that govern your trade. Which records you actually control.

---

*Issue 8 of So What, Now What · CC-BY 4.0 · Arguments and voice are mine. Claude is used as an editing and scaffolding tool. Others' concepts are referenced in [SOURCES.md](SOURCES.md).*
