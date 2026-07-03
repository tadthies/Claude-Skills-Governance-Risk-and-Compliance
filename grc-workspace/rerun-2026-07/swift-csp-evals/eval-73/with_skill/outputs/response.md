# SWIFT CSCF v2026 Gap Assessment

Before scoring, one scoping question: **which SWIFT architecture type applies (A1/A2/A3/A4/B)?** This determines which of the 32 controls are in scope. I've assumed **A1 (customer-managed, on-premises)** for this assessment since you describe a self-managed SWIFT zone — flag if that's wrong, as it changes applicability for 1.2 (OS Privileged Account Control, N/A for A3/A4).

Below I've rated the six controls where you gave me enough detail to assess, plus flagged every other mandatory control that is **not assessed** because no information was provided — these still need to be evidenced before your v2026 KYC-SA attestation (window: **July 1 – December 31, 2026**).

---

## Part 1 — Controls Assessed From Facts Provided

| Control ID | Control Name | Status | Evidence Required | Gap Notes |
|---|---|---|---|---|
| **1.1** | SWIFT Environment Protection | 🔴 Not Implemented | Network architecture diagram; firewall ruleset; system inventory; evidence of no dual-homing | SWIFT zone exists but sits on a **shared VLAN** with other internal systems — this is dual-homing/lack of isolation, a direct breach of the core requirement that the Secure Zone be isolated by deny-by-default firewalls. This is one of the most heavily scrutinized controls in independent assessments. |
| **2.2** | Security Updates | 🔴 Not Implemented | Patch/vulnerability management reports for SWIFT-scoped systems; SWIFT advisory tracking log; exception register | Critical vulnerabilities patched within **30 days**; CSCF v2026 SLA for Critical/Emergency is **3 calendar days**. You are ~27 days outside SLA with no evidence of a documented exception or compensating control. |
| **4.2** | Multi-Factor Authentication | 🔴 Not Implemented | MFA configuration evidence per SWIFT interface; token inventory; authentication logs | Software-based OTP (authenticator app) is in use. Per CSCF v2026, software OTP **does not satisfy** this control for most architecture types — hardware OTP tokens, smart cards with PIN, or FIDO2 keys are required. This is one of the most common non-compliance findings industry-wide. |
| **6.4** | Log and Monitoring | 🔴 Not Implemented | SIEM configuration showing SWIFT log sources; log retention policy/technical evidence; alert rules; 30-day log review records | Two independent failures: (1) retention is **6 months**, vs. the required minimum of **1 year online / 3 years total**; (2) logs are collected but **not reviewed** — the control requires daily review of authentication/transaction anomalies and weekly review of other events, with automated alerting. Collection without review or adequate retention does not meet the control. |
| **7.1** | Cyber Incident Response Planning | 🔴 Not Implemented | SWIFT-specific IRP document (dated, approved); annual tabletop/drill record; SWIFT notification contact list | A general IT incident response plan exists, but there is **no SWIFT-specific IRP**. The control requires explicit coverage of SWIFT notification obligations (24-hour notification to SWIFT CISO on confirmed incidents, 30-day full report), SWIFT fraud scenarios, and evidence-preservation procedures — none of which a generic IT IRP typically addresses. |
| **5.1** | Logical Access Controls | 🟡 Partially Implemented | User access list with roles/approvals; quarterly access review records; evidence of dual authorisation for high-risk actions; leaver-access-removal timing evidence | Named individual operator accounts (no shared accounts) is a genuine strength and satisfies the core anti-repudiation requirement. However, no information was provided on role-based least privilege, quarterly access reviews, dual authorisation for high-risk operations (e.g., new BIC/RMA setup), or 24-hour leaver deprovisioning — all required sub-elements. Rated Partial pending that evidence, not a full 🟢. |

**Related control also implicated by the shared-VLAN finding:**

| Control ID | Control Name | Status | Evidence Required | Gap Notes |
|---|---|---|---|---|
| **2.1** | Internal Data Flow Security | 🟡 Partially Implemented | Data flow diagram; TLS configuration for internal SWIFT connections; certificate inventory | Not directly described, but a shared VLAN strongly suggests internal SWIFT-to-back-office/internal traffic may not be adequately segmented or encrypted. Needs explicit verification — do not assume compliance here. |
| **2.4** | Back-Office Data Flow Security *(new Mandatory in v2026)* | 🔴 Likely Not Implemented | Data flow mapping SWIFT↔back-office; mutual TLS 1.2+ evidence; dedicated interface/firewall rules | Not directly described, but this control was **promoted from Advisory to Mandatory in v2026** and a shared VLAN environment is the classic precondition for failing it. Given the network segmentation gap already identified, treat 2.4 as high-risk-of-failure until back-office data flows are explicitly mapped and tested. Many organisations that skipped 2.4 as advisory have unencrypted or unauthenticated back-office links. |

---

## Part 2 — Mandatory Controls Not Assessed (Insufficient Information)

No detail was provided on the following mandatory controls. They must still be evidenced for KYC-SA attestation and should not be assumed compliant:

1.2 OS Privileged Account Control · 1.4 Restriction of Internet Access · 2.3 System Hardening · 2.6 Operator Session Confidentiality and Integrity · 2.7 Vulnerability Scanning · 2.8 Critical Activity Outsourcing · 2.10 Application Hardening · 3.1 Physical Security · 4.1 Password Policy · 5.2 Token Management · 5.4 Physical and Logical Password Storage · 6.1 Malware Protection · 6.2 Software Integrity · 6.3 Database Integrity · 7.2 Security Training and Awareness

Recommend a follow-up evidence-gathering pass on these before assessor engagement.

---

## Part 3 — Prioritised Remediation Plan

Ranked by (a) attestation risk if unresolved, (b) fraud/breach exposure, (c) effort to remediate.

### Priority 1 — Critical (target: 30 days)

| # | Control | Action | Owner | Why now |
|---|---|---|---|---|
| 1 | **4.2** | Procure and deploy hardware OTP tokens or FIDO2 keys for all SWIFT operators; deactivate software OTP once cutover complete; update token inventory | IT Security / SWIFT Ops | Highest-risk control industry-wide; directly enables credential-theft-based fraud (Bangladesh Bank-style attacks) |
| 2 | **1.1** | Migrate SWIFT infrastructure off the shared VLAN onto a dedicated, firewalled Secure Zone segment with deny-by-default rules; eliminate any dual-homed systems | Network/Infrastructure | Foundational control — most other controls assume an isolated zone; assessors treat this as a blocking finding |
| 3 | **2.2** | Tighten patch SLA to 3 days for Critical/Emergency SWIFT advisories; stand up an accelerated emergency-patch process distinct from standard 30-day cycle; document risk-accepted exceptions where 3 days is technically infeasible | IT Security / Patch Mgmt | 27-day SLA gap is a material, easily-cited finding |

### Priority 2 — High (target: 60–90 days)

| # | Control | Action | Owner | Why |
|---|---|---|---|---|
| 4 | **6.4** | Extend log retention to 1 year hot / 3 years total; onboard Alliance Access/Gateway, OS, auth, and network logs into SIEM; implement daily review of authentication/transaction anomalies and weekly review of other events; configure automated alert rules | SOC / Security Engineering | Detection gap means fraud or intrusion could go unnoticed for months |
| 5 | **7.1** | Draft a SWIFT-specific IRP addendum: detection triggers, 24-hour SWIFT CISO notification procedure, 30-day full report process, evidence preservation, SWIFT fraud scenarios; run a tabletop exercise | InfoSec / Incident Response | Required for attestation; also closes a real response-time gap in a live-incident scenario |
| 6 | **2.4** | Map all SWIFT-to-back-office data flows; implement mutual TLS 1.2+ and dedicated firewall-restricted interfaces for back-office connections | Network/Infrastructure | Newly mandatory in v2026; likely compromised by the same shared-VLAN issue as #2 |
| 7 | **2.1** | Verify and document encryption/authentication on all internal SWIFT-zone connections following the 1.1 re-segmentation | Network/Infrastructure | Natural follow-on once the zone is isolated |

### Priority 3 — Medium (target: 90–120 days, ahead of Dec 31, 2026 attestation deadline)

| # | Control | Action | Owner | Why |
|---|---|---|---|---|
| 8 | **5.1** | Formalise quarterly access reviews, role-based least privilege, dual authorisation for high-risk actions, and a 24-hour leaver-deprovisioning SLA; document as evidence | IT Security / HR liaison | Named accounts already in place — this closes the remaining sub-requirements to move to 🟢 |
| 9 | All "not assessed" controls | Run a full evidence-gathering exercise (1.2, 1.4, 2.3, 2.6, 2.7, 2.8, 2.10, 3.1, 4.1, 5.2, 5.4, 6.1, 6.2, 6.3, 7.2) | Compliance/GRC | Needed before engaging an independent assessor for KYC-SA |

### Priority 4 — Attestation Readiness

| # | Action | Owner | Target |
|---|---|---|---|
| 10 | Engage an independent assessor (internal audit team independent of SWIFT ops, or external CSP-competent firm) for Community Standard Assessment | Compliance/GRC | After Priority 1–2 items close |
| 11 | Submit KYC-SA attestation | Compliance/GRC | Within the July 1 – Dec 31, 2026 window; do not wait until the deadline given the number of 🔴 findings |

---

## Summary Scorecard

| Rating | Count | Controls |
|---|---|---|
| 🔴 Not Implemented | 5 (assessed) + 1 (implicated) | 1.1, 2.2, 4.2, 6.4, 7.1, (2.4 likely) |
| 🟡 Partially Implemented | 2 | 2.1, 5.1 |
| 🟢 Implemented | 0 | — |
| ⚪ Not Assessed | 15 | See Part 2 |

**Bottom line:** with five confirmed 🔴 findings on mandatory controls — including two of the highest-scrutiny controls in the framework (1.1 environment isolation and 4.2 MFA) — this organisation is **not currently attestation-ready**. None of the described gaps are unusual (all appear in SWIFT's list of most common non-compliance patterns), and all are remediable within the July–December 2026 window if Priority 1 items start immediately. I'd recommend closing the 15 "not assessed" controls' evidence gaps in parallel with remediation so the independent assessor engagement isn't delayed.
