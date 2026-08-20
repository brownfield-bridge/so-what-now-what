# The commitment register

*Companion kit for* ***So What, Now What*** *- Issue 05: "Nobody should have to report their own bad news."*

**This file is the whole point.** Not the agent. The agent can be replaced tomorrow by a better one; this file is yours and nothing can take it away. It is a plain markdown table (or a CSV, if you prefer - the header is at the bottom) that lives somewhere you control and knows one thing nothing else in your company knows: **what was promised, in both directions, when anybody last mentioned it, and how it ended.**

Everything in the rest of this kit exists to keep this file current.

---

## The columns

| Column | What goes in it | Rules |
|---|---|---|
| `id` | `C-001`, `C-002`… | Never reused. A closed row keeps its id forever. |
| `what` | The commitment in one line, in the words it was made in | Not your paraphrase of what it should have been. |
| `owes` | Who has to do it | A person, not a team. "Ops" never delivers anything; a person does. |
| `owed` | Who is waiting for it | `you`, or the person or party waiting. |
| `relationship` | `report` · `peer` · `senior` · `customer` · `supplier` · `external` | Filled in **once per person**, not per row. This is the column that tells you where things rot. |
| `promised by` | The date it was promised for, or `none` | `none` is a legitimate and very common answer. Most real commitments never had a date. |
| `last mentioned` | The date anybody last said anything about it, anywhere in the folder | **This is the column the whole thing runs on.** Not the due date. |
| `quiet` | Days since `last mentioned` | Derived at run time. Never typed by hand. |
| `status` | `open` · `delivered` · `renegotiated` · `dropped` · `unclear` | See below. |
| `raised` | The date the controller last put this in front of you, or `-` | **The anti-nag column.** A row already raised is not raised again until it changes, or until `quiet` doubles. |
| `source` | The file it came from, and the sentence, verbatim | **No sentence, no row.** |

### The three closings, and why the last two matter

Commitments almost never fail outright. They end in one of three ways, and only the first is completion:

- **`delivered`** - the thing happened.
- **`renegotiated`** - a new date or a smaller scope was agreed. A decision was made. Usually nobody wrote it down.
- **`dropped`** - everyone stopped mentioning it and nobody ever said so. Also a decision. Also made by nobody in particular.

A register that records **which of the three** is the argument of Issue 5 in object form, and it costs one column.

`unclear` is not a closing. It means the material named a commitment but not a person or not a time, and the controller refused to guess. Leave them in. A short `unclear` list is a sign the thing is honest.

### Two triggers, not one

A row becomes a finding in one of two ways, and both matter:

- **Approaching.** It has a date, and the date is inside the lead time (default 5 days). Ordinary, and it has to work or the tool feels broken.
- **Quiet.** Nobody has mentioned it for longer than the silence bound (default 14 days), date or no date. **This is the half nothing else does**, because most real commitments never had a date.

What happens next depends on the direction as well as the trigger. Something *you owe* that is approaching deserves a line to the other person before they have to ask - that is the most valuable message this whole thing produces. Something *you are owed* that is merely approaching deserves nothing at all, because pre-nudging people who have not missed anything is how tools like this get a bad name.

### The one rule that everything else depends on

**Every row cites the sentence it came from.** File, and the words, verbatim.

A register with one invented row in it is worse than no register, because you will find the invented row on a day you were about to act on it, and after that you will never trust the other forty. If the material does not support a row, the controller writes `unclear` and moves on. Missing something is recoverable. Making something up is not.

---

## Worked example

Fictional. A Head of Operations at a mid-sized manufacturer, one month of real-shaped mess. **Run date: Monday 24 August 2026.**

### What you are owed

| id | what | owes | owed | rel | promised by | last mentioned | quiet | status | raised | source |
|---|---|---|---|---|---|---|---|---|---|---|
| C-014 | Revised pricing sheet for the Nordic tender | Marek | you | report | 2026-08-14 | 2026-08-07 | **17** | open | 2026-08-24 | `2026-08-07-weekly-ops.md` - "Marek will get the revised sheet over to you before the 14th" |
| C-011 | Survey dates for the Poznań line | Halden Systems (Ingrid) | you | supplier | 2026-08-12 | 2026-07-30 | **25** | open | 2026-08-24 | `2026-07-30-call-halden.md` - "They'll confirm survey dates in the next week or two - Ingrid said before the 12th at the latest" |
| C-018 | Come back on the Kessler MSA redlines | Anna | you | peer | none | 2026-08-19 | 5 | open | - | `2026-08-19-mail-export.md` - "I'll come back to you on the redlines, give me a few days" · *also 08-07, 08-11* |
| C-021 | Something on the warehouse capacity question | Halden Systems (Ingrid) | you | supplier | unclear | 2026-08-18 | 6 | **unclear** | - | `2026-08-18-call-note.md` - "we'll get you something on the warehouse question. no date given" |
| C-003 | Redo the onboarding deck for September | Tomas | you | report | 2026-07-31 | 2026-07-15 | **40** | **dropped** | 2026-08-24 | `2026-07-15-1to1-tomas.md` - "Agreed Tomas will redo the onboarding deck for September, wants it done before he goes on leave so end of the month" |

### What you owe

| id | what | owes | owed | rel | promised by | last mentioned | quiet | status | raised | source |
|---|---|---|---|---|---|---|---|---|---|---|
| C-009 | Q3 headcount plan to the board | you | Board (via Elena) | senior | 2026-08-28 | 2026-08-20 | 4 | open | 2026-08-24 | `2026-08-20-mail-export.md` - "confirming, you'll have the headcount plan by the 28th" |
| C-006 | Migration cutover, **was 14 Aug, now 4 Sep** | you | Bergmann | customer | 2026-09-04 | 2026-08-13 | 11 | **renegotiated** | - | `2026-08-13-call-bergmann.md` - "Agreed we'd push cutover to the 4th" |
| C-019 | Write up the incident post-mortem and circulate it | you | Ravi + ops team | peer | none | 2026-08-21 | 3 | **delivered** | - | `2026-08-21-mail-export.md` - "Post-mortem attached, as promised" · *promised 08-07* |

### And what the run actually said

> **One thing is coming up, and it is yours.**
>
> **C-009**, the headcount plan to the board, due Friday the 28th. Draft ready confirming it is on track.
>
> **Two things are quiet.**
>
> **C-011**, Halden Systems, 25 days. Supplier, and the promised date passed twelve days ago.
> **C-014**, Marek, 17 days. Your own report, so this one is cheap to ask about.
>
> **One thing closed itself.** C-003 has had no mention from anyone in 40 days. Marked `dropped`. Nobody decided this.
>
> **One is unclear.** C-021 has no person and no date. Left as unclear, not chased.
>
> Three drafts are waiting. Nothing has been sent.

That is a normal week. Note what is **not** in it. No score for Marek. No chart. No list of five things you must do today. And nothing about C-018 or C-006, which are both fine and neither of which you needed to hear about.

**Note also which draft came first.** The most useful message here is the one about your own commitment, going out four days early, before anybody had to ask. That is the cheapest conversation you will have all week, and it only exists because something was watching a date you had already stopped thinking about.

---

## Where to look first, and it is not the top of the list

The rows do not matter equally, and what decides it is not importance. **It is who you would have to talk to.**

Chasing your own report is free. Chasing a peer is awkward. Chasing somebody senior costs you something - and so does telling somebody senior that your own thing has slipped.

So read the register in two places only:

1. **What you are owed, by people you find it expensive to chase.** `owed = you` and `rel` in `peer · senior · customer · supplier`. This is where things quietly rot, because the cost of asking falls on you every single time.
2. **What you owe upwards.** `owes = you` and `rel = senior`. This is where you delay telling, and where delay costs the most.

In the example above, that is C-011 and C-009. The rest can wait a week and nothing happens.

---

## If you would rather have a CSV

Same object, same rules. Header:

```csv
id,what,owes,owed,relationship,promised_by,last_mentioned,quiet_days,status,raised,source_file,source_quote
```

`quiet_days` is derived at run time and overwritten on every run. Everything else is carried forward from the previous file, unchanged unless the new material says otherwise.

---

## What the register is not

- **Not a task list.** A task list holds work you have decided to do. This holds promises that were made, most of which nobody has decided anything about.
- **Not a project tool.** If work already sits in a system with a plan and an owner, leave it there. This is for everything that never got that far.
- **Not shared.** It is a register of other people's promises to you. Sharing it turns a working file into an accusation, and you will stop writing honest things in it within a fortnight.
- **Not a performance record.** No scores, no counts per person, no trend on who is late. The moment it becomes that, everybody starts making fewer promises out loud, and you have made the problem worse than you found it.

---

*Part of the Issue 05 kit: [`README.md`](README.md) · [`controller.skill.md`](controller.skill.md) · [`SETUP.md`](SETUP.md) · [`EXAMPLE-run-output.md`](EXAMPLE-run-output.md)*

*Concepts, arguments, and voice are mine. Claude is used as an editing and scaffolding tool.*

*CC BY 4.0 · So What, Now What · github.com/brownfield-bridge/so-what-now-what*
