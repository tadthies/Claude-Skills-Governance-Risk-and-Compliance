# CMMC Level 2 Gap Assessment

**Date:** July 3, 2026
**Scope:** CMMC Level 2 / NIST SP 800-171 Rev. 2 (110 practices), based on the current-state facts provided
**Disclaimer:** This is a preliminary desk-based gap assessment from the facts supplied. It is not a substitute for a formal SPRS self-assessment, a C3PAO Level 2 certification assessment, or a documented System Security Plan (SSP) review. All practice ratings below are estimates pending evidence review (policies, configs, screenshots, interviews).

---

## 1. Executive Summary

Based on the seven facts provided, this organization has **material gaps** in at least five NIST SP 800-171 practice families. The most severe issues — flat network with CUI on shared drives, no FIPS-validated encryption for CUI at rest, and MFA limited to cloud email only — represent foundational Access Control (AC) and System & Communications Protection (SC) failures that will drive a **significantly negative SPRS score** and block CMMC Level 2 certification until remediated.

**Estimated current SPRS score: approximately -30 to -45 (out of a possible 110)**, depending on how many of the ~110 practices are fully met versus how many "NOT MET" findings apply. Given the scope of gaps described (which touch high-weighted practices), a realistic working estimate is in the **-40 to -50 range** — well below the 88 threshold generally expected for POA&M eligibility under the interim/current DoD scoring methodology, and far below 110 (full compliance).

**Certification readiness: NOT READY.** Multiple Tier 1 ("NOT MET" = automatic disqualifiers if not on an approved POA&M with a closure plan) and Tier 2 gaps exist. Recommend a 90–120 day remediation sprint before engaging a C3PAO or submitting a SPRS self-assessment.

---

## 2. Methodology & Scoring Model Used

CMMC Level 2 / DoD Assessment Methodology (per NIST SP 800-171 DoD Assessment Methodology, version 1.2.1) scores against a **maximum of 110 points** (one point per practice, assuming full implementation of all 110 practices). Points are **subtracted** for each practice that is NOT MET, weighted as follows:

| Weight | Point Deduction | Typical Practice Examples |
|---|---|---|
| Weight 5 | -5 points | High-impact practices (e.g., MFA, encryption of CUI, boundary protection) |
| Weight 3 | -3 points | Moderate-impact practices (e.g., several AC, IR practices) |
| Weight 1 | -1 point | Lower-impact / foundational practices (e.g., policy documentation) |

A small subset of Weight-1 practices allow POA&M (Plan of Action & Milestones) closure within 180 days at the "NOT MET" state and still permit conditional certification; most Weight-3 and Weight-5 practices related to core security functions (encryption, MFA, boundary protection) generally do **not** qualify for POA&M treatment under CMMC 2.0 rules — they must be MET at time of assessment, with only a very limited set of practices eligible for POA&M. **Assume none of the gaps below are POA&M-eligible unless explicitly noted**, and validate against the current 32 CFR Part 170 rule text and DoD guidance at assessment time.

---

## 3. Practice-by-Practice Gap Rating

### 3.1 Access Control (AC) — **PARTIALLY MET / NOT MET (multiple sub-practices)**

| Practice ID | Practice | Rating | Rationale |
|---|---|---|---|
| AC.L2-3.1.1 | Limit system access to authorized users | Partially Met | No segmentation implies access is broader than necessary; likely over-permissioned |
| AC.L2-3.1.3 | Control CUI flow per approved authorizations | **Not Met** | Flat network + CUI on shared drives = no controlled CUI flow |
| AC.L2-3.1.5 | Least privilege | **Not Met** | Shared drives with CUI strongly suggest no least-privilege enforcement |
| AC.L2-3.1.12 | Monitor/control remote access | Unknown / Assume Partially Met | Not addressed in facts — flag for follow-up |
| AC.L2-3.1.20 | Verify/control connections to external systems | Partially Met | Cloud email MFA suggests some external system control, but inconsistent |

**Overall AC rating: NOT MET.** The flat network with CUI stored on shared drives is the single biggest AC finding — it violates the core principle of restricting CUI access to authorized users only and prevents enforcement of least privilege.

---

### 3.2 Identification & Authentication (IA) — **NOT MET**

| Practice ID | Practice | Rating |
|---|---|---|
| IA.L2-3.5.3 | Multifactor authentication for local and network access to privileged accounts and for network access to non-privileged accounts | **Not Met** |
| IA.L2-3.5.1 / 3.5.2 | Identify/authenticate users and devices | Partially Met (assume standard password auth exists) |

**Rationale:** MFA is only enabled on cloud email. IA.L2-3.5.3 requires MFA for **network access** to all accounts (privileged and non-privileged) and **local access to privileged accounts**, not just one SaaS application. This is a **Weight-5 practice** — one of the highest-impact deductions in the entire assessment. This alone represents a major point loss and is a near-universal C3PAO finding when orgs "check the box" with email-only MFA (e.g., relying solely on Microsoft 365/Google Workspace MFA without covering VPN, servers, admin consoles, domain admin accounts, etc.).

---

### 3.3 System & Communications Protection (SC) — **NOT MET**

| Practice ID | Practice | Rating |
|---|---|---|
| SC.L2-3.13.11 | Employ FIPS-validated cryptography to protect confidentiality of CUI | **Not Met** |
| SC.L2-3.13.16 | Protect confidentiality of CUI at rest | **Not Met** |
| SC.L2-3.13.1 | Boundary protection (monitor/control communications at external/internal boundaries) | **Not Met** (flat network = no internal boundary protection) |
| SC.L2-3.13.5 | Subnetworks for publicly accessible components | **Not Met / Not Applicable pending review** |

**Rationale:** No FIPS-validated encryption for CUI at rest is a direct, explicit violation of SC.L2-3.13.11 and SC.L2-3.13.16 — both Weight-5 practices. This is compounded by the flat network architecture, which also fails SC.L2-3.13.1 (no internal network boundaries/segmentation to isolate CUI). This cluster of findings is the most severe in the assessment.

---

### 3.4 Configuration Management (CM) — **PARTIALLY MET (inferred)**

Not directly addressed in the facts provided, but the flat network and shared-drive CUI storage strongly suggest weak configuration baselines and change control (CM.L2-3.4.1, 3.4.2, 3.4.6, 3.4.7). **Flag as a follow-up assessment area** — cannot rate definitively without evidence, but risk-inference suggests Partially Met at best.

---

### 3.5 System & Information Integrity (SI) — **UNKNOWN / Assume Partially Met**

Not directly addressed (SI.L2-3.14.1 malicious code protection, 3.14.6 monitoring). Flag for follow-up; do not assume compliance. Given the absence of network segmentation and encryption controls, it's reasonable to assume monitoring/alerting maturity is also underdeveloped.

---

### 3.6 Incident Response (IR) — **PARTIALLY MET**

| Practice ID | Practice | Rating |
|---|---|---|
| IR.L2-3.6.1 | Establish operational incident-handling capability (preparation, detection, analysis, containment, recovery, user response) | Partially Met — plan exists but capability unproven |
| IR.L2-3.6.2 | Track, document, and report incidents to designated officials | Partially Met — depends on whether the plan defines reporting chains (including DFARS 252.204-7012 72-hour DoD reporting, if applicable) |
| IR.L2-3.6.3 | Test the organizational incident response capability | **Not Met** |

**Rationale:** Having a written IR plan satisfies part of 3.6.1, but an untested plan means the organization cannot demonstrate operational capability. IR.L2-3.6.3 explicitly requires **testing** (tabletop exercise, simulation, or functional test) — this is unambiguously **Not Met**. Assessors will ask for test records/after-action reports; none exist. This is a Weight-3 practice.

---

### 3.7 Awareness & Training (AT) — **MET (likely, pending role-based content review)**

| Practice ID | Practice | Rating |
|---|---|---|
| AT.L2-3.2.1 | Ensure managers/system admins/users are aware of security risks and applicable policies | Met |
| AT.L2-3.2.2 | Ensure personnel are trained to carry out their assigned information-security-related duties | Partially Met — need to confirm role-based training (e.g., for privileged users/admins) exists beyond general annual awareness training |

**Rationale:** Annual security awareness training is a solid foundation and satisfies 3.2.1 for general awareness. However, 3.2.2 requires **role-based** training for personnel with specific security responsibilities (system admins, incident responders, personnel handling CUI). If training is purely general/annual with no role-specific component, rate 3.2.2 as Partially Met pending evidence.

---

### 3.8 Personnel Security (PS) — **MET**

| Practice ID | Practice | Rating |
|---|---|---|
| PS.L2-3.9.1 | Screen individuals prior to authorizing access to systems containing CUI | Met |
| PS.L2-3.9.2 | Ensure CUI/systems are protected during and after personnel actions (transfers, terminations) | Partially Met — background screening covers 3.9.1, but termination/transfer deprovisioning process not confirmed |

**Rationale:** Background screening for all staff satisfies 3.9.1. Confirm formal offboarding/deprovisioning procedures exist to fully close 3.9.2.

---

### 3.9 SSP Currency (Governance / Overarching Requirement)

| Item | Rating |
|---|---|
| System Security Plan (all 14 families require an SSP describing system boundary, environment, and how each practice is implemented) | **Partially Met / At Risk** |

**Rationale:** An SSP from 2022 is **4 years stale** as of July 2026. CMMC assessors expect the SSP to reflect the **current** system boundary, architecture, and control implementation. Given the described environment (flat network, CUI on shared drives, MFA gaps) likely doesn't match what a 2022 SSP describes, the SSP itself is likely **inaccurate**, which is a separate and serious finding — an inaccurate SSP undermines the credibility of the entire assessment package and will be flagged immediately by any C3PAO or DIBCAC reviewer. Recommend full SSP rewrite, not just an update.

---

## 4. Summary Ratings Table

| Practice Family | Overall Rating | Key Driver | Approx. Weight of Findings |
|---|---|---|---|
| Access Control (AC) | Not Met | Flat network, CUI on shared drives, no least privilege | High (multiple W3–W5) |
| Identification & Authentication (IA) | Not Met | MFA limited to cloud email only | High (W5 — 3.5.3) |
| System & Communications Protection (SC) | Not Met | No FIPS-validated encryption at rest; no boundary/segmentation | Highest (multiple W5) |
| Configuration Management (CM) | Partially Met (inferred) | Not directly assessed; flat network suggests weak baselines | Medium — needs follow-up |
| System & Information Integrity (SI) | Unknown | Not directly assessed | Needs follow-up |
| Incident Response (IR) | Partially Met | Plan exists, never tested (3.6.3 Not Met) | Medium (W3) |
| Awareness & Training (AT) | Met / Partially Met | Annual training solid; role-based training unconfirmed | Low |
| Personnel Security (PS) | Met | Background screening in place; offboarding process unconfirmed | Low |
| SSP Governance | Partially Met / At Risk | 2022 SSP stale and likely inaccurate | Cross-cutting |

---

## 5. SPRS Score Impact Estimate

**Illustrative scoring (not a certified calculation — use as directional guidance only):**

| Finding | Practice | Weight | Deduction |
|---|---|---|---|
| MFA not enforced network-wide / for privileged access | IA.L2-3.5.3 | 5 | -5 |
| No FIPS-validated encryption for CUI at rest | SC.L2-3.13.11 | 5 | -5 |
| CUI confidentiality at rest not protected | SC.L2-3.13.16 | 5 | -5 |
| No internal boundary protection (flat network) | SC.L2-3.13.1 | 5 | -5 |
| CUI flow not controlled (shared drives) | AC.L2-3.1.3 | 3 | -3 |
| Least privilege not enforced | AC.L2-3.1.5 | 3 | -3 |
| IR capability untested | IR.L2-3.6.3 | 3 | -3 |
| SSP inaccurate/stale (cross-cutting governance risk — may cascade into additional deductions once the assessor traces boundary/architecture claims) | N/A (overarching) | — | Risk multiplier, not a direct point |
| **Subtotal from named findings alone** | | | **~ -29** |

Because CMMC assessments score **all 110 practices**, and this snapshot only covers ~10-15 of them explicitly, additional undiscovered gaps in CM, SI, Media Protection (MP), Risk Assessment (RA), and Audit & Accountability (AU) are likely once a full assessment is performed — especially given the flat-network/shared-drive finding, which typically correlates with weak logging, weak media protection, and weak configuration management.

**Realistic full-scope estimate: SPRS score in the -35 to -50 range**, well below the certification threshold. A score below 0 or in strongly negative territory also raises DoD contracting risk under DFARS 252.204-7019/7020 (contracting officers can view SPRS scores; negative scores may affect award/renewal decisions even before formal CMMC certification is required).

**POA&M eligibility:** Under current CMMC 2.0 rules, POA&Ms are permitted for a **limited, defined set of lower-weighted practices** and require closure within 180 days; high-weight foundational practices (like MFA and FIPS-validated encryption) are generally **not eligible** for POA&M treatment for certification purposes and should be remediated before assessment, not deferred.

---

## 6. Prioritized Remediation Plan

### Phase 1 — Quick Wins (0–30 days)

1. **Expand MFA beyond cloud email (IA.L2-3.5.3)** — Enforce MFA for VPN/remote access, all privileged/admin accounts (domain admin, server admin, firewall/network device management), and all systems in the CUI boundary. Most cloud IdP/MFA tools (Entra ID, Duo, Okta) can be extended quickly if already licensed. **Highest priority — Weight 5.**
2. **Begin SSP rewrite** — Stand up a current-state SSP project immediately; even a draft-in-progress SSP with an honest gap list is better than a stale, inaccurate 2022 document. Assign an owner and 30–45 day completion target.
3. **Restrict shared drive access as an interim compensating control** — While full segmentation is designed, immediately apply folder-level access controls / ACLs to shared drives containing CUI to enforce least privilege (AC.L2-3.1.5) as a stopgap.
4. **Schedule and conduct a tabletop IR test (IR.L2-3.6.3)** — Low-cost, fast to execute, closes a discrete Weight-3 gap. Document results as evidence.
5. **Confirm/formalize offboarding procedures (PS.L2-3.9.2)** — Document the deprovisioning workflow if not already written down.
6. **Add role-based training modules (AT.L2-3.2.2)** — Supplement annual general training with targeted modules for IT admins, incident responders, and CUI handlers.

### Phase 2 — Core Remediation (30–90 days)

7. **Implement FIPS-validated encryption for CUI at rest (SC.L2-3.13.11 / 3.13.16)** — Deploy FIPS 140-2/140-3 validated encryption (e.g., BitLocker in FIPS mode, validated full-disk encryption, or a FIPS-validated encrypted file share/CUI enclave solution). Inventory all CUI repositories first (this will also inform Phase 2 segmentation work).
8. **Design and begin network segmentation (AC.L2-3.1.3, SC.L2-3.13.1, SC.L2-3.13.5)** — Architect a segmented environment isolating CUI (dedicated VLAN/subnet, firewall/ACL rules, ideally a defined "CUI enclave"). This is often the largest and most expensive remediation item — consider a managed GCC High / CUI enclave / dedicated CMMC boundary approach if a full internal segmentation project is too costly for the organization's size.
9. **Migrate CUI off general shared drives into access-controlled, encrypted, logged repository** — Pair with segmentation work; enforce least privilege and audit logging on the new CUI repository.
10. **Stand up centralized logging/monitoring** for the new CUI boundary to support AU and SI families (not explicitly scoped but will be required for full 110-practice compliance).

### Phase 3 — Finalize & Validate (90–120 days)

11. **Complete SSP** reflecting the new segmented architecture, encryption implementation, and MFA scope — must accurately describe the environment as it will exist at assessment time.
12. **Conduct a full internal NIST SP 800-171 self-assessment against all 110 practices** (not just the areas flagged here) to surface CM, SI, MP, RA, and AU gaps not covered by the facts provided.
13. **Run a mock/readiness assessment** (internally or via a consultant/RPO) before engaging a C3PAO.
14. **Update SPRS score in the DoD SPRS system** to reflect the true current-state score, per DFARS 252.204-7020 self-assessment requirements, once Phase 1–2 items are substantially complete.
15. **Engage a C3PAO for formal Level 2 certification assessment** only after re-scoring internally shows a score at or near 110 (or an approved, DoD-compliant POA&M covers any remaining lower-weight gaps).

---

## 7. Key Risks If Unaddressed

- **Contractual risk:** DFARS 252.204-7012/7019/7020 require accurate SPRS scores; a materially inaccurate or stale SSP combined with unremediated Weight-5 gaps creates False Claims Act exposure if the organization has attested to compliance it doesn't have.
- **Breach risk:** Flat network + unencrypted CUI on shared drives + MFA gaps is a classic lateral-movement/ransomware exposure profile — this is a data breach waiting to happen, independent of the compliance angle.
- **Certification timeline risk:** Waiting until a contract requires certification is too late — segmentation and encryption projects alone typically take 60–120 days for a small-to-mid-size organization.

---

## 8. Recommended Next Steps

1. Validate this desk assessment with a full evidence-based review (configs, policies, network diagrams, access control lists) — ideally performed by or with a CMMC Registered Practitioner (RP) or C3PAO-adjacent advisor.
2. Prioritize Phase 1 items this month; they are low-cost/high-impact.
3. Budget and scope Phase 2 (encryption + segmentation) as a formal project with executive sponsorship — this is where most of the SPRS point recovery will come from.
4. Do not submit or update the SPRS score until at least Phase 1 is complete and Phase 2 is underway with a credible completion date, to avoid submitting a score that misrepresents current risk.

---

*This assessment is based solely on the seven facts provided and general knowledge of the NIST SP 800-171 Rev. 2 / CMMC 2.0 Level 2 framework as of mid-2026. It does not constitute a certified CMMC assessment, legal advice, or a substitute for a full 110-practice evidence-based review. Verify current DoD scoring methodology, POA&M rules, and the 32 CFR Part 170 CMMC rule text at the time of action, as program details may be updated.*
