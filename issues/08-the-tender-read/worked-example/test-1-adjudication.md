# Test 1: adjudicating the 40 flags

*The 40 flags in `review-check-one-instruction.md` were judged by a separate Claude session, told to be adversarial toward the checker. It read only the review, the bid pack and the flags. Run on 29 September 2026, unedited apart from dash style. It is a model's judgement too: read the flags your decision rests on with the clause open.*

**Result:**
- **Holds:** 11.
- **Holds in part:** 19.
- **Does not hold:** 10.
- **Material to the decision:** 4, all missed by the first hand-built check.

---

# Adjudication of the 40 qualification flags: Vendor Review, RFQ NV-2026-114

Sources read: review.md, bid-pack.md, baseline-output.md only. No web.

| ID | Verdict | Materiality | Reason |
|---|---|---|---|
| A1 | HOLDS | MATERIAL | C18 puts only *enhanced* analytics on the roadmap, and the Summary, Risk ("only"), Recommendation and Negotiation lines turn that into a proven contradiction of C1, which is the lead stated ground for Pass; the flag leaves out that the Concerns line also keeps "enhanced", and Pass would probably survive on C7, C14 and C24 anyway. |
| A2 | PARTLY HOLDS | MATERIAL | The review never mentions B23, and the consequential-loss exclusion really does limit what the "uncapped data loss" carve-out is worth, so it belongs in the Hartlowe negotiation list; but "caused by Hartlowe" is implicit in any liability carve-out, and Hartlowe is still the best of the four on liability, so the ranking is not overstated. |
| A3 | PARTLY HOLDS | MINOR | The Concerns and Risk lines state as fact that the ERP-side endpoints fall on Northvale, which A3 leaves open; but the review's own matrix says "owner unclear" and its negotiation point asks the right question, so the harm is small. |
| A4 | PARTLY HOLDS | MINOR | "Paid tier" and "add-on" read more into A10 than it says, but a named Enhanced tier above a standard one is a fair inference; the flag's claim that the review plays down "can be discussed" is wrong, because the matrix quotes it and the checker's own section D lists A10 as correctly reported. |
| A5 | DOES NOT HOLD | MINOR | A21 ties the uplift to the vendor's own rate card and states no ceiling, so "uncapped and set by the vendor" is an accurate reading, not an unsupported conclusion. |
| A6 | PARTLY HOLDS | MINOR | "Most of the scope" overstates D18, but less than the flag says: migration, the third carrier, on-site training, discovery *and* the ERP integration effort (D5) all sit outside the fixed price, and Pass does not depend on the wording. |
| A7 | PARTLY HOLDS | MINOR | The Concerns line does drop "default" and "configurable", and there is no "real-time option" in D3; but the flag cuts the Risk mitigation short, and that mitigation opens with "Demonstrate at the configured cycle", which acknowledges configurability. |
| A8 | HOLDS | MINOR | A7, B8 and D8 are all "indicative", and the review never says so where it compares rollouts; because all three carry the same qualifier, the relative ranking barely moves. |
| A9 | PARTLY HOLDS | MINOR | C11 ("subsequent sites will follow") plainly staggers, and D8's "to first site" implies later sites; only Pellworth's staggering is an inference, and the flag wrongly treats a missing interval as missing staggering. |
| A10 | PARTLY HOLDS | MATERIAL | Appendices 1, 2 and 5 are part of Calderon's 76-page response and are only missing from the extract, so "documents it did not supply" and "Provide appendices 1, 2 and 5" misstate the position and weaken a Pass ground; the separate Service Description (C14) is, however, fairly called not supplied. |
| A11 | PARTLY HOLDS | MINOR | A14 is a specific, testable EU-hosting statement, so "only" is too strong for 3.7; but the 3.1 half is weak, because the review's "commits against 3.1" means the measurement support that B2-B3 do commit to. |
| B1 | DOES NOT HOLD | MINOR | No reader takes "from day one" for a dispatch report to mean before go-live; the flag invents a misreading. |
| B2 | HOLDS | MINOR | "Locked" drops B25's termination-of-employment exception; the exception is standard key-person wording, but it is worth closing in negotiation. |
| B3 | PARTLY HOLDS | MINOR | Migration being fixed price is a fair inference from B21, since migration is implementation scope; but the matrix does drop "full" and "by the date in the project plan" from Northvale's extract obligation, and that dependency is real. |
| B4 | PARTLY HOLDS | MINOR | B19 does not say "shift overlap", and the RFQ gives no concurrency figures; still, 85 concurrent against about 134 people implies overlap, and the review's action ("confirm the peak") is the right one. |
| B5 | HOLDS | MATERIAL | Hartlowe states selected terms (B17-B23) but not its standard terms under RFQ 4.3; the review marks it as complete while criticising Meridian's MSA on request, and it never asks the preferred vendor for its full terms before contract. |
| B6 | DOES NOT HOLD | MINOR | B9 does use RFQ 3.6's own words ("during operating hours"), maintenance inside those hours logically counts, and the claim-in-writing condition is stated in the matrix, in Concerns ("not automatic") and in a negotiation point. |
| B7 | PARTLY HOLDS | MINOR | The Strengths line drops the maintenance exclusion, which the matrix, Risk and Negotiation lines keep; but the charge of an inconsistent "target" test is weak, because A8 says Meridian "commits to" a measured target, while Calderon is marked down for having no basis or remedy, not for the word. |
| B8 | HOLDS | MINOR | "Every commitment that matters" is contradicted by specific Meridian terms (A8, A12, A14, A27), some of which the review itself lists as Strengths. |
| B9 | HOLDS | MINOR | Only A23 and A26 are "on request"; "mostly" overstates the bid. |
| B10 | HOLDS | MINOR | A28 names a published sub-processor register, so "not identified" is wrong for sub-processors, although it is right for delivery partners (A29). |
| B11 | PARTLY HOLDS | MINOR | "No ISO 27001" is factually right, and the matrix keeps "being pursued"; the review never claims that security certification or support hours are RFQ requirements, although "Fails on" does read like pass/fail against criteria the RFQ does not set. |
| B12 | PARTLY HOLDS | MINOR | "At will" is an inference, but a fair one, since D11's handbook is Pellworth's own document, "updated from time to time", with no consent or notice mechanism. |
| B13 | HOLDS | MINOR | D4 is a compatibility statement, and the review labels the same silence "Not stated" for A and C but "Excluded in effect" for D; the Notes column ("budget separately whoever wins") limits the harm. |
| B14 | DOES NOT HOLD | MINOR | "Not yet chosen" against "confirmed at contract stage", and "No named people" against "unable to name… at this stage", are faithful paraphrases; this is hair-splitting. |
| B15 | PARTLY HOLDS | MINOR | "In every case" is not stated for C9 or D7, but given RFQ 1.2 (the legacy experts have left) it is a sound planning assumption rather than a misreading. |
| B16 | DOES NOT HOLD | MINOR | C9 makes migration a Calderon-led implementation workstream, and C24 prices implementation on T&M, so the reading is direct, not a stretch. |
| B17 | PARTLY HOLDS | MINOR | The Negotiation line does harden RFQ 2.4's "approximately" into "the actual count of 134"; but the matrix says "implies" and the Risk table correctly says "the actual user count", so the correct position is already in the review. |
| C1 | HOLDS | MINOR | The review nowhere mentions that A13 supplies training materials; the burden of training still falls on Northvale. |
| C2 | PARTLY HOLDS | MINOR | "Expected" is softer than "must", but with support limited to 18 months the practical effect is the same, so the hardening is a fair inference. |
| C3 | DOES NOT HOLD | MINOR | Under A18 releases are delivered to all customers automatically, so GA and adoption coincide, and the flag's "shorter effective window" has no basis. |
| C4 | HOLDS | MINOR | The five-day notice in A9 is cited but never described; it does not cure the concern that maintenance can fall in operating hours. |
| C5 | PARTLY HOLDS | MINOR | The Strengths line drops "hosting operations"; the matrix keeps it, and the contrast with B28 is visible there. |
| C6 | DOES NOT HOLD | MINOR | Follow-the-sun coverage cannot be delivered from EU time zones alone, the review words it as an implication, and the Risk and Negotiation lines treat it as a question to confirm, which is exactly what the flag asks for. |
| C7 | PARTLY HOLDS | MINOR | B20 and D17 are not limited to licence fees, so "licence spend" narrows the base; the percentage effects are unchanged, and the comparison between vendors is unaffected. |
| C8 | HOLDS | MINOR | RFQ section 3 has no labour-planning requirement, so putting C19 next to C1 implies a contradiction that does not exist. |
| C9 | DOES NOT HOLD | MINOR | "A suspension right" in the Summary is accurate shorthand, and the trigger is given in the matrix and Risk table; nothing is overstated. |
| C10 | DOES NOT HOLD | MINOR | "Capped at CPI or 4%" is not wrong, and the flag itself concedes that the matrix states "lower of" correctly. |
| C11 | PARTLY HOLDS | MINOR | Neither bid names a commercial schedule, so their existence is assumed; this is harmless, but it sits oddly next to the review telling Calderon it "did not supply" its appendices (see A10). |
| C12 | DOES NOT HOLD | MINOR | The review hedges with "~" and "about", any earlier response date would only make the lapse earlier, and the flag concedes the point is fair. |

## Totals

- **HOLDS:** 11 (A1, A8, B2, B5, B8, B9, B10, B13, C1, C4, C8)
- **PARTLY HOLDS:** 19 (A2, A3, A4, A6, A7, A9, A10, A11, B3, B4, B7, B11, B12, B15, B17, C2, C5, C7, C11)
- **DOES NOT HOLD:** 10 (A5, B1, B6, B14, B16, C3, C6, C9, C10, C12)
- **MATERIAL among HOLDS:** 2 (A1, B5). Among all flags, 4 are MATERIAL (A1, A2, A10, B5).

## The five most material flags that hold

Only two flags both fully hold and are material, so the list goes on with the strongest material partly-holds and then the most consequential minor hold.

1. **A1 (HOLDS, MATERIAL).** Calderon's "contradiction" rests on dropping "enhanced" from C18 and adding "only". The lead ground for Pass should be restated as an open question to Calderon. The verdict itself probably stands on T&M pricing, scoping after award and the missing SLA terms.
2. **B5 (HOLDS, MATERIAL).** The preferred vendor's full standard terms have not been seen, and the review does not ask for them. They should go on the Hartlowe negotiation list before contract.
3. **A2 (PARTLY HOLDS, MATERIAL).** B23's exclusion of consequential loss is never mentioned. It sits alongside the uncapped data-loss carve-out and should be negotiated. The "caused by Hartlowe" half of the flag carries no weight.
4. **A10 (PARTLY HOLDS, MATERIAL).** Calderon's appendices are missing from the extract, not from the bid. Northvale should pull them from the full 76-page response before relying on "cannot be evaluated" as a reason to pass.
5. **A8 (HOLDS, MINOR).** Every rollout comparison rests on indicative timetables. Committed milestones are not asked of anyone, and they belong in the contract whoever wins.

## Errors in the checker itself

- **A4:** the flag says the review plays down "can be discussed", but the checker's own section D lists A10 "can be discussed" as correctly reported.
- **A7:** the flag quotes the Risk mitigation without its first sentence, "Demonstrate at the configured cycle", which is the part that answers the flag.
- **A9:** the flag treats a missing interval as a missing stagger, although C11 plainly staggers.
- **B1, B14, C3, C10, C12:** these are paraphrase-level objections that no reasonable reader would take as errors. C10 and C12 are conceded as fair within the flags themselves.
- **A5:** the flag argues that a vendor-controlled rate card with no stated ceiling is not "uncapped", which is not a tenable reading.
