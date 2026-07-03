# SWIFT CSCF v2026 Gap Assessment

**Disclaimer:** This is a preliminary self-assessment based on the details you provided. It is not a substitute for a formal review against the published SWIFT Customer Security Controls Framework (CSCF) v2026 documentation, and it should be validated by your SWIFT compliance/security team or an independent assessor before submission via the KYC-SA Security Attestation Application. Control numbering below reflects the CSCF's long-standing architecture type numbering (1.x Restrict Internet Access / Segregation, 2.x Reduce Attack Surface, 3.x Physical Security, 4.x Prevent Compromise of Credentials, 5.x Manage Identities & Segregate Privileges, 6.x Detect Anomalous Activity, 7.x Plan for Incident Response & Info Sharing) — confirm exact wording/numbering against the current v2026 CSCF PDF, as SWIFT periodically renumbers/adds controls.

---

## 1. Summary of Current State Inputs

| # | Fact Provided |
|---|---|
| 1 | SWIFT secure zone exists but sits on a shared VLAN with other internal systems |
| 2 | Critical vulnerabilities patched within 30 days |
| 3 | Operator MFA uses software OTP |
| 4 | SWIFT logs collected but not reviewed; retention only 6 months |
| 5 | General IT incident response plan exists; nothing SWIFT-specific |
| 6 | Operators use named individual accounts |

---

## 2. Control-by-Control Rating

Rating scale: **Compliant (C)**, **Partially Compliant (PC)**, **Non-Compliant (NC)**, **Not Assessed / Insufficient Info (N/A)**

### Architecture Type 1 — Restrict Internet Access & Segregate Critical Systems

**1.1 SWIFT Environment Protection** — *Mandatory*
- Requirement: The secure zone must be segregated from the general IT/enterprise network via strict access control (physical or virtual segmentation, e.g., dedicated VLAN with firewalling, not just logical labeling).
- **Rating: Non-Compliant (NC)**
- Rationale: A shared VLAN with other internal systems does not constitute segregation. Broadcast domain and often routing-level adjacency to non-SWIFT systems means the secure zone is exposed to lateral movement, ARP spoofing, VLAN hopping, and compromise pivoting from lower-trust systems. This is one of the most fundamental CSCF controls and is almost always in-scope for full compliance (not a "may implement" control).

**1.2 Operating System Privileged Account Control** — *Mandatory*
- **Rating: N/A** — insufficient information provided on OS-level privileged account controls (separate from operator app accounts).

**1.3 Virtualization Platform Protection** — *Advisory* (if applicable)
- **Rating: N/A** — not addressed.

**1.4 Restriction of Internet Access** — *Mandatory*
- **Rating: N/A** — no information given on internet access from SWIFT-related components; flag for follow-up given the shared VLAN finding (increases likelihood internet-reachable systems are adjacent).

**1.5A Customer Environment Protection (Non-Prod / A4/L2 variants, where applicable)**
- **Rating: N/A** — architecture type (A1/A2/A3/A4/AWP/L2/L2BE) not specified; needed to confirm which controls are in-scope. Recommend confirming architecture type as a pre-requisite step.

---

### Architecture Type 2 — Reduce Attack Surface & Vulnerabilities

**2.1 Internal Data Flow Security** — *Mandatory*
- **Rating: N/A** — not addressed; the shared VLAN finding raises a strong prompt to also check whether internal SWIFT-related data flows are encrypted/integrity protected.

**2.2 Security Updates (Patch Management)** — *Mandatory*
- Requirement: Timely application of security patches, with a risk-based patching cadence for critical vulnerabilities (SWIFT/CSCF guidance and most organizations' own policy commonly target ≤30 days for critical/high severity, ideally faster for actively exploited vulnerabilities).
- **Rating: Partially Compliant (PC)**
- Rationale: 30 days for critical vulnerabilities is at the outer edge of acceptable and is commonly viewed as a minimum bar, not best practice. This is compliant only if it is documented in a formal patch management policy with defined SLAs, exception/risk-acceptance process, and evidence of consistent adherence (metrics/tracking). If patching is ad hoc or undocumented, this drops to NC. Recommend tightening SLA for critical/actively-exploited CVEs (e.g., emergency patching within 72 hours–7 days) and formalizing the policy.

**2.3 System Hardening** — *Mandatory*
- **Rating: N/A** — not addressed.

**2.4A Back Office Data Flow Security** — *Advisory/Mandatory depending on architecture*
- **Rating: N/A** — not addressed.

**2.5A External Transmission Data Protection** — *Mandatory*
- **Rating: N/A** — not addressed.

**2.6 Operator Session Confidentiality & Integrity** — *Mandatory*
- **Rating: N/A** — not addressed.

**2.7 Vulnerability Scanning** — *Mandatory*
- **Rating: N/A** — patching cadence given, but no mention of a formal vulnerability scanning program (authenticated scans, cadence, coverage of SWIFT-related components). Flag for follow-up — you cannot patch on a 30-day SLA reliably without a scanning/discovery process feeding it.

**2.8 Outsourced Critical Activities** — *Advisory* (if applicable)
- **Rating: N/A**

**2.9 Transaction Business Controls** — *Advisory*
- **Rating: N/A**

**2.10 Application Hardening** — *Advisory*
- **Rating: N/A**

**2.11A RMA Business Controls** — *Advisory*
- **Rating: N/A**

---

### Architecture Type 3 — Physical Security

**3.1 Physical Security** — *Mandatory*
- **Rating: N/A** — not addressed.

---

### Architecture Type 4 — Prevent Compromise of Credentials

**4.1 Password Policy** — *Mandatory*
- **Rating: N/A** — not addressed directly, but named individual accounts (see 5.1) is a positive input; password complexity/rotation policy not described.

**4.2 Multi-Factor Authentication** — *Mandatory*
- Requirement: MFA required for all interactive access to the SWIFT-related operator/application layer, including OS-level access to critical systems, and for privileged/remote access. Token type matters for risk rating: hardware tokens/hardware-backed MFA are preferred; software OTP is acceptable but rated higher-risk than hardware, and SWIFT's guidance notes a preference hierarchy (hardware token > software token on a separate device > software token on the same device as the client).
- **Rating: Partially Compliant (PC)**
- Rationale: Software OTP satisfies the letter of the MFA requirement (a control is in place), so this is not an outright NC — but it is weaker than hardware-token MFA, particularly if the software OTP resides on the same general-purpose device/workstation used to access SWIFT (which would be a materially higher risk, especially combined with the shared-VLAN finding). Confirm: (a) is the OTP app on a separate, dedicated, hardened device from the SWIFT workstation; (b) is MFA enforced for ALL operators including admins and for remote/dial-up access; (c) is MFA also required at OS/hypervisor level for privileged accounts, not just the messaging interface. If software OTP resides on the same device as SWIFT access, downgrade to NC-equivalent risk in your internal risk register even though the assertion may technically pass.

---

### Architecture Type 5 — Manage Identities & Segregate Privileges

**5.1 Logical Access Control** — *Mandatory*
- Requirement: Access is granted based on individual accountability (named accounts, no shared/generic IDs), least privilege, and need-to-know/need-to-use.
- **Rating: Compliant (C)** — provisionally
- Rationale: Named individual accounts is exactly what this control requires and is a genuine strength. To confirm full compliance, verify: (a) no shared/generic/service accounts are used for interactive operator access, (b) access is periodically recertified, (c) least-privilege role mapping exists (not just individually named but over-privileged accounts), and (d) joiner/mover/leaver deprovisioning is timely. Provisional "Compliant" pending confirmation of these details.

**5.2 Token Management** — *Mandatory*
- **Rating: N/A** — related to 4.2; not enough detail on how software OTP tokens/seeds are provisioned, stored, and revoked.

**5.3A Personnel Vetting Process** — *Advisory*
- **Rating: N/A**

**5.4 Physical and Logical Password Storage** — *Mandatory*
- **Rating: N/A**

---

### Architecture Type 6 — Detect Anomalous Activity

**6.1 Malware Protection** — *Mandatory*
- **Rating: N/A** — not addressed.

**6.2 Software Integrity** — *Mandatory*
- **Rating: N/A**

**6.3 Database Integrity** — *Mandatory*
- **Rating: N/A**

**6.4 Logging and Monitoring** — *Mandatory*
- Requirement: Logging of security events across the SWIFT environment, with active review/monitoring (not just collection) and defined retention sufficient for investigation needs (SWIFT/CSCF expectation and common industry baseline is a minimum of 12 months retention, often longer per local regulation).
- **Rating: Non-Compliant (NC)**
- Rationale: Two independent failures here: (1) logs are collected but not reviewed — a SIEM/log repository with no monitoring or alerting process provides no actual detection capability, which is the core intent of this control; (2) 6-month retention falls short of the ~12-month (or greater) expectation used for forensic/investigative purposes and is likely below your regulator's/SWIFT's expected minimum. This is a high-priority gap because it directly undermines your ability to detect and investigate fraud or compromise — the primary purpose of the CSCF's detect category.

**6.5A Intrusion Detection** — *Advisory*
- **Rating: N/A** — closely related to 6.4; if logs aren't reviewed, any IDS/IPS alerting is also likely not being actioned. Flag for review.

---

### Architecture Type 7 — Plan for Incident Response & Information Sharing

**7.1 Cyber Incident Response Planning** — *Mandatory*
- Requirement: A documented incident response plan specifically covering SWIFT-related systems/scenarios (e.g., fraudulent transaction, compromised operator credentials, unauthorized message injection), including roles, escalation paths, communication plan, and integration with SWIFT's own incident notification obligations, tested periodically (tabletop/simulation).
- **Rating: Non-Compliant (NC)**
- Rationale: A general IT incident response plan is a good foundation but does not satisfy this control, which specifically requires SWIFT-relevant scenarios and procedures (e.g., how to isolate the SWIFT environment, who contacts SWIFT/correspondent banks, how to handle a suspected fraudulent payment, coordination with the CSP's own SWIFT-specific runbooks). Absence of SWIFT-specific IR planning combined with the logging gaps in 6.4 compounds risk materially — you would struggle to detect an incident and would not have a tested plan to respond to one.

**7.2 Security Training and Awareness** — *Mandatory*
- **Rating: N/A** — not addressed.

**7.3A Penetration Testing** — *Advisory*
- **Rating: N/A**

**7.4A Scenario Risk Assessment** — *Advisory*
- **Rating: N/A**

---

## 3. Rating Summary Table

| Control | Title | Rating | Severity of Gap |
|---|---|---|---|
| 1.1 | SWIFT Environment Protection | **NC** | Critical |
| 2.2 | Security Updates | **PC** | Medium |
| 4.2 | Multi-Factor Authentication | **PC** | Medium-High (verify token placement) |
| 5.1 | Logical Access Control | **C** (provisional) | Low — verify details |
| 6.4 | Logging and Monitoring | **NC** | Critical |
| 7.1 | Cyber Incident Response Planning | **NC** | High |

All other mandatory/advisory controls: **N/A — insufficient information**, listed above for completeness and follow-up data collection.

---

## 4. Prioritised Remediation Plan

### Priority 1 — Critical (target: 0–30 days to start; complete within 90 days)

**P1-A. Segregate the SWIFT secure zone (Control 1.1)**
- Move SWIFT-related components (messaging interface, HSM/tokens, connector, jump servers) onto a dedicated, physically or strictly logically segregated VLAN/network segment with dedicated firewalling — not just VLAN tagging shared with other internal traffic.
- Implement default-deny firewall rules between the SWIFT zone and the rest of the internal network; only allow explicitly required flows (documented data flow diagram).
- Deploy jump servers/bastion hosts as the sole access path into the zone, with MFA enforced at that boundary.
- Validate with an internal network segmentation test (and ideally a penetration test) post-implementation.
- *Why first:* This is the foundational control the CSCF architecture is built around; every other control's effectiveness is undermined if the zone itself isn't segregated. It is also the gap most likely to trigger a compliance failure/attestation issue.

**P1-B. Stand up active log review and extend retention (Control 6.4)**
- Immediate: extend log retention from 6 months to a minimum of 12 months (confirm current v2026 CSCF and your regulatory requirements — some jurisdictions require longer).
- Implement a daily/near-real-time log review process — either a SIEM with defined use cases/alert rules for SWIFT-relevant events (failed logins, privilege escalation, off-hours access, message modification attempts) or, at minimum, a documented manual daily review procedure with sign-off.
- Assign clear ownership (SOC, security team, or designated reviewer) and define escalation criteria.
- *Why first:* Without active monitoring, a compromise (including one exploiting the shared-VLAN weakness) could go undetected indefinitely. This pairs directly with P1-A — segmentation reduces the attack surface, monitoring catches what gets through.

### Priority 2 — High (target: 30–90 days)

**P2-A. Build a SWIFT-specific incident response plan (Control 7.1)**
- Extend/branch the existing general IT IR plan with a SWIFT-specific annex covering: suspected fraudulent payment, compromised operator credentials, unauthorized/altered SWIFT message, HSM/token compromise, and correspondent bank/SWIFT notification procedures.
- Define roles (who can halt outbound payments, who liaises with SWIFT and correspondent banks), escalation timelines, and communication templates.
- Run a tabletop exercise within the 90-day window to validate the plan.
- Align with SWIFT's own guidance on incident notification obligations under the CSCF/attestation framework.

**P2-B. Tighten MFA implementation for operators (Control 4.2)**
- Confirm software OTP tokens are hosted on a separate, dedicated, hardened device — not the same workstation used for SWIFT access. If they are co-located, remediate immediately (treat as equivalent to P1 given compounding risk with the VLAN issue).
- Extend MFA enforcement to cover OS-level/privileged access to all SWIFT-related components, not just the operator application layer.
- Evaluate roadmap to hardware tokens for highest-privilege operators/admins as a medium-term uplift (even if software OTP remains acceptable for standard operators).

### Priority 3 — Medium (target: 90–180 days)

**P3-A. Formalize and tighten patch management (Control 2.2)**
- Document a formal patch management policy with SLA tiers (e.g., critical/actively exploited: ≤7 days or emergency out-of-cycle; high: ≤30 days; medium/low: defined longer windows).
- Implement or confirm a vulnerability scanning program (Control 2.7) feeding the patch process, with regular authenticated scans of SWIFT-related components.
- Track and report patch compliance metrics to management.

**P3-B. Close information gaps via full CSCF self-assessment**
- Confirm your SWIFT architecture type (A1/A2/A3/A4/AWP/L2/L2BE) to finalize the exact mandatory/advisory control set that applies.
- Complete a full control-by-control review for all N/A items above (physical security, hardening, malware protection, data flow encryption, vulnerability scanning, token management, personnel vetting, training, etc.).
- Update the KYC-SA attestation once P1 and P2 items are remediated.

---

## 5. Key Risk Narrative (for management reporting)

The most material risk in your current environment is the **combination** of a non-segregated SWIFT zone (1.1) with **no active log review** (6.4). This pairing means the environment most susceptible to lateral compromise from adjacent internal systems is also the one least likely to have an intrusion detected in time to respond. The absence of a SWIFT-specific incident response plan (7.1) compounds this further — even if an incident were detected, the organization's ability to respond quickly (e.g., halting fraudulent payments, notifying SWIFT/correspondents) is untested and not clearly defined. Recommend treating P1-A and P1-B as a single urgent remediation program, with executive sponsorship and a fixed 90-day deadline, given their direct bearing on both fraud risk and attestation compliance.

---

## 6. Recommended Next Steps

1. Confirm SWIFT architecture type and full in-scope component inventory to complete the N/A-rated controls above.
2. Commission an independent penetration test / segmentation test focused on the SWIFT zone before and after remediation.
3. Assign an executive owner and project-manage P1 items on a 30/60/90-day tracked plan.
4. Re-run this gap assessment (or a full CSCF self-assessment) after P1 and P2 remediations to update your KYC-SA attestation with accurate ratings.
5. Consider engaging a SWIFT-experienced third-party assessor for independent validation prior to attestation submission, particularly given the criticality of the segmentation finding.
