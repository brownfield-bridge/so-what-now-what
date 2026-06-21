# The Strategy Stress-Test

*Companion tool for* ***So What, Now What*** *— Issue 01: "Stop writing strategies. Start stress-testing them."*

An AI-guided method for telling the difference between a strategic move that will survive a volatile AI landscape and a move that only works if one specific future arrives. You answer a short set of questions, one at a time, and it produces a one-page **Decision Memo**. Built on Mintzberg's emergent strategy and the Oxford Scenarios approach to planning under uncertainty.

License: CC-BY 4.0. Use it, adapt it, ship it inside your own work. A credit back to *So What, Now What* is appreciated, not required.

## What's here

- **`stress-test.skill.md`** — the gift. A skill you run inside your own AI. It interviews you (the decision, what it assumes, your plausible futures), judges each move against each future, and writes the Decision Memo. A paste-prompt version is included for any model that doesn't support skills.
- **`decision-memo-sample.pdf`** — a filled example, so you can see the output before you start.
- This README — the method in plain words.

## How to use it

You run this in *your own* AI, so your strategy stays in the account you already use. You decide what to share.

- **In Claude (or Cowork):** add `stress-test.skill.md` as a skill, then ask to "run the strategy stress-test." It will start the interview.
- **In any chat model (ChatGPT, Gemini, Claude.ai):** open `stress-test.skill.md`, copy the paste-prompt at the bottom into a new chat, and answer the questions as they come.

It works in about five short turns, like a sharp colleague would: it asks for the few things only you can give, does the first-pass scoring itself, and you correct what it got wrong. It goes faster if you talk rather than type, and it works as a group exercise with one person at the keyboard. At the end it asks whether you want the result as a PDF, a Word document, or slides.

## The method in five steps

1. **List your bets.** The strategic moves you are about to commit budget or headcount to. One at a time. Be concrete: "build an in-house AI support agent this quarter on our current vendor's model" beats "invest in AI."

2. **Define your futures.** Use the four defaults, rename them, drop one, or add your own (three to five works). Scenario thinking means picking futures that are plausible, distinct, and outside your control. You are not predicting which one arrives.
   - **Capability leap** — models get much better and cheaper.
   - **Supply shock** — a model or vendor you rely on is pulled, repriced, or restricted.
   - **Agents arrive** — the work gets done end to end by agents.
   - **Slow lane** — progress stalls; today's tools are roughly next year's.

3. **Stress-test each bet.** For every future, decide whether the bet **Holds**, **Bends**, or **Breaks**. In your context, not in the abstract.

4. **Read the verdict.**
   - **Robust** — holds across all four. Do it now.
   - **Fragile** — holds in two or three. Hedge, stage, or delay.
   - **One-future bet** — holds in only one. Name the bet out loud and set a trigger.
   - **Reconsider** — holds in none. The assumption underneath is the real risk.

5. **Act on what survives.** Do the robust moves now. Turn the fragile ones into hedges. For each one-future bet, write the single early signal you will watch that tells you that future is arriving.

## Why this works (Mintzberg + Oxford Scenarios)

Mintzberg showed most
