# CMMC Level 2: What It Means for Your Company

Congratulations on the new DoD contract. This is a common moment for small and mid-sized defense contractors — you win the work, and then you find a clause buried in the contract (DFARS 252.204-7021) that points you toward an entirely new compliance regime. Here's a plain-English breakdown of what you're dealing with.

---

## 1. What Is CMMC, in Plain English?

**CMMC (Cybersecurity Maturity Model Certification)** is the Department of Defense's program for verifying that contractors and subcontractors are actually protecting sensitive government information on their networks — not just claiming to.

Before CMMC, companies could self-attest that they met DoD's cybersecurity requirements. DoD found that many companies said they were compliant but weren't. CMMC closes that gap by requiring companies to prove it, either through a rigorous self-assessment or through an independent third-party audit, depending on the sensitivity of the information they handle.

CMMC has three levels:

- **Level 1 (Foundational)** — for companies that only handle Federal Contract Information (FCI). Basic cyber hygiene, 15 practices, annual self-assessment.
- **Level 2 (Advanced)** — for companies that handle **Controlled Unclassified Information (CUI)**. This is where you are. It requires implementing **110 security controls** from **NIST SP 800-171**, and most companies will need a **third-party assessment**.
- **Level 3 (Expert)** — for a small subset of companies supporting DoD's highest-priority programs, involving the most sensitive CUI. Adds controls from NIST SP 800-172 and requires government-led assessment. You almost certainly are not in this tier.

Because your contract cites DFARS 252.204-7021 and requires CMMC Level 2, this tells us your company will be creating, receiving, storing, or transmitting **CUI** as part of this contract — engineering data, technical drawings, specifications, or similar controlled information related to the DoD program.

---

## 2. What Is CUI, and Why Does It Matter?

**Controlled Unclassified Information (CUI)** is government-created or government-owned information that isn't classified, but still needs protection because of laws, regulations, or government-wide policies. For an aerospace engineering firm, common examples include:

- Technical drawings, specifications, and engineering data marked as **export-controlled** or **CUI//SP-EXPT** (ITAR/EAR-related technical data)
- Unclassified DoD program specifications or performance requirements
- Certain manufacturing process data tied to a DoD weapons system or platform
- Test data, technical reports, or engineering analyses delivered to or received from the government

CUI will typically be **marked** in the contract or in documents your contracting officer sends you (look for "CUI," "Controlled Unclassified Information," "Distribution Statement," or legacy markings like "FOUO"). Your DD Form 254 (if this is a classified-adjacent contract) or your contract's Statement of Work should indicate what CUI you'll be handling. If you're not sure, **ask your contracting officer or prime contractor directly** — this determines your entire compliance scope.

The key distinction:
- **FCI (Federal Contract Information)** — information provided by or for the government under contract, not intended for public release. Lower sensitivity. Triggers CMMC Level 1.
- **CUI** — a specific, higher-sensitivity subset that requires safeguarding under NIST SP 800-171. Triggers CMMC Level 2.

---

## 3. What Does CMMC Level 2 Actually Require?

### The 110 Controls

CMMC Level 2 is built entirely on **NIST SP 800-171 Revision 2** (DoD is transitioning some references toward Rev 3, but Rev 2 is the current baseline for most active contracts — confirm which revision your contract cites). This standard has **110 security requirements** organized into **14 families**:

1. Access Control (AC)
2. Awareness and Training (AT)
3. Audit and Accountability (AU)
4. Configuration Management (CM)
5. Identification and Authentication (IA)
6. Incident Response (IR)
7. Maintenance (MA)
8. Media Protection (MP)
9. Personnel Security (PS)
10. Physical Protection (PE)
11. Risk Assessment (RA)
12. Security Assessment (CA)
13. System and Communications Protection (SC)
14. System and Information Integrity (SI)

These controls cover things like: multi-factor authentication, encryption of CUI at rest and in transit, access control based on least privilege, audit logging, incident response planning, security awareness training, vulnerability management, and physical security of facilities where CUI is processed.

### Self-Assessment vs. Third-Party Assessment (C3PAO)

This is the part most companies misunderstand:

- **CMMC Level 2 (Self-Assessment)** applies to a limited subset of programs where DoD determines the risk is lower. You self-attest via annual affirmation in the DoD's Supplier Performance Risk System (SPRS), signed by a senior company official.
- **CMMC Level 2 (C3PAO Assessment)** — the **majority of Level 2 requirements** — requires a **certified third-party assessment organization (C3PAO)** to conduct a formal audit of your environment every **three years**, with **annual self-affirmations** in between.

Your contract will specify which applies. Given that you're a first-time DoD contractor with a specific CUI-handling requirement, **assume you will need the C3PAO (third-party) assessment** unless your contracting officer explicitly tells you otherwise. Most Level 2 requirements in real contracts land in the C3PAO bucket, not the self-assessment bucket.

### Scoring Threshold

To pass a C3PAO assessment, you generally need a score of **at least 88 out of 110** on the day of assessment, with all remaining deficiencies covered by an approved **Plan of Action & Milestones (POA&M)** for a limited set of allowable controls (POA&Ms cannot be used for certain high-priority controls, and all POA&M items must typically be closed within 180 days).

---

## 4. Practical Next Steps

Here's a realistic, sequenced roadmap:

### Step 1: Scoping (2–4 weeks)
Determine exactly which systems, networks, and facilities touch CUI. This is the single most important step because it determines your cost and effort. Many companies overscope by assuming the whole company network needs to be in-boundary, then discover they can dramatically shrink the footprint by isolating CUI into a segmented enclave (a separate network segment, dedicated engineering workstations, or a cloud-based GCC High / govcloud environment). For a 45-person engineering firm, a well-scoped **enclave approach** is usually far cheaper than trying to bring your entire IT environment into compliance.

### Step 2: Gap Assessment (4–8 weeks)
Compare your current environment against all 110 NIST SP 800-171 controls. This is typically done with help from a **Registered Practitioner Organization (RPO)** or CMMC-experienced consultant (look for individuals holding the **RP** or **CCP/CCA** credentials through the Cyber AB, the official CMMC accreditation body). Output is a detailed list of what's in place, what's partially in place, and what's missing.

### Step 3: System Security Plan (SSP) (concurrent with gap assessment)
Document how each of the 110 controls is (or will be) implemented in your environment. The SSP is a required artifact for both self-assessments and C3PAO assessments — it's the map assessors use to evaluate you.

### Step 4: Plan of Action & Milestones (POA&M)
For every gap identified, document what will be done, who owns it, and by when. This becomes your remediation roadmap.

### Step 5: Remediation (3–9 months, the biggest variable)
This is where most of your time and budget goes. Common remediation work for a company at your stage includes:
- Deploying multi-factor authentication everywhere
- Implementing centralized logging and log review
- Encrypting CUI at rest and in transit (FIPS-validated cryptography)
- Formal access control and account management procedures
- Security awareness and role-based training program
- Incident response plan and testing
- Physical security controls for any facility/area processing CUI
- Vendor/subcontractor flow-down of requirements if you share CUI with subcontractors
- Possibly migrating email/file storage to a GCC High or equivalent CUI-capable cloud environment if you currently use commercial Microsoft 365/Google Workspace

### Step 6: SPRS Score Submission
Before or alongside remediation, submit your current NIST SP 800-171 score to the **Supplier Performance Risk System (SPRS)** — this is already required today under existing DFARS clauses, separate from CMMC certification itself, and DoD contracting officers can check it.

### Step 7: Formal C3PAO Assessment (Level 2)
Once you're ready (target: score of 88+ with acceptable POA&M items), schedule your assessment with a certified C3PAO. Booking lead time can be **2–4 months** due to limited assessor availability — book early.

### Step 8: Certification, Then Continuous Compliance
Certification is valid for **3 years**, with **annual affirmations** required in between. You'll also need to maintain your POA&M closures, re-assess after major system changes, and keep training/logging/monitoring running continuously — CMMC is not a one-time project.

---

## 5. Realistic Timeline

For a 45-person firm starting from essentially zero CMMC maturity:

| Phase | Duration |
|---|---|
| Scoping & initial gap assessment | 1–2 months |
| SSP drafting + POA&M development | 1–2 months (overlaps with above) |
| Remediation (tooling, policies, training, MFA, encryption, logging, possible cloud migration) | 4–9 months |
| C3PAO scheduling + formal assessment | 2–4 months (mostly waiting for assessor availability) |
| **Total, realistic estimate** | **9–15 months** |

Companies that are already reasonably mature on IT security (using modern cloud tools, MFA already in place, some documented policies) can compress this toward the lower end. Companies starting from consumer-grade IT with no formal security program should plan for **12–18 months** and budget accordingly.

**Cost expectation:** For a company your size, all-in costs (consulting/RPO support, tooling and technology upgrades, possible cloud environment migration, C3PAO assessment fees, and internal staff time) commonly range from **$100,000–$300,000+** depending on your starting point and whether you need to migrate to a govcloud email/collaboration environment. This varies widely — get quotes early so you can budget realistically.

---

## 6. Immediate Action Items This Week

1. **Confirm with your contracting officer or prime** exactly what CUI you'll handle and whether your Level 2 requirement is self-assessment or C3PAO-assessed.
2. **Check your DFARS 252.204-7012 obligations** — this related, currently-active clause already requires NIST SP 800-171 compliance and CUI incident reporting to DoD within 72 hours, independent of CMMC certification timing. You may already be contractually on the hook for these obligations even before your CMMC assessment happens.
3. **Engage an RPO/consultant** experienced in CMMC for aerospace/manufacturing environments to run your gap assessment — don't try to self-navigate all 110 controls from scratch with a 45-person team that has no dedicated security staff.
4. **Ask about your CMMC assessment deadline** in the contract — DoD is phasing CMMC requirements into contracts, and your specific solicitation/contract will state when certification must be complete (sometimes at contract award, sometimes at a specified future date, sometimes at option period exercise).
5. **Start the SPRS self-assessment score submission now** if you haven't — this is a near-term, lower-cost action that demonstrates good faith and may already be required.

---

## Bottom Line

CMMC Level 2 means the DoD wants documented, verified proof that any government engineering/technical data you handle is protected to a defined standard (110 NIST SP 800-171 controls), validated either by your own signed attestation or, more likely for you, by an independent certified assessor (C3PAO) every three years. For a 45-person firm starting fresh, budget **9–15 months** and plan for meaningful investment in IT security tooling, policy documentation, and possibly a dedicated CUI enclave or govcloud environment. The sooner you scope your CUI boundary and start your gap assessment, the more control you'll have over cost and timeline — this is very achievable, but it is a real program, not a checkbox.
