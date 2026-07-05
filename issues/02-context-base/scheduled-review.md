# Running the weekly review on a schedule

The weekly upkeep works as a calendar reminder you action by hand. If you would rather it ran itself, you can schedule it, with one rule kept intact: **it still proposes a checklist for you to approve, and never edits your files on its own.** Automation here means the review shows up without you remembering it, not that a machine rearranges your base while you sleep.

## Option A - Cowork or Claude scheduled task (easiest)

If you use Claude in Cowork, ask it to schedule the maintenance:

> "Every week, at the day and time I choose, run my context-base weekly review on `~/strategy-base` using the context-base-maintenance skill, and message me the checklist to approve. Do not change any files until I reply."

Pick whatever cadence fits how fast your base changes. Weekly is a sensible default; daily is usually too much, monthly lets drift pile up. The day and time are yours. It runs the review on your schedule and hands you the checklist; you approve the items you want, and only then does anything change. Update the path to your own.

## Option B - your own machine (cron or Task Scheduler)

For a fully local setup, schedule a weekly job that opens your base with your AI command-line tool of choice and runs the maintenance prompt. A minimal shape (adapt the tool and paths to yours):

```
# Weekly, at a day and time YOU choose. Cron fields: minute hour * * weekday (0 = Sunday).
# The line below is only an example slot; change it to whenever suits you.
[minute] [hour] * * [weekday]  cd ~/strategy-base && your-ai-cli --prompt-file ./weekly-maintenance-prompt.txt > ./review-$(date +\%F).md
```

This kit includes `weekly-maintenance-prompt.txt` ready to use; point the job at it. The job writes a dated checklist; you open it, approve, and make the changes yourself. The schedule removes the remembering, not the judgment.

## The one rule, restated

Whatever you automate, keep the human gate. The value of a context base is that it answers from what you decided and why; an unattended process that quietly rewrites that history is how you lose the thing you were building. Schedule the *review*. Keep the *decisions*.

---

*The Context Base · So What, Now What, Issue 02 · github.com/brownfield-bridge/so-what-now-what · CC-BY 4.0*
