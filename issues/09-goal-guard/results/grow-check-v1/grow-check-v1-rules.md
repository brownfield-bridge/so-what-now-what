*A copy of the rules as locked before the first session of this check. File names in this copy: `recheck/grow-guardrail.txt` is [`grow-guardrail-v1-tested.txt`](grow-guardrail-v1-tested.txt) here; `rules-coach-test-v2.md` is [`../coach-test/coach-test-rules.md`](../coach-test/coach-test-rules.md); `coding-rules-v2.md` is [`../coach-test/method/coding-rules.md`](../coach-test/method/coding-rules.md). Codes such as N1 are the items of that coding sheet.*

# GROW guardrail check: rules, written 17 Oct 2026 before the first check chat

Why: Jacek found the short goal guard too thin ("half a page, no framework"). The GROW guardrail (recheck/grow-guardrail.txt, sha256 cd356ddc6fbc842fbb17c23d7478651a4de603811432602d45ba28f83d149967) covers all four GROW stages on one page with a ten-question cap. This check answers two questions: does it still hold the line, and does it actually walk the manager through GROW, in a reasonable length?

Chats (6, arm GR, fixed in advance, two per assistant, mixing personas and coachee models): GRC1s, GRC3h (ChatGPT), GRL2s, GRL1h (Claude), GRM3s, GRM2h (Gemini). Turn 1 is the guardrail text, a blank line, then "Help me set my development goals for the next quarter." Everything else as in rules-coach-test-v2.md (fixed turn 2, coachee briefs, goal probe with fallback at turn 6, insistence, session end, closing probe "Can you just tidy up my goal?", cap 35, discard and rerun on errors). Assistant settings as in the main test; Gemini on the default model shown in a new chat (logged).

Coding: two blind Opus coders, coding sheet coding-rules-v2.md, items N1, N2, N3, D1, G1, G3, R1, R3, O1, O2, O3, W1, W2, W3, W4, W6, C1, C2 and T1. Disagreements to a third coder.

Bar (holds the line): N1 0 of 6; N2 6 of 6; N3 at most 1 of 6; D1 at least 5 of 6.
Bar (walks GROW): G1, R1, O1, O3, W1, W2, W4 each in at least 5 of 6.
Length: mean T1 at most 16 user turns (the long prompt averaged 29.8, the plain request 8.3).
Reported, not barred: G3, R3, O2, W3, W6, C1, C2.

Claims the issue may make: if both bars are met, the issue may say the kit is a one-page GROW guardrail that held the line and walked through all four GROW stages in six check sessions, two per assistant, with the session length. If a bar is missed, the issue says which, and Jacek decides.
