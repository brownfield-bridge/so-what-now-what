# Recipe: the synthesizer in Claude Code (full control)

Same discipline, run from the command line, version-controlled, scriptable. This rung is for readers who want the relevance window in a file they own, the brief written to disk every week, and the whole thing wired into cron or CI rather than a desktop app.

If the Cowork recipe is the executive's hands-off path, this is the operator's path. Pick it if you live in a terminal, want the window under git, or want to pipe the brief somewhere of your own.

## What you need

- [Claude Code](https://docs.claude.com/en/docs/claude-code) installed and authenticated.
- Web search available (on by default).
- Optional: a mailbox MCP server (for example a Gmail MCP) if you want it reading your inbox as well as the web. Web-only works fine; the inbox just sharpens the set.

## What is in this folder

- `CLAUDE.md`: the standing context. Holds the synthesis discipline so every run behaves the same. You should not need to touch it.
- `relevance-window.md`: your window. This is the one file you edit. Three to five watch areas, your role, your horizon.
- `.claude/commands/synthesize.md`: the `/synthesize` command. Reads your window, gathers signals, scores, writes the brief.
- `run-weekly.sh`: a one-line headless runner for cron.
- `briefs/`: where each week's brief lands, dated.

## Setup

1. Copy this folder to where you want it to live (or keep it as a clone of the repo).
2. Open `relevance-window.md` and replace the placeholders with your own window. This is the only required edit.
3. From inside the folder, run an interactive test:

   ```
   claude
   > /synthesize
   ```

   It reads your window, pulls the week's signals from the web (and your mailbox if an MCP is connected), scores them, and writes `briefs/YYYY-MM-DD-brief.md`.

4. Read the brief. If it is flat, your window is too generous. Tighten `relevance-window.md` and run again.

## Run it every week without you

`run-weekly.sh` runs the command headless and exits:

```bash
#!/usr/bin/env bash
cd "$(dirname "$0")"
claude -p "/synthesize" --allowedTools "WebSearch,Read,Write" --model claude-sonnet-4-6
```

Schedule it with cron for Sunday 17:00:

```
0 17 * * 0  /path/to/claude-code-recipe/run-weekly.sh >> /path/to/claude-code-recipe/briefs/cron.log 2>&1
```

The brief is written to `briefs/` by Monday. Pipe it onward however you like: email it with `mail`, drop it in a synced folder, post it to a channel. That last step is yours, deliberately. The brief is for you to read before anyone else acts on it.

## Cost

You pay per run through your Claude Code usage. A weekly synthesis is a small job: a batch of web reads and one structured write. Switch the `--model` flag to a smaller model if you want it cheaper still.

## The honest limits

- Web-only sees public sources. Connect a mailbox MCP if your real signal arrives by newsletter.
- The score is a first pass built from the window you wrote. You overrule it; that is the point of keeping the window in a file you control.
- Keep the outward send as a step you own. Unattended gathering is safe. Unattended broadcasting is not.

## License

CC-BY 4.0. Use it, adapt it, ship it. Attribution appreciated.
