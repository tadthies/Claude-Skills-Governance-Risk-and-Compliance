# Hosting RESTRICTED Data in AWS Sydney (Offshore) — NZISM Requirements

Short answer: **it may be possible, but not by default, and not without formal approval.** The NZISM treats offshore hosting of Restricted-and-above information as an exception that requires explicit risk acceptance, not a routine architecture choice. AWS Sydney is offshore relative to New Zealand, so it triggers the NZISM's data sovereignty and offshore hosting controls.

## What the NZISM Requires

### 1. Data Sovereignty Is the Default Position
NZISM Data Management controls establish that **government data should be stored and processed in New Zealand unless approved otherwise**. Offshore hosting (including Australia) is a deviation from this default and must be justified and formally approved — it is not something you can decide unilaterally at a project level.

### 2. Cloud-Specific Controls (NZISM Section 17 — Cloud Computing)
Before adopting any cloud service for Restricted+ information, the NZISM requires:
- **A cloud risk assessment** — mandatory before adopting cloud services for Restricted and above information
- **Compliance with the NZ Government Cloud Computing Risk & Resilience Guide** — this is the specific NCSC NZ policy instrument that governs cloud adoption decisions and must be followed alongside the NZISM
- **A data residency assessment** — specifically evaluating the implications of storing/processing Restricted data outside NZ
- **A documented shared responsibility model** agreed with AWS, reviewed at least annually
- **Preference for providers with recognised security certification** (e.g., ISO 27001 or equivalent) — AWS generally holds these, but certification alone does not satisfy the NZISM's offshore approval requirement
- **An exit strategy** — data portability and secure deletion provisions on contract termination

### 3. Offshore Hosting Approval (Restricted-Specific Control)
For Restricted information specifically, the NZISM requires:
- **Accrediting Authority approval** before Restricted+ data can be hosted offshore. This is a formal, documented risk-acceptance decision — not a technical sign-off — made by the senior official responsible for accepting residual risk for the system.
- The agency **remains fully responsible for information security** even though AWS hosts the infrastructure. Using a hyperscale cloud provider does not transfer accountability.

### 4. Certification & Accreditation Implications
Because this is a Restricted system, it must go through the standard NZISM C&A process, and the offshore hosting decision becomes part of that:
- The **System Security Plan (SSP)** must document the AWS Sydney hosting arrangement, the shared responsibility split, and compensating controls.
- The **Security Risk Assessment** must specifically address the risks introduced by offshore hosting (e.g., foreign legal jurisdiction/access requests, data-in-transit exposure, incident response coordination across borders, AWS's own personnel and facility security).
- The Accrediting Authority's ATO decision must explicitly cover acceptance of the offshore hosting risk — this cannot be bundled in as an assumption.

## Practical Checklist Before You Can Proceed

| Requirement | Status Needed |
|---|---|
| Cloud risk assessment specific to AWS Sydney completed | Required |
| Assessment against NZ Government Cloud Computing Risk & Resilience Guide | Required |
| Data residency/offshore risk assessment documented | Required |
| Shared responsibility matrix with AWS documented and agreed | Required |
| Encryption at rest and in transit for Restricted data (TLS 1.2+, encryption at rest) | Required, verify AWS configuration meets NCSC NZ approved cipher suites |
| Accrediting Authority formal approval for offshore hosting | Required — this is the key gating decision |
| SSP updated to reflect AWS Sydney architecture and controls | Required |
| Security Risk Assessment addresses jurisdictional/legal access risk (Australian legal environment, US CLOUD Act exposure via AWS as a US-headquartered company) | Strongly recommended |
| Incident notification clauses with AWS (breach notification timeframes) | Required per third-party supplier controls |
| Exit strategy / data portability and secure deletion terms in the AWS agreement | Required |

## Key Risk Considerations to Flag to Your Accrediting Authority

- **Jurisdictional exposure**: AWS Sydney is subject to Australian law, and AWS as a US company may also be subject to US legal instruments (e.g., CLOUD Act) that could compel data access regardless of physical location. This is a common sticking point in offshore approval decisions and should be addressed head-on in your risk assessment.
- **Incident response coordination**: your Incident Response Plan needs to account for a cross-border incident, including how quickly AWS will notify you and how NCSC NZ notification timeframes will still be met.
- **Aggregation risk**: even if individual data elements seem lower-sensitivity, confirm the aggregate dataset genuinely warrants Restricted (not higher) — this affects whether offshore hosting is viable at all, since Confidential+ typically prohibits offshore processing without Accrediting Authority approval and is subject to much stricter constraints.

## Bottom Line

You cannot proceed with AWS Sydney for Restricted data based on convenience or a standard vendor security review alone. You need: a cloud risk assessment against the NZ Government Cloud Computing Risk & Resilience Guide, a documented data residency/offshore risk assessment, and — critically — **explicit, documented approval from your Accrediting Authority** accepting the offshore hosting risk as part of your C&A process. Until that approval exists, treat this as not authorised.

I can help draft the offshore hosting risk assessment, the SSP section documenting the AWS shared responsibility model, or a briefing paper for your Accrediting Authority if useful.

---
*This is general compliance guidance, not legal advice. Verify current requirements against official NZISM/NCSC NZ guidance and the NZ Government Cloud Computing Risk & Resilience Guide, and consult your Accrediting Authority or qualified counsel for the offshore hosting decision.*
