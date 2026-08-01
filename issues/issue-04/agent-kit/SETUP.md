# Set up your agent — make it yours

*About 20–30 minutes, no coding. You do this once. After that, each cycle is a single trigger — or a schedule.*

This is where you swap the demo (a manufacturer's monthly review) for your own work. You change four things: your **sources**, your **standard**, your **shape**, and **where the finished output lands**. Then you install and run.

> **Legend:** anywhere you see **EDIT ▸** in these files, that's yours to change. Files not tagged (`agentic-manager.skill.md`, `CONNECT.md`) install as-is — nothing to edit.

### Your setup checklist
- [ ] **Visibility check (do this first)** — list what's already shared "anyone with the link" and lock down anything that shouldn't be open.
- [ ] **Create two folders, not one** — a sources folder for input (e.g. `<Name> — Sources`) and a separate delivery folder for output (e.g. `<Name> — Reviews`). Keep them apart: the agent reads the first and never writes to it; it only ever writes into the second. One folder for both invites the agent to treat its own last output as a "source" next cycle.
- [ ] **`sources/`** — delete the demo files, drop in your own (one file per source).
- [ ] **`manager-brief.md`** — set the deliverable, cadence, who signs; write your 4–6 "good" rules; set guardrails; point the Delivery section at your output folder.
- [ ] **`report-template.md`** — set the sections your deliverable needs.
- [ ] Install `agentic-manager.skill.md` in your agent app; attach the sources folder, brief, and template.
- [ ] Run once → check both files landed in your delivery folder → read the red-pen and decisions → sign.
- [ ] After a few good runs → schedule it.

---

## 0. Before you begin — a two-minute visibility check
Before you point any agent at your data, know what is already open. Ask your assistant to list every document, sheet or drive set to "anyone with the link", and tighten anything that should not be public — plenty of private material sits exposed and indexed simply because a share setting was never changed. The agent's guardrails govern what it *does* with your data; this step governs what your data already *exposes*. Do it once, now, before the first run.

---

## 1. Your sources → the `sources/` folder
This folder is the agent's whole world. It reads everything in here and nothing outside it.

> **Or skip the folder and read straight from your tools.** In an agent app with a read-only connection to your email, drive, or CRM, point the agent at where the sources already live and it pulls them itself, then delivers the finished pack back to you. Same agent, one step on. See `CONNECT.md`. The folder is the simplest start; connect a tool when refilling it by hand is the only thing slowing you down.

- **Delete the four demo files** and drop in your own. One file per source is best — the numbers, the updates, the extracts the deliverable draws on.
- Any readable format works (Markdown, CSV, pasted text, exported PDF). Name them plainly: `finance.md`, `sales.csv`, `ops-report.pdf`.
- **The one rule:** every figure the agent uses must come from a file in here. If a number is not in the folder, the agent will not use it — that is the point.
- Look at the demo files first (`01-finance-close.md` … `04-cost-and-mix.md`) to see the shape: a short header saying which system it came from, then the figures. Yours do not need to be that tidy — the agent reads messy exports fine — but the cleaner the source, the sharper the check.

*No files yet? Start with one. Even a single pasted export is enough for the first run.*

## 2. Your standard → `manager-brief.md`
Open it. It is filled in as a worked example (the manufacturer's review) so you can see a good one. **Replace each field with yours:**

- **The deliverable** — what it is, how often, who receives and signs it. *(e.g. "Weekly pipeline review for the VP of Sales.")*
- **The bar — the 4–6 rules that make it "good", in your words.** This is the part only you can write. Good rules are checkable, not vague. Compare:
  - Weak: "make it insightful."
  - Strong: "every metric that moved more than 10% gets a one-line reason grounded in the data."
  - Fastest way to write them: paste one past deliverable you were proud of and ask the agent to *extract the rules from it*, then edit.
- **The substrate** — leave it pointing at your `sources/` folder.
- **The guardrails** — what may run alone (formatting, arithmetic) and what must never leave without your name (financials, forward-looking claims, anything client- or board-facing).

## 3. Your shape → `report-template.md`
Open it and set the sections you want the deliverable to have. Each section says what figures it needs and ends with a "so what". Two ways:
- Edit the sample sections directly, or
- Hand the agent a past version of the deliverable and say *"draft this template from it"* — then tidy.

**Optional but powerful — a model report.** If you have a past report you were proud of, drop it in as `model-report.md` (there's a sample to see the idea). The agent matches its scope, format, tone and depth — the fastest way to show what "good" looks like, beyond the rules in the brief and the skeleton in the template. It takes the *shape and standard* from the model, never its numbers: your figures always come from `sources/`. Delete the file if you'd rather not use one.

## 4. Your delivery → create an output folder, separate from your sources
The agent's own guardrails say it never writes into a source system — so the sources folder from Step 1 is not where finished output goes. Create a second folder for that (Drive, local, wherever your sources live) — e.g. if your sources sit in `Northwind — June 2026`, name the output folder something like `Northwind - Reviews`.

- Point `manager-brief.md`'s **Delivery** section at this folder by name.
- Every run then saves both the **deliverable draft** and the **red-pen self-check** into it automatically — no separate instruction needed each cycle, and nothing left stranded as a download-only chat artifact.
- If your delivery folder is on Google Drive, tell the agent to save the self-check with its content type kept as HTML (not auto-converted to a Google Doc) so the styled verdict chips and struck-through figures survive — otherwise it flattens into plain text.
- Prefer email delivery instead? Note the recipient in the brief's **Delivery** section and it sends both as attachments there instead of (or alongside) filing them in a folder.

Two folders, two jobs: the sources folder is read-only input, the delivery folder is where the agent is allowed to write. Never point them at the same place.

---

## 5. Install the agent and run it
In your agent app (one that lets you install a skill and attach files):
1. Install `agentic-manager.skill.md` as a skill.
2. Attach the `sources/` folder, `manager-brief.md`, and `report-template.md`.
3. Trigger it once: *"Run this cycle."*

From that single trigger it reads the sources folder, drafts the deliverable, runs its self-check, saves both files into your delivery folder, and returns three things in chat too: the **draft**, the **red-pen review** (its own work marked against your bar — wrong figures struck through, unsupported claims flagged), and the **decisions only you can make**.

## 6. Make the calls and sign
Go through the decisions. Fix what failed, keep what is yours, ground or cut any forward-looking line. Your name goes on it — and it means something, because it was actually checked.

## 7. Teach it one line
Add one line to the brief: the thing it got wrong or missed this time. Next cycle it will not. The brief is yours and it compounds while you do less.

## 8. Let it run itself — from day one, on a day you choose
You don't need to wait. Because the review only ever comes to **you**, there is nothing to lose by scheduling it from the very first cycle — the worst case is a draft you choose not to sign, exactly like a manual run. So set it up whenever you like. In your agent runtime, create a **recurring task** that fires the skill over the folder on the day the deliverable is due:
- a **specific date each month** — e.g. the 3rd, once month-end close has landed; or
- a **specific weekday each week** — e.g. Monday morning for a weekly review.

On that day it reads the folder, drafts, runs the self-check, and delivers the finished review **to you** — emails you (or drops into your inbox / app) the draft plus the red-pen, waiting the morning it's due: *"your review is ready to sign."* You open it, make the calls, and send it onward yourself.

The one line that never moves — and the reason automating it early is risk-free: it delivers the checked draft **to you, never to the recipients.** Nobody sees anything until you sign. It brings you the review; it does not send for you.

---

## Keeping cycles comparable (from cycle 2 on)
A recurring report is only useful if this month looks like last month and lines up next to it. Two habits keep it that way:

- **Give it last cycle's report as a reference.** After you sign the first one, drop it into a `previous/` folder **inside your delivery folder** (not the sources folder — it's your own past output, not a source of new figures). Each new run then matches that format exactly, computes the period-over-period deltas for you, and its self-check flags anything that drifted or was carried over word-for-word from last time.
- **The template is the contract — evolve it on purpose, not by accident.** The format stays constant across cycles. If you *do* want to change how the report looks, edit `report-template.md` and note the change in the brief's revision log. That way the format only ever changes when you decide it should.

The agent keeps the **shape and the definitions** constant so periods compare cleanly, but the **content** is always this period's — it never carries last month's conclusions forward, and a genuinely new issue still gets raised inside the same structure.

---

## What you have
An agent that reads your sources, does the work to your standard, checks itself, keeps every cycle comparable to the last, and brings you only the decisions — on demand, or on its own. You own it, and it is portable: rename it, move it between models and tools.

*Ready to move off the folder to live data? See `CONNECT.md`.*
