# Run v5, 4 September 2026 — memory off. Four cells, one question.

Not a full run. Four cells, asked to settle one thing: was the convergence in `run-v4/` caused by
the models remembering the document, or is it real?

Every chat was private. Claude incognito, Gemini Temporary Chat, ChatGPT Temporary Chat with
personalisation off. None of them reads saved memory, none writes to it, and no account setting was
changed to get there.

```
python3 ../independence_test.py --answers cells.json
```

## The answer is no, and it is the wrong way round

| same model asked twice          | v3, 30 Aug | v4, 4 Sep | v5, 4 Sep |
|---------------------------------|------------|-----------|-----------|
| memory                          | on         | on        | **off**   |
| had the account seen the doc?   | no         | yes       | yes       |
| **it agreed with itself**       | 0.321      | 0.75      | **1.00**  |
| second verdict                  | differed   | matched   | matched   |

**With memory off it agreed with itself perfectly.** Five criticisms, same five targets, same
verdict. If recall were driving the convergence, switching memory off should have pushed that number
down. It went up.

Three checks, one question each, like for like across all three runs:

| | v3 | v4 | v5 |
|---|---|---|---|
| mean agreement | 0.209 | 0.316 | **0.42** |
| effective opinions from three | 2.12 | 1.84 | **1.63** |

The line runs one way, and the cleanest run of the three is the least independent.

## What we now think, and what we are not claiming

**Recall is out.** It was the leading candidate in `run-v4/README.md` and this run removes it.

**What is left is that these models genuinely agree about this document**, and that 30 August was
the outlier rather than the norm. Two readings survive and four cells cannot separate them: the
models changed between 30 August and 4 September, or run-v3 drew an unusually loose sample and the
later runs are closer to the truth.

**This is three runs of one document.** It is not a trend, and we are not going to call it one.

## What it does to the method, which is the part that matters

Nothing, and it sharpens why the repeat step exists. A floor of 1.00 is not a failure. It says the
model is deterministic on this document, so **every scrap of spread in your panel came from the
crossing and none of it from randomness**. A floor of 0.32, which is what v3 returned, says the
opposite: much of what looks like independence is one model being inconsistent.

Both readings are useful and you cannot know which you have without running the repeat. That is the
whole argument for the step, and it is stronger after this run than before it.

**One caveat for readers of Issue 6.** The newsletter reports run-v3, where the repeat returned a
different verdict the second time. In v4 and v5 it did not. Take the floor as a number to read, not
as a behaviour to expect.

---

The measure here belongs to survey statistics and the findings it rests on are other people's; both are cited in the sources above. What is mine is the assembly, the run, and the reading of it.

Arguments and voice are mine. Claude is used as an editing and scaffolding tool. If others' concepts are used, they are referenced in the sources section.
