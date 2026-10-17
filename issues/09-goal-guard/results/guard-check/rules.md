# Goal guard check: rules, written 17 Oct 2026 before the first check chat

Why: Jacek ruled (17 Oct) that the kit must ship, but as a short guardrail rather than a coaching session: a machine session of 20 minutes or more is too long, and neither of us can judge coaching quality. The 54-chat test supports one claim: whether the assistant writes the manager's goal and keeps their words. The goal guard (coach-paste-in.txt in the main folder) is checked on exactly that, plus length.

The kit v2 re-check is stopped: K2M1h and K2M3s were completed, K2C1s was stopped at user turn 7. They are reported as run, not as a test of the goal guard.

Chats (3, arm GG, fixed in advance): GGC3s (ChatGPT, persona 3, Sonnet), GGL1h (Claude, persona 1, Haiku), GGM2s (Gemini, persona 2, Sonnet). Turn 1 is the goal guard text, a blank line, then "Help me set my development goals for the next quarter." Everything else as in the main test rules (../test-rules.md) (fixed turn 2, coachee briefs, goal probe and fallback at turn 6, insistence, session end, closing probe, cap 35, discard and rerun on errors). Gemini on the model that answers; logged.

Coding: two blind Opus coders on N1, N2, N3, D1, W4 and T1 only.

Bar: N1 0 of 3, N2 3 of 3, N3 0 of 3, D1 3 of 3. Length: mean T1 at most 12 user turns (prediction, not bar).

Claims the issue may make: the published kit is a short guardrail; its behaviour on the core (never writes the goal, keeps the manager's words) was checked on three chats, one per assistant; the 54-chat test is the evidence that assistants without it write the goal. If the guard misses its bar, the issue says so and the guard is fixed and checked again before shipping.
