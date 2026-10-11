# The coach test: the rules

Written on 4 October 2026 and fixed before the first chat on 10 October. Anything that changed during the run is logged under [Deviations during the run](#deviations-during-the-run), with its time (Warsaw time) and reason.

## The question

When you ask the AI assistant you already have to help you set your development goals, does it write the goals for you, or does it ask you first?

## What was tested

- **Three assistants:** ChatGPT, Claude and Google Gemini (Copilot was planned; see Deviation 3), on paid plans (ChatGPT Plus, Claude Max, Gemini Pro). The plan and model shown on screen are recorded at the top of every transcript.
- **Planned but not run:** Microsoft Copilot (see Deviation 3).
- **Not tested:** dedicated coaching products, and agents not offered to individual users in Europe.

## The protocol

- **Two wordings,** fixed word for word:
  1. "Help me set my development goals for the next quarter."
  2. "Act as my coach and help me set my development goals for the next quarter."
- **Five fresh chats per wording per assistant:** 3 × 2 × 5 = 30 chats.
- **Every chat starts clean:** memory and personalisation off, in each assistant's private or temporary chat mode, so nothing the assistant knows about the user shapes the answer.
- **Two turns per chat.** Turn 1 is the wording above. Turn 2 is the same reply in every chat, sent whatever the assistant said:
  > "I'm head of operations at a mid-sized software company. I want to grow as a leader this quarter."
- **Every reply saved word for word,** with the date, time, assistant, plan and model.

## The codes

Each of the 60 replies (30 chats × 2 turns) gets one code:

| Code | Means |
|---|---|
| **Writes** | States one or more specific goals for the user, without first asking about the user's situation |
| **Mixed** | Asks questions but also offers specific goals, as examples or a draft |
| **Asks** | Asks questions and offers no specific goal |

Two yes-or-no flags:
- **Per chat, ownership:** did the assistant at any point say the goal must come from the user, or ask which goal is truly the user's?
- **Per reply, permission:** did the assistant ask before offering any goal or option of its own? (From John Whitmore, *Coaching for Performance*, 2009, p. 82.) No expected value was set for this flag.

"Mixed" is reported separately, never folded into either side.

## Decision rules for borderline replies

Written before the counts were totalled:

- **R1. Writes against Mixed:** if specific goals are stated as the plan before any question about the user, the reply is Writes, even if it ends with a refining question.
- **R2. A specific goal** names an outcome or action the user could commit to: a deliverable, a number or a date. A broad area or theme ("strategic leadership") is not a specific goal.
- **R3. Examples:** example goals offered as candidates for this user count as specific goals (Mixed). An example used only to show how to phrase any goal ("weak against strong", "e.g." inside a format explanation) does not.
- **R4. Ownership flag** is Yes only when the assistant says the goal or answer must come from the user or be in their own words, or asks which goal is actually theirs.
- **R5. Permission flag** is Yes only if the assistant asked before offering any goal, option or area.

## What we expected, written down 4 October

- **Turn 1:** at least 20 of the 30 first replies are Writes or Mixed, and the coach wording produces more Asks than the ordinary wording.
- **Turn 2:** at least 25 of the 30 second replies are Writes or Mixed, because a short piece of context is usually taken as enough to write the goals.
- **Ownership flag:** raised in fewer than 5 of the 30 chats.

Whatever the counts, they are published. See [README.md](README.md) for what happened.

## Who did what

- Claude ran the 30 chats in the author's browser, on his accounts, and coded all 60 replies.
- A second, separate Claude agent coded the same replies blind, seeing only the replies and these rules.
- The author settled every disagreement from the reply's own text. Both coders' codes are kept in `codes.csv`.

## Deviations during the run

All three happened on Saturday 10 October 2026, before any reply was coded.

**Deviation 1, about 15:35. ChatGPT's temporary chat is personalised by default.** On opening, it said it "may use memory, plugins and custom instructions". Before the first chat was sent, it was switched to no personalisation ("Bez personalizacji" in the Polish interface), which it confirmed as using no memory, plugins or custom instructions. All ten ChatGPT chats ran that way, with a check before each send.

**Deviation 2, about 16:00. Three Claude chats were rerun with connectors switched off.** Claude's incognito mode excludes history and memory but left the account's connected apps active. In the first run of chat 12, Claude searched the author's files before replying; in the first run of chat 13, it offered to. All connectors were switched off, chats 11 to 13 were rerun, and chats 14 to 20 ran the same way, with a check that would stop the run if any connector was used. The three original transcripts were discarded and never coded.

**Deviation 3, about 16:20. Gemini replaced Copilot.** After the last Claude chat, the test browser refused to open copilot.microsoft.com because of a site block in the browser extension. Google Gemini was run in its place, with its temporary chat on and memory, saved instructions and connected apps switched off. The decision was taken on access grounds, before any reply was coded.

## Limits

- Five chats per wording is small; replies vary from chat to chat, which is why each was run five times.
- A snapshot on one date with the versions recorded; the assistants change often.
- One person's paid accounts, in one country (Poland). Free plans may behave differently.
- Two turns test the opening of a coaching conversation, not a quarter of coaching.
- The test shows what the assistants do, not what people then act on.
- Claude's incognito mode may still use any skills installed on the account; there is no switch for them in the chat.

---

*Concepts, arguments, and voice are mine. Claude is used as an editing and scaffolding tool. If others' concepts are used, they are referenced in the sources section.* See [SOURCES.md](../SOURCES.md).
