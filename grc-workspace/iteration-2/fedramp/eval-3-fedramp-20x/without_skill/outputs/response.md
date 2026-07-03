# FedRAMP 20x: Overview and Path Selection Guidance

## What Is FedRAMP 20x?

**FedRAMP 20x** is a modernization initiative launched by the FedRAMP Program Management Office (PMO) to reform and streamline the federal cloud authorization process. The "20x" designation signals a significant generational improvement — the goal is to make FedRAMP authorization dramatically faster, more automated, and more continuous than the traditional process.

FedRAMP 20x represents a philosophical shift from the legacy model, which relied on large, document-heavy, point-in-time security packages, to a more agile, technology-driven approach centered on automation, machine-readable data formats, and continuous compliance validation.

---

## Key Changes FedRAMP 20x Introduces

### 1. Automation and Continuous Assessment
Traditional FedRAMP authorizations are largely manual processes — teams produce static documents (SSP, SAP, SAR, POA&M) that represent a point-in-time assessment. FedRAMP 20x aims to automate significant portions of the assessment process by:
- Enabling automated control validation through tooling
- Collecting security evidence continuously rather than at discrete assessment intervals
- Integrating continuous monitoring more tightly with the authorization itself

### 2. Machine-Readable Controls via OSCAL
A central pillar of FedRAMP 20x is the adoption of **OSCAL (Open Security Controls Assessment Language)** — a set of machine-readable data formats developed by NIST for expressing security control catalogs, profiles, system security plans, assessment plans, and assessment results.

OSCAL enables:
- Automated validation of security packages
- Machine-to-machine exchange of authorization data
- Reduced manual document review burden
- Reusable control implementations

The FedRAMP PMO has been moving toward requiring OSCAL submissions, with mandates for OSCAL-format packages being rolled out progressively.

### 3. Continuous Monitoring Improvements
FedRAMP 20x envisions a more integrated continuous monitoring (ConMon) model where security posture is assessed and reported on an ongoing basis rather than through discrete monthly/annual reporting cycles. This is intended to reduce the lag between when vulnerabilities exist and when they are identified and remediated.

### 4. Modular, Iterative Authorizations
FedRAMP 20x supports more modular approaches to authorization, potentially allowing CSPs to authorize incremental portions of a system rather than requiring a complete system-wide assessment every time.

---

## Current Status and Timeline of FedRAMP 20x

FedRAMP 20x has been an evolving initiative:

- The FedRAMP PMO began publicizing FedRAMP 20x concepts and pilots in the early-to-mid 2020s
- Pilot programs have allowed select CSPs to test the new approach
- The program is actively rolling out — guidance, templates, and requirements continue to be published at fedramp.gov
- **OSCAL adoption** is being phased in, with the PMO increasingly expecting or requiring OSCAL-format submissions for new authorizations
- The traditional SSP/SAP/SAR template-based process remains in effect and available for CSPs not yet able to participate in FedRAMP 20x

**Current status**: FedRAMP 20x is an active, ongoing initiative. CSPs should check fedramp.gov regularly for the latest guidance, as the program's requirements and timelines are actively evolving.

---

## FedRAMP 20x vs. Traditional FedRAMP Authorization

| Dimension | Traditional FedRAMP | FedRAMP 20x |
|---|---|---|
| Assessment model | Point-in-time | Continuous / automated |
| Package format | PDF/Word templates | OSCAL (machine-readable) |
| Evidence collection | Manual, periodic | Automated tooling |
| ConMon | Separate monthly/annual process | Integrated continuous assessment |
| Speed | 12–24+ months | Designed to be faster |
| Maturity | Established, well-understood | Still evolving |
| Guidance availability | Comprehensive | Actively being developed |

---

## Should You Pursue FedRAMP 20x or Traditional Authorization?

### Consider FedRAMP 20x If:
- You are a **cloud-native organization** with modern DevSecOps practices
- You have the engineering capacity to invest in **OSCAL tooling** and automated compliance
- You want to position for the long-term future of FedRAMP
- You are a new entrant without legacy investment in traditional FedRAMP processes

### Consider Traditional Authorization If:
- You need a **proven, well-understood path** with comprehensive existing guidance
- Your system is complex and does not fit an incremental modular approach
- You have an agency sponsor ready to work within the traditional package review model
- You need authorization quickly and FedRAMP 20x guidance for your use case is still being finalized

### Practical Recommendation:
For most new CSPs today, **begin with traditional FedRAMP authorization** while **investing in OSCAL capabilities in parallel**. The traditional process has clear, established templates and requirements; FedRAMP 20x is still maturing. However, since OSCAL is increasingly expected (and will be required), building OSCAL tooling now is wise regardless of which path you formally pursue.

Stay engaged with the FedRAMP PMO and monitor fedramp.gov — as FedRAMP 20x matures, migrating to it (or starting with it, for later-stage entrants) will likely become the better option.

---

*This guidance is based on publicly available FedRAMP information. Check fedramp.gov for the latest FedRAMP 20x requirements and timelines, as the program is actively evolving.*
