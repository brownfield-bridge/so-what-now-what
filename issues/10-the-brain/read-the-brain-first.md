# Read the brain first

Add these lines to the instructions of any other agent or project you use (in Claude Code, its `CLAUDE.md`; in the Claude app, the project instructions). Replace the brackets.

---

## The [SUBJECT] brain
- Before any task that touches [SUBJECT], read `[PATH TO BRAIN]/index.md`, then the pages it points to. In your answer, list the pages you used.
- The brain is where you start, not where you stop. If the answer depends on anything that can change (a law or rule, a price, who holds a role, a recent figure, the news), check current sources and report what you found, with the source and its date, apart from what the pages say. If a current source disagrees with a page, say so.
- If the brain does not cover something you need, say so. Mark anything you add from general knowledge.
- When a question calls for a judgment, ask for my view first, or set out the best case for each option before giving yours.
- If your work produces something the brain should keep, save it as a new file in `[PATH TO BRAIN]/intake/`. Never edit the brain's pages directly; what you find outside goes through the same gate as everything else.
- On my computer, use only this brain for [SUBJECT]. Do not search the rest of my computer or drives for it.

---

**Make the pages read-only for other agents, where the tool allows it.** The line "never edit the brain's pages" is an instruction, and an agent can stretch an instruction. A permission is far harder to get round. In Claude Code, for example, add deny rules to the other project's permission settings for every edit in the brain folder except `intake/` (that covers `pages/`, `raw/`, `review/`, `CLAUDE.md`, `index.md` and `log.md`). The agent keeps its normal permissions in its own project. This was not tested in the run. Check your tool's documentation for the exact form.

*Changed after the 24 to 28 Oct 2026 run: the earlier line "Use only this brain for [SUBJECT]" likely kept agents from checking current sources, and a clean chat with web search answered a question on current law better than either brain. The judgment line follows the design advice in Herdağdelen, Joren and Tamkin (Anthropic, 2026), see SOURCES.md.*

*Concepts, arguments, and voice are mine. Claude is used as an editing and scaffolding tool. If others' concepts are used, they are referenced in the sources section.*
