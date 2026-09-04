# Run v4, 4 September 2026 — the same document, five days later

Same vendor sheet as `run-v3/`, same ten cells, same three makers. Run again for one reason: the
answers in v3 were collected before the `if_true` field existed, so scoring them cannot show the
part of the output that matters most. This run can.

```
python3 ../independence_test.py --answers cells.json
```

## What changed, and it is not small

|                              | run-v3, 30 Aug | run-v4, 4 Sep |
|------------------------------|----------------|---------------|
| mean agreement               | 0.289          | **0.406**     |
| effective opinions from nine | 2.72           | **2.12**      |
| noise floor, one model twice | 0.321          | **0.75**      |
| distinct problems            | 21             | **13**        |
| raised by one check only     | 10             | **3**         |

**The panel converged.** Five days apart, on an identical document and identical prompts, the nine
checks agreed with each other far more and found four fewer fifths of the problems. Nine checks are
now worth 2.12 opinions rather than 2.72.

**The most likely cause is us, and it is worth more than the finding would have been.**

Memory and personalisation were **on** in every account for every run. Isolation is instructed
inside each block and nothing more; the run sheet has always said that an instruction asks a model
not to retrieve while the setting stops it. On 30 August that cost nothing, because run-v3 was the
first time any of these accounts had seen this document. The 29 August void run tested the
newsletter article, not the vendor sheet.

**Run v4 is the second time.** Same document, same three accounts, five days later, memory on. The
number that moved furthest is the one recall would move first: the noise floor, one model asked the
same thing twice, went from 0.321 to 0.75. A model that remembers what it said last week agrees
with itself for a reason that has nothing to do with independence.

So there are three candidates and this kit cannot separate them:

1. **Recall.** The models had seen the document, and memory was on. Leading candidate, because it
   explains the noise floor directly.
2. **The models changed.** The direction matches Kim, Garg, Peng and Garg (ICML 2025), who find
   that larger and more accurate models have the most correlated errors.
3. **30 August was a lucky draw.** One document, one run, either way.

**Take the lesson rather than the number.** If you run the same document twice, turn memory and
personalisation off, or use accounts that have not seen it. Otherwise your second run measures
what the model remembers, and it will look more converged than it is. That failure runs in the
direction that flatters nothing: it makes your panel look worse than it is, so you throw away
checks that were actually working.

## The result that is worth your attention

**Eight findings change the decision. None of them was raised by only one check.**

In `run-v3` ten of twenty-one problems came from a single check. Here the decisive findings are
unanimous or near it: every check found the arithmetic error in the section 3 totals, the weights
set after the demonstrations, and the cultural-fit reversal. The cross of decisive-and-solo, which
this kit calls the point of the exercise, is **empty on this run**.

That is not a failure of the method. It is what the method is for. A document with three unmissable
errors does not need nine checks to find them, and the tool says so instead of manufacturing a
list. Run it on a subtler document and the cross fills up.

## What is here

- **`cells.json`** — the ten answers as returned, every criticism carrying `if_true`.
- The document, the sealed human baseline and the run sheet are in `run-v3/`, unchanged. This run
  used the same ones.

## Provenance, stated because it should be

Cells B and C were pasted into Gemini and ChatGPT by hand, one brand-new chat each. Cells A were run
twice: first through isolated agent contexts, then again by hand in fresh Claude chats after we
suspected the agent route was inflating self-agreement. **It was not.** Both routes returned a noise
floor of 0.75 and n_eff within 0.12 of each other. The hand-run cells are the ones shipped here.

---

The measure here belongs to survey statistics and the findings it rests on are other people's; both are cited in the sources above. What is mine is the assembly, the run, and the reading of it.

Arguments and voice are mine. Claude is used as an editing and scaffolding tool. If others' concepts are used, they are referenced in the sources section.
