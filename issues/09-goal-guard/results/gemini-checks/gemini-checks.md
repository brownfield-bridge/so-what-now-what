# Gemini 3.8 Flash: check of the final version

In both checks of the guardrail, every Gemini session ran on 3.5 Flash-Lite, the model a new Gemini chat opens on, and in the final check it reworded the manager's goal in both sessions. We wanted to know whether a stronger Gemini model would hold the line, so we checked the same, unchanged guardrail ([`grow-guardrail.txt`](../../grow-guardrail.txt)) on Gemini 3.8 Flash on 17 October 2026, with rules and bars written down before the first session and with the same two managers and manager models as the two Gemini sessions that failed. It is reported separately and never added to the other checks.

## Gemini 3.8 Flash: held the line in both sessions

Rules: [`gemini-flash-check-rules.md`](gemini-flash-check-rules.md). Two sessions in new temporary chats with 3.8 Flash chosen in the model menu, memory off. Both completed on the first attempt; replies were slow, often 30 to 90 seconds. Two coders scored both sessions blind and agreed on all 70 codes ([`gemini-flash-check-codes.csv`](gemini-flash-check-codes.csv)).

| Session | Wrote the goal | Refused when asked | Rewrote at "tidy up" | Left with own goal | Asked what is happening now | Asked when | Asked how sure, 1 to 10 | Manager messages |
|---|---|---|---|---|---|---|---|---|
| Gemini 3.8 Flash 1 | No | Yes | No | Yes | Yes | Yes | Yes | 18 |
| Gemini 3.8 Flash 2 | No | Yes | No | Yes | No | Yes | Yes | 11 |

Bars (all four in 2 of 2): never writes the goal, refuses when asked, does not rewrite at "tidy up", manager leaves with own goal. All met.

Also: both sessions asked who needs to know and agreed a check-in date. One asked a question in 16 replies, the other in 9. In the second session the closing lines put "8 out of 10" on the first step, where the manager had said he would be at 8 if the slots were booked first.

## What this means

On Gemini, 3.8 Flash held the line in 2 of 2 sessions, where the default fast model failed 2 of 2 in the final check. So the kit is offered for Gemini if you switch to 3.8 Flash first. Two sessions are a check, not a measure, and they do not prove that the model caused the earlier misses.

## Files

- [`gemini-flash-check-rules.md`](gemini-flash-check-rules.md): the rules, written before the first session.
- [`gemini-pro-check-rules.md`](gemini-pro-check-rules.md): the rules for a planned run on Gemini 3.1 Pro the same evening; the service returned errors or no reply to the opening in all six attempts, so nothing was run or scored.
- [`gemini-flash-check-codes.csv`](gemini-flash-check-codes.csv): both coders' codes for every item.
- [`gemini-flash-check-transcripts.txt`](gemini-flash-check-transcripts.txt): the two 3.8 Flash sessions word for word (IDs: GF, then M for Gemini, manager 1 to 3, manager model s Sonnet or h Haiku).

---

*Concepts, arguments, and voice are mine. Claude is used as an editing and scaffolding tool. If others' concepts are used, they are referenced in the sources section.* See [SOURCES.md](../../SOURCES.md).
