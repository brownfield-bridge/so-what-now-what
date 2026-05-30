# The So-What / Now-What Synthesizer

A paste-and-run prompt for executives who decide more than they read.

Ships with Issue 0 of *So What, Now What*. Read the issue for the framework, the worked example, and the agency frame: [so-what-now-what.beehiiv.com](https://so-what-now-what.beehiiv.com).

## How to use

1. Replace the bracketed placeholders in `MY RELEVANCE WINDOW` with your own values.
2. Paste this week's signals (10 to 30 items) into `THIS WEEK'S SIGNALS`.
3. Run in Claude, GPT, or Gemini.
4. The output is your first weekly brief.

## The prompt

```
I need a So-What / Now-What synthesis on this week's signals,
filtered against my relevance window and scored for materiality.

MY RELEVANCE WINDOW
- Domain: [3-5 watch areas, e.g. industrial automation, agentic
  commerce, EU AI regulation, mid-cap industrial M&A, energy
  procurement]
- Function: [my role, e.g. CEO of a 500-person components
  manufacturer]
- Decision horizon: [near 0-3m / mid 3-12m / long 12m+]

THIS WEEK'S SIGNALS
[paste 10-30 signals here: headlines, summaries, links]

YOUR TASK
1. Drop signals outside my relevance window.
2. Score remaining signals on three axes 1 to 5:
   - Speed of impact (how fast does this hit my P&L)
   - Scope of impact (how broad across functions and units)
   - Reversibility cost (how expensive to wait)
3. For signals scoring 9 or higher out of 15, write:
   - So What: one sentence specific to my business, no abstractions
   - Now What: one concrete move available this week or this month
4. Signals scoring below 9 go to Monitor with a one-line note
   on what would push them above threshold.

OUTPUT
- Top: 3-line headline summary
- Body: table with Signal | Score | So What | Now What
- Bottom: Monitor list

CONSTRAINTS
No generic answers. If the So What could apply to any company,
rewrite. If you cannot name a concrete Now What, demote to Monitor.
The brief is one page, not a digest.
```

## Validation discipline

Before relying on this for real decisions, test the prompt on 3 to 5 known scenarios. Confirm: it filters aggressively (most signals demoted to Monitor), the So Whats are specific to the business (not generic), every brief-worthy signal has a concrete Now What.

If most signals fail to demote, the relevance window is too broad. Tighten it.

If the So Whats read generic, the model has too little business context. Add 2-3 sentences about your competitive position, recent decisions, or current operating constraints.

## Boundary condition

The synthesizer works on bounded windows. Diversified holding-company or PE-portfolio operators should run separate windows in parallel per portfolio company, then aggregate manually. One window covering five unrelated businesses produces a digest, not a synthesis.

## License

CC-BY 4.0. Use it, adapt it, ship it. Attribution appreciated.
