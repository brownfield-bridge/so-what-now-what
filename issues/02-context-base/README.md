# The Context Base

*Companion kit for* ***So What, Now What*** *- Issue 02: "You don't need a knowledge platform. You need a context base."*

A context base is a private folder of plain files your AI can reason over: your decisions, your assumptions, your market notes, the things you keep re-explaining to a chat window every morning. No vector database, no embeddings pipeline, no platform. A frontier model already reasons over a clear structure better than over a pile; you supply the structure, it supplies the reasoning. This kit stands one up in an afternoon and keeps it honest after that.

License: CC-BY 4.0. Use it, adapt it, ship it inside your own work. A credit back to *So What, Now What* is appreciated, not required.

## What's here

- **`GUIDE.md`** - start here. The step-by-step walkthrough: build, fill, ask, feed, maintain.
- **`setup-prompt.txt`** (and `setup-prompt.md`) - the entry rung. Paste it into any AI and it stands up a base for one area of your work from a cold start: it proposes your folders, writes your root map, and gives you a retrieval prompt. No account beyond the AI you already use.
- **`context-base.skill.md`** - the same setup as an installable skill for Claude or Cowork, so you can re-run it for each new area.
- **`retrieval-prompt.txt`** - paste this at the start of a session so your AI answers from the base and names its sources.
- **`starter/`** - a clonable scaffold. A worked folder tree with the root map (`CONTEXT.md`) written and a self-contained example (a decision, an assumption, and a signal that contradicts it), so you see the whole thing work before you replace it with your own.
- **`weekly-maintenance.skill.md`** (and `weekly-maintenance-prompt.txt`) - the part that lasts. A gated weekly upkeep loop: it reviews your base for staleness and drift and proposes a checklist, and never moves or deletes a file without your yes.
- **`scheduled-review.md`** - how to run that upkeep on a schedule, still gated to your approval.
- **`visuals/`** - the four-move one-pager and a sample of what a base looks like.
- **`README.md`** - the method in plain words.

## The four moves

A context base is four moves, and the first three take one afternoon.

1. **Shape.** Folders that mirror how the work is actually organised, so the model walks them like a well-ordered report, not a heap.
2. **Anchor.** One root file (`CONTEXT.md`) that tells any model what the base is, who you are, what each folder holds, and how to navigate it. The highest-leverage page you will write.
3. **Feed.** One named, dated place where new material lands (`inbox/`), so the base compounds instead of scattering across a drive.
4. **Maintain.** A weekly pass to prune the stale and re-file the drift. This is the practice, not the chore: a base nobody tends rots into the pile you were escaping.

## How to use it

You run all of this in *your own* AI, so the base stays in the storage and the account you already use. Nothing is uploaded to a third-party platform.

- **Fastest start:** open `setup-prompt.md`, paste it into your AI, answer four lines, and create the folders it proposes.
- **Pre-built start:** clone `starter/`, open `CONTEXT.md`, and edit the bracketed lines to fit your area. Drop your own files into the folders.
- **In Claude or Cowork:** add `context-base.skill.md` and `weekly-maintenance.skill.md` as skills. Say "set up a context base" to build one, and "run my weekly context-base review" to maintain it.
- **Hands-off upkeep:** follow `scheduled-review.md` to run the weekly review automatically. It still hands you a checklist to approve; it does not edit your files on its own.

## Why this works

For years, making a machine-usable knowledge base meant specialist infrastructure: you sliced documents into fragments, turned each into numbers, and retrieved by similarity. That was a buy, so for most people it meant a platform and a project. Two things changed. Models got good enough to read a structured document the way a person does, walking from the contents page to the right section and reasoning about what is relevant rather than what merely sounds similar. And the open technical work caught up: a vectorless, reasoning-based approach (see PageIndex below) now outperforms the heavyweight stack on the hardest financial-document tests. The cost of the build collapsed, so the make-or-buy boundary moved. For an individual, a team, or a single project, you can build, and the build is just folders you can make yourself.

The asset was never the model, which everyone rents from the same few suppliers. The asset is your structured knowledge, kept current. The labs will keep renaming the technique; the folder of your own thinking, kept current, outlasts every name they give it.

## Sources

- PageIndex (VectifyAI), the open-source vectorless, reasoning-based retrieval project: [github.com/VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex). MIT licence. Its Mafin 2.5 system reports 98.7% on FinanceBench, far ahead of vector-RAG baselines.
- The "skills standardize AI use in firms" framing is Ethan Mollick's (June 2026).
- The enterprise example (a university finance team built a treasury skill that reasons over its own records and recovered $100,000 in mis-routed payments) is the Cornell case, June 2026.

---

*The Context Base · So What, Now What, Issue 02 · github.com/brownfield-bridge/so-what-now-what · CC-BY 4.0*
