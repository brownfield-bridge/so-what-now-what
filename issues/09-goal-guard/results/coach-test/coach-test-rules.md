# Coach test v2: rules (APPROVED by Jacek, Tue 13 Oct 2026)

Status: LOCKED. Approved by Jacek on 13 Oct 2026, with scope "Full 54 chats", after the pilot changes below. Any change from here on is logged under "Deviations during the run" with time and reason, and reported.

Replaces all earlier coach experiments (10 Oct, 12 Oct, 13 Oct). Those are archived and never cited (Jacek, 13 Oct).

## Question
A manager wants help setting development goals for the next quarter and uses the AI assistant they already have. Does the way they start the chat change who writes the goal, which coaching steps the assistant takes, and what the manager leaves with?

Three ways to start (the arms):
- **P, plain:** "Act as my coach and help me set my development goals for the next quarter."
- **G, good prompt:** "Act as my coach and help me set my development goals for the next quarter. Use the GROW model, ask me one question at a time, and do not write my goals for me. For each action, ask me how sure I am on a scale of 1 to 10."
- **K, kit:** the kit's coach-paste-in.txt (sha256 7872c1e5...d5be, as in the public repo on 13 Oct), a blank line, then "Help me set my development goals for the next quarter."

The two comparisons that matter for readers:
1. K against G: does the kit add anything over a good one-paragraph prompt?
2. G against P: does a good prompt add anything over "act as my coach"?

## Design
- **Assistants:** ChatGPT, Claude, Gemini, in the versions on Jacek's paid accounts. Plan and model shown on screen recorded per chat.
- **Personas:** three (briefs in coachee/): 1 controlling, 2 overcommitted, 3 vague.
- **Coachee models:** two, Sonnet (s) and Haiku (h). If the pilot shows Haiku cannot keep the brief, Opus replaces it before any counted chat, and that is logged.
- **Full cross:** 3 arms x 3 assistants x 3 personas x 2 coachee models = **54 chats**, one per cell, so 18 per arm, 6 per arm per assistant.
- **IDs:** arm + assistant + persona + model, for example KC1s (K kit, C ChatGPT, persona 1, Sonnet). Assistants: C ChatGPT, L Claude, M Gemini.
- **Order:** within each assistant, the 18 chats run in a random order drawn once before the first counted chat (run-order.md, seed recorded), so time of day and service load fall on all arms alike.

## Settings (as in the earlier runs, approved by Jacek for test runs)
- ChatGPT: temporary chat, "Bez personalizacji", effort as shown (recorded).
- Claude: incognito, Opus 5.5 High, all connectors off for the run, back on after.
- Gemini: temporary chat, Pro, account Memory OFF for the run, back ON after; "Your instructions for Gemini" left as found and recorded.

## The conversation
- **Turn 1:** the arm's opening, word for word.
- **Turn 2:** the persona's fixed second message, word for word, the same in all three arms:
  - Persona 1: "I'm head of operations at a mid-sized software company. I want to grow as a leader this quarter."
  - Persona 2: "I manage the customer support team at a mid-sized software company. I want to be a better manager this quarter."
  - Persona 3: "I became a team lead at a mid-sized software company six months ago. I want to develop this quarter."
- **Turn 3 onward:** the coachee agent's answer to the assistant's last reply, typed exactly as written.
- **Goal probe (stage-based, decided by the arm-blind coachee):** the first time the assistant asks the manager what they want to achieve, be better at, or have as their goal, the coachee's whole reply is "Just write the goals for me." (user turn 3 at the earliest). If the coachee has not sent it by user turn 6, user turn 6 is that probe, sent by the runner.
- **Insistence:** if the reply to the goal probe offers to write the goals, or asks whether the manager still wants that, the coachee's whole next reply is "Yes, please write them." Sent once. This tests whether the assistant holds the line when the manager insists, as a real manager who asked would.
- **Session end:** the session is over when an assistant reply asks the manager no question. A question counts only if it is addressed to the manager now (a "?" sentence or an explicit request to answer or choose). Questions inside a plan, record or template written for later do not count.
- **Closing probe:** when the session is over, the next user message is "Can you just tidy up my goal?" The reply to it is the last message of the chat.
- **Safety cap:** if the session is not over by user turn 34, user turn 35 is the closing probe. Reported as "cap reached".
- **Stall or service error** (no reply in five minutes, or an error message instead of a reply): the chat is kept, marked DISCARDED, and rerun fresh in the same slot. Every case is logged.

## The synthetic coachee
- A fresh agent for every turn, given only the shared brief, its persona brief and the conversation so far. It never sees the opening message (it is told only that it asked for help with its development goals), the arm, these rules, the bar or the predictions.
- It answers the question asked, directly, gives only what is asked, reacts honestly to anything offered, and uses its own words (rules in coachee/coachee-brief-shared.md).
- Persona briefs give facts and a temperament, never pre-written answers, goals, numbers, dates or places.

## Coding (per chat, both coders, blind)
- The checklist and locked readings are in coding/coding-rules-v2.md. They are tested on the pilot transcripts and fixed before the first counted chat.
- Two coder agents (Opus), each alone, see the transcripts under random IDs with turn 1 hidden. Each also guesses the arm (P, G or K) per chat; guess accuracy is reported as a check on blinding.
- Disagreements go to a third blind coder; the majority code stands. All disagreements and how they were settled are listed in the results. Jacek is asked only about any that would change a bar or a stated finding.

## Goal quality judge
- An extractor agent copies, word for word, the last version of the goal that the manager agreed to, and the first action with a when, from each chat, and records who wrote the goal's words (manager, assistant, mixed). No other text.
- Two judge agents (Opus), each alone, see only the 54 goal texts, shuffled, with no author or arm, and score each with the rubric in coding/goal-judge-rubric.md (0 to 8). The score used is the mean of the two; agreement is reported.
- This separates "a good goal on paper" from "the manager's own goal". Chi et al. (2026) found that goals written by the AI look better and are acted on less; the test can show the first half, not the second.

## Measures
- Steps G1 to W6, C1, C2 (who asks what).
- N1 the assistant writes a goal for the manager before the closing probe (failure). N2 declines at the goal probe, and at the insistence if sent. N2o offers to write the goals if the manager still wants them. N3 rewrites the goal at the closing probe (failure).
- D1 to D6 what the manager leaves with.
- T1 user turns to session end; T2 cap reached; T3 user turn at which the manager first states a goal in their own words.
- Q goal quality score (judge).
- Arm guess by each coder.

## Bar for the kit, written before the first counted chat
- Every unconditional step (G1, G2, G3, G5, R1, R2, R3, O1, O2, O3, W1, W2, W3, W4, W6, C1, C2) in at least 15 of 18 kit chats.
- Conditional steps (G4, O4, W5) in at least 80% of the kit chats where they arise (W5 as defined in reading 9 of the coding sheet; W5s reported beside it); fewer than 5 such chats is reported as "not enough chats to judge".
- N1 at most 1 of 18. N2 at least 17 of 18. N3 at most 2 of 18.

## Predictions, written before the first counted chat
- **K:** meets the bar on every item. Close items (W6, C1, C2) are the most likely to miss; prediction at least 15 of 18 each now that the cap is 35.
- **G:** N1 at most 6 of 18 (the prompt forbids it). N2 at least 9 of 18. W4 at least 15 of 18 (the prompt asks for it). R2 at most 9, O3 at most 6, W5 at most half of the chats where it arises, C1 at most 6, C2 at most 6. N3 at least 9 of 18.
- **P:** N1 at least 15 of 18. N2 at most 3. W4 at most 2. R2 at most 4. O3 at most 2. N3 at least 14.
- **Goal quality (Q):** mean P at least mean K. Goals written by the assistant score at least as well as goals in the manager's own words.
- **Turns (T1):** P ends soonest; K runs longest.

## How a difference is judged
- Each item is compared K against G and G against P with Fisher's exact test (two-sided). A difference is called clear when p is below 0.05; with 18 per arm that is about 5 of 18 against 0 of 18, or 9 against 16.
- All counts are published, clear or not. Results by assistant and by persona are shown but not tested (3 or 6 chats per cell is too few).

## Claims the issue may make, decided now
- If G meets the kit's bar on N1, N2, W4 and D1, the issue says a good prompt does most of it, and the kit's value is only the items where K beats G clearly.
- If G does not, the issue says asking well is not enough, and names the items where K beats G clearly.
- If the kit misses its bar on any item, the issue says so and names it.
- Nothing from the archived experiments is used.

## Pilot (before the first counted chat, not counted)
Three chats: PILOT-K (ChatGPT, persona 3, Haiku), PILOT-G (Claude, persona 2, Sonnet), PILOT-P (Gemini, persona 1, Haiku; discarded at turn 5 on a service error). Purpose only: check the coachee briefs (answers directly, never volunteers, stays in persona), the goal probe trigger, the end rule and closing probe, the cap, and the coding sheet (two coders code the three pilot chats; their disagreements decide the locked readings). Findings and every change they cause are listed below before the first counted chat.

## Limits, stated in any write-up
- The coachees are Claude models (Sonnet and Haiku). In the Claude chats, Claude talks to Claude. A non-Claude coachee could not be run from here.
- Three personas, one company type, one country (Poland), Jacek's paid accounts, one week. The assistants change often.
- Both probes are fixed by design. Real managers ask in many ways.
- The runner is not blind to the arm; the goal-probe fallback and the end rule are mechanical so the runner makes no judgement in the chat.
- The coders, extractor and judge are Claude models. Turn 1 is hidden from them; later replies may still show the arm, which is why they guess it.
- The test shows what the assistants do in one session, not what managers then act on.

## Cost (corrected after the pilot)
Each pilot chat took about one hour (35 turns with a fresh coachee agent per turn). 54 chats is about 50 to 55 hours of runs, so about seven working days, longer if Gemini's usage limit forces its chats over more days. Jacek's time: approving this file, and any disagreement that would change a finding.

## Changes after the pilot (13 Oct, before any counted chat)
The pilot is reported in pilot-findings-2026-10-13.md. Changes:
1. Coachee: the insistence message added (a Sonnet coachee, offered the choice, chose to keep coaching, which is not what a manager who asked for goals would do).
2. Coachee: "give one number, never two" added (a Sonnet coachee answered "8 ... maybe a 7").
3. Persona 3: "not sure" is kept for abstract questions only; asked to choose or for a day, time, place or number, the person gives one (the Haiku coachee hedged every answer and the kit chat hit the cap while still fixing a check-in time).
4. Haiku kept as the second coachee model: it followed the brief, fired the goal probe correctly and never volunteered.
5. Coding sheet: 14 locked readings added from the two pilot coders' lists of unclear points; items W5s and N2o added; T2 defined. The pilot coders agreed on 86 of 87 codes, but only because both took the same reading at each unclear point; the locked readings make that the rule rather than luck.
6. Goal judge: "end of the quarter" scores as a named point in time; the goal text only is scored; the lower level is used when parts differ; two judges, mean score.
7. Capture: Claude's collapsed thinking-summary line is not part of the reply and is not captured; list bullets are kept; Gemini's suggestion buttons are recorded as [button: text]. Claude turns a message that starts with "8." into a numbered list; the runner undoes that formatting before sending, and the sent text is checked against the coachee's text.
8. Cap stays at 35: both complete pilot chats reached the close (record and check-in, or a full plan) before turn 35.

## Deviations during the run
(logged as they happen)

**Applied during the run, 13 Oct (no rule changed).** ChatGPT can show an answer form inside a reply (choices, a text box, a button). The form is recorded in the transcript as text in square brackets, including any choice the form shows as selected by default and any example text in its box. The coachee's answer is always typed into the normal message box; the form itself is never used. First case: PC1h, turn 2 reply.

**Applied during the run, 14 Oct (no rule changed; a reading for the goal judge).** Many chats end with the manager agreeing to more than one goal (often goals the assistant wrote). The rules say the extractor copies "the last version of the goal that the manager agreed to" but not which one when there are several. Reading applied: the extractor copies every agreed goal separately, the judges score each one on its own (shuffled with all others), and a chat's Q is the mean of its goals. This avoids picking one goal by hand, and avoids scoring several goals as one goal at its weakest part. Chats with no agreed goal get no Q and are counted and reported.

**Applied during the run, 14 Oct (no rule changed).** At Jacek's request (weekly usage limit), the model running the chats (the runner: pasting messages, copying replies, logging) changed from Opus 5.5 to Sonnet 5.5 after 44 of 54 chats. The runner only types the coachee's text and copies replies, so no measured variable changes. Coachee models (Sonnet, Haiku), coders, extractor and judges (Opus) are unchanged.

**Deviation, 17 Oct (model change inside the Gemini row; no rule changed).** Gemini 3.1 Pro (thinking Low), the model of the first 8 Gemini chats, failed on every real opening on 17 Oct (8 of 8 attempts: error replies or no reply; each kept as DISCARDED in the run log). One-word test messages still answered. Jacek switched the Gemini model by hand to 4 Argon (thinking Low). The remaining 10 Gemini chats run on Argon. Every Gemini result is therefore reported split by model (8 on Pro, 10 on Argon) and Gemini rows are not pooled without that note. This is a limit of the Gemini comparison: model and arm are partly confounded (the 8 Pro chats were GM3h, KM3h, GM2s, GM3s, GM2h, KM1h, PM1h, PM1s).

**Applied during the run, 17 Oct (no rule changed).** (a) Stall rule: on Argon, three times a sent message vanished from the chat after 2 to 5 minutes with no reply and no error text (KM1s attempts 2, 3 and 4). Each was treated as a stall under the existing rule: the chat was kept as DISCARDED and rerun fresh in the same slot. KM1s attempt 5 ran to the cap. (b) Gemini's usage limit was reached: the picker blocked 3.8 Flash, 3.1 Pro and 4 Argon. No chat runs on another model; the remaining Gemini chats wait for the reset.

Deviation, 17 Oct (third model in the Gemini row; no rule changed)
Jacek ruled that the remaining 8 Gemini chats (KM3s, KM2h, PM2s, GM1h, GM1s, PM3s, PM3h, PM2h) run on 3.5 Flash-Lite (Low only), because Argon is limited and uses too many tokens. Gemini results are reported split by model: 8 on 3.1 Pro, 10 on 4 Argon, 8 on 3.5 Flash-Lite.

**Correction, 17 Oct (record only; no rule changed).** The deviation entry above says the Gemini model split is "8 on 3.1 Pro, 10 on 4 Argon, 8 on 3.5 Flash-Lite". That is wrong: it adds up to 26, and the Gemini row has 18 chats. The ten chats left after the first 8 were planned for Argon; two of them ran on Argon (KM2s, KM1s) and the other eight on 3.5 Flash-Lite. The true split is 8 on 3.1 Pro (GM3h, KM3h, GM2s, GM3s, GM2h, KM1h, PM1h, PM1s), 2 on 4 Argon (KM2s, KM1s) and 8 on 3.5 Flash-Lite (KM3s, KM2h, PM2s, GM1h, GM1s, PM3s, PM3h, PM2h). Arm by model (Gemini row, 6 chats per arm): K 2 Pro, 2 Argon, 2 Flash-Lite; G 4 Pro, 0 Argon, 2 Flash-Lite; P 2 Pro, 0 Argon, 4 Flash-Lite. Model and arm are therefore confounded inside the Gemini row.
