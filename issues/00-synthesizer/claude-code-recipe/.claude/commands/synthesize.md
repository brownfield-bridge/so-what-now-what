---
description: Build this week's So-What / Now-What brief from the reader's relevance window
allowed-tools: WebSearch, Read, Write
---

Build a So-What / Now-What synthesis for this week, following the discipline in `CLAUDE.md`.

Steps:

1. Read `relevance-window.md`. If it is missing or still contains placeholder text in brackets, stop and tell me to fill it in first.

2. Gather 8 to 15 distinct signals from the last 7 calendar days:
   - From the web: the most significant developments across my domain areas, each with publisher, working link, and date. Prefer the primary source (regulator, company, lab) over secondary coverage.
   - From my mailbox, only if a mailbox MCP is connected: newsletters, briefings, and alerts from the last 7 days. One distinct story is one signal, not one email.
   - Merge both streams, collapse duplicates (same story, keep the stronger source), and tag each `[web]`, `[inbox]`, or `[both]`.

3. Drop signals outside my relevance window. Send to a Monitor list any signal whose first material impact falls outside my decision horizon.

4. Score each remaining signal 1 to 5 on three axes: Speed (how fast it hits operations, budget, or mandate), Scope (how broad across functions and units), Reversibility (how expensive it is to wait). Total out of 15.

5. Brief at most the top 5 that clear 9 of 15. Demote the rest to Monitor.

6. For each brief-worthy signal, write:
   - So What: one sentence true only for my business. Use only the context in the window. Mark any inference with "(assumes ...)".
   - Now What: one concrete move I can start within my horizon.

7. Write the result to `briefs/YYYY-MM-DD-brief.md` using today's date, with this shape:
   - A 3-line headline summary at the top.
   - A table: `Signal (tagged + linked) | Score | So What | Now What`.
   - A Monitor list at the bottom, each item with the trigger that would promote it.
Rules: "this week" is the last 7 calendar days, and a standing future deadline is not a new signal unless it changed this week; cite the primary source (regulator, company, or lab's own page), not a vendor blog or secondary coverage, and tag [unverified] if only secondary exists; confirm every link resolves to a real page or drop it and mark [unverified] rather than guess a URL; corroborate single-source or vendor figures once; no generic So Whats; demote anything without a concrete Now What; never invent a signal, figure, or source to fill the set; one page, not a digest. Write the file only. Do not send it anywhere.

After writing, tell me the filename and a one-line summary of what cleared the threshold.
