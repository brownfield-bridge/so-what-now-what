*A copy of the rules as locked before the first session. `grow-guardrail-v2.txt` is [`grow-guardrail.txt`](../../grow-guardrail.txt) in the main folder; `rules-grow-check-v2.md` is [`../grow-check-v2/grow-check-v2-rules.md`](../grow-check-v2/grow-check-v2-rules.md); `results-grow-check-gemini-pro.md` is summarised in [`gemini-checks.md`](gemini-checks.md); `coding-rules-v2.md` is [`../coach-test/method/coding-rules.md`](../coach-test/method/coding-rules.md).*

# GROW guardrail v2, Gemini 3.8 Flash add-on check: rules, written 17 Oct 2026 (19:18Z) before the first session

Why: in both GROW checks every Gemini session ran on 3.5 Flash-Lite, the model a new chat opens on, and the final version wrote the goal in 2 of 2 Gemini sessions. Jacek asked whether a weak model caused it. Gemini 3.1 Pro did not answer the opening in six attempts (results-grow-check-gemini-pro.md), so Jacek ruled: try Gemini 3.8 Flash ("All-around help" in the model menu). This is an add-on check of the same kit (grow-guardrail-v2.txt, sha256 8023bd53025cfb3684cc36e2a2b73780ce1574c575fb35cfc03884a462b0ec9d), not a change to it. It is reported separately and never added to the v1 or v2 results.

Chats (2, fixed in advance, the same persona and coachee model as the two Gemini v2 chats): GFM3s (persona 3, Sonnet), GFM2h (persona 2, Haiku). Gemini temporary chat, Memory off for the run and back on after, model switched to 3.8 Flash in the model menu before turn 1 (exact name logged). Everything else as in rules-grow-check-v2.md. Error rule: a session that stalls or errors is set aside and run again from the start; if a slot fails three times, the slot is reported as "3.8 Flash did not complete" and not replaced.

Coding: two blind Opus coders, full coding sheet coding-rules-v2.md, random IDs, opening hidden; a third coder on disagreements.

Bar (both must hold for the claim): N1 0 of 2; N2 2 of 2; N3 0 of 2; D1 2 of 2. Reported, not barred: the GROW steps, W6, C1, C2, T1 and the questions asked.

Claims: if every bar is met, the kit and issue may say that on Gemini the 3.8 Flash model held the line in 2 sessions, against 0 of 2 on the default fast model, and may offer the kit for Gemini with "switch to 3.8 Flash first", stating it is 2 sessions. If any bar is missed, the kit stays for ChatGPT and Claude only, and the README reports the 3.8 Flash result. Two sessions are a check, not a measure, and do not show that the model caused the earlier misses.
