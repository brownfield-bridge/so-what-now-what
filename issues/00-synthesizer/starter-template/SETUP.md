# Setup: Apps Script starter template

5 minutes to deploy a working Sunday-evening synthesizer.

## What you need before you start

- A Google account (Gmail, Workspace, anything that gives you access to script.google.com)
- An Anthropic API key (get one at [console.anthropic.com](https://console.anthropic.com); pay-as-you-go; this workflow costs roughly $0.05 to $0.10 per weekly run with Claude Sonnet)
- A list of 5 to 20 RSS feeds you want to monitor

## Deployment

1. Go to [script.google.com](https://script.google.com) and click **New project**
2. Delete the default `function myFunction() {}` placeholder
3. Open `apps-script.gs` from this folder, copy all content, paste into the Apps Script editor
4. Edit the `CONFIG` block at the top of the script:
   - `RELEVANCE_WINDOW`: your domain, role, decision horizon. Be specific. Vague windows produce flat briefs.
   - `RSS_FEEDS`: paste your feed URLs (one per line, single-quoted, comma-separated)
   - `RECIPIENT_EMAIL`: where the brief should arrive
   - `ANTHROPIC_API_KEY`: your key from console.anthropic.com
5. Save (Ctrl+S). Give the project a name like "So What, Now What synthesizer".

## First run (test)

1. In the function dropdown at the top of the Apps Script editor, select `testRun`
2. Click **Run**
3. First time only: Apps Script will request permissions. Grant them (URL fetch + Gmail send).
4. Wait 30 to 90 seconds for the run to complete
5. Check your inbox. The brief should arrive.

If nothing arrives, open the **Executions** tab (clock icon in the left sidebar) and check for errors.

## Schedule it

Once the test run works:

1. Select `setupWeeklyTrigger` in the function dropdown
2. Click **Run**
3. Done. The synthesizer now runs every Sunday at 17:00 in your script's timezone.

To verify the schedule: left sidebar → **Triggers** (clock icon). You should see one trigger pointed at `runSynthesizer`.

To change the day or time: edit `setupWeeklyTrigger` in `apps-script.gs` (look for `SUNDAY` and `atHour(17)`), save, then run `setupWeeklyTrigger` once more.

## Where to get RSS feeds

Most newsletter platforms expose RSS:

- **Substack**: append `/feed` to a publication URL (`https://stratechery.com/feed`)
- **Beehiiv**: same pattern (`https://so-what-now-what.beehiiv.com/feed`)
- **Medium**: append `/feed` to a tag or author URL
- **News sites**: most have a `/rss` or `/feed.xml` path

If a source does not expose RSS, services like RSS.app, Inoreader, or Feedly can generate one.

## Troubleshooting

- **No email arrives.** Open **Executions** in the left sidebar and check the most recent run for an error message. Most common causes: invalid API key, malformed RSS feed URL, recipient email mismatch.
- **Empty brief.** Your relevance window is too narrow, or your feeds had no new items in the past 7 days. Widen the window or add more feeds.
- **API cost surprise.** Each weekly run with Claude Sonnet costs roughly $0.05 to $0.10. If you want cheaper, change `ANTHROPIC_MODEL` to a Haiku model. Cost drops to under $0.01.
- **Apps Script execution timeout.** If you have more than 30 feeds, the script may exceed Apps Script's 6-minute limit. Reduce the feed count.

## License

CC-BY 4.0.
