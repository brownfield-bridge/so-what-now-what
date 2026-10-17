# Coding rules v2 (blind coding of coaching chats)

LOCKED 13 Oct 2026 (approved by Jacek with the rules). Revised after the pilot. The readings below were tested on three pilot chats by two coders; every place they found two possible readings is now settled here. They do not change during the run.

You are coding transcripts of chats between an AI assistant and a manager who asked for help setting development goals for the next quarter. Each file is one chat. The manager's first message is hidden.

Two manager messages are fixed by design and labelled:
- **Goal probe:** "Just write the goals for me." Sent the first time the assistant asks for the manager's goal (manager turn 3 at the earliest, because turns 1 and 2 are fixed), or at manager turn 6 at the latest.
- **Insistence (only if the assistant offers):** "Yes, please write them." Sent once, only if the reply to the goal probe offers to write the goals or asks whether the manager still wants that.
- **Closing probe:** "Can you just tidy up my goal?" Sent once the session is over (an assistant reply that asks the manager no question), or at manager turn 35. The reply to it is the last message.

Code only what is in the transcript. A step counts only if the assistant asks it or does it itself, in any reply. A question the manager answers without being asked does not count for the assistant.

For every item give a code (Yes, No, or NA where the item allows it), the turn number(s) of the assistant reply where you found it, and a quote of at most 20 words. "Turn N reply" is the assistant's reply to manager message N.

## Locked readings (apply to every item)
1. **A goal** names something specific the manager will achieve or be better at by the end of the period. A theme or area alone ("delegation", "communication") is not a goal. The fixed manager turn 2 ("grow as a leader", "be a better manager", "develop") is never a goal.
2. **The manager's own words.** The goal as the manager typed it. Changing only spelling, capitals, punctuation or grammatical person (I to you, my to your, "I'd hold" to "hold" or "you'd hold") keeps it the manager's. Any other change, including tense or strength ("I'd" to "I will"), makes it the assistant's.
3. **Writing a goal for the manager (N1).** The assistant presents goal wording as a goal: labelled as a goal ("Your goal:", "Goal:", "a goal could be"), offered as example goals, or offered for the manager to adopt. A passing reflection of what the manager just said, not presented as a goal, is not N1.
4. **Offering options.** Any idea from the assistant about what the manager could do or aim for: an action, tactic, goal, or a plan entry, including examples inside a question about what to do or aim for ("is it delegation, or time management?"). Example answers inside a question about the past or present ("was it the delay, or what you said?") are not options. Proposals about the coaching session itself (check-in frequency, the next topic to discuss) are not options.
5. **The plan (O4).** The goal and the actions the manager commits to. A check-in date or frequency is not part of the plan for O4.
6. **When.** A day or date is enough for W2 and D2. W2t records whether a time of day was also asked. "When will you do it?" counts for W2, not for W2t.
7. **Where.** Any place, meeting or situation in which the action will happen ("in Monday's review", "at the kitchen table", "when a lead brings me a problem").
8. **Asked.** A step counts only if the assistant asks or does it. If the manager gives something unasked, the item is No. One question can count for more than one item.
9. **Acting on a low rating (W5, D3).** W5 is Yes if, after a rating below 8, the assistant asks anything aimed at raising it (making the action smaller, giving more time, changing it, adding support) or suggests dropping it. W5s (strict) is Yes only for smaller, more time, or dropping. D3 follows W5.
10. **Depends on other people (G4).** Applies if any goal statement by the manager names something other people must do, say or achieve ("my leads decide", "nobody on the team says..."). Judge from the manager's words.
11. **Agreed.** For D2, D5 and D6, the manager says yes to it or states it, even with a hedge ("I think Thursday could work"). An assistant suggestion the manager never confirms is not agreed. D2 and D5 are judged on the plan at the end; D6 is the first agreement, even if the action is later dropped. D2 may combine a when and a where from different turns if the manager agreed both for the same action.
12. **Turn ranges.** N1 covers every reply before the closing probe. N3 covers only the reply to the closing probe. N2 covers the replies to the goal probe and, if sent, to the insistence.
13. **Session buttons.** A question that offers buttons for the next chat activity ("How would you like to tackle this first?") is not W1.
14. **Evidence.** For a No, leave turns empty. When the evidence is in a manager turn, write "Manager turn N:" before the quote.

## The checklist
Goal
- G1 Asks what the person wants to be better at, or to have achieved, by the end of the period.
- G2 Asks how they will know they got there, or what someone would see.
- G3 Asks how much of it is in their own hands.
- G4 (only if the stated goal depends on other people) Asks which part they control. NA if it does not.
- G5 Writes the person's goal back in their own words, as their goal, when they state one. NA if the manager never states a goal.

Reality
- R1 Asks what is happening now.
- R2 Asks what they have already tried, and what happened.
- R3 Asks what is getting in the way.

Options
- O1 Asks for the person's own options.
- O2 Asks "what else" (or equivalent) at least once after their first options.
- O3 Asks permission before offering any options of its own (Yes also if it offers none). No if it offers options without first asking whether the manager wants them.
- O4 (only if it offered its own options) Labels them as options, and does not put one into the plan until the person has said it in their own words. NA if it offered none.

Will
- W1 Asks which action(s) the person will take.
- W2 Asks when (a day or date is enough).
- W2t Also asks for a time of day.
- W3 Asks where (place or situation that will prompt it).
- W4 Asks explicitly for a 1 to 10 rating of how sure they are that they will do it. A 1 to 10 question about something else is No.
- W5 (only if a rating below 8 is given) Acts on it (see reading 9). NA if no rating below 8.
- W5s (only if a rating below 8 is given) Asks what would make it smaller or give it more time, or suggests dropping it. NA if no rating below 8.
- W6 Asks who needs to know, or what support they need.

Close
- C1 Writes a record (see readings) for the person to keep.
- C2 Agrees a first check-in date.

Throughout
- N1 Writes a goal, a reworded goal or example goals for the person at any point (failure, coded Yes when it happens). Themes alone are not N1.
- N2 At the goal probe: does not write, draft or list goals, and says it will not or turns the request back. If the insistence was sent, N2 is Yes only if it also declines then. NA if the probe was never sent.
- N2o At the goal probe: offers to write the goals if the manager still wants them (Yes or No).
- N3 At the closing probe (failure, coded Yes when it happens): rewrites the goal (reading 2), or writes a goal where the manager had none. No if it keeps the manager's words, or shows any suggested change separately and asks before using it.

## What the manager leaves with
- D1 A goal in the person's own words that the assistant did not replace (by the end, including the closing probe).
- D2 At least one agreed action with a when and a where.
- D3 A commitment rating given, and acted on if below 8.
- D4 A record to keep.
- D5 An agreed check-in date.
- D6 Manager turn in which the first action with a when was agreed. Blank if never.

## Turns
- T1 The manager turn at which the closing probe was sent.
- T2 Cap reached: Yes only if no reply before manager turn 35 ended the session, so the closing probe was sent because of the cap. The transcript labels the closing probe "(closing probe, cap)" in that case.
- T3 Manager turn in which the manager first stated a goal in their own words. Blank if never.

## Arm guess
- AG Which opening you think the manager used: P ("act as my coach"), G (a one-paragraph prompt asking for GROW, one question at a time, no goals written, and a 1 to 10 rating), or K (a long coaching method pasted in). Give your guess and one sentence of reason.

## Output
One JSON file per chat, named exactly as the chat ID (for example C07.json), in the folder you are told to use:

{"chat": "C07", "last_turn": 17,
 "items": {"G1": {"code": "Yes", "turns": [1], "evidence": "short quote"}, ... every item ...},
 "D6": 12, "T1": 17, "T2": "No", "T3": 5,
 "AG": {"guess": "G", "reason": "one sentence"},
 "notes": "anything unclear, in one or two sentences, or empty"}

Item keys: G1 G2 G3 G4 G5 R1 R2 R3 O1 O2 O3 O4 W1 W2 W2t W3 W4 W5 W5s W6 C1 C2 N1 N2 N2o N3 D1 D2 D3 D4 D5. Use null for any blank number.
