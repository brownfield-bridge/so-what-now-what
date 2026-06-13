# Recipe: the hands-off synthesizer (no code)

The paste-and-run prompt gives you a brief whenever you remember to run it. This recipe removes the remembering. You describe the job once in plain language, connect your mailbox, set it to run every Sunday, and the brief is waiting on Monday. No code, no API key.

This is the rung most readers want. You stay the one who set the filter and reads the result. The assistant does the gathering and the first-pass scoring, which is the part that was never going to happen by hand.

## What you need

- Claude with Cowork (the desktop app). Cowork is in research preview, so the exact buttons may move; the recipe below is written in terms of what you are asking it to do, not where to click.
- Your mailbox connected (Gmail or Outlook), so it can read the week's newsletters.
- Web search on, so it can pull primary sources directly.
- A folder it can write to, if you want the brief saved as a file rather than sent back as a message.

No Anthropic API key. No RSS feed list to assemble. The mailbox and the web are the signal set.

## Set it up once

1. Connect your mailbox and turn on web search.
2. Write your relevance window once (see `relevance-window.md` in this folder for the template). This is the only thinking the recipe asks of you, and it is the whole game. Three to five watch areas, your role, your decision horizon.
3. Create a scheduled task set to run every Sunday afternoon, and paste the standing instruction below into it, with your relevance window filled in.
4. Choose where the brief lands: saved to your folder as a dated file, or sent back to you as a message you read Monday morning.

That is the setup. From then on it runs without you.

## The standing instruction to schedule

Paste this as the scheduled task, with the bracketed parts replaced:

```
Every Sunday, build me a So-What / Now-What synthesis on this
week's signals, filtered against the relevance window below and
scored for materiality.

MY RELEVANCE WINDOW
- Domain: [3-5 watch areas]
- Function: [my role]
- Decision horizon: [near 0-3m / mid 3-12m / long 12m+]

GATHER THIS WEEK'S SIGNALS YOURSELF, from two sources:
- The web: this week's most significant developments across my
  domain areas. Capture publisher, link, and date. Prefer the
  primary source (regulator, company, lab) over coverage of it.
- My mailbox: every newsletter, briefing, and alert from the last
  7 days. Treat each distinct story as one signal, not each email.
- Merge both, collapse duplicates, tag each [web], [inbox], or
  [both]. Aim for 8 to 15 distinct signals before filtering.

THEN:
1. Drop signals outside my relevance window.
2. Send to a Monitor list any signal whose first material impact
   falls outside my decision horizon.
3. Score each remaining signal 1 to 5 on Speed, Scope, and
   Reversibility (cost of waiting). Total out of 15.
4. Brief at most the top 5 that clear 9 of 15. Demote the rest.
5. For each brief-worthy signal write:
   - So What: one sentence true only for my business. Mark any
     inference "(assumes ...)".
   - Now What: one concrete move I can start within my horizon.

GIVE ME:
- A 3-line headline summary
- A table: Signal (tagged + linked) | Score | So What | Now What
- A Monitor list, each with the trigger that would promote it

RULES: "This week" means the last 7 calendar days; do not treat a
standing future deadline as a new signal unless it changed this
week. Cite the primary source (the regulator, company, or lab's
own page); do not pass off a vendor blog or secondary coverage as
the source, and if only secondary exists, tag the signal
[unverified]. Confirm every link resolves to a real page; if you
cannot, drop the link and mark the item [unverified] rather than
guess a URL. No generic So Whats. If you cannot name a concrete
Now What, demote to Monitor. Never invent a signal, figure, or
source to fill the set. One page, not a digest. Save it as
[folder/file] and tell me it is ready.
```

## What good looks like

You open the brief Monday. Two or three signals, each with a So What only your business could have written and a Now What you can act on this week. A Monitor list you skim in ten seconds. Everything else from the week is gone, correctly.

If the brief reads flat, the recipe is not failing. Your filter is too generous. Tighten the watch areas in your relevance window. A mediocre brief is the system telling you the window is wrong, which is exactly the feedback the manual prompt gives you too, just slower.

## The honest limits

- It reads what your mailbox and the web hold. If your real signal lives in a closed Slack or a paid terminal it cannot reach, it will not see it. Add those sources by hand on the weeks they matter.
- It scores on the window you gave it. A vague window produces a vague brief. The scoring is a first pass for you to overrule, not a verdict.
- Set it to write a draft or a file, not to send anything outward. The brief is for you.

## License

CC-BY 4.0. Use it, adapt it, ship it. Attribution appreciated.
