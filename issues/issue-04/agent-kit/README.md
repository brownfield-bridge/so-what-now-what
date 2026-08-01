# Build your own AI manager

Free, CC-BY 4.0. From *So What, Now What*, Issue 4.

## This is an agent, not an assistant
An assistant waits for you to prompt it, one step at a time, and hands the work back for you to check. This is the other thing. You give it a goal, your sources (a folder, or a read-only connection to where they already live, your email, drive or systems), and the guardrails you set — and from a **single trigger** it does the whole job itself: reads every source, drafts the deliverable to your template, runs an independent check on its own work, and brings you a sign-off-ready draft with only the decisions that need your name. You do not drive it through the steps. It runs the loop; you own the judgment. Once you trust it, it runs on a schedule and brings the finished draft to you.

It never invents a figure, never returns "looks good", and never sends — it stops at your name.

## What's in the box
| File / folder | What it is | Do you edit it? |
|---|---|---|
| `sources/` | A folder of source files the agent reads (demo: a mid-cap manufacturer's month). | **Yes — replace with your own.** |
| *(a delivery folder — you create this)* | A **separate** folder where the agent files the finished draft and self-check. Not shipped in the box — you create one alongside `sources/`, e.g. `<Name> — Reviews`. | **Yes — create it and name it in the brief.** |
| `manager-brief.md` | Your owned spec: the deliverable, the bar for "good", output format, delivery destination, the guardrails. | **Yes — make it yours.** |
| `report-template.md` | The section structure the agent fills. | **Yes — shape it to your deliverable.** |
| `model-report.md` *(optional)* | A gold-standard example that fixes scope, format and the quality bar. | **Optional — drop in a great past report.** |
| `agentic-manager.skill.md` | The agent itself. Install as a skill in your agent app. | No — install as-is. |
| `SETUP.md` | How to make it yours and run it. **Start here.** | — |
| `CONNECT.md` | Read your sources read-only from live tools (email, drive, CRM), and deliver the finished pack to you. | — |

**Two folders, not one.** The agent's guardrails forbid writing into a source system, so its own sources folder can't double as the output location — mixing the two means next cycle's run could mistake last cycle's finished report for a new source. Keep an input folder (`sources/`) and a separate output folder (you name it) side by side, always.

## Make it yours (about 20–30 minutes, no coding)
You change four things — your data, your standard, your shape, and where the output lands:

1. **Your sources → the `sources/` folder.** Delete the demo files, drop in your own (one file per source: your numbers, updates, extracts). The rule the agent obeys: every figure it uses must trace to a file in here.
2. **Your standard → `manager-brief.md`.** Say what the deliverable is, who signs it, and the 4–6 rules that make it "good" *in your words*. This is the part only you can do, and it is the whole point — the agent is held to your bar, not a generic one.
3. **Your shape → `report-template.md`.** Set the sections you want, or hand the agent a past deliverable and let it draft the template from it.
4. **Your delivery → a folder you create, separate from `sources/`.** Name it in the brief's Delivery section and every cycle files the finished draft and self-check there on its own — nothing left as a chat-only download you have to place by hand.

`SETUP.md` walks each of these with examples. The two sample files (`manager-brief.md`, `report-template.md`) are filled in as a worked example so you can see a good one before you edit.

> **How to spot what's yours to change:** every editable file opens with a **▸ EDIT THIS FILE** box, and every spot you fill in is tagged **EDIT ▸**. If a line isn't tagged, leave it. The skill and `CONNECT.md` install as-is.

## How it runs
Install the skill in your agent app, attach your sources folder + brief + template, and trigger it once. It reads → drafts → self-checks → **files the draft and the red-pen review in your delivery folder** and also returns them in chat, alongside the **decisions** only you can make. You make the calls and sign. When a few cycles have gone well and you trust it, schedule it — now it fires itself on the deliverable's date, files the checked draft in your delivery folder (or emails it to you, if that's what the brief specifies), waiting for your sign-off. It brings *you* the review; it never sends to the recipients for you.

## The method: the self-check pass
The self-check pass is the independent review the agent runs over its *own* draft: assume every line is wrong until a source proves it right, hold the work to *your* bar, check this cycle against the last so the reports look alike and compare cleanly (same sections, units and definitions, no content carried over as if new), and surface only the decisions a human must make. It is what makes an agent you can put your name on. Name it in your setup, reuse it, hold every agent you build to it.

## The 30-day move
Point the agent at one recurring deliverable's sources. Fill the brief. Run it once and look hard at the decisions before you sign. Thirty days from now you will not have rented a pilot — you will own an agent with a track record, running when you tell it to or on its own.

*The standard is yours. The decision is yours. The name on it is yours. This just makes sure you never sign the wrong thing by accident.*
