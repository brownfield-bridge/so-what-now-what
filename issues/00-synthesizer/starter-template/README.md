# Starter template: weekly synthesizer workflow

A working automation that runs the synthesizer prompt on your RSS feed list every Sunday evening and emails the brief to your inbox by Monday morning.

## v1: Google Apps Script (free, ~5 minutes to deploy)

The Apps Script version is the lowest-friction path for most readers. No new platform sign-up; runs on the Google account you already have.

- [`apps-script.gs`](apps-script.gs): the working script (about 230 lines, well-commented)
- [`SETUP.md`](SETUP.md): 5-minute deployment guide

Recommended for readers who:

- Want the fastest path from clone to running
- Already have a Google account
- Have or are willing to get an Anthropic API key

## What the workflow does

1. Pulls signals from your RSS feed list (5 to 20 feeds you configure)
2. Filters to items published in the past 7 days
3. Calls Claude (Anthropic API) with the synthesizer prompt and your relevance window
4. Emails the brief to your inbox by Monday morning

Cost: roughly $0.05 to $0.10 per weekly run with Claude Sonnet. Switch to Haiku for under $0.01.

## Alternative platforms (coming later)

Make.com scenario and n8n workflow versions are on the roadmap for readers who prefer those tools. They will land in a future issue's artefact pack. Apps Script does the same job today with less setup.

## License

CC-BY 4.0. Use it, adapt it, ship it. Attribution appreciated.
