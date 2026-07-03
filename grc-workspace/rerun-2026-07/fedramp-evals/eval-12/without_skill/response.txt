FedRAMP Impact Levels: Low, Moderate, and High
================================================

FedRAMP impact levels are derived from FIPS 199 / NIST SP 800-60, which classify federal
information systems based on the potential impact to the confidentiality, integrity, and
availability of information if there were a security breach. Each system is rated Low,
Moderate, or High for each of the three security objectives (confidentiality, integrity,
availability), and the system's overall categorization is the HIGH-WATER MARK — i.e., the
highest of the three individual ratings.

1. FedRAMP Low
---------------
- Impact of a breach: Limited adverse effect on organizational operations, assets, or
  individuals.
- Typical data: Public or low-sensitivity information where loss of confidentiality,
  integrity, or availability would cause minor damage, minor financial loss, or minor harm.
- Control baseline: ~125-156 NIST SP 800-53 controls (Low baseline, FedRAMP-tailored).
- Common use cases: Public-facing websites, low-risk collaboration tools, systems with no
  PII or sensitive government data.
- Also note "Low-Impact SaaS (LI-SaaS)" — a lighter-weight baseline for low-risk SaaS
  applications with minimal data storage.

2. FedRAMP Moderate
--------------------
- Impact of a breach: Serious adverse effect on operations, assets, or individuals (this is
  the most common FedRAMP baseline — roughly 80% of authorized CSPs use Moderate).
- Typical data: Controlled Unclassified Information (CUI), personally identifiable
  information (PII), and most non-public federal agency data used in day-to-day operations.
- Control baseline: ~325 controls from NIST SP 800-53.
- Common use cases: Standard SaaS/PaaS/IaaS platforms handling typical agency business data,
  HR systems, case management systems, most cloud productivity and collaboration platforms.

3. FedRAMP High
----------------
- Impact of a breach: Severe or catastrophic adverse effect on operations, assets, or
  individuals — including loss of life, major financial loss, or major mission failure.
- Typical data: The most sensitive unclassified data used in the government's most sensitive
  and critical unclassified systems. This includes data related to:
  - Law enforcement (e.g., criminal investigations, evidentiary data)
  - Emergency services
  - Financial systems with significant financial impact
  - Health information at large scale
  - Other systems where a breach could threaten public safety, national economic security,
    or civilian liberty
- Control baseline: ~421 controls from NIST SP 800-53 (the most stringent baseline),
  including enhanced requirements for encryption, incident response, continuous monitoring,
  and personnel security.
- Common use cases: Systems supporting law enforcement, emergency response, healthcare
  delivery at scale, and financial management for federal agencies.

Key Differences Summary
------------------------
| Factor                  | Low            | Moderate         | High                    |
|--------------------------|----------------|------------------|-------------------------|
| Breach impact            | Limited        | Serious          | Severe/Catastrophic     |
| Approx. control count    | ~125-156       | ~325             | ~421                    |
| Typical data              | Public data    | CUI, PII, agency data | LE-sensitive, life-safety, high-value financial data |
| % of marketplace          | Small minority | ~80% majority    | Small minority          |
| Authorization difficulty  | Lowest effort  | Moderate effort  | Highest effort/cost     |

Which Impact Level Applies to Law Enforcement Sensitive Data?
----------------------------------------------------------------
Data explicitly described as "law enforcement sensitive" (LES) is one of the specific
categories NIST SP 800-60 and FedRAMP guidance call out as warranting a HIGH impact rating,
particularly for the confidentiality objective. Law enforcement data often carries the risk
that unauthorized disclosure or loss of integrity could:
- Compromise ongoing investigations or informants
- Endanger law enforcement personnel or witnesses
- Undermine judicial proceedings
- Threaten public safety

Because of this, systems that store, process, or transmit law enforcement sensitive data
are almost always categorized as FedRAMP HIGH, not Moderate. This is consistent with
FedRAMP's own guidance, which explicitly lists "law enforcement" as an example use case
for the High baseline (alongside emergency services and healthcare at scale).

Recommendation for Your Product
---------------------------------
Given that your product handles law enforcement sensitive data:
1. Plan for FedRAMP HIGH — this is the baseline you should scope your architecture,
   controls, and budget around. Do not assume Moderate will suffice.
2. Confirm with your sponsoring agency. The agency's own data owner/Authorizing Official
   (AO) makes the final categorization decision using FIPS 199 / NIST SP 800-60, in
   consultation with your team. If the agency you're working with (e.g., DOJ, FBI, DHS
   component, or a state/local justice partner via a federal sponsor) confirms the data is
   "law enforcement sensitive," they will very likely require High.
3. Expect a heavier lift: FedRAMP High requires the full ~421-control baseline, more
   rigorous continuous monitoring, stronger encryption (FIPS 140-2/140-3 validated
   cryptography), enhanced incident response timelines, and typically a longer, more
   expensive 3PAO assessment and ATO process compared to Moderate.
4. Boundary scoping matters: If only a discrete subset of your system touches law
   enforcement sensitive data, you may be able to isolate that data within a more tightly
   scoped High-categorized boundary or enclave, while the rest of the system remains
   Moderate — but this requires careful system security plan (SSP) boundary design and
   agency concurrence. In practice, many CSPs find it simpler to run the entire authorized
   boundary at High if LES data is a core part of the product's value proposition.

Bottom line: Because your product handles law enforcement sensitive data, you should plan
for and pursue FedRAMP High, and validate that determination early with your federal
sponsoring agency's Authorizing Official.
