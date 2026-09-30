# Worked example: the run

**What this is.** The `sourcing-read` guided read, run over `bid-pack.md` after Anthropic's `/vendor-review` had read the same bids (`vendor-review-run.md`). Every current count below is computed by `verify_ledger.py`: the findings from `ledger.csv`, which lists all 142 with the clause each comes from, a verbatim quote, and any condition or exception that qualifies it; and the checklist marks, the relief list and the register from the lists inside the script, each quote checked against the request or the response it cites.

**What the script checks, and what it does not.** It checks **quotation accuracy and arithmetic**: every quote and every recorded condition appears word for word where it is cited, every clause and every checklist line is accounted for, and every count is computed rather than typed. **It does not check whether a finding or a mark is right, whether a condition was missed, or whether anything was left out.** A quote can be accurate and the reading still incomplete. That review is a person's job.

**The limitation, stated first.** The bid pack is fictional and was written by the same hand that wrote the method, so this shows what the read surfaces, not how common it is. The pack publishes the numbered clauses of each response, which is what was read.

**On a second run.** These models are not deterministic, so a rerun may differ. Traceability is not something the model guarantees; it is something you verify, and this ledger is how.

---

# STAGE 1: THE REQUEST AGAINST THE CHECKLIST

Of the **core twelve** decisions, RFQ NV-2026-114 settles **none**; it partly addresses 5: A2, A3, B1, D1, D7. Of the full 47 lines it **answers 1, partly answers 11, and does not address 35**.

Every line not in this table is NOT ANSWERED: nothing in the request addresses it.

| Line | Mark | Request | Quote | What it leaves open |
|---|---|---|---|---|
| A2 | **PARTIAL** | 1.3 | *"orders received before 14:00 will be dispatched within 48 hours"* | Names a cut-off, but not which system event starts the clock or what counts as dispatched. |
| A3 | **PARTIAL** | 1.3 | *"We have committed to our three largest customers"* | Says whose orders the commitment covers; not what share of volume the system's service level must bind. |
| A4 | **ANSWERED** | 2.1 | *"across all four sites"* | Scope by site and function is stated (with 1.1 naming the sites). |
| B1 | **PARTIAL** | 3.4 | *"The system must provide reporting on warehouse performance."* | Implies the new system produces the figures; whether they sit on a record the buyer controls is not stated. |
| B3 | **PARTIAL** | 3.4 | *"The system must provide reporting on warehouse performance."* | Reporting is required; frequency, format and access to raw records are not. |
| C1 | **PARTIAL** | 1.1 | *"approximately 11,000 active stock keeping units"* | A size is given; no volume band is tied to the price or the service level. |
| D1 | **PARTIAL** | 4.3 | *"Please state your standard contract terms."* | Raises which conditions govern and leaves the answer to each supplier. |
| D7 | **PARTIAL** | 4.3 | *"Please state your standard contract terms."* | Asks for the supplier's position and states none of its own. |
| E1 | **PARTIAL** | 4.1 | *"Please provide licence costs, implementation costs and annual support costs separately."* | Asks for three cost lines; the charging basis of each is not defined. |
| F1 | **PARTIAL** | 2.2 | *"Integration with our existing ERP (finance and order management) and with three carrier systems."* | Integrations are in scope; who builds them and who pays when they change is not stated. |
| F4 | **PARTIAL** | 3.2 | *"The system must give us accurate stock visibility across all four sites."* | Visibility is required; live data versus reports, and how accuracy is measured, are not. |
| I3 | **PARTIAL** | 3.7 | *"Data must be held within the European Union."* | One requirement is stated; who evidences compliance is not. |

The most expensive line in the request is 4.3: *"Please state your standard contract terms."* It hands the liability position to the other side. All four responses answered it with their own terms.

---

# STAGE 2: THE RELIEF LIST

Run against RFQ NV-2026-114 only. Twenty things a capable WMS vendor would be relieved Northvale did not ask for, each marked against the request. Where the request comes close, the nearest clause is quoted to show why it does not cover the item.

| # | What a vendor would be relieved you did not ask | Mark | Nearest clause |
|---|---|---|---|
| 1 | What event starts the dispatch clock in the system, and what event stops it | **NOT COVERED** | 1.3: *"orders received before 14:00 will be dispatched within 48 hours"* |
| 2 | Which system of record produces the dispatch performance figure | **NOT COVERED** | 1.3: *"We currently measure this manually"* |
| 3 | A stock accuracy figure, and how accuracy is measured | **NOT COVERED** | 3.2: *"accurate stock visibility"* |
| 4 | Maximum acceptable latency for cross-site stock visibility | **NOT COVERED** |  |
| 5 | An availability percentage, and over what window | **NOT COVERED** | 3.6: *"must be available during our operating hours"* |
| 6 | Whether availability is measured including or excluding planned maintenance | **NOT COVERED** |  |
| 7 | Whether service credits exist, and whether they are applied automatically | **NOT COVERED** |  |
| 8 | Restoration targets by severity, not only response targets | **NOT COVERED** | 2.5: *"Support from go-live."* |
| 9 | Support hours expressed in the time zones of all four sites | **NOT COVERED** |  |
| 10 | Data export format, timeframe and cost at exit | **NOT COVERED** |  |
| 11 | Who owns the operational data, and whether extraction is chargeable | **NOT COVERED** |  |
| 12 | A cap on the annual licence uplift | **NOT COVERED** | 4.1: *"annual support costs separately"* |
| 13 | How long the quoted price remains valid | **NOT COVERED** |  |
| 14 | What is excluded from the quoted price | **NOT COVERED** |  |
| 15 | Whether implementation is fixed price or time and materials | **NOT COVERED** | 4.1: *"implementation costs"* |
| 16 | Named individuals, and what happens when they leave | **NOT COVERED** |  |
| 17 | Whether implementation is sub-contracted, and to whom | **NOT COVERED** |  |
| 18 | The liability cap, and whether loss of data is carved out of it | **NOT COVERED** | 4.3: *"Please state your standard contract terms."* |
| 19 | Release policy: whether the customer can be forced to upgrade | **NOT COVERED** |  |
| 20 | Whether any required capability is not yet built | **NOT COVERED** |  |

**Asked for in the request, and so not reliefs.** Listed for contrast only; they are not part of the twenty.

| Item | Clause |
|---|---|
| Data residency | 3.7: *"Data must be held within the European Union."* |
| Three carrier integrations | 2.2: *"three carrier systems"* |
| Training volumes | 2.4: *"approximately 120 warehouse users and 14 supervisors"* |
| Migration of stock records, locations and open orders | 2.3: *"Migration of current stock records, locations and open orders."* |

### **RELIEFS NOT COVERED: 20 of 20**

**Read this count for what it is.** The list is built to find gaps: it asks for the twenty things a supplier would most like you to have missed. A thin request will leave most or all of them open, as this one does. So the count is a list of what to ask next, not a score of the document. The checklist coverage in Stage 1 is the measurement, because it has a denominator the request did not choose.

**The finding of this stage.** Item 18 is not an omission, it is an invitation. Request 4.3, *"Please state your standard contract terms"*, hands the liability position to the supplier and calls it a question. A, B and D state their own liability caps. C points to standard terms without stating one. B alone explicitly excludes data loss or corruption it causes from its cap.

---

# STAGE 3: CHECKING THE AI REVIEW

Before this read, the bids were run through Anthropic's `/vendor-review` (see `vendor-review-run.md`). It is accurate and fast: every figure checked against the bid pack was right, and it found the lapsed price validity at B21, which this run had not headlined. **Use it.** Then check the lines your decision will rest on against the bids' own words.

| The review says | Clause | The bid says | Verdict |
|---|---|---|---|
| *"Lead and two seniors named in contract and locked"* | B25 | *"except on termination of employment"* | **DROPS A CONDITION** |
| *"commits in terms Northvale can enforce"* |  |  | **OUTSIDE A READ** |
| *"**Negotiate** (preferred)"* |  |  | **RECOMMENDATION** |
| *"Northvale responsible for extraction and data quality"* | A5 | *"The customer is responsible for data extraction and data quality."* | **MATCHES** |
| *"valid 90 days from 12 June (lapsed ~10 Sep 2026)"* | B21 | *"The price is valid for 90 days from the date of this response."* | **MATCHES** |
| *"Data loss uncapped"* | B22 | *"caused by Hartlowe"* | **DROPS A CONDITION** |
| *"which contradicts its claim to meet section 3"* | C18 | *"Enhanced dispatch performance analytics are on our published roadmap for release in Q1 2027."* | **OVERSTATES** |
| *"on the roadmap for Q1 2027"* | C18 | *"on our published roadmap for release in Q1 2027"* | **MATCHES** |
| *"during Northvale operating hours, including maintenance"* | B9 | *"during Northvale's operating hours, including all maintenance"* | **MATCHES** |

**Recorded conditions the review carries: 10 of 12.** It drops two. At B25 it calls the named team "locked"; the clause keeps them only until their employment ends, whoever ends it. At B22 it writes "Data loss uncapped"; the clause uncaps only data loss "caused by Hartlowe". It also turns C18's roadmap for *enhanced* analytics into a contradiction of C1, which is a question for Calderon, not a finding. It also says one bid commits in terms Northvale "can enforce", which no reading of a bid can establish, and it ends in a recommendation. The recommendation is the tool's call. It does not go into the signer's record.

---

**A second pass with a short prompt found more.** Given the prompt printed in `review-check-one-instruction.md` (it begins *"Check every material claim in this review against the bids and keep every qualification"*), a second Claude instance, given only the review and the bid pack, listed 40 flags, with 42 bid quotes and 43 review quotes, every one confirmed by `verify_ledger.py` (`review-check-one-instruction.md`). Another Claude session, instructed to challenge every flag, then judged each one against the bids (`test-1-adjudication.md`): **it upheld 11, upheld 19 in part, rejected 10, and marked 4 as potentially material**. These are a model's judgements, not settled facts. The four are C18's overstated contradiction, B23's exclusion of consequential loss beside the uncapped data-loss carve-out, the preferred bidder's full terms never seen, and Calderon's appendices missing from the extract rather than from the bid. The table above, as first built, caught none of the four. It is the weaker check.

**B22 is disputed.** The same adjudicator judged that "caused by Hartlowe" adds little, since a supplier is only liable for loss it causes. It may matter if a hosting sub-processor causes the loss. The mark above is kept, with this note.

---

# STAGE 4: OBLIGATIONS, TERMS, EXCLUSIONS AND SILENCES

This run took the structured route, with the four tables and their counts. The short read, without counts, is the other route in the skill.

Read in the order received: A, B, C, D. **The unit is the finding, not the clause**, so 111 clauses yield 142 findings. One clause, D18, yields none, because it restates exclusions already recorded at D5, D6, D7 and D12.

| Response | Clauses | Obligations | Terms | Declared exclusions | Silences | Findings |
|---|---|---|---|---|---|---|
| **A Meridian** | 30 | **9** | 7 | 3 | **16** | 35 |
| **B Hartlowe** | 29 | **27** | 11 | 5 | **4** | 47 |
| **C Calderon** | 28 | **5** | 5 | 0 | **21** | 31 |
| **D Pellworth** | 24 | **11** | 4 | 7 | **7** | 29 |
| **TOTAL** | **111** | **52** | **27** | **15** | **48** | **142** |

**A count is not a verdict.** Twenty-seven commitments are not better than nine unless they are the ones your purchase needs. These numbers describe documents; they rank nobody.

**The refusal that tells you most.** B4: *"Hartlowe makes no commitment as to whether Northvale achieves 48-hour dispatch. That depends on Northvale's operation. Hartlowe commits that Northvale will be able to prove whether it did."* B2 and B3 are the proof: elapsed time per order line, reported from day one, with the raw data exportable at no charge.

**The verb.** RFQ 3.1: *"must support"*. A2: *"supports … 48-hour dispatch workflows."* A echoes the requirement; B tells you what you will be able to check.

**Zero.** C declares no exclusions at all. It never says what it will not do.

### Read to the end of the sentence

The findings below carry a condition or exception, quoted from the same clause. **A commitment read without its exception is a misreading, however accurate the quote.**

| Clause | Finding | Condition or exception |
|---|---|---|
| B25 | no replacement without consent | *"except on termination of employment"* |
| B14 | sev1 oncall | *"for Severity 1 only"* |
| B10 | service credits | *"to a maximum of 30% of the monthly fee"* |
| B11 | service credits | *"in writing within 30 days"* |
| B18 | successor cooperation | *"for 90 days after termination"* |
| B21 | implementation price | *"valid for 90 days"* |
| B3 | raw data export free | *"without charge at any time"* |
| D10 | support hours mon fri | *"excluding public holidays in the Republic of Ireland"* |
| D21 | exit data 30d | *"for 30 days"* |
| A8 | availability | *"measured monthly"* |
| D9 | availability | *"measured annually"* |
| B22 | data loss uncapped | *"caused by Hartlowe"* |

The one that matters most is B25: *"Hartlowe will name the implementation lead and two senior consultants in the contract, and will not replace them without Northvale's written agreement except on termination of employment."* The protection is real, and for each of the three it ends with their employment, whoever ends it.

---

# STAGE 5: WHERE THE BIDS DIFFER

**Obligations only.** A real difference is a commitment some responses make and others do not. Only one obligation is made by all four: data in eu.

On the current grouping, **41 obligations separate the field**: B alone carries 21, A alone 4, C alone 2, D alone 8, and 6 are shared by two or three.

⚠ **This count depends on how commitments are grouped, and it moved when the grouping was corrected.** An earlier version gave all four bids one label for ERP integration. That hid the real difference: B commits to building against the ERP version the buyer confirms and testing it jointly, while D leaves scope and effort to a chargeable discovery workshop. Splitting that one label moved the total from 37 to 41. **Treat the count as a map of where to look, not as a finding.** It is not used in the newsletter for that reason.

**Carried by B alone:** availability incl maintenance, carrier integration all three, dispatch elapsed report, dispatch report day one, erp integration confirmed version tested jointly, exit export free, named personnel, no data move without consent, no replacement without consent, no subcontracting, raw data export free, roadmap published, sev1 oncall, sev1 restoration 8h, sev2 resolution 5d, sev2 response 4h, successor cooperation, support hours mon sat, training all users, training refresher, trial migrations.

**Carried by D alone:** carrier integration two, cutoff configured, erp integration scope after workshop, exit data 30d, iso9001, stock sync 15min, support hours mon fri, training remote.

**Carried by A alone:** erp integration standard interface, maintenance notice 5d, release support 18m, subprocessor register.

**Carried by C alone:** erp integration via platform, training academy access.

**Shared:** data migration (ABC); deliver scope (BD); device support (BD); iso27001 (AB); sev1 response 1h (AB); training supervisors (AC).

---

# STAGE 6: THE WEEK AFTER

Suppose the panel scores A highest. The read turns the evidence into the work of the next five days.

### The clarification letter to A

Every silence in A's response becomes one question, citing the sentence it answers, or a stated reason for none.

| # | Clause | A wrote | Question |
|---|---|---|---|
| 1 | A1 | *"confirms full functional coverage of the scope"* | Against each function in section 2.1, which are standard, which need configuration and which need development? |
| 2 | A2 | *"supports high-velocity dispatch operations including same-day and 48-hour dispatch workflows"* | What will you measure for 48-hour dispatch: which system events start and stop the clock, and which report will Northvale receive from go-live? |
| 3 | A4 | *"pre-built connections to more than sixty carriers"* | Are Northvale's three carriers among the pre-built connections, and is their integration inside the fixed price? |
| 4 | A6 | *"a proven five-phase approach refined across more than 400 implementations"* | Please name the five phases, the deliverable and acceptance test at the end of each, and what Northvale must provide in each. |
| 5 | A7 | *"Indicative timetable: 26 weeks"* | Which milestones will you commit to in the contract, and what applies if one is missed? |
| 6 | A8 | *"commits to a platform availability target of 99.7%"* | Will you commit to availability as an obligation, measured during Northvale's operating hours and including maintenance? |
| 7 | A10 | *"can be discussed as part of commercial negotiation"* | Which service credits apply in the standard support tier, and are they applied automatically? |
| 8 | A11 | *"follow-the-sun coverage"* | What are the support hours and restoration targets by severity for each site, and from which countries can support staff access Northvale data? |
| 9 | A15 | *"more than 200 standard reports and a self-service report builder"* | Which standard reports meet section 3.4, and which would Northvale have to build? |
| 10 | A16 | *"Performance measurement against dispatch commitments is fully supported"* | Is dispatch performance measurement a standard report at go-live, or something built with the report builder, and is it in the price? |
| 11 | A17 | *"architected for scale and additional sites can be onboarded rapidly"* | What are the price and lead time to add a fifth site? |
| 12 | A23 | *"A copy is available on request."* | Please send the Master Services Agreement before shortlisting. |
| 13 | A26 | *"Customer data may be exported on request in a standard format."* | At exit, in what format, within what time and at what cost is the data returned, and is the database schema included? |
| 14 | A29 | *"drawn from Meridian's delivery organisation and approved delivery partners"* | Please name the delivery partners and the key individuals, and say whether any can be replaced without Northvale's agreement. |

**No question, with the reason:**

- **A25** *"committed to a long-term partnership with Northvale and to your continued success"*: Nothing a supplier could write would settle it. It goes into the register as a claim that cannot be checked.
- **A30** *"We would be pleased to discuss any specific requirements not addressed above."*: An offer to talk, not a claim about the service.

### The schedule of commitments for the contract

For the people who draft the agreement: every obligation in A's response, word for word, with its condition. Whether and where each is written into the signed agreement is their call; the read does not say what is enforceable.

| Clause | Commitment | Condition |
|---|---|---|
| A3 | *"will deliver a standard ERP integration using our published REST interface"* | none recorded |
| A5 | *"will migrate stock records, location data and open orders"* | none recorded |
| A9 | *"Planned maintenance windows are notified not less than five working days in advance."* | none recorded |
| A12 | *"Severity 1 incidents receive a response within one hour."* | none recorded |
| A13 | *"will provide a train-the-trainer programme covering 14 supervisor users"* | none recorded |
| A14 | *"hosted in our Frankfurt and Amsterdam regions"* | none recorded |
| A19 | *"Releases are supported for 18 months from general availability."* | none recorded |
| A27 | *"maintains ISO 27001 certification across our hosting operations"* | none recorded |
| A28 | *"Sub-processors are listed in our published sub-processor register."* | none recorded |

**Excluded by A. Decide who carries each:**

- **A5** *"The customer is responsible for data extraction and data quality."*
- **A8** *"excluding planned maintenance"*
- **A13** *"Onward training of warehouse users is delivered by the customer"*

**Terms the drafters must see:**

- **A18** *"New functionality is delivered to all customers automatically."*
- **A19** *"Customers are expected to remain on a supported release."*
- **A20** *"per named user per annum, with a minimum commitment of 140 users"*
- **A21** *"Annual licence uplift is applied each year in line with our published rate card."*
- **A22** *"Implementation is quoted as a fixed price based on the scope as understood"*
- **A23** *"standard Master Services Agreement applies"*
- **A24** *"limit liability to the fees paid in the preceding twelve months"*

14 questions, 9 commitments, 3 exclusions and 7 terms, drafted from the ledger. The checks in the register below get their dates from the same pass.

---

# STAGE 7: THE REGISTER

Suppose the panel awarded to A. These are the five claims its scoring leaned on, each turned into what you would observe if it held, when, and on which record.

| Claim | What you would observe | When | Record | Verdict |
|---|---|---|---|---|
| **A16** *"Performance measurement against dispatch commitments is fully supported"* | A dispatch performance report you can run in your own tenant | Go-live | Your own tenant: you run the report | **CHECKABLE** |
| **A7** *"Indicative timetable: 26 weeks from contract signature to first site go-live"* | The actual first go-live date. Offered as indicative, so checkable but not binding | First go-live | Your project record | **CHECKABLE** |
| **A2** *"supports high-velocity dispatch operations including same-day and 48-hour dispatch workflows"* | Only that dispatch workflows exist, which any such system has. Nothing would show whether they meet the 48-hour commitment the request asked about | None | None | **CANNOT BE CHECKED** |
| **A8** *"platform availability target of 99.7% measured monthly, excluding planned maintenance"* | Monthly availability, but only as the supplier reports it, with maintenance removed first | First service review | Supplier reporting only | **CANNOT BE CHECKED** |
| **A25** *"committed to a long-term partnership with Northvale and to your continued success"* | Nothing | None | None | **CANNOT BE CHECKED** |

### **CLAIMS THAT CANNOT BE CHECKED: 3 of 5**

**Why A16 passes and A2 does not, when both use the same verb.** A16 names one specific capability, dispatch performance measurement, and its absence at go-live would show the claim false: you run the report in your own tenant or you cannot. A2 names no outcome. Any such system has dispatch workflows, so nothing you could observe would show it false, and nothing would show whether the 48-hour commitment the request asked about is supported. A16 is still a silence in the ledger, because it promises a capability and not a result. A8 fails for a different reason: availability can only be read from the supplier's own reporting.

### Odds, reasoned from causes

For the two claims that can be checked, write your odds that each holds. **Four bids give you no pattern to learn from**: there is no history of bids like these and what followed them. So do not ask a model to predict the supplier. Start from how often projects like this slip, which is a question about the class of project, not this one. Then run a pre-mortem: it is the milestone and the claim failed. What in this contract would have caused it?

The guided read finds the causes, each tied to a clause. **The odds are yours; the read never sets them.**

| Claim | What would cause it to fail | Evidence |
|---|---|---|
| **A7** | Data extraction from a legacy system no one left in the business understands, and it is Northvale's job | Request 1.2: *"The two people who understood it have left the business."*; A5: *"The customer is responsible for data extraction and data quality."* |
| **A7** | Anything outside the scope as A understood it goes through change control | A22: *"Changes to scope are handled through our change control process."* |
| **A7** | A slip costs A nothing: the timetable is offered as indicative | A7: *"Indicative timetable"* |
| **A16** | The measurement may be something Northvale has to build itself | A15: *"a self-service report builder"* |
| **A16** | The report can exist and measure the wrong thing: the request never fixed the start and stop events | Request 1.3: *"orders received before 14:00 will be dispatched within 48 hours"* |

At go-live you learn two things: whether the claim held, and how far your odds were from the outcome. The workbook scores that for you. Over several decisions it becomes a record of how well your own judgment about suppliers is calibrated.

**What to ask for next time**, one line from each of the three:

1. From A2: require the dispatch measurement as a named deliverable with an acceptance test, not as a supported capability.
2. From A8: require availability to be evidenced from a source the buyer can read, and define whether maintenance is inside or outside the measure.
3. From A25: strike unfalsifiable commitment language from the response template, or stop scoring it.

Those three lines go into the next request.

---

# THE CARD

The two answers side by side, labelled *Fictional worked example*:

> **A:** *"supports … 48-hour dispatch workflows"*
> **B:** *"makes no commitment as to whether Northvale achieves 48-hour dispatch … commits that Northvale will be able to prove whether it did"*

---

# WHAT RUNNING IT CHANGED IN THE METHOD

**The first pass had no box for an honest refusal.** B's refusals landed among the non-answers, and the most transparent bidder looked the most evasive. Adding declared exclusions reversed the reading.

**Terms were counted as obligations**, and clauses were counted as findings. Both are now separate, and the counts are generated from the ledger.

**A target is not a commitment wherever it appears**: A8 and D9 are silences, and B8's indicative timetable is a silence while its refusal to compress go-lives is an exclusion.

**Accurate quotes hid incomplete readings.** A review of the ledger found three: B25's exception was left out of the finding, B22's separate carve-out for data loss was not recorded, and one shared label for ERP integration concealed a real difference. All three are fixed, and the ledger now has a conditions column so exceptions stay visible.

**Counts that were typed did not survive being checked.** The relief list reported 16 not covered while listing 20, and the checklist coverage was reported as 3 answered, 4 partly and 40 not before any mark had to carry a quote. Once every mark did, and an independent check had argued with the marks, it came to {n['ANSWERED']}, {n['PARTIAL']} and {n['NOT ANSWERED']}. The checklist marks, the relief list and the register are now in the script, so every count in this file is computed.

**An AI review now comes first.** Anthropic's `/vendor-review` read the same bids, accurately, and found one thing this read had not headlined: the lapsed price at B21. A second pass with a one-sentence instruction checked the review better than this read's own hand-built check did. So this read no longer competes with it. Its job moved to checking the review, keeping the decision with the signer, and the work of the week after.

**The checklist gained four lines** from things the run found: D7, F5, F6, F7.

# WHAT THE RUN DID NOT DO

It did not rank, price or recommend. It never saw the weights. It cannot tell you the losing bids were worse, does not tell you to stay or walk, and does not decide what is enforceable.
