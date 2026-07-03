# GDPR to CCPA/CPRA Gap Analysis: What You Still Need to Do

## Executive Summary

Your existing GDPR programme gives you a genuinely strong foundation — privacy notices, data subject rights processes, processor agreements, data minimisation practices, and records of processing activities all translate meaningfully to CCPA/CPRA. However, GDPR compliance does **not** automatically satisfy CCPA/CPRA. California's law was built on a different legal philosophy and introduces obligations that GDPR simply does not contemplate. The gaps are specific, concrete, and in several cases require visible consumer-facing changes to your website and contracts.

---

## 1. GDPR as Foundation — But Not a Complete Answer

GDPR and CCPA/CPRA share common DNA: both require transparency about data collection and use, both grant consumers/data subjects rights over their personal data, and both impose obligations on businesses when they engage third-party vendors to process data. Your GDPR programme will have already produced:

- **Privacy notices** disclosing categories of data collected and purposes of use
- **Data subject rights workflows** for access, deletion, and portability
- **Data processing agreements (DPAs)** with vendors and processors
- **Data minimisation and purpose limitation controls**
- **Records of processing activities (RoPA)**

All of these map to analogous CCPA/CPRA requirements and give you a running start. That said, CCPA/CPRA was enacted independently of GDPR and contains obligations that exist nowhere in the European framework. Treating your GDPR programme as a "done" answer to CCPA/CPRA compliance is a common and costly mistake.

---

## 2. CCPA/CPRA-Specific Additions You Must Implement

### 2a. "Do Not Sell or Share My Personal Information" Link

This is the most visible and California-specific obligation. If your business sells or shares personal information — including sharing for cross-context behavioural advertising — you must:

- **Post a clear and conspicuous link** titled "Do Not Sell or Share My Personal Information" on your homepage and any page where personal information is collected.
- **Process opt-out requests within 15 business days** of receipt and instruct downstream third parties to comply within 90 days.
- **Honour Global Privacy Control (GPC) signals** automatically. As of current CPPA enforcement guidance, if a consumer's browser sends a GPC opt-out signal, your systems must treat it as a valid opt-out request without requiring any further action from the consumer. This is a technical implementation requirement — your tag management, consent management platform (CMP), and advertising stack must be configured to detect and act on GPC.

GDPR has no equivalent to this link or GPC obligation. Your GDPR cookie consent banner does not satisfy this requirement.

### 2b. "Limit the Use of My Sensitive Personal Information" Link (CPRA Addition)

CPRA (the 2020 amendment to CCPA, operative since January 1, 2023) introduced a separate category of "sensitive personal information" (SPI) with its own opt-out right. SPI includes:

- Social Security and government ID numbers
- Financial account credentials
- Precise geolocation
- Racial or ethnic origin, religious beliefs, union membership
- Contents of mail, email, and text messages
- Genetic and biometric data
- Health and sex life data

If you use SPI for purposes beyond those listed as necessary under CPRA (e.g., providing the requested service), you must:

- **Post a separate "Limit the Use of My Sensitive Personal Information" link** on your homepage.
- Allow consumers to restrict SPI use to narrowly defined permitted purposes.

Note: while GDPR also treats many of these same categories as "special category data" requiring explicit consent under Article 9, the CPRA mechanism is different — it is an **opt-out** right (consumers must affirmatively request limitation), not a consent gate. The practical implementation differs significantly.

### 2c. Automated Decisionmaking Technology (ADMT) Opt-Out

CPRA regulations require businesses using ADMT — defined broadly to include profiling that produces legal or similarly significant effects — to provide consumers with the right to opt out. The compliance deadline for ADMT opt-out mechanisms is **January 1, 2027**. You should begin scoping this now: identify all automated systems used for profiling, assess whether they produce significant effects on consumers, and design your opt-out workflow.

---

## 3. The Opt-Out vs. Opt-In Model Difference

This is the most fundamental philosophical difference between the two regimes, and it has significant practical consequences.

**GDPR is predominantly an opt-in regime** for high-risk and marketing processing. Sensitive data requires explicit consent (Article 9). Marketing based on profiling requires consent or a legitimate interests assessment. Consent must be freely given, specific, informed, and unambiguous — and pre-ticked boxes do not qualify.

**CCPA/CPRA is primarily an opt-out regime.** Businesses may collect and use personal information — including for sale and sharing — until a consumer exercises their right to opt out. There is no requirement to obtain consumer consent before collecting or selling data; the obligation is to stop once an opt-out is received and to make opting out easy.

**Practical consequences of this difference:**

| Scenario | GDPR Requirement | CCPA/CPRA Requirement |
|---|---|---|
| Email marketing to existing customers | Consent or legitimate interests (with balancing test) | Opt-out link in each email; no pre-collection consent required |
| Behavioural advertising via third-party cookies | Consent before placement | "Do Not Sell or Share" link; honour GPC signals |
| Profiling for credit decisions | Likely requires explicit consent; DPIA required | Opt-out from ADMT (from Jan 2027); no upfront consent needed |
| Collecting SPI (e.g., precise geolocation) | Explicit consent under Art. 9 | "Limit SPI" link + opt-out mechanism; no prior consent required |

If your business is operating under GDPR consent models, you may be more restrictive than CCPA/CPRA requires in some areas — but you cannot assume that your consent gates satisfy California's opt-out infrastructure, because they address the problem from opposite directions.

---

## 4. No Lawful Basis Requirement Under CCPA/CPRA

GDPR's six lawful bases for processing (Article 6) — consent, contract, legal obligation, vital interests, public task, and legitimate interests — have **no equivalent under CCPA/CPRA**. California law does not require a business to identify or document a legal basis before collecting or processing personal information.

This means:

- **You do not need to map lawful bases to CCPA/CPRA processing activities.** Your GDPR RoPA lawful basis column is irrelevant in the California context.
- **Legitimate interests assessments (LIAs)** are a GDPR concept with no CCPA/CPRA counterpart.
- **Consent is not a prerequisite** to data collection under California law, except in limited circumstances (e.g., certain uses of SPI for advertising purposes, or ADMT in certain contexts under CPRA regulations).

However, this cuts both ways: CCPA/CPRA introduces obligations (the opt-out mechanisms, the specific notice requirements, the vendor contract clauses) that GDPR does not, and your lawful basis documentation does nothing to satisfy them.

---

## 5. Private Right of Action and Vendor Contract Differences

### 5a. Private Right of Action for Data Breaches

This is one of the most significant legal exposure differences between the two regimes.

**GDPR** does not give individual data subjects a private right of action for damages in most jurisdictions — enforcement is handled by supervisory authorities (DPAs), which can impose fines of up to €20 million or 4% of global annual turnover. Individual data subjects may claim compensation under Article 82, but this requires litigation through national courts and proof of material or non-material damage.

**CCPA/CPRA** creates a **statutory private right of action** for consumers whose non-encrypted, non-redacted personal information is subject to a data breach resulting from a business's failure to implement reasonable security measures. Consumers can sue without proving actual harm and recover **$100 to $750 per consumer per incident** (or actual damages, whichever is greater), plus injunctive relief and attorneys' fees. Class actions multiply this dramatically.

**What this means for your risk posture:**

- California data breaches carry immediate, scalable litigation risk that European breaches do not carry in the same way.
- Your security controls and breach response programme must be evaluated against CCPA/CPRA's "reasonable security" standard (California's current guidance references the CIS Controls).
- Cyber insurance policies should be reviewed to confirm CCPA/CPRA class action exposure is covered.
- Breach notification under CCPA/CPRA is governed by California's separate data breach notification law (Cal. Civ. Code § 1798.29 and § 1798.82), not CCPA itself — but the private right of action activates on the same underlying security failure event.

### 5b. Vendor and Service Provider Contract Differences

Your GDPR Data Processing Agreements are a good starting point, but CCPA/CPRA "service provider" contracts require specific clauses that differ from GDPR DPA requirements:

| Required Clause | GDPR DPA (Art. 28) | CCPA/CPRA Service Provider Agreement |
|---|---|---|
| Purpose limitation | Yes — processing only on documented instructions | Yes — prohibited from retaining, using, or disclosing PI for any purpose other than specified business purposes |
| Prohibition on sale/sharing | Not applicable (no "sale" concept) | **Required** — service provider must certify it will not sell or share PI received from the business |
| Deletion of PI on contract termination | Yes | Yes |
| Audit rights | Yes | Yes |
| Subprocessor restrictions | Yes | Yes — subcontractors must be bound by equivalent restrictions |
| Certification of understanding | Not required | **Required** — service provider must certify it understands and will comply with restrictions |
| Contractor/third-party distinction | Not applicable | Contracts must specify whether recipient is a "service provider," "contractor," or "third party" — each carries different obligations |

**Action required:** Review all existing vendor DPAs and add CCPA/CPRA-specific addenda or standalone service provider agreements. Particular attention is needed for advertising technology vendors, analytics providers, and data brokers, where the "sale" and "sharing" concepts are most likely triggered.

---

## 6. Summary Gap Checklist

The following items are required under CCPA/CPRA but are NOT covered by your existing GDPR programme:

| Gap | Priority | Deadline |
|---|---|---|
| "Do Not Sell or Share My Personal Information" link on website | Critical | Immediate |
| GPC (Global Privacy Control) signal detection and compliance | Critical | Immediate |
| "Limit the Use of My Sensitive Personal Information" link (if applicable) | High | Immediate |
| Updated privacy notice with CCPA/CPRA-required disclosures | High | Immediate |
| Consumer opt-out request intake and processing workflow (15-day response) | High | Immediate |
| CCPA/CPRA service provider agreement clauses added to vendor contracts | High | Immediate |
| ADMT opt-out mechanism design and implementation | Medium | January 1, 2027 |
| "Reasonable security" controls audit under California standard | High | Immediate |
| Cyber insurance review for CCPA class action coverage | Medium | Near-term |
| CPPA regulatory monitoring programme | Ongoing | Continuous |

---

## 7. Key Takeaway

GDPR and CCPA/CPRA are complementary but not interchangeable. Your GDPR programme gives you documentation discipline, rights workflows, and vendor management practices that map directly to California requirements. But the structural differences — opt-out rather than opt-in, no lawful basis requirement, the "Do Not Sell or Share" and GPC obligations, the SPI limitation mechanism, the private right of action, and the specific vendor contract clauses — require dedicated CCPA/CPRA work that cannot be satisfied by pointing to your European compliance programme.

Treat the two frameworks as parallel obligations. Where they overlap, your GDPR controls will satisfy both. Where they diverge — particularly on the consumer-facing opt-out infrastructure and the litigation exposure from breaches — CCPA/CPRA requires its own dedicated solution.
