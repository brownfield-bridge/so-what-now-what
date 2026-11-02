# Weekly prep prompt (read-only)

*Prompt by Jacek Kieszkowski, Claude used as editing and scaffolding tool; sources in SOURCES.md of the kit.*

This is the text the scheduled job runs. It may read the whole brain and write one file: this week's brief. Its permissions should allow nothing else (see `weekly-prep/schedule.md` in the kit).

---

You are preparing this week's brief for the brain in this folder. Read `CLAUDE.md` first and follow it.

1. List everything in `intake/`, and any file in `raw/` that no page lists among its sources yet. Every file counts, whatever its name. If a file is too large to open, use its text copy in `raw/text/` or mark it NOT ASSESSED.
2. For each item: apply the gate in `CLAUDE.md`. If it passes, name the page it belongs on and the change you propose, in two lines, with the tag each new claim would carry. If it fails, say which test it failed.
3. Under the heading **NEEDS DECISION**, list anything that contradicts an existing page, with both sides in one line each. Do not mark either side as recommended.
4. Under **TO CONFIRM**, list every `[inferred]` claim on the pages that the owner has not yet confirmed, one line each.
5. Under **CHECK**, list up to five pages that look stale, have untagged claims (summary lines included), lack a source, or have a `[[link]]` with no matching page file.
6. Write all of this to `review/[TODAY'S DATE]-brief.md`. Write nothing else.
7. Your last line must be exactly one of: `BRIEF WRITTEN: review/[date]-brief.md` or `NOTHING IN INTAKE THIS WEEK`.
