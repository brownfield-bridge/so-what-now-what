# PROMISE BRIEF — repair or replace. **BUILD 3.**

**Supersedes `the-long-way-round/the-first-brief.md` for building purposes. Everything not restated below carries forward from it unchanged.**

    written:   2026-09-15
    input:     the interview (9 Sep) · build 1 (11 Sep) · the second-model pass (14 Sep)
               · the open-field build (15 Sep, one line, no brief)
    method:    the open build was read, its findings scored, and each one either taken,
               re-shaped, or refused with the rule that refused it named.
    status:    5 of 6. Up one from build 1, and the field that moved is stated below.

---

## 0. WHY THERE IS A BUILD 3

The brief was written first and built second. That was the wrong order, and we found out by accident: a one-line prompt, run on the same problem with no brief at all, produced eight things this document did not contain.

**This build is the brief rewritten from what the unbriefed build revealed.** Four takes, three refusals, and one correction to a section of the old brief that had gone stale.

**The selection is the point.** A brief that took all eight would not be a brief, it would be a wishlist. What follows is the instrument doing its job on material it did not produce.

---

## 1. CORRECTION — the old Part 8 is dead

The superseded brief, Part 8, reads:

> *"Business model, decided upstream: commission on every completed job, repair or replace, so the tool earns the same either way."*

**That is no longer true and it was the fourth defect.** Commission on completed jobs requires a step this brief rules out, so as written the honest answer arrived and nobody was ever paid. The model that replaced it, after three rejected designs:

> **Repair shops and retailers each pay a flat fee to be listed. Nothing per answer, per referral or per completed job.** Revenue is decoupled from the verdict, so the tool can say it does not know as often as the data requires and it costs nothing.

**Part 4's closing line changes with it.** "The commission is answer-neutral by design" becomes: **the fee does not move with the answer, so there is no commission to be neutral about.**

---

## 2. ⚠ DEFECT 5 — found this afternoon, before this build rather than after

Checking the new takes against the money exposed a flaw in how the money was tested.

The test that killed three business models was **a refusal must not cost revenue.** All four takes pass it. But running cost, once added, systematically shifts the verdict mix toward replace - a new machine is more efficient than an old one in every class. The fee stays flat. **What each side gets for it does not.** Retailers gain, repairers lose, and repairers churn off at renewal.

> **We proved the money cannot bend the verdict. We never checked whether the verdict bends the money. It does - not through the price, through who stays.**

**The rule is replaced:** *no verdict may change what any party pays **or who stays**.*

Under the new rule the flat fee still passes on price and is **watched on retention**. Repairer churn against verdict mix is recorded as a thing to measure, not a thing solved. It is not solved here and this brief does not pretend otherwise.

---

## 3. THE FOUR TAKES, RE-SHAPED

### 3.1 The walk-away price — TAKEN, re-framed as a stop-loss

*"Pay no more than X to fix it."* Computed from our own records and the user's own rule. Revenue-neutral under a flat fee.

⚠ **But a published ceiling is an anchor.** A repairer who would have quoted €90, seeing the tool tell the customer "up to €280", has been handed a reason to quote €280. That works against the promise.

**Three conditions, all of them build requirements:**

1. **It appears only after the user has entered their quote.** Never before. It cannot be read as a price guide if it cannot be seen until the price exists.
2. **It is framed as a stop-loss during the job, not a fair price before it.** The case it exists for is the engineer opening the machine and finding more. On screen: *"If the total passes this while the job is open, stop there."*
3. **The screen says what it is not:** *"This is not an estimate of what the repair should cost."*

### 3.2 Running cost — TAKEN AS AN UNKNOWN, not as a term in the verdict

The open build added electricity to both sides. It is the most valuable thing it found and **we cannot compute it.**

To get the difference you need what the old machine actually draws now. Nobody has that. The open build solved it by assuming every machine draws 3% more per year of age. **That constant is invented, and it is a claim about how products behave - must-not 6, squarely.**

**So the take is the honest half:**

- The declared energy figure for a **new machine of this class** is displayed, marked as declared under the regulated test, never aged and never blended into the verdict. Admissible on the same footing as a published price: a fact about what was declared, not a claim about what happens in a kitchen.
- **What the old machine draws is shown as unknown**, because it is, with the two ways the user can find out: the machine's own label, or a plug meter.
- ⚠ **Bound to the appliance class and the make. Never the model.** Our records stop at the make. Claiming per-model precision is defect 2, committed a second time after we found it.

**This is the take that keeps Dependency at YES.** The verdict stands on nothing anybody else owns. A displayed declared figure is context, not a dependency.

### 3.3 Currency — TAKEN, and the naive fix rejected

The open build made currency a dropdown. That lets a householder pick złoty against a job history priced in euro: it looks like localisation and is a unit error.

> **Currency follows the record set, not the user's preference. Displayed, stated, never chosen.**

This is the proper fix for defect 3. The old brief papered it with a sentence in Part 1; a control would have papered it with a widget. The data has a currency and the screen reports it.

### 3.4 The householder's own horizon — TAKEN as is

*"We are moving, or replacing the kitchen, within two years."* The reader's own circumstance, not a claim about the machine. It shortens the horizon the repair has to cover and pushes toward the cheap fix.

Clean under every must-not, and a mild counterweight to the retention effect in §2, since it leans toward the repairer.

---

## 4. THE THREE REFUSALS, AND WHAT REFUSED THEM

Recorded as refusals, in the brief, so the build does not quietly re-add them.

| Refused | The rule | Why it is not negotiable |
|---|---|---|
| **Sixteen appliance types** with per-type lifespans | Q9, smallest version worth having | Scope discipline is what got Dependency to YES. Buying the breadth costs the field |
| **Asserted lifespans and kWh constants** - "washing machine, 10 years, 150 kWh" | Must-not 6 | Unsourced claims about how products behave. Same failure as the supplier tool's invented weights, better dressed |
| **The diagnostic checklist** - *"brushes and belts are cheap, drum bearings are not"* | Must-not 6 | Claims about how products behave. **This is the one that hurts** - it is the most customer-useful thing the open build produced, and it tries to stop the user paying for a call-out at all |

### 4.1 But the checklist splits, and half of it is admissible

Claims about **machines** are barred. Questions about **the transaction** are not. So the checklist is refused and this replaces it:

> **Before you agree to the job, ask the repairer:** is the call-out fee credited against the repair; does the repair carry twelve months on parts and labour; is the part still manufactured, or is this a salvaged one.

Process, not product behaviour. Admissible, useful, and it survives must-not 6 intact.

---

## 5. THE TWO FIELDS THAT WERE AT RISK, RESOLVED

### 5.1 Instrument — held at YES by adding one

The walk-away price is a fourth output and had nothing measuring it. Rather than publish it unmeasured:

> **Third instrument: the share of completed jobs that finished at or under the walk-away line.**

The intake gate already collects the quote and the decision. It now also collects **the final amount paid**, which passes must-not 5 because it is a field computed on - it measures the stop-loss and it feeds the cost records the next user gets.

⚠ **Stated weakness: this one is self-reported.** We are not in the kitchen when the engineer opens the machine. Weaker evidence than the other two instruments and labelled as such.

⚠ **Its baseline is missing too**, on the same terms as §5.2: the share of jobs that currently overrun their quote. Recoverable from the same repairer records, and not recovered here.

### 5.2 Dependency — held at YES by §3.2

Running cost enters as a displayed declared figure and an explicit unknown, never as a term in the verdict. Nothing the verdict stands on is owned by anybody else.

**Had we taken running cost the way the open build did, this field would have gone to NO and the score to 3 of 6.** The single most attractive idea in the open build was the one that would have cost the most.

---

## 6. THE SCORE

| # | Field | Build 1 | Build 3 |
|---|---|---|---|
| 1 | Horizon | YES | **YES** - unchanged |
| 2 | Scope | YES | **YES** - held by refusing the sixteen types |
| 3 | Instrument | YES | **YES** - three now, the third self-reported and labelled |
| 4 | Party | SPLIT | **YES** - see below |
| 5 | Baseline | NO | **NO** - still missing, now missing in two places |
| 6 | Dependency | YES | **YES** - held by §3.2, and it was close |

### 5 of 6.

**Party moves, and not because anybody was persuaded.** Horizon A was always checkable by anyone with a machine and a quote; the field was empty because nobody had been *asked*. The kit ships the brief and the build together, so the checking party at Horizon A is **any reader who runs the five faults and tries to break it**, and the empty field becomes an open invitation with a date on it. Horizon B is checked by users through the intake gate, as before.

**Baseline stays NO and is now worse than it was**, because §5.1 added a second instrument with a second missing baseline. Both are recoverable, neither is recovered, and both ship as gaps.

*A commitment with no date, no scope and no instrument is not a commitment. It is a mood.*

---

## 7. WHAT THE OPEN FIELD CHANGED — the record

1. **A better decision frame we did not take whole.** Cost per year of service on both sides is the right question and half of it is uncomputable without inventing a constant. We took the half we can stand on.
2. **The walk-away price**, which is the most useful single output in either build and came from the one with no brief.
3. **Defect 3 fixed properly**, by the build that did not have it.
4. **Defect 5 found**, because the takes were checked against the money before the build rather than after.
5. **Part 8 corrected**, four days late.
6. **One field gained, five refusals or re-shapings made.** The brief cost scope and a decision frame. It bought refusals, sourcing and a score. Both halves of that are true and the issue says so.

---

## 8. STILL DELIBERATELY NOT SPECIFIED

Unchanged from build 1: how confidence is expressed, what the thin-data screen shows beyond saying it is thin, whether reasoning is inline or on request, and interaction, layout and flow throughout.

**Added:** how the unknown old-machine energy draw is presented. It must be visible and it must not look like a missing number the user failed to supply.

---

## 9. PRE-REGISTRATION FOR THIS BUILD

Fixed before the build runs, on the same terms as the 15 September run.

**Build 3 succeeds only if, against build 2 (the open-field build):**

1. The walk-away price appears **after** the quote, framed as a stop-loss, with the disclaimer on screen.
2. Old-machine energy draw is **shown as unknown** rather than estimated.
3. Currency is **reported from the data**, not chosen.
4. None of the three refusals reappears.
5. The thin-data refusal and the safety stop survive intact from build 1.

**If build 3 is not visibly better than build 2 on these five, the method claim fails and Issue 7 publishes that instead.**

n = 1 throughout. One domain, one weekend, three artefacts. This shows what happened once.
