# So-What / Now-What synthesizer

This project runs a weekly synthesis on the week's AI and strategy signals, filtered to one reader's relevance window and scored for materiality. It turns a flood of newsletters and headlines into one short brief with named decisions.

The discipline comes from Issue 0 of *So What, Now What* (github.com/brownfield-bridge/so-what-now-what). The animating rule: the reader sets the filter and makes the decision. This tool gathers and scores. It never decides.

## The reader's relevance window

The window lives in `relevance-window.md`. Read it at the start of every run. It defines the domain (3 to 5 watch areas), the function (the reader's role), and the decision horizon. Everything is filtered and scored against it. If the window file is missing or still has placeholder text, stop and say so rather than guessing.

## How a run works

When asked to synthesize (or when `/synthesize` is invoked):

1. Read `relevance-window.md`.
2. Gather 8 to 15 distinct signals from the last 7 calendar days:
   - From the web: the most significant developments across the domain areas, with publisher, link, and date. Prefer primary sources over coverage of them.
   - From the mailbox, if a mailbox MCP is connected: every newsletter, briefing, and alert from the last 7 days. One distinct story is one signal, not one email.
   - Merge both streams, collapse duplicates, tag each `[web]`, `[inbox]`, or `[both]`.
3. Drop signals outside the window. Send to Monitor any whose first material impact falls outside the horizon.
4. Score each remaining signal 1 to 5 on Speed, Scope, and Reversibility (cost of waiting). Total out of 15.
5. Brief at most the top 5 that clear 9 of 15. Demote the rest to Monitor.
6. For each brief-worthy signal write a So What (one sentence true only for this business; mark inferences with "(assumes ...)") and a Now What (one concrete move inside the horizon).
7. Write the brief to `briefs/YYYY-MM-DD-brief.md`.

## Output shape

- A 3-line headline summary.
- A table: `Signal (tagged + linked) | Score | So What | Now What`.
- A Monitor list, each item with the trigger that would promote it to a future brief.

## Rules that do not bend

- "This week" means the last 7 calendar days. Ignore older items even if unread, and do not treat a standing future deadline as a new signal unless it changed this week.
- Cite the primary source: the regulator, company, or lab's own page, or the original announcement. Do not pass off a vendor blog, an SEO roundup, or secondary coverage as the source; if only secondary coverage exists, link the best one and tag the signal [unverified].
- Confirm every link resolves to a real page before including it; if you cannot, drop the link and mark the item [unverified] rather than guess a URL.
- If a figure comes from a single source or a vendor, try one corroborating source before flagging it unverified.
- No generic So Whats. If a sentence could be true for any company, rewrite it until only this reader could have written it.
- If you cannot name a concrete Now What, demote the signal to Monitor.
- Never invent a signal, figure, or source to fill the set. If the week was quiet, a short brief is the correct answer.
- If web access or the mailbox is unavailable, say so and proceed with whatever source you have.
- The brief is one page, not a digest. Do not send it anywhere; only write the file.
