# FedRAMP Impact Levels and CR26 Certification Classes

## Important Context: CR26 Transition

As of July 2026, FedRAMP is undergoing **CR26 (Certification Reform 2026)**, which is replacing FIPS 199-based impact levels (Low/Moderate/High/LI-SaaS) with **Certification Classes A–D**. However, existing FedRAMP documentation still references Low/Moderate/High extensively, and the CR26 class-to-control baseline mapping is still being published by the FedRAMP PMO. This response covers both the legacy framework (which remains in active use) and the emerging CR26 structure.

---

## Legacy FedRAMP Impact Levels (FIPS 199-Based)

### Basis for Categorization: FIPS 199

The Federal Information Processing Standard (FIPS) Publication 199 — "Standards for Security Categorization of Federal Information and Information Systems" — is the foundational standard for determining impact level. FIPS 199 defines impact based on the potential adverse effect on an organization if information or a system is compromised, with three dimensions:
- **Confidentiality** (unauthorized disclosure)
- **Integrity** (unauthorized modification or destruction)
- **Availability** (disruption of access or use)

Each dimension is rated Low, Moderate, or High. The overall impact level is the **high-water mark** — the highest rating across all three dimensions determines the system's categorization.

---

### FedRAMP Low Impact

**Definition**: Compromise would have a **limited adverse effect** on agency operations, assets, or individuals.

**Characteristics**:
- No personally identifiable information (PII)
- Publicly available data or non-sensitive federal information
- Loss of confidentiality, integrity, or availability would not significantly impair mission capability

**Control Count (NIST SP 800-53 Rev 5)**: Approximately **156 controls**

**Special Category — LI-SaaS (Low Impact SaaS)**:
LI-SaaS is a tailored baseline for low-impact Software-as-a-Service offerings that meet specific criteria:
- No sensitive federal data (no PII, no law enforcement data, no national security information)
- Federal data is not stored in the service (only transited or processed temporarily)
- Simplified authorization process with reduced documentation requirements
- Leverages a subset of ~47 controls from the Low baseline
- Must have a sponsoring agency; not eligible for JAB review
- Not all SaaS products qualify — the CSP must demonstrate the reduced-impact profile

---

### FedRAMP Moderate Impact

**Definition**: Compromise would have a **serious adverse effect** on agency operations, assets, or individuals.

**Characteristics**:
- Most common impact level — covers the majority of FedRAMP authorizations
- Federal information where unauthorized disclosure, modification, or unavailability would significantly impair mission capability
- May include some PII or sensitive-but-unclassified (SBU) information

**Control Count (NIST SP 800-53 Rev 5)**: **323 controls**

**Examples**: Agency financial systems, HR systems, collaboration tools handling government data, most SaaS platforms used by federal workers

---

### FedRAMP High Impact

**Definition**: Compromise would have a **severe or catastrophic adverse effect** on agency operations, assets, or individuals.

**Characteristics**:
- Most stringent FedRAMP baseline
- Systems handling the most sensitive unclassified federal data
- Compromise could result in severe harm to individuals, mission failure, or significant financial damage
- Applies to systems where loss of confidentiality, integrity, or availability would be catastrophic

**Control Count (NIST SP 800-53 Rev 5)**: **421 controls**

**Examples**: Law enforcement systems, criminal justice data, healthcare/health records systems (VA, HHS), financial crime systems, emergency response systems

---

## CR26 Certification Classes (Replacing Impact Levels)

Under CR26, the FedRAMP PMO is aligning control baselines to Certification Classes:

| Class | Name | Legacy Equivalent | Description |
|---|---|---|---|
| A | Basic | Low | Cloud-native, low federal data sensitivity; limited scope |
| B | Standard | Moderate | Most common — federal data with serious adverse effect if compromised |
| C | Enhanced | High | Severe/catastrophic effect if compromised — law enforcement, financial, health data |
| D | Specialized | New category | Critical/ultra-sensitive systems with additional requirements |

> The FedRAMP PMO is publishing updated control baselines aligned to each class. CSPs should monitor fedramp.gov for final CR26 class-based control counts.

---

## Your Situation: Law Enforcement Sensitive Data

**Assessment**: Products handling **law enforcement sensitive data** almost certainly require **FedRAMP High impact (Class C under CR26)**.

Here is the reasoning:

1. **Law enforcement data is explicitly cited as High-impact data**: The FedRAMP documentation and federal data categorization guidance consistently categorizes law enforcement sensitive information (criminal records, case files, investigative data, surveillance data) at the High impact level under FIPS 199.

2. **Confidentiality is paramount**: Law enforcement data typically requires the highest confidentiality protections — unauthorized disclosure could compromise investigations, endanger informants, or violate individuals' rights.

3. **CR26 Class C alignment**: Under CR26, Class C (Enhanced) explicitly covers data where compromise has "severe or catastrophic effect," including law enforcement data. This maps directly to your use case.

4. **What this means for you**:
   - **421 controls** to implement under NIST SP 800-53 Rev 5 (High baseline)
   - More stringent requirements in areas like encryption (FIPS 140-2/3), access control, incident response, and physical security
   - Fewer IaaS platforms are FedRAMP High authorized (though AWS GovCloud is FedRAMP High authorized, which is commonly used)
   - More intensive 3PAO assessment and longer authorization timeline
   - Likely requires engagement with law enforcement or defense agencies as your authorization sponsor

**Recommendation**: Begin your FedRAMP journey assuming High impact / Class C. Engage a 3PAO early to conduct a formal FIPS 199 categorization assessment if you want an independent confirmation — but given the nature of law enforcement data, it would be unusual to land below High.

---

## Control Count Comparison

| Impact Level / Class | Controls (Rev 5) | Best For |
|---|---|---|
| Low / Class A | ~156 | Public-facing, non-sensitive apps |
| LI-SaaS | ~47 | Very limited-scope SaaS; no federal data storage |
| Moderate / Class B | 323 | Most federal cloud services |
| High / Class C | 421 | Law enforcement, health, financial, critical systems |

---

*Use official FedRAMP templates from fedramp.gov — this content should be inserted into the appropriate template section. Conduct a formal FIPS 199 categorization with your sponsoring agency to confirm your impact level.*
