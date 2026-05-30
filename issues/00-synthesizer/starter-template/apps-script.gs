/**
 * So What, Now What — Synthesizer Starter Template (v1)
 *
 * A Google Apps Script that runs the So-What / Now-What synthesizer
 * on your RSS feed list every Sunday evening and emails the brief
 * to your inbox by Monday morning.
 *
 * Setup: see SETUP.md in the same folder.
 *
 * License: CC-BY 4.0
 * Source: github.com/brownfield-bridge/so-what-now-what
 */

// =============================================================
// CONFIGURATION — edit these values, then save
// =============================================================

const CONFIG = {
  // Your relevance window. Be specific. Vague windows produce flat briefs.
  RELEVANCE_WINDOW: {
    domain: '3-5 watch areas, e.g. industrial automation, agentic commerce, EU AI regulation, mid-cap industrial M&A, energy procurement',
    function: 'your role, e.g. CEO of a 500-person components manufacturer',
    horizon: 'mid 3-12m', // one of: 'near 0-3m', 'mid 3-12m', 'long 12m+'
  },

  // RSS feeds to monitor (5 to 20 is a reasonable starting range)
  RSS_FEEDS: [
    'https://example.com/feed1.xml',
    'https://example.com/feed2.xml',
    // Add more feeds here, one per line, between single quotes, with commas
  ],

  // Where to send the brief
  RECIPIENT_EMAIL: 'your-email@example.com',

  // Anthropic API config
  ANTHROPIC_API_KEY: 'sk-ant-...', // Get one at console.anthropic.com
  ANTHROPIC_MODEL: 'claude-sonnet-4-6', // or 'claude-haiku-4-5' for cheaper/faster
  MAX_TOKENS: 4096,
};

// =============================================================
// MAIN — runs weekly via trigger
// =============================================================

function runSynthesizer() {
  try {
    Logger.log('Synthesizer run started: ' + new Date());

    const signals = fetchAllSignals();
    Logger.log('Fetched ' + signals.length + ' signals from ' + CONFIG.RSS_FEEDS.length + ' feeds');

    if (signals.length === 0) {
      sendEmail(
        'Synthesizer: no signals this week',
        'No new items in your feeds in the past 7 days. Check your RSS feed list or widen the window.'
      );
      return;
    }

    const prompt = buildPrompt(signals);
    Logger.log('Prompt size: ' + prompt.length + ' chars');

    const brief = callClaude(prompt);
    Logger.log('Brief size: ' + brief.length + ' chars');

    sendEmail(
      'So What, Now What — your weekly brief (' + formatDate(new Date()) + ')',
      brief
    );
    Logger.log('Email sent to ' + CONFIG.RECIPIENT_EMAIL);
  } catch (e) {
    Logger.log('Error: ' + e.message);
    sendEmail(
      'Synthesizer error',
      'The synthesizer hit an error and did not produce a brief.\n\n' +
        'Error: ' + e.message + '\n\nStack:\n' + e.stack
    );
  }
}

// =============================================================
// RSS — fetch and parse feeds
// =============================================================

function fetchAllSignals() {
  const allSignals = [];

  for (const feedUrl of CONFIG.RSS_FEEDS) {
    try {
      const response = UrlFetchApp.fetch(feedUrl, { muteHttpExceptions: true });
      if (response.getResponseCode() !== 200) {
        Logger.log('Skip ' + feedUrl + ' (HTTP ' + response.getResponseCode() + ')');
        continue;
      }
      const xml = response.getContentText();
      const items = parseRssFeed(xml, feedUrl);
      allSignals.push.apply(allSignals, items);
    } catch (e) {
      Logger.log('Failed to fetch ' + feedUrl + ': ' + e.message);
    }
  }

  return allSignals;
}

function parseRssFeed(xml, feedUrl) {
  const items = [];
  try {
    const document = XmlService.parse(xml);
    const root = document.getRootElement();
    const channel = root.getChild('channel');
    if (!channel) return items;

    const channelItems = channel.getChildren('item');
    for (const item of channelItems) {
      const title = getChildText(item, 'title');
      const link = getChildText(item, 'link');
      const pubDate = getChildText(item, 'pubDate');
      const description = stripHtml(getChildText(item, 'description'));

      if (pubDate && !isWithinPastWeek(pubDate)) {
        continue;
      }

      items.push({
        title: title,
        link: link,
        date: pubDate,
        description: description.substring(0, 300),
        source: feedUrl,
      });
    }
  } catch (e) {
    Logger.log('Parse error for ' + feedUrl + ': ' + e.message);
  }
  return items;
}

function getChildText(parent, childName) {
  const child = parent.getChild(childName);
  return child ? child.getText() : '';
}

function stripHtml(html) {
  return html.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
}

function isWithinPastWeek(dateString) {
  try {
    const itemDate = new Date(dateString);
    const weekAgo = new Date();
    weekAgo.setDate(weekAgo.getDate() - 7);
    return itemDate >= weekAgo;
  } catch (e) {
    return true; // If we can't parse the date, include the item
  }
}

// =============================================================
// PROMPT — build the synthesizer prompt
// =============================================================

function buildPrompt(signals) {
  const window = CONFIG.RELEVANCE_WINDOW;

  const signalText = signals
    .map(function (s, i) {
      return (
        i + 1 + '. ' + s.title + '\n' +
        '   ' + s.description + '\n' +
        '   Link: ' + s.link
      );
    })
    .join('\n\n');

  return (
    'I need a So-What / Now-What synthesis on this week\'s signals,\n' +
    'filtered against my relevance window and scored for materiality.\n\n' +
    'MY RELEVANCE WINDOW\n' +
    '- Domain: ' + window.domain + '\n' +
    '- Function: ' + window.function + '\n' +
    '- Decision horizon: ' + window.horizon + '\n\n' +
    'THIS WEEK\'S SIGNALS\n' +
    signalText + '\n\n' +
    'YOUR TASK\n' +
    '1. Drop signals outside my relevance window.\n' +
    '2. Score remaining signals on three axes 1 to 5:\n' +
    '   - Speed of impact (how fast does this hit my P&L)\n' +
    '   - Scope of impact (how broad across functions and units)\n' +
    '   - Reversibility cost (how expensive to wait)\n' +
    '3. For signals scoring 9 or higher out of 15, write:\n' +
    '   - So What: one sentence specific to my business, no abstractions\n' +
    '   - Now What: one concrete move available this week or this month\n' +
    '4. Signals scoring below 9 go to Monitor with a one-line note\n' +
    '   on what would push them above threshold.\n\n' +
    'OUTPUT FORMAT\n' +
    '- Top: 3-line headline summary\n' +
    '- Body: table with Signal | Score | So What | Now What\n' +
    '- Bottom: Monitor list\n\n' +
    'CONSTRAINTS\n' +
    'No generic answers. If the So What could apply to any company,\n' +
    'rewrite. If you cannot name a concrete Now What, demote to Monitor.\n' +
    'The brief is one page, not a digest.'
  );
}

// =============================================================
// CLAUDE — call the Anthropic API
// =============================================================

function callClaude(prompt) {
  const url = 'https://api.anthropic.com/v1/messages';
  const payload = {
    model: CONFIG.ANTHROPIC_MODEL,
    max_tokens: CONFIG.MAX_TOKENS,
    messages: [{ role: 'user', content: prompt }],
  };

  const options = {
    method: 'post',
    contentType: 'application/json',
    headers: {
      'x-api-key': CONFIG.ANTHROPIC_API_KEY,
      'anthropic-version': '2023-06-01',
    },
    payload: JSON.stringify(payload),
    muteHttpExceptions: true,
  };

  const response = UrlFetchApp.fetch(url, options);
  const responseCode = response.getResponseCode();
  const responseText = response.getContentText();

  if (responseCode !== 200) {
    throw new Error('Claude API returned HTTP ' + responseCode + ': ' + responseText);
  }

  const json = JSON.parse(responseText);
  return json.content[0].text;
}

// =============================================================
// EMAIL — send the brief
// =============================================================

function sendEmail(subject, body) {
  GmailApp.sendEmail(CONFIG.RECIPIENT_EMAIL, subject, body, {
    name: 'So What, Now What Synthesizer',
  });
}

function formatDate(date) {
  return Utilities.formatDate(date, Session.getScriptTimeZone(), 'EEEE d MMMM yyyy');
}

// =============================================================
// TRIGGERS — set up the weekly schedule
// =============================================================

/**
 * Run this ONCE to set up the weekly schedule.
 * Default: every Sunday at 17:00 in your script timezone.
 * Edit the .onWeekDay() and .atHour() calls below to change the schedule.
 */
function setupWeeklyTrigger() {
  // Remove existing triggers first to avoid duplicates
  const triggers = ScriptApp.getProjectTriggers();
  for (const trigger of triggers) {
    if (trigger.getHandlerFunction() === 'runSynthesizer') {
      ScriptApp.deleteTrigger(trigger);
    }
  }

  ScriptApp.newTrigger('runSynthesizer')
    .timeBased()
    .everyWeeks(1)
    .onWeekDay(ScriptApp.WeekDay.SUNDAY)
    .atHour(17)
    .create();

  Logger.log('Weekly trigger set: every Sunday at 17:00 (script timezone)');
}

/**
 * Run this to test the synthesizer manually
 * without waiting for the Sunday schedule.
 */
function testRun() {
  runSynthesizer();
}
