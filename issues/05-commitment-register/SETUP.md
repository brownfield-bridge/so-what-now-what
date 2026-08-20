# Setup

*Companion kit for* ***So What, Now What*** *- Issue 05.*

**Ten minutes to a first run. No coding, no account, no permission from anybody.**

The whole design is one folder and one file. Everything else here is detail you can skip until you want it.

> **Read this first.** This page is the version that runs on a folder you fill yourself. It works everywhere and needs nobody's permission, which makes it the right place to start and the right fallback for good.
>
> **It is not the version you should still be running in a month.** If you are exporting mail threads into a folder every week, you will stop, and you will be right to. Once a first run has convinced you, connect it - see [`CONNECT.md`](CONNECT.md) - and the weekly handling drops to nothing.

![How it works](assets/issue-5-flow.png)

---

## The ten-minute version

1. **Make two things on your machine.** A folder called `folder/` and, next to it, an empty `register.md`. Names do not matter; keeping them separate does. The controller reads the folder and writes the register, never the other way round.
2. **Put a month of material in the folder.** Not curated - whatever you actually have. Meeting notes, a few exported mail threads, anything you typed after a call. Date the filenames, `YYYY-MM-DD-something.md`.
3. **Give the controller to your assistant.** Paste [`controller.skill.md`](controller.skill.md) into a chat model, or install it as a skill in an agent app. Attach the folder and the register.
4. **Say: run.**
5. **Read the second list.** Not the one about what you owe - you know that one. The list of what you are owed.

That is the first run. It is not the point; run two is the point, because **the value of this thing is entirely in the difference between runs.**

---

## The three ways to run it

### A. Any chat model, by hand *(works today, works everywhere)*

Paste the contents of `controller.skill.md` into the chat, attach the folder's files and last week's register, and say run. It hands back the updated register, which you save over the old one.

Crude, and it works in any model, on any account, with nothing installed. **The state lives in your file, not in the tool**, which is the design decision that makes everything else optional. If your assistant changes next year, you copy one file across and carry on.

### B. As a skill, with the folder attached *(the normal way)*

Install `controller.skill.md` as a skill in an agent app that can read a local folder. Point it at the folder, point it at the register, and trigger it. Same loop, less handling.

### C. Connected and on a schedule *(where this is meant to end up)*

Connected to your mail, files and calendar, looking daily, speaking rarely. Mail and files arrive without anybody doing anything, drafts land in your drafts folder, and dated rows appear on a calendar of their own. See [`CONNECT.md`](CONNECT.md).

**Do not start here.** Connect after two or three runs you have read properly. A scheduled tool you do not read is worse than no tool, because you now believe something is watching.

---

## What you set, and what you cannot

### Five dials - expect to change several inside a fortnight

| Dial | Default | Turn it if |
|---|---|---|
| **Capture threshold** | person **and** time identifiable, or somebody visibly waiting | The register is full of things that were never really promises → tighten. You keep finding it missed something real → loosen, slightly. |
| **Silence bound** | 14 days | You are getting findings every week → raise it. Things are rotting for a month before you see them → lower it. |
| **Lead time** | 5 days | How early a dated commitment is raised. Longer if your work needs notice; shorter if five days out is too early to act. |
| **Cadence** | look daily, digest weekly | It looks every day and says nothing unless something crossed a line. The digest is the one message you get regardless, even when it is empty. |
| **Pre-nudge on what you are owed** | **off** | Leave it off. Chasing somebody who has not missed anything yet is how tools like this get a reputation. Turn it on per relationship if a particular supplier needs it. |

**Start tighter than feels comfortable.** A tool that misses things and is trusted beats one that catches everything and gets ignored.

If it is putting five things in front of you every Monday, **the bounds are wrong, and the bounds are yours.** Fix them before you decide the idea does not work.

### And one rule that is not a dial: it never raises the same thing twice

Every row carries a `raised` date. Once something has been put in front of you it will not come back until the row actually changes, or until the silence doubles. If you saw a draft and chose not to send it, that was a decision, and it is respected without comment.

This is the single most important thing standing between this and every nagging reminder tool you have already muted.

### Two things that do not turn

1. **It never creates a row it cannot trace to something somebody actually wrote.**
2. **It never sends.**

These are not settings. One invented row and you will never trust the other forty; one message sent on your behalf and you have handed away the only thing that made this safe to run.

---

## The one habit, and how it gets smaller

Everything in your working life writes itself down somewhere - mail, chat, meeting notes, calendar. **Calls do not.**

So: **when you put the phone down, one line. Who, what, by when.** Twenty seconds, dictated, typed, photographed, whatever fits how you work. Drop it in the folder.

Look at [`folder/2026-08-18-call-note.md`](folder/2026-08-18-call-note.md) to see how little is enough. It is one line, lowercase, no punctuation, and it produced a correct row.

That is the whole of the manual work - and connected, it shrinks again. The controller reads your calendar, spots the meetings and calls that produced no record anywhere, and asks you one question in the weekly digest: *"Tuesday, 30 minutes with Ingrid, and nothing came out of it. Anything promised?"* A habit you have to remember becomes a question you only have to answer.

---

## Getting material into the folder without effort

The folder is the connector, which is why this works with everything and needs nobody's permission. Some ways people do it, cheapest first:

- **Meeting notes already land somewhere.** Whatever takes them for you - your notetaker, your own file, the minutes somebody emails round - point it at this folder or copy them in weekly.
- **Mail: export the threads that matter.** Not your whole inbox. The handful of threads where things get promised. Most clients will let you save a thread as text; forwarding to yourself and saving works too.
- **Chat: export the channel.** Weekly, or when something was agreed there.
- **Photos of pages.** A notebook page, a whiteboard, a printed agenda with scribbles. Drop the image straight in.
- **Dictate.** Any voice-note app that saves text.

**If you can drop it in, it counts.** There is no ingestion format and there never will be.

**And when you are tired of doing this: [`CONNECT.md`](CONNECT.md).** Connected, mail and files need no exporting at all, and only the three manual things are left.

---

## First run: what good looks like, and what to check

The first run has no history, so nothing can be quiet yet. It should give you a register, both directions, every row quoted.

**Then check three things before you trust it with anything:**

1. **Pick five rows at random and read the quote.** Does the sentence actually say what the row says? If any row cannot be traced to real words, stop and fix the threshold before going further. This is the failure that kills the tool.
2. **Look for the same commitment listed twice.** The same promise appears in a meeting note, then a thread, then a chat. It must be **one row**, with the later date in `last mentioned`. If you see duplicates, tell it: same commitment, merge, keep the earliest source and the latest date.
3. **Look at what it refused to do.** The `unclear` list should not be empty. If everything in a messy month came out clean and confident, it is guessing.

**Run two is where you find out whether it works.** A week later, same folder plus the new week's material, register carried forward. The question is not whether the list looks right. It is whether it is **right about what changed** - what moved, what went quiet, what closed.

If run two does not produce a table you would show a colleague, do not use it yet. Say so out loud and fix the dials.

---

## When it will annoy you, and what to do

**It found something that was never a commitment.** Tighten the capture threshold, and tell it what the false row looked like. One example is usually enough.

**It listed the same thing three times.** The dedup rule needs the pair (who owes, what) rather than the wording. Tell it to merge, and to prefer keeping rows separate and flagging them over merging things that are not the same.

**It marked something dropped that is alive.** It has been 42 days with nobody saying anything. That may be correct and unwelcome. If it genuinely is alive, the mention exists somewhere the folder cannot see, which is a folder problem, not a tool problem.

**It produced nothing.** That is the intended outcome of a good week, and the weekly digest still arrives to tell you so - one line, nothing quiet, nothing due. That line is what makes the silence on the other days trustworthy. Issue 4's agent produced something every time you ran it; this one is at its best when it produces nothing at all.

**You stopped reading it.** The honest failure mode, and the common one. Either the cadence is wrong or the bounds are. Ten minutes on a Monday, or it will not survive the month.

---

## What this is not for

If work already sits in a system with a plan and an owner, **leave it there**. Project tools are good at project work and this is not trying to be one.

This is for everything that never got that far: the promise made in a meeting, the yes on a call, the somebody-will-send-it-by-Thursday. Hundreds of them, in both directions, in no system anywhere.

---

*Part of the Issue 05 kit: [`README.md`](README.md) · [`register.md`](register.md) · [`controller.skill.md`](controller.skill.md) · [`CONNECT.md`](CONNECT.md) · [`EXAMPLE-run-output.md`](EXAMPLE-run-output.md)*

*Concepts, arguments, and voice are mine. Claude is used as an editing and scaffolding tool.*

*CC BY 4.0 · So What, Now What · github.com/brownfield-bridge/so-what-now-what*
