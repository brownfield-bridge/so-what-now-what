# Build notes

**The receipts, including the things that went wrong.** Nothing here is in the issue; it is all here because someone checking the issue would want it.

---

## What each build cost

| | When | How | Passes |
|---|---|---|---|
| **Build 1** | Tue 15 Sep | one sentence, one sitting, no follow-up | 1 |
| **Build 2** | Tue 15 Sep | [the build prompt](the-build-prompt.md), one sitting | 1, then 4 rounds of corrections |

**Do not judge the two on polish.** Build 2 got four more rounds and build 1 got none. Everything build 2 refuses was in its first output, before any of that - the later rounds were numbers and wording. The asymmetry is the point rather than a flaw in it: **there was a document to check build 2 against, so there was something to fix. Build 1 could only be made prettier.**

---

## ⚠ The measurement the issue rests on

Build 1's electricity price is pre-filled at €0.29/kWh, unsourced, and sits inside a collapsed panel headed *Fine print (optional)*.

Holding everything else fixed - washing machine, 7 years old, €130 to repair, €449 new - and moving only that one number:

| Electricity price | Verdict | Repair | New | Walk-away |
|---|---|---|---|---|
| €0.00 | **Repair it** | €43/yr | €45/yr | €135 |
| €0.10 | **Line ball** | €61/yr | €60/yr | €125 |
| **€0.29 (the default)** | **Replace it** | €96/yr | €88/yr | **€107** |
| €0.40 | Replace it | €116/yr | €105/yr | €97 |
| €0.60 | Replace it | €152/yr | €135/yr | €78 |

**One unsourced number, hidden behind a disclosure triangle, swings the verdict from repair to replace and moves the walk-away price by forty per cent.**

Two further things fell out of testing it:

**The field cannot be reached by script until the panel is forced open** - a browser automation refuses it as *not visible*. The most load-bearing input in the tool is hidden by default.

**The currency menu eats the user's own figure.** Type `0.42`, switch currency, and the field silently becomes `0.27`. A real number off a real bill, overwritten by an invented one.

**In fairness to build 1:** the field does say *"off your bill, all charges in"*, so it asks for the reader's real figure. Seeded with an invention, but correctable - which is more than the lifespan constants ever offer.

---

## ⚠ A contaminated run that had to be killed

The build prompt was first given to a coding agent connected to the newsletter's own repository. Its first move, before engaging with the instructions at all:

> *"I'll start by getting oriented in the repo."*
> *"There's an existing single-page tool in this repo. Let me study the house conventions."*

**It had found the earlier build and was about to copy it.** The run was stopped and restarted somewhere with nothing in it.

**The lesson is not "write a better instruction."** No line inside the prompt could have caught this, because the agent looked around before it read properly. Only an empty context prevents it.

And there is a finding in it worth more than the inconvenience: **what is lying around beats both a one-liner and a careful prompt.** The comparison in this issue only means anything because the second run had nothing to copy from.

*This was the second contamination of the weekend. The first was an earlier build reading a notes file left one directory above its working folder.*

---

## Things still wrong, or unfinished

**No baseline.** Both instruments are comparisons and nobody took the "before" reading. Recoverable by measuring, not by building. Not done.

**No customer contact.** Provenance is LIVED - the author has faced this decision on his own appliances. Nobody outside the room has said the promise sentence out loud. One phone call to one repair business moves it to HEARD and takes half an hour. It was not made.

**The follow-on figure is a point estimate.** An earlier build carried confidence intervals; build 2 states *"24 of 54 came back"* as a count and lists the cases. That is a deliberate choice for legibility, not an oversight, and it is a regression against the earlier build.

**The twelve-month column can never fill from the reader.** Build 2 asks what you decided and what it cost, and then says plainly that it will never learn whether your repair held - because it has chosen not to hold anything that could reach you in a year. That is the promise's own contradiction, rendered on screen instead of hidden.

---

## Reproducing any of this

Both builds are single HTML files with no backend, no build step and no dependencies beyond two webfonts. Open them in a browser.

- [builds/01-from-one-line.html](builds/01-from-one-line.html)
- [builds/02-from-the-prompt.html](builds/02-from-the-prompt.html)

The demonstration records in build 2 are generated from a fixed seed, so the numbers quoted in the issue and in these notes come out the same way every time.
