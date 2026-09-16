# The one line

Typed into a chat window on Tuesday 15 September 2026. Nothing else given. No attachment, no document, no follow-up turn.

```
Prepare a simple app for the user of house appliance which has broken
after the guarantee period and he needs an advice to replace or to repair.
```

**Reproduced exactly, including the grammar.** It is printed as typed on purpose: a prompt that has been cleaned up is not the prompt anybody actually sends, and the claim this issue makes only holds for the real one.

**What it produced:** [build 1](builds/01-from-one-line.html).

---

## Three things it found that two days of interviewing had missed

**Cost per year of service, on both sides.** The repair spread over the life left in the machine, against a new one spread over its whole life. That is the decision-relevant quantity and the brief had not asked for it.

**Running cost.** On an appliance that runs all day, the electricity can matter more than the repair bill. The brief had not considered it once.

**A walk-away price.** *Pay no more than this to fix it, and if the engineer opens the machine and finds more, stop there.* This is the failure mode that actually happens in a kitchen, and one sentence found it while two days of planning did not.

---

## And four classes of invented number underneath it

None of these came from anywhere. They are not necessarily wrong. They are **asserted** - reasonable-sounding constants with no source, sitting under an answer that reads exactly as confidently as one built on evidence.

| Constant | Value in build 1 |
|---|---|
| Typical appliance life | 10 years for a washing machine, 13 for a fridge, and so on for sixteen types |
| Annual consumption | 150 kWh for a washing machine, 2000 for a water heater |
| Ageing of consumption | 3% more per year of age, capped at twenty years |
| **Price of electricity** | **€0.29 / zł1.10 / £0.27 / $0.17 per kWh** |

**The last one decides the answer, and it is hidden.** It sits inside a collapsed panel headed *Fine print (optional)*, pre-filled. See [build notes](BUILD-NOTES.md) for the measurement: moving that one number alone turns the verdict from repair to replace and shifts the walk-away price by forty per cent.

**It also picks the thresholds.** Above one ratio you replace, below another you repair. Those numbers are hard-coded, invisible, and are the entire verdict. Nobody is asked where their own line sits.

**And it never declines.** Thin evidence, no evidence, an appliance it holds nothing about: always a verdict, never once *I do not know*.

---

**None of that is a complaint about this build.** Every one-line build made during this issue did the same thing, because a model has no way of knowing which wrong answers you can live with. It fills a gap rather than showing you one.

Deciding what it must never do is the part that cannot be delegated, and it is not a technical problem. That is [what the promise is for]().
