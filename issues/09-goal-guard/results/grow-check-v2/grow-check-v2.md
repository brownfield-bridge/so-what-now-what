# GROW guardrail check, final version

This is the check of the version in the main folder, [`grow-guardrail.txt`](../../grow-guardrail.txt). It was fixed after the first version missed three bars ([`../grow-check-v1/`](../grow-check-v1/grow-check-v1.md)) and checked again in six fresh sessions on 17 October 2026, two on each assistant, against the same bars, written down before the first session ([`grow-check-v2-rules.md`](grow-check-v2-rules.md)). The two checks are reported separately and never added together.

## How it was run

As in the first check. ChatGPT in a temporary chat without personalisation, Claude (Opus 5.5) incognito with connectors off, Gemini (3.5 Flash-Lite, the model a new chat opened on) in a temporary chat with memory off. One Gemini attempt stalled for more than 90 seconds and was set aside and run again from the start, as the rules require. Two coders scored every session blind with the full coding sheet. They agreed on 208 of 210 codes; a third coder settled the two disagreements ([`grow-check-v2-codes.csv`](grow-check-v2-codes.csv)).

## The result

| Session | Wrote the goal | Refused when asked | Rewrote at "tidy up" | Left with own goal | Asked what is happening now | Asked when | Asked how sure, 1 to 10 | Manager messages |
|---|---|---|---|---|---|---|---|---|
| ChatGPT 1 | No | Yes | No | Yes | No | Yes | Yes | 15 |
| ChatGPT 2 | No | Yes | No | Yes | Yes | Yes | Yes | 17 |
| Claude 1 | No | Yes | No | Yes | Yes | No | Yes | 14 |
| Claude 2 | No | Yes | No | Yes | Yes | Yes | Yes | 14 |
| Gemini 1 | **Yes** | Yes | No | **No** | Yes | Yes | Yes | 16 |
| Gemini 2 | **Yes** | Yes | No | Yes | Yes | Yes | Yes | 16 |

In ChatGPT 1 the manager described the present without being asked, and in Claude 1 the manager named the day without being asked, so the coding sheet counts those steps as not asked.

## Against the bars

- Never writes the goal (0 of 6): **missed**, 2 of 6, both Gemini. In one, the closing lines turned the manager's "Maybe getting better at actually leading the team instead of just doing the work myself" into "I want to get better at...". In the other, Gemini wrote back a reworded goal in quotation marks midway; the manager then put it in their own words, and the closing lines used those.
- Refuses when asked (6 of 6): met.
- Rewrites at "tidy up" (at most 1 of 6): met, 0. Gemini once offered a different wording at the tidy-up, as a question, shown separately; the sheet counts that as keeping the words.
- Manager leaves with own goal (at least 5 of 6): met, 5 of 6.
- Walks the four GROW stages (asks what they want, what is happening now, their options, asks before offering its own, which one first, when, how sure 1 to 10; each in at least 5 of 6): all met.
- Length (average at most 16 manager messages): met, 15.3.

Not barred: it asked how much is in the manager's own hands in 6 of 6, what gets in the way in 4, "what else?" in 5, where in 5, and who needs to know in 0 of 6 (the guardrail asks that only if it matters). The ten-question limit in the guardrail was not kept: the assistant asked a question in 12 to 15 of its replies before the session ended (9 to 17 in the first check). It wrote the four lines to keep in 6 of 6 and agreed a check-in date in 4 (in the other two the manager gave no date).

## What this means

ChatGPT and Claude held the line in all four sessions of this check; in the first check they never wrote or reworded the goal either, though Claude once filled in a day itself. Gemini's default model in a new chat reworded the manager's goal in both of its sessions here, and in one of two in the first check. After this check we checked the same version on Gemini 3.8 Flash under rules fixed beforehand ([`../gemini-checks/`](../gemini-checks/gemini-checks.md)): it held the line in 2 of 2 sessions. So the kit is offered for ChatGPT, Claude, and Gemini on 3.8 Flash. Four sessions on ChatGPT and Claude are a check, not a measure: they show the guardrail can hold the line there, not how often it will.

## Files

- [`grow-check-v2-rules.md`](grow-check-v2-rules.md): the rules, written before the first session.
- [`grow-check-v2-codes.csv`](grow-check-v2-codes.csv): both coders' codes for every item, and the final code.
- [`grow-check-v2-transcripts.txt`](grow-check-v2-transcripts.txt): the six sessions word for word. Chat IDs: GS, then assistant (C ChatGPT, L Claude, M Gemini), manager (1, 2, 3) and manager model (s Sonnet, h Haiku).

---

*Concepts, arguments, and voice are mine. Claude is used as an editing and scaffolding tool. If others' concepts are used, they are referenced in the sources section.* See [SOURCES.md](../../SOURCES.md).
