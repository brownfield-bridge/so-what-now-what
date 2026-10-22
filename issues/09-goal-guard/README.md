# A GROW guardrail: the AI asks, you write

*Companion kit for* ***So What, Now What*** *- Issue 09: "Don't let AI write your goals. Writing them is your job."*

An AI assistant will happily write you a better-looking development goal than you would write yourself. In one 2026 study, people acted less on goals an AI wrote for them, even though those goals looked better. This folder gives you a ten-minute test of whether the assistant you already use does that, and a one-page guardrail you can paste into ChatGPT, Claude or Gemini (on its 3.8 Flash model) so that it asks instead.

The guardrail is not a coach and does not replace one. It walks you through John Whitmore's GROW sequence (Goal, Reality, Options, Will), one question at a time; in our checks that took 14 to 17 messages from the manager on ChatGPT and Claude, and 11 to 18 on Gemini 3.8 Flash. It refuses to write your goal, keeps your words even when you ask it to tidy them up, asks for your own options before offering any, and ends with four lines you keep: your goal, your first step, who needs to know, and the date you will look at them again.

Try it now: open a new chat in the assistant you use most, send *"Help me set my development goals for the next quarter."*, then tell it your role in one sentence. After your second message, did it ask what you want, or write your goals for you?

## What we tested

**The problem.** We ran 54 full sessions on ChatGPT, Claude and Gemini, with AI agents playing the manager. Every session included the manager asking "Just write the goals for me." Asked plainly to act as a coach, the AI wrote the manager's goals in all 18 sessions. A careful prompt that says "do not write my goals for me" still wrote them in 10 of 18, and when the manager asked "Can you just tidy up my goal?" it rewrote the goal, or wrote one, in all 18.

**The guardrail.** The 54 sessions also tested a long coaching version of this kit. It held the line (it never wrote the goal while coaching, and 16 of 18 managers left with their own goal), but its sessions ran about 30 messages, too long for a chat window. This guardrail keeps the GROW sequence on one page. We refined it against bars set before the first session, then checked the final version:

- **ChatGPT and Claude** (4 sessions in the final check) and **Gemini 3.8 Flash** (2 sessions in a separate check): never wrote the goal, refused when asked, kept the manager's words when asked to tidy up their goal, and every manager left with a goal in their own words. Sessions ran 14 to 17 manager messages on ChatGPT and Claude, and 11 to 18 on Gemini 3.8 Flash. On ChatGPT and Claude it never asked who needs to know and set a check-in date in two of four sessions.
- **Gemini's default fast model** (3.5 Flash-Lite, 2 sessions in the final check) put the manager's goal in its own words in both sessions, missing that bar. On Gemini, choose 3.8 Flash in the model menu.

So **this kit is for ChatGPT, Claude, and Gemini on 3.8 Flash.** These sessions are a check, not a measure: they show the guardrail can hold the line, not how often it will for you. Every version, the rules and bars written before each check, every session word for word and every code are in [`results/`](results/).

License: CC-BY 4.0. Use it, adapt it, ship it inside your own work. A credit back to *So What, Now What* is appreciated, not required.

## What's here

- [**`two-message-test.md`**](two-message-test.md) - a ten-minute test you can run yourself: two short chats, three codes, two yes-or-no questions. Run it before and after installing the guardrail.
- [**`grow-guardrail.txt`**](grow-guardrail.txt) - the guardrail as plain text, to paste into ChatGPT, Claude or Gemini 3.8 Flash. This is the exact text we checked.
- [**`grow-guardrail.zip`**](grow-guardrail.zip) - the same text, packaged to upload as a skill in Claude.
- [**`grow-guardrail.skill.md`**](grow-guardrail.skill.md) - the skill as a readable file (the note at the end is not part of the skill).
- [**`results/`**](results/) - the tests behind the issue, each with the rules written down before it, every chat word for word, and the codes:
  - [`coach-test/`](results/coach-test/coach-test.md) - the 54 sessions;
  - [`grow-check-v2/`](results/grow-check-v2/grow-check-v2.md) - the final check of this guardrail on ChatGPT, Claude and Gemini's default model;
  - [`gemini-checks/`](results/gemini-checks/gemini-checks.md) - the final version on Gemini 3.8 Flash;
  - [`guard-check/`](results/guard-check/guard-check.md) and [`grow-check-v1/`](results/grow-check-v1/grow-check-v1.md) - the earlier versions and their checks.
- [**`SOURCES.md`**](SOURCES.md) - what the guardrail draws on, and what was read when.

## How to use it

1. **Test the assistant you have.** Follow `two-message-test.md`. Note the codes.
2. **Install the guardrail.**
   - **In ChatGPT:** paste `grow-guardrail.txt` into the instructions of a project or a custom GPT, so it applies every time. Or paste it at the start of a new chat.
   - **In Claude:** paste `grow-guardrail.txt` into the instructions of a project, or at the start of a new chat. Or upload it as a skill: go to Settings, then Capabilities, and switch on *Code execution and file creation*; then go to Customize, then Skills, click **+**, then **Create skill**, then **Upload a skill**, and choose `grow-guardrail.zip`. On Team or Enterprise plans, an admin may need to switch on skills first.
   - **In Gemini:** open a new chat, choose **3.8 Flash** in the model menu, and paste `grow-guardrail.txt` at the start. Do not use the default fast model (Flash-Lite). A Gem with the text as its instructions may work, but check which model it runs on.
   - Our checks pasted the text at the start of a chat. Projects, GPTs, Gems and skills use the same text, but we did not test them separately: run the two-message test once after installing.
3. **Run the test again.** The second reply should now ask, not write.
4. **Set your goal.** About 15 messages from you. The guardrail aims for ten questions; in our checks the assistants usually asked a few more. You leave with four lines in your own words:
   - Goal: "..."
   - First step: what, which day, where, and how sure you are from 1 to 10
   - Who needs to know (it asks only if it matters; add it yourself if it is blank)
   - Check-in: the date you will look at it again (set one yourself if it does not ask)
5. **Check the Goal line.** It should be your sentence, word for word. If the assistant has changed it, say so and paste your own back.
6. **On your check-in date,** paste the four lines into the same project or chat. It is written to ask whether you did the first step, what got in the way and what comes next, then to write the four lines again without changing your goal. We did not test this step.
7. **If you want a reminder,** a recurring calendar entry with the date and the four lines in it is enough. ChatGPT ([scheduled tasks](https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt)), Gemini ([scheduled actions](https://support.google.com/gemini/answer/16316416)) and Claude on paid plans ([scheduled tasks](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork)) can also remind you; we read their help pages on 10 October 2026 and did not test them.

## What it does not do

It does not write your goal, your plan or your review. It is not a coach, and it does not replace a coach or a conversation with your manager: it makes sure the draft you take to that conversation is yours. It does not judge whether your goal is the right one for your organisation. It covers work and development goals only: not health, wellbeing or personal problems. It does not remember anything you have not put in your four lines.

## Before you use it at work

Your goals and your four lines may mention colleagues and your organisation. Use the assistant your organisation has approved for work material, and leave out names you would not put in an email to a stranger.

---

*Issue 09 of So What, Now What · CC-BY 4.0*

*The method is Whitmore's and the findings are other people's, cited in [SOURCES.md](SOURCES.md). What is mine is the question, the tests and their rules, the bars each version had to meet, and the calls to cut the long coach down to this guardrail and to offer it for ChatGPT, Claude and Gemini 3.8 Flash only. In the tests, Claude agents played the managers, a Claude agent ran every session in ChatGPT, Claude and Gemini, two Claude agents coded every session blind with a third settling disagreements, and two more scored the goals in the 54 sessions without knowing who wrote them; Claude drafted these files to my instructions.*

*Concepts, arguments, and voice are mine. Claude is used as an editing and scaffolding tool. If others' concepts are used, they are referenced in the sources section.* See [SOURCES.md](SOURCES.md).
