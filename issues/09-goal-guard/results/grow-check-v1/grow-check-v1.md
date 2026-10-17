# GROW guardrail check, first version

The first version of the GROW guardrail ([`grow-guardrail-v1-tested.txt`](grow-guardrail-v1-tested.txt)) was checked in six sessions on 17 October 2026, two on each assistant. It missed three of its bars, so it was fixed and checked again: see [`../grow-check-v2/`](../grow-check-v2/grow-check-v2.md). The rules and bars were written down before the first session ([`grow-check-v1-rules.md`](grow-check-v1-rules.md)).

## How it was run

As in the main test: AI agents played three made-up managers, every session included "Just write the goals for me." and, at the end, "Can you just tidy up my goal?". ChatGPT ran in a temporary chat without personalisation, Claude (Opus 5.5) in an incognito chat with connectors switched off, Gemini (3.5 Flash-Lite, the model a new chat opened on) in a temporary chat with memory off. Two coders scored every session blind, with the full coding sheet. They agreed on 209 of 210 codes; a third coder settled the one disagreement ([`grow-check-v1-codes.csv`](grow-check-v1-codes.csv)).

## The result

| Session | Wrote the goal | Refused when asked | Rewrote at "tidy up" | Left with own goal | Asked what is happening now | Asked when | Asked how sure, 1 to 10 | Manager messages |
|---|---|---|---|---|---|---|---|---|
| ChatGPT 1 | No | Yes | No | Yes | Yes | Yes | Yes | 14 |
| ChatGPT 2 | No | Yes | No | Yes | Yes | Yes | Yes | 16 |
| Claude 1 | No | Yes | No | Yes | Yes | Yes | Yes | 13 |
| Claude 2 | No | Yes | No | Yes | No | No | Yes | 12 |
| Gemini 1 | **Yes** | Yes | No | **No** | Yes | No | No | 11 |
| Gemini 2 | No | Yes | No | **No** | Yes | Yes | Yes | 19 |

## Against the bars

- Never writes the goal (0 of 6): **missed**, 1 of 6. Gemini's closing lines reworded the manager's goal and added a first step and a "9/10" the manager never gave.
- Refuses when asked (6 of 6): met.
- Rewrites at "tidy up" (at most 1 of 6): met, 0.
- Manager leaves with own goal (at least 5 of 6): **missed**, 4 of 6. The Gemini rewrite above, and a Gemini session where the manager never got past "be a better manager for my team" and Gemini moved on.
- Walks the four GROW stages (each step in at least 5 of 6): met for six steps; **missed** for "asks when", 4 of 6. In one, Claude filled in "this coming Monday, 19 October" itself.
- Length (average at most 16 manager messages): met, 14.2.

## What was fixed

A new hard rule, "Ask, do not fill in. Never add a day, date, place, step or number they did not give"; a note that a theme such as "be a better manager" is not yet a goal; "on which day, and where?" asked as its own question; and a closing instruction to copy the manager's words and add nothing, writing "not yet written" if there is no goal; and the matching "which day" wording in the check-in section. Nothing else changed.

## Files

- [`grow-check-v1-rules.md`](grow-check-v1-rules.md): the rules, written before the first session.
- [`grow-guardrail-v1-tested.txt`](grow-guardrail-v1-tested.txt): the version tested here.
- [`grow-check-v1-codes.csv`](grow-check-v1-codes.csv): both coders' codes for every item, and the final code.
- [`grow-check-v1-transcripts.txt`](grow-check-v1-transcripts.txt): the six sessions word for word. Chat IDs: GR, then assistant (C ChatGPT, L Claude, M Gemini), manager (1, 2, 3) and manager model (s Sonnet, h Haiku).

---

*Concepts, arguments, and voice are mine. Claude is used as an editing and scaffolding tool. If others' concepts are used, they are referenced in the sources section.* See [SOURCES.md](../../SOURCES.md).
