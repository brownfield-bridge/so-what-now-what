#!/usr/bin/env python3
"""
The Independence Test
---------------------
You asked several AI checks to review the same thing. They agreed.
This tells you how much of that agreement was information, and how much was echo.

It does one thing nothing off-the-shelf does: it audits the panel instead of
running it. Eval frameworks (promptfoo, DeepEval, Langfuse, Braintrust) will
happily run a jury and take a majority vote. None of them tell you whether the
jury is one opinion wearing nine hats.

Two numbers come back.

    n_eff = n / (1 + (n - 1) * r_bar)

The effective number of independent opinions. It is the design effect survey
statisticians use to discount a sample of respondents who are not independent
of each other. Reviewers are a sample too. If your checks never agree,
n_eff = n. If they always agree, n_eff = 1. Everything real sits in between.

Then the same agreement, split by what varied. The default nine checks are a
balanced 3 x 3: three model families crossed with three framings. Every pair
therefore either changed the framing and held the model, or changed the model
and held the framing, or changed both. Averaging the first two groups
separately tells you which axis actually bought you independence on your own
document, instead of asking you to take it from the literature.

Usage:
    python independence_test.py --answers answers.json --doc "board paper"
    python independence_test.py --verify      # reproduce the published figures

You run the ten checks yourself, in your own chat windows, using prompts.md.
This does the arithmetic on what came back. No API keys, no accounts, no cost,
no server, no database. One file, standard library only.

It does not call any model. That is deliberate: a version that called the
models for you existed and was cut, because it needed three keys and three
SDKs, it hardcoded model names that go stale, and it had never been run. A kit
with one tested path is worth more than one with two paths where one is a
promise.

CC BY 4.0 - So What, Now What, Issue 6.
"""

import argparse, itertools, json, os, random, re, sys, textwrap
from dataclasses import dataclass, field

# --------------------------------------------------------------------------
# The nine configurations: a balanced crossing, three families x three framings.
#
# Balanced is not decoration. It is what lets the report separate the two axes.
# Nine cells give nine framing-axis pairs and nine model-axis pairs, so both
# averages rest on the same amount of evidence. Drop a cell and the comparison
# stops being a comparison.
#
# Why these three framings and not four. Neutral, adversarial and inverted vary
# the instruction while the model sees the same document. A fourth framing in
# circulation, "stripped" (withhold the author's reasoning and sources), varies
# the document instead. It is a useful check in its own right and the prompt is
# kept below, but it does not belong on an axis built to isolate framing, and
# mixing it in would confound the very number this tool exists to report.
# --------------------------------------------------------------------------

AXIS_FRAMINGS = ["neutral", "adversarial", "inverted"]

FRAMINGS = {
    "neutral":     "You are reviewing the work below. List what is wrong with it.",
    "adversarial": "The work below contains at least one material error. Find it. "
                   "Do not report that the work is sound.",
    "inverted":    "Argue the opposite case to the one the work below makes. "
                   "Then list what the work would have to show to survive your argument.",
    # Off-axis. Varies the document, not the instruction. Not in the default nine.
    "stripped":    "Review the work below. You have not been given the author's "
                   "reasoning or their sources. Judge only what is on the page.",
}



OUTPUT_CONTRACT = textwrap.dedent("""
    Return JSON only, no prose around it:
    {
      "verdict": "SOUND" | "MINOR_ISSUES" | "MATERIAL_PROBLEMS" | "UNSOUND",
      "criticisms": [
        {"target": "<the specific claim, section or number you are criticising>",
         "criticism": "<one sentence, one problem, no hedging>",
         "if_true": "CHANGES_THE_DECISION" | "WEAKENS_THE_EVIDENCE" | "NEITHER"}
      ]
    }
    if_true asks one thing: if this criticism is correct, does the work's own
    recommendation still follow? CHANGES_THE_DECISION means it does not.
    WEAKENS_THE_EVIDENCE means a supporting claim is unreliable but the
    conclusion may still stand. NEITHER means it is true and does not move the
    decision. Answer it about your own criticism; do not rank the others.
    Return EXACTLY FIVE criticisms, ranked most serious first. Not four, not six.
    One problem each. Be specific about the target - "the revenue figure in
    section 3", not "the analysis". If you believe the work is sound, still name
    the five weakest points; "no criticism" is not an available answer.
""").strip()


@dataclass
class Review:
    config_id: str
    verdict: str = ""
    criticisms: list = field(default_factory=list)
    error: str = ""
    family: str = ""
    framing: str = ""
    doc: str = ""
    replicate: bool = False


# --------------------------------------------------------------------------
# Matching. Two criticisms are the same criticism when they hit the same target
# with the same complaint. This is the honest hard part: matching is a
# judgement, and a lexical matcher will get some of them wrong.
#
# What matters is WHICH WAY it gets them wrong. A missed match makes two
# identical criticisms look like two opinions, which inflates n_eff and flatters
# you. A false match makes two distinct criticisms look like one, which deflates
# n_eff and costs you nothing but a little credit. For a tool whose entire
# subject is people over-counting their own independence, the second error is
# the safe one, so the thresholds here lean that way deliberately and the report
# says so.
#
# --matcher llm uses a model instead, which you should treat with suspicion,
# because it makes the audit itself another correlated check. The tool says so
# in its own output rather than hiding it.
# --------------------------------------------------------------------------

STOP = set("the a an of to in for is are was were on at by with and or that this "
           "it its as be been from not no than then there their has have had "
           "which what when will would could should may might do does did".split())

SUFFIXES = ("ations", "ation", "ically", "ingly", "ions", "ing", "ion", "ies",
            "ed", "es", "ly", "s")


def stem(w):
    for s in SUFFIXES:
        if w.endswith(s) and len(w) - len(s) >= 4:
            return w[:-len(s)]
    return w


def bag(s):
    return {stem(w) for w in re.findall(r"[a-z0-9]+", (s or "").lower())
            if w not in STOP and len(w) > 2}


def containment(x, y):
    """Overlap as a share of the smaller set. Forgiving about length, which
    matters because one model writes eight words and another writes twenty."""
    if not x or not y:
        return 0.0
    return len(x & y) / min(len(x), len(y))


def same_criticism(x, y, target_t=0.5, crit_t=0.25, crit_alone_t=0.6):
    tx, ty = bag(x.get("target")), bag(y.get("target"))
    cx, cy = bag(x.get("criticism")), bag(y.get("criticism"))
    if not cx or not cy:
        return False
    c = containment(cx, cy)
    if containment(tx, ty) >= target_t and c >= crit_t:
        return True
    return c >= crit_alone_t


def criticism_overlap(A, B, matcher):
    """One-to-one matching, then Jaccard over the matched sets.

    Both lists empty means both checks looked and raised nothing. That is
    complete agreement, not complete disagreement. Scoring it as 0.0 was the
    single largest source of inflated n_eff in the previous version, and it hit
    the commonest real case: a document everyone waves through.
    """
    if not A and not B:
        return 1.0
    if not A or not B:
        return 0.0
    used, matches = set(), 0
    for x in A:
        for j, y in enumerate(B):
            if j in used:
                continue
            if matcher.same(x, y):
                used.add(j)
                matches += 1
                break
    return matches / (len(A) + len(B) - matches)


# --------------------------------------------------------------------------
# Two matchers.
#
# The lexical one is the default and needs nothing. The LLM one is a single
# call: every criticism from every check goes in at once and comes back
# clustered, so the same clustering drives both the overlap scores and the solo
# findings. One call, not one per pair.
#
# It is genuinely better at paraphrase and genuinely worse epistemically,
# because the audit now contains a model. The report names the model that did
# it. That is the disclosure, and it is the reason this is not the default.
# --------------------------------------------------------------------------

class LexicalMatcher:
    name = "lexical"
    note = ("It leans toward calling two criticisms the same, which pushes\n"
            "  n_eff down rather than up. That is the safe direction here.")

    def same(self, x, y):
        return same_criticism(x, y)


class LLMMatcher:
    def __init__(self, clusters, model):
        self.clusters = clusters
        self.model = model
        self.name = f"llm ({model})"
        self.note = (f"{model} decided which criticisms were the same. Your audit\n"
                     "  now contains a model, and it is not independent of the models\n"
                     "  being audited. Treat this number as indicative, not audited.")

    def same(self, x, y):
        a, b = self.clusters.get(x.get("_id")), self.clusters.get(y.get("_id"))
        return a is not None and a == b


CLUSTER_PROMPT = textwrap.dedent("""
    Below are {n} criticisms of the same piece of work, each with an id.

    Group the ids that are making THE SAME criticism: the same problem, about
    the same target. Two different problems with the same target are NOT the
    same criticism. Two criticisms are not the same merely because they are
    about the same section, or equally severe, or equally vague.

    Return JSON only, no prose:
    {{"clusters": [[1, 4, 7], [2], [3, 5]]}}

    Every id must appear exactly once, in exactly one cluster.

    --- CRITICISMS ---
    {items}
""").strip()


VERDICT_WEIGHT = 0.25   # see the note below


def pair_agreement(a: Review, b: Review, matcher):
    """Agreement on the verdict, and overlap of the criticisms raised.

    The verdict used to carry half the weight. That put a floor under r_bar
    whenever every check returned the same verdict, which is the common case,
    and the floor put a ceiling on n_eff: at nine checks it could never exceed
    1.8, however different the criticisms were. A tool that asks you to compare
    your number against a published 2.18 must be able to reach 2.18.

    So the verdict now carries a quarter. It is still information - agreeing on
    the bottom line is agreement - but the reasons are three quarters of the
    answer, which is the right way round for a measure of independent opinion.
    Verdict unanimity is reported separately so nothing is hidden.
    """
    v = 1.0 if (a.verdict and a.verdict == b.verdict) else 0.0
    return v, criticism_overlap(a.criticisms, b.criticisms, matcher)


SEVERITY_ORDER = ["CHANGES_THE_DECISION", "WEAKENS_THE_EVIDENCE", "NEITHER"]


# --------------------------------------------------------------------------
# Answers you already have. The whole analysis runs on ten JSON blobs; nothing
# in it needs an API key. This is the path for someone who ran the checks by
# hand in three chat windows and wants the arithmetic done properly.
# --------------------------------------------------------------------------
def load_answers(path, doc="your document"):
    """Read cells from a JSON file (list or single object) or a directory of them.

    Each cell needs cell_id (or config_id), verdict and criticisms. Family,
    framing and replicate are read from the id when not given explicitly, so
    "A-neutral", "B-adversarial", "C-inverted" and "A-neutral#2" all work, and
    so does any other labelling as long as it is <group>-<framing>.
    """
    def _read(fp):
        try:
            return json.load(open(fp, encoding="utf-8"))
        except json.JSONDecodeError as e:
            raise SystemExit(
                f"{fp} is not valid JSON: {e.msg}, line {e.lineno}.\n"
                "Paste each model's answer exactly as it came back, with nothing "
                "before or after it, and put the ten of them in a list: [ {...}, {...} ].")
        except OSError as e:
            raise SystemExit(f"Cannot read {fp}: {e.strerror}.")

    blobs = []
    if os.path.isdir(path):
        for f in sorted(os.listdir(path)):
            if f.endswith(".json"):
                blobs.append(_read(os.path.join(path, f)))
    else:
        blobs.append(_read(path))

    cells = []
    for b in blobs:
        cells.extend(b if isinstance(b, list) else [b])

    out, seen_ids = [], set()
    for c in cells:
        cid = c.get("cell_id") or c.get("config_id")
        if not cid:
            raise SystemExit("A cell has no cell_id. Every answer must echo the id "
                             "of the block it came from, or you cannot tell which "
                             "chat it came out of.")
        if cid in seen_ids:
            raise SystemExit(f"Two answers both claim to be {cid}. One came from the "
                             f"wrong chat. Re-run that cell rather than guessing.")
        seen_ids.add(cid)
        base = cid.split("#")[0]
        fam = c.get("family") or base.split("-")[0]
        fr = c.get("framing") or (base.split("-", 1)[1] if "-" in base else "neutral")
        out.append(Review(config_id=cid, verdict=c.get("verdict", ""),
                          criticisms=c.get("criticisms", []), family=fam, framing=fr,
                          doc=c.get("doc", doc),
                          replicate=bool(c.get("replicate", "#" in cid))))
    if not out:
        raise SystemExit("No cells found in " + path)
    return out


def n_effective(n, r_bar):
    if n <= 1:
        return float(n)
    r_bar = max(0.0, min(1.0, r_bar))
    return n / (1 + (n - 1) * r_bar)


def classify(a: Review, b: Review):
    """What varied between these two checks."""
    same_family = a.family and a.family == b.family
    same_framing = a.framing and a.framing == b.framing
    if same_family and same_framing:
        return "replicate"         # changed nothing: this is the noise floor
    if same_family and not same_framing:
        return "framing_axis"      # changed the framing, held the model
    if same_framing and not same_family:
        return "model_axis"        # changed the model, held the framing
    return "both"


def _pairs(reviews, matcher):
    """All within-document pairs of live checks."""
    out = []
    for a, b in itertools.combinations(reviews, 2):
        if a.doc != b.doc:
            continue
        v, o = pair_agreement(a, b, matcher)
        out.append({"pair": f"{a.config_id} / {b.config_id}", "doc": a.doc,
                    "varied": classify(a, b), "ids": (a.config_id, b.config_id),
                    "verdict_match": v, "criticism_overlap": round(o, 3),
                    "agreement": round(VERDICT_WEIGHT * v + (1 - VERDICT_WEIGHT) * o, 3)})
    return out


def _mean(vals):
    return round(sum(vals) / len(vals), 3) if vals else None


def analyse(reviews, matcher=None):
    matcher = matcher or LexicalMatcher()
    live = [r for r in reviews if not r.error]
    grid = [r for r in live if not r.replicate]
    reps = [r for r in live if r.replicate]
    docs = sorted({r.doc for r in grid})
    if len(grid) < 2:
        return None

    # n is checks per document, not checks in total.
    per_doc = [len([r for r in grid if r.doc == d]) for d in docs] or [len(grid)]
    n = round(sum(per_doc) / len(per_doc))
    if n < 2:
        return None

    pairs = _pairs(grid, matcher)
    if not pairs:
        return None
    r_bar = sum(p["agreement"] for p in pairs) / len(pairs)

    def axis(kind):
        g = [p["agreement"] for p in pairs if p["varied"] == kind]
        return _mean(g), len(g)

    framing_r, framing_n = axis("framing_axis")
    model_r, model_n = axis("model_axis")

    # Is the gap between the two axes bigger than shuffling would produce?
    # Without this the report will announce a winner from a difference of 0.05
    # across nine noisy pairs, which is the exact error this tool exists to
    # catch. A direction is printed only when the data supports one.
    axis_p = None
    fa = [x["agreement"] for x in pairs if x["varied"] == "framing_axis"]
    ma = [x["agreement"] for x in pairs if x["varied"] == "model_axis"]
    if len(fa) >= 3 and len(ma) >= 3:
        obs = abs(sum(fa) / len(fa) - sum(ma) / len(ma))
        pool, hits, N = fa + ma, 0, 20000
        rng = random.Random(0)
        for _ in range(N):
            rng.shuffle(pool)
            a, b = pool[:len(fa)], pool[len(fa):]
            if abs(sum(a) / len(a) - sum(b) / len(b)) >= obs - 1e-12:
                hits += 1
        axis_p = round(hits / N, 3)

    # ---- noise floor: the same model, same framing, run twice -------------
    floor_pairs = []
    for rep in reps:
        twin = next((r for r in grid if r.doc == rep.doc and r.family == rep.family
                     and r.framing == rep.framing), None)
        if twin:
            v, o = pair_agreement(rep, twin, matcher)
            floor_pairs.append(VERDICT_WEIGHT * v + (1 - VERDICT_WEIGHT) * o)
    r_self = _mean(floor_pairs)

    # ---- jackknife: drop one check, see where n_eff lands -----------------
    jack = []
    for cid in sorted({r.config_id for r in grid}):
        keep = [p["agreement"] for p in pairs if cid not in p["ids"]]
        if keep and n > 2:
            jack.append(round(n_effective(n - 1, sum(keep) / len(keep)), 2))

    # ---- per-document n_eff ----------------------------------------------
    by_doc = {}
    for d in docs:
        dp = [p["agreement"] for p in pairs if p["doc"] == d]
        dn = len([r for r in grid if r.doc == d])
        if dp and dn >= 2:
            by_doc[d] = round(n_effective(dn, sum(dp) / len(dp)), 2)

    # ---- solo findings, computed inside each document --------------------
    distinct = solo = 0
    solo_examples = []
    decisive, decisive_solo, weakening, severity_seen = [], [], [0], [False]
    for d in docs:
        seen = {}
        for r in [x for x in grid if x.doc == d]:
            for c in r.criticisms:
                k = next((k for k, v in seen.items() if matcher.same(c, v["c"])), None)
                if k is None:
                    seen[len(seen)] = {"c": c, "by": {r.config_id},
                                       "sev": [c.get("if_true")]}
                else:
                    seen[k]["by"].add(r.config_id)
                    seen[k]["sev"].append(c.get("if_true"))
        distinct += len(seen)
        for v in seen.values():
            if len(v["by"]) == 1:
                solo += 1
                solo_examples.append(v["c"])
            worst = next((x for x in SEVERITY_ORDER if x in v["sev"]), None)
            if worst:
                severity_seen[0] = True
                if worst == "CHANGES_THE_DECISION":
                    decisive.append(v["c"])
                    if len(v["by"]) == 1:
                        decisive_solo.append(v["c"])
                elif worst == "WEAKENS_THE_EVIDENCE":
                    weakening[0] += 1

    verdicts = [r.verdict for r in grid if r.verdict]
    top = max(set(verdicts), key=verdicts.count) if verdicts else ""
    unanimity = (verdicts.count(top), len(verdicts), top)

    return {"n": n, "documents": len(docs), "r_bar": round(r_bar, 3),
            "severity_reported": severity_seen[0],
            "changes_the_decision": len(decisive),
            "changes_the_decision_solo": len(decisive_solo),
            "weakens_the_evidence": weakening[0],
            "decisive_findings": decisive, "decisive_solo_findings": decisive_solo,
            "verdict_unanimity": unanimity,
            "n_eff": round(n_effective(n, r_bar), 2),
            "n_eff_jackknife": (min(jack), max(jack)) if jack else None,
            "n_eff_by_document": by_doc,
            "pairs": pairs,
            "framing_axis_agreement": framing_r, "framing_axis_pairs": framing_n,
            "axis_difference_p": axis_p,
            "model_axis_agreement": model_r, "model_axis_pairs": model_n,
            "noise_floor_agreement": r_self,
            "n_eff_at_noise_floor": round(n_effective(n, r_self), 2) if r_self is not None else None,
            "families_run": sorted({r.family for r in grid if r.family}),
            "distinct_criticisms": distinct,
            "raised_by_one_config_only": solo,
            "unique_issue_rate": round(solo / distinct, 3) if distinct else 0.0,
            "solo_findings": solo_examples}


def report(res, reviews, matcher):
    print("\n" + "=" * 66)
    print("  THE INDEPENDENCE TEST")
    print("=" * 66)
    for r in reviews:
        tag = f"{r.config_id}{' (replicate)' if r.replicate else ''}"
        doc = f"  [{r.doc}]" if r.doc and len({x.doc for x in reviews}) > 1 else ""
        print(f"  {tag:<26} {r.error if r.error else r.verdict}{doc}")
    if not res:
        print("\n  Fewer than two checks completed. Nothing to compare.")
        return
    print("-" * 66)
    d = res["documents"]
    print(f"  Checks per document             {res['n']}"
          f"{'' if d == 1 else f'   (over {d} documents)'}")
    print(f"  Mean agreement between them     {res['r_bar']}")
    u = res.get("verdict_unanimity")
    if u and u[1]:
        print(f"  Verdicts                        {u[0]} of {u[1]} said {u[2]}")
    print(f"\n  EFFECTIVE INDEPENDENT OPINIONS  {res['n_eff']}\n")
    lost = res["n"] - res["n_eff"]
    print(f"  You ran {res['n']} checks and got {res['n_eff']} opinions' worth of")
    print(f"  information. {lost:.2f} of them were echo.")
    if res["n_eff_jackknife"]:
        lo, hi = res["n_eff_jackknife"]
        print(f"  Drop any single check and it lands between {lo} and {hi}.")
    if d == 1:
        print("  One document. Read this as indicative. See --help on why.")

    print("-" * 66)
    print("  WHAT BOUGHT THE INDEPENDENCE      (lower agreement = more bought)")
    f_r, f_n = res["framing_axis_agreement"], res["framing_axis_pairs"]
    m_r, m_n = res["model_axis_agreement"], res["model_axis_pairs"]
    print(f"    Changed the framing, held the model   "
          f"{'not measured' if f_r is None else f'{f_r:<6} ({f_n} pairs)'}")
    print(f"    Changed the model, held the framing   "
          f"{'not measured' if m_r is None else f'{m_r:<6} ({m_n} pairs)'}")
    pv = res.get("axis_difference_p")
    if f_r is not None and m_r is not None:
        if pv is not None and pv >= 0.05:
            print(f"    -> Indistinguishable. Shuffling the pairs at random produces a")
            print(f"       gap this big {pv:.0%} of the time, so this run cannot tell the")
            print("       two axes apart. Do not read a winner into it.")
        elif f_r < m_r:
            print(f"    -> Changing the framing bought more (p = {pv}).")
        else:
            print(f"    -> Changing the model bought more (p = {pv}).")
            print("       Worth keeping. It is not what the literature reports.")

    if res["noise_floor_agreement"] is not None:
        print("-" * 66)
        print("  THE NOISE FLOOR       (same model, same framing, asked twice)")
        print(f"    It agreed with itself                 {res['noise_floor_agreement']}")
        print(f"    n_eff if every check were that check  {res['n_eff_at_noise_floor']}")
        gap = res["n_eff"] - res["n_eff_at_noise_floor"]
        if gap <= 0.15:
            print("    -> Your panel is at its own noise floor. What looks like")
            print("       disagreement is the same model being random twice.")
        else:
            print(f"    -> Your panel clears its noise floor by {gap:.2f}. That gap,")
            print("       not n_eff itself, is what the crossing actually bought.")

    if len(res["n_eff_by_document"]) > 1:
        print("-" * 66)
        print("  PER DOCUMENT")
        for k, v in res["n_eff_by_document"].items():
            print(f"    {k:<44} {v}")

    print("-" * 66)
    print(f"  Distinct problems raised        {res['distinct_criticisms']}")
    print(f"  Raised by only one check        {res['raised_by_one_config_only']}"
          f"  ({res['unique_issue_rate']:.0%})")
    if res["solo_findings"]:
        print("\n  The findings you would have lost by running one check:")
        for c in res["solo_findings"][:6]:
            print(f"    - [{c.get('target','?')}] {c.get('criticism','')}")
    print("-" * 66)
    if res.get("severity_reported"):
        print("  WHAT WOULD CHANGE THE DECISION    (each check's own call on its own")
        print("                                     criticism, not a fourth model's)")
        print(f"    Findings that change the decision     {res['changes_the_decision']}")
        print(f"      of those, raised by one check only  {res['changes_the_decision_solo']}")
        print(f"    Findings that only weaken evidence    {res['weakens_the_evidence']}")
        if res["decisive_solo_findings"]:
            print("\n    Read these first. One check found each, and each one means")
            print("    the recommendation does not follow:")
            for c in res["decisive_solo_findings"][:4]:
                print(f"      - [{c.get('target','?')}] {c.get('criticism','')}")
        elif res["decisive_findings"]:
            print("\n    Read these first. Each means the recommendation does not follow:")
            for c in res["decisive_findings"][:4]:
                print(f"      - [{c.get('target','?')}] {c.get('criticism','')}")
        else:
            print("    -> No check said any of its own findings changes the decision.")
            print("       Either the work is sound, or nobody looked at the numbers")
            print("       the conclusion is computed from.")
    else:
        print("  WHAT WOULD CHANGE THE DECISION")
        print("    -> Not available. No check returned the if_true field, so this run")
        print("       predates it. Sorting the findings is yours to do, with one")
        print("       question: if this criticism is true, does the recommendation")
        print("       still follow? Do not hand that question to another model.")
    print("-" * 66)
    if res["n_eff"] < 2:
        print("  READ THIS AS: you have one opinion. Not a review.")
    elif res["n_eff"] < 3:
        print("  READ THIS AS: two opinions. Better than one, not a panel.")
    else:
        print("  READ THIS AS: a real spread. Unusual. Keep whatever you did.")
    print(f"\n  Matcher: {matcher.name}. {matcher.note}")
    print("=" * 66 + "\n")


def verify():
    """Reproduce the published figures, so the claim that it does is checkable."""
    print("\n  Reproducing arXiv 2605.29800 from its reported mean correlation.\n")
    for n, published in ((9, 2.18), (5, 1.96)):
        got = n_effective(n, 0.391)
        flag = "matches" if abs(got - published) < 0.011 else "DOES NOT MATCH"
        print(f"    n={n}, r_bar=0.391  ->  n_eff = {got:.2f}"
              f"   (paper: {published})  {flag}")
    print("\n  Degenerate cases:")
    for label, n, r in (("checks never agree ", 9, 0.0),
                        ("checks always agree", 9, 1.0)):
        print(f"    {label}  ->  n_eff = {n_effective(n, r):.2f}")
    print()


EPILOGUE = """
Getting a number you can quote
------------------------------
n_eff from nine checks on ONE document is a first look, not a measurement. The
nine checks are your sample size for the panel; the document is your sample size
for the agreement. One document gives you one draw of r_bar, and r_bar is the
whole answer. The published 0.391 rests on three datasets, not one paragraph.

So: do it over three to five pieces of work you actually had checked, one at a
time, and look at whether the numbers land near each other. If they are far
apart, you have learned something more useful than any average.

Run one block twice. Without that repeat you cannot tell disagreement from
randomness, and a model being random twice reads as independence. Compare n_eff
against that noise floor, not against zero.
"""


def main():
    ap = argparse.ArgumentParser(
        description="Measure whether your AI checks are independent.",
        epilog=EPILOGUE, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--answers", metavar="PATH",
                    help="the checks you ran by hand: a JSON file of cells, or a "
                         "directory of them. This is the only way in. No API keys, "
                         "no accounts, no cost.")
    ap.add_argument("--json", help="write the full result to this path")
    ap.add_argument("--doc", default="your document",
                    help="name for the document, used with --answers")
    ap.add_argument("--verify", action="store_true",
                    help="reproduce the published figures and exit")
    a = ap.parse_args()

    if a.verify:
        verify()
        return
    if not a.answers:
        ap.error("give me --answers with the checks you ran, or --verify")

    if True:
        reviews = load_answers(a.answers, doc=a.doc)
        n_rep = sum(1 for r in reviews if r.replicate)
        print(f"Read {len(reviews)} checks from {a.answers}"
              f"{' (one of them a repeat)' if n_rep == 1 else ''}. "
              f"No models were called.", file=sys.stderr)
        if n_rep == 0:
            print("  Note: no repeated cell, so there is no noise floor and you "
                  "cannot tell\n  disagreement from randomness. Run one block a "
                  "second time.", file=sys.stderr)
    k = 0
    for r in reviews:
        for c in r.criticisms:
            c["_id"] = k
            k += 1

    matcher = LexicalMatcher()

    res = analyse(reviews, matcher)
    report(res, reviews, matcher)
    if a.json and res:
        json.dump({"result": res, "matcher": matcher.name,
                   "reviews": [r.__dict__ for r in reviews]},
                  open(a.json, "w"), indent=2)
        print(f"Full result written to {a.json}\n")


if __name__ == "__main__":
    main()
