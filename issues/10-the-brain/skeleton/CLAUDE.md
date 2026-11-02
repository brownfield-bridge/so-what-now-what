# [SUBJECT] brain: rules

*Template from the So What, Now What Issue 10 kit (CC-BY 4.0). Claude used as editing and scaffolding tool; sources in the kit's SOURCES.md.*

**Owner:** [NAME]. **Weekly review:** [DAY].

## The subject and its edges
- Covers: [what is in].
- Does not cover: [what is out].
- Helps with: [the decisions or outputs this brain serves].
- Sources I trust, in order: [for example: peer-reviewed studies and official statistics first; firm surveys next; consultancy reports last, marked as commercial].

## The folder
- `raw/` - sources. Read them, never edit them. `raw/text/` holds text copies of files too large to open.
- `intake/` - new material waiting for the weekly review, including answers other agents saved.
- `pages/` - pages written from the sources. One topic per page. The file name is exactly the page title. Every page ends with a **Sources** list, with dates.
- `review/` - weekly briefs.
- `index.md` - one line per page. Read it first, every time.
- `log.md` - one dated line per change: `## [YYYY-MM-DD] add | ...`, `## [YYYY-MM-DD] decide | ...` (a yes or no at the review), `## [YYYY-MM-DD] answer | ...`, `## [YYYY-MM-DD] check | ...`.

## Where each claim came from
Every claim on a page ends with one tag, including claims in a page's opening summary. Choose it from the path the claim came in by, never from how sure it sounds:

| Tag | Use it when | Must show |
|---|---|---|
| `[read]` | You read the whole source in `raw/` | The file name |
| `[abstract]` | You saw only a summary or abstract (for example a map-of-the-field row) | The link |
| `[told]` | The owner said it or dropped it in `intake/` with no source to open | The intake file and date, or "setup answers" and the build date |
| `[owner]` | The owner decided it in a weekly review | The `log.md` date |
| `[inferred]` | You connected sources and no single source says it | The sources you connected |

If two paths apply, use the stronger one, in the order above. Never write `[owner]` yourself: only a yes in the review creates it. `[inferred]` stays until the owner confirms it (it becomes `[owner]`) or drops it.

*Optional:* add `commercial` inside the tag when the source sells what it reports on (for example `[read: 02; commercial]`).

## The gate
[Paste from feed-gate.md and adjust.]

## The agent's three tasks
- **Add a source:** read it, propose which pages change, change them after the owner's yes, update the index and log.
- **Answer from the pages:** read the index, then the pages; name the pages you used. Carry each claim's limits into the answer: if the source is `[abstract]`, one study, one firm, not randomised or self-reported, say so in the same sentence. For anything that can change (a law, a price, who holds a role, a recent figure), check current sources and report them with source and date, apart from the pages. Save a good answer to `intake/`, never to the pages.
- **Check the pages:** contradictions, stale claims, claims without a tag (summary lines included), `[inferred]` claims the owner has not confirmed, pages without sources, `[[links]]` with no matching page file.

## The weekly review
For every item under NEEDS DECISION and TO CONFIRM: set out both sides, ask the owner's view first, and mark no option as recommended. Change the pages only after the owner's yes, and log each decision with its date.

## The one rule
Pages change only after the owner's yes. A scheduled job may prepare a brief; it may not change a page.

## When a better model arrives
The sources in `raw/` and the decisions in `log.md` stay. The pages may be rewritten from them; every `[owner]` claim carries over with its date.
