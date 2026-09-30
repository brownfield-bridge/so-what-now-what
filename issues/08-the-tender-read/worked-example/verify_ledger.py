# Concepts, logic, and instructions by Jacek Kieszkowski.
# Claude used as editing and scaffolding tool.
# Third-party sources referenced in SOURCES.md.
"""
verify_ledger.py - rebuilds the worked-example ledger and checks it.

WHAT IT CHECKS: quotation accuracy and arithmetic.
  - every quote, and every recorded condition or exception, appears character
    for character inside the clause it cites in bid-pack.md;
  - every clause has at least one finding or a stated reason for none;
  - every count is computed from the ledger alone.

WHAT IT DOES NOT CHECK: whether each finding is classified correctly, whether
a condition was missed, or whether anything was left out. A quote can be
accurate and the reading still incomplete. That review is a person's job, and
the `condition` column is there so exceptions are visible when you do it.

It also checks Stage 1 (the request against the standing checklist), Stage 2
(the relief list), the check of the AI review, the clarification letter,
and the register and its pre-mortem the same way: every quote must be
found in the request or the response it cites, every checklist line must carry
a mark, and every count is computed here, not typed.

Run:  python verify_ledger.py
"""
import csv, re, sys, os, collections

HERE = os.path.dirname(os.path.abspath(__file__))
PACK = os.path.join(HERE, "bid-pack.md")
CHECKLIST = os.path.join(HERE, "..", "standing-checklist.md")

# (clause, category, commitment_key, verbatim quote)
# OBL = obligation, TERM = term, EXCL = declared exclusion, SIL = silence
F = [
# ---------------- A Meridian ----------------
("A1","SIL","functional_fit","confirms full functional coverage of the scope"),
("A2","SIL","dispatch_48h","supports high-velocity dispatch operations including same-day and 48-hour dispatch workflows"),
("A3","OBL","erp_integration_standard_interface","will deliver a standard ERP integration using our published REST interface"),
("A4","SIL","carrier_integration","pre-built connections to more than sixty carriers"),
("A5","OBL","data_migration","will migrate stock records, location data and open orders"),
("A5","EXCL","data_migration","The customer is responsible for data extraction and data quality."),
("A6","SIL","implementation_method","a proven five-phase approach refined across more than 400 implementations"),
("A7","SIL","timetable","Indicative timetable: 26 weeks"),
("A8","SIL","availability","commits to a platform availability target of 99.7%"),
("A8","EXCL","availability","excluding planned maintenance"),
("A9","OBL","maintenance_notice_5d","Planned maintenance windows are notified not less than five working days in advance."),
("A10","SIL","service_credits","can be discussed as part of commercial negotiation"),
("A11","SIL","support_hours","follow-the-sun coverage"),
("A12","OBL","sev1_response_1h","Severity 1 incidents receive a response within one hour."),
("A13","OBL","training_supervisors","will provide a train-the-trainer programme covering 14 supervisor users"),
("A13","EXCL","training_all_users","Onward training of warehouse users is delivered by the customer"),
("A14","OBL","data_in_eu","hosted in our Frankfurt and Amsterdam regions"),
("A15","SIL","reporting","more than 200 standard reports and a self-service report builder"),
("A16","SIL","dispatch_measurement","Performance measurement against dispatch commitments is fully supported"),
("A17","SIL","scalability","architected for scale and additional sites can be onboarded rapidly"),
("A18","TERM","release_policy","New functionality is delivered to all customers automatically."),
("A19","OBL","release_support_18m","Releases are supported for 18 months from general availability."),
("A19","TERM","release_policy","Customers are expected to remain on a supported release."),
("A20","TERM","licensing","per named user per annum, with a minimum commitment of 140 users"),
("A21","TERM","indexation","Annual licence uplift is applied each year in line with our published rate card."),
("A22","TERM","implementation_price","Implementation is quoted as a fixed price based on the scope as understood"),
("A23","TERM","contract_terms","standard Master Services Agreement applies"),
("A23","SIL","contract_terms","A copy is available on request."),
("A24","TERM","liability_cap","limit liability to the fees paid in the preceding twelve months"),
("A25","SIL","partnership","committed to a long-term partnership with Northvale and to your continued success"),
("A26","SIL","exit_data","Customer data may be exported on request in a standard format."),
("A27","OBL","iso27001","maintains ISO 27001 certification across our hosting operations"),
("A28","OBL","subprocessor_register","Sub-processors are listed in our published sub-processor register."),
("A29","SIL","subcontracting","drawn from Meridian's delivery organisation and approved delivery partners"),
("A30","SIL","other","We would be pleased to discuss any specific requirements not addressed above."),
# ---------------- B Hartlowe ----------------
("B1","OBL","deliver_scope","Hartlowe will deliver the scope in section 2"),
("B2","OBL","dispatch_elapsed_report","will report elapsed time between those two events per order line"),
("B3","OBL","dispatch_report_day_one","available as a standard report from day one of each site go-live"),
("B3","OBL","raw_data_export_free","raw order-level data is exportable in CSV without charge at any time"),
("B4","EXCL","dispatch_48h","Hartlowe makes no commitment as to whether Northvale achieves 48-hour dispatch."),
("B5","OBL","erp_integration_confirmed_version_tested_jointly","ERP integration will be built by Hartlowe against the ERP version Northvale confirms, tested jointly"),
("B5","TERM","implementation_price","Two integration change requests are included in the implementation fee."),
("B6","OBL","carrier_integration_all_three","Carrier integrations to Northvale's three carriers are included"),
("B6","TERM","carrier_price","Additional carriers are quoted at £6,500 each."),
("B7","OBL","data_migration","Hartlowe will perform data migration."),
("B7","SIL","data_migration","in an agreed format by the date in the project plan"),
("B7","OBL","trial_migrations","Hartlowe will run two trial migrations before cutover."),
("B8","SIL","timetable","Indicative timetable: 31 weeks"),
("B8","EXCL","timetable","Hartlowe will not compress site go-lives below 6 weeks."),
("B9","OBL","availability_incl_maintenance","99.5% measured monthly during Northvale's operating hours, including all maintenance"),
("B10","TERM","service_credits","Northvale may claim a credit of 5% of that month's support fee per 0.1% shortfall"),
("B11","TERM","service_credits","Hartlowe does not apply credits automatically."),
("B12","OBL","sev1_response_1h","Severity 1: response within 1 hour"),
("B12","OBL","sev1_restoration_8h","restoration or documented workaround within 8 working hours"),
("B13","OBL","sev2_response_4h","Severity 2: response within 4 hours"),
("B13","OBL","sev2_resolution_5d","resolution within 5 working days"),
("B14","OBL","support_hours_mon_sat","Support hours are 06:00 to 20:00 CET Monday to Saturday."),
("B14","OBL","sev1_oncall","an on-call number is provided for Severity 1 only"),
("B15","OBL","training_all_users","will train all 120 warehouse users on site"),
("B15","OBL","training_refresher","will provide refresher training at 90 days after each go-live"),
("B16","OBL","data_in_eu","Hosting is in Frankfurt."),
("B16","OBL","no_data_move_without_consent","will not move Northvale data outside the European Union without 90 days written notice and Northvale's consent"),
("B17","OBL","exit_export_free","complete data export in CSV and in the documented database schema, within 15 working days, at no charge"),
("B18","OBL","successor_cooperation","co-operation to a successor supplier for 90 days after termination"),
("B18","SIL","successor_cooperation","reasonable co-operation"),
("B18","TERM","successor_cooperation","chargeable at our standard day rate"),
("B19","TERM","licensing","Licensing is per concurrent user."),
("B19","SIL","licensing","Northvale's stated volumes indicate 85 concurrent licences."),
("B20","TERM","indexation","Annual uplift is the lower of CPI or 4%"),
("B21","TERM","implementation_price","The price is valid for 90 days from the date of this response."),
("B22","TERM","liability_cap","limit liability to the greater of £750,000 or the fees paid in the preceding twelve months"),
("B22","TERM","data_loss_uncapped","Liability for loss of or corruption of Northvale data caused by Hartlowe is not subject to that cap."),
("B23","TERM","consequential_loss","Indirect and consequential loss is excluded."),
("B24","OBL","no_subcontracting","Hartlowe does not sub-contract implementation."),
("B25","OBL","named_personnel","will name the implementation lead and two senior consultants in the contract"),
("B25","OBL","no_replacement_without_consent","will not replace them without Northvale's written agreement"),
("B26","EXCL","returns","three-tier returns inspection is not supported without development, quoted separately at £84,000"),
("B27","EXCL","hardware","Hartlowe does not provide handheld hardware."),
("B27","OBL","device_support","We support the two device families listed in appendix 4."),
("B28","OBL","iso27001","holds ISO 27001 for its hosting and development operations"),
("B29","OBL","roadmap_published","product roadmap is published to customers quarterly"),
("B29","EXCL","roadmap_dates","Hartlowe does not commit to roadmap dates in contract."),
# ---------------- C Calderon ----------------
("C1","SIL","functional_fit","meets the requirements of section 3"),
("C2","SIL","dispatch_48h","readily supports 48-hour and shorter dispatch cycles"),
("C3","SIL","stock_visibility","Real-time multi-site stock visibility is a core capability"),
("C4","SIL","device_support","fully supported across all major handheld device platforms"),
("C5","SIL","reporting","comprehensive operational reporting out of the box"),
("C6","OBL","erp_integration_via_platform","Integration with the customer's ERP will be achieved through our integration platform"),
("C6","SIL","erp_integration","supports all common enterprise systems"),
("C7","SIL","erp_integration","scoping will be undertaken during the discovery phase following contract award"),
("C8","SIL","carrier_integration","delivered via our logistics partner ecosystem"),
("C9","OBL","data_migration","Calderon will lead the data migration workstream"),
("C10","SIL","timetable","Our proposed timetable is 22 weeks to first go-live"),
("C11","SIL","timetable","accelerated template approach"),
("C12","SIL","availability","Calderon targets 99.9% platform availability"),
("C13","SIL","support_hours","proactive service management and a named Customer Success Manager"),
("C14","SIL","sev1_response_1h","Incident response times are set out in our Service Description document."),
("C15","OBL","training_academy_access","unlimited access for all licensed users"),
("C16","OBL","training_supervisors","Supervisor enablement sessions are delivered on site during each go-live."),
("C17","OBL","data_in_eu","EU data residency is available and will be configured for Northvale."),
("C18","SIL","dispatch_measurement","Enhanced dispatch performance analytics are on our published roadmap for release in Q1 2027."),
("C19","SIL","roadmap_dates","scheduled for the following release"),
("C20","SIL","scalability","invests over 18% of revenue in research and development"),
("C21","TERM","licensing","Licensing is per site plus a volume-based transaction component."),
("C22","TERM","licensing","Transaction volumes above the contracted band are charged at the rates in appendix 2."),
("C23","TERM","indexation","Annual increases are applied in accordance with our standard commercial terms."),
("C24","TERM","implementation_price","quoted on a time and materials basis"),
("C24","SIL","implementation_price","an indicative estimate provided in appendix 1"),
("C25","TERM","contract_terms","standard terms and conditions apply"),
("C25","SIL","contract_terms","a summary of which is at appendix 5"),
("C26","SIL","subcontracting","will confirm the delivery model at contract stage"),
("C27","SIL","partnership","the strongest strategic fit for Northvale's ambitions"),
("C28","SIL","other","would welcome the opportunity to discuss commercial flexibility"),
# ---------------- D Pellworth ----------------
("D1","OBL","deliver_scope","will supply and implement the Pellworth WMS in accordance with section 2"),
("D2","SIL","dispatch_48h","The platform handles dispatch scheduling"),
("D2","OBL","cutoff_configured","will be configured to reflect Northvale's 14:00 order cut-off"),
("D3","OBL","stock_sync_15min","The default cycle is 15 minutes and is configurable."),
("D4","OBL","device_support","supported on Android devices running version 11 or later"),
("D5","OBL","erp_integration_scope_after_workshop","Pellworth will build the ERP integration."),
("D5","EXCL","erp_integration","confirmed following a chargeable discovery workshop"),
("D6","OBL","carrier_integration_two","Two carrier integrations are included."),
("D6","EXCL","carrier_integration","The third will be quoted following review"),
("D7","EXCL","data_migration","Data migration is provided as an optional service and is not included in the price"),
("D8","SIL","timetable","Indicative timetable: 20 weeks to first site."),
("D9","SIL","availability","Availability target is 99.5% measured annually."),
("D10","OBL","support_hours_mon_fri","Support is provided 08:00 to 18:00 CET Monday to Friday"),
("D11","SIL","sev1_response_1h","contained in our support handbook, which is updated from time to time"),
("D12","OBL","training_remote","Training is delivered remotely."),
("D12","EXCL","training_all_users","On-site training is available at additional cost."),
("D13","OBL","data_in_eu","Hosting is provided on a major public cloud in an EU region."),
("D14","SIL","subcontracting","The partner will be confirmed at contract stage."),
("D15","EXCL","named_personnel","Pellworth is unable to name individual consultants at this stage."),
("D16","TERM","licensing","Licensing is per named user with a three-year minimum term."),
("D17","TERM","indexation","Annual uplift is 6% or CPI, whichever is higher."),
("D19","TERM","liability_cap","limit liability to 50% of the fees paid in the preceding twelve months"),
("D20","TERM","suspension_right","reserves the right to suspend the service in the event of non-payment beyond 30 days"),
("D21","OBL","exit_data_30d","customer data is made available for 30 days in Pellworth's native export format"),
("D21","EXCL","exit_data","Extraction assistance is chargeable."),
("D22","OBL","iso9001","Pellworth holds ISO 9001."),
("D22","EXCL","iso27001","ISO 27001 certification is being pursued."),
("D23","SIL","partnership","long-established provider with deep sector knowledge"),
("D24","SIL","other","would be pleased to arrange a reference visit"),
]
# Conditions and exceptions that qualify a finding, quoted verbatim from the same clause.
# A commitment read without its exception is a misreading, however accurate the quote.
CONDITIONS = {
    ("B25","no_replacement_without_consent"): "except on termination of employment",
    ("B14","sev1_oncall"): "for Severity 1 only",
    ("B10","service_credits"): "to a maximum of 30% of the monthly fee",
    ("B11","service_credits"): "in writing within 30 days",
    ("B18","successor_cooperation"): "for 90 days after termination",
    ("B21","implementation_price"): "valid for 90 days",
    ("B3","raw_data_export_free"): "without charge at any time",
    ("D10","support_hours_mon_fri"): "excluding public holidays in the Republic of Ireland",
    ("D21","exit_data_30d"): "for 30 days",
    ("A8","availability"): "measured monthly",
    ("D9","availability"): "measured annually",
    ("B22","data_loss_uncapped"): "caused by Hartlowe",
}
# Clauses that yield no finding, with the reason, so absence is visible too.
NO_FINDING = {"D18": "Restates the exclusions already recorded at D5, D6, D7 and D12; not counted twice."}

# ---------------- STAGE 1: the request against the standing checklist ----------------
# Every checklist line not listed here is NOT ANSWERED. Each mark cites the request
# clause and quotes it; the reason says what the clause leaves open.
STAGE1 = [
("A2","PARTIAL","1.3","orders received before 14:00 will be dispatched within 48 hours","Names a cut-off, but not which system event starts the clock or what counts as dispatched."),
("A3","PARTIAL","1.3","We have committed to our three largest customers","Says whose orders the commitment covers; not what share of volume the system's service level must bind."),
("A4","ANSWERED","2.1","across all four sites","Scope by site and function is stated (with 1.1 naming the sites)."),
("B1","PARTIAL","3.4","The system must provide reporting on warehouse performance.","Implies the new system produces the figures; whether they sit on a record the buyer controls is not stated."),
("B3","PARTIAL","3.4","The system must provide reporting on warehouse performance.","Reporting is required; frequency, format and access to raw records are not."),
("C1","PARTIAL","1.1","approximately 11,000 active stock keeping units","A size is given; no volume band is tied to the price or the service level."),
("D1","PARTIAL","4.3","Please state your standard contract terms.","Raises which conditions govern and leaves the answer to each supplier."),
("D7","PARTIAL","4.3","Please state your standard contract terms.","Asks for the supplier's position and states none of its own."),
("E1","PARTIAL","4.1","Please provide licence costs, implementation costs and annual support costs separately.","Asks for three cost lines; the charging basis of each is not defined."),
("F1","PARTIAL","2.2","Integration with our existing ERP (finance and order management) and with three carrier systems.","Integrations are in scope; who builds them and who pays when they change is not stated."),
("F4","PARTIAL","3.2","The system must give us accurate stock visibility across all four sites.","Visibility is required; live data versus reports, and how accuracy is measured, are not."),
("I3","PARTIAL","3.7","Data must be held within the European Union.","One requirement is stated; who evidences compliance is not."),
]
CORE_TWELVE = ["A2","A3","A5","B1","B4","C2","D1","D3","D7","E3","G1","H2"]

# ---------------- STAGE 2: the relief list ----------------
# Twenty things a capable supplier would be relieved the request did not ask.
# Where the request comes close, the nearest clause is quoted to show why it
# does not cover the item.
RELIEF = [
("What event starts the dispatch clock in the system, and what event stops it","1.3","orders received before 14:00 will be dispatched within 48 hours"),
("Which system of record produces the dispatch performance figure","1.3","We currently measure this manually"),
("A stock accuracy figure, and how accuracy is measured","3.2","accurate stock visibility"),
("Maximum acceptable latency for cross-site stock visibility",None,None),
("An availability percentage, and over what window","3.6","must be available during our operating hours"),
("Whether availability is measured including or excluding planned maintenance",None,None),
("Whether service credits exist, and whether they are applied automatically",None,None),
("Restoration targets by severity, not only response targets","2.5","Support from go-live."),
("Support hours expressed in the time zones of all four sites",None,None),
("Data export format, timeframe and cost at exit",None,None),
("Who owns the operational data, and whether extraction is chargeable",None,None),
("A cap on the annual licence uplift","4.1","annual support costs separately"),
("How long the quoted price remains valid",None,None),
("What is excluded from the quoted price",None,None),
("Whether implementation is fixed price or time and materials","4.1","implementation costs"),
("Named individuals, and what happens when they leave",None,None),
("Whether implementation is sub-contracted, and to whom",None,None),
("The liability cap, and whether loss of data is carved out of it","4.3","Please state your standard contract terms."),
("Release policy: whether the customer can be forced to upgrade",None,None),
("Whether any required capability is not yet built",None,None),
]
# Things the request does ask. They are listed for contrast and are not reliefs.
ASKED = [
("Data residency","3.7","Data must be held within the European Union."),
("Three carrier integrations","2.2","three carrier systems"),
("Training volumes","2.4","approximately 120 warehouse users and 14 supervisors"),
("Migration of stock records, locations and open orders","2.3","Migration of current stock records, locations and open orders."),
]

# ---------------- STAGE 5: the register ----------------
# Fictional award to A. The five claims its scoring leaned on.
# (clause, quote, what you would observe, when, record, verdict)
REGISTER = [
("A16","Performance measurement against dispatch commitments is fully supported","A dispatch performance report you can run in your own tenant","Go-live","Your own tenant: you run the report","CHECKABLE"),
("A7","Indicative timetable: 26 weeks from contract signature to first site go-live","The actual first go-live date. Offered as indicative, so checkable but not binding","First go-live","Your project record","CHECKABLE"),
("A2","supports high-velocity dispatch operations including same-day and 48-hour dispatch workflows","Only that dispatch workflows exist, which any such system has. Nothing would show whether they meet the 48-hour commitment the request asked about","None","None","CANNOT BE CHECKED"),
("A8","platform availability target of 99.7% measured monthly, excluding planned maintenance","Monthly availability, but only as the supplier reports it, with maintenance removed first","First service review","Supplier reporting only","CANNOT BE CHECKED"),
("A25","committed to a long-term partnership with Northvale and to your continued success","Nothing","None","None","CANNOT BE CHECKED"),
]

# Pre-mortem for the checkable claims: it is the milestone and the claim failed.
# Each cause cites the clause that would produce it. The odds are the buyer's
# to set and are never written here.
# (claim, cause, "RFQ" or "BID", clause, verbatim quote)
PREMORTEM = [
("A7","Data extraction from a legacy system no one left in the business understands, and it is Northvale's job","RFQ","1.2","The two people who understood it have left the business."),
("A7","","BID","A5","The customer is responsible for data extraction and data quality."),
("A7","Anything outside the scope as A understood it goes through change control","BID","A22","Changes to scope are handled through our change control process."),
("A7","A slip costs A nothing: the timetable is offered as indicative","BID","A7","Indicative timetable"),
("A16","The measurement may be something Northvale has to build itself","BID","A15","a self-service report builder"),
("A16","The report can exist and measure the wrong thing: the request never fixed the start and stop events","RFQ","1.3","orders received before 14:00 will be dispatched within 48 hours"),
]

# ---------------- CHECKING THE AI REVIEW ----------------
REVIEW = os.path.join(HERE, "vendor-review-run.md")
# (statement quoted verbatim from vendor-review-run.md, clause, verbatim clause text, verdict)
# MATCHES: the clause says it. DROPS A CONDITION: the clause says more than the review.
# OUTSIDE A READ: a claim no reading of a bid can support. RECOMMENDATION: the tool's call, kept out of the record.
REVIEW_CHECK = [
("Lead and two seniors named in contract and locked","B25","except on termination of employment","DROPS A CONDITION"),
("commits in terms Northvale can enforce",None,None,"OUTSIDE A READ"),
("**Negotiate** (preferred)",None,None,"RECOMMENDATION"),
("Northvale responsible for extraction and data quality","A5","The customer is responsible for data extraction and data quality.","MATCHES"),
("valid 90 days from 12 June (lapsed ~10 Sep 2026)","B21","The price is valid for 90 days from the date of this response.","MATCHES"),
("Data loss uncapped","B22","caused by Hartlowe","DROPS A CONDITION"),
("which contradicts its claim to meet section 3","C18","Enhanced dispatch performance analytics are on our published roadmap for release in Q1 2027.","OVERSTATES"),
("on the roadmap for Q1 2027","C18","on our published roadmap for release in Q1 2027","MATCHES"),
("during Northvale operating hours, including maintenance","B9","during Northvale's operating hours, including all maintenance","MATCHES"),
]
# Each recorded condition, and the review text that carries it (None if the review drops it).
CONDITION_COVERAGE = {
("B25","no_replacement_without_consent"): None,
("B14","sev1_oncall"): "Sev 1 on call outside those hours",
("B10","service_credits"): "capped at 30%",
("B11","service_credits"): "Must be claimed in writing within 30 days",
("B18","successor_cooperation"): "90 days of successor co-operation at day rate",
("B21","implementation_price"): "valid 90 days from 12 June",
("B3","raw_data_export_free"): "free CSV export",
("D10","support_hours_mon_fri"): "excluding Irish public holidays",
("D21","exit_data_30d"): "30 days in native format",
("A8","availability"): "99.7% monthly",
("D9","availability"): "99.5% **annually**",
("B22","data_loss_uncapped"): None,
}

# ---------------- THE WEEK AFTER: clarification letter to A ----------------
# Every silence in A's response gets one question, or a stated reason for none.
# (clause, verbatim quote of the silence, question or None, reason if None)
CLARIFY_A = [
("A1","confirms full functional coverage of the scope","Against each function in section 2.1, which are standard, which need configuration and which need development?",None),
("A2","supports high-velocity dispatch operations including same-day and 48-hour dispatch workflows","What will you measure for 48-hour dispatch: which system events start and stop the clock, and which report will Northvale receive from go-live?",None),
("A4","pre-built connections to more than sixty carriers","Are Northvale's three carriers among the pre-built connections, and is their integration inside the fixed price?",None),
("A6","a proven five-phase approach refined across more than 400 implementations","Please name the five phases, the deliverable and acceptance test at the end of each, and what Northvale must provide in each.",None),
("A7","Indicative timetable: 26 weeks","Which milestones will you commit to in the contract, and what applies if one is missed?",None),
("A8","commits to a platform availability target of 99.7%","Will you commit to availability as an obligation, measured during Northvale's operating hours and including maintenance?",None),
("A10","can be discussed as part of commercial negotiation","Which service credits apply in the standard support tier, and are they applied automatically?",None),
("A11","follow-the-sun coverage","What are the support hours and restoration targets by severity for each site, and from which countries can support staff access Northvale data?",None),
("A15","more than 200 standard reports and a self-service report builder","Which standard reports meet section 3.4, and which would Northvale have to build?",None),
("A16","Performance measurement against dispatch commitments is fully supported","Is dispatch performance measurement a standard report at go-live, or something built with the report builder, and is it in the price?",None),
("A17","architected for scale and additional sites can be onboarded rapidly","What are the price and lead time to add a fifth site?",None),
("A23","A copy is available on request.","Please send the Master Services Agreement before shortlisting.",None),
("A26","Customer data may be exported on request in a standard format.","At exit, in what format, within what time and at what cost is the data returned, and is the database schema included?",None),
("A29","drawn from Meridian's delivery organisation and approved delivery partners","Please name the delivery partners and the key individuals, and say whether any can be replaced without Northvale's agreement.",None),
("A25","committed to a long-term partnership with Northvale and to your continued success",None,"Nothing a supplier could write would settle it. It goes into the register as a claim that cannot be checked."),
("A30","We would be pleased to discuss any specific requirements not addressed above.",None,"An offer to talk, not a claim about the service."),
]

def check_review_and_week(clauses):
    review = open(REVIEW, encoding="utf-8").read()
    bad = []
    for stmt, cl, q, v in REVIEW_CHECK:
        if stmt not in review: bad.append(f"REVIEW CHECK: statement not in review: {stmt}")
        if cl and (cl not in clauses or q not in clauses[cl]): bad.append(f"REVIEW CHECK: quote not in {cl}: {q}")
    if set(CONDITION_COVERAGE) != set(CONDITIONS): bad.append("CONDITION COVERAGE does not list every recorded condition")
    for k, snip in CONDITION_COVERAGE.items():
        if snip and snip not in review: bad.append(f"CONDITION COVERAGE {k}: not in review: {snip}")
    a_sil = {(c, q) for c, cat, k, q in F if c.startswith("A") and cat == "SIL"}
    covered = {(c, q) for c, q, *_ in CLARIFY_A}
    if a_sil != covered: bad.append(f"CLARIFY_A does not match A's silences: missing {a_sil - covered}, extra {covered - a_sil}")
    for c, q, question, why in CLARIFY_A:
        if bool(question) == bool(why): bad.append(f"CLARIFY_A {c}: needs a question or a reason, not both")
    if bad:
        print("\n".join(bad)); sys.exit(1)
    caught = sum(1 for v in CONDITION_COVERAGE.values() if v)
    verdicts = collections.Counter(v for *_, v in REVIEW_CHECK)
    print(f"\nAI REVIEW CHECK. {len(REVIEW_CHECK)} statements checked: " + ", ".join(f"{n} {v}" for v, n in verdicts.items()) + ".")
    print(f"  Recorded conditions carried by the review: {caught} of {len(CONDITION_COVERAGE)}. Dropped: {[k[0] for k, v in CONDITION_COVERAGE.items() if not v]}")
    nq = sum(1 for r in CLARIFY_A if r[2])
    print(f"THE WEEK AFTER. Clarification letter to A: {nq} questions, {len(CLARIFY_A) - nq} silences with a stated reason for none.")
    obl = [f for f in F if f[0].startswith("A") and f[1] == "OBL"]
    exc = [f for f in F if f[0].startswith("A") and f[1] == "EXCL"]
    trm = [f for f in F if f[0].startswith("A") and f[1] == "TERM"]
    print(f"  Schedule of commitments for A: {len(obl)} obligations with their conditions, {len(exc)} exclusions to allocate, {len(trm)} terms for the drafters.")

# ---------------- THE ONE-INSTRUCTION CHECK ----------------
ONE_CHECK = os.path.join(HERE, "review-check-one-instruction.md")

def check_one_instruction(text):
    out = open(ONE_CHECK, encoding="utf-8").read().split("\n---\n", 1)[1]
    review = open(REVIEW, encoding="utf-8").read().replace("**", "")
    pack = text.replace("**", "")
    norm = lambda s: s.replace("**", "").replace("'", '"')
    bid_q = re.findall(r'\*\*(?:Bid|RFQ)[^:*]*:\*\*\s*"([^"]+)"', out) + re.findall(r'\| [A-D]\d+: "([^"]+)"', out)
    rev_q = re.findall(r'\*\*Review[^:*]*:\*\*\s*"([^"]+)"', out)
    def found(q, src):
        parts = [p.strip(" .,") for p in re.split(r"…|\.\.\.", norm(q)) if p.strip(" .,")]
        return all(p in src.replace("'", '"') for p in parts)
    bad = [("BID", q) for q in bid_q if not found(q, pack)] + [("REVIEW", q) for q in rev_q if not found(q, review)]
    if bad:
        for w, q in bad: print(f"ONE-INSTRUCTION CHECK: {w} quote not found: {q}")
        sys.exit(1)
    n = len(re.findall(r"^### [A-B]\d+\.", out, re.M)) + len(re.findall(r"^\| C\d+ \|", out, re.M))
    print(f"ONE-INSTRUCTION CHECK. {n} claims listed; {len(bid_q)} bid quotes and {len(rev_q)} review quotes all found verbatim.")

def check_stages(text, clauses):
    rfq = dict(re.findall(r"^(\d\.\d) (.+)$", text.split("# PART 2")[0], re.M))
    lines = re.findall(r"^\*\*([A-I]\d)\.\*\*", open(CHECKLIST, encoding="utf-8").read(), re.M)
    bad = []
    for ln, mark, cl, q, why in STAGE1:
        if ln not in lines: bad.append(f"STAGE 1 line {ln} is not in the checklist")
        if cl not in rfq or q not in rfq[cl]: bad.append(f"STAGE 1 {ln}: quote not found in request {cl}: {q}")
    for item, cl, q in RELIEF + ASKED:
        if cl and (cl not in rfq or q not in rfq[cl]): bad.append(f"RELIEF '{item}': quote not found in request {cl}: {q}")
    for c, q, *_ in REGISTER:
        if c not in clauses or q not in clauses[c]: bad.append(f"REGISTER {c}: quote not found: {q}")
    for c, cause, src, cl, q in PREMORTEM:
        if c not in {r[0] for r in REGISTER if r[5] == "CHECKABLE"}: bad.append(f"PRE-MORTEM {c} is not a checkable register claim")
        pool = rfq if src == "RFQ" else clauses
        if cl not in pool or q not in pool[cl]: bad.append(f"PRE-MORTEM {c}: quote not found in {src} {cl}: {q}")
    if len(RELIEF) != 20: bad.append(f"RELIEF LIST HAS {len(RELIEF)} ITEMS, NOT 20")
    if bad:
        print("\n".join(bad)); sys.exit(1)
    marks = {ln: m for ln, m, *_ in STAGE1}
    n = collections.Counter(marks.get(ln, "NOT ANSWERED") for ln in lines)
    core = [ln for ln in CORE_TWELVE if marks.get(ln) == "ANSWERED"]
    print(f"\nSTAGE 1. Of {len(lines)} checklist lines, the request answers {n['ANSWERED']}, partly answers {n['PARTIAL']}, and does not address {n['NOT ANSWERED']}.")
    print(f"  Core twelve settled: {len(core)} of {len(CORE_TWELVE)}. Partly addressed: {[ln for ln in CORE_TWELVE if marks.get(ln)=='PARTIAL']}")
    print(f"STAGE 2. Relief list: {len(RELIEF)} items, {len(RELIEF)} not covered. Asked for, and so not reliefs: {len(ASKED)}.")
    cbc = sum(1 for r in REGISTER if r[5] == "CANNOT BE CHECKED")
    print(f"STAGE 5. Register: {len(REGISTER)} claims, {cbc} cannot be checked from a record you control.")
    print(f"  Pre-mortem: {sum(1 for p in PREMORTEM if p[1])} causes, {len(PREMORTEM)} citations, for the {len({p[0] for p in PREMORTEM})} checkable claims. Odds are left to the buyer.")
    print(f"All {len(STAGE1)} checklist quotes, {sum(1 for r in RELIEF+ASKED if r[1])} relief-list quotes, {len(REGISTER)} register quotes and {len(PREMORTEM)} pre-mortem citations found verbatim.")

def main():
    text = open(PACK, encoding="utf-8").read()
    clauses = dict(re.findall(r"^\*\*([A-D]\d+)\.\*\*\s*(.+)$", text, re.M))
    bad = [f for f in F if f[0] not in clauses or f[3] not in clauses[f[0]]]
    bad += [(c,"COND",k,q) for (c,k),q in CONDITIONS.items() if c not in clauses or q not in clauses[c]]
    if bad:
        for c,cat,k,q in bad: print(f"QUOTE NOT FOUND  {c} {cat}: {q}")
        sys.exit(1)
    covered = {f[0] for f in F} | set(NO_FINDING)
    missing = sorted(set(clauses) - covered, key=lambda x:(x[0], int(x[1:])))
    if missing:
        print("CLAUSES WITH NO FINDING AND NO REASON:", missing); sys.exit(1)

    with open(os.path.join(HERE, "ledger.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh); w.writerow(["response","clause","category","commitment_key","verbatim_quote","condition_or_exception"])
        for c,cat,k,q in F: w.writerow([c[0], c, cat, k, q, CONDITIONS.get((c,k),"")])

    names = {"A":"Meridian","B":"Hartlowe","C":"Calderon","D":"Pellworth"}
    cnt = collections.Counter((f[0][0], f[1]) for f in F)
    ncl = collections.Counter(c[0] for c in clauses)
    print(f"All {len(F)} quotes and {len(CONDITIONS)} conditions found verbatim in the clauses they cite. {len(clauses)} clauses checked.")
    print("This confirms quotation accuracy and arithmetic only, not that every reading is correct or complete.\n")
    print(f"{'':12}{'clauses':>8}{'OBL':>6}{'TERM':>6}{'EXCL':>6}{'SIL':>6}{'total':>7}")
    tot = collections.Counter()
    for r in "ABCD":
        row = [cnt[(r,x)] for x in ("OBL","TERM","EXCL","SIL")]
        for x,v in zip(("OBL","TERM","EXCL","SIL"),row): tot[x]+=v
        print(f"{r} {names[r]:10}{ncl[r]:>8}" + "".join(f"{v:>6}" for v in row) + f"{sum(row):>7}")
    print(f"{'TOTAL':12}{sum(ncl.values()):>8}" + "".join(f"{tot[x]:>6}" for x in ('OBL','TERM','EXCL','SIL')) + f"{sum(tot.values()):>7}\n")

    # Difference pass: OBLIGATIONS ONLY. A real difference is a commitment key
    # that some responses carry as an obligation and others do not.
    carriers = collections.defaultdict(set)
    for c,cat,k,q in F:
        if cat == "OBL": carriers[k].add(c[0])
    diffs = {k:v for k,v in carriers.items() if 0 < len(v) < 4}
    sole = collections.Counter(next(iter(v)) for v in diffs.values() if len(v) == 1)
    print(f"Obligations held by every response (not differences): {sorted(k for k,v in carriers.items() if len(v)==4)}")
    print(f"Real differences, obligations only: {len(diffs)}")
    for r in "ABCD": print(f"  carried by {r} alone: {sole[r]}")
    print(f"  shared by two or three: {sum(1 for v in diffs.values() if len(v)>1)}")
    check_stages(text, clauses)
    check_review_and_week(clauses)
    check_one_instruction(text)

if __name__ == "__main__":
    main()
