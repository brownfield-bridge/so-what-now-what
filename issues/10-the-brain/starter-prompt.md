# Starter prompt

*Prompt by Jacek Kieszkowski, Claude used as editing and scaffolding tool; sources in SOURCES.md.*

Paste everything below the line into Claude Code or the Claude app, opened on a copy of the `skeleton/` folder for one subject. Fill in the two brackets first.

---

You will build and keep a brain for one subject: **[THE SUBJECT, in one line]**. I am **[YOUR NAME]**, the owner. This folder is the brain. Work with me step by step, and ask one question at a time.

1. **Set up the folder.** Make sure these exist: `raw/` (my sources; you read them and never edit them), `raw/text/` (text copies of large files), `intake/` (new material waiting for review), `pages/` (pages you write), `review/` (weekly briefs), `index.md` (one line per page) and `log.md` (one dated line per change). Keep any that already exist. Follow `CLAUDE.md` from now on.
2. **Ask me five questions**, one at a time: what this subject covers and what it does not; which decisions or outputs the brain should help with, and any calls I have already made; my main sources and which I trust most; what must never go in; and which day I will review.
3. **Seed.** Read everything in `raw/`. If a file is too large to read, say so and use its text copy in `raw/text/` if there is one. Before writing anything, propose the list of pages (topics, people or organisations, open questions), each with one line on what it will hold, and wait for my OK. Then write the pages:
   - name each page file exactly like the page title, so `[[links]]` work in any Markdown notes app;
   - end every claim with a tag saying where it came from (`[read]`, `[abstract]`, `[told]`, `[owner]`, `[inferred]`, as defined in `CLAUDE.md`), including claims in a page's opening summary;
   - end every page with the sources it rests on, with the date of each source;
   - update `index.md` and `log.md`.
4. **Fill in the rules** in `CLAUDE.md` from my answers: owner and review day; the subject, its edges and what it helps with; the gate (from `feed-gate.md`), with what must never go in added under "What stays out"; the sources I trust and in what order. Save each call I have already made as a file in `intake/`, so it becomes an `[owner]` claim at my first review. Keep it short.
5. **Finish** with: how many sources you read and pages you wrote; anything you could not read; every `[[link]]` that has no matching page file; and three questions this brain cannot answer yet.
