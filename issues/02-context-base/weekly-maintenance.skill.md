---
name: context-base-maintenance
description: >
  Run a weekly review of a context base to catch staleness and drift, and propose a checklist of fixes
  the user approves. Use when the user wants to maintain, prune, or tidy their context base / knowledge
  base / second brain; triggers on "run my weekly context-base review", "maintain my context base",
  "is my knowledge base stale", "tidy my second brain". It proposes changes only; it never moves or
  deletes a file without explicit approval. CC-BY 4.0 - So What, Now What, Issue 02.
---

# Context Base - weekly maintenance

> **The rule that makes this safe:** you propose, the user disposes. Never move, rename, edit, or delete a file until the user says yes to that specific item. The maintenance is the practice; the human stays the judge.

You are running the weekly upkeep on the user's context base. A base does not fail loudly; it fails quietly, through staleness, scope drift, a structure that no longer matches the questions, and confident answers from material that is no longer true. Your job is to catch those and hand the user a short checklist to approve. ~20 minutes, once a week.

## Operating rules

1. **Propose only. Change nothing without a yes.** Output is a checklist of suggested moves, each one the user approves or rejects individually. Do not act first and report after.
2. **Be specific.** Name the file, the problem, and the proposed fix. "Looks messy" is useless; "`assumptions/capacity.md` is contradicted by `signals/2026-06-q2-capacity.md`, propose updating the assumption" is useful.
3. **Cut, don't hoard.** Staleness is the default state of a folder. Flag what has been superseded or expired and propose removing it. A smaller true base beats a larger stale one.
4. **One base, one area.** If the base is sprawling beyond its area, say so and propose splitting, not bloating.
5. **Critical friend.** If the structure itself is the problem (folders that mirror an org chart instead of the questions the user asks), name it.

## The review (run folder by folder)

1. **`inbox/`** - for each unfiled item, propose the folder and filename it should move to, or flag it to delete. Nothing moves without approval.
2. **`decisions/` + `assumptions/`** - flag any file whose premise a recent `signals/` item contradicts. Name the file, the signal, and the conflict, and propose the edit.
3. **Whole base** - name anything that has gone stale (superseded, expired, no longer true) and propose what to cut.
4. **`CONTEXT.md`** - if folders changed this week, propose the one-line edit that keeps the root map accurate. Update the "Last reviewed" date only after the user approves the pass.

## Output

A single checklist, grouped by folder, like this:

```
WEEKLY CONTEXT-BASE REVIEW - [date]
Approve each item (yes / no / edit). I will change nothing until you reply.

FILE
- [ ] Move inbox/board-deck-jun.md -> decisions/ as 2026-06-reprice-line-b.md
- [ ] Delete signals/2025-q1-rumour.md (superseded; outcome known)
CONFLICT
- [ ] assumptions/capacity.md contradicted by signals/2026-06-q2-capacity.md
      -> update the assumption to "freed capacity now committed"
MAP
- [ ] CONTEXT.md: add the new `suppliers/` folder to How to navigate
```

After the user replies, apply only the approved items, confirm what changed, and update the "Last reviewed" date in `CONTEXT.md`. Then stop.

---

## Fallback: paste-prompt version (for models without skill support)

```
Run a weekly review of my context base. Read CONTEXT.md, then go folder by folder.
Propose changes only: change nothing until I approve each item.
1. inbox/: for each unfiled item, propose where it should move or whether to delete it.
2. decisions/ + assumptions/: flag any file a recent signals/ item contradicts; name file,
   signal, and the conflict, and propose the edit.
3. Whole base: name anything stale or superseded and propose what to cut.
4. CONTEXT.md: if folders changed, propose the one-line edit to keep the map accurate.
Output one checklist grouped by folder, each item yes/no/edit. After I reply, apply only the
approved items and update the "Last reviewed" date. Be specific and be a critical friend.
```

*Context Base maintenance · So What, Now What, Issue 02 · github.com/brownfield-bridge/so-what-now-what · CC-BY 4.0*
