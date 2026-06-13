# Issue 0 — The Synthesizer

Drops Sunday 14 June 2026 morning at [so-what-now-what.beehiiv.com](https://so-what-now-what.beehiiv.com).

## What ships in this folder

- `README.md` (this file): what's inside and how to use it
- `prompt.md`: the paste-and-run So-What / Now-What synthesizer prompt
- `one-pager.png`: the framework visual (Filter, Score, Synthesize, Activate)
- `cowork-recipe/`: the hands-off version with no code. You describe the job once, connect your mailbox, and the brief arrives every Monday.
- `claude-code-recipe/`: the full-control version. Your relevance window in a file you own, the brief written to disk, wired into cron.
- `starter-template/`: a Google Apps Script workflow that wires the prompt to an RSS feed list and ships a brief to your inbox every Sunday evening.

## Four rungs, same discipline

The framework is one prompt. How automatically it runs is up to you. Each rung does the same job; they differ only in how much of the gathering you hand off and how much control you keep.

1. **Paste-and-run** (`prompt.md`). You run it when you remember to. Works in any frontier model, nothing to set up. Start here.
2. **Apps Script** (`starter-template/`). Scheduled, RSS-based, emails you the brief. Needs a Google account and an Anthropic API key.
3. **Cowork, no code** (`cowork-recipe/`). Reads your mailbox and the web, runs every Sunday, no key and no feed list to assemble. The rung most readers want.
4. **Claude Code** (`claude-code-recipe/`). Full control from the command line. Your relevance window under git, the brief written to disk, wired into cron. The operator's path.

Start at rung 1. Move down only when the discipline has earned a place in your week. The thinking the synthesizer asks of you, your relevance window, is identical at every rung; the rungs differ only in how much of the gathering you hand off.

## License

All artefacts are CC-BY 4.0. Use them, adapt them, ship them. Attribution appreciated.
