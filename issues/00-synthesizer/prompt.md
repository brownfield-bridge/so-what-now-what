# The So-What / Now-What Synthesizer

A paste-and-run prompt for decision-makers, from this week's noise to your next move.

Ships with Issue 0 of *So What, Now What*. Read the issue for the framework, the worked example, and the agency frame: [so-what-now-what.beehiiv.com](https://so-what-now-what.beehiiv.com).

## How to use

1. Fill in `MY RELEVANCE WINDOW` once. Reuse it every week; only the signals change.
2. Run it in a web-connected Claude, GPT, or Gemini. The prompt gathers this week's signals itself, from the web and (if your tool can reach it) your mailbox. No pasting required.
3. If your model cannot reach the web or your mailbox, it will say so and work with whatever source it has. You can also paste signals in by hand on the weeks that matter.
4. The output is your first weekly brief: a 3-line summary, a scored table, and a Monitor list.

## The prompt

```
I need a So-What / Now-What synthesis on this week's signals,
filtered against my relevance window and scored for materiality.

MY RELEVANCE WINDOW   (write this once, reuse it every week;
only the signals change)
- Domain: [3-5 watch areas, e.g. EU AI regulation, industrial
  automation, agentic commerce]
- Function: [my role, e.g. CFO of a 500-person manufacturer,
  COO of a hospital network, founder of a B2B SaaS]
- Decision horizon: [near 0-3m / mid 3-12m / long 12m+]

THIS WEEK'S SIGNALS   (gathered automatically from two sources,
no pasting)
You have web access and a connected mailbox. Do not ask me to
paste anything. Build the signal set yourself:
- From the web: pull this week's most significant developments
  across my domain areas. For each, capture publisher, source
  link, and date. Prefer primary sources (regulator, company,
  lab) over secondary coverage.
- From my mailbox: read every newsletter, briefing, and alert
  that arrived in the last 7 days. Treat each distinct story as
  one signal, not each email; one newsletter can carry several.
- Merge both streams and collapse duplicates: the same story
  from web and inbox is one signal, keep the stronger source.
- Aim for 8-15 distinct signals before filtering. Tag each
  [web], [inbox], or [both] so I can see where it came from.

YOUR TASK
1. Drop signals outside my relevance window.
2. Send to Monitor any signal whose first material impact falls
   outside my decision horizon.
3. Score each remaining signal on three axes, 1 to 5:
   - Speed: how fast it hits my operations, budget, or mandate
   - Scope: how broad across functions and units
   - Reversibility: how expensive it is to wait
4. Rank by total score. Brief at most the top 5. If more than
   five clear 9 out of 15, brief only the top five; send the rest
   to Monitor.
5. For each brief-worthy signal write:
   - So What: one sentence true only for my business. Use only the
     context I gave you. Mark any inference "(assumes ...)".
   - Now What: one concrete move I can start within my horizon
     (this week, this month, or commission this quarter for
     long-cycle changes).

OUTPUT
- Top: 3-line headline summary
- Body: table with Signal (tagged + linked) | Score | So What |
  Now What
- Bottom: Monitor list, each with the trigger that promotes it

CONSTRAINTS
No generic answers. If the So What could apply to any company,
rewrite until only my business fits. "This week" means the last
7 calendar days; ignore older items, and do not treat a standing
future deadline as a new signal unless it changed this week.
Sourcing: cite the primary source, the regulator, company, or
lab's own page, or the original announcement. Do not pass off a
vendor blog, an SEO roundup, or secondary coverage as the source;
if only secondary coverage exists, link the best one and tag the
signal [unverified]. Before you include any link, confirm it
resolves to a real page; if you cannot, drop the link and mark
the item [unverified] rather than guess a URL. Never invent a
signal, a figure, or a source to fill the set. If you cannot name
a concrete Now What, demote to Monitor. If web access or the
mailbox is unavailable, say so and work with whatever source you
have. The brief is one page, not a digest.
```

## Want it hands-off?

Three sibling recipes run the same discipline without you remembering to:

- `cowork-recipe/` runs it with no code and no API key, reading your mailbox and the web directly.
- `claude-code-recipe/` runs it from the command line, version-controlled, wired into cron.
- `starter-template/` runs it on an RSS feed list via Google Apps Script and emails you the brief.

## License

CC-BY 4.0. Use it, adapt it, ship it. Attribution appreciated.
