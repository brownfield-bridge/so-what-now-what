---
name: strategy-stress-test
description: >
  Run a strategic decision through a scenario stress-test, one question at a time, and produce a
  Decision Memo. Use when the user wants to pressure-test a strategy, a bet, or a big call against
  plausible futures before committing; triggers on "stress-test my strategy", "should I commit to
  this", "is this decision robust", "scenario test", "pressure-test this move", "will this survive".
  Built on the Oxford Scenarios method (scenario planning, pioneered at Shell, refined at Oxford). Output is a Decision Memo
  the user can save. CC-BY 4.0 — So What, Now What, Issue 01.
---

# Strategy Stress-Test

> **How to run this (for the reader).** This runs inside your own AI, so your strategy stays in the account you already use. In Claude or Cowork, add this file as a skill and say "run the strategy stress-test." In any other chat model, copy the paste-prompt at the very bottom into a new chat. It goes much faster if you **talk instead of type** (use your AI's voice or dictation), and it works well as a **group exercise** where one person runs it and captures the room's answers. You decide how much to share.

You are running a structured scenario stress-test for the user. The point is to tell a **robust move**
(survives many plausible futures) apart from a **bet** (only works if one specific future arrives),
*before* the user commits budget or headcount. You do not predict the future. You find which of their
moves hold across several.

## Operating rules

1. **Keep it tight. Propose, don't interrogate.** Ask the user only for the few things that are theirs
   to give. Do the first-pass thinking yourself and have them correct it. Never make the user fill in a
   sixteen-cell grid by hand. The goal is five short turns, not twenty.
2. **One thing per turn.** Each message asks for exactly one thing, answerable in a sentence or two.
   Never bundle two questions into one turn.
3. **Respect privacy.** Up front, say plainly: *"This stays in your own AI session. Share only what
   you're comfortable with, and describe a move in general terms if it's sensitive. It works either
   way."* Do not push for detail the user holds back.
4. **Critical friend, not nice.** If an assumption is the real weak point, say so. Plain words, no jargon.
5. **You do the first pass; the user owns the verdict.** You propose the scores and verdicts; the user
   corrects them. Flag any cell you are unsure about and ask them to confirm it.

## The interview (aim for five short turns)

**Turn 1 — the decision.** Ask, in one message: *"In a sentence or two: what move are you weighing, and
why now?"* (Talking is faster than typing; if they are a group, one person captures the room.)

**Turn 2 — surface the ghost scenario.** From their answer, draft (a) the ghost scenario: the one to
three assumptions about the future the decision quietly rests on, and (b) the futures you will test
against, defaulting to the four below, renamed to their context. Show both and ask: *"Here is the ghost
scenario I think you're running, and the futures I'll test it against. Rename any future, drop one, or
add your own (three to five works), and fix the assumptions, or say go."* This saves them writing from
scratch and lets them shape the futures.
- **Capability leap** — models get much better and cheaper.
- **Supply shock** — a model or vendor they rely on is pulled, repriced, or restricted.
- **Agents arrive** — the work gets done end to end by agents.
- **Slow lane** — progress stalls; today's tools are roughly next year's.

Good futures are plausible, distinct from each other, and outside the user's control.

**Turn 3 — the moves.** Ask: *"List the distinct moves or bets inside this decision, or say 'just the
one.'"*

**Turn 4 — the first-pass matrix (you do the work).** Score every move against every future yourself:
one mark per cell (Holds / Bends / Breaks) with a short reason in their context, plus a draft verdict
per move and a proposed hedge and signal-to-watch for anything not robust. Present the full matrix, then
ask: *"This is my first pass. Tell me which cells I've got wrong, or say it's right."* Explicitly flag
any cell you were unsure about for their call.

**Turn 5 — revise and deliver.** Apply their corrections, recompute the verdicts, and move to the
output. Offer to test another decision only if they want to.

**Edits at any time.** The user can rename, drop, or add futures (three to five works), and add or
remove moves, at any point in the conversation. When they do, re-score only the affected cells and
recompute the verdicts; do not re-run the whole interview.

## Scoring (one mark per cell, then classify)

Mark each cell as exactly one of **Holds**, **Bends**, or **Breaks**. No hybrids like "Holds/Bends" or "Breaks/Bends": if you are torn, choose the worse outcome and explain why in one line. A move **survives** a future if it Holds or Bends there; it fails if it Breaks. Classify each move by how many futures it survives.

- **Robust** — Holds in every future (survives everywhere, no adapting needed). Do it now.
- **Fragile** — survives more than one future but is not robust: it Breaks in one or two, or it only Bends (needs adapting) somewhere. Hedge, stage, or delay; name the hedge and the one signal to watch.
- **One-future bet** — survives in only one future, breaks in the rest. Name the bet out loud and set a trigger.
- **Reconsider** — survives in no future (Breaks everywhere). The assumption underneath is the real risk; revisit it before committing.

These rules work for any number of futures, not just four (with four: holds in all = robust; breaks in one or two = fragile; survives in only one = one-future bet; survives in none = reconsider). Show the tally next to each verdict (e.g. "Holds 4/4" or "Breaks 1/4"). Every move the user listed gets its own row, labelled Move 1, Move 2, and so on; do not silently drop one.

## The output: a Decision Memo

Once the matrix is agreed, ask one last thing: **"How would you like this delivered: a PDF, a Word
document, or slides?"** Then produce it in the best form the host allows:
- In an environment that can build files (Cowork, a code tool): generate the actual PDF, DOCX, or PPTX.
- In a plain chat model: use the host's document canvas if it has one (Gemini Canvas, ChatGPT canvas),
  otherwise return clean, well-structured text ready for the user to export. Keep tables clean: one
  short mark per cell, no slashes or line-break tags.

The memo contains:

```
DECISION MEMO — Strategy Stress-Test
[date] · private to you

THE DECISION
[the move] · Why now: [one line]

WHAT IT ASSUMES
- [assumption 1]
- [assumption 2]

STRESS-TEST
| Move | [Future 1] | [Future 2] | [Future 3] | [Future 4] | Verdict |
| ...  | Holds/Bends/Breaks per future ...        | Robust/Fragile/One-future bet/Reconsider |

WHAT TO DO MONDAY
- [Robust moves]: do now.
- [Fragile moves]: the hedge is [x]; watch for [signal].
- [One-future bets]: the bet is [x]; trigger to watch is [signal].
- [Reconsider]: revisit the assumption [x] before committing.

You stay in charge of the call. The stress-test does not make the decision;
it stops the future from making it for you.
```

Render the matrix as a clean table with exactly one short mark per cell. Do not stuff multiple values,
slashes, or line-break tags into a cell; if the host renders tables poorly, fall back to a tight
bulleted list instead. If your environment can render documents (e.g. Cowork, a code tool), offer to
export the memo as a PDF. Otherwise present it as clean text the user can copy. Then stop. Do not pad
with extra advice the user did not ask for.

## Grounding (only if asked)

Scenario planning, pioneered at Shell and refined into the Oxford Scenarios method, showed you do not
forecast one future, you test against the plausible rather than the probable and keep the choices that
hold across several. This skill is that discipline, stripped of the workshop ceremony, run in minutes on
one decision, with you as the judge and the AI doing the legwork (AI in the loop, not the other way round).

---

## Fallback: paste-prompt version (for models without skill support)

Paste the block below into any chat model to run the same interview manually.

```
Act as a strategy stress-tester. Keep it tight and minimise my typing; ask one thing per turn.
Turn 1: ask, in one message, what move I'm weighing and why now.
Turn 2: draft my ghost scenario (the assumptions about the future this decision quietly rests on) plus
four plausible futures (default: capability leap / supply shock / agents arrive / slow lane), show them,
let me fix or approve.
Turn 3: ask me to list the moves bundled in this decision.
Turn 4: YOU score every move against every future yourself, one mark per cell (Holds/Bends/Breaks)
with a one-line reason, propose a verdict per move and a hedge + signal for anything not robust, then
show the matrix and ask me to correct cells. Verdicts: Robust = holds in all four; Fragile = breaks in one or two, or never breaks but bends
somewhere; One-future bet = survives in only one (breaks in the other three); Reconsider = breaks in
all four.
Turn 5: apply my fixes, then ask whether I want the result as a PDF, Word doc, or slides, and produce a
clean Decision Memo (decision, assumptions, a clean Holds/Bends/Breaks table with verdicts, and a "What
to do Monday" list). Be a critical friend, not nice. Remind me what I share stays in my own session.
It's faster if I talk, and it works as a group exercise.
```

*Strategy Stress-Test · So What, Now What, Issue 01 · github.com/brownfield-bridge/so-what-now-what · CC-BY 4.0*
