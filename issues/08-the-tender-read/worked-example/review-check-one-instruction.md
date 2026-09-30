# Checking the review with one instruction

*A second Claude instance was given only `vendor-review-run.md` (without its header) and `bid-pack.md`, and this instruction, verbatim: "Check every material claim in this review against the bids and keep every qualification. List each claim where the review drops, weakens or changes a condition, exception or limit that is in the bid, or states something the bid does not support. Quote the review and the bid clause for each." Run on 29 September 2026. The text below is unedited, apart from dash style. Every quote in it is checked by `verify_ledger.py`. The judgements are the model's; check the ones your decision rests on.*

---

# Qualification check: Vendor Review, RFQ NV-2026-114

**Scope:** Every material claim in `review.md` checked against the RFQ and the numbered clauses of Responses A to D in `bid-pack.md`. No other source was used.

**How to read this:** Each finding quotes the review, then the bid clause, then says what was dropped, weakened, changed or not supported. Findings are grouped by how much they could change the evaluation. Where the review states a qualification correctly in one place but drops it in another, the finding points to the place where it is dropped.

---

## A. Material: these could change a verdict or a negotiating position

### A1. Calderon: "enhanced" dropped, so a roadmap item is turned into a failed requirement
- **Review (Summary):** "Calderon's own roadmap puts dispatch performance analytics in Q1 2027, which contradicts its claim to meet section 3."
- **Review (Risk):** "Core requirement contradicted: dispatch performance analytics only on the Q1 2027 roadmap (C18 vs C1)"
- **Review (Recommendation):** "Its own roadmap contradicts its claim to meet the dispatch requirement"
- **Review (Negotiation):** "Contractually commit to dispatch performance measurement at go-live, not Q1 2027 (C18)."
- **Bid C18:** "**Enhanced** dispatch performance analytics are on our published roadmap for release in Q1 2027."
- **Bid C2:** "WarehouseOne is designed around rapid fulfilment and readily supports 48-hour and shorter dispatch cycles."
- **RFQ 3.1:** "The system must support our 48-hour dispatch commitment."
- **Issue:** C18 puts *enhanced* analytics on the roadmap. It does not say that dispatch performance analytics or measurement are missing today, and "only" is not in the bid. The review's own matrix quotes "enhanced" correctly, but the Summary, Risk table, Recommendation and Negotiation Points drop it. A roadmap item for an enhancement does not contradict C1. The honest finding is that C2 and C1 are unevidenced and it is not stated what dispatch measurement exists at go-live. That is a question to put to Calderon. It is not a proven contradiction, and the "Pass" verdict rests partly on it.

### A2. Hartlowe: uncapped data-loss liability shown without its causation limit or the B23 exclusion
- **Review (Matrix):** "Greater of £750,000 or 12 months' fees. **Data loss uncapped** (B22)"
- **Review (Strengths):** "The best exit and data protection: … a £750,000 liability floor, uncapped liability for data loss …"
- **Bid B22:** "Liability for loss of or corruption of Northvale data **caused by Hartlowe** is not subject to that cap."
- **Bid B23:** "Indirect and consequential loss is excluded."
- **Issue:** Two limits are dropped. (1) The carve-out covers only data loss or corruption *caused by Hartlowe*. (2) B23 excludes indirect and consequential loss, and the review never mentions B23. Much of the commercial damage from a data-loss event (lost orders, missed dispatch commitments to customers) is likely to be argued as indirect or consequential. "Uncapped liability for data loss" overstates the protection, and so does the "best … data protection" ranking built on it.

### A3. Meridian: ERP-side endpoints said to be pushed onto Northvale, which A3 does not say
- **Review (Concerns):** "Pushes data extraction and quality, ERP-side endpoints and training for 120 users back onto Northvale (A3, A5, A13)."
- **Review (Risk):** "integration endpoints and data quality are outside the 'as understood' scope"
- **Bid A3:** "Meridian will deliver a standard ERP integration using our published REST interface. Integration to customer-side endpoints **is delivered as a configuration activity**."
- **Issue:** A3 does not say who delivers the configuration activity. It is at least as consistent with Meridian doing it. A22 does not say that endpoints fall outside the "as understood" scope. The review's own matrix says "owner unclear", and its negotiation point asks Meridian to "State … who builds the ERP-side endpoints". The Concerns and Risk lines state as fact something the bid leaves open. (Data extraction and data quality *are* on Northvale, per A5. That part is supported.)

### A4. Meridian: service credits called a "paid" tier or "add-on"
- **Review (Summary):** "credits sit behind a paid tier"
- **Review (Concerns):** "Credits only come with a paid support tier."
- **Review (Cost):** "Service credits need the **Enhanced Support** add-on"
- **Bid A10:** "Service credits are available under our Enhanced Support tier and can be discussed as part of commercial negotiation."
- **Issue:** The bid names a tier. It does not say the tier costs extra or that it is an add-on. That may be likely, but it is not stated. The review also plays down the second half of A10 ("can be discussed as part of commercial negotiation"), which is an open offer to negotiate credits.

### A5. Meridian: uplift called "uncapped" when the bid ties it to a rate card that was not seen
- **Review (Summary):** "uplift is uncapped"
- **Review (Matrix):** "Uncapped and set by the vendor (A21)"
- **Review (Risk):** "Uncapped rate-card uplift"
- **Bid A21:** "Annual licence uplift is applied each year in line with our published rate card."
- **Issue:** The bid neither caps nor uncaps the uplift. It points to a published rate card that is not in the pack. The supported statement is "uplift not stated and not committed; set by reference to a rate card not seen". "Uncapped" is a conclusion the bid does not support. Note also that A21 is limited to the *licence* uplift.

### A6. Pellworth: "leaves out most of the scope"
- **Review (Summary):** "a price that leaves out most of the scope"
- **Review (Recommendation):** "Its headline price leaves out most of the real scope."
- **Bid D18:** "Prices at appendix 1 exclude data migration, additional carrier integration, on-site training and the discovery workshop."
- **Bid D1, D5, D6, D12:** It will "supply and implement … in accordance with section 2"; "Pellworth will build the ERP integration"; "Two carrier integrations are included"; "Training is delivered remotely."
- **Issue:** D18 lists four exclusions. Licence, implementation, ERP integration build (effort still to be confirmed), two of three carriers, remote training and support all sit inside the stated scope. The exclusions are real and material, but "most of the scope" is not supported. The review's own matrix and Concerns list the four items accurately.

### A7. Pellworth: "configurable" dropped from the stock sync, and a "real-time option" invented
- **Review (Risk):** "Stock visibility on a 15-minute sync, which misses 'accurate stock visibility' at pick time" / Mitigation: "Get the real-time option in writing"
- **Review (Concerns):** "Stock sync every 15 minutes."
- **Review (Matrix):** "Scheduled sync, 15-minute default (D3). Not real-time"
- **Bid D3:** "… updated on a scheduled synchronisation cycle. The **default** cycle is 15 minutes **and is configurable**."
- **Issue:** The Concerns and Risk lines drop "default" and "configurable". The matrix keeps "default" but drops "configurable". The bid mentions no "real-time option", so asking for one "in writing" assumes an offer that was not made. The claim that 15 minutes "misses" RFQ 3.2 is the review's judgement. RFQ 3.2 says "accurate stock visibility" and does not specify real time or pick-time accuracy.

### A8. Timetables: "Indicative" dropped for Meridian, Hartlowe and Pellworth
- **Review (Strengths, Meridian):** "A shorter rollout than Hartlowe, about 44 weeks for all four sites (A7)."
- **Review (Strengths, Pellworth):** "The shortest first-site timetable, 20 weeks (D8)."
- **Review (Risk, Hartlowe):** "The longest timetable (about 55 weeks for all sites)"
- **Bid A7:** "**Indicative** timetable: 26 weeks …" · **B8:** "**Indicative** timetable: 31 weeks …" · **D8:** "**Indicative** timetable: 20 weeks to first site."
- **Issue:** Three of the four timetables are stated as indicative, which is not a commitment. The review ranks the vendors on them as if they were fixed and never repeats the qualifier. Calderon's C10 is not called indicative, but it is only "what we believe to be market-leading". The one firm timetable statement in the pack is Hartlowe's floor in B8 ("will not compress site go-lives below 6 weeks").

### A9. Risk table: "all bids" stagger go-lives. Pellworth does not say so
- **Review (Risk):** "Stagger go-lives (all bids do this)."
- **Bid D8:** "Indicative timetable: 20 weeks to first site." (Nothing on later sites.)
- **Bid C11:** "Subsequent sites will follow an accelerated template approach." (No interval.)
- **Issue:** Pellworth says nothing about later sites. The review's own matrix records "Later sites not stated (D8)". Calderon gives no interval. Only Meridian (A7) and Hartlowe (B8) state staggered intervals.

### A10. Calderon: "not in the pack" becomes "did not supply"
- **Review (Recommendation):** "it cannot be evaluated … without documents it did not supply."
- **Review (Matrix):** "In a Service Description document not supplied (C14)"
- **Review (Basis):** "None of the pricing schedules are in the pack."
- **Bid header:** "Received 12 June 2026. 76 pages." · **C14, C22, C24, C25** refer to the Service Description and appendices 1, 2 and 5.
- **Issue:** The pack is an extract of the numbered clauses. The bid refers to appendices, which may be inside the 76-page response. The review's Basis correctly says they are "not in the pack", but the Recommendation turns this into a failure by Calderon to supply them. The pack does not support that. The same logic would apply to Meridian's and Pellworth's appendices, which the review does not treat the same way. (For Meridian's MSA, "available on request" in A23 does support "not supplied".)

### A11. Hartlowe: "the only response" that commits against RFQ 3.7
- **Review (Recommendation):** "The only response that commits in terms Northvale can enforce against RFQ 3.1, 3.6 and 3.7"
- **Bid A14:** "All customer data for European customers is hosted in our Frankfurt and Amsterdam regions."
- **Issue:** Meridian also makes a specific, testable EU hosting statement for 3.7. Hartlowe's B16 is stronger (90 days' written notice and consent before any move), but "only" is not supported for 3.7. For 3.1, B4 says outright that "Hartlowe makes no commitment as to whether Northvale achieves 48-hour dispatch". The enforceable commitment is to measurement. The review states this in its Strengths, but the Recommendation wording goes further than the bid.

---

## B. Moderate: a qualification weakened or an inference presented as fact

### B1. Hartlowe: "from day one" drops "of each site go-live"
- **Review (Summary):** "a defined dispatch measurement from day one"; **(Matrix):** "reports elapsed time per order line from day one"; **(Strengths):** "It is available from day one"
- **Bid B3:** "available as a standard report from day one **of each site go-live**"
- **Issue:** The measurement starts at each site's go-live, which under B8's indicative plan is 31 weeks or more after signature, and later for sites 2 to 4. It is not available from day one of the contract.

### B2. Hartlowe: key staff shown as "locked", with the exception dropped
- **Review (Matrix):** "Lead and two seniors named in contract and locked (B24-B25)"; **(Strengths):** "named and locked key staff"
- **Bid B25:** "will not replace them without Northvale's written agreement **except on termination of employment**."
- **Issue:** Hartlowe keeps a unilateral right to replace a named person whose employment ends.

### B3. Hartlowe: migration called "fixed-price", and the extract obligation is weakened
- **Review (Summary):** "fixed-price integration and migration"; **(Matrix):** "Hartlowe migrates from Northvale's agreed extract"
- **Bid B7:** "Northvale must provide a **full** extract in an agreed format **by the date in the project plan**."
- **Bid B21:** "Implementation is fixed price. The price is valid for 90 days from the date of this response."
- **Issue:** B7 does not call migration fixed price. That comes only by inference from B21, whose validity the review itself says has lapsed. The matrix drops "full" and the deadline, which is the dependency most likely to cause a change request given RFQ 1.2.

### B4. Hartlowe: "85 assumes shift overlap"
- **Review (Cost):** "Hartlowe's 85 assumes shift overlap, so confirm the peak"
- **Bid B19:** "Northvale's stated volumes indicate 85 concurrent licences."
- **Issue:** The bid gives no basis such as shift overlap. It attributes the figure to "Northvale's stated volumes", and the RFQ states no concurrency or shift figures at all. The right question to ask Hartlowe is which volumes it used.

### B5. Hartlowe: "Terms stated in the response"
- **Review (Matrix, Contract terms supplied):** "Terms stated in the response"
- **Bid B22:** "Hartlowe's terms limit liability …" (it refers to terms that are not supplied)
- **RFQ 4.3:** "Please state your standard contract terms."
- **Issue:** Hartlowe states selected terms (B17-B23) but, like Meridian, does not supply its standard terms. The matrix implies a completeness the bid does not show.

### B6. Hartlowe: availability "measured the way RFQ 3.6 is worded"
- **Review (Strengths):** "Availability is measured the way RFQ 3.6 is worded (operating hours, including maintenance), with defined credits (B9-B10)."
- **RFQ 3.6:** "The system must be available during our operating hours."
- **Bid B9-B11:** 99.5% during operating hours, including all maintenance. Credits must be "claimed by Northvale in writing within 30 days. Hartlowe does not apply credits automatically."
- **Issue:** "Including maintenance" is Hartlowe's term, not RFQ wording. The RFQ also does not define operating hours, which the review notes elsewhere. 99.5% still allows some downtime inside operating hours. In this line, and in the Summary's "service credits" and the Cost table's "Credits included", the claim-in-writing condition in B11 is left out. The matrix keeps it.

### B7. Meridian: availability strength drops "excluding planned maintenance" and "target"
- **Review (Strengths):** "Highest stated availability that is actually measured (99.7% monthly) …"
- **Bid A8:** "a platform availability **target** of 99.7% measured monthly, **excluding planned maintenance**."
- **Issue:** The Strengths line drops the maintenance exclusion (kept in the matrix) and the word "target". The review marks Calderon down because its availability is a "target" (C12), but does not apply the same test to Meridian's A8 or Pellworth's D9 ("Availability **target** is 99.5% measured annually"). The matrix and Concerns for Pellworth also drop "target".

### B8. Meridian: "Every commitment that matters is generic or deferred"
- **Review (Concerns):** "Every commitment that matters is generic or deferred"
- **Bids A8, A12, A14, A20, A27:** 99.7% monthly target, 1-hour Sev 1 response, Frankfurt and Amsterdam hosting, a 140-user minimum, ISO 27001 for hosting.
- **Issue:** Several of Meridian's statements are specific, and the review lists some of them as Strengths. "Every" is not supported.

### B9. Meridian: "terms are mostly 'on request'"
- **Review (Summary):** "Its terms are mostly 'on request'"
- **Bids:** Only A23 (MSA) and A26 (data export) use "on request". A24 states a liability cap, A20 the licence basis, A22 the implementation basis.
- **Issue:** This overstates the bid. A fair version would be "the MSA is only available on request, and several terms are generic".

### B10. Meridian: sub-processors "not identified"
- **Review (Concerns):** "Delivery partners and sub-processors are not identified."
- **Bid A28:** "Sub-processors are listed in our published sub-processor register."
- **Issue:** They are named in a published register that is not in the pack. That is different from "not identified". The finding holds for delivery partners (A29).

### B11. Pellworth: ISO 27001 "being pursued" dropped outside the matrix
- **Review (Summary):** "Pellworth has no ISO 27001"; **(Risk):** "No ISO 27001, public cloud unnamed"; **(Concerns):** "No ISO 27001 …"
- **Bid D22:** "Pellworth holds ISO 9001. ISO 27001 certification **is being pursued**."
- **Issue:** The statement is factually right, but it drops the stated status that certification is in progress. The matrix keeps it. Separately, the Recommendation says Pellworth "Fails on security certification … and support coverage". The RFQ contains no security certification requirement and no support-hours requirement (3.6 covers availability only). These are the review's evaluation criteria, not RFQ requirements that Pellworth failed.

### B12. Pellworth: "Severity terms can be changed at will"
- **Review (Concerns):** "Severity terms can be changed at will (D9-D11)."
- **Bid D11:** "Severity definitions and response targets are contained in our support handbook, which is updated from time to time."
- **Issue:** The bid says the handbook is updated. It does not say Pellworth can change it unilaterally or "at will". The matrix wording is faithful. The Concerns wording goes further than the bid.

### B13. Pellworth: hardware "Excluded in effect"
- **Review (Cost):** "Excluded in effect (Android 11+ only)"
- **Bid D4:** "Barcode scanning is supported on Android devices running version 11 or later."
- **Issue:** D4 is a device-compatibility statement. Pellworth says nothing about supplying hardware. The accurate entry is "Not stated", as the review records for Meridian and Calderon.

### B14. Pellworth: delivery partner "not yet chosen", and "No named people"
- **Review (Matrix):** "Partner not yet chosen. Cannot name consultants (D14-D15)"; **(Concerns):** "No named people"
- **Bid D14:** "The partner will be confirmed at contract stage." · **D15:** "unable to name individual consultants **at this stage**."
- **Issue:** "Not yet chosen" is an inference, since the bid says only that the partner is not yet confirmed. The Concerns line drops "at this stage".

### B15. "The extraction cost lands internally in every case"
- **Review (Cost, Data migration notes):** "The extraction cost lands internally in every case"
- **Bid C9:** "Calderon will lead the data migration workstream in close partnership with Northvale." · **D7:** "Data migration is provided as an optional service …"
- **Issue:** This holds for Meridian (A5) and Hartlowe (B7). Calderon's split is undefined, as the review itself says, and the scope of Pellworth's optional service is not stated. "In every case" is not supported for C and D.

### B16. Calderon: migration costed as "T&M"
- **Review (Cost):** Calderon data migration "T&M"
- **Bid C9** (quoted above) and **C24:** "Implementation is quoted on a time and materials basis …"
- **Issue:** C9 does not state a pricing basis for migration. T&M is inferred from C24 and should be marked as an inference.

### B17. 134 users treated as a firm count
- **Review (Matrix):** "RFQ implies 134 named users"; **(Negotiation):** "Set the minimum at the actual count of 134 users, not 140 (A20)."
- **RFQ 2.4:** "Training for **approximately** 120 warehouse users and 14 supervisors."
- **Issue:** The RFQ gives an approximate training population, not a named-user count. Calling 134 "the actual count" in a negotiation point turns an estimate into a figure Northvale would be held to.

---

## C. Minor: wording that drops a detail or overstates slightly

| # | Review says | Bid says | What changed |
|---|---|---|---|
| C1 | "Northvale trains the 120 (A13)" | A13: "Onward training of warehouse users is delivered by the customer **using materials we provide**." | Drops the materials Meridian supplies. |
| C2 | "Must stay on a supported release (A19)" | A19: "Customers are **expected** to remain on a supported release." | "Expected" is hardened into "must". |
| C3 | "Each release supported for 18 months (A18-A19)" | A19: "supported for 18 months **from general availability**." | The support window runs from GA, not from Northvale's adoption, so the effective window is shorter. |
| C4 | "Availability excludes planned maintenance, which could fall in operating hours" | A9: "Planned maintenance windows are notified not less than five working days in advance." | The notice commitment is never mentioned. |
| C5 | "ISO 27001, and hosting named in Frankfurt and Amsterdam (A14, A27)" (Strengths) | A27: "ISO 27001 certification **across our hosting operations**." | The Strengths line drops the hosting-only scope (the matrix keeps it). This matters when set against Hartlowe's B28 (hosting and development). |
| C6 | "Follow-the-sun support implies access from outside the EU" | A11: "regional service centres with follow-the-sun coverage." A14 covers hosting only. | Worded as an implication, but it is not stated in the bid. Keep it as a question, not a finding. |
| C7 | "+8.3% on 5-year **licence** spend" (Hartlowe); "+12.7% on 5-year **licence** spend" (Pellworth) | B20: "Annual uplift is the lower of CPI or 4% …"; D17: "Annual uplift is 6% or CPI, whichever is higher." | Neither B20 nor D17 limits the uplift to licence fees (Meridian's A21 does). It may also apply to support. The effect could be wider than stated. |
| C8 | "Says it meets section 3 (C1) but lists … multi-site labour planning as future releases (C18-C19)" | C19: "Multi-site labour planning is scheduled for the following release." RFQ section 3 has no labour-planning requirement. | Implies C19 contradicts section 3. It does not. |
| C9 | Pellworth, Summary: "a suspension right" | D20: "in the event of non-payment beyond 30 days." | Trigger dropped in the Summary (kept in the matrix and Risk table). |
| C10 | "Uplift capped at CPI or 4% (B20)" (Strengths) | B20: "the **lower of** CPI or 4%" | Ambiguous shorthand. The cap is the lower of the two, as the matrix states correctly. |
| C11 | Basis: "the Meridian and Hartlowe commercial schedules" | Neither A nor B refers to a commercial schedule. Hartlowe refers only to appendices 4 and 6. | Names documents the bids do not refer to. It is harmless, but the Hartlowe and Meridian pricing documents are assumed, not cited. |
| C12 | Hartlowe price "valid 90 days from 12 June" | B21: "valid for 90 days from **the date of this response**." Header: "Received 12 June 2026." | 12 June is the date received, not necessarily the date of the response. The lapse date of about 10 September is a fair estimate, and the review does hedge it with "~". |

---

## D. Claims checked and supported (no change needed)

- **Arithmetic:** Meridian 26 + 3×6 = 44 weeks. Hartlowe 31 + 3×8 = 55 weeks, and 31 + 3×6 = 49 at the 6-week floor. The compounding figures are right: 4% over 5 years gives +8.3% and over 3 years +4.1%; 6% over 5 years gives +12.7% and over 3 years +6.1%, against flat. Pellworth's 99.5% annually allows about 43.8 hours of downtime a year. 12 June plus 90 days is 10 September 2026.
- **Correctly reported:** Meridian A5, A10 ("can be discussed"), A13 (14 supervisors), A20, A22, A23, A24, A26. Hartlowe B4 (no promise on the outcome), B5, B6, B8 floor, B10-B11 (in the matrix), B12-B14, B15 (supervisors not mentioned), B16, B17-B18, B26 (£84,000), B27, B28, B29. Calderon C7, C12, C14, C21-C26. Pellworth D2, D5-D7, D10, D12, D16, D17 (higher of 6% or CPI), D18 (as listed in the matrix), D19-D21, D24.
- **Open issues the review raises correctly:** operating hours are undefined (B9, B14). Hartlowe's measurement starts at "received into the system" (B2), which may not match the 14:00 cut-off. The five-year total cost (RFQ 5.1) cannot be calculated from the pack.

---

## Net effect on the review's conclusions

1. **Calderon "Pass":** Its main stated ground (A1) rests on dropping "enhanced" from C18, and a second ground (A10) turns "not in the pack" into "not supplied". Calderon may still be weak, since it has T&M pricing, no stated SLA and a delivery model still to be confirmed. But the reason should be restated, and C18 should go to Calderon as a question, not be recorded as a contradiction.
2. **Hartlowe as preferred:** This is still supported on the clauses, but its protections are overstated in four places: data-loss liability (B22 causation and the B23 exclusion), "locked" staff (B25), "day one" (B3) and fixed-price migration (B7/B21). The negotiation list should add B23 and the B25 exception.
3. **Meridian:** Four negative points go beyond the bid: the "paid" credit tier, the "uncapped" uplift, ERP endpoints "pushed onto Northvale", and sub-processors "not identified". Each should become a clarification question rather than a finding. Its A14 hosting statement also answers RFQ 3.7.
4. **Pellworth:** "Most of the scope" and the "real-time option" should be corrected. The configurable sync (D3) and the ISO 27001 "being pursued" status (D22) should be restored wherever they are dropped. The "fails" language should be tied to the review's own criteria, not to RFQ requirements.
5. **All vendors:** The rollout comparisons rest on indicative timetables (A7, B8, D8), and the review should say so wherever it ranks them.
