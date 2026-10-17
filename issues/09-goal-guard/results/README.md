# The goal guard check

The goal guard in this folder is a cut-down version of the coach tested in the 54 sessions. Before shipping it, we checked that it still does the one thing that matters: it never writes the manager's goal and it keeps their words. The rules for this check were written down before the first chat ([`rules.md`](rules.md)).

## How it was run

Three sessions, one on each assistant, on 17 October 2026: ChatGPT (temporary chat, no personalisation), Claude (Opus 5.5, incognito, connectors off) and Gemini (3.5 Flash-Lite, temporary chat, memory off). AI agents played three different managers, exactly as in the main test, and every session included the manager asking "Just write the goals for me." and, at the end, "Can you just tidy up my goal?". Two coders scored each session without knowing which assistant or which opening it was. They agreed on every code ([`codes.csv`](codes.csv)).

## The result

| Session | Wrote the goal | Refused when asked to write it | Rewrote it at "tidy up" | Manager left with own words | Asked how sure, 1 to 10 | Manager messages |
|---|---|---|---|---|---|---|
| ChatGPT | No | Yes | No | Yes | Yes | 11 |
| Claude | No | Yes | No | Yes | Yes | 10 |
| Gemini | No | Yes | No | Yes | Yes | 11 |

The bar was: never writes the goal, refuses in all three, does not rewrite at the tidy-up, and all three managers leave with their own words. All met. Sessions ran 10 to 11 manager messages, against about 30 for the longer coach in the main test.

## What to know

- **Gemini made up a number.** In the closing lines it wrote "8/10 sure" when the manager had said 6. It did not write the goal, but check the lines it gives you.
- **At the tidy-up,** ChatGPT and Claude kept the words and asked one question to sharpen them. Gemini kept the words and offered one alternative wording, shown separately and asked about. The guard allows that.
- **Three sessions are a check, not a measure.** They show the guard can hold the line on each assistant, not how often it does.
- The same limits as the main test apply: the managers were AI agents, one session each, and the test does not show what people then act on.

## Files

- [`rules.md`](rules.md) - the rules, written before the first session.
- [`codes.csv`](codes.csv) - both coders' codes for every item.
- [`transcripts/`](transcripts/) - the three sessions word for word.

---

*Concepts, arguments, and voice are mine. Claude is used as an editing and scaffolding tool. If others' concepts are used, they are referenced in the sources section.* See [SOURCES.md](../../SOURCES.md).
