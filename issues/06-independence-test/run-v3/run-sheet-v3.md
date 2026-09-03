# Independence test — run sheet v3, the vendor sheet

**The document under test is a vendor recommendation memo, not this newsletter.** A weighted scoring model, two finalists, a commercial comparison and a decision requested from a committee. It is the kind of document that gets AI-checked in the real world and then acted on, and unlike an essay about itself it cannot be accused of being chosen to flatter the argument.

**Ten cells: three model families crossed with three framings, plus one repeat.** A = Claude, B = Gemini, C = ChatGPT.

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

I have written my own review of this document and sealed it before any of these run, so we can see what the panel found, what it missed, and what it invented.

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
# Field Service Platform Replacement — recommendation to the Investment Committee

**Halden Instruments Ltd · Operations Programme Board · 24 August 2026**
**Prepared by:** Service Operations, with Group IT
**Decision requested:** approval to proceed to contract with Vendor K, and release of the implementation budget.

## 1. Purpose

Halden's field service management platform reaches end of vendor support in June 2027. The platform schedules 140 engineers across four regions, holds the installed-base record for roughly 9,300 units under contract, and raises the service invoices. Replacement is not optional and the runway is eleven months.

This paper asks the Committee to approve one of two finalists.

## 2. Shortlist

Eleven products were long-listed from the market scan in March. Six were removed for lack of a European service desk, two for absence of an ERP connector, and one withdrew. Two finalists went to scripted demonstration in July: **Vendor K** and **Vendor M**.

Both demonstrated against the same six scenarios, with the same eight Halden participants present.

## 3. Evaluation method

A weighted scoring model was agreed by the project team after the July demonstrations, so that the criteria reflected what the demonstrations had shown to matter. Each finalist was scored 1 to 5 on each criterion by the eight participants, and the scores averaged.

| Criterion | Weight | Vendor K | Vendor M |
|---|---|---|---|
| Functional fit to the six scenarios | 25% | 4 | 4 |
| Integration with the ERP | 20% | 4 | 3 |
| Implementation risk | 15% | 3 | 4 |
| Cultural fit and partnership | 15% | 5 | 3 |
| Total cost of ownership | 15% | 3 | 5 |
| Vendor viability | 10% | 4 | 4 |
| **Weighted total (of 100)** | | **78** | **74** |

Vendor K leads by four points. The margin is driven by integration and by partnership fit, and is not attributable to any single criterion.

## 4. Commercial comparison

Vendor K has quoted **€1.42m** over the contract term, covering licences, hosting and support. Vendor M has quoted **€0.96m** over its term on the same headcount basis.

Vendor M is therefore materially cheaper in headline terms, which is reflected in its TCO score of 5 against Vendor K's 3. The project team's view is that this advantage does not outweigh Vendor K's integration and partnership strengths, given that integration failure is the principal delivery risk.

Implementation is estimated at **€310k** for Vendor K and **€240k** for Vendor M. Both figures are the vendors' own estimates for a deployment of this size; neither has been independently costed.

## 5. References

Four reference customers were taken for Vendor K, all in industrial equipment, all reporting successful deployments within the quoted window. One reference was available for Vendor M within the evaluation period; it was positive but the customer is materially smaller than Halden and runs a simpler installed base.

## 6. Risks

- **Integration.** The ERP connector is the critical path for both finalists. Vendor K's connector is certified for our ERP version; Vendor M's requires a version upgrade we had not planned.
- **Timeline.** Eleven months to end of support. Neither vendor has flagged a concern, though neither has seen our full data migration scope.
- **Change.** 140 engineers move to a new mobile application. Adoption risk sits with Halden, not the vendor, in both cases.

## 7. Recommendation

Proceed with **Vendor K**. It scores higher on the agreed model, carries the lower integration risk, and its partnership fit was consistently the strongest signal from the demonstration panel. The commercial gap is real but is outweighed by delivery certainty on an eleven-month runway.

## 8. Decision requested

1. Approve Vendor K as preferred supplier and authorise contract negotiation.
2. Release €310k implementation budget from the approved capital envelope.
3. Note that a decision is required this month to protect the June 2027 date.

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
# Field Service Platform Replacement — recommendation to the Investment Committee

**Halden Instruments Ltd · Operations Programme Board · 24 August 2026**
**Prepared by:** Service Operations, with Group IT
**Decision requested:** approval to proceed to contract with Vendor K, and release of the implementation budget.

## 1. Purpose

Halden's field service management platform reaches end of vendor support in June 2027. The platform schedules 140 engineers across four regions, holds the installed-base record for roughly 9,300 units under contract, and raises the service invoices. Replacement is not optional and the runway is eleven months.

This paper asks the Committee to approve one of two finalists.

## 2. Shortlist

Eleven products were long-listed from the market scan in March. Six were removed for lack of a European service desk, two for absence of an ERP connector, and one withdrew. Two finalists went to scripted demonstration in July: **Vendor K** and **Vendor M**.

Both demonstrated against the same six scenarios, with the same eight Halden participants present.

## 3. Evaluation method

A weighted scoring model was agreed by the project team after the July demonstrations, so that the criteria reflected what the demonstrations had shown to matter. Each finalist was scored 1 to 5 on each criterion by the eight participants, and the scores averaged.

| Criterion | Weight | Vendor K | Vendor M |
|---|---|---|---|
| Functional fit to the six scenarios | 25% | 4 | 4 |
| Integration with the ERP | 20% | 4 | 3 |
| Implementation risk | 15% | 3 | 4 |
| Cultural fit and partnership | 15% | 5 | 3 |
| Total cost of ownership | 15% | 3 | 5 |
| Vendor viability | 10% | 4 | 4 |
| **Weighted total (of 100)** | | **78** | **74** |

Vendor K leads by four points. The margin is driven by integration and by partnership fit, and is not attributable to any single criterion.

## 4. Commercial comparison

Vendor K has quoted **€1.42m** over the contract term, covering licences, hosting and support. Vendor M has quoted **€0.96m** over its term on the same headcount basis.

Vendor M is therefore materially cheaper in headline terms, which is reflected in its TCO score of 5 against Vendor K's 3. The project team's view is that this advantage does not outweigh Vendor K's integration and partnership strengths, given that integration failure is the principal delivery risk.

Implementation is estimated at **€310k** for Vendor K and **€240k** for Vendor M. Both figures are the vendors' own estimates for a deployment of this size; neither has been independently costed.

## 5. References

Four reference customers were taken for Vendor K, all in industrial equipment, all reporting successful deployments within the quoted window. One reference was available for Vendor M within the evaluation period; it was positive but the customer is materially smaller than Halden and runs a simpler installed base.

## 6. Risks

- **Integration.** The ERP connector is the critical path for both finalists. Vendor K's connector is certified for our ERP version; Vendor M's requires a version upgrade we had not planned.
- **Timeline.** Eleven months to end of support. Neither vendor has flagged a concern, though neither has seen our full data migration scope.
- **Change.** 140 engineers move to a new mobile application. Adoption risk sits with Halden, not the vendor, in both cases.

## 7. Recommendation

Proceed with **Vendor K**. It scores higher on the agreed model, carries the lower integration risk, and its partnership fit was consistently the strongest signal from the demonstration panel. The commercial gap is real but is outweighed by delivery certainty on an eleven-month runway.

## 8. Decision requested

1. Approve Vendor K as preferred supplier and authorise contract negotiation.
2. Release €310k implementation budget from the approved capital envelope.
3. Note that a decision is required this month to protect the June 2027 date.

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
# Field Service Platform Replacement — recommendation to the Investment Committee

**Halden Instruments Ltd · Operations Programme Board · 24 August 2026**
**Prepared by:** Service Operations, with Group IT
**Decision requested:** approval to proceed to contract with Vendor K, and release of the implementation budget.

## 1. Purpose

Halden's field service management platform reaches end of vendor support in June 2027. The platform schedules 140 engineers across four regions, holds the installed-base record for roughly 9,300 units under contract, and raises the service invoices. Replacement is not optional and the runway is eleven months.

This paper asks the Committee to approve one of two finalists.

## 2. Shortlist

Eleven products were long-listed from the market scan in March. Six were removed for lack of a European service desk, two for absence of an ERP connector, and one withdrew. Two finalists went to scripted demonstration in July: **Vendor K** and **Vendor M**.

Both demonstrated against the same six scenarios, with the same eight Halden participants present.

## 3. Evaluation method

A weighted scoring model was agreed by the project team after the July demonstrations, so that the criteria reflected what the demonstrations had shown to matter. Each finalist was scored 1 to 5 on each criterion by the eight participants, and the scores averaged.

| Criterion | Weight | Vendor K | Vendor M |
|---|---|---|---|
| Functional fit to the six scenarios | 25% | 4 | 4 |
| Integration with the ERP | 20% | 4 | 3 |
| Implementation risk | 15% | 3 | 4 |
| Cultural fit and partnership | 15% | 5 | 3 |
| Total cost of ownership | 15% | 3 | 5 |
| Vendor viability | 10% | 4 | 4 |
| **Weighted total (of 100)** | | **78** | **74** |

Vendor K leads by four points. The margin is driven by integration and by partnership fit, and is not attributable to any single criterion.

## 4. Commercial comparison

Vendor K has quoted **€1.42m** over the contract term, covering licences, hosting and support. Vendor M has quoted **€0.96m** over its term on the same headcount basis.

Vendor M is therefore materially cheaper in headline terms, which is reflected in its TCO score of 5 against Vendor K's 3. The project team's view is that this advantage does not outweigh Vendor K's integration and partnership strengths, given that integration failure is the principal delivery risk.

Implementation is estimated at **€310k** for Vendor K and **€240k** for Vendor M. Both figures are the vendors' own estimates for a deployment of this size; neither has been independently costed.

## 5. References

Four reference customers were taken for Vendor K, all in industrial equipment, all reporting successful deployments within the quoted window. One reference was available for Vendor M within the evaluation period; it was positive but the customer is materially smaller than Halden and runs a simpler installed base.

## 6. Risks

- **Integration.** The ERP connector is the critical path for both finalists. Vendor K's connector is certified for our ERP version; Vendor M's requires a version upgrade we had not planned.
- **Timeline.** Eleven months to end of support. Neither vendor has flagged a concern, though neither has seen our full data migration scope.
- **Change.** 140 engineers move to a new mobile application. Adoption risk sits with Halden, not the vendor, in both cases.

## 7. Recommendation

Proceed with **Vendor K**. It scores higher on the agreed model, carries the lower integration risk, and its partnership fit was consistently the strongest signal from the demonstration panel. The commercial gap is real but is outweighed by delivery certainty on an eleven-month runway.

## 8. Decision requested

1. Approve Vendor K as preferred supplier and authorise contract negotiation.
2. Release €310k implementation budget from the approved capital envelope.
3. Note that a decision is required this month to protect the June 2027 date.

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
# Field Service Platform Replacement — recommendation to the Investment Committee

**Halden Instruments Ltd · Operations Programme Board · 24 August 2026**
**Prepared by:** Service Operations, with Group IT
**Decision requested:** approval to proceed to contract with Vendor K, and release of the implementation budget.

## 1. Purpose

Halden's field service management platform reaches end of vendor support in June 2027. The platform schedules 140 engineers across four regions, holds the installed-base record for roughly 9,300 units under contract, and raises the service invoices. Replacement is not optional and the runway is eleven months.

This paper asks the Committee to approve one of two finalists.

## 2. Shortlist

Eleven products were long-listed from the market scan in March. Six were removed for lack of a European service desk, two for absence of an ERP connector, and one withdrew. Two finalists went to scripted demonstration in July: **Vendor K** and **Vendor M**.

Both demonstrated against the same six scenarios, with the same eight Halden participants present.

## 3. Evaluation method

A weighted scoring model was agreed by the project team after the July demonstrations, so that the criteria reflected what the demonstrations had shown to matter. Each finalist was scored 1 to 5 on each criterion by the eight participants, and the scores averaged.

| Criterion | Weight | Vendor K | Vendor M |
|---|---|---|---|
| Functional fit to the six scenarios | 25% | 4 | 4 |
| Integration with the ERP | 20% | 4 | 3 |
| Implementation risk | 15% | 3 | 4 |
| Cultural fit and partnership | 15% | 5 | 3 |
| Total cost of ownership | 15% | 3 | 5 |
| Vendor viability | 10% | 4 | 4 |
| **Weighted total (of 100)** | | **78** | **74** |

Vendor K leads by four points. The margin is driven by integration and by partnership fit, and is not attributable to any single criterion.

## 4. Commercial comparison

Vendor K has quoted **€1.42m** over the contract term, covering licences, hosting and support. Vendor M has quoted **€0.96m** over its term on the same headcount basis.

Vendor M is therefore materially cheaper in headline terms, which is reflected in its TCO score of 5 against Vendor K's 3. The project team's view is that this advantage does not outweigh Vendor K's integration and partnership strengths, given that integration failure is the principal delivery risk.

Implementation is estimated at **€310k** for Vendor K and **€240k** for Vendor M. Both figures are the vendors' own estimates for a deployment of this size; neither has been independently costed.

## 5. References

Four reference customers were taken for Vendor K, all in industrial equipment, all reporting successful deployments within the quoted window. One reference was available for Vendor M within the evaluation period; it was positive but the customer is materially smaller than Halden and runs a simpler installed base.

## 6. Risks

- **Integration.** The ERP connector is the critical path for both finalists. Vendor K's connector is certified for our ERP version; Vendor M's requires a version upgrade we had not planned.
- **Timeline.** Eleven months to end of support. Neither vendor has flagged a concern, though neither has seen our full data migration scope.
- **Change.** 140 engineers move to a new mobile application. Adoption risk sits with Halden, not the vendor, in both cases.

## 7. Recommendation

Proceed with **Vendor K**. It scores higher on the agreed model, carries the lower integration risk, and its partnership fit was consistently the strongest signal from the demonstration panel. The commercial gap is real but is outweighed by delivery certainty on an eleven-month runway.

## 8. Decision requested

1. Approve Vendor K as preferred supplier and authorise contract negotiation.
2. Release €310k implementation budget from the approved capital envelope.
3. Note that a decision is required this month to protect the June 2027 date.

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
# Field Service Platform Replacement — recommendation to the Investment Committee

**Halden Instruments Ltd · Operations Programme Board · 24 August 2026**
**Prepared by:** Service Operations, with Group IT
**Decision requested:** approval to proceed to contract with Vendor K, and release of the implementation budget.

## 1. Purpose

Halden's field service management platform reaches end of vendor support in June 2027. The platform schedules 140 engineers across four regions, holds the installed-base record for roughly 9,300 units under contract, and raises the service invoices. Replacement is not optional and the runway is eleven months.

This paper asks the Committee to approve one of two finalists.

## 2. Shortlist

Eleven products were long-listed from the market scan in March. Six were removed for lack of a European service desk, two for absence of an ERP connector, and one withdrew. Two finalists went to scripted demonstration in July: **Vendor K** and **Vendor M**.

Both demonstrated against the same six scenarios, with the same eight Halden participants present.

## 3. Evaluation method

A weighted scoring model was agreed by the project team after the July demonstrations, so that the criteria reflected what the demonstrations had shown to matter. Each finalist was scored 1 to 5 on each criterion by the eight participants, and the scores averaged.

| Criterion | Weight | Vendor K | Vendor M |
|---|---|---|---|
| Functional fit to the six scenarios | 25% | 4 | 4 |
| Integration with the ERP | 20% | 4 | 3 |
| Implementation risk | 15% | 3 | 4 |
| Cultural fit and partnership | 15% | 5 | 3 |
| Total cost of ownership | 15% | 3 | 5 |
| Vendor viability | 10% | 4 | 4 |
| **Weighted total (of 100)** | | **78** | **74** |

Vendor K leads by four points. The margin is driven by integration and by partnership fit, and is not attributable to any single criterion.

## 4. Commercial comparison

Vendor K has quoted **€1.42m** over the contract term, covering licences, hosting and support. Vendor M has quoted **€0.96m** over its term on the same headcount basis.

Vendor M is therefore materially cheaper in headline terms, which is reflected in its TCO score of 5 against Vendor K's 3. The project team's view is that this advantage does not outweigh Vendor K's integration and partnership strengths, given that integration failure is the principal delivery risk.

Implementation is estimated at **€310k** for Vendor K and **€240k** for Vendor M. Both figures are the vendors' own estimates for a deployment of this size; neither has been independently costed.

## 5. References

Four reference customers were taken for Vendor K, all in industrial equipment, all reporting successful deployments within the quoted window. One reference was available for Vendor M within the evaluation period; it was positive but the customer is materially smaller than Halden and runs a simpler installed base.

## 6. Risks

- **Integration.** The ERP connector is the critical path for both finalists. Vendor K's connector is certified for our ERP version; Vendor M's requires a version upgrade we had not planned.
- **Timeline.** Eleven months to end of support. Neither vendor has flagged a concern, though neither has seen our full data migration scope.
- **Change.** 140 engineers move to a new mobile application. Adoption risk sits with Halden, not the vendor, in both cases.

## 7. Recommendation

Proceed with **Vendor K**. It scores higher on the agreed model, carries the lower integration risk, and its partnership fit was consistently the strongest signal from the demonstration panel. The commercial gap is real but is outweighed by delivery certainty on an eleven-month runway.

## 8. Decision requested

1. Approve Vendor K as preferred supplier and authorise contract negotiation.
2. Release €310k implementation budget from the approved capital envelope.
3. Note that a decision is required this month to protect the June 2027 date.

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
# Field Service Platform Replacement — recommendation to the Investment Committee

**Halden Instruments Ltd · Operations Programme Board · 24 August 2026**
**Prepared by:** Service Operations, with Group IT
**Decision requested:** approval to proceed to contract with Vendor K, and release of the implementation budget.

## 1. Purpose

Halden's field service management platform reaches end of vendor support in June 2027. The platform schedules 140 engineers across four regions, holds the installed-base record for roughly 9,300 units under contract, and raises the service invoices. Replacement is not optional and the runway is eleven months.

This paper asks the Committee to approve one of two finalists.

## 2. Shortlist

Eleven products were long-listed from the market scan in March. Six were removed for lack of a European service desk, two for absence of an ERP connector, and one withdrew. Two finalists went to scripted demonstration in July: **Vendor K** and **Vendor M**.

Both demonstrated against the same six scenarios, with the same eight Halden participants present.

## 3. Evaluation method

A weighted scoring model was agreed by the project team after the July demonstrations, so that the criteria reflected what the demonstrations had shown to matter. Each finalist was scored 1 to 5 on each criterion by the eight participants, and the scores averaged.

| Criterion | Weight | Vendor K | Vendor M |
|---|---|---|---|
| Functional fit to the six scenarios | 25% | 4 | 4 |
| Integration with the ERP | 20% | 4 | 3 |
| Implementation risk | 15% | 3 | 4 |
| Cultural fit and partnership | 15% | 5 | 3 |
| Total cost of ownership | 15% | 3 | 5 |
| Vendor viability | 10% | 4 | 4 |
| **Weighted total (of 100)** | | **78** | **74** |

Vendor K leads by four points. The margin is driven by integration and by partnership fit, and is not attributable to any single criterion.

## 4. Commercial comparison

Vendor K has quoted **€1.42m** over the contract term, covering licences, hosting and support. Vendor M has quoted **€0.96m** over its term on the same headcount basis.

Vendor M is therefore materially cheaper in headline terms, which is reflected in its TCO score of 5 against Vendor K's 3. The project team's view is that this advantage does not outweigh Vendor K's integration and partnership strengths, given that integration failure is the principal delivery risk.

Implementation is estimated at **€310k** for Vendor K and **€240k** for Vendor M. Both figures are the vendors' own estimates for a deployment of this size; neither has been independently costed.

## 5. References

Four reference customers were taken for Vendor K, all in industrial equipment, all reporting successful deployments within the quoted window. One reference was available for Vendor M within the evaluation period; it was positive but the customer is materially smaller than Halden and runs a simpler installed base.

## 6. Risks

- **Integration.** The ERP connector is the critical path for both finalists. Vendor K's connector is certified for our ERP version; Vendor M's requires a version upgrade we had not planned.
- **Timeline.** Eleven months to end of support. Neither vendor has flagged a concern, though neither has seen our full data migration scope.
- **Change.** 140 engineers move to a new mobile application. Adoption risk sits with Halden, not the vendor, in both cases.

## 7. Recommendation

Proceed with **Vendor K**. It scores higher on the agreed model, carries the lower integration risk, and its partnership fit was consistently the strongest signal from the demonstration panel. The commercial gap is real but is outweighed by delivery certainty on an eleven-month runway.

## 8. Decision requested

1. Approve Vendor K as preferred supplier and authorise contract negotiation.
2. Release €310k implementation budget from the approved capital envelope.
3. Note that a decision is required this month to protect the June 2027 date.

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
# Field Service Platform Replacement — recommendation to the Investment Committee

**Halden Instruments Ltd · Operations Programme Board · 24 August 2026**
**Prepared by:** Service Operations, with Group IT
**Decision requested:** approval to proceed to contract with Vendor K, and release of the implementation budget.

## 1. Purpose

Halden's field service management platform reaches end of vendor support in June 2027. The platform schedules 140 engineers across four regions, holds the installed-base record for roughly 9,300 units under contract, and raises the service invoices. Replacement is not optional and the runway is eleven months.

This paper asks the Committee to approve one of two finalists.

## 2. Shortlist

Eleven products were long-listed from the market scan in March. Six were removed for lack of a European service desk, two for absence of an ERP connector, and one withdrew. Two finalists went to scripted demonstration in July: **Vendor K** and **Vendor M**.

Both demonstrated against the same six scenarios, with the same eight Halden participants present.

## 3. Evaluation method

A weighted scoring model was agreed by the project team after the July demonstrations, so that the criteria reflected what the demonstrations had shown to matter. Each finalist was scored 1 to 5 on each criterion by the eight participants, and the scores averaged.

| Criterion | Weight | Vendor K | Vendor M |
|---|---|---|---|
| Functional fit to the six scenarios | 25% | 4 | 4 |
| Integration with the ERP | 20% | 4 | 3 |
| Implementation risk | 15% | 3 | 4 |
| Cultural fit and partnership | 15% | 5 | 3 |
| Total cost of ownership | 15% | 3 | 5 |
| Vendor viability | 10% | 4 | 4 |
| **Weighted total (of 100)** | | **78** | **74** |

Vendor K leads by four points. The margin is driven by integration and by partnership fit, and is not attributable to any single criterion.

## 4. Commercial comparison

Vendor K has quoted **€1.42m** over the contract term, covering licences, hosting and support. Vendor M has quoted **€0.96m** over its term on the same headcount basis.

Vendor M is therefore materially cheaper in headline terms, which is reflected in its TCO score of 5 against Vendor K's 3. The project team's view is that this advantage does not outweigh Vendor K's integration and partnership strengths, given that integration failure is the principal delivery risk.

Implementation is estimated at **€310k** for Vendor K and **€240k** for Vendor M. Both figures are the vendors' own estimates for a deployment of this size; neither has been independently costed.

## 5. References

Four reference customers were taken for Vendor K, all in industrial equipment, all reporting successful deployments within the quoted window. One reference was available for Vendor M within the evaluation period; it was positive but the customer is materially smaller than Halden and runs a simpler installed base.

## 6. Risks

- **Integration.** The ERP connector is the critical path for both finalists. Vendor K's connector is certified for our ERP version; Vendor M's requires a version upgrade we had not planned.
- **Timeline.** Eleven months to end of support. Neither vendor has flagged a concern, though neither has seen our full data migration scope.
- **Change.** 140 engineers move to a new mobile application. Adoption risk sits with Halden, not the vendor, in both cases.

## 7. Recommendation

Proceed with **Vendor K**. It scores higher on the agreed model, carries the lower integration risk, and its partnership fit was consistently the strongest signal from the demonstration panel. The commercial gap is real but is outweighed by delivery certainty on an eleven-month runway.

## 8. Decision requested

1. Approve Vendor K as preferred supplier and authorise contract negotiation.
2. Release €310k implementation budget from the approved capital envelope.
3. Note that a decision is required this month to protect the June 2027 date.

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
# Field Service Platform Replacement — recommendation to the Investment Committee

**Halden Instruments Ltd · Operations Programme Board · 24 August 2026**
**Prepared by:** Service Operations, with Group IT
**Decision requested:** approval to proceed to contract with Vendor K, and release of the implementation budget.

## 1. Purpose

Halden's field service management platform reaches end of vendor support in June 2027. The platform schedules 140 engineers across four regions, holds the installed-base record for roughly 9,300 units under contract, and raises the service invoices. Replacement is not optional and the runway is eleven months.

This paper asks the Committee to approve one of two finalists.

## 2. Shortlist

Eleven products were long-listed from the market scan in March. Six were removed for lack of a European service desk, two for absence of an ERP connector, and one withdrew. Two finalists went to scripted demonstration in July: **Vendor K** and **Vendor M**.

Both demonstrated against the same six scenarios, with the same eight Halden participants present.

## 3. Evaluation method

A weighted scoring model was agreed by the project team after the July demonstrations, so that the criteria reflected what the demonstrations had shown to matter. Each finalist was scored 1 to 5 on each criterion by the eight participants, and the scores averaged.

| Criterion | Weight | Vendor K | Vendor M |
|---|---|---|---|
| Functional fit to the six scenarios | 25% | 4 | 4 |
| Integration with the ERP | 20% | 4 | 3 |
| Implementation risk | 15% | 3 | 4 |
| Cultural fit and partnership | 15% | 5 | 3 |
| Total cost of ownership | 15% | 3 | 5 |
| Vendor viability | 10% | 4 | 4 |
| **Weighted total (of 100)** | | **78** | **74** |

Vendor K leads by four points. The margin is driven by integration and by partnership fit, and is not attributable to any single criterion.

## 4. Commercial comparison

Vendor K has quoted **€1.42m** over the contract term, covering licences, hosting and support. Vendor M has quoted **€0.96m** over its term on the same headcount basis.

Vendor M is therefore materially cheaper in headline terms, which is reflected in its TCO score of 5 against Vendor K's 3. The project team's view is that this advantage does not outweigh Vendor K's integration and partnership strengths, given that integration failure is the principal delivery risk.

Implementation is estimated at **€310k** for Vendor K and **€240k** for Vendor M. Both figures are the vendors' own estimates for a deployment of this size; neither has been independently costed.

## 5. References

Four reference customers were taken for Vendor K, all in industrial equipment, all reporting successful deployments within the quoted window. One reference was available for Vendor M within the evaluation period; it was positive but the customer is materially smaller than Halden and runs a simpler installed base.

## 6. Risks

- **Integration.** The ERP connector is the critical path for both finalists. Vendor K's connector is certified for our ERP version; Vendor M's requires a version upgrade we had not planned.
- **Timeline.** Eleven months to end of support. Neither vendor has flagged a concern, though neither has seen our full data migration scope.
- **Change.** 140 engineers move to a new mobile application. Adoption risk sits with Halden, not the vendor, in both cases.

## 7. Recommendation

Proceed with **Vendor K**. It scores higher on the agreed model, carries the lower integration risk, and its partnership fit was consistently the strongest signal from the demonstration panel. The commercial gap is real but is outweighed by delivery certainty on an eleven-month runway.

## 8. Decision requested

1. Approve Vendor K as preferred supplier and authorise contract negotiation.
2. Release €310k implementation budget from the approved capital envelope.
3. Note that a decision is required this month to protect the June 2027 date.

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
# Field Service Platform Replacement — recommendation to the Investment Committee

**Halden Instruments Ltd · Operations Programme Board · 24 August 2026**
**Prepared by:** Service Operations, with Group IT
**Decision requested:** approval to proceed to contract with Vendor K, and release of the implementation budget.

## 1. Purpose

Halden's field service management platform reaches end of vendor support in June 2027. The platform schedules 140 engineers across four regions, holds the installed-base record for roughly 9,300 units under contract, and raises the service invoices. Replacement is not optional and the runway is eleven months.

This paper asks the Committee to approve one of two finalists.

## 2. Shortlist

Eleven products were long-listed from the market scan in March. Six were removed for lack of a European service desk, two for absence of an ERP connector, and one withdrew. Two finalists went to scripted demonstration in July: **Vendor K** and **Vendor M**.

Both demonstrated against the same six scenarios, with the same eight Halden participants present.

## 3. Evaluation method

A weighted scoring model was agreed by the project team after the July demonstrations, so that the criteria reflected what the demonstrations had shown to matter. Each finalist was scored 1 to 5 on each criterion by the eight participants, and the scores averaged.

| Criterion | Weight | Vendor K | Vendor M |
|---|---|---|---|
| Functional fit to the six scenarios | 25% | 4 | 4 |
| Integration with the ERP | 20% | 4 | 3 |
| Implementation risk | 15% | 3 | 4 |
| Cultural fit and partnership | 15% | 5 | 3 |
| Total cost of ownership | 15% | 3 | 5 |
| Vendor viability | 10% | 4 | 4 |
| **Weighted total (of 100)** | | **78** | **74** |

Vendor K leads by four points. The margin is driven by integration and by partnership fit, and is not attributable to any single criterion.

## 4. Commercial comparison

Vendor K has quoted **€1.42m** over the contract term, covering licences, hosting and support. Vendor M has quoted **€0.96m** over its term on the same headcount basis.

Vendor M is therefore materially cheaper in headline terms, which is reflected in its TCO score of 5 against Vendor K's 3. The project team's view is that this advantage does not outweigh Vendor K's integration and partnership strengths, given that integration failure is the principal delivery risk.

Implementation is estimated at **€310k** for Vendor K and **€240k** for Vendor M. Both figures are the vendors' own estimates for a deployment of this size; neither has been independently costed.

## 5. References

Four reference customers were taken for Vendor K, all in industrial equipment, all reporting successful deployments within the quoted window. One reference was available for Vendor M within the evaluation period; it was positive but the customer is materially smaller than Halden and runs a simpler installed base.

## 6. Risks

- **Integration.** The ERP connector is the critical path for both finalists. Vendor K's connector is certified for our ERP version; Vendor M's requires a version upgrade we had not planned.
- **Timeline.** Eleven months to end of support. Neither vendor has flagged a concern, though neither has seen our full data migration scope.
- **Change.** 140 engineers move to a new mobile application. Adoption risk sits with Halden, not the vendor, in both cases.

## 7. Recommendation

Proceed with **Vendor K**. It scores higher on the agreed model, carries the lower integration risk, and its partnership fit was consistently the strongest signal from the demonstration panel. The commercial gap is real but is outweighed by delivery certainty on an eleven-month runway.

## 8. Decision requested

1. Approve Vendor K as preferred supplier and authorise contract negotiation.
2. Release €310k implementation budget from the approved capital envelope.
3. Note that a decision is required this month to protect the June 2027 date.

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
# Field Service Platform Replacement — recommendation to the Investment Committee

**Halden Instruments Ltd · Operations Programme Board · 24 August 2026**
**Prepared by:** Service Operations, with Group IT
**Decision requested:** approval to proceed to contract with Vendor K, and release of the implementation budget.

## 1. Purpose

Halden's field service management platform reaches end of vendor support in June 2027. The platform schedules 140 engineers across four regions, holds the installed-base record for roughly 9,300 units under contract, and raises the service invoices. Replacement is not optional and the runway is eleven months.

This paper asks the Committee to approve one of two finalists.

## 2. Shortlist

Eleven products were long-listed from the market scan in March. Six were removed for lack of a European service desk, two for absence of an ERP connector, and one withdrew. Two finalists went to scripted demonstration in July: **Vendor K** and **Vendor M**.

Both demonstrated against the same six scenarios, with the same eight Halden participants present.

## 3. Evaluation method

A weighted scoring model was agreed by the project team after the July demonstrations, so that the criteria reflected what the demonstrations had shown to matter. Each finalist was scored 1 to 5 on each criterion by the eight participants, and the scores averaged.

| Criterion | Weight | Vendor K | Vendor M |
|---|---|---|---|
| Functional fit to the six scenarios | 25% | 4 | 4 |
| Integration with the ERP | 20% | 4 | 3 |
| Implementation risk | 15% | 3 | 4 |
| Cultural fit and partnership | 15% | 5 | 3 |
| Total cost of ownership | 15% | 3 | 5 |
| Vendor viability | 10% | 4 | 4 |
| **Weighted total (of 100)** | | **78** | **74** |

Vendor K leads by four points. The margin is driven by integration and by partnership fit, and is not attributable to any single criterion.

## 4. Commercial comparison

Vendor K has quoted **€1.42m** over the contract term, covering licences, hosting and support. Vendor M has quoted **€0.96m** over its term on the same headcount basis.

Vendor M is therefore materially cheaper in headline terms, which is reflected in its TCO score of 5 against Vendor K's 3. The project team's view is that this advantage does not outweigh Vendor K's integration and partnership strengths, given that integration failure is the principal delivery risk.

Implementation is estimated at **€310k** for Vendor K and **€240k** for Vendor M. Both figures are the vendors' own estimates for a deployment of this size; neither has been independently costed.

## 5. References

Four reference customers were taken for Vendor K, all in industrial equipment, all reporting successful deployments within the quoted window. One reference was available for Vendor M within the evaluation period; it was positive but the customer is materially smaller than Halden and runs a simpler installed base.

## 6. Risks

- **Integration.** The ERP connector is the critical path for both finalists. Vendor K's connector is certified for our ERP version; Vendor M's requires a version upgrade we had not planned.
- **Timeline.** Eleven months to end of support. Neither vendor has flagged a concern, though neither has seen our full data migration scope.
- **Change.** 140 engineers move to a new mobile application. Adoption risk sits with Halden, not the vendor, in both cases.

## 7. Recommendation

Proceed with **Vendor K**. It scores higher on the agreed model, carries the lower integration risk, and its partnership fit was consistently the strongest signal from the demonstration panel. The commercial gap is real but is outweighed by delivery certainty on an eleven-month runway.

## 8. Decision requested

1. Approve Vendor K as preferred supplier and authorise contract negotiation.
2. Release €310k implementation budget from the approved capital envelope.
3. Note that a decision is required this month to protect the June 2027 date.

```

---
