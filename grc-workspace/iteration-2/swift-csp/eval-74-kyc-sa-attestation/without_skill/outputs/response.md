# SWIFT KYC-SA Attestation Process

## Overview

The KYC Security Attestation (KYC-SA) is SWIFT's annual compliance attestation program under the Customer Security Programme (CSP). All SWIFT users must annually attest to their compliance with the Customer Security Controls Framework (CSCF). Here is a complete walkthrough for your A1 architecture bank.

---

## Step 1: Preparation

### What You Need

Before beginning the attestation, prepare the following:

**1. Control Assessment**
Conduct an assessment of your compliance posture against all mandatory CSCF controls applicable to A1 architecture. For each control, document:
- Current implementation status
- Evidence supporting your status
- Any gaps and remediation plans

**2. Evidence Portfolio**
Gather evidence for each control:
- Network topology diagrams (Control 1.1)
- Patch management records (Control 2.2)
- Hardware token deployment records (Control 4.2)
- SIEM configuration and log retention evidence (Control 6.4)
- Incident response plan (Control 7.1)
- Physical security access logs (Control 3.1)

**3. Independent Assessor Arrangement**
Identify and engage your independent assessor (see Step 2) well in advance of the attestation window.

---

## Step 2: Independent Assessor Requirements

SWIFT requires an **independent assessment** of your CSCF compliance. The assessor must be independent from your SWIFT operations team.

### Who Qualifies as an Independent Assessor?

| Assessor Type | Notes |
|--------------|-------|
| **Internal Audit** | Must be organizationally independent from the team that manages SWIFT operations. Typically the internal audit department reporting to the audit committee is acceptable. |
| **External Auditor or Cybersecurity Firm** | A qualified external firm with SWIFT CSP knowledge. Big 4 audit firms and specialist cybersecurity firms are commonly used. Look for firms with demonstrated CSCF experience. |
| **SWIFT-Certified Assessors** | SWIFT maintains a directory of third-party assessors who have been certified for CSP assessments. These are typically the most straightforward option for KYC-SA purposes. |

The assessor must:
- Have relevant SWIFT CSP knowledge
- Be independent from the SWIFT operations function
- Review your evidence and controls
- Provide sign-off on your attestation

---

## Step 3: The Attestation Window

**v2026 Attestation Window:** July 1 – December 31, 2026

### Key Dates

| Milestone | Date |
|-----------|------|
| Window opens | July 1, 2026 |
| Deadline for submission | December 31, 2026 |
| Attestation visible to counterparties | Immediately upon submission |
| Non-attesting users flagged | After deadline |

### Consequences of Late or Missing Attestation

- SWIFT notifies your counterparties that you have not attested by the deadline
- Counterparties may treat you as non-compliant and initiate additional due diligence
- In severe cases, SWIFT may restrict your ability to send or receive messages
- Regulatory implications in some jurisdictions

**Recommendation:** Do not wait until December. Aim to submit by October or November to allow time for any last-minute corrections.

---

## Step 4: Completing the KYC-SA Form

### Accessing the Portal

The KYC-SA attestation is submitted through the **SWIFT MySwift portal** at **swift.com/myswift**. Log in with your institution's SWIFT credentials and navigate to the KYC-SA section.

### Attestation Status Options

For each control, you select one of three statuses:

| Status | Meaning |
|--------|---------|
| **Implemented** | The control is fully implemented as required by the CSCF |
| **Partially Implemented** | The control is partially in place — some requirements met, some not yet |
| **Not Implemented** | The control has not been implemented |

### Working Through the Controls

For each of the 24 mandatory controls applicable to your A1 architecture:
1. Review your assessment and evidence
2. Select the appropriate attestation status
3. Reference or attach supporting evidence as prompted
4. Note any plans for partially/not implemented controls

### Advisory Controls

For advisory controls (1.3A, 1.5A, 2.5A, etc.), you may voluntarily attest or mark as not applicable. Advisory controls are not required for attestation.

### Independent Assessor Sign-Off

Once you have completed the control-by-control attestation, your independent assessor must review and provide their sign-off within the portal system.

### Submission

Submit the completed attestation. This makes your compliance status immediately visible to all your SWIFT counterparties.

---

## Step 5: After Submission — Counterparty Visibility

Once your attestation is submitted:

**What counterparties see:**
- Your overall attestation status
- Per-control attestation status (Implemented / Partially / Not Implemented)
- Date of attestation
- Whether an independent assessor was used

**Counterparty actions:**
- Correspondent banks reviewing your compliance status as part of their due diligence
- Requests for clarification on controls marked Partially Implemented or Not Implemented
- Some counterparties may impose conditions on their banking relationship based on your attestation

---

## Key Tips for A1 Banks

1. **Start early**: The assessment and evidence gathering process takes several weeks
2. **Control 2.4**: Verify whether back-office data flow security is mandatory in your applicable CSCF version — SWIFT has been moving it from advisory to mandatory
3. **Hardware tokens for 4.2**: Ensure all SWIFT operators are using hardware MFA tokens before attesting Implemented
4. **Log retention for 6.4**: Confirm you have 12 months of log retention before attesting
5. **SWIFT-specific IRP**: A general IT incident response plan is not sufficient for Control 7.1

For the most current and precise requirements, always reference the official CSCF v2026 document available through swift.com, as specific requirements can be updated annually.
