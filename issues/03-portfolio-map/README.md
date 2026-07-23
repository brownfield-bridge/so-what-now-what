# The AI Portfolio Map
**Run it now in your browser:** https://brownfield-bridge.github.io/so-what-now-what/issues/03-portfolio-map/tool/

*Companion kit for* ***So What, Now What*** *- Issue 03: "Your AI pilots are not necessarily wrong. Your org chart might be."*

Maybe you have a dozen AI initiatives running. Maybe two quiet experiments and pressure to show more. Maybe just a budget and a decision about where to place the first real bet. Whichever you are, the same trap applies: the tools get bought, the pilots report success, the invoices are paid, and the company still runs the way it ran two years ago. The cause is rarely the technology and rarely your people. It is the shape of the decisions: AI is being decided the way IT gets decided, and IT decisions do not transform the business. This kit gives you the test that separates the two shapes, and a map that runs your whole portfolio through it in about half an hour. It works on the initiatives you already run and the ones you have not yet started.

License: CC-BY 4.0. Use it, adapt it, ship it inside your own work. A credit back to *So What, Now What* is appreciated, not required.

## The test

An AI decision is **IT-shaped** if it can succeed end to end without changing anyone's job: budget approved, vendor selected, rollout completed, everyone works as before. IT-shaped decisions produce pilots.

An AI decision is **org-design-shaped** only when it answers four questions:

1. **Owner** - a named *business* owner whose own number moves when this works, not a systems owner and not nobody.
2. **Process (and the skill it demands)** - a named way of working changes when it succeeds, and it demands a new skill someone actually builds. If nothing changes, it is a purchase. Literacy training on its own does not count; the skill has to be bolted to a changed process.
3. **Autonomy boundary** - you have decided what the system may do alone and what needs sign-off.
4. **Own success test** - you judge it on a test you wrote, not the vendor's benchmark.

Org-design decisions produce operating change. Most portfolios lean heavily to the first shape, which is why they produce mostly pilots. The column that stays empty tells you which decision was never made.

The same test runs *before* you spend. Ask the four questions of a bet you are only weighing, and if the honest answers are just budget, vendor and rollout, you already know it is heading toward a pilot, so you can reshape it before the money moves.

## What's here

- **`tool/index.html`** - the fastest way in. A self-contained web tool: enter your initiatives (the live ones and the ones you are only weighing), answer the four questions on each, and it classifies every one, names the missing decision, flags the single live initiative with the widest gap between spend and change, lists any not-yet-started bets under "Before you fund", and writes a forwardable memo. No install, nothing stored, nothing leaves your browser. Open the file, or use the hosted version linked in the issue.
- **`diagnostic-prompt.txt`** - the no-tool floor. Paste it into any AI, list your initiatives, and it runs the same interrogation in your own chat window.
- **`portfolio-diagnostic.skill.md`** - the same diagnostic as an installable skill for Claude or Cowork, so you can re-run it and have it write the memo for you.
- **`examples/portfolio-map-worked-example.csv`** - a full worked portfolio (five live initiatives, two of which turn out to be theater, plus one bet still being weighed), so you see the whole thing before you replace it with your own.
- **`examples/portfolio-map-template.csv`** - the blank map with the columns and one example row, if you would rather work in a spreadsheet.
- **`README.md`** - the method in plain words.

## How to run it

Three rungs. Use the one that fits you.

- **Fastest:** open `tool/index.html` (or the hosted link in the issue), edit the worked example or clear it, and enter your own initiatives. Copy the memo or save the page as a PDF when you are done.
- **In your own chat window:** paste `diagnostic-prompt.txt`, list your initiatives, and let the model push back on your classifications.
- **In Claude or Cowork:** add `portfolio-diagnostic.skill.md` as a skill and say "run the portfolio diagnostic." It runs the interrogation one initiative at a time and writes the memo.

However you run it, the output is the same: your real AI strategy on one page, and the one initiative to reframe this week.

## The worked example

The included portfolio is a fictional mid-market distribution and services group, one COO seat. Five live initiatives: two IT choices, one org-shaped on paper but stuck on a missing autonomy boundary, and two theater. The customer-service copilot is IT-shaped: live for eight months, satisfaction flat, because no queue, script, or staffing changed around it. The demand-forecast model looks org-shaped but the planner quietly reruns everything by hand, so the missing decision is the autonomy boundary. A sixth row is a bet the group is still weighing (a contract-review assistant with budget earmarked but no owner), which the map treats as "before you fund" rather than "this week". It is deliberately pan-industry; swap in your own seat.

## The now-what

Pick the one initiative with the widest gap between what it costs and what it has changed, and reframe it this week: name a business owner, define what it may do alone, and write three test tasks of your own. One initiative, one week. The map tells you the next one.

## Why this works

Business theory settled the underlying point in 1962, when Alfred Chandler showed that structure follows strategy. The AI version is blunter: if the structure does not change, the strategy was a purchase. And the numbers now say the same thing. BCG's work across hundreds of companies finds that only about 10 percent of AI's value comes from the algorithms and 20 percent from the technology; the remaining 70 percent comes from rethinking the people, roles, and workflows around the tools. McKinsey, testing 25 things companies do with AI against actual profit, found that redesigning workflows had the biggest effect on the bottom line, yet only about a fifth of companies have fundamentally redesigned any. The constraint is how you organize, not which model you buy. The reclassification is a working session, and this kit is the instrument.

This connects to the two issues before it. **Issue 01** stress-tests the decision (is it robust across futures?). **Issue 02** builds the context base the decision runs on (the knowledge your AI reasons over). **Issue 03** is about the shape of the decision itself. Stress-test the call, give it a substrate, then make sure it is a decision and not a purchase.

## Sources

- The 10-20-70 value split (about 10% of AI's value from algorithms, 20% from enabling technology, 70% from the people/workforce component), the ~5% of firms reaching substantial gains, and the 50%-versus-20% upskilling figures are BCG, "AI Transformation Is a Workforce Transformation" (Julie Bedard and Vinciane Beauchene, February 2026).
- "Workflow redesign has the biggest effect on EBIT impact from gen AI" (of 25 attributes tested) and the ~21% that have fundamentally redesigned any workflows are from McKinsey, "The State of AI: How Organizations Are Rewiring to Capture Value" (QuantumBlack / AI by McKinsey, March 2025).
- The work-redesign point is Jacqui Canney, ServiceNow's chief people officer, on the MIT Sloan Management Review podcast Me, Myself, and AI ("Disintegrating the Org Chart", April 2026).
- "Structure follows strategy" is Alfred Chandler, *Strategy and Structure* (1962).

---

*The AI Portfolio Map · So What, Now What, Issue 03 · github.com/brownfield-bridge/so-what-now-what · CC-BY 4.0*
