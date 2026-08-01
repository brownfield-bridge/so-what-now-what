# Example run — Northwind Components, June MBR
*A real dry-run of `agentic-manager.skill.md` against the sample `sources/` folder, `manager-brief.md`, and `report-template.md`. One trigger; the agent read the four sources, drafted the review, then ran its self-check pass over its own draft. Nothing here was hand-authored as a "gotcha" — this is what the loop produced and caught.*

---

## Part 1 — Sign-off-ready draft (Monthly Business Review, June)

**Revenue.** June revenue $14.2m against plan $14.8m, down 4.1% [01-finance-close]. The shortfall sits in OEM components ($8.6m vs $8.9m plan) [01]. *So what:* the miss is inside the 5% bar and concentrated in OEM phasing, not a broad demand problem (see Backlog).

**Margin.** Gross margin 30.4%, down 2.6 points on plan (33.0%) and 1.6 on May (32.0%) [01]. That is a 7.9% relative miss on plan — over the 5% bar, so it carries an explanation [04]: input costs rose 6% month-on-month (steel +8.3%), and the mix shifted to lower-margin Line C (38% of units vs 29% in May; entry margin 22%) as Line C ran hot (94% utilisation) to clear backlog. *So what:* the margin miss, not the revenue miss, is the month's real story, and it is cost-and-mix driven — largely external.

**Delivery.** On-time delivery 91.2%, down 2.8 points from 94.0% in May [02]. Five orders were late; three trace to supplier X, which is 22% of direct spend and single-sourced on two key alloys [02, 04]. *So what:* supplier-X concentration is now costing delivery — a dual-sourcing review is warranted.

**Backlog / orders.** Committed backlog $9.1m, up from $8.3m in May (+9.6%); new orders $15.0m, book-to-bill 1.06 [03]. *So what:* the order book grew — demand is firm and building.

**The read.** Revenue landed 4.1% under plan while backlog rose and book-to-bill exceeded 1.0 — so the shortfall is OEM timing, not weak demand. Margin fell on input-cost inflation and a deliberate mix shift to clear backlog. Delivery slipped on supplier-X concentration.

**Forward view.** *[Judgment call — for the CFO, not asserted.]* If input costs hold or ease and the Line-C surge unwinds as backlog clears, margin could move back toward plan next quarter. Nothing in the sources fixes forward input costs, so this is the CFO's call to sign or cut.

---

## Part 2 — Self-check pass (the agent's review of its own draft)

**A. Facts vs source — all figures trace; deltas re-derived.**
- Revenue −4.1% (14.2 vs 14.8 = −4.05%) ✓ · Gross margin −2.6pp (30.4 vs 33.0) ✓ · vs May −1.6pp (30.4 vs 32.0) ✓
- On-time delivery −2.8pp (94.0 → 91.2) ✓ · Backlog +$0.8m / +9.6% (8.3 → 9.1) ✓ · Input cost +6.0% (106.0 → 112.4) ✓
- Line C unit share 38% vs 29% May ✓ · Supplier X = 3 of 5 late orders ✓
- **Result: no figure failed against source.** Every number the draft uses is in the folder.

**B. Reads vs data — 1 caught.**
- **First-pass draft said the revenue miss was "softer OEM demand."** The data contradicts it: backlog rose $8.3m → $9.1m and book-to-bill is 1.06. Demand is not soft. **Corrected** to OEM *timing/phasing*, with the backlog cited as the counter-evidence. *(This is the one that would have sent leadership chasing demand instead of phasing.)*

**C. Bar conformance — all five rules met (after the two fixes).**
- Every figure cites its source file ✓ · The one variance over the 5% bar (margin, −7.9% vs plan) carries its explanation ✓ · Every section ends with a "so what" ✓ · Every "why" claim is now backed by a figure ✓ · The forward line is flagged, not asserted ✓ *(see D)*

**D. Forward / high-risk — 1 caught.**
- **First-pass draft asserted "margin will recover next quarter as costs normalise" as fact.** Nothing in the sources supports a forward cost path. **Reworded** as an explicit judgment call routed to the CFO, with the missing basis named (no contracted forward input-cost data in the folder).

**E. Consistency & repetition — first cycle, baseline set.**
- No prior report to compare against yet — this run sets the format the next cycle will be held to (sections, units, definitions). From cycle 2, drop this signed report into `previous/` and the check will hold July to exactly this shape.
- Internal scan: no section restates another, no figure stated twice. Clean.

**F. Decisions surfaced for the human**
1. Confirm the read: OEM **timing + cost/mix**, not soft demand. (One sentence changes what leadership does next.)
2. Keep or cut the forward-recovery line. If kept, it is your forecast, on your name — and it needs a basis the sources don't hold (how much input cost is contracted forward?).
3. Approve opening a **supplier-X dual-sourcing review** (single-source on two alloys + 3 of 5 late orders).
4. Rule on the **Line-C mix shift**: one-month backlog clearance, or a portfolio/pricing question to escalate?

**And the three questions your CFO/board will ask that this draft cannot yet answer:**
- If demand isn't soft, why did OEM miss — phasing, lost share, or price?
- Of the 2.6-point margin miss, how much is input cost vs mix, and which is in our control?
- You say margin recovers — on what basis, and how much input cost is contracted forward?

---

## Bottom line
The agent sourced every figure correctly and got the arithmetic right. What it caught in its **own** first pass was two reasoning errors, not number errors: a confident causal claim the data denies ("soft demand") and a forward statement dressed as fact. Both were exactly the kind of thing a fast read waves through — and both were headed for the board. Two minutes of the CFO's judgment on the four decisions, and this is a review you can stand behind. That gap, between a plausible draft and a checked one, is the whole tool.
