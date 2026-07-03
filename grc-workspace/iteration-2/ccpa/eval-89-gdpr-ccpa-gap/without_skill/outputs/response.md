# GDPR to CCPA/CPRA Gap Analysis: What You Still Need to Do

## Executive Summary

A mature GDPR compliance programme provides a strong foundation for CCPA/CPRA compliance, but the two regimes differ enough in philosophy, scope, and mechanics that meaningful additional work is required. GDPR is an opt-in, rights-based regime built on lawful bases and data minimisation. CCPA/CPRA is primarily an opt-out, transparency-and-control regime with a distinct commercial focus on data selling and sharing. The gaps are real and in some cases require entirely new processes, contracts, and technical controls.

---

## 1. What GDPR Compliance Gives You for Free

The following GDPR programme elements map reasonably well to CCPA/CPRA requirements and can be leveraged with limited additional effort:

**Data Inventory and Mapping**
Your GDPR Record of Processing Activities (RoPA) is the natural starting point for CCPA's required disclosures about categories of personal information collected, purposes of collection, and third parties with whom data is shared. You will need to extend it to capture the CCPA-specific categories (e.g., "sensitive personal information" as defined by CPRA) and to tag data flows by whether they constitute a "sale" or "sharing" under CCPA's broad definitions, but the inventory discipline carries over.

**Privacy Notice Infrastructure**
Your GDPR-compliant privacy policy will already cover many CCPA notice requirements: categories of data collected, purposes, and retention periods. The drafting and maintenance process transfers.

**Data Subject Rights Workflows**
GDPR's Article 15-22 rights workflows (access, deletion, portability, correction) align with CCPA consumer rights. If you have a functioning request intake, identity verification, and fulfilment process, the mechanics apply—though the timelines, scope, and specific rights differ (see Section 3 below).

**Vendor Management Discipline**
Your practice of reviewing third-party data processors and executing Data Processing Agreements (DPAs) maps to CCPA's service provider and contractor contract requirements. The habit of due diligence and contractual controls transfers, even though the contract language must change.

**Security Programme**
CCPA's private right of action is specifically tied to data breaches resulting from failure to implement reasonable security. Your existing security controls and incident response programme directly reduce this liability.

**Data Retention Policies**
CPRA added an explicit data minimisation and retention limitation principle (mirroring GDPR), so your existing retention schedules provide a useful head start.

---

## 2. CCPA/CPRA-Specific Requirements Not in GDPR

These are the areas where GDPR compliance provides little or no credit and new work is required:

### "Do Not Sell or Share My Personal Information" (DNSMI)

CCPA's defining requirement is the consumer's right to opt out of the "sale" or "sharing" of their personal information. "Sale" includes any exchange of personal information for monetary or other valuable consideration—a definition broad enough to capture many advertising technology arrangements (data broker feeds, behavioural advertising platforms, audience data partnerships) that GDPR programmes do not necessarily surface as a distinct compliance category.

CPRA (effective January 1, 2023) added "sharing" as a separate concept covering disclosure of personal information to third parties for cross-context behavioural advertising, even where no money changes hands.

Required actions:
- Audit all data flows to determine which constitute sales or sharing under the statute
- Implement a "Do Not Sell or Share My Personal Information" link on your homepage (or a Global Privacy Control (GPC) signal recognition mechanism, which CPRA mandates must be honoured)
- Build the opt-out intake, propagation, and downstream notification process
- Implement a 12-month re-solicitation restriction (you cannot ask opted-out consumers to opt back in for 12 months)

### Sensitive Personal Information (SPI) Controls (CPRA Addition)

CPRA created a new "sensitive personal information" category (SPI) with elevated rights, including the right to limit use and disclosure to what is necessary to perform the requested service. SPI includes:
- Social Security numbers and government IDs
- Financial account credentials
- Precise geolocation
- Race, ethnicity, religion
- Union membership
- Personal communications content (mail, email, text)
- Genetic and biometric data
- Health and sex life/sexual orientation data

Required actions:
- Identify all SPI processed
- Implement a separate "Limit the Use of My Sensitive Personal Information" link or mechanism
- Restrict SPI processing to specified permitted purposes unless the consumer affirmatively authorises broader use

Note: GDPR treats many of these as "special category" data requiring explicit consent—but the CPRA SPI framework operates differently. CPRA does not prohibit SPI processing outright; it creates a right to limit it. The control mechanism and the underlying logic differ from GDPR Article 9.

### Financial Incentives and Non-Discrimination

CCPA prohibits discriminating against consumers who exercise their privacy rights (e.g., denying service, charging different prices). However, it expressly permits financial incentives—loyalty programmes, price differences, service variations—in exchange for consumer data, provided the incentive is reasonably related to the value of the data and the business provides a good-faith estimate of that value.

GDPR has no equivalent. The CCPA financial incentive notice and valuation requirement is entirely new and requires actuarial or economic analysis to support the "reasonably related to value" standard.

### Opt-Out Preference Signals (Global Privacy Control)

CPRA requires businesses to treat a GPC browser signal (or equivalent) as a valid opt-out of sale and sharing. This is a technical requirement to detect and honour browser-level signals, with no GDPR equivalent.

### California-Specific Notice at Collection

CCPA requires a "notice at collection"—a just-in-time, abbreviated notice at the point of data collection—that identifies the categories of personal information being collected and links to the full privacy policy. While GDPR's transparency requirements achieve a similar outcome, the specific trigger (at collection), format (abbreviated), and required elements differ enough to warrant a dedicated implementation review.

### Contractor vs. Processor—Different Contract Terms

See Section 7 below.

---

## 3. Consumer Rights: Where CCPA/CPRA Differs from GDPR

| Right | GDPR | CCPA/CPRA |
|---|---|---|
| Access | Categories + copy of data | Categories collected, sources, purposes, third parties, and specific pieces (upon verified request) |
| Deletion | Right to erasure (Article 17) with exceptions | Right to delete with different exceptions; business must instruct service providers and contractors to delete |
| Correction | Right to rectification (Article 16) | CPRA added explicit correction right (not in original CCPA) |
| Portability | Structured, machine-readable format | Specific pieces of personal information in portable format |
| Opt-out of automated decisions | Article 22—right not to be subject to solely automated decisions | CPRA added right to opt out of automated decision-making; implementing regulations still developing |
| Opt-out of sale/sharing | No equivalent | Core CCPA right—see above |
| Limit SPI use | No direct equivalent | CPRA right to limit SPI use to necessary purposes |

Key procedural differences:
- Response timeline: CCPA allows 45 days (extendable by another 45 with notice) vs. GDPR's 30 days (extendable by 60 for complex requests)
- Identity verification: CCPA requires "reasonably verifying" identity but sets a higher bar for sensitive requests (access to specific pieces requires higher assurance); GDPR is less prescriptive
- Authorised agents: CCPA explicitly addresses requests made by authorised agents acting on behalf of consumers; your GDPR process may not accommodate this

---

## 4. Opt-Out vs. Opt-In: The Fundamental Philosophical Difference

This is the most architecturally significant difference between the two regimes.

**GDPR: Opt-In by Default**
GDPR requires a lawful basis before any processing occurs. Consent (where relied upon) must be freely given, specific, informed, and unambiguous—meaning it must be an affirmative act before processing begins. This makes GDPR fundamentally opt-in for consent-based processing.

**CCPA/CPRA: Opt-Out by Default**
CCPA permits businesses to sell or share personal information by default and gives consumers the right to opt out. There is no requirement to obtain affirmative consent before selling data (with the exception of minors—see below). Businesses can proceed unless and until a consumer exercises the opt-out right.

**The Minor Exception: Where CCPA Is Stricter Than GDPR**
For consumers under 16, CCPA flips to opt-in:
- Ages 13-15: The consumer must affirmatively opt in to the sale of their personal information
- Under 13: A parent or guardian must opt in

This is not a GDPR concept and requires age-gating or verification logic if your service targets or is reasonably likely to reach minors.

**Practical Implication for GDPR Programmes**
If your GDPR programme uses consent as the lawful basis for marketing or advertising data processing, you have built opt-in controls that go beyond CCPA's requirements for adults. However, the consent management infrastructure you built for GDPR consent may not map cleanly to CCPA's opt-out mechanism—they are fundamentally different UX flows and technical implementations. You likely need a separate CCPA opt-out mechanism, not a repurposed GDPR consent widget.

---

## 5. Lawful Basis: A Concept That Does Not Exist in CCPA/CPRA

GDPR requires a lawful basis for every processing activity—consent, contract, legal obligation, vital interests, public task, or legitimate interests. The lawful basis framework drives your entire GDPR compliance structure (impact assessments, DPAs, data subject rights responses, retention decisions).

CCPA/CPRA has no equivalent concept. There is no requirement to identify a legal basis before processing personal information. The law instead operates through:
- Transparency obligations (notice of what you collect and why)
- Consumer control rights (opt-out of sale/sharing, limit SPI use, deletion)
- Prohibited practices (discrimination for exercising rights, processing beyond what was disclosed)

This has two practical consequences:

First, your GDPR legitimate interests assessments (LIAs) and consent records have no CCPA counterpart. You do not need to maintain or produce them for California compliance purposes.

Second, activities you currently justify under legitimate interests for GDPR purposes may face no CCPA hurdle at all—provided you disclose them in your privacy notice and honour consumer rights requests. Conversely, activities that are lawful under GDPR (e.g., you have a valid lawful basis) may still trigger CCPA obligations if they involve selling or sharing data, because CCPA imposes independent requirements regardless of whether a GDPR lawful basis exists.

---

## 6. Private Right of Action and Enforcement: A Critical Difference

**GDPR Enforcement**
GDPR enforcement is almost entirely regulatory. Data subjects can lodge complaints with supervisory authorities (DPAs), and the DPA investigates and issues fines (up to EUR 20 million or 4% of global annual turnover). Private lawsuits by individuals for GDPR violations are theoretically possible but relatively uncommon, expensive, and procedurally difficult in most EU jurisdictions.

**CCPA/CPRA Enforcement**

There are two tracks:

*Track 1: California Privacy Protection Agency (CPPA) and AG Enforcement*
The California Attorney General enforces CCPA/CPRA with civil penalties of up to $2,500 per unintentional violation and $7,500 per intentional violation. The CPPA (created by CPRA) has independent enforcement authority and rulemaking power. Unlike GDPR, there was historically a 30-day cure period before enforcement action could be brought—CPRA eliminated this cure period as of January 1, 2023.

*Track 2: Private Right of Action for Data Breaches*
This is a major divergence from GDPR. CCPA Section 1798.150 grants consumers a private right of action—without needing to prove actual damages—when their non-encrypted, non-redacted personal information is subject to a data breach resulting from a business's failure to implement reasonable security procedures. Statutory damages are $100 to $750 per consumer per incident, or actual damages if greater. Class action litigation is possible.

This creates direct litigation exposure that GDPR does not. The practical implication is that any California resident whose data is breached can potentially sue without proving they suffered harm. This changes the risk calculus for security investment and breach notification decisions.

**What This Means in Practice**
- You need to assess whether your security controls satisfy California's "reasonable security" standard (California's CIS Controls guidance is the relevant reference)
- Your breach response plan needs to specifically address the CCPA private right of action, including pre-litigation demand letter response procedures
- Cyber insurance policies should be reviewed to confirm CCPA class action coverage
- The litigation-exposure dimension of CCPA is not replicated in your GDPR programme and needs independent legal risk management

---

## 7. Vendor Contract Differences

**GDPR: Data Processing Agreements (DPAs)**
GDPR Article 28 requires a written DPA with every processor that handles personal data on your behalf. The DPA must include mandatory clauses covering processing only on instructions, confidentiality, security, sub-processor rules, data subject rights assistance, audit rights, and deletion or return of data.

**CCPA/CPRA: Service Provider and Contractor Agreements**

CCPA/CPRA distinguishes three third-party categories with different contract requirements:

*Service Providers:* Entities that process personal information on your behalf pursuant to a written contract. The contract must prohibit the service provider from: retaining, using, or disclosing personal information for any purpose other than the specified business purpose; selling or sharing the personal information; retaining, using, or disclosing the data outside the direct business relationship. The service provider must also grant you the right to audit their compliance (or provide equivalent independent assessment). Disclosures to service providers under a compliant contract do not constitute a "sale."

*Contractors:* A CPRA addition—entities to whom you make personal information available (not necessarily for processing on your behalf). Must execute a contract with similar prohibitions as service providers, and must certify compliance.

*Third Parties:* All other recipients. Sharing with third parties generally constitutes a sale or sharing, triggering the opt-out right.

**Key Contract Gaps if You Rely on GDPR DPAs**

Your GDPR DPAs will not automatically satisfy CCPA/CPRA because:
1. GDPR DPAs do not contain the CCPA-specific prohibitions on selling, sharing, or retaining data for unauthorised purposes
2. GDPR DPAs do not address the CCPA service provider certification requirement
3. The tripartite CCPA classification (service provider / contractor / third party) does not map to GDPR's controller/processor binary
4. Many GDPR DPAs omit the CCPA audit right language in the required form

**Recommended Action**
Add a CCPA/CPRA addendum to existing vendor DPAs. Many vendors offer standard CCPA addenda. Alternatively, incorporate CCPA service provider language into a unified privacy annex alongside GDPR terms. Prioritise vendors who receive data that could constitute a "sale" absent the service provider restriction—these carry the highest risk.

---

## 8. Scope and Applicability Thresholds

GDPR applies to any organisation that processes EU residents' data, regardless of size or revenue. CCPA applies to for-profit businesses that collect California consumers' personal information and meet ANY ONE of:
- Annual gross revenue exceeding $25 million
- Annually buys, sells, receives, or shares personal information of 100,000 or more California consumers or households (CPRA raised from CCPA's original 50,000)
- Derives 50% or more of annual revenue from selling consumers' personal information

This means some organisations subject to GDPR may not be subject to CCPA (small businesses below all thresholds). Conversely, the revenue threshold catches many US businesses not previously focused on GDPR.

---

## 9. Practical Gap-Closure Roadmap

For an organisation with a mature GDPR programme, the priority actions to close CCPA/CPRA gaps are:

**Immediate/High Priority**
1. Audit data flows for sales and sharing—determine which third-party data transfers constitute "sales" or "sharing" under CCPA's broad definitions
2. Implement the DNSMI opt-out mechanism, including GPC signal recognition
3. Implement the "Limit the Use of My SPI" mechanism for CPRA
4. Update privacy notice with California-specific disclosures (categories collected in the last 12 months, categories sold or shared, categories of sources, purposes)
5. Execute CCPA service provider addenda with all relevant vendors

**Medium Priority**
6. Build or update consumer rights intake to handle CCPA-specific rights (including authorised agent requests, the new correction right, and opt-out of automated decision-making)
7. Implement minor opt-in controls if your service reaches under-16 users
8. Review financial incentive programmes for CCPA compliance (valuation analysis, written programme terms)
9. Assess security controls against California's reasonable security standard; address gaps to limit private right of action exposure

**Ongoing**
10. Train customer-facing, marketing, and legal teams on CCPA's different framework (particularly the opt-out default and the absence of lawful basis requirements)
11. Monitor CPPA rulemaking—CPRA regulations on automated decision-making and risk assessments are still being finalised and will impose additional obligations
12. Update breach response procedures to address CCPA private right of action

---

## Summary: Where the Two Laws Differ Most Significantly

| Dimension | GDPR | CCPA/CPRA |
|---|---|---|
| Default posture | Opt-in (lawful basis required) | Opt-out (processing permitted, consumers can opt out of sale/sharing) |
| Lawful basis | Required for all processing | Not a concept in the law |
| Sale/sharing of data | No specific prohibition; addressed through lawful basis | Core focus; distinct opt-out right required |
| Sensitive data | Special category—generally requires explicit consent | SPI—right to limit use to necessary purposes |
| Private right of action | Rare; primarily regulatory enforcement | Yes, for data breaches; statutory damages without proof of harm |
| Enforcement body | National data protection authorities (EU/EEA) | California AG + California Privacy Protection Agency |
| Vendor contracts | DPA required; controller/processor binary | Service provider / contractor / third party tripartite; different prohibited-use clauses |
| Minor protections | Age of digital consent (13-16 varies by member state) | Affirmative opt-in for under-16; parental for under-13 |
| Financial incentives | Not addressed | Permitted with disclosure and value justification |
| Retention limitation | Explicit principle (Article 5(1)(e)) | CPRA added minimisation principle; less prescriptive than GDPR |

The deepest structural difference is the inversion of the consent model. GDPR treats data as locked until a basis is established; CCPA treats data as available unless the consumer objects. Both protect individuals, but they require fundamentally different compliance architectures—which is why a GDPR programme, while enormously helpful, does not substitute for CCPA/CPRA compliance work.
