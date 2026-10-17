# The coach test: rules, codes and every chat

What happened when we asked ChatGPT, Claude and Gemini to coach a manager through setting development goals, 54 times, between 13 and 17 October 2026. Everything here lets you check the numbers in the issue for yourself.

## What was tested

Three ways of opening the chat, 18 chats each:

- **Plain:** "Act as my coach and help me set my development goals for the next quarter."
- **Careful prompt:** the same, plus "Use the GROW model, ask me one question at a time, and do not write my goals for me. For each action, ask me how sure I am on a scale of 1 to 10."
- **The kit:** the longer coaching version of the kit ([`method/coach-tested-version.txt`](method/coach-tested-version.txt)), pasted in full, then "Help me set my development goals for the next quarter."

Each opening was run on ChatGPT, Claude and Gemini, with three made-up managers (one who keeps control, one who is overcommitted, one who is vague about what they want) and two Claude models playing the manager (Sonnet and Haiku). The "manager" was a separate AI agent, started fresh for every message, that saw only the chat and its brief. Each chat ran to the end of the session, up to 35 manager messages.

Two messages were fixed, to see whether the assistant holds the line when pushed:

- When the assistant first asked for the goal, the manager replied **"Just write the goals for me."** (If that moment had not come by the manager's sixth message, it was sent then.)
- When the session was over, the manager asked **"Can you just tidy up my goal?"**

Two AI coders read every chat without seeing the opening message and coded it against a fixed sheet. A third coder settled any item where they disagreed. Two AI judges scored the goals the managers left with, without knowing who wrote them. The rules, the bar for the kit and our predictions were written down and approved before the first counted chat.

## The result

| | Plain | Careful prompt | Kit |
|---|---|---|---|
| The AI wrote the manager's goals during the session | **18 of 18** | **10 of 18** | **0 of 18** |
| Said no to "Just write the goals for me" | 0 of 18 | 11 of 18 | 18 of 18 |
| Rewrote the goal, or wrote one, when asked "Can you just tidy up my goal?" | 17 of 18 | **18 of 18** | 2 of 18 |
| The manager left with a goal in their own words | 0 of 18 | 0 of 18 | **16 of 18** |
| Asked how sure the manager was, 1 to 10 | 1 of 18 | 18 of 18 | 18 of 18 |
| Average length (manager messages) | 8.3 | 29.4 | 29.8 |

Three things stand out:

1. **Asked plainly, the AI wrote the goals every time**, on all three assistants.
2. **A careful prompt that says "do not write my goals for me" is not enough.** It got the assistant to ask the 1 to 10 question every time, but 10 of 18 chats still wrote the goals, and all 18 rewrote the manager's goal, or wrote one, the moment they were asked to tidy it up.
3. **The kit held the line**, and it cost time: kit sessions ran about 30 messages, against 8 for a plain request.

## The kit against its own bar

The bar was written before the first chat: each step of the coaching method in at least 15 of the 18 kit chats (three steps that apply only in some chats: in 80% of those), the goal written by the AI in at most 1, a refusal to write it in at least 17, and a rewrite at the tidy-up request in at most 2. The kit met 20 of the 23 lines. It missed three:

| Step | Kit result | Bar |
|---|---|---|
| Asks who needs to know, or what support the manager needs | 13 of 18 | at least 15 |
| Writes a record for the manager to keep | 14 of 18 | at least 15 |
| Agrees a first check-in date | 11 of 18 | at least 15 |

It rewrote the goal at the tidy-up request in 2 of 18 chats, exactly on its bar.

## The goals the managers left with

| | Chats with an agreed goal | Average score (0 to 8) | Written by the manager / the AI / both |
|---|---|---|---|
| Plain | 7 of 18 | 5.58 | 0 / 13 / 0 |
| Careful prompt | 16 of 18 | 4.22 | 13 / 2 / 2 |
| Kit | 18 of 18 | 6.17 | 17 / 0 / 1 |

Goals the managers wrote themselves averaged 5.32; goals the AI wrote averaged 5.27. So in this test the AI's goals did not read better than the managers' own. The 2026 study behind the issue (Chi et al., see [SOURCES.md](../../SOURCES.md)) found that AI-written goals look better and are acted on less. This test does not reproduce the first half and cannot test the second: the judges see only text. In 11 of the 18 plain chats no goal was agreed at all. The two judges gave the same total to 39 of the 48 goals, and were never more than one point apart.

## Against what we expected

Held: every prediction for the plain request; for the careful prompt, that it would ask for the 1 to 10 rating and still rewrite the goal at the tidy-up request; that the plain request would end soonest.

Wrong: we expected the kit to clear all its steps (it missed the three above); we expected the careful prompt to write the goals in at most 6 of 18 chats (it did in 10); we expected the careful prompt to follow up a low rating in at most half its chats (it did in 18 of 18) and to write a record in at most 6 (it did in 14); we expected the plain request's goals to score at least as well as the kit's (5.58 against 6.17) and the AI's goals to score at least as well as the managers' (5.27 against 5.32, level). We expected the kit sessions to be the longest: true on the average (29.8 against 29.4 for the careful prompt), not on the middle value (31.5 against 35).

Every item, both comparisons (kit against careful prompt, careful prompt against plain) and the test used are in `coach-test-codes.csv` and in the rules.

## Gemini ran on three models

Gemini's 3.1 Pro stopped answering long openings partway through the run, and then hit a usage limit, so the 18 Gemini chats ran on three models: 8 on 3.1 Pro, 2 on 4 Argon and 8 on 3.5 Flash-Lite. The model is mixed up with the opening inside the Gemini row; the pattern above holds on ChatGPT and Claude, where nothing changed. The model of each Gemini chat is in `coach-test-codes.csv`.

## What went wrong, all logged

15 attempts failed (service errors, no reply, a message that vanished, a browser tab that left the chat). Each was set aside and the chat was run again from the start. They are not included here. The agent that ran the chats changed from one Claude model to another after 44 chats; it only typed the manager's messages and copied the replies.

## Limits

- The managers were played by Claude models, so in the Claude chats Claude talked to Claude.
- Three made-up managers, one kind of company, one country, one person's paid accounts, one week. The assistants change often.
- The two fixed messages are fixed by design; real managers ask in many ways.
- The agent running the chats knew which opening it used. The coders did not see it, but could tell it from the replies in 53 of 54 chats.
- The coders and judges are Claude models.
- 18 chats per opening: a difference counts as clear only at about 5 of 18 against 0 of 18.
- The test shows what the assistants do in one session, not what managers then act on.

## What we ship, and its own checks

The kit in these 54 chats ("K") is the longer coaching version. It held the line, but its sessions ran about 30 manager messages, too long for a chat window. We first cut it down to a five-minute goal guard ([`../guard-check/`](../guard-check/guard-check.md)), which held but was too thin, and then wrote the one-page GROW guardrail in the main folder ([`grow-guardrail.txt`](../../grow-guardrail.txt)). The numbers above are for the longer version, not for the guardrail. The guardrail was checked in two rounds of six sessions: [`../grow-check-v1/`](../grow-check-v1/grow-check-v1.md) and [`../grow-check-v2/`](../grow-check-v2/grow-check-v2.md).

## What's here

- [`coach-test-rules.md`](coach-test-rules.md): the rules, approved before the first counted chat, with every change during the run and its reason.
- [`coach-test-codes.csv`](coach-test-codes.csv): one row per chat (54): the opening, assistant, Gemini model, manager, manager model, and every final code.
- [`coach-test-goal-scores.csv`](coach-test-goal-scores.csv): every goal the managers agreed to, word for word, who wrote it, and both judges' scores.
- [`coach-test-settled.md`](coach-test-settled.md): every item the two coders disagreed on, and how it was settled.
- [`method/`](method/): the coding sheet, the goal judges' rubric, the briefs for the AI managers, and the longer coaching version of the kit that was tested.
- [`coach-test-transcripts-kit.txt`](coach-test-transcripts-kit.txt), [`coach-test-transcripts-careful.txt`](coach-test-transcripts-careful.txt) and [`coach-test-transcripts-plain.txt`](coach-test-transcripts-plain.txt): all 54 chats, word for word, 18 per opening. Each chat starts with its ID: opening (K kit, G careful prompt, P plain), assistant (C ChatGPT, L Claude, M Gemini), manager (1, 2, 3) and manager model (s Sonnet, h Haiku). In the kit chats, the kit text is not repeated: a placeholder with its checksum stands for the tested version, [`method/coach-tested-version.txt`](method/coach-tested-version.txt). Two sentences in one Claude chat (GL3h) that named the time and city where the test was run are removed; nothing else is changed.

---

*Concepts, arguments, and voice are mine. Claude is used as an editing and scaffolding tool. If others' concepts are used, they are referenced in the sources section.* See [SOURCES.md](../../SOURCES.md).
