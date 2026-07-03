# EU AI Act Compliance Analysis: Predictive Policing Tool for Municipal Deployment

## Executive Summary

A predictive policing AI system that scores neighbourhoods by crime risk using historical arrest data, social media monitoring, and demographic data falls squarely within the **highest-risk categories** under Regulation (EU) 2024/1689 (the EU AI Act). The vendor's characterisation as a mere "decision support tool" is legally irrelevant to classification and does not reduce regulatory obligations. Depending on specific system features, this deployment may be **outright prohibited** or, at minimum, subject to the most stringent conformity requirements under the Act.

---

## 1. Classification Under the EU AI Act

### 1.1 Definition of an AI System (Article 3)

The EU AI Act defines an AI system as a machine-based system designed to operate with varying levels of autonomy that, for explicit or implicit objectives, infers from inputs how to generate outputs such as predictions, content, recommendations, or decisions that can influence real or virtual environments. A neighbourhood crime-risk scoring tool plainly meets this definition: it ingests data, applies inference techniques (machine learning, statistical modelling, or similar), and produces outputs (risk scores) that influence real-world decisions about resource deployment, surveillance, and potentially individual targeting.

### 1.2 Prohibited AI Practices (Article 5)

Several prohibitions in Article 5 of the EU AI Act are directly relevant:

**Article 5(1)(d) — Real-time remote biometric identification in publicly accessible spaces for law enforcement purposes**
If the social media monitoring component scrapes or processes photos, videos, or voice data to identify individuals in conjunction with the neighbourhood scoring, there is a serious risk of crossing into prohibited real-time biometric identification. Although the tool may be framed as neighbourhood-level, individual-level profiling derived from social media can constitute de facto biometric identification when combined with location data.

**Article 5(1)(e) — Biometric categorisation systems using sensitive attributes**
The use of demographic data (which may include or correlate with race, ethnicity, national origin, religion, or other protected characteristics) as an input to a risk-scoring model constitutes exactly the kind of biometric categorisation system in the context of law enforcement that Article 5(1)(e) prohibits. Even if demographic data is not labelled as such, proxy variables derived from arrest history in areas with historically discriminatory policing practices can effectively categorise individuals or groups by protected characteristics.

**Article 5(1)(f) — AI systems assessing or predicting the risk of a natural person committing criminal offences based solely on profiling or personality traits**
This prohibition applies directly to systems that profile individuals or groups for criminal risk. A neighbourhood-level crime-risk scoring system based on historical arrest data and demographic features is, in substance, a profiling system that attributes criminal risk to people in specific areas based on group characteristics. The prohibition does not require that individual persons be named — profiling populations by geographic location using demographic proxies may constitute individual risk assessment when combined with enforcement actions targeting those areas.

**Critical point:** If any of these prohibitions apply, no amount of technical safeguards, transparency, or human oversight can remedy the situation. The system cannot be deployed lawfully in the EU regardless of how it is marketed.

### 1.3 High-Risk AI System Classification (Annex III)

Even if the system avoids the absolute prohibitions, it is a **high-risk AI system** under Annex III, Point 6 (AI systems intended to be used by or on behalf of competent authorities or Union institutions, bodies, offices or agencies for:

- **6(a)**: Performing risk assessments of natural persons with a view to assessing the risk of them offending or re-offending
- **6(b)**: Use as polygraphs or similar tools
- **6(c)**: Making risk assessments regarding criminal activity within law enforcement contexts

Neighbourhood crime risk scoring is unambiguously within Point 6(a) and (6(c)) of Annex III. The fact that it operates at neighbourhood rather than individual level does not remove this classification — the risk assessments still influence enforcement actions that affect individuals within those areas.

**Note on the "decision support" framing:** Article 6 and Annex III make clear that classification as high-risk is based on the system's intended purpose and actual use in the operational context, not on vendor marketing language. A system is "intended" for a purpose if it is placed on the market or put into service for that use, regardless of disclaimers. Municipal law enforcement use of a crime-risk scoring tool is precisely the scenario the high-risk classification was designed to capture.

---

## 2. High-Risk AI System Requirements (Articles 8–15 and 26)

If the system is classified as high-risk (and avoids outright prohibition), it must comply with a comprehensive set of obligations before and during deployment:

### 2.1 Risk Management System (Article 9)

A continuous risk management process must be established and documented throughout the AI system's lifecycle, including:
- Identification and analysis of reasonably foreseeable risks to health, safety, or fundamental rights
- Estimation and evaluation of risks emerging from intended use and reasonably foreseeable misuse
- Adoption of appropriate risk management measures
- Residual risk evaluation after measures are applied

For a predictive policing tool, this risk management system must specifically address the risk of discriminatory outcomes, over-policing of minority communities, self-reinforcing feedback loops (where increased policing of certain areas generates more arrests, which feeds back into the model as evidence of higher crime), and violations of the presumption of innocence.

### 2.2 Data and Data Governance (Article 10)

This is one of the most demanding requirements and one most likely to be problematic:

- Training, validation, and testing datasets must be subject to data governance and management practices
- Datasets must be relevant, sufficiently representative, and free of errors and complete to the extent possible
- **Datasets must be examined for possible biases** that could affect fundamental rights or lead to discrimination
- Appropriate bias detection and mitigation measures must be implemented

Historical arrest data is inherently problematic under Article 10. Research consistently shows that arrest data reflects prior policing practices and biases rather than the underlying distribution of criminal activity. Using biased arrest data as a proxy for crime rates will systematically over-predict risk in areas with historically over-policed minority populations. This is not a technical deficiency that can be corrected by adding more data — it is a structural problem with the training data itself that may make compliance with Article 10 impossible.

### 2.3 Technical Documentation (Article 11 and Annex IV)

Detailed technical documentation must be drawn up before placing the system on the market, covering:
- General description, intended purpose, and version history
- Description of the elements and components, including hardware requirements
- Design specifications, including architecture and logic of algorithms
- Description of the training methodology and training datasets
- Validation and testing procedures and test datasets used
- Monitoring, functioning, and control capabilities

The municipality, as deployer, should request this documentation from the vendor before any procurement. Absence of this documentation should be treated as a serious red flag.

### 2.4 Record-Keeping and Logging (Article 12)

High-risk AI systems must have capabilities to automatically record events throughout operation (logging). For law enforcement AI, this must enable reconstruction of queries, risk scores generated, parameters used, and system state at the time of each output. This logging is essential for accountability and for investigating complaints of discriminatory treatment.

### 2.5 Transparency and Information to Deployers (Article 13)

The system must be designed to operate with sufficient transparency to enable deployers to interpret its output and use it appropriately. The information provided with the system must include:
- The system's capabilities and limitations
- Performance metrics on specified test sets, including with regard to persons or groups of persons where testing was carried out
- Known and foreseeable circumstances under which the system may fail or produce inaccurate outputs
- The level of accuracy on specific groups of persons, if available

### 2.6 Human Oversight (Article 14)

High-risk AI systems must be designed and developed in a way that enables effective human oversight. Specifically, the persons assigned to oversight must be able to:
- Fully understand the system's capabilities and limitations
- Monitor operation for signs of anomaly, dysfunction, or unexpected performance
- Decide not to use the system or override its output
- Intervene or stop the system via a halt function

This is directly relevant to the "decision support tool" framing. While the vendor's characterisation implies human decisions are still taken by officers or commanders, Article 14 requires that this human oversight be *meaningful* rather than nominal. If officers routinely act on crime-risk scores without genuine evaluation of alternatives, the "human in the loop" is illusory and does not satisfy Article 14. The deploying municipality bears responsibility for ensuring genuine oversight is operational.

### 2.7 Accuracy, Robustness, and Cybersecurity (Article 15)

High-risk AI systems must achieve an appropriate level of accuracy, robustness, and cybersecurity. For law enforcement applications, the Act specifically requires resilience against attempts to alter use or performance through adversarial inputs. Social media monitoring data in particular is susceptible to manipulation (e.g., coordinated posting designed to falsely elevate or suppress risk scores for particular areas).

---

## 3. Deployer Obligations (Article 26)

Even if the provider (vendor) has fulfilled all its obligations, the municipality as **deployer** bears significant independent obligations under Article 26:

- **Use the system according to instructions**: Deploy only for the purposes and in the manner specified in the technical documentation. Any use beyond specified scope makes the municipality a co-provider with full provider obligations.
- **Conduct a Fundamental Rights Impact Assessment (FRIA)** before deployment: Article 27 requires deployers who are public bodies to conduct a FRIA prior to deploying a high-risk AI system, assessing the impact on fundamental rights listed in the EU Charter of Fundamental Rights.
- **Assign qualified persons for human oversight**: Article 26(5) requires that staff responsible for oversight have the necessary competence, training, and authority to fulfil their oversight role.
- **Monitor system performance in deployment**: Article 26(6) requires deployers to monitor system performance with reference to post-market monitoring and to report serious incidents to the provider and relevant national authority.
- **Data protection compliance**: Where personal data processing is involved, the deployer must comply with the GDPR concurrently with EU AI Act obligations. The municipality acts as data controller for all personal data processed by the system.

---

## 4. Fundamental Rights and Other Legal Risks

### 4.1 EU Charter of Fundamental Rights

Predictive policing tools implicate multiple Charter rights that must be addressed in the FRIA:

- **Article 7 (Respect for private and family life)**: Social media monitoring and location-based profiling affects the right to private life.
- **Article 8 (Protection of personal data)**: Processing of personal data must comply with data protection law and be collected for specified, explicit, and legitimate purposes (data minimisation and purpose limitation under GDPR).
- **Article 21 (Non-discrimination)**: Use of demographic data as a risk factor, or use of arrest data that encodes historical discrimination, constitutes indirect discrimination on grounds of race, ethnic origin, or other protected characteristics.
- **Article 47 (Right to an effective remedy and to a fair trial)**: Individuals targeted as a result of risk scores must have access to effective redress. If the scoring algorithm is opaque and outputs are not disclosed, individuals cannot effectively challenge enforcement actions taken against them.
- **Article 48 (Presumption of innocence)**: Attributing elevated crime risk to individuals or populations based on demographic characteristics or historical data violates the presumption of innocence at the systemic level.

### 4.2 GDPR Compliance

The social media monitoring and demographic data inputs present serious GDPR issues independent of the EU AI Act:

- **Lawful basis**: Law enforcement data processing is governed by the Law Enforcement Directive (LED, 2016/680) for competent authorities. The LED imposes strict necessity and proportionality requirements, and requires that personal data processing be strictly necessary for the stated law enforcement purpose.
- **Special category data**: If demographic data includes or correlates with racial or ethnic origin, processing is of special category data under Article 9 GDPR, requiring explicit legal authorisation.
- **Automated decision-making**: Article 22 GDPR restricts solely automated decision-making that produces legal or similarly significant effects on individuals. Even if framed as decision support, if enforcement actions are routinely triggered by score thresholds, Article 22 may apply.
- **Data minimisation and storage limitation**: Continuous social media monitoring is difficult to justify as data minimisation-compliant.

### 4.3 Feedback Loops and Self-Reinforcing Bias

A specific risk that regulators and courts have identified with crime-risk tools is the self-reinforcing feedback loop: the system scores certain areas as high-risk, police deploy more resources there, more arrests occur (including for low-level offences that would not be discovered without intensive presence), more data enters the training set, and the system's predictions for those areas become more entrenched. This mechanism means that even a technically accurate model (in the sense that its predictions correlate with observed arrest rates) may be systematically biased against certain communities in a way that constitutes discrimination and violates Article 10 data governance requirements.

---

## 5. The "Decision Support Tool" Defence

The EU AI Act explicitly anticipates and rejects marketing-framing-based approaches to avoiding classification. Several provisions are relevant:

1. **Article 6** classifies systems as high-risk based on their intended purpose as manifested by the context of deployment, not by labels applied by vendors.
2. **Recitals 57 and 58** of the Act address the risk that systems may be marketed in ways designed to circumvent classification, and indicate that supervisory authorities should look through such characterisations.
3. **Article 26(1)** makes clear that deployers are responsible for using systems in accordance with their instructions and for ensuring the systems are used for their intended purpose — if that purpose is high-risk, deployer obligations apply regardless of the "support" framing.
4. **The "human in the loop" exception** under Article 6(3) allows certain AI systems that assist human decision-making to escape the Annex III high-risk classification only if the human decision-making is genuinely substantive and the AI output is only one input among several with no systematic, substantial influence on the outcome. Given that crime risk scores in predictive policing directly determine resource allocation and enforcement priorities, this exception is extremely unlikely to apply.

---

## 6. Practical Legal Risks for the Municipality

### 6.1 Administrative Fines

The EU AI Act provides for significant fines for non-compliance:
- Violations of the prohibited practices provisions (Article 5): Up to €35 million or 7% of total annual worldwide turnover, whichever is higher
- Non-compliance with high-risk AI system requirements: Up to €15 million or 3% of global annual turnover
- Provision of incorrect or misleading information to authorities: Up to €7.5 million or 1.5% of global annual turnover

For a municipality, the 7% of turnover cap may not be directly applicable (as municipalities do not have commercial turnover in the standard sense), but national implementing legislation will specify equivalent sanctions for public bodies.

### 6.2 Suspension or Prohibition Orders

National market surveillance authorities (and, in law enforcement contexts, relevant national supervisory authorities) have the power to order withdrawal of the AI system from use, issue mandatory corrective measures, and restrict access to national markets. A municipality deploying a non-compliant system could face mandatory cessation of the tool mid-operation.

### 6.3 Individual Liability and Civil Claims

Individuals who are subjected to enforcement actions influenced by discriminatory risk scores may have claims under:
- The GDPR (Article 82 — right to compensation for data protection breaches)
- National administrative law (challenging enforcement decisions that relied on unlawful profiling)
- Anti-discrimination law (both EU framework directives and national implementing legislation)
- The EU Charter of Fundamental Rights (directly applicable against public authorities)

### 6.4 Political and Reputational Risk

Beyond legal liability, municipalities that deploy predictive policing tools that are later found to be discriminatory face significant political and reputational risk. Several European and US jurisdictions have prohibited or discontinued similar tools following public controversy and civil liberties investigations.

---

## 7. Recommended Steps Before Any Procurement

Given the extreme risk profile of this deployment, the following steps should be completed before any procurement or pilot:

1. **Legal opinion from qualified EU AI Act counsel**: Obtain a written legal opinion specifically addressing the applicability of Article 5 prohibitions to this specific tool given its data inputs and proposed use.

2. **Fundamental Rights Impact Assessment**: Commission and publish a FRIA under Article 27 before any deployment, engaging stakeholders including civil society organisations and community representatives from potentially affected neighbourhoods.

3. **Data Protection Impact Assessment (DPIA)**: Conduct a DPIA under Article 35 GDPR given the large-scale processing of sensitive data and the systematic surveillance character of the tool.

4. **Technical audit of training data**: Request and review the vendor's documentation of training datasets, including demographic breakdown of outcomes and statistical analysis of disparate impact across protected groups.

5. **Consultation with national data protection authority and AI supervisory authority**: Proactively engage relevant national authorities before deployment, particularly given the law enforcement context.

6. **Legal basis analysis under the Law Enforcement Directive**: Confirm that a clear and specific legal basis exists under national transposition of the LED for this specific form of processing.

7. **Procurement contract review**: Ensure the vendor contract assigns clear responsibilities for conformity, provides access to all required technical documentation, and includes audit rights, incident notification, and liability provisions consistent with EU AI Act deployer obligations.

---

## 8. Conclusion

The proposed predictive policing tool presents the following compliance picture under the EU AI Act:

| Issue | Assessment |
|---|---|
| Probable classification | High-risk AI system (Annex III, Point 6) at minimum |
| Risk of absolute prohibition | Significant — Articles 5(1)(d), (e), and (f) may apply |
| "Decision support" framing | Legally irrelevant to classification or obligations |
| FRIA required | Yes, mandatory for public body deployers |
| GDPR compliance | Serious concerns, particularly for special category data and automated profiling |
| Discriminatory feedback loops | Structural risk not addressable by technical fixes alone |
| Recommended action | Do not proceed without comprehensive legal review and impact assessments |

This deployment, as described, carries a high risk of violating the EU AI Act's prohibited practices provisions outright. Even if it clears that threshold, it faces a demanding compliance burden under the high-risk framework that historical arrest data, demographic data inputs, and social media surveillance are unlikely to satisfy. The municipality should approach this procurement with extreme caution and should not rely on the vendor's own characterisation of the tool's regulatory status.

---

*Analysis prepared 2 July 2026. Based on Regulation (EU) 2024/1689 (EU AI Act) and publicly available guidance. This analysis does not constitute legal advice. Specific deployment decisions should be reviewed by qualified legal counsel with expertise in EU AI Act compliance and law enforcement AI regulation.*
