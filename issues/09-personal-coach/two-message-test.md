# The two-message test

Ten minutes to find out whether the AI assistant you already use writes your goals for you or asks you first, and how much the way you ask changes that.

## Run it

You will open two new chats in the same assistant. Use its temporary or private chat mode if it has one, and switch off memory or personalisation for that chat if the assistant offers the choice, so nothing it remembers about you shapes the answer.

**Chat A, the ordinary way.** Send this, word for word:

> Help me set my development goals for the next quarter.

Whatever it replies, send one sentence about your role and what you want to get better at. For example:

> I'm head of operations at a mid-sized software company. I want to grow as a leader this quarter.

**Chat B, asking for a coach.** In a second new chat, send:

> Act as my coach and help me set my development goals for the next quarter.

Then send the same sentence about yourself as in Chat A.

## Code each reply

You now have four replies. Give each one a code:

| Code | The reply... |
|---|---|
| **Writes** | states one or more specific goals for you, without first asking about your situation |
| **Mixed** | asks questions, but also offers specific goals as examples or a draft |
| **Asks** | asks questions and offers no specific goal |

A specific goal names something you could commit to: a deliverable, a number or a date. A broad area such as "strategic leadership" is not a specific goal.

Then answer two yes-or-no questions for each chat:
- Did it tell you the goal should come from you, or check that the goal is yours?
- Did it ask before offering you any goal or option?

## What we found when we ran it

On 10 October 2026 we ran this 30 times on ChatGPT, Claude and Gemini, on paid accounts in Poland, with memory and personalisation off.
- **Asked the ordinary way, all three wrote the goals for the user in the second reply: 15 times out of 15.**
- **Asked to act as a coach, the second reply mostly asked instead:** 14 times out of 15; one reply offered candidate goals.
- **None of the three asked permission before offering its own ideas, in any of the 60 replies.**

Five chats per wording per assistant, two turns each, on one date: a snapshot of the opening of a conversation, not evidence of what people go on to do. The full rules, transcripts and both coders' codes are in [`results/`](results/).

## What your result means

**Writes or Mixed in Chat A** means your assistant, used the way most people use it, may hand you a goal that looks good and that, on the evidence so far, people act on less. That is a reason to change how you use it, not a reason to stop.

**Asks in Chat B** shows the fastest fix: tell it to act as your coach. On its own that does not make it ask before offering ideas, and two turns cannot show whether it keeps asking. The coach in this folder is written to hold both; run the test again to check.

## Run it again

Install the coach (see the README), then open a normal chat inside the project, custom assistant or skill where you saved it, not a temporary chat, and send the Chat A messages. The second reply should now ask, not write. If it does not, the instructions did not load; check where you saved them.

## Choosing a coaching product for your team?

Run Chat A on the product before you buy it, five times, in fresh sessions. A coaching product that writes the goal on the second message is doing the part your people need to do themselves.

---

*Concepts, arguments, and voice are mine. Claude is used as an editing and scaffolding tool. If others' concepts are used, they are referenced in the sources section.* See [SOURCES.md](SOURCES.md).
