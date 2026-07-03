# CMMC Level 2 — Plain-English Guide for a First-Time DoD Contractor

Congratulations on the contract award. Here's what DFARS 252.204-7021 and CMMC Level 2 actually mean for a 45-person aerospace engineering firm.

## 1. What CMMC Level 2 Is

CMMC (Cybersecurity Maturity Model Certification) 2.0 is the Department of Defense's cybersecurity compliance framework for the Defense Industrial Base (DIB), codified in **32 CFR Part 170**. It has three levels; you've been told you need **Level 2 — Advanced**, which means:

- You are handling (or will handle) **Controlled Unclassified Information (CUI)** — government-sensitive but unclassified data such as technical drawings, export-controlled engineering data, or specifications.
- You must implement **all 110 security practices** from **NIST SP 800-171 Rev 2**, spanning 14 domains (access control, incident response, encryption, audit logging, personnel security, etc.).
- Depending on whether your program is "critical" (e.g., nuclear, certain weapons systems, highest-priority DoD programs) or not, you'll either:
  - Undergo a **third-party assessment by a C3PAO** (CMMC Third-Party Assessment Organization), or
  - Complete a **rigorous self-assessment** against all 110 practices.

The fact that DFARS 252.204-7021 is explicitly in your contract means the required level and assessment type are specified in the contract itself — check **Section L** or the **Performance Work Statement** to confirm whether you need C3PAO certification or self-assessment. Don't assume; verify against your actual contract text.

## 2. Why This Applies to You

As an aerospace engineering firm, you likely generate or receive **Controlled Technical Information (CTI)** — export-controlled (ITAR/EAR) technical data, drawings, or specifications — which is one of the most common CUI categories in aerospace/defense contracts. That's almost certainly why CUI-level protection (Level 2) is required rather than the lighter Level 1 (which only covers Federal Contract Information).

## 3. What You Need to Do — Step by Step

| Step | Action |
|------|--------|
| 1 | **Confirm your assessment path.** Check the contract for whether Level 2 self-assessment or C3PAO certification is required. |
| 2 | **Scope your environment.** Identify every system, network, and person that touches CUI. Classify assets as CUI Assets, Security Protection Assets, Contractor Risk Managed Assets, Specialized Assets, or Out-of-Scope. Consider building a segmented "CUI enclave" to shrink your assessment boundary — this is often the single biggest cost-saver for a 45-person firm. |
| 3 | **Perform a gap assessment** against all 110 NIST SP 800-171 practices to see where you stand today (expect this to be extensive if you're starting from zero). |
| 4 | **Write a System Security Plan (SSP)** documenting your system boundary, CUI data flows, and how each of the 110 practices is implemented (or why it's not applicable). |
| 5 | **Remediate gaps.** Common early priorities: multifactor authentication (MFA) everywhere CUI is accessed, FIPS-validated encryption for CUI at rest and in transit, centralized audit logging, an incident response plan, and CUI-aware access controls. |
| 6 | **Build a POA&M** (Plan of Action & Milestones) for any practices not yet met — note that a handful of "critical" practices (like MFA and encryption) can *never* be left open at certification time. |
| 7 | **Calculate and submit your SPRS score** at sprs.csd.disa.mil (required regardless of assessment path). |
| 8 | **Complete the assessment** — C3PAO engagement (if required) or formal self-assessment — and have a senior company official affirm the results. |
| 9 | **Maintain continuously.** Annual affirmation is required every year, and Level 2 C3PAO certification is valid for 3 years before reassessment.

## 4. Realistic Timeline

For a 45-person firm starting from essentially zero CMMC maturity, budget **9–18 months** end-to-end:

- **Gap assessment & scoping**: 4–8 weeks
- **Remediation** (MFA rollout, encryption, logging, policy/SSP writing, training): **6–12 months** — this is usually the long pole, especially if you need to procure and deploy new tools (SIEM, PAM, encryption) or restructure your network into a CUI enclave
- **C3PAO engagement (if required)**: select an authorized C3PAO via cyberAB.us, then 4–8 weeks for documentation review plus 1–3 weeks of assessment activity
- **POA&M closeout (if conditional certification is granted)**: up to 180 days post-certification for any open non-critical items

If your program is non-critical and self-assessment is permitted, you can move faster (potentially 6–9 months) since there's no C3PAO scheduling dependency — but the underlying technical work is the same.

## 5. Immediate Next Steps This Week

1. Pull the actual contract and confirm the required assessment path in Section L/PWS.
2. Identify what CUI you'll actually be handling (drawings, technical data, etc.) and who touches it.
3. Start a gap assessment against the 110 NIST SP 800-171 practices — MFA and encryption gaps are the most common findings and the most heavily weighted in scoring, so address those first.
4. Assign an internal owner (ISSO/ISSM role) to drive this — even part-time, someone needs to own it.

## Key Terms You'll Hear

- **CUI**: Controlled Unclassified Information — the data type driving the requirement
- **SSP**: System Security Plan — your master compliance document
- **POA&M**: Plan of Action & Milestones — remediation roadmap for gaps
- **SPRS**: Supplier Performance Risk System — where your score gets submitted
- **C3PAO**: the accredited firm that performs your third-party assessment, if required

---
*This is general compliance guidance, not legal advice. Confirm your specific level and assessment path against the actual contract language, and consider engaging a Registered Practitioner or CMMC consultant for hands-on implementation support.*
