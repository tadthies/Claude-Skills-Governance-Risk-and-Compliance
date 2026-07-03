# EU AI Act Compliance Analysis: Predictive Policing Tool for Municipal Deployment

## Executive Summary

The proposed predictive policing AI system — which scores neighbourhoods by crime risk using historical arrest data, social media monitoring, and demographic data — raises **critical legal concerns under EU AI Act Regulation (EU) 2024/1689**. The system is almost certainly prohibited outright under Article 5, and even if it were not, it would face the most demanding tier of regulatory obligations as a high-risk system under Annex III. The vendor's characterisation of the tool as a "decision support tool" does not affect this legal analysis. This deployment should not proceed without a fundamental legal reassessment and, in all likelihood, should not proceed at all in its current form.

---

## 1. Article 5(1)(d): Prohibited AI Practice — Predictive Criminal Risk Profiling

### The Prohibition

Article 5(1)(d) of the EU AI Act prohibits AI systems that make **risk assessments of natural persons** to predict the likelihood of a person offending or reoffending or assess personality traits of natural persons, where such assessments are based solely or predominantly on **profiling** or **personality traits**. This prohibition is absolute — it admits no exemptions for law enforcement needs, public interest, or proportionality balancing.

### Application to This System

Although the system is framed as scoring *neighbourhoods* rather than individuals, this distinction provides no meaningful legal insulation for several reasons:

**Demographic data as individual-level profiling by aggregation.** The use of demographic data as a predictive input means the system is, in substance, assigning risk based on the characteristics of people who *live in* or *move through* an area. When a neighbourhood's "crime risk" score is driven by the demographic composition of its residents, the system is effectively profiling individuals based on group membership — precisely the kind of reasoning that Article 5(1)(d) targets. EU regulators and the Commission's published guidelines (4 February 2025) make clear that prohibited profiling cannot be circumvented by using group-level proxies for individual characteristics.

**Historical arrest data as a biased proxy.** Arrest data does not measure criminality; it measures prior law enforcement activity, which is itself shaped by historical policing decisions. Using arrest data as a training signal incorporates and amplifies prior enforcement bias. The system learns to predict where police *have been*, not where crime *occurs*, and the predictive signal is inextricably tied to the demographic and social profiles of those previously arrested. This is profiling based on prior law enforcement contact, not on evidence of future criminal behaviour.

**Social media monitoring.** Social media monitoring of residents in target neighbourhoods constitutes surveillance of individuals and analysis of their expressed views, associations, and behaviour — classic profiling inputs. Where this data is used to assess the likelihood of criminal activity in an area, it crosses directly into the territory of Article 5(1)(d).

**The "solely or predominantly" threshold.** Even if the system incorporates some non-profiling inputs (e.g., time-of-day patterns or geographical infrastructure data), the use of demographic data and social media monitoring means profiling is at minimum a *predominant* factor in the risk score. The prohibition applies.

### Likely Conclusion

In the assessment of this advisor, the described system falls squarely within the Article 5(1)(d) prohibition. Deployment would constitute a **breach of an absolute prohibition** under EU law.

---

## 2. Article 5(1)(c): Social Scoring Risk — Neighbourhood Scoring Component

### The Prohibition

Article 5(1)(c) prohibits AI systems used by or on behalf of **public authorities** to evaluate or classify natural persons based on their **social behaviour** or **personal characteristics**, where those classifications lead to detrimental treatment of those persons that is either unrelated to the context in which the data was generated, or disproportionate to the social behaviour or its gravity.

### Application to This System

The municipality is a public authority. The scoring of neighbourhoods based on social media monitoring and demographic data is, in substance, a classification of *the people who live there* based on their social behaviour and personal characteristics. The downstream effect of the system — increased police presence, surveillance, and enforcement attention directed at high-scoring areas — constitutes detrimental treatment of residents based on where they live and who they are.

Several factors make this analysis particularly acute:

- Residents of high-scored neighbourhoods did not generate their social media data in a law enforcement context. Using it to direct policing against them is exactly the "use unrelated to the context in which data was generated" that Article 5(1)(c) targets.
- Demographic data has no legitimate place in a crime risk prediction algorithm. Its inclusion confirms that the system classifies people based on personal characteristics, not on individually observable behaviour.
- The system is initiated by a municipality, making the "public authority" element straightforward.

The neighbourhood framing does not escape this prohibition. The Commission's February 2025 guidelines on Article 5 prohibited practices confirm that systemic area-based scoring that functions to classify and disadvantage residents falls within the social scoring prohibition when operated by public authorities.

### Likely Conclusion

The neighbourhood scoring component, as described, faces a **credible and substantial risk of constituting prohibited social scoring** under Article 5(1)(c), in addition to the Article 5(1)(d) concern above.

---

## 3. The "Decision Support Tool" Framing Does Not Exempt the System

The vendor's characterisation of this product as a "decision support tool" is legally irrelevant to classification under the EU AI Act. This is a well-established principle confirmed by the Commission's guidelines and the text of the Act itself.

**Why the framing does not matter:**

- The EU AI Act classifies AI systems based on their **purpose, inputs, and outputs** — not on how the vendor labels or markets the product. Article 3 defines an AI system as a machine-based system designed to generate outputs such as predictions, recommendations, or decisions that influence real or virtual environments. The described system clearly meets this definition.
- Article 5 prohibitions apply based on what the system *does*, not what a vendor *calls* it. A prohibited AI system does not become permitted by adding a human in the loop who reviews the output, or by describing the AI output as merely "informing" a human decision.
- The Commission's February 2025 guidelines on prohibited practices explicitly address the "decision support" workaround: they confirm that systems which generate risk scores, predictions, or classifications that are fed into human decision-making processes remain subject to prohibition and classification rules. The human review layer does not launder the AI system's prohibited function.
- Recital 12 of the Act and the accompanying guidance note that even where AI output requires human confirmation before action is taken, the AI system itself is subject to the full rigour of the Act's classification framework.

**Practical implication:** If a human officer looks at a neighbourhood risk score before deciding to increase patrols, the AI system that generated that score is still the subject of regulatory analysis. The human decision layer neither changes the system's classification nor provides a compliance safe harbour.

---

## 4. Article 5 Prohibitions Apply from 2 February 2025

The EU AI Act's prohibition provisions in Article 5 entered into force and became applicable on **2 February 2025** — six months after the Act's publication, and well ahead of the broader high-risk system compliance deadline. This is not a future obligation; it is current law.

**Key implication for the municipality:** Any deployment of a system that falls within Article 5 after 2 February 2025 constitutes an **active and ongoing breach** of the EU AI Act. There is no grace period, transition window, or derogation available for prohibited practices. The municipality cannot argue it is still preparing for compliance — the prohibition is already fully in effect.

**Liability exposure:** The AI Act's enforcement regime assigns liability not only to providers (vendors) but also to **deployers** — the organisations that put AI systems into use. The municipality, as deployer, shares legal exposure for any prohibited deployment. Fines for breaching Article 5 prohibitions are set at up to **€35 million or 7% of worldwide annual turnover**, whichever is higher (Article 99(1)). Member State supervisory authorities are already operationally active, and the European AI Office has signalled enforcement priority on prohibited practices.

---

## 5. Even If Not Prohibited, the System Is High-Risk Under Annex III Area 6

If — contrary to the analysis above — a modified version of this system were found not to breach Article 5, it would still face classification as a **high-risk AI system** under Annex III, specifically Area 6: *AI systems intended to be used by law enforcement authorities for making individual risk assessments of natural persons in order to assess the risk of a natural person for offending or reoffending or the risk for potential victims of criminal offences*.

### Full Conformity Obligations Under Articles 8–26

High-risk classification triggers the most demanding compliance framework in the Act, with obligations that apply to both the vendor (provider) and the municipality (deployer). These obligations include:

**Risk management system (Art. 9):** A documented risk management system must be established, implemented, and maintained throughout the AI system lifecycle, identifying and mitigating foreseeable risks including risks of harm to fundamental rights.

**Data and data governance (Art. 10):** Training, validation, and testing datasets must meet strict requirements of relevance, representativeness, and freedom from errors — a standard that historical arrest data, which reflects prior enforcement bias, is unlikely to meet without substantial remediation. The use of demographic data as a predictive variable will face acute scrutiny under this article.

**Technical documentation (Art. 11):** Comprehensive technical documentation must be prepared before placing the system on the market or putting it into service, covering design choices, training methodology, performance metrics, and known limitations.

**Record-keeping and logging (Art. 12):** The system must maintain automatic logs of operation to ensure traceability of decisions and enable post-hoc review of outputs. This obligation is particularly demanding for systems used in law enforcement contexts.

**Transparency and provision of information to deployers (Art. 13):** The system must be designed to operate with an appropriate level of transparency, and providers must supply deployers with clear information about the system's purpose, capabilities, limitations, and conditions of use.

**Human oversight (Art. 14):** High-risk AI systems must be designed to allow effective human oversight. This means implementing mechanisms for human review and override — not simply having a human nominally in the loop, but ensuring that the human can meaningfully understand and challenge the system's output.

**Accuracy, robustness, and cybersecurity (Art. 15):** The system must demonstrate appropriate levels of accuracy, and performance metrics must be disclosed. For a system operating in a law enforcement context, the consequences of false positives — directing enforcement attention at individuals and communities who pose no actual risk — are severe.

**Conformity assessment (Art. 43):** High-risk systems in Annex III Area 6 require a conformity assessment before deployment. For most Annex III systems this can be done as an internal assessment under Annex VI, but it requires documentary evidence and must be completed prior to deployment.

**Registration in the EU AI Act database (Art. 71):** High-risk AI systems must be registered in the publicly accessible EU database maintained by the Commission before deployment.

**Compliance deadline:** For Annex III standalone systems, full compliance obligations apply from **2 December 2027**, but given that Article 5 prohibitions already apply, this deadline is relevant only as a secondary line of analysis for a substantially redesigned system that escapes prohibition.

---

## 6. Additional Legal Intersections

### GDPR and Law Enforcement Directive

The processing of personal data — including social media data, demographic data, and data derived from historical arrests — for law enforcement risk assessment purposes engages **Regulation (EU) 2016/679 (GDPR)** and **Directive (EU) 2016/680** (the Law Enforcement Directive). The use of special category data (which demographic data often implies when used as a proxy for ethnicity or religion) requires explicit legal basis under Articles 9–10 GDPR, which is unlikely to be satisfied for this use case. The municipality's Data Protection Officer must be consulted before any procurement decision.

### Fundamental Rights Impact

The use of AI-generated risk scores in a policing context engages Charter of Fundamental Rights obligations, including the right to non-discrimination (Art. 21), the right to privacy (Art. 7), the right to data protection (Art. 8), and the presumption of innocence (Art. 48). A Fundamental Rights Impact Assessment is a legal and practical necessity before any further steps are taken, and its outcome will almost certainly be negative for a system of this design.

---

## 7. Recommended Actions for the Municipality

1. **Do not proceed with deployment** of the system as described. The legal risks under Article 5 are not manageable risks to be mitigated — they are absolute prohibitions on the system's core function.

2. **Instruct legal counsel** to conduct a full Article 5 prohibited practices analysis before any further procurement steps, including any pilot or proof-of-concept deployment. The prohibition applies to operational use in any form.

3. **Reject the "decision support" framing** in vendor discussions and contracts. Ensure that the municipality's legal team evaluates the system based on what it does, not how the vendor markets it.

4. **If a redesigned system is considered**, ensure it is assessed against Annex III Area 6 high-risk criteria from the outset, with a clear roadmap to full Articles 8–26 conformity and registration in the EU AI Act database by 2 December 2027.

5. **Engage your supervisory authority** for preliminary guidance on any alternative approach before committing to procurement.

6. **Commission a Fundamental Rights Impact Assessment** and DPIA covering the full scope of personal data processing involved.

---

## Summary Table

| Issue | Provision | Status | Applies Since |
|---|---|---|---|
| Predictive criminal risk based on profiling | Art. 5(1)(d) | Likely prohibited | 2 February 2025 |
| Social scoring by public authority | Art. 5(1)(c) | Substantial risk of prohibition | 2 February 2025 |
| "Decision support" framing as exemption | N/A | Not a valid exemption | N/A |
| High-risk classification (if not prohibited) | Annex III Area 6 | High-risk; full Arts. 8–26 obligations | Compliance by 2 Dec 2027 |
| Maximum fine for Art. 5 breach | Art. 99(1) | Up to €35M or 7% global turnover | Active now |

---

*This analysis is provided as expert compliance guidance based on Regulation (EU) 2024/1689 (EU AI Act) and the Digital Omnibus (adopted 29 June 2026), including Commission guidelines on Article 5 prohibited practices published 4 February 2025. It does not constitute legal advice and does not create a legal adviser–client relationship. The municipality should obtain formal legal advice before making any procurement or deployment decision.*
