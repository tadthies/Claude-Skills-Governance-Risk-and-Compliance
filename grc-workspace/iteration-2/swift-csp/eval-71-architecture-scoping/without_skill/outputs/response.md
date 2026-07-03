# SWIFT Architecture Type and CSCF Control Applicability

## Architecture Identification

Based on your description — Alliance Access software running on your own on-premises servers, no HSMs, no service bureau — your architecture is most likely:

**Architecture Type A1: Customer Connector, Customer-Managed, Software-Based**

SWIFT defines several architecture types:
- **A1**: Software-based customer connector, fully customer-managed (Alliance Access on-premises without HSM) — this matches your setup
- **A2**: Hardware-based customer connector using HSM for key management
- **A3**: SWIFT-managed connector component (Alliance Lite2)
- **A4**: Cloud-based SWIFT connectivity
- **B**: Service bureau (third-party managed SWIFT connection)

Your Alliance Access on-premises deployment without HSMs fits Type A1. This is indeed the most common architecture for large and mid-tier banks that run their own SWIFT infrastructure.

---

## CSCF Controls for A1 Architecture

The SWIFT Customer Security Controls Framework (CSCF) organizes controls across three objectives. The specific version you should reference is the current applicable version (v2025 or v2026 depending on your attestation cycle).

### Mandatory Controls (Approximate for A1)

The mandatory controls for A1 typically include controls across all three security objectives:

**Objective 1 — Secure Your Environment:**
- 1.1 — SWIFT Environment Protection (network segregation)
- 1.2 — OS Privileged Account Control
- 1.4 — Restriction of Internet Access
- 2.1 — Internal Data Flow Security
- 2.2 — Security Updates (patching)
- 2.3 — System Hardening
- 2.6 — Operator Session Confidentiality and Integrity
- 2.7 — Vulnerability Scanning
- 2.8 — Critical Activity Outsourcing
- 2.10 — Application Hardening
- 3.1 — Physical Security

**Objective 2 — Know and Limit Access:**
- 4.1 — Password Policy
- 4.2 — Multi-Factor Authentication
- 5.1 — Logical Access Controls
- 5.2 — Token Management
- 5.4 — Physical and Logical Password Storage

**Objective 3 — Detect and Respond:**
- 6.1 — Malware Protection
- 6.2 — Software Integrity
- 6.3 — Database Integrity
- 6.4 — Log and Monitoring
- 7.1 — Cyber Incident Response Planning
- 7.2 — Security Training and Awareness

### Advisory Controls

Advisory controls in the CSCF are generally not required for attestation but SWIFT recommends their implementation:

- 1.3A — Virtualisation Platform Security
- 1.5A — Customer Environment Protection
- 2.5A — External Transmission Data Protection
- 2.9A — Transaction Business Controls
- 2.11A — RMA Business Controls
- 5.3A — Staffing
- 6.5A — Intrusion Detection
- 7.3A — Penetration Testing
- 7.4A — Scenario Risk Assessment

> **Note:** Control 2.4 (Back-Office Data Flow Security) has historically been advisory for some architecture types. You should verify in the current CSCF version whether it is mandatory or advisory for A1, as the framework evolves annually.

---

## A1 Architecture Context

A1 is the most demanding architecture from a compliance perspective as you bear full responsibility for all aspects of SWIFT environment security. Unlike service bureau (B) users who share some responsibility with their bureau, A1 users must implement all mandatory controls independently.

### Key Characteristics of A1
- Full control of the SWIFT infrastructure
- Full compliance responsibility
- Typically used by large banks, major broker-dealers, and custodians
- Alliance Access or Alliance Gateway software
- Direct SWIFT network connection (SWIFTNet Link)

---

## KYC-SA Attestation

For your annual KYC Security Attestation (KYC-SA):
- You must attest against all mandatory controls applicable to A1
- Advisory controls are generally not required for attestation but may be reviewed by counterparties
- Attestation is submitted through the SWIFT portal (swift.com/myswift)
- The attestation cycle aligns with SWIFT's annual framework versioning

**Recommendation:** Obtain the current CSCF document from swift.com to confirm the precise list of mandatory vs. advisory controls for A1 in the version applicable to your current attestation period, as control classifications can change between versions.
