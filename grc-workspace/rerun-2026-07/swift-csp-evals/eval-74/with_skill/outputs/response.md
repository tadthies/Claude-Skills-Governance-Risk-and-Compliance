# SWIFT CSCF KYC-SA Attestation — Complete Walkthrough (Architecture Type A1)

## Important deadline correction first

You mentioned a **July 31** deadline — that's the *traditional* annual SWIFT CSP deadline from prior cycles, but it no longer applies as-is. Under **CSCF v2026**, SWIFT has opened an **extended attestation window: July 1 – December 31, 2026**, with the actual submission deadline now **December 31, 2026**, not July 31. You have more runway than you think — but I'd still recommend treating July 31 as an internal target if that's what your governance calendar assumes, and confirm the exact date currently posted at swift.com/myswift, since PMO guidance can be updated.

I'll walk through the full process below regardless of which date you lock in.

---

## Step 1 — What You Need to Prepare (Architecture Type A1)

As an **A1** (customer connector, customer-managed, software-based — e.g., Alliance Access/Gateway on-premises), you are in scope for the full set of controls applicable to on-premises customer-managed connectivity. You need evidence for **all mandatory controls applicable to A1**, including the newly mandatory **Control 2.4**.

### Evidence checklist by control (KYC-SA attestation prep format)

| Control | Name | Attestation Status | Evidence Pointers |
|---------|------|--------------------|--------------------|
| 1.1 | SWIFT Environment Protection | Implemented / Partial / Not Implemented | Network diagram of SWIFT secure zone, firewall rule sets, dual-homing check |
| 1.2 | OS Privileged Account Control | — | Privileged account inventory, access review logs |
| 1.4 | Restriction of Internet Access | — | Firewall/proxy config showing no direct internet from SWIFT infra, jump server config |
| 2.1 | Internal Data Flow Security | — | Encryption config for internal SWIFT data flows |
| 2.2 | Security Updates | — | Patch management records (critical = 3 days, high = 90 days SLA evidence) |
| 2.3 | System Hardening | — | CIS Benchmark scan results or equivalent hardening standard evidence |
| **2.4** | **Back-Office Data Flow Security (NEW mandatory in v2026)** | — | Data flow map SWIFT zone ↔ back office, mutual TLS 1.2+ config, firewall rules restricting back-office access to named IP/ports, SIEM logging of back-office connections |
| 2.6 | Operator Session Confidentiality and Integrity | — | Session encryption config (e.g., TLS for Alliance Web Platform) |
| 2.7 | Vulnerability Scanning | — | Quarterly credentialed scan reports covering all SWIFT-connected systems |
| 2.8 | Critical Activity Outsourcing | — | Vendor/outsourcer due diligence records, contracts with security clauses |
| 2.10 | Application Hardening | — | Application-level hardening configuration evidence |
| 3.1 | Physical Security | — | Server room access logs, card access system records |
| 4.1 | Password Policy | — | Password policy document, technical enforcement config |
| 4.2 | Multi-Factor Authentication | — | MFA config for all interactive operator sessions — **hardware tokens required**, not app-based OTP |
| 5.1 | Logical Access Controls | — | Individual (non-shared) operator account listing, least-privilege role matrix, quarterly access reviews |
| 5.2 | Token Management | — | Hardware token inventory, issuance/deprovisioning records |
| 5.4 | Physical and Logical Password Storage | — | Password vault/storage config evidence |
| 6.1 | Malware Protection | — | AV/EDR deployment evidence on SWIFT-connected systems |
| 6.2 | Software Integrity | — | Integrity verification process for SWIFT software before/after updates |
| 6.3 | Database Integrity | — | Database access control and integrity check evidence |
| 6.4 | Log and Monitoring | — | SIEM ingestion of Alliance Access/Gateway logs, alert rules, 1-year minimum retention proof |
| 7.1 | Cyber Incident Response Planning | — | SWIFT-specific IRP with notification triggers and escalation path |
| 7.2 | Security Training and Awareness | — | SWIFT operator training records/completion logs |

> **Advisory controls** (1.3A, 1.5A, 2.5A, 2.9A, 2.11A, 5.3A, 6.5A, 7.3A, 7.4A) are not mandatory for attestation but strengthen your posture and may be requested by counterparties or regulators — consider including evidence for these if resources allow.

### Priority focus areas before you assess anything else

1. **Control 2.4** — this is new to mandatory status in v2026. If you previously treated it as advisory and skipped it, this is now a **gap that blocks a clean attestation**. Map all SWIFT-zone-to-back-office data flows, implement mutual TLS 1.2+, and segment with dedicated firewall rules before your assessor engagement.
2. **Control 4.2 (MFA)** — confirm hardware tokens are in use for all operators, not software OTP.
3. **Control 1.1** — confirm no dual-homed servers and a documented secure zone diagram exists.

### Practical prep sequence

1. Confirm A1 architecture scope with your SWIFT relationship manager/internal architecture owner (already confirmed here as A1).
2. Run an internal gap assessment against every mandatory control above, using: Control ID | Status (🔴/🟡/🟢) | Evidence Available | Evidence Type | Gap Description | Remediation Action | Owner | Target Date.
3. Remediate any 🔴/🟡 items — prioritize Control 2.4 given it's newly mandatory.
4. Assemble an evidence package (policies, configs, logs, screenshots, scan/test results) organized by control number.
5. Engage your independent assessor (see Step 2) with enough lead time before your target submission date.

---

## Step 2 — Who Can Act as Your Independent Assessor

Since CSCF v2020, self-attestation is no longer sufficient — an **independent assessment** is mandatory for all users, including A1 institutions. As an A1 bank not subject to an Enhanced Standard programme or specific regulator mandate, you fall under the **Community Standard Assessment (CSA)**.

**Eligible assessors:**
- **Your internal audit team** — permitted, *but only if sufficiently independent* from the team that operates your SWIFT environment (no operational responsibility, no reporting line conflict)
- **An external audit firm** with demonstrated SWIFT CSP assessment competency
- **SWIFT-certified assessors** listed on SWIFT's KYC Registry

**Key constraint:** The assessor **must not have operational responsibility** for the SWIFT environment being assessed. If your internal audit function reports into the same chain as SWIFT operations, or has previously configured/managed SWIFT infrastructure, they are disqualified — you'll need an external firm or KYC Registry-listed assessor instead.

**Assessment scope:** All mandatory controls applicable to A1 architecture (per the checklist in Step 1). Advisory controls can be included at your discretion but aren't required for the assessor's opinion.

**Action for you:** If you haven't already engaged an assessor, do so now — independent assessments (especially external firms) often have lead times of several weeks, and you'll need their sign-off before form completion.

---

## Step 3 — Completing the KYC-SA Form

1. **Access the portal**: Submission is via the SWIFT portal at **swift.com/myswift**.
2. **Per-control attestation**: For each of the mandatory controls applicable to A1, attest one of:
   - **Implemented**
   - **Partially Implemented**
   - **Not Implemented**
3. **Attach or reference evidence**: Ensure your evidence package (Step 1) maps directly to each control's attestation status — assessors and counterparties may request this.
4. **Independent assessor validation**: Your assessor's findings feed into or corroborate what you attest — discrepancies between your self-assessment and the assessor's findings should be resolved before submission.
5. **Architecture type declaration**: Confirm A1 is correctly declared in the portal, since this determines which controls are shown as applicable/mandatory.
6. **Review before submission**: Any control attested as "Partially Implemented" or "Not Implemented" should have a remediation plan ready, since counterparties can see your status and may follow up.

---

## Step 4 — What Happens After Submission

| Event | Timing / Detail |
|-------|-----------------|
| Counterparty visibility | **Immediate** upon submission — your correspondent banks and counterparties can view your attestation status right away |
| Counterparty queries | Counterparties may reach out directly for clarification on any "Partial" or "Not Implemented" controls — be prepared to respond |
| Non-attestation flag | If you miss the deadline, you will be **flagged to counterparties as non-attesting**, which can trigger enhanced due diligence or relationship reviews from your correspondents |
| Regulatory visibility | In several jurisdictions, SWIFT CSP compliance ties into supervisory expectations (e.g., ECB/EBA under DORA in the EU, NY DFS 23 NYCRR 500 in the US, MAS TRM in Singapore) — regulators may reference your attestation status |
| Non-compliance escalation | Sustained non-compliance can lead to counterparty notifications, potential relationship suspension by counterparties, and regulatory escalation |
| Next cycle | CSCF v2027 is expected to be published July 2026 — plan for a fresh control review ahead of the following attestation cycle |

---

## Summary — Your Action Checklist

- [ ] Confirm actual current deadline on swift.com/myswift (v2026 window runs July 1 – Dec 31, 2026; December 31 is the operative deadline, not July 31)
- [ ] Complete internal gap assessment across all mandatory A1 controls, with **Control 2.4 as top priority** (newly mandatory)
- [ ] Remediate any 🔴/🟡 gaps, especially 2.4 (back-office data flow encryption/authentication) and 4.2 (hardware MFA)
- [ ] Confirm assessor independence (internal audit only if no operational ties to SWIFT ops) or engage an external/KYC Registry-listed assessor
- [ ] Complete independent assessment against all applicable mandatory controls
- [ ] Assemble evidence package mapped to each control
- [ ] Complete and submit KYC-SA form via swift.com/myswift, declaring A1 architecture
- [ ] Prepare to respond to counterparty queries post-submission
