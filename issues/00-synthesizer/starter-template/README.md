# Starter template: Sunday-evening synthesizer workflow

Status: under construction. Final template lands before Issue 0 ships on Sunday 7 June 2026.

This folder will contain a working automation that runs the synthesizer prompt on your own signal feed every Sunday evening and drops a 1-page brief into your inbox by Monday morning.

## What the workflow does

1. Pulls signals from your RSS feed list (you configure 10 to 40 feeds)
2. Concatenates them into a single prompt input
3. Calls a frontier model (Claude, GPT, or Gemini) with the prompt from `../prompt.md` and your relevance window
4. Formats the output into a 1-page brief
5. Sends to your inbox or writes to a Notion page by 7am Monday

## What this folder will include

- `make-scenario.json`: a Make.com scenario you can import directly
- `n8n-workflow.json`: an n8n workflow as an alternative for self-hosters
- `SETUP.md`: step-by-step configuration (account setup, API keys, RSS feed list, relevance window, output destination)

## Why both Make and n8n

Make is the lowest-friction option (cloud-hosted, drag-and-drop, free tier covers most personal use). n8n is for readers who prefer self-hosting and want full control over the prompt and data flow.

You only need to set up one.

## License

CC-BY 4.0.
