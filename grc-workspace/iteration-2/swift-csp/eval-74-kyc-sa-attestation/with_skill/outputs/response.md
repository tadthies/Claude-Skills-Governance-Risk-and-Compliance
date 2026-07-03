# SWIFT KYC-SA Attestation Process — Complete Walkthrough

**Architecture:** A1 (Alliance Access, on-premises, customer-managed)
**Framework version:** CSCF v2026
**v2026 Attestation window:** July 1 – December 31, 2026

---

## Overview

The KYC Security Attestation (KYC-SA) is SWIFT's annual mechanism for all SWIFT users to declare their compliance status against the Customer Security Controls Framework (CSCF). As an A1 bank, you attest against all 24 mandatory controls. Your attestation is visible to your counterparties and affects your perceived compliance standing within the SWIFT community.

---

## Step 1: Preparation — What You Need Before Starting

### 1.1 Complete a Control-by-Control Assessment

Before logging into the portal, conduct a thorough internal assessment of all 24 mandatory controls. For each control, you need:

- **Current implementation status** (Implemented / Partially Implemented / Not Implemented)
- **Evidence artifacts** that support your attestation (configuration screenshots, policy documents, scan reports, training records, etc.)
- **Gap remediation plans** for any controls not yet fully implemented

As an A1 institution, your mandatory control scope is: 1.1, 1.2, 1.4, 2.1, 2.2, 2.3, 2.4, 2.6, 2.7, 2.8, 2.10, 3.1, 4.1, 4.2, 5.1, 5.2, 5.4, 6.1, 6.2, 6.3, 6.4, 7.1, 7.2.

**Key v2026 note:** Ensure Control 2.4 (Back-Office Data Flow Security) is included in your scope — it was promoted from Advisory to Mandatory in v2026. If your institution previously skipped 2.4, you have a mandatory gap.

### 1.2 Engage Your Independent Assessor

CSCF v2026 requires an **independent assessment** — you cannot simply self-attest without independent validation. Arrange your assessor early; assessors can be booked for 4–8 weeks out from July onward.

### 1.3 Gather Evidence Files

Organize evidence by control number. Typical evidence includes:
- Network topology diagrams (Control 1.1)
- Patch management records (Control 2.2)
- TLS configuration evidence for back-office connections (Control 2.4)
- Hardware token inventory and MFA configuration screenshots (Control 4.2)
- SIEM dashboards and log retention policy (Control 6.4)
- SWIFT-specific Incident Response Plan (Control 7.1)

---

## Step 2: Who Can Be Your Independent Assessor?

SWIFT requires that the attestation be validated by an **independent assessor** — someone who is independent from the team responsible for operating the SWIFT environment. Qualified assessors include:

| Assessor Type | Requirements |
|--------------|-------------|
| **Internal Audit** | Must be organizationally independent from SWIFT operations — the same team that runs SWIFT cannot audit itself. Internal audit reporting to the board/audit committee is acceptable. |
| **External Auditor** | A qualified external auditor (e.g., Big 4, specialist cybersecurity firm) with demonstrated SWIFT CSP competency and knowledge of the CSCF |
| **SWIFT-Certified Assessor** | Third-party assessors listed in SWIFT's certified assessor directory — these firms have formal SWIFT CSP credentials and are typically the most straightforward choice for KYC-SA compliance |

**Selection criteria:**
- Independence from SWIFT operations is mandatory
- Knowledge of CSCF v2026 controls and applicable architectures
- Familiarity with financial sector security requirements
- Ability to review evidence artifacts and sign off on attestation statements

SWIFT's directory of certified assessors is available through the SWIFT Customer Security Programme portal.

---

## Step 3: Completing the KYC-SA Form

### 3.1 Access the Portal

The KYC-SA attestation is submitted through the **SWIFT MySwift portal** at **swift.com/myswift**. Log in with your institution's SWIFT credentials. Navigate to **KYC-SA** within the portal.

### 3.2 Attestation Status Options

For each control, you select one of three statuses:

| Status | Meaning |
|--------|---------|
| **Implemented** | The control is fully implemented as required by the CSCF. You have evidence to support this. |
| **Partially Implemented** | The control is in progress or only partially deployed — some requirements met, others not yet. |
| **Not Implemented** | The control has not been implemented. This will be visible to counterparties. |

> **Important:** Do not attest "Implemented" unless you can provide evidence to support it. If your independent assessor reviews your evidence and disagrees, they can decline to certify the attestation.

### 3.3 Control-by-Control Attestation

Work through each mandatory control in the KYC-SA form:
1. Select the attestation status
2. Upload or reference supporting evidence (the portal may prompt for evidence references)
3. Add notes where relevant (e.g., compensating controls or planned remediation dates for Partially Implemented)

### 3.4 Independent Assessor Sign-Off

Your independent assessor must review the completed attestation and provide their sign-off within the portal. They confirm that the evidence they reviewed supports your attestation statements. This is not a rubber stamp — they are making a professional attestation that can have regulatory implications.

### 3.5 Submit

Once the independent assessor has signed off, you submit the attestation. Upon submission, the status is locked and immediately visible to counterparties.

---

## Step 4: v2026 Attestation Window and Key Dates

| Milestone | Date |
|-----------|------|
| **Attestation window opens** | July 1, 2026 |
| **Attestation deadline** | December 31, 2026 |
| **Attestation visible to counterparties** | Immediately upon submission |
| **Non-atteating users flagged to counterparties** | After December 31, 2026 |

**Consequences of late or missing attestation:**
- SWIFT notifies your counterparties that you have not attested
- Correspondent banks may treat you as non-compliant and initiate enhanced due diligence
- Regulatory escalation is possible in some jurisdictions
- In serious cases, SWIFT may restrict or suspend connectivity

**Recommendation:** Do not wait until December — submit as soon as your assessment is complete and remediation is in place. Submitting in October or November gives time to address any last-minute issues.

---

## Step 5: What Happens After Submission

### Counterparty Visibility

Your attestation is **immediately visible to your counterparties** once submitted. SWIFT correspondent banks, CSDs, and other financial market infrastructures can view your compliance status for each control. They see:

- Your overall attestation status
- Per-control attestation status (Implemented / Partially Implemented / Not Implemented)
- Date of attestation
- Whether an independent assessor was used

### Counterparty Enquiries

Counterparties may contact you to:
- Request clarification on controls marked Partially Implemented
- Ask for remediation timelines on Not Implemented controls
- Require full implementation before onboarding new correspondent banking relationships

### SWIFT's Use of Attestation Data

SWIFT uses aggregate attestation data to monitor ecosystem-wide security posture. Individual attestation data remains visible only to counterparties and SWIFT itself, not publicly disclosed.

---

## Common Pitfalls to Avoid

1. **Attesting "Implemented" without evidence** — your assessor will challenge this and your counterparties may too
2. **Missing Control 2.4** — it is now mandatory in v2026; do not treat it as advisory
3. **Engaging a non-independent assessor** — the SWIFT operations team cannot self-attest without independent review
4. **Waiting until December** — if you encounter issues (failed evidence, assessor availability), you may miss the deadline
5. **Incomplete control scope** — as an A1 institution, all 24 mandatory controls must be covered; do not inadvertently skip a control

Start your assessment now (July 2026) — you have exactly 6 months to complete assessment, remediate gaps, and submit attestation.
