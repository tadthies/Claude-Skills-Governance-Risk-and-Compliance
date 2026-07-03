# SWIFT CSCF v2026 Gap Assessment

**Assessment Date:** July 2, 2026
**Framework Version:** CSCF v2026
**Attestation Window:** July 1 – December 31, 2026

Based on the current state information provided, below is a structured gap assessment against the CSCF v2026 mandatory controls.

---

## Gap Assessment Results

| Control ID | Control Name | Status | Current State | Gap / Finding | Evidence Required |
|-----------|--------------|--------|--------------|---------------|-------------------|
| **1.1** | SWIFT Environment Protection | 🔴 RED | SWIFT zone on shared VLAN with other internal systems | **Critical gap**: SWIFT zone must be a dedicated, isolated network segment. Shared VLAN violates the fundamental requirement for a hardened SWIFT secure zone. Dual-homed systems and shared infrastructure are not permitted. | Network topology diagram showing dedicated VLAN; firewall rule set restricting traffic to/from SWIFT zone; no shared switches or segments with non-SWIFT systems |
| **1.2** | OS Privileged Account Control | 🟡 UNKNOWN | Not stated | Insufficient information provided — assess separately | Evidence of separate admin accounts; privileged access management logs |
| **1.4** | Restriction of Internet Access | 🟡 UNKNOWN | Not stated | Insufficient information provided — assess separately | Firewall rules blocking internet from SWIFT zone; no internet-capable browsers on SWIFT servers |
| **2.1** | Internal Data Flow Security | 🟡 UNKNOWN | Not stated | Insufficient information provided — assess separately | Data flow diagram; encryption evidence for SWIFT internal zone traffic |
| **2.2** | Security Updates | 🔴 RED | Critical vulnerabilities patched within 30 days | **Critical gap**: CSCF v2026 requires critical patches applied within **3 days** (not 30 days). A 30-day SLA is 10x over the SWIFT limit for critical vulnerabilities. High-severity patches must be applied within 90 days. | Patch management policy; patch SLA documentation showing 3-day critical SLA; sample patch records; vulnerability scan reports with remediation timestamps |
| **2.3** | System Hardening | 🟡 UNKNOWN | Not stated | Insufficient information provided — assess separately | Hardening baseline (CIS or equivalent); configuration scan results |
| **2.4** | Back-Office Data Flow Security | 🔴 RED | Back-office connections to core banking system exist but are **not encrypted** | **Critical gap (newly mandatory in v2026)**: Control 2.4 was promoted from Advisory to Mandatory in v2026. Unencrypted back-office connections directly violate this control. All data flows between SWIFT zone and back-office systems must use TLS 1.2+ with mutual authentication. This gap did not require mandatory remediation in v2025 — **v2026 makes it a compliance failure**. | TLS configuration evidence; certificate inventory; network diagram of back-office connections; firewall rules restricting back-office access |
| **2.6** | Operator Session Confidentiality and Integrity | 🟡 UNKNOWN | Not stated | Insufficient information provided — assess separately | Evidence of encrypted operator sessions (TLS); no cleartext protocols |
| **2.7** | Vulnerability Scanning | 🟡 UNKNOWN | Not stated | Insufficient information provided — assess separately | Quarterly credentialed scan reports covering all SWIFT components |
| **2.8** | Critical Activity Outsourcing | 🟡 UNKNOWN | Not stated | Insufficient information provided — assess separately | Third-party contracts with security clauses; vendor assessment records |
| **2.10** | Application Hardening | 🟡 UNKNOWN | Not stated | Insufficient information provided — assess separately | Alliance Access hardening checklist; SWIFT application configuration review |
| **3.1** | Physical Security | 🟡 UNKNOWN | Not stated | Insufficient information provided — assess separately | Data centre access logs; CCTV coverage; access control list |
| **4.1** | Password Policy | 🟡 UNKNOWN | Not stated | Insufficient information provided — assess separately | Password policy document; Active Directory/LDAP settings |
| **4.2** | Multi-Factor Authentication | 🔴 RED | Software OTP (assumed from "general IT" posture) | **High probability gap**: Software-based OTP does not meet the hardware token requirement of Control 4.2. All SWIFT operators must authenticate with hardware tokens. | MFA configuration evidence; hardware token inventory; authentication logs showing MFA enforcement |
| **5.1** | Logical Access Controls | 🟡 UNKNOWN | Not stated | Insufficient information provided — assess separately | Access control matrix; quarterly access review records; role definitions |
| **5.2** | Token Management | 🟡 UNKNOWN | Not stated | Insufficient information provided — assess separately | Token lifecycle management procedure; revocation records |
| **5.4** | Physical and Logical Password Storage | 🟡 UNKNOWN | Not stated | Insufficient information provided — assess separately | Password vault evidence; encryption of stored credentials |
| **6.1** | Malware Protection | 🟡 UNKNOWN | Not stated | Insufficient information provided — assess separately | AV/EDR deployment records; SWIFT zone endpoint protection evidence |
| **6.2** | Software Integrity | 🟡 UNKNOWN | Not stated | Insufficient information provided — assess separately | Hash verification records for SWIFT software installations |
| **6.3** | Database Integrity | 🟡 UNKNOWN | Not stated | Insufficient information provided — assess separately | Database integrity check logs; change records |
| **6.4** | Log and Monitoring | 🔴 RED | Logs collected but not reviewed; 6-month retention | **Dual gap**: (1) Logs must be actively monitored/reviewed — passive collection alone fails Control 6.4. A SIEM with alerting rules is expected. (2) Minimum log retention is **1 year** — your 6-month retention falls short by 6 months. | SIEM deployment evidence; alert rules for SWIFT anomaly detection; log retention policy showing 12+ months; evidence of regular log review (e.g., review tickets/records) |
| **7.1** | Cyber Incident Response Planning | 🟡 AMBER | General IT IRP exists but no SWIFT-specific plan | **Significant gap**: A generic IT IRP does not satisfy Control 7.1. SWIFT requires a SWIFT-specific IRP covering: SWIFT-specific detection triggers, 24-hour notification obligation to SWIFT, fraud scenario playbooks for SWIFT messaging, evidence preservation procedures, and communication protocols with correspondent banks. | SWIFT-specific IRP document; test/exercise records; evidence of SWIFT security@swift.com contact details embedded in IRP |
| **7.2** | Security Training and Awareness | 🟡 UNKNOWN | Not stated | Insufficient information provided — assess separately | Training completion records for SWIFT operators; SWIFT-specific security training curriculum |

---

## Critical Findings Summary

### 🔴 RED — Must Remediate Before Attestation

| Priority | Control | Finding |
|---------|---------|---------|
| 1 | **1.1** | SWIFT zone shares VLAN with internal systems — network segregation is a hard requirement |
| 2 | **2.2** | 30-day critical patch SLA exceeds CSCF v2026 limit of **3 days** for critical vulnerabilities |
| 3 | **2.4** | Back-office connections unencrypted — **newly mandatory in v2026** (was advisory in v2025) |
| 4 | **4.2** | Software OTP does not meet hardware token requirement |
| 5 | **6.4** | Log retention only 6 months (minimum 1 year) and logs not actively reviewed |

### 🟡 AMBER — Significant Gaps Requiring Remediation

| Control | Finding |
|---------|---------|
| **7.1** | General IT IRP only — SWIFT-specific IRP required |

---

## Remediation Priorities and Timeline

Given the v2026 attestation deadline of **December 31, 2026**, and today's date of July 2, 2026, you have approximately 6 months.

| Control | Remediation Action | Estimated Effort |
|---------|-------------------|-----------------|
| 1.1 | Design and implement dedicated SWIFT VLAN with stateful firewall; remove all non-SWIFT systems from segment | 4–8 weeks |
| 2.2 | Update patch management SLA to 3 days for critical; implement emergency patching procedure | 2–4 weeks |
| 2.4 | Implement TLS 1.2+ mutual authentication on all back-office connections | 4–6 weeks |
| 4.2 | Procure and deploy hardware tokens for all SWIFT operators | 6–10 weeks |
| 6.4 | Deploy SIEM or configure existing SIEM to ingest SWIFT logs; extend retention to 12 months; establish alert rules | 4–8 weeks |
| 7.1 | Draft SWIFT-specific IRP; conduct tabletop exercise | 3–5 weeks |

**Recommendation:** Initiate all remediation workstreams simultaneously given the 6-month window. Prioritize Controls 1.1 and 2.4 first as they involve infrastructure changes with the longest lead times.
