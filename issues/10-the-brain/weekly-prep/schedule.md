# Putting the weekly job on a schedule

**The rule that matters:** a scheduled job may prepare, never change. Give it tools to read, and permission to write in `review/` and nowhere else. A sentence in a prompt can be stretched; a permission set in the tool is far harder to get round.

**Check the file yourself.** The job is done when a dated brief sits in `review/`. After each run, look for the file. If it is not there, the week is missed, whatever the job reported.

## Claude Code with your computer's scheduler (ran unattended in the test)
Your computer must be on, and you must be logged in, at the scheduled time.

**To run it once by hand,** open a session in the brain folder and say: *"Read prep-prompt.md and do exactly what it says."*

**Windows.** Copy `weekly-prep.cmd` from this folder into your brain folder (double-click it to run the job once). The line that matters in it:

```
claude -p "Read prep-prompt.md and do exactly what it says." --allowedTools "Read" "Glob" "Grep" "Edit(review/**)" > review\last-run.txt 2>&1
```

This allows reading and an edit in `review/`. It holds as a limit only if your own Claude Code settings do not already allow broader edits or shell commands; check them before you rely on it.

Then register it once, in a terminal, with your own path, day and time (this example: Saturdays at 07:40). If the path has spaces, move the brain to a folder without spaces:

```
schtasks /create /tn "Brain weekly prep" /tr "C:\path\to\your-brain\weekly-prep.cmd" /sc weekly /d SAT /st 07:40 /f
```

Use `Edit(review/**)` for the write permission. In the test, `Write(review/**)` was not honoured: the first run could not write the brief, and its last line said so.

**Mac or Linux (not tested in the run).** The same command from cron, for example Saturdays at 07:40. Cron usually cannot find `claude` by name, so use its full path (run `which claude` to find it):

```
40 7 * * 6 cd /path/to/your-brain && /full/path/to/claude -p "Read prep-prompt.md and do exactly what it says." --allowedTools "Read" "Glob" "Grep" "Edit(review/**)" > review/last-run.txt 2>&1
```

## The Claude app
In the test, a scheduled task in the Claude app ran the prep reliably while the owner was present, but both attempts ran inside the open chat and asked for folder access first, so unattended they would have stopped. Use the Claude app to build the brain and to ask it questions; use the scheduler above for the weekly job, or check after each run that the brief appeared.

## Your weekly review (about 30 minutes)
Open a session in the brain folder and say:

> Read this week's brief in `review/` and integrate it. For every item under NEEDS DECISION and TO CONFIRM, ask me for my view first and set out both sides; do not mark any option as recommended. Change the pages only after my yes.

The session updates the pages, `index.md` and `log.md`, and moves processed items out of `intake/`.

*Concepts, arguments, and voice are mine. Claude is used as an editing and scaffolding tool. If others' concepts are used, they are referenced in the sources section.*
