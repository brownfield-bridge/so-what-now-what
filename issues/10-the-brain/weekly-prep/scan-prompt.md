# Weekly scan prompt (not tested in the run)

*Prompt by Jacek Kieszkowski, Claude used as editing and scaffolding tool; sources in SOURCES.md of the kit.*

A scheduled search that feeds the brain. It finds new material and saves it to `intake/`; it never touches `pages/`. The weekly prep job then sorts what it found through the gate, and you decide at your review. Run it before the prep job, with the same scheduler and the same kind of limits: it needs web search and permission to write in `intake/` only.

---

You are running this week's scan for the brain in this folder. Read `CLAUDE.md` first: the subject, its edges and the sources the owner trusts.

1. Search for material published in the last seven days that is inside the subject's edges, starting with the sources the owner trusts.
2. For each item worth the owner's time (at most ten), save one file in `intake/` named `scan-[date]-[short-title].md` with: the title, the source, the link, the publication date, and three lines on what it says. Do not judge it against the gate; the weekly prep does that.
3. Write nothing outside `intake/`.
4. Your last line must be exactly one of: `SCAN SAVED: [n] items in intake/` or `NOTHING NEW THIS WEEK`.
