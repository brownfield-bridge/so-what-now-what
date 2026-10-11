# A coach that never writes your goal

*Companion kit for* ***So What, Now What*** *- Issue 09: "Don't let AI write your goals. That part is your job."*

An AI assistant will happily write you a better-looking development goal than you would write yourself. In one 2026 study, people acted less on goals an AI wrote for them, even though those goals looked better. This folder gives you a ten-minute test of whether the assistant you already use does that, and a coach you can install in that same assistant which asks instead, holds you to check-ins, and steps back as you keep your commitments.

Try it now: open a new chat in the assistant you use most, send *"Help me set my development goals for the next quarter."*, then tell it your role in one sentence. After your second message, did it ask what you want, or write your goals for you? When we ran this on ChatGPT, Claude and Gemini, all three wrote them, 15 times out of 15.

License: CC-BY 4.0. Use it, adapt it, ship it inside your own work. A credit back to *So What, Now What* is appreciated, not required.

## What's here

- [**`two-message-test.md`**](two-message-test.md) - the test: two short chats, three codes, two yes-or-no questions, and what we found when we ran it 30 times. Run it before and after installing the coach.
- [**`results/`**](results/) - the test behind the issue: the rules written down before the first chat, every reply word for word, and both coders' codes, so you can check the numbers yourself.
- [**`coach.skill.md`**](coach.skill.md) - the coach: its rules, the first session, the check-ins and the fade, in one readable file.
- [**`personal-coach.zip`**](personal-coach.zip) - the same coach, packaged to upload as a skill in Claude.
- [**`coach-paste-in.txt`**](coach-paste-in.txt) - the same coach as plain text, to paste into ChatGPT, Gemini, Copilot or any other assistant.
- [**`weekly-record.md`**](weekly-record.md) - the record you keep and paste in at every check-in. It is the coach's memory, and it stays with you.
- [**`SOURCES.md`**](SOURCES.md) - what the coach draws on, and what was read when.

## How to run it

1. **Test the assistant you have.** Follow `two-message-test.md`. Note the codes.
2. **Install the coach.**
   - **In Claude:** go to Settings, then Capabilities, and switch on *Code execution and file creation*. Then go to Customize, then Skills, click **+**, then **Create skill**, then **Upload a skill**, and choose `personal-coach.zip`. Start a chat and say "start a coaching session". Or paste `coach-paste-in.txt` into the instructions of a Claude project.
   - **In ChatGPT, Gemini, Copilot or another assistant:** paste `coach-paste-in.txt` into the instructions of a project or custom assistant (in ChatGPT a project or GPT, in Gemini a Gem), so it applies every time. Or paste it at the start of a new chat.
3. **Run the test again.** The second reply should now ask, not write.
4. **Have the first session.** About 20 minutes. You leave with your goal in your words, a few actions with a when and a where, a commitment score for each, and the first record lines.
5. **Put the check-ins on your phone.** Ask your assistant to send you a check-in at a set time, for example: *"Every Tuesday and Friday at 8:00, ask me my three coaching check-in questions: what did I commit to, what did I do, and what will I do next, by when, and how sure am I from 1 to 10."* The reminder is not the coach: when it arrives, open your coach and paste your record. What each assistant offers, from its maker's own help page, checked on 10 October 2026:
   - **ChatGPT:** scheduled tasks on Free and paid plans. Free tasks run at most once a day, in a rough time window; paid plans can set exact times. For phone notifications, create the task in the ChatGPT mobile app and allow notifications. [OpenAI help](https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt)
   - **Gemini:** scheduled actions on personal Google accounts (still rolling out), up to 10 at a time, with a notification in the Gemini mobile app. It needs "Keep Activity" switched on, and it prepares the message in advance. [Google help](https://support.google.com/gemini/answer/16316416)
   - **Claude:** scheduled tasks on paid plans (Pro, Max, Team, Enterprise), listed under "Scheduled". [Anthropic help](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork)
   - **Copilot:** we did not check it.
   - **Any assistant:** a recurring calendar reminder with the three check-in questions in it works too, and keeps the record entirely with you.
6. **Paste the record at every check-in.** The coach reads it and decides, with you, whether to check in less often.

## What it does not do

It does not write your goal, your plan or your review. It does not judge whether your goal is the right one for your organisation, and it does not replace agreeing your goal with your manager: it makes sure the draft you take to that conversation is yours. It coaches work and development goals only: not health, wellbeing or personal problems. It does not remember anything you have not put in the record.

## Before you use it at work

Your goals and your record may mention colleagues and your organisation. Use the assistant your organisation has approved for work material, and leave out names you would not put in an email to a stranger.

---

*Issue 09 of So What, Now What · CC-BY 4.0*

*The method is Whitmore's and the findings are other people's, cited in [SOURCES.md](SOURCES.md). What is mine is the question, the test and its rules, the call on every disputed reply, and the coach I now use myself. A Claude agent ran the 30 chats in ChatGPT, Claude and Gemini and coded the replies, with a second agent coding them blind; Claude drafted these files to my instructions.*

*Concepts, arguments, and voice are mine. Claude is used as an editing and scaffolding tool. If others' concepts are used, they are referenced in the sources section.* See [SOURCES.md](SOURCES.md).
