# Sources for Issue 6, in full

The newsletter carries a short version. This is the long one, kept here because this is where
anyone who wants to check is already standing.

The measure itself: the design effect from survey sampling and the effective sample size it implies. The term and the formula are Leslie Kish's, in Survey Sampling, Wiley, 1965, taken here as Kohli states and uses it in his equation 1, and not read at first hand. One thing this tool does differently from the paper, stated because it is its last unfixed weakness: Kohli feeds the formula the pairwise phi coefficient, which for a binary right-or-wrong record is the ordinary correlation the formula asks for. This tool feeds it a weighted agreement score instead, which is inflated by how often two reviewers would coincide anyway. Inflated agreement gives a smaller effective number, so on that count the tool understates independence rather than overstating it. What the score is made of, and what it is worth, is set out in the next paragraph.


**What the agreement score actually is, and how much the setting matters.** The script does not use plain agreement. Line 249 sets `VERDICT_WEIGHT = 0.25`, and every pair is scored as `0.25 x (same verdict) + 0.75 x (criticism overlap)`. That is a choice, and it is the one place a reader could reasonably suspect this instrument of grading itself, so here is the whole of it.

The verdict used to carry half. Under verdict unanimity, which is the common case, agreement can never fall below the weight, so at nine checks a weight of 0.5 puts a hard ceiling of 1.80 on n_eff. A tool that asks you to compare your number against a published 2.18 must be able to reach 2.18, and at 0.5 it could not. At 0.25 the ceiling is 3.00. That is the reason for the change, and it is structural rather than a fit to the target.

Here is every headline figure in this kit recomputed across the full range, by driving this script:

| | w=0.00 | **0.25 (shipped)** | 0.50 | 0.75 | 1.00 |
|---|---|---|---|---|---|
| run-v3, nine checks | 3.11 | **2.72** | 2.42 | 2.17 | 1.98 |
| run-v4, nine checks | 2.25 | **2.12** | 2.00 | 1.89 | 1.80 |
| run-v5, three checks | 1.58 | **1.63** | 1.68 | 1.74 | 1.80 |

**On the headline the shipped setting is the conservative one.** A lower weight gives a lower mean agreement, a higher effective number, and a panel that looks *more* independent, which is weaker support for the argument this kit exists to make. Re-run run-v3 at the old 0.5 and you get 2.42 rather than 2.72: more damning, not less. Nothing was set to make the case easier.

**On the noise floor it is the generous one, and that half matters more.** The floor rests on a single repeated pair, so it moves faster than anything else here. At the shipped 0.25 run-v3's panel clears its floor by 0.20 (2.72 against 2.52). At 0.5 the floor rises to 3.32 and the panel sits 0.90 *below* it, which reverses the finding rather than softening it. Read the 0.20 as the most setting-dependent number in this kit and do not build an argument on it.

**Dating.** Every published figure in every file here, including the archived `run-v3/result-lexical.json` from 30 August, reproduces at 0.25 and only at 0.25. Nothing in this repo carries a figure produced under the old weight.

The constant is one line and it is yours to change. If you do, change it before you score anything and say so when you report the number.

The nine-judge result: G. Kohli (Apple), “Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation Panels”, arXiv 2605.29800, 28 May 2026, read at full text. His unit is model families, not companies: the paper says nine frontier LLMs from seven model families, and the newsletter's seven companies is a gloss that reads slightly more provider diversity into the panel than he claims. n_eff 2.18, with a 95% bootstrap interval of 2.07 to 2.31 and a mean pairwise correlation of 0.391, on 1,000 items across three natural-language-inference datasets and a pairwise preference task. A preprint, not peer reviewed, and run on classification rather than open-ended review, so read the 2.18 as a measured instance and not a universal constant. The five-judge figure of 1.96, the 90% and the 0.22 are his section 4.4. The human range of 4.0 to 5.8 is his table 3, estimated by drawing ten labels per item from the hundred-annotator pool and treating the annotators as interchangeable, so it is an estimate rather than an observed panel. The crowd at the country show: F. Galton, “Vox Populi”, Nature, 1907; his printed figures (middlemost 1207 lb, dressed weight 1198 lb) were corrected to 1208 and 1197 by K. F. Wallis, “Revisiting Francis Galton’s Forecasting Competition”, Statistical Science 29(3), 2014, so the true error is 11 lb rather than the 9 he reported. Correlated errors across more than 350 models: Kim, Garg, Peng & Garg, ICML 2025, arXiv 2506.07962; the 60% figure is reported on one of its leaderboard datasets, not across all of them. Dependence-aware aggregation, and the case that agreement should be discounted rather than counted: Balasubramanian, Podkopaev & Kasiviswanathan, ICML 2026, arXiv 2601.22336. Shared bias between models from the same family, and the 0.67-to-0.53 figure: arXiv 2603.17111, which measures seventeen vision-language models on visual question answering, so that figure is carried across modalities here. Read the pair precisely: its section 4.3 reports them as the Pearson correlation of per-question accuracy vectors across 136 model pairs, within-family 0.67 and cross-family 0.53, and its table 8 gives them per benchmark, so 0.67 and 0.53 is the VQAv2 row. It is not an agreement rate, and 0.67 is already two different models that share a family, so switching model inside a family moves nothing; the same paper puts effective voters at 2.5 to 3.6, above the nine-judge result. Where verification actually pays: arXiv 2608.06940, 7 August 2026, measured on code benchmarks with unit-test execution as the second signal, not a second model. Its own terms are pivotal queries and the one-vote margin, and the gain it reports is +10.4 to +23.3 percentage points across three headline configurations.

---

The measure here belongs to survey statistics, and putting it on a panel of AI judges is Guneet Kohli's move, not mine (arXiv 2605.29800). The findings this rests on are other people's and are cited in the sources. What is mine is crossing three framings against three models as a measured factor, the repeated cell used as a noise floor, the decision-impact tag and the solo-findings rule built on it, running it on a decision document rather than a labelling task, and packaging it so it needs no API key. The run and the reading of it are mine too.

Arguments and voice are mine. Claude is used as an editing and scaffolding tool. If others' concepts are used, they are referenced in the sources section.
