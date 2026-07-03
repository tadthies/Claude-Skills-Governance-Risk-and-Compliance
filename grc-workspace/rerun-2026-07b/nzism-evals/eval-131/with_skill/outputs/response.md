# NZISM Certification & Accreditation (C&A) Gap Analysis — RESTRICTED System

Below is a gap analysis against the NZISM C&A pathway, based on the current state you've described: a draft System Security Plan (SSP), no Security Risk Management Plan, partially implemented controls with no validation testing, and no ITSM (Information Technology Security Manager)/Accrediting Authority sign-off.

## What NZISM Requires for C&A

For any system handling **Restricted** and above, the NZISM mandates formal Certification and Accreditation before go-live. The pathway has five core stages:

1. **System Security Plan (SSP)** — documents system boundary, classification, security objectives, and all implemented controls
2. **Security Risk Assessment / Security Risk Management Plan (SRMP)** — identifies threats, vulnerabilities, likelihood, impact, and residual risk; drives risk treatment decisions
3. **Security Assessment (Certification)** — independent technical review/testing that validates controls actually work as documented
4. **Plan of Action & Milestones (POA&M)** — tracks remediation of any findings from the security assessment
5. **Accreditation Decision (ATO)** — the Accrediting Authority formally reviews residual risk and grants Authorisation to Operate
6. **Ongoing monitoring** — continuous control monitoring and periodic re-certification (typically every 1–3 years, or triggered by major change/incident/classification change)

## Gap Analysis

| C&A Element | NZISM Requirement | Current Status | Gap Notes |
|---|---|---|---|
| System Security Plan | Complete SSP documenting boundary, classification, objectives, and all controls | 🟡 Partial (draft only) | Draft SSP needs to be finalised — confirm system boundary is fully scoped, classification rationale is documented, and every implemented/planned control is mapped to an NZISM control ID |
| Security Risk Assessment / SRMP | Formal risk assessment identifying threats, vulnerabilities, likelihood, impact, residual risk | ❌ Not Implemented | This is a critical gap — the SRMP is a mandatory C&A artefact and a prerequisite for a meaningful Security Assessment. Without it, residual risk cannot be quantified or accepted by the Accrediting Authority |
| Control Implementation | Controls implemented per classification-appropriate baseline (Restricted-level controls, inheriting Unclassified/In-Confidence baseline) | 🟡 Partial | "Partially implemented" is not sufficient for certification. Each control needs a documented status (Implemented/Partial/Not Implemented) with evidence — an inventory of what's done vs outstanding is needed before assessment can proceed |
| Control Validation Testing | Independent technical review/testing confirming controls operate as documented | ❌ Not Implemented | No validation testing means there is no assurance evidence. This blocks the Security Assessment stage entirely — an assessor cannot certify controls that haven't been tested |
| Security Assessment (Certification) | Independent assessment against NZISM controls | ❌ Not started (blocked) | Cannot begin until SSP is finalised, SRMP exists, and controls have testable evidence |
| POA&M | Documented remediation plan for any assessment findings | ❌ Not Implemented | Cannot be created until a Security Assessment has been performed and findings identified |
| Accreditation / ATO | Accrediting Authority (ITSM/CISO or equivalent senior official) reviews residual risk and signs off | ❌ No sign-off obtained | No ATO can be issued until all preceding stages are complete. Operating without accreditation for a Restricted system is a compliance breach if the system goes live |
| Ongoing Monitoring | Continuous control monitoring; periodic re-certification cadence agreed | ❌ Not yet established | Should be scoped now so it's ready to activate once ATO is granted |

## Summary of Critical Gaps

Your most urgent and blocking gaps, in priority order:

1. **No Security Risk Management Plan (SRMP)** — this is foundational. Without it you cannot determine which controls are actually required, prioritise remediation, or give the Accrediting Authority anything meaningful to assess residual risk against.
2. **No control validation testing** — "partially implemented, unvalidated" controls cannot be certified. An independent technical assessment needs testable evidence (configuration reviews, vulnerability scans, penetration test results, log samples, access reviews, etc.).
3. **Incomplete SSP** — the draft needs to be finalised with a clearly defined system boundary and a control-by-control mapping before it can support certification.
4. **No ITSM/Accrediting Authority engagement** — sign-off has not even begun, meaning no ATO exists. If this system is intended to go live or is already live, that is a significant compliance exposure for a Restricted-classification system.

## Recommended Remediation Roadmap

| Phase | Activity | Suggested Duration |
|---|---|---|
| 1. Prepare | Finalise SSP; complete Security Risk Management Plan/risk register; complete control implementation and produce an evidence inventory | 4–8 weeks |
| 2. Certify | Commission independent Security Assessment (technical control validation/testing) | 2–4 weeks |
| 3. Remediate | Address findings via POA&M | 2–6 weeks |
| 4. Accredit | Submit SSP, SRMP, assessment report, and POA&M to the Accrediting Authority for ATO decision | 1–2 weeks |
| 5. Monitor | Establish continuous monitoring and set re-certification cadence (1–3 years, risk-dependent) | Ongoing |

**Immediate next steps I'd recommend:**
- Do not allow the system to go live (or continue operating, if already live) on Restricted data until an ATO is granted — this is a compliance and risk exposure.
- Start the SRMP in parallel with finalising the SSP; they inform each other.
- Engage your ITSM/Accrediting Authority now, even before all artefacts are complete, so they understand the timeline and can flag any early concerns (e.g., architecture, data residency).
- Consider engaging an independent assessor early to scope what validation testing will be required, so control implementation work is designed to produce the right evidence the first time.

I can help produce a full SSP outline, a Security Risk Management Plan template, or a control-by-control evidence checklist for the Restricted baseline if that would help move this forward.

---
*This is general compliance guidance, not legal advice. Verify current requirements against official NZISM/NCSC NZ guidance and consult your Accrediting Authority or an accredited assessor for certification decisions.*
