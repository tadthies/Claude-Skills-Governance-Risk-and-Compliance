# FedRAMP Authorization Process: From Start to Finish

## Overview

FedRAMP (Federal Risk and Authorization Management Program) provides a standardized approach to security assessment, authorization, and continuous monitoring for cloud products and services used by U.S. federal agencies. As of July 2026, the program has undergone significant changes under CR26 (Certification Reform 2026), which every new CSP (Cloud Service Provider) should understand before beginning the authorization journey.

---

## The FedRAMP Authorization Process: Step by Step

### Phase 1: Preparation & Readiness

**1. Determine Your Certification Class (CR26)**
Under CR26, the traditional Low/Moderate/High impact levels are being replaced with Certification Classes A–D:
- **Class A** (Basic): Low-impact, limited federal data sensitivity
- **Class B** (Standard): Most CSPs handling non-classified government data; replaces Moderate
- **Class C** (Enhanced): High-impact; law enforcement, financial, health data
- **Class D** (Specialized): Critical/ultra-sensitive systems

Classify your system based on the type of federal data you will process, store, or transmit.

**2. Choose Your Authorization Path**
- **FedRAMP 20x** (primary/preferred): Continuous authorization, modular API-driven submissions, automated evidence collection, OSCAL-native. This is now the primary authorization pathway.
- **Legacy Agency Authorization package**: Still available for complex systems during the CR26 transition period. Uses traditional SSP/SAP/SAR templates.

> **Note**: FedRAMP Ready designation retired on July 28, 2026. No new FedRAMP Ready designations are being issued. CSPs must pursue FedRAMP 20x or initiate a full authorization package.

**3. Define Your Authorization Boundary**
Everything that processes, stores, or transmits federal data must be inside the boundary. External services connected to in-scope systems must either be FedRAMP-authorized or documented with compensating controls.

**4. Select and Engage a 3PAO**
A **Third Party Assessment Organization (3PAO)** is an accredited independent assessor required for FedRAMP authorization. The 3PAO:
- Prepares the Security Assessment Plan (SAP)
- Conducts the independent security assessment
- Produces the Security Assessment Report (SAR)

CSPs do not perform their own assessments — this must be done by an accredited 3PAO. Choose your 3PAO early, as scheduling can take time.

**5. Build Your Documentation Package**
The core FedRAMP authorization package includes:
```
Authorization Package
├── System Security Plan (SSP) + Appendices A–Q
├── Security Assessment Plan (SAP) + Appendices A–D   [3PAO-prepared]
├── Security Assessment Report (SAR) + Appendices A–F  [3PAO-prepared]
└── Plan of Action & Milestones (POA&M)               [SSP Appendix O]
```

**6. OSCAL Requirement**
All authorization packages must be submitted in OSCAL (Open Security Controls Assessment Language) machine-readable format by **September 30, 2026** per RFC-0024. Begin building OSCAL-native tooling now.

---

### Phase 2: Security Assessment

**7. 3PAO Assessment**
The 3PAO conducts the formal security assessment against NIST SP 800-53 Rev 5 controls (the current baseline). They test implemented controls, review documentation, and conduct interviews with system personnel.

**8. Resolve Findings / Update POA&M**
After assessment, CSPs address findings. Critical and High findings typically must be resolved before authorization. Lower-risk findings may be accepted with a POA&M entry.

---

### Phase 3: Authorization

**9. Agency Authorization Review**
Under CR26, the FedRAMP PMO is the sole authorization body (JAB P-ATO has been fully suspended). An Agency AO (Authorizing Official) reviews the complete package and issues an ATO (Authority to Operate).

**10. ATO Issued**
The ATO is the formal authorization to operate within the federal environment. It is typically granted for 3 years, subject to continuous monitoring.

---

### Phase 4: Continuous Monitoring (ConMon)

Post-authorization compliance is ongoing:

**Monthly Requirements:**
- Submit vulnerability scan results to agency AOs
- Update POA&M (open findings, remediation progress)
- Update system inventory (new/removed assets)
- Submit ConMon Monthly Executive Summary

**Annual Requirements:**
- Full security assessment by 3PAO
- Updated SSP and appendices
- Tested Incident Response Plan (IRP) and Contingency Plan (CP)
- Updated SAR and POA&M

**Security Inbox Requirement (effective January 5, 2026):**
All authorized CSPs must maintain a dedicated Security Inbox with no CAPTCHAs or barriers for urgent vulnerability directives.

---

## Agency ATO vs. JAB P-ATO: What You Need to Know

### Agency ATO
- **What it is**: An ATO issued by a specific federal agency's Authorizing Official (AO) after reviewing the full authorization package
- **Sponsor**: A single federal agency that agrees to be your sponsor and review your package
- **Scope**: Initially authorizes you to operate for that one agency; other agencies can reuse the authorization via the FedRAMP Marketplace
- **Timeline**: Typically 9–18 months from package initiation to ATO
- **Best for**: CSPs with an existing federal agency customer willing to sponsor them

### JAB P-ATO (Joint Authorization Board Provisional ATO)
- **Status as of CR26**: **Fully suspended.** The JAB (Joint Authorization Board, comprising DoD, DHS, and GSA CIOs) is no longer issuing P-ATOs. This path is no longer available.
- **Historical context**: JAB P-ATO was a rigorous, government-wide authorization that granted broad federal marketability but was notoriously slow (18–24+ months) and had limited throughput.

**Bottom line**: As of CR26, Agency ATO (now funneled through the FedRAMP PMO) is the only path available.

---

## Recommendation for First Authorization

For a first-time authorization as a cloud software vendor, we recommend:

1. **Pursue FedRAMP 20x** — This is now the primary pathway and is designed to be faster, more automated, and more scalable than the legacy process. It uses machine-readable OSCAL packages and continuous authorization concepts.

2. **Find an agency sponsor early** — Identify a federal agency customer willing to sponsor your authorization. This relationship is critical; without it, you cannot initiate the process.

3. **Target Class B (Standard)** for most SaaS offerings — Unless your product specifically handles law enforcement, health, or financial data (which would likely require Class C/High), Class B covers the majority of federal use cases.

4. **Engage a 3PAO now** — 3PAOs have limited capacity and booking early is essential. Your 3PAO will be a key partner throughout the process.

5. **Invest in OSCAL tooling** — With the September 30, 2026 OSCAL mandate, building OSCAL-native processes from the start avoids costly retrofitting.

6. **Plan for ConMon from day one** — Authorization is not the finish line. Build the operational capacity for monthly vulnerability scanning, POA&M management, and annual reassessments into your team structure and budget before you begin.

---

*Use official FedRAMP templates from fedramp.gov — this content should be inserted into the appropriate template section.*
