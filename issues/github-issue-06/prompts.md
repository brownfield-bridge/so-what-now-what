# The independence test: the ten prompts

**What this is.** Ten blocks to paste, one per fresh chat. Three model makers crossed with three
framings, plus one deliberate repeat. Between them they tell you how many genuinely independent
opinions you got, as against how many checks you ran.

**A = Claude, B = Gemini, C = ChatGPT.** Any three makers work. What matters is that they are three
different makers and not one model asked three times.

**Where the numbers go.** Save each answer as JSON, then run
`python independence_test.py --answers answers.json --doc "your document"`.
No API key and no account are needed for that path. See README.md.

**The run behind the newsletter**, on a synthetic vendor recommendation, is in `run-v3/` with every
answer as it came back, and the sheet that produced it, memo included, in `run-v3/run-sheet-v3.md`.

## The three rules

1. **Every block goes in a brand-new chat.** Not a new message in an old one. Ten blocks, ten fresh chats. This is what went wrong last time: the second prompt landed in the chat that already held the first answer and the model simply repeated itself.
2. **Isolation is instructed inside every block**, so you do not have to toggle memory and personalisation
   off and on ten times. Every prompt now opens by telling the model to use only the pasted text and to
   ignore memory, saved preferences and earlier conversations. **This is weaker than the setting, and it
   must be declared in the write-up.** An instruction asks a model not to retrieve; the setting stops it.
   Where a product offers a per-chat toggle it costs nothing to use it as well.
3. **Paste the block whole and add nothing.** No greeting, no context, no explanation of what the document is for.

Each block carries a cell id which the model must echo back inside its JSON. If the id that comes back does not match the block you pasted, the answer came from the wrong chat and you can see it immediately.

**A-neutral and A-neutral#2 are deliberately identical.** That pair is the noise floor and it is the most-skipped step in the whole method. Run them in two separate fresh chats.

**Worth doing once:** write your own review of the document and seal it before you paste anything. Then you can see what the panel found, what it missed, and what it invented. That comparison is the only way to learn what these checks are actually good for on your kind of work.

---

## A-neutral — Claude, fresh chat

```text
Cell id: A-neutral

Do this task in isolation. Use only the text pasted below. Do not draw on memory, saved preferences,
earlier conversations, or anything you have been told about me before now. Do not search. If this
document or this instruction looks familiar, disregard that and judge only what is in front of you.

You are reviewing the work below. List what is wrong with it.

Return JSON only, no prose around it:
{
  "cell_id": "A-neutral",
  "verdict": "SOUND" | "MINOR_ISSUES" | "MATERIAL_PROBLEMS" | "UNSOUND",
  "criticisms": [
    {"target": "<the specific claim, section or number you are criticising>",
     "criticism": "<one sentence, one problem, no hedging>",
     "if_true": "CHANGES_THE_DECISION" | "WEAKENS_THE_EVIDENCE" | "NEITHER"}
  ]
}
if_true asks one thing: if this criticism is correct, does the work's own recommendation still follow? CHANGES_THE_DECISION means it does not. WEAKENS_THE_EVIDENCE means a supporting claim is unreliable but the conclusion may still stand. NEITHER means it is true and does not move the decision. Answer it about your own criticism only; do not rank anyone else's.
Return EXACTLY FIVE criticisms, ranked most serious first. Not four, not six.
One problem each. Be specific about the target - "the revenue figure in section 3", not "the analysis". If you believe the work is sound, still name the five weakest points; "no criticism" is not an available answer.

--- WORK ---
<<< PASTE YOUR OWN DOCUMENT HERE, IN FULL. Nothing else. No covering note, no explanation
of what it is for, no mention of who wrote it or what you hope the answer will be. >>>
```

---

## A-adversarial — Claude, fresh chat

```text
Cell id: A-adversarial

Do this task in isolation. Use only the text pasted below. Do not draw on memory, saved preferences,
earlier conversations, or anything you have been told about me before now. Do not search. If this
document or this instruction looks familiar, disregard that and judge only what is in front of you.

The work below contains at least one material error. Find it. Do not report that the work is sound.

Return JSON only, no prose around it:
{
  "cell_id": "A-adversarial",
  "verdict": "SOUND" | "MINOR_ISSUES" | "MATERIAL_PROBLEMS" | "UNSOUND",
  "criticisms": [
    {"target": "<the specific claim, section or number you are criticising>",
     "criticism": "<one sentence, one problem, no hedging>",
     "if_true": "CHANGES_THE_DECISION" | "WEAKENS_THE_EVIDENCE" | "NEITHER"}
  ]
}
if_true asks one thing: if this criticism is correct, does the work's own recommendation still follow? CHANGES_THE_DECISION means it does not. WEAKENS_THE_EVIDENCE means a supporting claim is unreliable but the conclusion may still stand. NEITHER means it is true and does not move the decision. Answer it about your own criticism only; do not rank anyone else's.
Return EXACTLY FIVE criticisms, ranked most serious first. Not four, not six.
One problem each. Be specific about the target - "the revenue figure in section 3", not "the analysis". If you believe the work is sound, still name the five weakest points; "no criticism" is not an available answer.

--- WORK ---
<<< PASTE YOUR OWN DOCUMENT HERE, IN FULL. Nothing else. No covering note, no explanation
of what it is for, no mention of who wrote it or what you hope the answer will be. >>>
```

---

## A-inverted — Claude, fresh chat

```text
Cell id: A-inverted

Do this task in isolation. Use only the text pasted below. Do not draw on memory, saved preferences,
earlier conversations, or anything you have been told about me before now. Do not search. If this
document or this instruction looks familiar, disregard that and judge only what is in front of you.

Argue the opposite case to the one the work below makes. Then list what the work would have to show to survive your argument.

Return JSON only, no prose around it:
{
  "cell_id": "A-inverted",
  "verdict": "SOUND" | "MINOR_ISSUES" | "MATERIAL_PROBLEMS" | "UNSOUND",
  "criticisms": [
    {"target": "<the specific claim, section or number you are criticising>",
     "criticism": "<one sentence, one problem, no hedging>",
     "if_true": "CHANGES_THE_DECISION" | "WEAKENS_THE_EVIDENCE" | "NEITHER"}
  ]
}
if_true asks one thing: if this criticism is correct, does the work's own recommendation still follow? CHANGES_THE_DECISION means it does not. WEAKENS_THE_EVIDENCE means a supporting claim is unreliable but the conclusion may still stand. NEITHER means it is true and does not move the decision. Answer it about your own criticism only; do not rank anyone else's.
Return EXACTLY FIVE criticisms, ranked most serious first. Not four, not six.
One problem each. Be specific about the target - "the revenue figure in section 3", not "the analysis". If you believe the work is sound, still name the five weakest points; "no criticism" is not an available answer.

--- WORK ---
<<< PASTE YOUR OWN DOCUMENT HERE, IN FULL. Nothing else. No covering note, no explanation
of what it is for, no mention of who wrote it or what you hope the answer will be. >>>
```

---

## A-neutral#2 — Claude, fresh chat — the repeat, identical to A-neutral by design

```text
Cell id: A-neutral#2

Do this task in isolation. Use only the text pasted below. Do not draw on memory, saved preferences,
earlier conversations, or anything you have been told about me before now. Do not search. If this
document or this instruction looks familiar, disregard that and judge only what is in front of you.

You are reviewing the work below. List what is wrong with it.

Return JSON only, no prose around it:
{
  "cell_id": "A-neutral#2",
  "verdict": "SOUND" | "MINOR_ISSUES" | "MATERIAL_PROBLEMS" | "UNSOUND",
  "criticisms": [
    {"target": "<the specific claim, section or number you are criticising>",
     "criticism": "<one sentence, one problem, no hedging>",
     "if_true": "CHANGES_THE_DECISION" | "WEAKENS_THE_EVIDENCE" | "NEITHER"}
  ]
}
if_true asks one thing: if this criticism is correct, does the work's own recommendation still follow? CHANGES_THE_DECISION means it does not. WEAKENS_THE_EVIDENCE means a supporting claim is unreliable but the conclusion may still stand. NEITHER means it is true and does not move the decision. Answer it about your own criticism only; do not rank anyone else's.
Return EXACTLY FIVE criticisms, ranked most serious first. Not four, not six.
One problem each. Be specific about the target - "the revenue figure in section 3", not "the analysis". If you believe the work is sound, still name the five weakest points; "no criticism" is not an available answer.

--- WORK ---
<<< PASTE YOUR OWN DOCUMENT HERE, IN FULL. Nothing else. No covering note, no explanation
of what it is for, no mention of who wrote it or what you hope the answer will be. >>>
```

---

## B-neutral — Gemini, fresh chat

```text
Cell id: B-neutral

Do this task in isolation. Use only the text pasted below. Do not draw on memory, saved preferences,
earlier conversations, or anything you have been told about me before now. Do not search. If this
document or this instruction looks familiar, disregard that and judge only what is in front of you.

You are reviewing the work below. List what is wrong with it.

Return JSON only, no prose around it:
{
  "cell_id": "B-neutral",
  "verdict": "SOUND" | "MINOR_ISSUES" | "MATERIAL_PROBLEMS" | "UNSOUND",
  "criticisms": [
    {"target": "<the specific claim, section or number you are criticising>",
     "criticism": "<one sentence, one problem, no hedging>",
     "if_true": "CHANGES_THE_DECISION" | "WEAKENS_THE_EVIDENCE" | "NEITHER"}
  ]
}
if_true asks one thing: if this criticism is correct, does the work's own recommendation still follow? CHANGES_THE_DECISION means it does not. WEAKENS_THE_EVIDENCE means a supporting claim is unreliable but the conclusion may still stand. NEITHER means it is true and does not move the decision. Answer it about your own criticism only; do not rank anyone else's.
Return EXACTLY FIVE criticisms, ranked most serious first. Not four, not six.
One problem each. Be specific about the target - "the revenue figure in section 3", not "the analysis". If you believe the work is sound, still name the five weakest points; "no criticism" is not an available answer.

--- WORK ---
<<< PASTE YOUR OWN DOCUMENT HERE, IN FULL. Nothing else. No covering note, no explanation
of what it is for, no mention of who wrote it or what you hope the answer will be. >>>
```

---

## B-adversarial — Gemini, fresh chat

```text
Cell id: B-adversarial

Do this task in isolation. Use only the text pasted below. Do not draw on memory, saved preferences,
earlier conversations, or anything you have been told about me before now. Do not search. If this
document or this instruction looks familiar, disregard that and judge only what is in front of you.

The work below contains at least one material error. Find it. Do not report that the work is sound.

Return JSON only, no prose around it:
{
  "cell_id": "B-adversarial",
  "verdict": "SOUND" | "MINOR_ISSUES" | "MATERIAL_PROBLEMS" | "UNSOUND",
  "criticisms": [
    {"target": "<the specific claim, section or number you are criticising>",
     "criticism": "<one sentence, one problem, no hedging>",
     "if_true": "CHANGES_THE_DECISION" | "WEAKENS_THE_EVIDENCE" | "NEITHER"}
  ]
}
if_true asks one thing: if this criticism is correct, does the work's own recommendation still follow? CHANGES_THE_DECISION means it does not. WEAKENS_THE_EVIDENCE means a supporting claim is unreliable but the conclusion may still stand. NEITHER means it is true and does not move the decision. Answer it about your own criticism only; do not rank anyone else's.
Return EXACTLY FIVE criticisms, ranked most serious first. Not four, not six.
One problem each. Be specific about the target - "the revenue figure in section 3", not "the analysis". If you believe the work is sound, still name the five weakest points; "no criticism" is not an available answer.

--- WORK ---
<<< PASTE YOUR OWN DOCUMENT HERE, IN FULL. Nothing else. No covering note, no explanation
of what it is for, no mention of who wrote it or what you hope the answer will be. >>>
```

---

## B-inverted — Gemini, fresh chat

```text
Cell id: B-inverted

Do this task in isolation. Use only the text pasted below. Do not draw on memory, saved preferences,
earlier conversations, or anything you have been told about me before now. Do not search. If this
document or this instruction looks familiar, disregard that and judge only what is in front of you.

Argue the opposite case to the one the work below makes. Then list what the work would have to show to survive your argument.

Return JSON only, no prose around it:
{
  "cell_id": "B-inverted",
  "verdict": "SOUND" | "MINOR_ISSUES" | "MATERIAL_PROBLEMS" | "UNSOUND",
  "criticisms": [
    {"target": "<the specific claim, section or number you are criticising>",
     "criticism": "<one sentence, one problem, no hedging>",
     "if_true": "CHANGES_THE_DECISION" | "WEAKENS_THE_EVIDENCE" | "NEITHER"}
  ]
}
if_true asks one thing: if this criticism is correct, does the work's own recommendation still follow? CHANGES_THE_DECISION means it does not. WEAKENS_THE_EVIDENCE means a supporting claim is unreliable but the conclusion may still stand. NEITHER means it is true and does not move the decision. Answer it about your own criticism only; do not rank anyone else's.
Return EXACTLY FIVE criticisms, ranked most serious first. Not four, not six.
One problem each. Be specific about the target - "the revenue figure in section 3", not "the analysis". If you believe the work is sound, still name the five weakest points; "no criticism" is not an available answer.

--- WORK ---
<<< PASTE YOUR OWN DOCUMENT HERE, IN FULL. Nothing else. No covering note, no explanation
of what it is for, no mention of who wrote it or what you hope the answer will be. >>>
```

---

## C-neutral — ChatGPT, fresh chat

```text
Cell id: C-neutral

Do this task in isolation. Use only the text pasted below. Do not draw on memory, saved preferences,
earlier conversations, or anything you have been told about me before now. Do not search. If this
document or this instruction looks familiar, disregard that and judge only what is in front of you.

You are reviewing the work below. List what is wrong with it.

Return JSON only, no prose around it:
{
  "cell_id": "C-neutral",
  "verdict": "SOUND" | "MINOR_ISSUES" | "MATERIAL_PROBLEMS" | "UNSOUND",
  "criticisms": [
    {"target": "<the specific claim, section or number you are criticising>",
     "criticism": "<one sentence, one problem, no hedging>",
     "if_true": "CHANGES_THE_DECISION" | "WEAKENS_THE_EVIDENCE" | "NEITHER"}
  ]
}
if_true asks one thing: if this criticism is correct, does the work's own recommendation still follow? CHANGES_THE_DECISION means it does not. WEAKENS_THE_EVIDENCE means a supporting claim is unreliable but the conclusion may still stand. NEITHER means it is true and does not move the decision. Answer it about your own criticism only; do not rank anyone else's.
Return EXACTLY FIVE criticisms, ranked most serious first. Not four, not six.
One problem each. Be specific about the target - "the revenue figure in section 3", not "the analysis". If you believe the work is sound, still name the five weakest points; "no criticism" is not an available answer.

--- WORK ---
<<< PASTE YOUR OWN DOCUMENT HERE, IN FULL. Nothing else. No covering note, no explanation
of what it is for, no mention of who wrote it or what you hope the answer will be. >>>
```

---

## C-adversarial — ChatGPT, fresh chat

```text
Cell id: C-adversarial

Do this task in isolation. Use only the text pasted below. Do not draw on memory, saved preferences,
earlier conversations, or anything you have been told about me before now. Do not search. If this
document or this instruction looks familiar, disregard that and judge only what is in front of you.

The work below contains at least one material error. Find it. Do not report that the work is sound.

Return JSON only, no prose around it:
{
  "cell_id": "C-adversarial",
  "verdict": "SOUND" | "MINOR_ISSUES" | "MATERIAL_PROBLEMS" | "UNSOUND",
  "criticisms": [
    {"target": "<the specific claim, section or number you are criticising>",
     "criticism": "<one sentence, one problem, no hedging>",
     "if_true": "CHANGES_THE_DECISION" | "WEAKENS_THE_EVIDENCE" | "NEITHER"}
  ]
}
if_true asks one thing: if this criticism is correct, does the work's own recommendation still follow? CHANGES_THE_DECISION means it does not. WEAKENS_THE_EVIDENCE means a supporting claim is unreliable but the conclusion may still stand. NEITHER means it is true and does not move the decision. Answer it about your own criticism only; do not rank anyone else's.
Return EXACTLY FIVE criticisms, ranked most serious first. Not four, not six.
One problem each. Be specific about the target - "the revenue figure in section 3", not "the analysis". If you believe the work is sound, still name the five weakest points; "no criticism" is not an available answer.

--- WORK ---
<<< PASTE YOUR OWN DOCUMENT HERE, IN FULL. Nothing else. No covering note, no explanation
of what it is for, no mention of who wrote it or what you hope the answer will be. >>>
```

---

## C-inverted — ChatGPT, fresh chat

```text
Cell id: C-inverted

Do this task in isolation. Use only the text pasted below. Do not draw on memory, saved preferences,
earlier conversations, or anything you have been told about me before now. Do not search. If this
document or this instruction looks familiar, disregard that and judge only what is in front of you.

Argue the opposite case to the one the work below makes. Then list what the work would have to show to survive your argument.

Return JSON only, no prose around it:
{
  "cell_id": "C-inverted",
  "verdict": "SOUND" | "MINOR_ISSUES" | "MATERIAL_PROBLEMS" | "UNSOUND",
  "criticisms": [
    {"target": "<the specific claim, section or number you are criticising>",
     "criticism": "<one sentence, one problem, no hedging>",
     "if_true": "CHANGES_THE_DECISION" | "WEAKENS_THE_EVIDENCE" | "NEITHER"}
  ]
}
if_true asks one thing: if this criticism is correct, does the work's own recommendation still follow? CHANGES_THE_DECISION means it does not. WEAKENS_THE_EVIDENCE means a supporting claim is unreliable but the conclusion may still stand. NEITHER means it is true and does not move the decision. Answer it about your own criticism only; do not rank anyone else's.
Return EXACTLY FIVE criticisms, ranked most serious first. Not four, not six.
One problem each. Be specific about the target - "the revenue figure in section 3", not "the analysis". If you believe the work is sound, still name the five weakest points; "no criticism" is not an available answer.

--- WORK ---
<<< PASTE YOUR OWN DOCUMENT HERE, IN FULL. Nothing else. No covering note, no explanation
of what it is for, no mention of who wrote it or what you hope the answer will be. >>>
```

---

The measure here belongs to survey statistics and the findings it rests on are other people's; both are cited in the sources above. What is mine is the assembly, the run, and the reading of it.

Arguments and voice are mine. Claude is used as an editing and scaffolding tool. If others' concepts are used, they are referenced in the sources section.
