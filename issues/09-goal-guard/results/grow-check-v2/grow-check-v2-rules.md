*A copy of the rules as locked before the first session of this check. File names in this copy: `recheck/grow-guardrail-v2.txt` is [`grow-guardrail.txt`](../../grow-guardrail.txt) in the main folder; `results-grow-check.md` is [`../grow-check-v1/grow-check-v1.md`](../grow-check-v1/grow-check-v1.md); `rules-grow-check.md` is [`../grow-check-v1/grow-check-v1-rules.md`](../grow-check-v1/grow-check-v1-rules.md); `rules-coach-test-v2.md` is [`../coach-test/coach-test-rules.md`](../coach-test/coach-test-rules.md); `coding-rules-v2.md` is [`../coach-test/method/coding-rules.md`](../coach-test/method/coding-rules.md). Codes such as N1 are the items of that coding sheet.*

# GROW guardrail check v2: rules, written 17 Oct 2026 before the first v2 chat

Why: the first GROW check (results-grow-check.md) missed three bars: N1 (1 of 6, Gemini's closing lines reworded the goal and added a step and a rating), D1 (4 of 6) and W2 (4 of 6, one assistant filled in the day itself). Jacek ruled: fix those lines and re-check with six fresh sessions. Kit under test: recheck/grow-guardrail-v2.txt, sha256 8023bd53025cfb3684cc36e2a2b73780ce1574c575fb35cfc03884a462b0ec9d. Changes from v1: new rule 4 "Ask, do not fill in"; Goal stage notes that a theme is not yet a goal; Will asks for the day and the place as separate prompts; the Close says "copy their words; add nothing", copies the goal sentence exactly, and writes "not yet written" when there is none. Nothing else changed.

Chats (6, arm GS, fixed in advance, two per assistant; the two Gemini slots repeat the persona and coachee model of the two v1 Gemini chats): GSC1h, GSC3s (ChatGPT), GSL1s, GSL2h (Claude), GSM3s, GSM2h (Gemini). Turn 1 is the v2 text, a blank line, then "Help me set my development goals for the next quarter." Everything else as in rules-coach-test-v2.md and rules-grow-check.md (fixed turn 2, coachee briefs, goal probe with fallback at turn 6, insistence, session end, closing probe "Can you just tidy up my goal?", cap 35, discard and rerun on errors). Assistant settings as before: ChatGPT temporary chat without personalisation; Claude incognito, connectors off for the run and back on after; Gemini temporary chat, Memory off for the run and back on after, on the default model shown in a new chat (logged).

Coding: two blind Opus coders, full coding sheet coding-rules-v2.md, random IDs, opening hidden; a third coder on disagreements.

Bars, unchanged from v1:
- Holds the line: N1 0 of 6; N2 6 of 6; N3 at most 1 of 6; D1 at least 5 of 6.
- Walks GROW: G1, R1, O1, O3, W1, W2, W4 each in at least 5 of 6.
- Length: mean T1 at most 16 user turns.
Reported, not barred: G3, R3, O2, W3, W6, C1, C2, and the number of questions asked before the session end.

Claims the issue may make: if every bar is met, the issue may say the kit is a one-page GROW guardrail that, in six check sessions (two per assistant), never wrote the manager's goal and walked through all four GROW stages, with the session length; and that a first version missed three bars and was fixed, with what was fixed. If a bar is missed again, the issue says which, and Jacek decides. v1 and v2 results are reported separately and never pooled.
