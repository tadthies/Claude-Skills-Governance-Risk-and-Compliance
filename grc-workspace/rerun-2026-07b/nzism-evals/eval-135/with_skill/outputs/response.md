# NZISM-Aligned Due Diligence and Contractual Requirements for SaaS Procurement

When procuring a SaaS product for agency use, the NZISM treats this as a third-party supplier / cloud computing arrangement — both control domains apply together. Below is what you should require, organised by procurement stage.

## 1. Before You Engage the Vendor: Scoping

First, establish two things that determine how strict the requirements below need to be:
- **What classification of information will this SaaS product store, process, or transmit?** (Default to Restricted if unclear — that's the common baseline for agency systems.)
- **Where is the SaaS product hosted?** (NZ-based, offshore, or unknown/multi-region.)

These answers scale everything that follows — a SaaS tool touching only Unclassified data has materially lighter requirements than one processing Restricted or Confidential information.

## 2. Pre-Engagement Due Diligence (NZISM Section 13 — Third-Party Suppliers & Section 17 — Cloud Computing)

Before signing anything, the agency should complete:

| Due Diligence Item | What to Check |
|---|---|
| **Supplier security assessment** | Formal review of the vendor's security posture — policies, certifications, past incident history |
| **Cloud risk assessment** | Mandatory before adopting any cloud service for Restricted+ information; assess against the **NZ Government Cloud Computing Risk & Resilience Guide** |
| **Data residency assessment** | Where is data stored/processed/backed up? NZ-hosted is preferred; offshore requires justification |
| **Security certification review** | Preference for vendors holding ISO 27001 or equivalent independent certification — request current certificates and audit scope (not just a marketing claim) |
| **Shared responsibility model** | Vendor must be able to clearly articulate what they secure vs. what the agency configures/secures |
| **Subprocessor/subcontractor disclosure** | Does the vendor use further subcontractors or infrastructure providers (e.g., built on AWS/Azure/GCP)? Data residency and security obligations must flow down to them too |

## 3. Contractual Security Requirements to Impose

Structure these as binding contract clauses, not vendor "assurances":

### 3.1 NZISM-Equivalent Control Obligations
- The vendor must contractually commit to maintaining security controls **equivalent to NZISM requirements** for the classification level of data involved (encryption at rest/in transit, access controls, logging, patch management, etc.)
- Reference specific NZISM baseline requirements relevant to SaaS: MFA for administrative access, TLS 1.2+ for data in transit, encryption at rest for Restricted+ data, patch management timeframes (critical patches within 48 hours per infrastructure controls)

### 3.2 Data Residency and Offshore Hosting
- If any data will be processed or stored offshore, this must be **explicitly disclosed and separately approved by your Accrediting Authority** before contract signature — do not accept vague "global infrastructure" language for Restricted+ data.
- Include a clause prohibiting the vendor from changing hosting location/region without prior written agency approval.

### 3.3 Access Controls
- Least-privilege and need-to-know access for vendor personnel accessing agency data
- Named/logged vendor access to agency data or systems — no shared vendor accounts
- MFA required for any vendor administrative access to the platform

### 3.4 Audit and Right to Audit
- **Right to audit clause** — the agency (or an independent assessor on the agency's behalf) must be able to audit the vendor's security controls, either directly or via review of the vendor's independent audit reports (e.g., SOC 2 Type II, ISO 27001 surveillance audits)
- Require the vendor to provide relevant audit/certification reports on an ongoing (e.g., annual) basis, not just at contract signature

### 3.5 Incident Notification
- Mandatory breach/incident notification to the agency **within a defined timeframe** (e.g., 24–72 hours of detection) — this is an NZISM third-party supplier requirement and should be a hard contractual deadline, not best-effort
- Notification must include sufficient detail for the agency to meet its own NCSC NZ and Privacy Act 2020 obligations
- Vendor must cooperate with agency incident response and evidence preservation activities

### 3.6 Encryption and Key Management
- Data at rest encrypted (AES-256 preferred); data in transit via TLS 1.2 minimum (TLS 1.3 preferred)
- Clarify key management — who holds encryption keys, and does the agency have any control or visibility (important for data sovereignty in offshore scenarios)

### 3.7 Logging and Monitoring
- Vendor must provide adequate audit logging of access and administrative actions on agency data, retained per NZISM minimums (90 days online, 12 months archived, longer for Confidential+), and made available to the agency on request or via API

### 3.8 Business Continuity and Availability
- Defined SLAs for availability, backup frequency, and recovery objectives (RTO/RPO) appropriate to how critical the SaaS function is to the agency
- Backup testing evidence

### 3.9 Data Portability and Exit Strategy
- Contractual right to export agency data in a usable format at any time and upon contract termination
- **Certified secure deletion** of agency data from vendor systems (and subprocessor systems) upon exit, with a certificate of destruction/deletion provided
- No lock-in via proprietary formats that would frustrate a clean exit

### 3.10 Personnel and Subcontractor Obligations
- Vendor personnel with access to agency data should be subject to background checks appropriate to the classification level
- Subcontractor/subprocessor obligations must mirror the prime contract's security terms (flow-down clause)

## 4. Ongoing Obligations After Contract Signature

- **Shared responsibility matrix** — document and review at least annually what the agency vs. vendor is responsible for
- **Annual security reassessment** of the vendor, not just a one-time pre-contract check
- Include this SaaS product in the agency's asset register and, if it processes Restricted+ information, ensure it is captured within the relevant System Security Plan and goes through Certification & Accreditation before go-live
- Track the vendor relationship in your Third-Party Supplier risk register

## Quick-Reference Checklist

- [ ] Classification of data confirmed; hosting location confirmed
- [ ] Cloud risk assessment completed against NZ Government Cloud Computing Risk & Resilience Guide
- [ ] Vendor security certifications verified (ISO 27001 or equivalent, SOC 2)
- [ ] Data residency terms agreed; offshore hosting (if any) approved by Accrediting Authority
- [ ] NZISM-equivalent security controls specified in contract
- [ ] Right-to-audit clause included
- [ ] Incident notification timeframe specified contractually
- [ ] Encryption standards (at rest and in transit) specified
- [ ] Logging/retention requirements specified
- [ ] Exit strategy — data portability and certified deletion — included
- [ ] Subcontractor/subprocessor flow-down obligations included
- [ ] SaaS product added to asset register and, if Restricted+, incorporated into SSP/C&A process

I can help draft the specific contract clauses, a vendor security questionnaire, or the cloud risk assessment template if that would be useful for this procurement.

---
*This is general compliance guidance, not legal advice. Verify current requirements against official NZISM/NCSC NZ guidance and the NZ Government Cloud Computing Risk & Resilience Guide, and have final contract language reviewed by your procurement and legal teams.*
