# NZISM Certification & Accreditation (C&A) Gap Analysis — RESTRICTED System

## 1. What the NZISM C&A Process Requires

Under the New Zealand Information Security Manual (NZISM), Certification and Accreditation is the formal process by which a system's security posture is validated (certification) and a risk-acceptance decision is made by an appropriately senior authority (accreditation) before the system is permitted to operate — particularly for systems processing classified information such as RESTRICTED.

The NZISM C&A lifecycle generally comprises the following stages:

1. **System Security Plan (SSP)** — Documents the system architecture, boundary, data flows, and the security controls selected (from the NZISM control catalogue) to protect the system commensurate with its classification (RESTRICTED in this case). The SSP should map controls to the relevant NZISM chapters (e.g., Information Security Governance, Access Control, Cryptography, Network Security, System Hardening, Physical Security, Incident Management).

2. **Security Risk Management Plan (SRMP)** — Documents the risk assessment process: identified threats and vulnerabilities, likelihood/consequence ratings, residual risk, and risk treatment decisions. The SRMP underpins the SSP by providing the risk rationale for control selection, and both should be read together. The SRMP should reference the agency's risk appetite and the NZ Government's risk assessment methodology (aligned to AS/NZS ISO 31000 principles as applied in the GCDO/NZISM context).

3. **Control Implementation and Validation** — Controls identified in the SSP must actually be implemented and then independently validated/tested. This typically includes:
   - Technical testing (e.g., vulnerability scanning, configuration review, penetration testing where warranted for RESTRICTED systems)
   - Compliance/conformance checking against NZISM "must"/"should" controls
   - Evidence collection to demonstrate operating effectiveness, not just design

4. **Certification** — An independent (or sufficiently separated) technical assessment confirming that the system, as built and operated, meets the security requirements documented in the SSP/SRMP. This is a technical statement of assurance, not a risk-acceptance decision.

5. **Accreditation** — A formal, documented decision by the agency's Accreditation Authority (typically the Chief Executive or a delegate such as the CISO/ITSM, depending on agency governance) to accept the residual risk and authorise the system to operate, usually for a defined period (subject to periodic reaccreditation, typically no more than every 3 years, or sooner if there is significant change).

6. **IT Security Manager (ITSM) Role** — The ITSM (or equivalent, e.g., CISO) is responsible for overseeing the agency's security posture, coordinating the C&A process, ensuring the SSP and SRMP are current, and providing a recommendation to the Accreditation Authority. Sign-off/endorsement from the ITSM is a standard prerequisite before submission for formal accreditation.

7. **Ongoing Assurance** — Post-accreditation, the system requires continuous monitoring, periodic vulnerability assessments, incident reporting, and change management to maintain its accredited status. Significant changes to the system typically trigger a review of the accreditation.

## 2. Gap Analysis Against Your Current State

| Requirement | Current State | Gap | Risk if Unaddressed |
|---|---|---|---|
| System Security Plan | Draft exists | Not finalised/approved; likely not yet validated against actual implementation | Cannot proceed to certification without a finalised, approved SSP |
| Security Risk Management Plan | Does not exist | **Critical gap** — no formal risk assessment underpinning the SSP's control selections | Control selection cannot be justified or risk-accepted; accreditation cannot proceed without this |
| Control Implementation | Partial | Controls not fully implemented | System does not yet meet minimum RESTRICTED baseline; residual risk unknown |
| Control Validation/Testing | None performed | **Critical gap** — no evidence controls operate as intended | Certification cannot be granted without independent validation; unverified controls cannot be relied upon |
| ITSM Sign-off | Not obtained | No endorsement from IT Security Manager | Accreditation Authority typically will not (and should not) accept a system without ITSM recommendation |
| Certification | Not started | Cannot certify until SSP, SRMP, and validated controls are in place | No independent assurance statement exists |
| Accreditation | Not started | Formal risk-acceptance decision cannot be made | **System is not authorised to process RESTRICTED information** |

## 3. Priority Remediation Path

1. **Develop the SRMP immediately** — this is your most significant gap and a blocking dependency for everything downstream. Conduct a formal risk assessment covering threats, vulnerabilities, likelihood, consequence, and residual risk, referencing NZISM baseline controls for RESTRICTED systems.
2. **Finalise the SSP**, ensuring it reflects the risk treatment decisions from the SRMP and maps explicitly to NZISM control references.
3. **Complete implementation** of all controls identified as mandatory ("must") for a RESTRICTED system, prioritising access control, cryptography (NZ-approved algorithms/products), network segmentation, logging/audit, and physical/personnel security controls.
4. **Commission independent validation testing** — vulnerability assessment and, given the RESTRICTED classification, likely a penetration test or independent technical review — to produce certification evidence.
5. **Obtain ITSM review and sign-off**, incorporating findings from testing and confirming the SSP/SRMP are fit for submission.
6. **Submit for formal certification**, then present to the Accreditation Authority for a documented accreditation decision (with any residual risks explicitly accepted, not implied).
7. **Do not process RESTRICTED information operationally** until accreditation is granted; if the system is already live, this should be flagged as an urgent compliance and risk issue to your agency's senior leadership/CISO, since operating an unaccredited system processing RESTRICTED data is a material control failure.

## 4. Summary

You currently have only one of the required foundational artefacts (a draft SSP) and none of the subsequent validation or governance steps. The most urgent and structurally blocking gap is the absence of a Security Risk Management Plan, since it should logically precede and justify the SSP's control set. Until the SRMP is created, controls are fully implemented and tested, and ITSM sign-off is obtained, the system cannot be certified, and therefore cannot be accredited to operate at RESTRICTED. Treat this as a program of work with the SRMP as the immediate next deliverable, followed by control closure, testing, and a phased path to certification and accreditation.

*Note: This response is based on general knowledge of the NZISM C&A framework as commonly understood. For definitive requirements, consult the current published NZISM (via the NZ GCSB/NCSC) and your agency's specific accreditation authority guidance, as processes and delegation arrangements can vary by agency and may be updated over time.*
