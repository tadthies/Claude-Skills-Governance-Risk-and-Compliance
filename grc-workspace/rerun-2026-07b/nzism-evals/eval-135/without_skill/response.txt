# NZISM-Aligned Due Diligence and Contractual Requirements for SaaS Procurement

## 1. Pre-Procurement Due Diligence

Before selecting a SaaS vendor, your agency should conduct structured due diligence aligned to NZISM principles for cloud/third-party services:

### a. Data Classification and Risk Assessment
- Determine the classification of data that will be stored/processed in the SaaS product (UNCLASSIFIED, IN-CONFIDENCE, RESTRICTED, etc.).
- Conduct a **cloud risk assessment** proportionate to that classification, consistent with NZISM cloud computing guidance — the higher the classification, the more rigorous the assessment and approval process required.
- Identify whether the SaaS product will process personal information (triggering Privacy Act 2020 obligations) and assess accordingly.

### b. Vendor Security Posture Assessment
- Request evidence of the vendor's security certifications/attestations (e.g., ISO 27001, SOC 2 Type II, or equivalent independent assessments).
- Assess whether the vendor has previously been evaluated under any NZ Government cloud risk assessment or panel/marketplace arrangement.
- Review the vendor's own subprocessor/subcontractor arrangements — SaaS products often rely on underlying cloud infrastructure (e.g., AWS, Azure, GCP) and third-party components, all of which extend your supply chain risk.
- Evaluate the vendor's incident history and security track record where available.

### c. Data Location and Sovereignty
- Confirm where data will be stored, processed, and backed up (including disaster recovery sites) — this may be offshore, which introduces jurisdictional and legal access risk that must be explicitly assessed and accepted by an appropriate authority for anything beyond UNCLASSIFIED/low-sensitivity data.
- Determine whether data residency in New Zealand is available/required for your use case.

### d. Architecture and Technical Review
- Review the vendor's approach to encryption (at rest and in transit), key management (who controls encryption keys), authentication (support for MFA/SSO/federated identity), logging and monitoring capability, and API/integration security.
- Assess multi-tenancy risk — how the vendor logically/physically separates your agency's data from other customers.

## 2. Contractual Security Requirements to Impose

### a. Data Ownership, Access, and Confidentiality
- Explicit clause confirming the agency retains ownership of all data; the vendor acts only as a data processor/holder.
- Restriction on vendor's use of agency data (no secondary use, no use for vendor's own analytics/AI training without explicit agency consent).
- Confidentiality obligations extending to all vendor personnel and subcontractors.

### b. Security Standards and Compliance
- Requirement that the vendor maintains security controls consistent with the classification of data being handled, referencing relevant standards (ISO 27001 or equivalent) and, where practicable, alignment with NZISM control expectations.
- Right for the agency (or an independent auditor on its behalf) to audit or request evidence of the vendor's security controls periodically.
- Requirement to notify the agency of material changes to the vendor's security posture, subprocessors, or hosting arrangements.

### c. Data Location and Sovereignty Clauses
- Explicit contractual commitment on where data will be stored and processed, including backups and disaster recovery, with agency approval required before any change.
- Restriction on offshoring beyond agreed jurisdictions without prior written agency consent.
- Clarity on which jurisdiction's laws could compel the vendor to disclose agency data, and vendor's obligation to notify the agency of any such legal request (subject to law).

### d. Encryption and Key Management
- Requirement for encryption of data at rest and in transit using industry-standard/approved algorithms.
- Where feasible for sensitive data, agency-controlled or agency-visible key management arrangements (e.g., customer-managed keys, bring-your-own-key).

### e. Access Control and Authentication
- Support for multi-factor authentication and, ideally, federation with the agency's identity provider (SSO).
- Role-based access control within the SaaS product.
- Vendor personnel access to agency data restricted on a least-privilege, need-to-know basis, with logging of administrative access.

### f. Incident Notification and Response
- Mandatory, time-bound (e.g., 24–72 hour) notification obligation to the agency in the event of any security incident, suspected breach, or unauthorised access affecting agency data — this should be a hard contractual deadline, not "as soon as reasonably practicable" left vague.
- Vendor obligation to cooperate fully with agency incident response and any regulatory investigation (including NCSC/CERT NZ or Privacy Commissioner involvement where relevant).
- Defined roles/responsibilities for breach communication to affected individuals if personal information is involved.

### g. Business Continuity and Availability
- Defined service levels (uptime, support response times) appropriate to the criticality of the service.
- Vendor obligations around backup, disaster recovery, and business continuity planning, with evidence/testing where the service is critical.

### h. Data Return and Deletion (Exit Provisions)
- Contractual right to retrieve all agency data in a usable format upon contract termination or expiry.
- Guaranteed secure deletion of agency data (including backups) from vendor systems within a defined period after contract end, with certification of deletion provided.
- No vendor lock-in mechanisms that impede data portability.

### i. Subcontractor/Subprocessor Management
- Requirement for vendor to disclose all subprocessors and flow down equivalent security obligations to them.
- Agency right to object to new subprocessors, particularly where they introduce new jurisdictions or risk.

### j. Liability, Insurance, and Audit Rights
- Appropriate liability provisions for data breach costs, including regulatory fines, notification costs, and reputational harm mitigation, proportionate to the sensitivity of the data.
- Requirement for the vendor to hold cyber insurance appropriate to the engagement.
- Ongoing audit/assurance rights — right to request updated certifications, penetration test summaries, or conduct security reviews periodically over the life of the contract.

### k. Compliance with NZ Legal and Policy Obligations
- Vendor commitment to support the agency's compliance with the Privacy Act 2020 (data processing agreement/privacy terms), Public Records Act (if applicable, for records retention/disposal obligations), and any sector-specific legislation.
- Where the data is classified (RESTRICTED or above), explicit vendor commitment to support the agency's NZISM-aligned certification and accreditation obligations, including providing evidence needed for the agency's own SSP/SRMP and risk assessment.

## 3. Governance and Approval Process

- The SaaS procurement and associated risk assessment should be reviewed by your ITSM/CISO before contract signature, particularly if any classified or personal data will be involved.
- For higher-sensitivity use cases, the residual risk of using the SaaS product should be **formally documented and accepted** by an appropriately senior/delegated risk owner — not assumed by procurement or the business unit alone.
- Where available, check whether the vendor is already on an **All-of-Government (AoG)** panel or has undergone a whole-of-government risk assessment, which may streamline due diligence and provide pre-negotiated favourable terms.

## Summary Checklist

- [ ] Data classification and cloud risk assessment completed
- [ ] Vendor security certifications reviewed (ISO 27001/SOC 2 or equivalent)
- [ ] Data location/sovereignty confirmed and contractually locked down
- [ ] Encryption and key management requirements defined
- [ ] MFA/SSO and access control support confirmed
- [ ] Incident notification clause with firm timeframe included
- [ ] Business continuity/DR obligations defined
- [ ] Data return and secure deletion (exit) clause included
- [ ] Subprocessor disclosure and flow-down obligations included
- [ ] Liability, insurance, and audit rights negotiated
- [ ] Privacy Act / NZISM compliance support obligations included
- [ ] ITSM/CISO and risk owner sign-off obtained before go-live

*Note: This guidance reflects general NZISM-aligned due diligence principles as commonly understood. For binding requirements, confirm current NZISM cloud computing guidance, any applicable All-of-Government cloud/SaaS panel terms, and your agency's specific procurement and risk governance policies, as these may have been updated.*
