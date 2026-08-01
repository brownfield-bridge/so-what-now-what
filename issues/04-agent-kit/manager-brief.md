# Manager brief

> ### ▸ EDIT THIS FILE
> It is filled in with a worked example (a manufacturer's monthly review) so the demo runs out of the box. **Replace the example values with yours.** Every line tagged **EDIT ▸** is a spot you change — keep the structure, change the content.

---

## The deliverable
- What it is — *Monthly Business Review for leadership*
  **EDIT ▸** your recurring deliverable
- Cadence — *monthly*
  **EDIT ▸** weekly / monthly / quarterly
- Who receives it and signs — *the CFO; it goes up to the board*
  **EDIT ▸** the named human who owns the sign-off
- Run day and delivery — *the 3rd of each month, once month-end close lands; the checked draft comes to me to sign*
  **EDIT ▸** the day it should run (a date each month, or a weekday each week) — and it delivers to **you**, never to the recipients

## The target — what "good" looks like, in my words
> **EDIT ▸ replace all of the rules below with your own.** Make them **checkable, not vague** ("every variance over 5% gets a reason grounded in the data", not "make it insightful"). Fastest way: paste a past deliverable you were proud of and ask the agent to extract the rules from it, then edit.
1. Every figure cites the exact source file it came from.
2. Every variance over 5% (relative) gets an explanation grounded in the sources.
3. Every section ends with a "so what", not just a number.
4. Any claim about *why* something moved is backed by a figure we actually hold.
5. Any forward-looking statement is flagged as a judgment call for a named human, never asserted as fact.

## Output format
- Render the self-check ("red-pen") review as a self-contained HTML artifact, matching the style of `red-pen-example.html` in the sources folder: verdict chips, figures struck through with the correct source value beside them, unsupported reads flagged/highlighted, and a closing box with the questions the recipient will ask.
- The deliverable draft itself stays a clean document (Markdown/Google Doc) — only the self-check gets the visual HTML treatment.

## Delivery — where the finished output lands (autonomous, no per-run instruction needed)
- **Destination folder: `Northwind - Reviews`** (a sibling Drive folder to the sources folder, same parent as `Northwind — June 2026`). Never write outputs into the sources folder itself — that folder is read-only input, per the guardrails below.
- On every run, after the self-check passes, **save both files directly into `Northwind - Reviews`** — do not just present them as chat artifacts and stop:
  1. **The deliverable draft** — upload as a Google Doc (default text-to-Doc conversion is fine).
  2. **The red-pen self-check** — upload with `content_mime_type: text/html` and `disable_conversion_to_google_type: true`, so it stays a real, styled `.html` file rather than being flattened into a Google Doc.
  - Name both files with the period, e.g. `Northwind MBR — June 2026.{gdoc,html}`, so cycles don't overwrite each other and stay sortable by date.
- If a live email address is configured instead of (or in addition to) Drive delivery, send both as attachments to the named recipient in **The deliverable** above; otherwise Drive delivery is the default.
- Confirm delivery in your final chat message with the Drive links to both saved files — don't just say "done," show where they landed.
  **EDIT ▸** if you'd rather have delivery go to a different folder name, or by email instead of Drive, say so here.

## The substrate — what the agent may draw on
- Sources folder — **`./sources/`** — use nothing outside it for figures, causes, or forecasts.
  *(Keep this pointing at your sources folder — no change needed unless you rename it.)*
- Off-limits: no figure, cause, or forecast may be invented or inferred beyond what the sources support.

## Guardrails and sign-off — autonomy by stakes
> **EDIT ▸ adjust to your risk.** What may the agent do alone, and what must always reach a named human?
- Runs alone: extraction, arithmetic, formatting, and delivering the finished draft + self-check to the Reviews folder (see Delivery above).
- Drafts with its reasoning shown, I review: interpretation and the "read".
- A named human signs, no exceptions: financial figures, forward-looking lines, anything that leaves for the board.
- The agent never writes into, edits, or overwrites anything in the **sources folder** — only into the separate Reviews/delivery destination.

## Revision log — the brief compounds
- 2026-06: created.
- 2026-08: added the Output format section — self-check now renders as a styled HTML artifact instead of plain text.
- 2026-08: added the Delivery section — both the draft and the self-check now save automatically to the `Northwind - Reviews` Drive folder every cycle (HTML saved as a real `.html` file, not flattened into a Doc), so a one-line trigger produces a finished, filed result with nothing left as a chat-only download.
  **EDIT ▸** add one line each cycle: the thing it got wrong or missed, so it does not repeat. Log any change to the report's **format** here too — the template is the contract, so its shape only changes when you decide it should, not by drift.
