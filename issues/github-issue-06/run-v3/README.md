# Run v3, 30 August 2026 — the run the newsletter cites

This is the run behind every one of our own figures in Issue 6. It is here so you can reproduce
them rather than take them on trust.

```
python3 ../independence_test.py --answers cells.json
```

That returns **2.72** effective opinions from nine checks, mean agreement **0.289**, a noise floor of
**0.321** (n_eff **2.52** if every check were the repeat), **21** distinct problems and **10** of them
raised by a single check. The subset figures the newsletter quotes come from the same file: three
makers asked one question each gives **2.12**, one maker asked three questions gives **1.92**.

## What is here

- **`cells.json`** — the ten answers exactly as the models returned them. Nine checks plus one repeat.
- **`vendor-sheet.md`** — the document under test. A vendor recommendation memo going to an investment
  committee. Made up for this, on purpose: testing the newsletter on itself would have let anyone say
  the document was chosen to flatter the method.
- **`reviewer-baseline-SEALED.md`** — the ten problems a human found, written and sealed *before* any
  model saw the document. This is what the panel is scored against.
- **`run-sheet-v3.md`** — how the run was set up, including the three rules and what is weaker here
  than it should be.
- **`score.py`, `result-lexical.json`** — the scoring used on the day and its output.

## What this run is not

One document, one run, one afternoon. Every figure from it is indicative. The panel found six of the
ten sealed problems and added one nobody had, and the two it missed are the two that most needed a
person.

---

The measure here belongs to survey statistics and the findings it rests on are other people's; both are cited in the sources above. What is mine is the assembly, the run, and the reading of it.

Arguments and voice are mine. Claude is used as an editing and scaffolding tool. If others' concepts are used, they are referenced in the sources section.
