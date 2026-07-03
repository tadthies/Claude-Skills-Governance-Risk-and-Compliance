# Your SWIFT Architecture Type: A1

Based on what you've described — **Alliance Access running on your own premises, self-managed, software-based key storage (no HSMs), no service bureau, no cloud-hosted SWIFT connectivity** — you are **Architecture Type A1 (Customer connector, customer-managed, software-based)**.

Why not the others:
- **Not A2** — A2 is also customer-managed but *hardware*-based (HSM-backed key storage). You explicitly have no HSMs, so you don't meet A2.
- **Not A3** — A3 is a SWIFT-managed connector (e.g., Alliance Lite2 / SWIFT-hosted component). You're running Alliance Access yourselves, not a SWIFT-hosted component.
- **Not A4** — A4 is SWIFT-defined cloud connectivity (SWIFT Cloud). You are explicitly not cloud-hosted.
- **Not B** — B is a service bureau connection managed by a third party. You connect directly and manage it yourselves.

**Note:** Confirm this self-assessment against your actual Alliance Access deployment configuration (key/token storage method in particular) before submitting your KYC-SA attestation — A1 vs. A2 hinges specifically on whether cryptographic material is hardware- or software-protected.

---

# CSCF v2026 Applicability Matrix — Architecture Type A1

25 Mandatory + 7 Advisory controls, all applicable to A1 (A1 is in scope for the full control set — no controls are excluded for this architecture type, unlike A3/A4 which are exempt from Control 1.2).

| Control | Name | Status for A1 | Objective |
|---------|------|----------------|-----------|
| 1.1 | SWIFT Environment Protection | ✅ Mandatory | 1 — Secure Your Environment |
| 1.2 | OS Privileged Account Control | ✅ Mandatory | 1 |
| 1.3A | Virtualisation Platform Security | 🔶 Advisory | 1 |
| 1.4 | Restriction of Internet Access | ✅ Mandatory | 1 |
| 1.5A | Customer Environment Protection | 🔶 Advisory | 1 |
| 2.1 | Internal Data Flow Security | ✅ Mandatory | 1 |
| 2.2 | Security Updates | ✅ Mandatory | 1 |
| 2.3 | System Hardening | ✅ Mandatory | 1 |
| **2.4** | **Back-Office Data Flow Security** | ✅ **Mandatory — NEW in v2026 (was Advisory in v2025)** | 1 |
| 2.5A | External Transmission Data Protection | 🔶 Advisory | 1 |
| 2.6 | Operator Session Confidentiality and Integrity | ✅ Mandatory | 1 |
| 2.7 | Vulnerability Scanning | ✅ Mandatory | 1 |
| 2.8 | Critical Activity Outsourcing | ✅ Mandatory | 1 |
| 2.9A | Transaction Business Controls | 🔶 Advisory | 1 |
| 2.10 | Application Hardening | ✅ Mandatory | 1 |
| 2.11A | RMA Business Controls | 🔶 Advisory | 1 |
| 3.1 | Physical Security | ✅ Mandatory | 1 |
| 4.1 | Password Policy | ✅ Mandatory | 2 — Know and Limit Access |
| 4.2 | Multi-Factor Authentication | ✅ Mandatory | 2 |
| 5.1 | Logical Access Controls | ✅ Mandatory | 2 |
| 5.2 | Token Management | ✅ Mandatory | 2 |
| 5.3A | Staffing | 🔶 Advisory | 2 |
| 5.4 | Physical and Logical Password Storage | ✅ Mandatory | 2 |
| 6.1 | Malware Protection | ✅ Mandatory | 3 — Detect and Respond |
| 6.2 | Software Integrity | ✅ Mandatory | 3 |
| 6.3 | Database Integrity | ✅ Mandatory | 3 |
| 6.4 | Log and Monitoring | ✅ Mandatory | 3 |
| 6.5A | Intrusion Detection | 🔶 Advisory | 3 |
| 7.1 | Cyber Incident Response Planning | ✅ Mandatory | 3 |
| 7.2 | Security Training and Awareness | ✅ Mandatory | 3 |
| 7.3A | Penetration Testing | 🔶 Advisory | 3 |
| 7.4A | Scenario Risk Assessment | 🔶 Advisory | 3 |

**Totals for A1: 25 Mandatory, 7 Advisory (the full 32-control set applies to you).**

---

## The One Thing That Changed for You This Cycle: Control 2.4

**Control 2.4 — Back-Office Data Flow Security** moved from Advisory to **Mandatory** in CSCF v2026. As an on-premises Alliance Access shop, you almost certainly have connections between the SWIFT secure zone and back-office systems (core banking, payment hub, trading platforms) — this control now directly applies to you and must be attested.

**What it requires:**
- Encrypted data flows between the SWIFT secure zone and back-office systems
- Authentication of back-office systems connecting into the SWIFT zone
- Prevention of unauthorized data exfiltration via back-office channels
- Network segmentation between the SWIFT zone and back-office environment

**v2026 scope note:** SWIFT's phased rollout means encryption is required now between the general IT environment and the secure SWIFT infrastructure (including flows via any bridging server). Legacy direct connections and the "first hop" from a bridging server to back-office systems are **not yet mandatory** — SWIFT has signaled full enforcement there for v2028. Don't use this phase-in as a reason to defer — start remediation now.

**Common gap for on-prem Alliance Access deployments:** unencrypted or unauthenticated messaging between Alliance Access and the back-office payment hub, often on a shared VLAN with no mutual TLS.

**Remediation approach:**
1. Map all data flows between the SWIFT secure zone and back-office systems.
2. Implement TLS 1.2+ with certificate-based mutual authentication on all connections.
3. Route all back-office connections through a dedicated interface within the secure zone.
4. Apply firewall rules restricting back-office access to named IPs/ports only.
5. Log all back-office connection events to your SIEM (supports Control 6.4 too).

---

## Priority Controls Given Your Profile (On-Prem, No HSM)

Because you're software-based (A1, not A2), a few controls deserve particular attention:

1. **4.2 — Multi-Factor Authentication.** Since you have no HSMs, your operator authentication and any application-level key protection rely more heavily on software controls. Hardware OTP tokens, smart cards with PIN, or FIDO2 keys are required for interactive SWIFT sessions — software-based OTP on shared devices does **not** satisfy this for A1.
2. **2.4 — Back-Office Data Flow Security.** New mandatory control this cycle — see above.
3. **1.1 — SWIFT Environment Protection.** Confirm your Alliance Access/Gateway servers sit in a dedicated secure zone with no dual-homing and deny-by-default firewall rules — this is the most commonly cited finding in assessments generally.
4. **2.10 — Application Hardening.** Apply SWIFT's published Security Hardening Guide specifically for Alliance Access (and Alliance Gateway if deployed).
5. **5.4 — Physical and Logical Password Storage.** With no HSM to offload key/credential protection, ensure SWIFT credentials sit in an approved PAM/vault solution, not flat files or spreadsheets.
6. **6.4 — Log and Monitoring.** Ensure your SIEM ingests Alliance Access/Gateway logs with 1-year hot / 3-year total retention and daily anomaly review.

---

## Attestation Timeline

| Activity | Timing |
|----------|--------|
| v2026 attestation window opens | July 1, 2026 |
| Assessment period | July 1 – December 31, 2026 |
| KYC-SA attestation deadline | December 31, 2026 |
| Assessment type | Community-standard independent assessment (self-attestation alone is generally no longer sufficient) |

As an on-premises A1 institution, you'll need an independent assessment (internal audit function with appropriate independence, or external assessor) covering all 25 mandatory controls, submitted via the KYC-SA portal within this window.

---

*Verify this applicability mapping against the official CSCF v2026 documentation on the SWIFT Knowledge Centre (swift.com/myswift) before finalizing your attestation — SWIFT can adjust control status and architecture applicability between publication and your assessment date.*
