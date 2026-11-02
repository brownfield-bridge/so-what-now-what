# The test run, 24 to 28 October 2026

One owner built two brains from this kit on the same subject, "getting value from AI in companies", from 12 free public reports and papers: brain A in Claude Code, brain B in the Claude app. The rules and the predictions were fixed before the first build; changes during the run were logged. The brains themselves stay private. These are the counts.

## The headline numbers

| | Brain A (Claude Code) | Brain B (the Claude app) |
|---|---|---|
| Time from paste to finished brain | about 34 min | about 55 min |
| Sources read | 12 of 12 | 12 of 12 |
| Pages written | 11 | 26 |
| Claims on the pages carrying a tag | 220 of 220 | 715 of 715 |
| Tags pointing to a real source, log line or map row (structural check; whether each is the right tag was not checked) | 220 of 220 | 715 of 715 |
| Pages changed by the weekly job | 0 (19 of 19 files unchanged) | 0 (33 of 33 unchanged) |
| Intake items sorted as expected | 4 of 4 | 4 of 4, under its own owner's gate |
| Pages written before the owner's yes | 0 | 0 |
| Links that resolve in Obsidian | 0 of 11 | all |

The owner answered the five setup questions differently in each build, so A and B are two owners' brains, not one spec built twice.

**The research scan** (see `research-funnel.md`): 174,274 unique arXiv records, 111,926 new in the six-month window, 6,671 in the chosen categories, 525 past the first pass, 303 qualifying, 50 on the map. About 35 minutes; the classifier cost $0.30. 24 of the 50 rows passed the weekly review.

**The weekly job.** Run by hand: brief written, last line correct, no page changed. Scheduled in Claude Code with Windows Task Scheduler: the first run wrote no brief, because the permission line `Write(review/**)` is not honoured; the job refused to print a success line and corrected an earlier claim of its own. After the fix to `Edit(review/**)` it ran unattended and wrote the brief. It could not open one 16 MB PDF and marked it not assessed. In the Claude app, both scheduled attempts ran inside the open chat and asked for folder access, which the owner granted; unattended running was not shown.

**The weekly review** (brain A, 36 minutes): 6 of 6 decisions put to the owner; 26 inferred claims confirmed and 1 dropped; 24 map rows added after a check against their abstracts (9 reworded, 1 advice line dropped as not in the abstract); 30 claims now carry the owner's dated yes, each with a matching line in the log. The AI marked one option "Recommended" for each decision, and the owner took it every time.

**The questions** (four; Q1 to Q3 fixed before the first build, Q4 after the weekly review; see `seed-and-questions.md`): each tool answered from its own brain and from the other's, and the Claude app also read brain A through the computer link. Pages were named in every answer. On the question the brains were built not to cover (current EU law), all four brain sessions said so and marked general knowledge. A clean chat (no brain, memory off, web search on) answered the same four questions.

**The citation check.** One AI reviewer checked all 293 tagged claims in the brain-backed answers against the pages they cited; a second re-checked the 31 disputed or borderline ones and agreed on 28. Final: 269 supported (91.8%), 22 overstated, 2 not found, 0 contradicted. Brain A answers 83.5%, brain B answers 98.2%. The overstatements mostly dropped a qualifier ("one firm", "not randomised", "abstract only"); two started in a page's own summary line.

## Prediction by prediction

| Measure | Predicted | Result | |
|---|---|---|---|
| Build time | under 90 min | 34 and 55 min | met |
| Sources read | 12 of 12 | 12 of 12, both | met |
| Pages with no Sources list | 0 | 0, both | met |
| Pages before the yes | none | none, both | met |
| Rules file holds edges, gate, one rule | 3 of 3 | 3 of 3, both | met |
| Manual prep: brief, last line, no page changed | hold | hold, both | met |
| Intake sorted | 3 of 3 in one build | 4 of 4 in A; correct under its own gate in B | met |
| Scheduled run, Claude Code | fires | fired; first run wrote no brief; second run, after the fix, wrote it | met after a kit fix |
| Scheduled run, the Claude app | cannot reach a local folder | reached it, inside the open chat, after asking for access | not tested to the end |
| Weekly review | all decisions put; pages match | 6 of 6; pages match the log | met |
| Pages named in answers | every answer | every answer, both tools, both brains | met |
| Uncovered question marked | holds | all four brain sessions | met |
| No search outside the brain folder | holds | answers saved to intake only; tool logs not checked | not verified |
| Obsidian links | work | B yes; A 0 of 11 (titles in links, short names on files) | half missed |
| Clean chat claims supported | lower than the brain's | not checked claim by claim | not measured |
| Clean chat names sources | 2 of 3 | every answer; about half its links were aggregators or summaries | met |
| Uncovered question, clean chat | answers without marking | searched the web and answered the law question well, with sources, better than either brain | missed |
| The owner's ruling (Q4) | brain follows it; clean chat gives the default | did not discriminate: the ruling matches the published consensus | missed |
| Claims tagged | 95%+ | 100%, both | met |
| Tags match the path | 90%+ | 100%, structural check only | met, structurally |
| Owner tags with no yes in the log | 0 | 0 | met |
| Inferred claims listed for confirmation | all | A 27 of 27; B 89 of 89 | met |
| Research scan: under 1% reach the page | under 1% | 0.03% | met |
| Citation check | 90%+ | 91.8% | met, narrowly |

## What the kit changed after the run
- The weekly job's permission is `Edit(review/**)` (`weekly-prep/schedule.md`).
- Claude Code with the computer's scheduler is recommended for the weekly job.
- Large files get a text copy in `raw/text/`.
- The review asks the owner's view first and marks no option as recommended.
- The read-first block now sends agents to current sources for anything that can change; the old line "use only this brain" likely kept them from it.
- Answers carry a claim's limits ("abstract only", "one study") into the answer.
- The page check covers summary lines and links with no matching file.
- File name = page title, so links resolve in any Markdown notes app.
- The `commercial` flag (brain B's own idea) is offered as an option.
- A note on rebuilding the pages from the sources when a better model arrives.

Apart from the `Edit(review/**)` fix, these changes were made after the run and have not been re-tested.

## Limits
One person, two builds, one subject, public reports. The questions and the intake items were fixed by Claude; the reviewers are Claude models; both tools ran Claude, so no agent from another maker was tested. The run used Anthropic's tools, so there is a potential bias. The tools change often; these counts are for 24 to 28 October 2026.

*Concepts, arguments, and voice are mine. Claude is used as an editing and scaffolding tool. If others' concepts are used, they are referenced in the sources section.*
