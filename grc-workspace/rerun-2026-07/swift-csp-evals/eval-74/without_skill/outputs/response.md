IMPORTANT CAVEAT: "KYC-SA" (KYC Self-Assessment) and "A1 architecture" are most commonly associated with the SWIFT Customer Security Programme (CSP) ecosystem — SWIFT does define "architecture types" (A1, A2, A3, A4, B) for the CSCF (Customer Security Controls Framework) attestation. However, the "KYC-SA" naming (KYC-Registry Self-Attestation / Know Your Customer for Correspondent Banking due diligence) is a related but distinct SWIFT product — the SWIFT KYC Registry and its Security Attestation. I am not able to verify current-year (2026) procedural specifics, exact form field names, or current independent assessor rules with certainty from memory alone, since these details are updated annually by SWIFT/the relevant scheme and I have not consulted current source documents. Treat the following as a general process walkthrough based on how these programs have historically operated, and verify every procedural and deadline detail against the current official SWIFT/KYC-SA portal guidance and your compliance/SWIFT RMA team before acting. Do not submit based on this document alone.

---

# Annual KYC-SA Attestation Walkthrough (A1 Architecture) — General Guidance

## 1. What "A1 Architecture" Means for Your Attestation

In the SWIFT Customer Security Controls Framework (CSCF), architecture type determines which of the mandatory and advisory controls apply to you and how you attest:

- **A1** = You have a local SWIFT infrastructure (messaging interface, connectivity/communication component, possibly a local SWIFT-related application) fully within your own environment, not hosted by a service bureau or shared infrastructure provider.
- This is the most common architecture for banks that run their own SWIFT Alliance Access/Gateway or equivalent messaging interface on-premises or in their own controlled cloud environment.

Because you are A1, your attestation must cover the full scope of your local SWIFT infrastructure — you cannot rely on a service bureau's attestation to cover any part of your environment. This typically means a broader control scope and more evidence to assemble than B-architecture (service-bureau-hosted) participants.

## 2. What You Need to Prepare

**A. Scope definition**
- Confirm and document your current SWIFT architecture diagram: messaging interface, connector/communication interface, HSM (hardware security module) or token, any local SWIFT-related applications, and jump servers/secure zones.
- Confirm this matches what you declared as "A1" in the prior year — if your environment changed (e.g., migrated to a hosted or cloud-based interface), your architecture type itself may need to be reclassified before you attest.

**B. Control self-assessment evidence**
- Gather evidence against the current year's CSCF control baseline (mandatory controls, plus any advisory controls you've chosen to implement). Typical evidence includes:
  - Network segmentation diagrams and firewall rule reviews (secure zone controls)
  - Access control lists, privileged access reviews, multi-factor authentication configuration
  - Patch management and vulnerability scan reports
  - Logging and monitoring configuration, SIEM integration evidence
  - Physical security controls for on-premises infrastructure
  - Business continuity/backup evidence
  - Security awareness training records
  - Incident response plan and test records
- Identify any gaps versus the current control set and determine whether you need to file for an exception or remediation plan for any non-compliant mandatory control.

**C. Prior year attestation and any exceptions**
- Pull your prior year's submitted attestation and any approved exceptions to check what has changed.

**D. Internal sign-off**
- Most institutions require CISO or Head of Operations sign-off, and often board/senior management awareness, before external submission, given this is a regulatory/counterparty-facing attestation.

## 3. Who Can Act as Your Independent Assessor

Historically, SWIFT CSP attestations allow three assessment routes, and your institution's own internal policy plus counterparty expectations determine which is acceptable:

1. **Self-assessment** — attested internally, typically by CISO/senior security officer, without external validation. Some counterparties and regulators increasingly do not accept pure self-assessment for A1 architecture banks, especially larger or systemically important institutions.
2. **Internal audit-led assessment** — performed by your own internal audit function, provided it is organizationally independent from the teams that implement and operate the controls (standard three-lines-of-defense independence).
3. **External/independent third-party assessor** — a qualified external audit firm or specialized security assessment provider. For SWIFT-related attestations, the assessor generally needs to demonstrate relevant expertise (e.g., CISA, CISSP-qualified staff, experience with the CSCF or equivalent control framework) and organizational independence from your bank (no conflict of interest, not the same firm providing remediation consulting on the same controls being assessed).

Practical recommendations:
- Check whether your regulator, correspondent banks, or the scheme/network operator mandates independent (external or internal-audit) assessment for your tier/size of institution — many jurisdictions now require independent validation rather than pure self-attestation, particularly for banks above a certain asset size or transaction volume.
- If using an external assessor, engage them well before the deadline (independent assessments commonly take 3-6 weeks including fieldwork, evidence review, and report drafting) — starting in early July for a July 31 deadline is tight; expedite this immediately.
- Ensure the assessor's engagement letter explicitly scopes them to assess against the current year's control framework version, not a prior year's baseline.
- Retain the assessor's report/workpapers — you will likely need to reference or retain evidence of who performed the assessment (name/firm, credentials, independence confirmation) as part of your submission or for your own audit trail.

## 4. How to Complete the KYC-SA Form

While I cannot confirm the exact current-year field layout without pulling the live portal, the general structure of this type of form typically includes:

1. **Institutional identifiers** — BIC(s) in scope, legal entity name, jurisdiction, group parent (if applicable).
2. **Architecture type declaration** — confirm A1, with supporting description of your infrastructure.
3. **Control-by-control responses** — for each mandatory (and any elected advisory) control: compliant / not compliant / compliant with exception, with a free-text field for context and remediation timelines where applicable.
4. **Assessment methodology declaration** — indicate whether the attestation is self-assessed, internal-audit assessed, or independently/externally assessed, and provide assessor details (name, firm, date of assessment).
5. **Signatory/attestor details** — name and title of the accountable officer (commonly CISO, Head of Information Security, or equivalent) who is formally attesting on behalf of the institution.
6. **Supporting documentation upload** — some programs allow or require attaching the independent assessment report or a summary letter.
7. **Submission and confirmation** — a final review/lock step; many portals allow a draft state before final submission, after which the record typically becomes read-only.

Before completing the form:
- Confirm the current control framework version number/year applies (control baselines are updated annually and sometimes mid-year).
- Cross-check every "compliant" response against actual evidence gathered in step 2 — do not respond based on memory of last year's answers, as controls and their wording can change year to year.
- For anything not fully compliant, prepare a clear remediation plan with dates, since incomplete or unexplained gaps are the most common reason attestations get flagged or rejected.

## 5. What Happens After Submission

Typically:
- **Immediate**: You receive a submission confirmation/receipt, often with a timestamp that matters for deadline compliance (aim to submit several days before July 31, not on the deadline itself, in case of portal issues).
- **Validation/quality checks**: The receiving body (scheme operator, regulator, or clearing counterparty network) may run automated completeness checks and, in some programs, a percentage of attestations are selected for spot-check or deeper review.
- **Visibility to counterparties**: For programs like the SWIFT KYC Registry, your attestation status typically becomes visible to your correspondent banking counterparties who have permissioned access to your KYC Registry profile — they use it as part of their own due diligence/KYC refresh on you. A late, incomplete, or "non-compliant with no remediation plan" attestation can trigger enhanced due diligence requests or, in some cases, correspondent relationship review.
- **Regulatory reporting**: Depending on your jurisdiction, your regulator may receive an aggregate compliance status or may request your attestation directly during examinations.
- **Non-compliance consequences**: If you attest to non-compliance on mandatory controls without an acceptable remediation timeline, you may face escalation — ranging from enhanced monitoring by counterparties/scheme operator, to restrictions, to regulatory inquiry, depending on severity and jurisdiction.
- **Record retention**: Retain your submitted attestation, evidence pack, and assessor report for your own audit trail — these are commonly requested again during regulatory exams or counterparty due diligence refreshes even after submission.

## Immediate Action Items Given Your July 31 Deadline

1. Today: Confirm the exact program/portal this "KYC-SA" attestation refers to internally (SWIFT KYC Registry Security Attestation vs. another network's program) and pull the current-year control baseline/form from the official source — do not rely on last year's template.
2. This week: Finalize architecture scope confirmation (A1) and complete the evidence-gathering checklist above.
3. This week: If independent assessment is required or preferred, engage the assessor immediately — this is your critical path item given the ~4-week runway.
4. Week of assessment: Remediate or document exceptions for any control gaps found.
5. Before July 31 (ideally by July 27-28): Complete internal sign-off, finalize the form, and submit with buffer time before the deadline.
6. After submission: File the confirmation receipt and full evidence/assessor package in your compliance record repository.

Recommended next step: Confirm with your compliance or SWIFT operations team which specific program and portal "KYC-SA" refers to, then pull this year's official instructions and control baseline directly from that source so the specific form fields, exact assessor eligibility rules, and current deadlines/consequences can be verified precisely rather than relied on from general knowledge.
