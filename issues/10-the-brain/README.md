# The brain your agents read first

*Companion kit for* ***So What, Now What*** *- Issue 10: "Make your AI agent start from what you trust."*

Your AI agents act on what they infer about your work. Today most of that sits inside the tools: instructions pasted into one tool's settings, files uploaded into a chat, memory a tool keeps for itself. You cannot read most of it, correct it, or take it to the next tool. This kit builds the alternative: **one brain per subject**, a folder of plain files you own. An agent builds it from your sources and helps feed it every week; you set the guardrails, decide what enters and settle the disagreements. Nothing enters the brain without your yes, and every agent, in any tool, reads it first.

License: CC-BY 4.0. Use it, adapt it, ship it inside your own work. A credit back to *So What, Now What* is appreciated, not required.

## What's here

- **[`starter-prompt.md`](starter-prompt.md)** - start here. Paste it into Claude Code or the Claude app, opened on a copy of `skeleton/`, and the AI builds the brain with you.
- **[`skeleton/`](skeleton/)** - copy this folder to start a brain for one subject.
  - **[`skeleton/CLAUDE.md`](skeleton/CLAUDE.md)** - the brain's rules: edges, gate, tags, jobs, and the one rule. The starter fills it in from your answers.
  - **[`skeleton/feed-gate.md`](skeleton/feed-gate.md)** - what may enter, what stays out, and where each kind of feed lands.
  - **[`skeleton/prep-prompt.md`](skeleton/prep-prompt.md)** - the weekly job's prompt: it reads the intake and writes one brief, nothing else.
  - **`skeleton/index.md`**, **`skeleton/log.md`**, and the folders **`raw/`** (with **`raw/text/`**), **`intake/`**, **`pages/`**, **`review/`**, each with a one-line README.
- **[`weekly-prep/schedule.md`](weekly-prep/schedule.md)** - how to put the weekly job on a schedule, with the command that ran unattended in the test.
- **[`weekly-prep/weekly-prep.cmd`](weekly-prep/weekly-prep.cmd)** - the Windows version of that command, ready to copy into your brain folder.
- **[`weekly-prep/scan-prompt.md`](weekly-prep/scan-prompt.md)** - a weekly search that saves new material on your subject into `intake/` (not tested in the run).
- **[`read-the-brain-first.md`](read-the-brain-first.md)** - the standing block for any other agent: read the brain first, check current sources for anything that can change, save answers to intake only.
- **[`research-funnel.md`](research-funnel.md)** - a screened scan of a whole research database, turned into one map-of-the-field page that goes to intake.
- **[`when-to-split.md`](when-to-split.md)** - one brain per subject, when to split, and what to do when a job spans two brains.
- **[`results/README.md`](results/README.md)** - the test run of 24 to 28 October 2026: every count, prediction by prediction, the misses, and what the kit changed afterwards.
- **[`results/seed-and-questions.md`](results/seed-and-questions.md)** - the 12 free seed sources, the four intake items and the four test questions.
- **[`visuals/obsidian-two-brains.png`](visuals/obsidian-two-brains.png)** - the two test brains in Obsidian, side by side (source: **`visuals/obsidian-two-brains.pptx`**).
- **[`visuals/brain-architecture.png`](visuals/brain-architecture.png)** and **[`visuals/test-process.png`](visuals/test-process.png)** - how a brain is built, and how the test ran; **`visuals/brain-architecture.pptx`** and **`visuals/test-process.pptx`** are their editable PowerPoint sources.
- **[`SOURCES.md`](SOURCES.md)** - everything the issue and the kit rest on.

## How to run it

**1. Build (about an hour).**
- *In Claude Code:* copy the empty brain folder (`skeleton/`), rename it for your subject, put the documents you already have into `raw/`, open Claude Code in the folder, paste `starter-prompt.md` with the brackets filled in, and answer its five questions. When Claude Code asks whether you trust the folder, say yes only for the brain folder you just made.
- *In the Claude app:* the same, with your computer linked in the desktop app and Claude given access to the brain folder.
- Large PDFs: save a text copy of each in `raw/text/` (same name, `.md` or `.txt`). In the test, the read-only weekly job could not open a 16 MB PDF.

**2. Feed it.** Drop new material into `intake/`: notes, links, reports, screenshots, an agent's saved answer. Nothing goes straight into `pages/`.

**3. Run the weekly job, then put it on a schedule.** To run it once by hand: open a session in the brain folder and say *"Read prep-prompt.md and do exactly what it says."* (on Windows you can also double-click `weekly-prep.cmd` once you have copied it in). To schedule it, see `weekly-prep/schedule.md`. For a weekly search that drops new material into `intake/`, see `weekly-prep/scan-prompt.md`. In the test, Claude Code plus the computer's own scheduler ran the job unattended. The Claude app ran it reliably with the owner present; running it on its own, with nobody at the computer, was not shown.

**4. Check the file yourself.** The job's work is done when a dated brief sits in `review/`. Look for the file. An agent can report "done" when it is not.

**5. Review it yourself (about 30 minutes a week).** Use the review instruction in `weekly-prep/schedule.md`: it asks for your view first and marks no option as recommended. In the test, the owner took the AI's "Recommended" option on all six decisions when one was marked.

**6. Let other agents read it.** Add `read-the-brain-first.md` to the instructions of every other agent you use. Where the tool allows, back this with a permission, so those agents can write to the brain's `intake/` and nothing else in the brain.

**7. Read it yourself.** Open the brain folder in a notes app that opens plain text files, such as Obsidian ("Open folder as vault"). Links work when each file is named exactly like its page; the starter checks this at the end of the build.

## Read the brain first, then look further
For anything that can change, such as a law, a price, who holds a role or this quarter's figures, the agent checks current sources and reports them, with the source and its date, apart from what the pages say. In the test, the first version of the read-first block said "use only this brain", and a new chat with no brain but with web search answered a question on current law better than either brain; that line was likely why. The block now says otherwise.

## Keep the sources, rebuild the pages
The sources in `raw/` are never edited. When a better model arrives, let it rewrite the pages from them. The pages are the part you can throw away; your decisions are dated in `log.md` and carry over as `[owner]` claims.

## Sweep or keep
Newer models need fewer instructions. That does not mean delete everything, and it does not mean keep everything. Sort it.

| Sweep: the model can work it out | Keep: it cannot know |
|---|---|
| How to write a report or build a deck | The subject's edges: what is in, what is out |
| General style rules it already follows | What an agent may touch, and what needs your yes |
| Step-by-step procedures it now does better | Your best practices and your own research results |
| About-me text that changes no decision | The sources you trust, and how you read each one |
| Rules written around an older model's quirks | The decisions you made, and why |

**Test before you delete.** Switch one rule off for a week. If nothing breaks, delete it; if something breaks, put it back. Sources are never swept to make the brain lighter; they are checked instead.

## Where the brain lives
- **A folder on your computer** is the default. Claude Code, Obsidian, and the Claude app with your computer linked can all read it.
- **A synced cloud folder or a private repository on GitHub** when an agent that runs in the cloud must reach it while your computer is off.
- Wherever it lives, it stays plain files. Moving it is copying a folder.

## What never goes in
Material your employer has not cleared you to use, other people's personal data, passwords and keys. A brain about your own health or finances stays on your own computer and is never connected to a shared or cloud tool.

## There is no single formula
A brain starts to work as a system when you keep improving it: a new feed, another scheduled job, answers that flow back for your review, a rule switched off because the model no longer needs it. Wire it around your own work. This kit is a way to get started.

---

*Builds on Andrej Karpathy's "LLM Wiki" idea (post on X and GitHub gist, April 2026), credited, not copied. The research scan is adapted from Ruben Hassid's Jev research prompt (How to AI, 20 September 2026). Full list in `SOURCES.md`.*

*Concepts, arguments, and voice are mine. Claude is used as an editing and scaffolding tool. If others' concepts are used, they are referenced in the sources section.*

*Visuals: made by Claude to author's instructions.*

*The brain your agents read first · So What, Now What, Issue 10 · CC-BY 4.0*
