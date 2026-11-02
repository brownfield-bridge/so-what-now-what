# Research at scale: a map of the field in one page

**What it is for.** Your brain grows from what you happen to read. This feed gives it breadth: a screened map of everything published on your subject in the last few months, cheap enough to rerun every quarter.

**What it is not.** It is not evidence. Every row comes from an abstract only. A paper enters a real page only after you have read it and it has passed the feed gate.

**Credit.** Adapted from Ruben Hassid, "Jev. Copy & paste prompts for this new AI", How to AI, 20 September 2026, section 3 (https://ruben.substack.com/p/jev). His example screens six months of AI papers on arXiv for people who use AI in a chat window; he invites readers to swap in their own case. The structure below is his. The changes are mine: the reader's fit goes into the ranking, and the output lands as one page in your brain instead of a sheet and a website.

## The five steps

1. **Harvest the whole field, not a search.** Take title, abstract, authors, categories, first-submitted date and link for every paper in your categories and window. For arXiv, use the bulk harvesting feed (OAI-PMH), not the search interface, which is built for queries and unreliable past a few thousand results. Two details matter:
   - The feed's date filter is the last update, so filter in code on the first version's date. Remove duplicates by paper ID.
   - Before going on, count one week of one category and compare it with arXiv's own listing for that week. If you are more than 10% off, stop.
   - Two traps we hit in our own run. On arXiv, the date in the standard metadata is often a later version's date, not the first; ask for the format that lists every version (`arXivRaw`) and take the first version's date from it. And a page of results can come back carrying a pointer to the wrong next page, which would skip a week without any error; harvest one week at a time and check that each page carries on from the last.
2. **First pass: drop only what is clearly not for your reader.** A typed classifier answers a few questions per abstract, such as "what is the main contribution" and "is this about the subject or only mentions it". It drops a paper only when it is confident (0.7 or above) that the paper is outside the subject. Everything else goes on.
3. **Check 50 before running thousands.** Run the first pass on 50 random papers and read the answers yourself. Fix the questions if they misfire, then run the rest.
4. **Second pass: score the survivors, rank in code.** The classifier answers usefulness to your reader, topic, audience fit, strength of evidence and whether the finding holds across several models. Code does the counting and the ranking. Rank on usefulness, evidence and fit together, so a paper written for someone else cannot top your list. Answers below 0.6 confidence go to a borderline list, labelled only with the broad bucket.
5. **Prose only for the top rows.** A strong model reads the abstracts of the top rows only and writes, for each, one line on what to do differently and one on what to watch out for, with the link. Then it writes the page into `intake/`.

## Rules
- The classifier decides categories. Code does every count, date and rank. The strong model writes prose only for the top rows.
- Abstracts only. Never download the full papers in this run.
- Respect the database's rate limits, and save every page as it arrives, so a stopped run can resume and a rerun costs nothing.

## Why it is cheap
- Rules remove most of the pile before any model runs.
- A typed classifier answers in a few words with a confidence, at a fraction of a strong model's price.
- The strong model sees only the top rows, and only their abstracts.

One run, for scale (Issue 10 test, 24 October 2026, subject "getting value from AI in companies", six months of arXiv in econ.GN, cs.CY and cs.HC, with cs.AI only when cross-listed): 174,274 unique records harvested, 111,926 first submitted in the window, 6,671 in the chosen categories, 525 past the first pass, 303 qualifying, top 50 on the map. About 35 minutes from harvest to page; the classifier cost $0.30, with no failed calls. A spot check against arXiv's own listing for 19 to 23 October matched 102 of 103 papers (the 103rd was correctly outside the window). At the weekly review, 24 of the 50 rows went into the brain after a check against their abstracts.

## The prompt (fill the brackets)

```
Use [your typed classifier] for every classification. You write and run the code; I only read results.

QUESTION
Which [database] papers from the last [months] actually help [the reader the brain serves] do [the work]? Not [what is out of scope].

1. HARVEST. Pull title, abstract, authors, categories, first-submitted date, ID and link for every paper in [categories] first submitted in the window. Use the bulk harvesting interface, not search. Follow every page until done, wait between requests, save each page as it arrives. Filter in code on the first version's date; dedupe on ID. Sanity check one week against the database's own listing; if more than 10% off, stop and tell me. Print counts per category per month.
2. FIRST PASS (all papers, title and abstract only). Ask at once:
   - main_contribution: choice of [6 to 10 options, each with one crisp criterion]
   - on_subject: yes/no/unknown "[The main finding is about the subject, not a passing mention.]"
   Drop only [out-of-subject options] with confidence 0.7 or above. Report how many were dropped and why.
3. CHECKPOINT. Run the first pass on 50 random papers, show me title, answers and confidence, wait for my OK, then run all.
4. SECOND PASS (survivors). Ask at once:
   - usefulness: score from "useless to [reader]" to "changes how [reader] should work"
   - topic: choice of [your topics]
   - fit: choice of [reader types], including "other audience"
   - evidence: score from "opinion" to "multi-model or large controlled study"
   - generalises: yes/no/unknown "The finding holds across several models or settings."
5. RANK in code: keep usefulness 3 or above with confidence 0.6 or above; sort by usefulness x evidence, and exclude fit = other audience from the top [N]. Below 0.6 confidence goes to a Borderline list with the broad bucket only.
6. For the top [N] only, you (not the classifier) read the abstract and write one line on what to do differently and one line on what to watch out for, with the link. Translate, do not paraphrase.
7. OUTPUT. raw/field-scan-[date].csv with every row; intake/map-of-the-field-[date].md with the date, the count at each step, the clusters and the top rows, each tagged [abstract]; a run log with time and cost.

RULES: the classifier decides categories; code does all counting, dates and ranking. Abstracts only. Cache everything. Stop only for missing access, a failed sanity check, or the checkpoint.
```

## Where it lands
- `raw/field-scan-[date].csv`: all rows, never edited.
- `intake/map-of-the-field-[date].md`: the one page, written into intake like any other feed. At the weekly review you approve it into `pages/` (replacing the last one) or refuse it; the model never writes it into `pages/` itself.
- Single papers: you move one into intake when you decide to read it in full.

## Tools
The original recipe uses Jev, a typed classifier from TypeSafe, run from Claude Code or Codex through the TypeSafe skill. Ruben's post (section 0) shows how to install it. A cheap model with structured output can stand in; this kit's run measured Jev only. Disclosure: I was among Jev's first 100,000 users. I have no other link to TypeSafe.

*Concepts, arguments, and voice are mine. Claude is used as an editing and scaffolding tool. If others' concepts are used, they are referenced in the sources section.*
