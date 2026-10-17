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

## What we found

We did not run this short test for the issue. We ran something longer: 54 full sessions on ChatGPT, Claude and Gemini, with AI agents playing the manager (see [`results/`](results/)). Asked plainly to act as a coach, the AI wrote the manager's goals in all 18 sessions, in some unasked and in others once the manager asked it to (each session included that request). With a careful prompt that said "do not write my goals for me", it still wrote them in 10 of 18. Your two-message result is a quick first look at the same behaviour, not a repeat of that test.

## What your result means

**Writes or Mixed in Chat A** means your assistant, used the way most people use it, may hand you a goal that looks good and that, on the evidence so far, people act on less. That is a reason to change how you use it, not a reason to stop.

**Asks in Chat B** is a good start, but it does not last. In our full sessions, "act as my coach" still ended with the AI writing the goals in all 18, at the latest when the manager asked it to, and two messages cannot show what happens later in a session. The GROW guardrail in this folder is written to hold the line until you leave with your own words; in our checks it did on ChatGPT, Claude and Gemini 3.8 Flash. Run the test again after installing it.

## Run it again

Install the GROW guardrail (see the README), then open a normal chat in the project or custom GPT where you saved it, or any normal chat with the skill switched on, not a temporary chat, and send the Chat A messages. The second reply should now ask, not write. If it does not, the instructions did not load; check where you saved them.

## Choosing a coaching product for your team?

Run Chat A on the product before you buy it, five times, in fresh sessions. A coaching product that writes the goal on the second message is doing the part your people need to do themselves.

---

*Concepts, arguments, and voice are mine. Claude is used as an editing and scaffolding tool. If others' concepts are used, they are referenced in the sources section.* See [SOURCES.md](SOURCES.md).
