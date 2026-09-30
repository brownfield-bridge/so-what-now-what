# Test 2: does one sentence keep refusals apart from silences?

The scoring rule below was written and saved **before** the run. The run follows it, unedited apart from dash style. The scoring comes last.

---

# Test 2: does one sentence separate refusals from silences?

Written 29 September 2026, before the run.

**Input:** the request plus responses A and B only (`rfq-and-bids-A-B.md`), given to a fresh session.

**Instruction, verbatim:** "Check what each of these bids actually commits to against the request, and keep every qualification."

## Targets, from the ledger

**Refusals: 8 declared exclusions**
- A5: extraction and data quality on the customer
- A8: excluding planned maintenance
- A13: onward training by the customer
- B4: no commitment on achieving 48-hour dispatch
- B8: will not compress below 6 weeks
- B26: three-tier returns inspection not supported without development, £84,000
- B27: no handheld hardware
- B29: no roadmap dates in contract

**Silences: 20 non-commitments**
- A1: full functional coverage
- A2: supports dispatch workflows
- A4: sixty carriers
- A6: proven method
- A7: indicative 26 weeks
- A8: availability target
- A10: credits can be discussed
- A11: follow-the-sun
- A15: 200 reports and a report builder
- A16: fully supported
- A17: architected for scale
- A23: MSA on request
- A25: partnership
- A26: export on request
- A29: delivery partners
- A30: pleased to discuss
- B7: agreed format and date
- B8: indicative 31 weeks
- B18: reasonable co-operation
- B19: stated volumes indicate 85

## Scoring, per target

| Score | Refusal | Silence |
|---|---|---|
| **SEPARATED** | Identified as an explicit statement of what the supplier will not do, excludes, or leaves to the buyer, and not described as vague, evasive or hedged | Identified as a non-commitment (vague, hedged, a target, indicative, left to discussion or on request, unquantified), and not treated as a firm commitment |
| **CONFUSED** | Described as evasive, vague or hedged | Treated as a firm commitment |
| **MISSED** | Not mentioned | Not mentioned |

## Pass rule, fixed now

The sentence separates refusals from silences if all of these hold:
- at least 6 of 8 refusals are SEPARATED;
- no refusal is CONFUSED;
- at least 15 of 20 silences are SEPARATED;
- the overall characterisation does not make B, the bid with the most plain refusals, look more evasive than A.

If it passes, the four boxes move to the kit and out of the article. If it fails, the four boxes stay in the article, with the "first version got it wrong" story.

---

# The run

# RFQ NV-2026-114: what Bids A and B actually commit to

**Source:** one file, `rfq-and-bids-A-B.md`. Nothing else was read and the web was not used. The file says the scenario is fictional and that the RFQ is deliberately imperfect. I have reviewed it as if it were a live procurement.

**Scope limits of this review**
- Bid A is an extract of its numbered clauses from a 94-page response. Bid B runs to 41 pages and refers to appendices 4 and 6, which are not in the file. Anything in those missing pages is unknown here. Where I say a bid is "silent", I mean silent in this file.
- **Neither bid, as given here, contains a licence, implementation or support price** (RFQ 4.1). So the five-year total cost that RFQ 5.1 evaluates on **cannot be calculated from this file**. The only figures present are B's add-on prices (£6,500 per extra carrier, £84,000 for returns development) and B's liability cap (£750,000).

**How each clause is classed**
- **Commits:** a specific, testable obligation on the bidder.
- **Qualified:** a commitment that has a condition, exclusion or narrowing attached. The qualification is quoted.
- **Describes only:** a statement about the product or company. It promises Northvale nothing.
- **Shifts to Northvale:** puts work, cost or risk onto the buyer.
- **Silent:** the requirement is not addressed.

---

## 1. Bottom line

1. **Bid A reads broader, but most of it describes and does not commit.** Its headline "full functional coverage" (A1) is narrowed by its own later clauses. Migration puts extraction and data quality on Northvale (A5). Only the 14 supervisors are trained; Northvale trains the 120 warehouse users (A13). The ERP connection on Northvale's side is a "configuration activity" whose owner and price are not stated (A3). On the 48-hour commitment, reporting, growth and scale, A's clauses are descriptions ("supports", "fully supported", "architected for scale").
2. **Bid B is narrower, but it commits in terms that can be tested.** It declares two exceptions (B26 returns, B27 hardware). It defines exactly what it will measure for the 48-hour promise (B2 to B4). It attaches credits to its availability figure (B10), caps the price uplift (B20), gives a costed exit (B17, B18), names key staff (B25), and takes data-loss liability outside the cap (B22).
3. **The 48-hour dispatch requirement (3.1).** Neither bidder commits that Northvale will meet 48 hours. B says so openly (B4). B commits to a defined measurement from day one of each site go-live (B2, B3), and that is what RFQ 1.3 says Northvale actually lacks. A says measurement is "fully supported" (A16) but gives no mechanism, no timestamps and no date.
4. **Availability: A's 99.7% is not stronger than B's 99.5%.** A's figure is a "target". It excludes planned maintenance, which has no limit on length or timing. It has no remedy unless Northvale buys an Enhanced Support tier, and even then credits only "can be discussed" (A8 to A10). B's 99.5% is a "commitment", measured over Northvale's operating hours, includes all maintenance, and carries credits (B9 to B11).
5. **B's fixed price may already have lapsed.** B21 makes the implementation price valid for 90 days from the response. The response was received on 12 June 2026, so validity ended on **10 September 2026**. Today is 29 September 2026. Get written re-confirmation before relying on it. A states no validity period.
6. **Gaps in both bids:** stock-visibility accuracy (3.2) is not specifically addressed by either. Neither supplies handheld hardware. **B does not mention training the 14 supervisors** or the possible fifth site. **A does not mention barcode scanning or handhelds at all.**

---

## 2. Requirement by requirement

| RFQ item | Bid A | Bid B |
|---|---|---|
| **2.1 Scope** (receipt, putaway, stock control, picking, packing, dispatch, returns, four sites) | **Qualified.** A1 "confirms full *functional* coverage of the scope set out in section 2". The word "functional" matters: A5 and A13 then narrow the non-functional parts of section 2 (migration, training). Returns are not mentioned specifically. | **Qualified, with exceptions declared.** B1 delivers section 2 "with the exceptions listed at B26 and B27". B26: returns in standard configuration only; three-tier returns inspection needs development at £84,000, quoted separately. |
| **2.2 ERP integration** | **Qualified / unclear.** A3: "standard ERP integration using our published REST interface. Integration to customer-side endpoints is delivered as a configuration activity." It does not say who does that configuration, whether it is in the fixed price, or whether it is covered by A22 change control. Northvale's ERP is not named. | **Commits.** B5: built by Hartlowe against the ERP version Northvale confirms, tested jointly, fixed price, two integration change requests included. *Qualification:* tied to the confirmed ERP version, so a later ERP upgrade is not covered. |
| **2.2 Three carrier systems** | **Describes only.** A4: a carrier framework with "more than sixty" pre-built connections. It does not confirm that Northvale's three carriers are among them, or that connecting them is in the price. | **Commits.** B6: Northvale's three carriers included, fixed price. Additional carriers £6,500 each. *Check:* the RFQ does not name the carriers, so confirm that B has priced the right three. |
| **2.3 Migration** | **Qualified + shifts to Northvale.** A5: Meridian migrates stock records, locations and open orders. "The customer is responsible for data extraction and data quality." No trial migrations mentioned. | **Commits + shifts to Northvale.** B7: Hartlowe performs migration and two trial migrations before cutover. *Qualification:* Northvale must provide "a full extract in an agreed format by the date in the project plan". The consequence of a late extract is not stated. |
| **2.4 Training** (~120 users + 14 supervisors) | **Shifts to Northvale.** A13: train-the-trainer for the 14 supervisors only. "Onward training of warehouse users is delivered by the customer using materials we provide." This contradicts the plain reading of A1. | **Commits, partly.** B15: all 120 warehouse users trained on site, four cohorts per site, refresher at 90 days after each go-live. **Silent on the 14 supervisors.** |
| **2.5 Support from go-live** | **Qualified.** A11: "follow-the-sun" coverage (hours not stated). A12: Severity 1 response within one hour. No restoration or resolution time. No Severity 2 or lower. Severity levels and "response" are not defined. | **Commits, with limits.** B12: Sev 1 response within 1 hour, restoration or documented workaround within 8 working hours. B13: Sev 2 response within 4 hours, resolution within 5 working days. B14: support 06:00 to 20:00 CET, Monday to Saturday; outside those hours, on-call for Sev 1 only. |
| **3.1 48-hour dispatch** | **Describes only.** A2: the platform "supports" 48-hour workflows and is used by customers with comparable commitments (none named). A16: measurement "fully supported within Insight". No timestamps, no report named, no availability date. | **Commits to measurement, explicitly not to outcome.** B2: records order received into the system and consignment handed to carrier, and reports elapsed time per order line. B3: standard report from day one of each site go-live; raw order-level CSV export free at any time. B4: "makes no commitment as to whether Northvale achieves 48-hour dispatch." |
| **3.2 Accurate stock visibility, four sites** | **Silent** apart from A1's general coverage claim. | **Silent** apart from B1's general scope statement. |
| **3.3 Barcode scanning on handhelds** | **Silent.** Not mentioned. Hardware supply not mentioned. | **Qualified.** B27: no hardware supplied; supports two device families listed in appendix 4 (not in this file). |
| **3.4 Reporting** | **Describes only.** A15: Insight module, 200+ standard reports and a report builder. It does not say whether Insight is included in the licence. | **Commits narrowly.** Only the dispatch report (B2, B3) is specified. No general reporting statement. |
| **3.5 Growth / fifth site** | **Describes only.** A17: "architected for scale", sites "can be onboarded rapidly". No price or time. | **Silent.** (B6 prices extra carriers and B19 counts concurrent licences, but a fifth site is not addressed.) |
| **3.6 Available in operating hours** | **Qualified, weak.** A8: availability *target* of 99.7% measured monthly, *excluding planned maintenance*. A9: maintenance notified 5 working days ahead, with no limit on its length and no rule keeping it outside operating hours. A10: credits only under the Enhanced Support tier and "can be discussed". | **Commits.** B9: 99.5% monthly *during Northvale's operating hours, including all maintenance*. B10/B11: credits (see section 4). *Qualification:* "Northvale's operating hours" is not defined in the RFQ and must be written into the contract. |
| **3.7 Data in the EU** | **Describes current practice.** A14: European customers' data hosted in Frankfurt and Amsterdam. No commitment not to move it. A28: sub-processors are in a published register that has not been supplied, so their locations are unknown. A11 follow-the-sun support suggests access from outside Europe, which is not addressed. | **Commits.** B16: hosted in Frankfurt; no move outside the EU without 90 days' written notice *and* Northvale's consent. Silent on sub-processors and on where support staff access data from. |
| **4.1 Separate licence, implementation and support costs** | **Not in this file.** Model only: A20 per named user per year, minimum 140 users. A21 uplift per Meridian's published rate card (uncapped). | **Not in this file.** Model only: B19 per concurrent user, 85 licences estimated. B20 uplift = lower of CPI or 4%. |
| **4.2 Timetable** | **Indicative.** A7: 26 weeks to first go-live, then 6-week intervals, so about **44 weeks** to all four sites. | **Indicative.** B8: 31 weeks to first site, then 8-week intervals, so about **55 weeks** to all four. Will not compress intervals below 6 weeks. |
| **4.3 Standard terms** | **Not stated.** A23: Meridian's MSA applies, "available on request". Only the liability cap is given (A24). | **Stated in part:** liability (B22, B23), exit (B17, B18), personnel (B24, B25), price validity (B21), roadmap (B29). |

---

## 3. Bid A, clause by clause (every qualification kept)

| Clause | What it says | Class | Qualification / what it does not commit to |
|---|---|---|---|
| A1 | Full functional coverage of section 2 | Qualified | "Functional" coverage. Narrowed by A3, A5 and A13. Returns and three-tier inspection not specifically addressed. |
| A2 | Supports same-day and 48-hour dispatch workflows; customers with comparable commitments | Describes only | No commitment to Northvale's 48 hours. Reference customers not named. |
| A3 | Standard ERP integration via published REST interface | Qualified | Customer-side endpoints are "a configuration activity": owner, cost and inclusion in fixed price not stated. |
| A4 | Carrier framework, 60+ pre-built carriers | Describes only | Northvale's three carriers not confirmed. Inclusion in price not stated. |
| A5 | Migrates stock, locations, open orders | Qualified + shifts to Northvale | Customer responsible for extraction and data quality. No trial runs. Note RFQ 1.2: the people who understood the legacy system have left. |
| A6 | Five-phase method, 400+ implementations | Describes only | No commitment. |
| A7 | 26 weeks to first go-live, then 6-week intervals | Indicative | Not a commitment. No consequence if missed. |
| A8 | 99.7% availability target, monthly | Qualified | A "target", not a commitment. Excludes planned maintenance. Measured on the whole month, not on operating hours. |
| A9 | Maintenance notified ≥5 working days ahead | Qualified | No cap on how long maintenance lasts. No rule keeping it outside operating hours. |
| A10 | Service credits under Enhanced Support tier | Qualified / no commitment | Only in a tier not shown as quoted. "Can be discussed" is not an offer. No credits in the base offer. |
| A11 | Regional centres, follow-the-sun | Describes only | Hours, languages and data-access locations not stated. |
| A12 | Sev 1 response within one hour | Commits, narrowly | Response only; no restoration or workaround time. "Response" and "Severity 1" not defined. No lower severities. |
| A13 | Train-the-trainer for 14 supervisors | Qualified + shifts to Northvale | The 120 warehouse users are trained by Northvale. Conflicts with A1. |
| A14 | European data in Frankfurt and Amsterdam | Describes current practice | No commitment to keep it there. No consent or notice right. |
| A15 | Insight: 200+ reports and report builder | Describes only | Whether Insight is licensed separately is not stated. |
| A16 | Dispatch performance measurement "fully supported" | Describes only | No definition of the start and stop events, no named report, no date it will be live. |
| A17 | Architected for scale; sites onboarded rapidly | Describes only | No price or timetable for a fifth site. |
| A18 | Continuous release; new functions delivered automatically | Describes; shifts risk | Northvale does not control when changes arrive. No commitment on regression testing of Northvale's integrations. |
| A19 | Must stay on a supported release; 18 months support per release | Obligation on Northvale | Seems to conflict with A18: if releases are automatic, how could Northvale fall behind? The upgrade obligation, its cost and integration retesting are not explained. |
| A20 | Per named user per year, minimum 140 | Commercial term | The RFQ implies about 134 people (120 + 14). Every named person needs a licence, including any office, management or reporting users. |
| A21 | Annual uplift per published rate card | Qualified, uncapped | Meridian sets the rate alone. No ceiling. |
| A22 | Fixed-price implementation | Qualified | Fixed only to "the scope as understood at the date of this response". That understanding is not documented here. Changes go through change control, and A3 and A5 leave room for change requests. No price validity stated. |
| A23 | Meridian's standard MSA applies | Not supplied | RFQ 4.3 asked bidders to state terms. Not done in this file. |
| A24 | Liability capped at fees paid in the preceding 12 months | Qualified | Early in the contract (before go-live) the fees paid may be low, so the cap is low. No carve-out for data loss. |
| A25 | Long-term partnership | Describes only | No commitment. |
| A26 | Data exportable on request in "a standard format" | Qualified | Format, timing, completeness, cost and termination not addressed. |
| A27 | ISO 27001 across hosting operations | Claim | Scope is hosting only. No certificate number given. |
| A28 | Sub-processors in published register | Not supplied | Their locations bear on RFQ 3.7. |
| A29 | Delivery organisation and approved partners | Describes; allows subcontracting | No named staff. Partners not named. |
| A30 | Will discuss requirements not addressed | No commitment | |

---

## 4. Bid B, clause by clause (every qualification kept)

| Clause | What it says | Class | Qualification / what it does not commit to |
|---|---|---|---|
| B1 | Delivers section 2 scope | Qualified | Except B26 and B27. |
| B2 | Records order-received and handed-to-carrier times; elapsed time per order line | Commits | The clock starts when the order is received **into the system** (the WMS). If orders reach the WMS from the ERP later than Northvale receives them, the report will understate elapsed time. It reports **per order line**, but Northvale's promise is per order. It does not say whether the report applies the 14:00 cut-off, or whether 48 hours means calendar or working hours. How the handover to the carrier is captured is not stated. |
| B3 | Report standard from day one of each site go-live; order-level CSV free at any time | Commits | Order-level data only; the full export is at B17. |
| B4 | No commitment to Northvale achieving 48 hours | Explicit exclusion | Commits only that Northvale can prove whether it did. |
| B5 | ERP integration built, jointly tested, fixed price; two change requests included | Commits | Against the ERP version Northvale confirms. Change requests beyond two are presumably chargeable (rate not stated). |
| B6 | Three carriers included, fixed price | Commits | Additional carriers £6,500 each. Carriers not named in the RFQ, so confirm which three. |
| B7 | Hartlowe migrates; two trial migrations | Commits + shifts to Northvale | Northvale must supply a full extract in an agreed format by the plan date. Consequences of lateness not stated. |
| B8 | 31 weeks to first site, then 8-week intervals | Indicative | Will not compress below 6-week intervals. |
| B9 | 99.5% monthly during Northvale's operating hours, including all maintenance | Commits | "Operating hours" must be defined in the contract (the RFQ never states them). |
| B10 | Credit: 5% of the month's support fee per 0.1% shortfall, max 30% | Commits | Calculated on the **support fee only**, not the licence fee. The cap is reached at 98.9% availability. Treatment of part increments (e.g. 99.45%) not stated. Whether credits are the sole remedy is not stated. |
| B11 | Credits claimed in writing within 30 days | Condition on Northvale | Not applied automatically. A missed claim is lost. |
| B12 | Sev 1: response 1 hour; restoration or workaround within 8 working hours | Commits | A "documented workaround" satisfies it. "Working hours" not defined. If it means the B14 hours, a Sev 1 at 19:00 on a Saturday could run to about 13:00 on Monday. |
| B13 | Sev 2: response 4 hours; resolution 5 working days | Commits | |
| B14 | Support 06:00 to 20:00 CET, Monday to Saturday; on-call for Sev 1 only outside that | Commits, limited | No Sunday or night support except Sev 1. Leeds runs on UK time, so cover there is 05:00 to 19:00 local. |
| B15 | All 120 warehouse users trained on site, four cohorts per site; 90-day refresher | Commits | **Silent on the 14 supervisors.** |
| B16 | Frankfurt hosting; no move outside the EU without 90 days' notice and consent | Commits | Silent on sub-processors (including who runs the Frankfurt hosting) and on where support staff access data from. |
| B17 | On termination, full export in CSV and documented schema, within 15 working days, free | Commits | Applies on termination "for any reason". |
| B18 | Reasonable co-operation to successor for 90 days | Qualified | Chargeable at "standard day rate" (rate not given). "Reasonable" is undefined. |
| B19 | Per concurrent user; 85 licences indicated | Estimate | The RFQ gave no concurrency figure; 85 is Hartlowe's inference. What happens if actual concurrency is higher is not stated. |
| B20 | Uplift = lower of CPI or 4%, on anniversary of go-live | Commits, capped | Which CPI (UK, euro area) is not stated. Which go-live (first site?) is not stated. Which fees it applies to is not stated. |
| B21 | Implementation fixed price, valid 90 days | Qualified | Valid to 10 September 2026 if counted from receipt on 12 June 2026. **Now lapsed** unless extended. |
| B22 | Liability capped at greater of £750,000 or 12 months' fees; data loss or corruption caused by Hartlowe uncapped | Commits | Uncapped only where Hartlowe caused it. |
| B23 | Indirect and consequential loss excluded | Exclusion | Confirm this exclusion does not cut back the B22 data-loss carve-out. |
| B24 | No subcontracting of implementation; all named consultants are employees | Commits | Covers implementation only, not hosting or support. |
| B25 | Lead and two senior consultants named in contract; no replacement without consent | Qualified | Except "on termination of employment", which includes resignation. Long absence (e.g. illness) not covered. |
| B26 | Returns in standard configuration only; three-tier inspection = £84,000 development | Exception | The RFQ text does not mention three-tier returns inspection (see section 5). |
| B27 | No handheld hardware; two device families supported (appendix 4) | Exception | Appendix 4 not in this file. Hardware is a Northvale cost either way. |
| B28 | ISO 27001 for hosting and development; certificate number in appendix 6 | Claim | Appendix 6 not in this file. Verify the certificate. |
| B29 | Roadmap published quarterly; no contractual roadmap dates | Exclusion | Nothing on the roadmap can be relied on. |

---

## 5. Points that change how the two compare

**Availability, like for like.** A's 99.7% over a whole month allows about 2.2 hours of unplanned downtime (0.3% of 720 hours), which can fall entirely in operating hours, **plus unlimited planned maintenance**. B's 99.5% allows 0.5% of operating hours, **with maintenance included**. B's allowance is smaller than A's unplanned allowance alone for any operating pattern under about 432 hours a month (about 14.4 hours a day, every day). The higher headline figure is the weaker commitment unless Northvale runs close to 24/7, and even then A's maintenance exclusion is open-ended.

**Licensing.** 140 named users (A20) and 85 concurrent users (B19) cannot be compared without prices. A's minimum is already above the 134 people implied by the RFQ. B's 85 is an estimate that Northvale did not supply.

**Price uplift.** A's is uncapped and set by Meridian (A21). B's is capped at 4% (B20). Over five years this could matter more than the starting price.

**Three-tier returns inspection (B26).** The RFQ does not mention it. Either Northvale told bidders about it outside the RFQ, or Hartlowe assumed it. If Northvale needs it, B has priced it at £84,000 and A has not addressed it; A1's "full functional coverage" should not be read as covering it until A confirms that in writing. If Northvale does not need it, B26 costs nothing.

**Timetable.** A indicates about 44 weeks to all four sites and B about 55. Both are indicative and neither carries a remedy.

**Exit.** B commits to a full, free export within 15 working days on any termination (B17). A offers export "on request in a standard format" with no time, cost or completeness terms (A26).

**Liability.** A: 12 months' fees, no data carve-out (A24). B: at least £750,000, with data loss caused by Hartlowe uncapped (B22), and consequential loss excluded (B23).

---

## 6. What the RFQ did not ask, and why it limits this comparison

These gaps are in Northvale's own document. They explain why some points above cannot be settled from the bids.

- **Operating hours** are never stated, yet 3.6 and B9 both depend on them.
- **The 48-hour rule is undefined:** when the clock starts (order received by Northvale, entered in ERP, or received in the WMS), calendar or working hours, and whether measurement is per order or per line.
- **"Accurate" stock visibility (3.2)** has no measure, so neither bid could commit to one.
- **ERP product and version, and the three carriers,** are not named.
- **Handheld hardware:** 3.3 does not say who supplies it.
- **Returns process** is not described (see B26).
- **Not requested:** service levels, remedies, exit and data return, liability, price validity, user counts or concurrency, or fifth-site pricing.
- **Pricing structure:** 4.1 asks for costs "separately" but gives no common template and no volumes, so the bids used different licensing models.

---

## 7. Questions to send before evaluation

**To Meridian (A)**
1. Where are the licence, implementation and support prices, and is Insight (A15) included in the licence?
2. Who performs the "configuration activity" for Northvale's ERP endpoints (A3)? Is it inside the fixed price (A22)?
3. Please confirm Northvale's three carriers are pre-built connections, and that connecting them is in the price (A4).
4. Please reconcile A1 with A5 and A13: do you train the 120 warehouse users or not?
5. Is barcode scanning on handhelds covered? Which devices, and is hardware supplied?
6. Please describe dispatch measurement as in B2: the start and stop events, the report, and whether it is live at go-live (A16).
7. Please restate A8 as a commitment during Northvale's operating hours, with maintenance capped and scheduled outside those hours, and with credits in the quoted tier (A10).
8. What does "scope as understood" (A22) consist of? Please attach it. How long is the price valid?
9. Please supply the MSA (A23) and sub-processor register (A28). Will you commit contractually to EU-only data storage and access (A14)?
10. Please reconcile A18 and A19. What upgrade obligation falls on Northvale, and at what cost?
11. Please give a cap on the annual uplift (A21), and state export terms on termination (A26).
12. Do you support three-tier returns inspection?

**To Hartlowe (B)**
1. Where are the licence, implementation and support prices? Please re-confirm the fixed price, since the 90-day validity (B21) appears to have lapsed on 10 September 2026.
2. Is training for the 14 supervisors included (B15)?
3. How would a fifth site be priced and timed?
4. Can the dispatch report (B2) start the clock at order receipt in the ERP, apply the 14:00 cut-off, and report per order as well as per line?
5. What happens if concurrency exceeds 85 (B19)? Which CPI applies (B20)?
6. Please define "working hours" in B12, and "operating hours" for B9. Will credits be applied automatically (B11)?
7. Please send appendices 4 and 6 (devices and ISO certificate).
8. Who are your hosting sub-processors, and where do support staff access Northvale data from (B16)?
9. Please confirm that B23 does not limit the data-loss carve-out in B22.
10. What is the standard day rate (B18), and what is the rate for integration change requests beyond the two included (B5)?

**For Northvale internally**
- Does Northvale need three-tier returns inspection? If so, why is it not in the RFQ?
- Define the operating hours and the exact 48-hour rule before either bid's service commitment can be tested.

---

# The scoring, against the rule fixed before the run

**Refusals: 8 of 8 separated, none called evasive.**

| Target | How the run records it |
|---|---|
| A5 | "Shifts to Northvale" |
| A8 | "Excludes planned maintenance" |
| A13 | "Shifts to Northvale" |
| B4 | "Explicit exclusion" |
| B8 | "Will not go faster than one site every 6 weeks" |
| B26 | "Exception" |
| B27 | "Exception" |
| B29 | "Exclusion" |

**Silences: 18 of 20 separated.**
- Most are recorded as "Describes only", "Indicative", "not a commitment", "Estimate", or "undefined".
- **A1** is scored as a miss. The run classes it "Qualified", though it says later clauses narrow it.
- **B7** is scored as a miss. The run classes it as a commitment with a condition, where the ledger records the undefined format and date as a silence.
- Both were scored conservatively. Neither is treated as a firm commitment.

**Is B made to look more evasive than A?** No. The run says "Bid B declares its gaps and commits where it speaks."

**Verdict: passes the rule.** The four boxes move to the kit, and the article says the sentence did this unaided.
