# SWIFT CSCF Gap Assessment

**Framework:** SWIFT Customer Security Controls Framework (CSCF)
**Assessment Date:** July 2, 2026

Based on the current state information provided, below is a gap assessment against the key CSCF mandatory controls.

---

## Gap Assessment Results

| Control ID | Control Name | Status | Current State | Gap / Finding |
|-----------|--------------|--------|--------------|---------------|
| **1.1** | SWIFT Environment Protection | 🔴 RED | SWIFT zone on shared VLAN with internal systems | Network segregation is a fundamental requirement. The SWIFT secure zone must be isolated from all other internal network segments using stateful firewalls. A shared VLAN does not satisfy this requirement. |
| **2.2** | Security Updates | 🟡 AMBER | Critical vulnerabilities patched within 30 days | The CSCF sets tighter patching SLAs than standard IT practice. Critical patches should be applied significantly faster than 30 days — typically within 7–14 days for critical severity. Verify the exact SLA in your applicable CSCF version, as the specific timeframe varies. |
| **2.4** | Back-Office Data Flow Security | 🟡 AMBER/RED | Back-office connections to core banking not encrypted | Unencrypted back-office connections are a gap. Whether this is a mandatory finding depends on your CSCF version — Control 2.4 has been advisory in some versions. Verify if it is mandatory in your current applicable version. If mandatory, this is a critical finding. |
| **4.2** | Multi-Factor Authentication | 🔴 RED | Software OTP for operator MFA | Software-based OTP (TOTP apps) typically does not meet the CSCF requirement for hardware authentication tokens for SWIFT operators. Hardware tokens are required. |
| **6.4** | Log and Monitoring | 🔴 RED | Logs collected but not reviewed; 6-month retention | Two issues: (1) Passive log collection without review/monitoring is insufficient — active monitoring with alerting is required. (2) Log retention appears to fall below the 12-month minimum typically required by CSCF for SWIFT events. |
| **7.1** | Cyber Incident Response Planning | 🟡 AMBER | General IT IRP only | A SWIFT-specific incident response plan is required. A generic IT IRP does not address SWIFT-specific requirements including SWIFT notification obligations and SWIFT-specific incident scenarios. |

---

## Detailed Findings

### Control 1.1 — SWIFT Environment Protection 🔴

**Finding:** Your SWIFT zone shares a VLAN with other internal systems.

**Requirement:** The SWIFT environment must be logically and/or physically separated from the rest of your internal network. A shared VLAN with other internal systems does not provide the required isolation.

**Remediation:**
- Create a dedicated VLAN/network segment exclusively for SWIFT systems
- Implement stateful firewall rules controlling all traffic to/from the SWIFT zone
- Ensure no SWIFT servers are dual-homed to other network segments
- Document the network segmentation in a topology diagram

---

### Control 2.2 — Security Updates 🟡

**Finding:** 30-day patching for critical vulnerabilities is likely too slow for CSCF compliance.

**Requirement:** CSCF sets specific patching timelines. Critical vulnerabilities require very rapid patching — consult the current CSCF document for exact SLAs, but they are typically much tighter than 30 days.

**Remediation:**
- Establish an emergency patching process for critical SWIFT vulnerabilities
- Implement vulnerability scanning to quickly identify critical issues
- Test patches in a non-production environment but expedite production deployment

---

### Control 2.4 — Back-Office Data Flow Security 🟡/🔴

**Finding:** Back-office connections to core banking are not encrypted.

**Requirement:** Data flows between SWIFT systems and back-office systems should be protected. In recent CSCF versions this has been an advisory control, but the trend is toward mandatory status.

**Remediation:**
- Implement TLS encryption on all back-office connections
- Authenticate back-office systems with certificates
- Review the applicable CSCF version to confirm current mandatory/advisory status

---

### Control 4.2 — Multi-Factor Authentication 🔴

**Finding:** Software OTP does not meet hardware token requirements.

**Requirement:** SWIFT requires hardware authentication tokens for operator access to SWIFT systems.

**Remediation:**
- Deploy hardware OTP tokens (RSA SecurID, Thales SafeNet, or similar)
- Configure Alliance Access to require hardware-backed MFA
- Enroll all SWIFT operators

---

### Control 6.4 — Log and Monitoring 🔴

**Finding:** Logs collected but not actively reviewed; 6-month retention.

**Requirements:**
1. Active monitoring — logs must be reviewed and alerts configured, not just collected
2. Minimum retention — typically 12 months for SWIFT-related logs

**Remediation:**
- Deploy or configure SIEM for SWIFT log ingestion with alerting rules
- Extend log retention to at least 12 months
- Establish regular log review cadence and document reviews

---

### Control 7.1 — Cyber Incident Response Planning 🟡

**Finding:** General IT IRP only; no SWIFT-specific IRP.

**Requirement:** A SWIFT-specific IRP is required covering SWIFT notification obligations, SWIFT-specific incident scenarios, and evidence preservation.

**Remediation:**
- Develop a SWIFT-specific annex or standalone IRP
- Include SWIFT notification contacts and 24-hour notification obligation
- Define SWIFT-specific incident scenarios (fraudulent transactions, compromised operator, etc.)

---

## Summary of Findings

| Control | Rating | Key Issue |
|---------|--------|-----------|
| 1.1 | 🔴 RED | Shared VLAN — network segregation failure |
| 2.2 | 🟡 AMBER | 30-day patching likely too slow for CSCF |
| 2.4 | 🟡/🔴 | Unencrypted back-office connections — severity depends on CSCF version |
| 4.2 | 🔴 RED | Software OTP not compliant with hardware token requirement |
| 6.4 | 🔴 RED | No active monitoring; insufficient log retention |
| 7.1 | 🟡 AMBER | No SWIFT-specific IRP |

**Recommendation:** Address all RED findings before your KYC-SA attestation. Start with network segregation (1.1) and hardware tokens (4.2) as these require the most lead time.
