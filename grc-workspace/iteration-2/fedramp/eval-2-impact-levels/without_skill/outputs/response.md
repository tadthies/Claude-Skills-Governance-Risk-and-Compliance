# FedRAMP Impact Levels: Low, Moderate, and High

## The Basis for Impact Level Determination: FIPS 199

FedRAMP impact levels are derived from **FIPS 199** (Federal Information Processing Standard Publication 199 — "Standards for Security Categorization of Federal Information and Information Systems"). FIPS 199 defines the potential adverse impact of a security breach along three dimensions:

- **Confidentiality**: Protection against unauthorized disclosure
- **Integrity**: Protection against unauthorized modification or destruction
- **Availability**: Ensuring reliable access and use

Each dimension is rated Low, Moderate, or High. The system's overall impact level is the **high-water mark** — the highest rating across all three dimensions.

---

## FedRAMP Low Impact

**Definition**: Loss of confidentiality, integrity, or availability would have a **limited adverse effect** on organizational operations, assets, or individuals.

**Characteristics**:
- Non-sensitive federal information
- No PII or limited, non-sensitive PII
- Business disruption would be minor
- Example use cases: Public websites, collaboration tools for non-sensitive work

**Approximate control count**: ~125 controls (NIST SP 800-53)

**Special Category — LI-SaaS**:
LI-SaaS (Low Impact Software as a Service) is a tailored subset of the Low baseline for SaaS products that:
- Store no federal data (only transit or process it briefly)
- Have no PII
- Meet a simplified authorization profile with fewer required controls (~47 controls)
This is the lightest-weight FedRAMP path but applies only to a narrow set of qualifying SaaS products.

---

## FedRAMP Moderate Impact

**Definition**: Loss of confidentiality, integrity, or availability would have a **serious adverse effect** on organizational operations, assets, or individuals.

**Characteristics**:
- The most common impact level — majority of FedRAMP-authorized services are Moderate
- Federal information where unauthorized access would significantly harm mission performance
- May include some PII or sensitive-but-unclassified information
- Example use cases: Agency productivity suites, HR systems, financial management systems

**Approximate control count**: ~325 controls

---

## FedRAMP High Impact

**Definition**: Loss of confidentiality, integrity, or availability would have a **severe or catastrophic adverse effect** on organizational operations, assets, or individuals.

**Characteristics**:
- Most stringent FedRAMP baseline
- Data where compromise could cause severe harm — loss of life, major financial damage, mission failure
- Applies to emergency services, law enforcement, health records, and financial crime systems
- Requires the most robust security architecture and controls
- Example use cases: Law enforcement databases, criminal justice systems, Veterans Affairs health records, emergency response platforms

**Approximate control count**: ~421 controls

---

## Comparison Table

| Level | Adverse Impact | Control Count | Typical Use Cases |
|---|---|---|---|
| Low | Limited | ~125 | Public info, non-sensitive collaboration |
| LI-SaaS | Limited (SaaS-specific) | ~47 | No-storage SaaS only |
| Moderate | Serious | ~325 | Most federal cloud services |
| High | Severe / Catastrophic | ~421 | Law enforcement, health, financial crime |

---

## Your Situation: Law Enforcement Sensitive Data

Products handling **law enforcement sensitive data** almost certainly require **FedRAMP High**.

**Why High applies**:
- Law enforcement data (criminal records, case files, investigative records, informant data) is explicitly categorized as requiring the highest confidentiality protections in federal guidance
- Unauthorized disclosure of law enforcement data can compromise active investigations, endanger individuals, and violate legal protections
- FIPS 199 analysis for law enforcement data routinely results in a High confidentiality rating, which drives the overall categorization to High

**Practical implications of FedRAMP High**:
- Approximately 421 controls to implement under NIST SP 800-53
- More stringent requirements across nearly every control family
- FIPS 140-2 validated encryption is mandatory
- Multi-factor authentication requirements are more extensive
- Physical and environmental controls are more demanding
- Infrastructure must be FedRAMP High authorized (e.g., AWS GovCloud, Azure Government)
- Longer timeline and higher cost to achieve authorization

**Recommendation**: Plan for FedRAMP High from the outset. Have a qualified 3PAO conduct a formal FIPS 199 / FIPS 200 security categorization to confirm, but given the nature of law enforcement data, a High designation is the expected outcome.
