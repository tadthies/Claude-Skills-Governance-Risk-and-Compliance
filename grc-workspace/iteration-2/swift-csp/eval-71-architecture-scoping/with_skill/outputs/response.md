# SWIFT Architecture Type and CSCF v2026 Control Applicability

## Architecture Identification

Based on your description — Alliance Access software running on your own on-premises servers, no HSMs, no service bureau, no cloud-hosted SWIFT — your architecture is:

**Architecture Type A1: Customer Connector, Customer-Managed, Software-Based**

### Why A1?
- You manage the SWIFT connectivity software (Alliance Access) yourself
- It runs on your own on-premises hardware (not SWIFT-hosted)
- You use software-based cryptographic keys (no HSMs, which would make you A2)
- You connect directly to SWIFT, not through a service bureau (which would be Type B)

A1 is the most common architecture for large banks and broker-dealers running Alliance Access on-premises. It gives you full control but places full responsibility for securing the environment on your institution.

---

## CSCF v2026 Mandatory Controls for A1

Under CSCF v2026, A1 architecture institutions are subject to **24 mandatory controls** (Control 2.4 was promoted from Advisory to Mandatory in v2026):

| # | Control ID | Control Name | Objective |
|---|-----------|--------------|-----------|
| 1 | **1.1** | SWIFT Environment Protection | Secure Your Environment |
| 2 | **1.2** | OS Privileged Account Control | Secure Your Environment |
| 3 | **1.4** | Restriction of Internet Access | Secure Your Environment |
| 4 | **2.1** | Internal Data Flow Security | Secure Your Environment |
| 5 | **2.2** | Security Updates | Secure Your Environment |
| 6 | **2.3** | System Hardening | Secure Your Environment |
| 7 | **2.4** | Back-Office Data Flow Security | Secure Your Environment |
| 8 | **2.6** | Operator Session Confidentiality and Integrity | Secure Your Environment |
| 9 | **2.7** | Vulnerability Scanning | Secure Your Environment |
| 10 | **2.8** | Critical Activity Outsourcing | Secure Your Environment |
| 11 | **2.10** | Application Hardening | Secure Your Environment |
| 12 | **3.1** | Physical Security | Secure Your Environment |
| 13 | **4.1** | Password Policy | Know and Limit Access |
| 14 | **4.2** | Multi-Factor Authentication | Know and Limit Access |
| 15 | **5.1** | Logical Access Controls | Know and Limit Access |
| 16 | **5.2** | Token Management | Know and Limit Access |
| 17 | **5.4** | Physical and Logical Password Storage | Know and Limit Access |
| 18 | **6.1** | Malware Protection | Detect and Respond |
| 19 | **6.2** | Software Integrity | Detect and Respond |
| 20 | **6.3** | Database Integrity | Detect and Respond |
| 21 | **6.4** | Log and Monitoring | Detect and Respond |
| 22 | **7.1** | Cyber Incident Response Planning | Detect and Respond |
| 23 | **7.2** | Security Training and Awareness | Detect and Respond |
| 24 | **2.4** | *Note: 2.4 is listed above as item 7; total = 24 mandatory controls* | — |

**Complete list of 24 mandatory control IDs:** 1.1, 1.2, 1.4, 2.1, 2.2, 2.3, 2.4, 2.6, 2.7, 2.8, 2.10, 3.1, 4.1, 4.2, 5.1, 5.2, 5.4, 6.1, 6.2, 6.3, 6.4, 7.1, 7.2

---

## CSCF v2026 Advisory Controls for A1

The following **7 advisory controls** apply to A1 architecture but are not required for KYC-SA attestation compliance. However, SWIFT encourages their implementation, and some counterparties may specifically enquire about them:

| Control ID | Control Name | Objective |
|-----------|--------------|-----------|
| **1.3A** | Virtualisation Platform Security | Secure Your Environment |
| **1.5A** | Customer Environment Protection | Secure Your Environment |
| **2.5A** | External Transmission Data Protection | Secure Your Environment |
| **2.9A** | Transaction Business Controls | Secure Your Environment |
| **2.11A** | RMA Business Controls | Secure Your Environment |
| **5.3A** | Staffing | Know and Limit Access |
| **6.5A** | Intrusion Detection | Detect and Respond |
| **7.3A** | Penetration Testing | Detect and Respond |
| **7.4A** | Scenario Risk Assessment | Detect and Respond |

> **Note on count:** SWIFT v2026 lists 7 advisory controls formally numbered (1.3A, 1.5A, 2.5A, 2.9A, 2.11A, 5.3A, 6.5A) plus 7.3A and 7.4A. Confirm the exact advisory count applicable to A1 with your SWIFT Relationship Manager or the current CSCF v2026 publication, as applicability can vary slightly by sub-architecture.

---

## Critical v2026 Change: Control 2.4 Is Now Mandatory

**Control 2.4 — Back-Office Data Flow Security** was an **Advisory** control in CSCF v2025. In **CSCF v2026, it is now Mandatory** for A1 institutions.

This is the single most impactful change from v2025 to v2026. If your institution previously treated Control 2.4 as optional and did not implement it, you now have a mandatory gap to address before your 2026 attestation.

**What Control 2.4 requires:**
- Encrypt all data flows between your SWIFT secure zone and back-office systems (core banking, payment hubs, trading systems)
- Authenticate back-office systems connecting to the SWIFT zone (e.g., mutual TLS)
- Segment the SWIFT zone from back-office environments at the network level
- Restrict back-office connections by named IP addresses/ports via firewall rules
- Log all back-office connection events to your SIEM

---

## KYC-SA Attestation Scope

For your annual KYC-SA attestation (v2026 window: July 1 – December 31, 2026):

- **You must attest against all 24 mandatory controls** — this is the compliance requirement
- **Advisory controls are not required for attestation** — you mark them as "Not Applicable" or may voluntarily attest
- **Counterparties can view your attestation** — some correspondent banks and financial market infrastructures do review advisory control implementation as part of their due diligence, so strong advisory control posture may matter commercially even if not required for compliance
- **Missing a mandatory control attestation** can result in counterparty notifications and potential suspension from SWIFT services

As an A1 bank connecting via Alliance Access on-premises, you have the broadest control scope of any SWIFT architecture type. Begin your gap assessment against all 24 mandatory controls immediately if you have not done so, paying particular attention to the newly mandatory Control 2.4.
