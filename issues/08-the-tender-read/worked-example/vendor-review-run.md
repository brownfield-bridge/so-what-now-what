# /vendor-review, run on the bid pack

*Output of Anthropic's `/vendor-review` skill (Operations plugin 1.3.0, `anthropics/knowledge-work-plugins`, commit da38ec1), run on 29 September 2026 by a Claude instance following the published SKILL.md exactly. Its only inputs were the skill and `bid-pack.md`. This is a faithful run of the published instructions, not the Cowork runtime itself. The text below is unedited, except that en dashes in clause ranges were changed to hyphens to match this repository's style.*

---

## Vendor Review: Meridian vs Hartlowe vs Calderon vs Pellworth (RFQ NV-2026-114, Warehouse and Dispatch Management System)
**Date:** 29 September 2026 | **Type:** Comparison (new vendor, four responses)

**Basis:** The numbered response clauses in the bid pack for all four vendors, checked against the RFQ. None of the pricing schedules are in the pack. That covers Calderon appendices 1 and 2, Pellworth appendix 1, and the Meridian and Hartlowe commercial schedules. So no total cost can be calculated yet, and the only figures below are the ones the vendors wrote into their clauses.

### Summary
**Hartlowe** is the only response that makes commitments Northvale can test. It gives a defined dispatch measurement from day one, availability measured during Northvale's operating hours, service credits, fixed-price integration and migration, on-site training for all 120 users, free exit data, and named staff. It should be the lead candidate and go to negotiation. Its implementation price validity ran out on about 10 September 2026, so the price has to be confirmed again. **Meridian** is a credible second choice but needs tightening before it can be compared fairly. Its terms are mostly "on request", credits sit behind a paid tier, uplift is uncapped, and it pushes data extraction and training for 120 users back onto Northvale. **Calderon** and **Pellworth** should be passed in their current form. Calderon's own roadmap puts dispatch performance analytics in Q1 2027, which contradicts its claim to meet section 3. Pellworth has no ISO 27001, a 6% uplift floor, a suspension right, weak exit terms and a price that leaves out most of the scope.

### Comparison Matrix

| Dimension | Meridian (A) | Hartlowe (B) | Calderon (C) | Pellworth (D) |
|---|---|---|---|---|
| **Pricing: licence model** | Per named user, minimum 140 (A20). RFQ implies 134 named users | Per concurrent user, 85 licences proposed (B19) | Per site plus volume-based transactions, overage at appendix 2 rates (C21-C22) | Per named user, three-year minimum term (D16) |
| **Pricing: annual uplift** | "In line with our published rate card". Uncapped and set by the vendor (A21) | Lower of CPI or 4%, from the go-live anniversary (B20) | "In accordance with our standard commercial terms". Unstated (C23) | **Higher** of 6% or CPI. Floor of 6%, no cap (D17) |
| **Pricing: implementation basis** | Fixed price for scope "as understood", with change control (A22) | Fixed price, **valid 90 days from 12 June (lapsed ~10 Sep 2026)** (B21) | Time and materials with an indicative estimate (C24) | Appendix 1 price excludes migration, third carrier, on-site training and discovery workshop (D18) |
| **Timetable** | 26 weeks to first site, then 6-week intervals, so about 44 weeks for all four (A7) | 31 weeks to first site, then 8-week intervals, so about 55 weeks for all four. Will not compress below 6 weeks (B8) | 22 weeks to first site, then an unquantified "accelerated template" (C10-C11) | 20 weeks to first site. Later sites not stated (D8) |
| **Feature: 48h dispatch (RFQ 3.1)** | "Supports… 48-hour dispatch workflows" and "fully supported within Insight". No definition of the measurement (A2, A16) | Records order-received time and carrier-handover time, reports elapsed time per order line from day one, free CSV export. Explicitly does not promise the result (B2-B4) | Claims ready support (C2), but "enhanced dispatch performance analytics" are on the roadmap for Q1 2027 (C18) | Will configure the 14:00 cut-off (D2). No measurement or reporting commitment |
| **Feature: stock visibility (3.2)** | Covered only through the generic "full functional coverage" (A1) | Covered as scope item "stock control" (B1). No specific statement | "Real-time multi-site" (C3) | Scheduled sync, 15-minute default (D3). Not real-time |
| **Feature: handheld scanning (3.3)** | Not addressed specifically | Two device families (appendix 4). No hardware supplied (B27) | "All major handheld platforms" (C4) | Android 11+ only (D4) |
| **Feature: reporting (3.4)** | Insight module, 200+ reports and a report builder (A15) | Dispatch report stated. Wider reporting not described | "Comprehensive… out of the box" (C5) | Not addressed |
| **Feature: growth / fifth site (3.5)** | "Architected for scale" (A17) | Concurrent licensing. Extra carriers £6,500 each (B6) | Per-site licence, so a fifth site adds a licence (C21) | Not addressed |
| **Feature: returns** | Covered only through the generic claim (A1) | Standard config only. Three-tier inspection needs **£84,000** development (B26) | Not addressed | Not addressed |
| **Integration: ERP** | "Standard" REST interface. Customer-side endpoints are a "configuration activity", owner unclear (A3) | Built by Hartlowe for the confirmed ERP version, jointly tested, fixed price, 2 change requests included (B5) | Scoped after award (C6-C7) | Built by Pellworth after a **chargeable** discovery workshop (D5) |
| **Integration: carriers** | Framework of 60+ carriers. Northvale's three not confirmed (A4) | All three included at fixed price (B6) | "Logistics partner ecosystem". Unpriced (C8) | Two included, third quoted later (D6) |
| **Data migration** | Meridian migrates. **Northvale responsible for extraction and data quality** (A5) | Hartlowe migrates from Northvale's agreed extract, with two trial migrations (B7) | "Lead… in close partnership". Split of responsibilities undefined (C9) | Optional and **not in price** (D7) |
| **Training (134 users)** | Train-the-trainer for 14 supervisors only. Northvale trains the 120 (A13) | All 120 users on site, four cohorts per site, 90-day refresher. Supervisors not mentioned (B15) | Digital academy plus on-site supervisor sessions (C15-C16) | Remote. On-site costs extra (D12) |
| **Security certification** | ISO 27001 for hosting (A27) | ISO 27001 for hosting and development, certificate number in appendix 6 (B28) | Not stated | ISO 9001 only. 27001 "being pursued" (D22) |
| **EU data residency (3.7)** | Frankfurt and Amsterdam (A14). Sub-processors per public register (A28). Follow-the-sun support implies access from outside the EU | Frankfurt. No move outside the EU without 90 days' notice **and consent** (B16) | "Available and will be configured" (C17) | "Major public cloud in an EU region". Provider and region not named (D13) |
| **Support hours** | Follow-the-sun (A11) | 06:00-20:00 CET Mon-Sat. Sev 1 on call outside those hours (B14) | Named CSM (C13). Hours not stated | 08:00-18:00 CET Mon-Fri, **excluding Irish public holidays** (D10) |
| **Support response** | Sev 1: 1-hour response. No restore target (A12) | Sev 1: 1h response and 8 working hours to restore or workaround. Sev 2: 4h / 5 days (B12-B13) | In a Service Description document not supplied (C14) | In a handbook "updated from time to time" (D11) |
| **Availability** | 99.7% monthly, **excluding planned maintenance** (A8-A9) | 99.5% monthly **during Northvale operating hours, including maintenance** (B9) | "Targets" 99.9%. No measurement basis (C12) | 99.5% **annually** (D9), which allows about 44 hours in a year, possibly all at once |
| **Service credits** | Only under the Enhanced Support tier, "can be discussed" (A10) | 5% of monthly support fee per 0.1% shortfall, capped at 30%. Must be claimed in writing within 30 days (B10-B11) | None stated | None stated |
| **Feature delivery cadence** | Continuous release, auto-deployed. Each release supported for 18 months (A18-A19) | Quarterly roadmap. No contractual dates (B29) | 18% of revenue to R&D (C20). Key features on roadmap (C18-C19) | Not stated |
| **Contract terms supplied** | MSA "available on request" (A23) | Terms stated in the response | Summary only, appendix 5 (C25) | Key terms stated |
| **Liability cap** | 12 months' fees (A24) | Greater of £750,000 or 12 months' fees. **Data loss uncapped** (B22) | Not stated | **50%** of 12 months' fees (D19) |
| **Exit / data return** | Export "on request in a standard format" (A26) | Full CSV plus documented schema within 15 working days, free. 90 days of successor co-operation at day rate (B17-B18) | Not stated | 30 days in native format. Extraction help is chargeable (D21) |
| **Other terms** | Must stay on a supported release (A19) | Price validity 90 days (B21) | None stated | Can suspend service for non-payment beyond 30 days (D20) |
| **Delivery team** | Own staff plus "approved delivery partners" (A29) | Employees only. Lead and two seniors named in contract and locked (B24-B25) | Partner network, model confirmed at contract stage (C26) | Partner not yet chosen. Cannot name consultants (D14-D15) |
| **References** | "400+ implementations" and "comparable" customers, none named (A2, A6) | None offered | None offered | Reference visit offered (D24) |

### Cost Analysis

The skill's template asks for annual figures. The RFQ (5.1) evaluates on **five-year** total cost. None of the price figures are in the pack, so the table below maps the cost structure and marks what is still unknown. The totals can only be filled in once the pricing appendices are to hand.

| Component | Meridian | Hartlowe | Calderon | Pellworth | Notes |
|---|---|---|---|---|---|
| License/subscription | Not in pack. Billed on at least 140 named users | Not in pack. 85 concurrent users | Not in pack. Per site plus transaction band | Not in pack. Named users, three-year minimum | Named-user models bill 134+ people. Hartlowe's 85 assumes shift overlap, so confirm the peak |
| Annual uplift, 5-year effect | Uncapped (rate card) | At most 4%, so at most **+8.3%** on 5-year licence spend vs flat (+4.1% over 3 years) | Unstated | At least 6%, so at least **+12.7%** on 5-year licence spend vs flat (+6.1% over 3 years) | Compounding figures are calculated from the uplift clauses |
| Implementation | Not in pack. Fixed, but scope "as understood" | Not in pack. Fixed. **Validity lapsed about 10 Sep** | Not in pack. Time and materials, "indicative" only | Not in pack. Discovery workshop extra | Only Hartlowe's price is tied to a defined scope |
| Integration: ERP | Inside the fixed price? Customer-side endpoint work may fall to Northvale | Included, plus 2 change requests | T&M, scoped after award | Chargeable discovery, then effort confirmed | |
| Integration: carriers | Framework. Confirm Northvale's 3 carriers are in it | 3 included. **£6,500** per extra carrier | Partner ecosystem, unpriced | 2 included. Third to be quoted | |
| Data migration | Included, but extraction and data-quality work on Northvale | Included. Extract on Northvale | T&M | **Excluded** | Northvale's own legacy system knowledge has left the business (RFQ 1.2). The extraction cost lands internally in every case |
| Training and onboarding | 14 supervisors only. Internal cost to train 120 users | All 120 on site plus 90-day refresher | Digital plus supervisor sessions | Remote. On-site extra | |
| Hardware (handhelds) | Not stated | Excluded | Not stated | Excluded in effect (Android 11+ only) | Budget separately whoever wins |
| Support/maintenance | Not in pack. Service credits need the **Enhanced Support** add-on | Not in pack. Credits included | Not in pack | Not in pack | |
| Known optional development | Unknown | Three-tier returns: **£84,000** if required | Unknown | Unknown | Only Hartlowe declared this gap. Ask the others about it |
| Transaction overage | n/a | n/a | Appendix 2 rates | n/a | Growth and a fifth site raise Calderon's cost twice (volume and site) |
| Exit costs | Unknown. MSA not seen | Data export free. Successor co-operation at day rate | Unknown | Extraction help chargeable. 30-day window. Three-year lock-in | |
| **Total Year 1** | **Cannot be calculated** | **Cannot be calculated** | **Cannot be calculated** | **Cannot be calculated** | Needs the pricing appendices |
| **Total 3-Year** | **Cannot be calculated** | **Cannot be calculated** | **Cannot be calculated** | **Cannot be calculated** | |
| **Total 5-Year (RFQ 5.1 basis)** | **Cannot be calculated** | **Cannot be calculated** | **Cannot be calculated** | **Cannot be calculated** | |
| **Price certainty** | Medium | **High** | Low | Low | Best judgement on what is visible |

### Risk Assessment

| Vendor | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| All | Financial stability not evidenced. No vendor supplied accounts, ownership or customer base data | Unknown | High | Request the last two years' accounts and a credit check before award |
| All | Business continuity and disaster recovery not addressed (backup, RPO/RTO, failover) | Medium | High | Require DR terms and tested recovery objectives in the contract |
| All | Concentration: one platform runs dispatch at all four sites | Medium | High | Stagger go-lives (all bids do this). Keep an offline or manual dispatch fallback and a proven exit route |
| All | Northvale-side data extraction from a legacy system whose experts have left | High | High | Start the extraction and cleansing work now. Favour a vendor that runs trial migrations (Hartlowe B7) |
| Meridian | Scope creep via change control, because integration endpoints and data quality are outside the "as understood" scope | Medium | Medium | Attach a scope schedule that names the ERP-side work and the three carriers |
| Meridian | Uncapped rate-card uplift and a minimum of 140 users | High | Medium | Cap the uplift. Set the minimum at the actual user count |
| Meridian | Availability excludes planned maintenance, which could fall in operating hours. Credits need a paid tier | Medium | Medium | Measure during operating hours, including maintenance. Put credits in the base tier |
| Meridian | Forced upgrades (continuous release, 18-month support) create retesting cost | Medium | Medium | Contractual regression testing of Northvale's integrations for each release |
| Meridian | MSA, sub-processors and delivery partners not seen. Possible non-EU support access | Medium | Medium | Get the MSA and sub-processor list. Confirm where support staff access data from |
| Hartlowe | Price validity has lapsed. The price may move | High | Medium | Request written reconfirmation before sign-off |
| Hartlowe | Returns gap (£84,000) if three-tier inspection is actually needed | Medium | Medium | Confirm the internal returns requirement, then negotiate or descope |
| Hartlowe | Support gaps: Sunday and night cover is Sev 1 only, and hours may not match operating hours | Medium | Medium | Define operating hours in the contract. Extend cover if sites run outside 06:00-20:00 Mon-Sat |
| Hartlowe | The longest timetable (about 55 weeks for all sites) keeps the old system running longer | High | Medium | Accept, or negotiate 6-week intervals (their stated floor) for later sites |
| Hartlowe | Concurrent-licence ceiling at peak (85 assumed) | Medium | Low | Price the step-up per concurrent licence and allow temporary peaks |
| Calderon | Core requirement contradicted: dispatch performance analytics only on the Q1 2027 roadmap (C18 vs C1) | High | High | Contractual commitment with remedies, or pass |
| Calderon | Uncapped cost: T&M implementation, integration scoped after award, transaction overage | High | High | Fixed price after scoping, or pass |
| Calderon | No stated SLA, credits, liability, exit terms, security certification or delivery team | High | High | Every item needs to be in writing before any evaluation |
| Pellworth | No ISO 27001, public cloud unnamed | High | High | Pass, or require certification before award |
| Pellworth | Stock visibility on a 15-minute sync, which misses "accurate stock visibility" at pick time | Medium | Medium | Demonstrate at the configured cycle. Get the real-time option in writing |
| Pellworth | Service suspension for non-payment beyond 30 days could stop dispatch during an invoice dispute | Low | High | Remove the clause or require notice and exclude disputed amounts |
| Pellworth | Lock-in: three-year minimum, 6% uplift floor, native-format export for only 30 days | High | High | Pass, or rewrite the exit and uplift terms |
| Pellworth | Support Mon-Fri 08:00-18:00, Irish holidays, while no Northvale site is in Ireland | High | Medium | Pass, or extend hours to match operating hours |

### Strengths

**Meridian**
- The most mature-sounding platform: 400+ implementations, 60+ carrier connectors and 200+ standard reports (A4, A6, A15).
- Highest stated availability that is actually measured (99.7% monthly), with a 1-hour Sev 1 response and follow-the-sun support (A8, A11-A12).
- ISO 27001, and hosting named in Frankfurt and Amsterdam (A14, A27).
- A shorter rollout than Hartlowe, about 44 weeks for all four sites (A7).

**Hartlowe**
- Turns the 48-hour requirement into a measurement Northvale can audit. It is available from day one, gives raw data free, and is honest that the result is Northvale's (B2-B4). This is the problem stated in RFQ 1.3.
- The strongest commercial certainty: fixed-price ERP and carrier integration, two change requests included, and two trial migrations (B5-B7).
- Availability is measured the way RFQ 3.6 is worded (operating hours, including maintenance), with defined credits (B9-B10).
- The best exit and data protection: a free full export with schema, a £750,000 liability floor, uncapped liability for data loss, and no move outside the EU without consent (B16-B17, B22).
- Delivery risk is controlled: employees only, with named and locked key staff (B24-B25). On-site training for all 120 users with a refresher (B15).
- Uplift capped at CPI or 4% (B20).

**Calderon**
- Claims real-time multi-site stock visibility and all major handheld platforms (C3-C4).
- Unlimited digital training for all licensed users, and a named Customer Success Manager (C13, C15).
- A fast first go-live claim of 22 weeks (C10).

**Pellworth**
- Explicitly configures the 14:00 order cut-off (D2).
- Offers a reference visit, the only vendor to do so (D24).
- The shortest first-site timetable, 20 weeks (D8).

### Concerns

**Meridian**
- Every commitment that matters is generic or deferred: "full functional coverage", "fully supported", MSA "on request" (A1, A16, A23).
- Pushes data extraction and quality, ERP-side endpoints and training for 120 users back onto Northvale (A3, A5, A13).
- Credits only come with a paid support tier. Uplift is uncapped. Maintenance is excluded from availability (A8, A10, A21).
- Delivery partners and sub-processors are not identified. Liability is capped at 12 months' fees (A24, A28-A29).

**Hartlowe**
- Price validity lapsed around 10 September 2026 (B21).
- The longest timetable (B8). Support is thinner on Sundays and at night (B14). Credits are not automatic (B11).
- The returns exception (£84,000) and no hardware (B26-B27). Supervisors are not explicitly covered in training (B15).
- The dispatch measure runs from "received into the system". That needs to match Northvale's 14:00 cut-off rule and the time the order enters the ERP, not the WMS (B2).
- No roadmap commitments (B29). References not offered.

**Calderon**
- Says it meets section 3 (C1) but lists enhanced dispatch performance analytics and multi-site labour planning as future releases (C18-C19).
- Nothing is priced firmly. Implementation is T&M, integration is scoped after award, carriers go through partners, and uplift is unstated (C7-C8, C23-C24).
- SLA, liability, exit, security certification and delivery team are absent or in documents not supplied (C14, C25-C26).
- Availability is a "target" with no basis or remedy (C12).

**Pellworth**
- No ISO 27001, and the hosting provider is not named (D13, D22).
- The price excludes migration, a carrier, on-site training and discovery. The ERP integration effort is unknown (D5-D7, D18).
- The uplift floor is 6%, compounding. There is a three-year minimum. Liability is 50% of 12 months' fees. There is a suspension right. Exit is poor (D16-D21).
- Availability is measured annually. Support is weekday-only on an Irish holiday calendar. Severity terms can be changed at will (D9-D11).
- Stock sync every 15 minutes. Android 11+ only. No named people (D3-D4, D15).

### Recommendation

| Vendor | Verdict | Reasoning |
|---|---|---|
| **Hartlowe** | **Negotiate** (preferred) | The only response that commits in terms Northvale can enforce against RFQ 3.1, 3.6 and 3.7, with the best cost certainty and exit position. It is not "Proceed" yet because its price has lapsed, the pricing schedule is not in the pack, and the returns, support-hours and hardware points need closing. |
| **Meridian** | **Negotiate** (keep as competitor) | A capable platform with a credible support model, but its commitments cannot be enforced as written. Keep it in the process to hold Hartlowe to a competitive price, and give it the chance to convert its generic claims into Hartlowe-level commitments. |
| **Calderon** | **Pass** | Its own roadmap contradicts its claim to meet the dispatch requirement, and it cannot be evaluated on RFQ 5.1 cost or capability without documents it did not supply. Reconsider only if it resubmits with a fixed price and contractual SLA, liability and exit terms. |
| **Pellworth** | **Pass** | Fails on security certification, lock-in, uplift, support coverage and exit. Its headline price leaves out most of the real scope. |

The five-year total required by RFQ 5.1 cannot be compared until Hartlowe's and Meridian's pricing schedules are available side by side. The ranking above could still change if the price gap between them is large.

### Negotiation Points

**Hartlowe**
- Reconfirm the fixed implementation price in writing with a new validity date that covers the sign-off timetable. Use Meridian as the alternative.
- Define "Northvale operating hours" in the contract (B9, B14). Extend full support to all operating hours, or at least cover Sev 2 on Saturday.
- Make service credits apply automatically, or extend the 30-day claim window (B11).
- Returns: confirm whether three-tier inspection is actually needed. If it is, negotiate the £84,000 down or into the fixed price. If it is not, descope it in writing (B26).
- Tie the dispatch report to the 14:00 cut-off and to order receipt in the ERP, and include it in integration acceptance testing (B2-B3).
- State supervisor training (14) explicitly alongside the 120 users (B15).
- Price extra concurrent licences in advance and allow a peak-season margin above 85 (B19).
- Ask for 6-week site intervals, their stated floor, to shorten the rollout from about 55 to about 49 weeks (B8).
- Make successor co-operation (B18) free for a defined number of days. Ask for two customer references.

**Meridian**
- Put service credits in the standard support tier (A10). Measure availability during operating hours, including maintenance (A8-A9).
- Cap the annual uplift at the lower of CPI or 4%, matching Hartlowe (A21). Set the minimum at the actual count of 134 users, not 140 (A20).
- State in the fixed price who builds the ERP-side endpoints, and confirm that all three Northvale carriers are pre-built (A3-A4).
- Take on data-quality remediation and trial migrations. Train all 120 users, or credit the internal cost (A5, A13).
- Provide the MSA, the sub-processor list, the non-EU access position and the delivery partner names before shortlisting. Name the key staff (A23, A28-A29).
- Raise liability above 12 months' fees and carve out data loss (A24). Define exit export format, timing and cost (A26).
- Commit to regression testing Northvale's integrations for each release (A18-A19). Name reference customers with comparable dispatch commitments (A2).

**Calderon** (only if it resubmits)
- Contractually commit to dispatch performance measurement at go-live, not Q1 2027 (C18).
- Convert T&M to a fixed price after a capped discovery (C7, C24). Provide appendices 1, 2 and 5 and the Service Description (C14, C22, C25).

**Pellworth** (only if it resubmits)
- Provide ISO 27001 or an equivalent independent attestation, and name the cloud provider and region (D13, D22).
- Replace the uplift with the lower of CPI or 4% and remove the three-year minimum (D16-D17). Remove the suspension right (D20). Offer a free export with schema (D21).
- Include migration, the third carrier, discovery and on-site training in a fixed price (D18).
