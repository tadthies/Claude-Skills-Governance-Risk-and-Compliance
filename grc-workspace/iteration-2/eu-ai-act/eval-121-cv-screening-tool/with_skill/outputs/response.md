# EU AI Act Compliance Analysis: AI-Powered CV Screening and Candidate Ranking Tool

**Date:** 2 July 2026
**Scenario:** US SaaS company launching an AI CV screening and candidate ranking tool to European employers in Germany and France (Q1 next year)

---

## Executive Summary

Yes, your AI-powered CV screening and candidate ranking tool is squarely within scope of the EU AI Act (Regulation (EU) 2024/1689) and is classified as **high-risk**. As a US-based provider deploying to EU customers, you have significant compliance obligations that must be met before you can legally offer this system on the EU market. This analysis walks through your classification, obligations, key deadlines, and the conformity assessment path you must follow.

---

## 1. Territorial Scope: Does the EU AI Act Apply to a US Company?

Yes. The EU AI Act has explicit extraterritorial reach under **Article 2(1)(c)**. The Act applies to:

- **Providers** (vendors like your company) who place AI systems on the EU market or put them into service in the EU — regardless of where the provider is established.
- **Deployers** (your European employer customers) who use the system within the EU.

Since you are selling your CV screening tool to employers in Germany and France, you are placing an AI system on the EU market. You are therefore a **"provider"** under Article 3(3) of the Act and are subject to all provider obligations applicable to your system's risk classification.

---

## 2. High-Risk Classification Under Annex III, Area 4 (Art. 6(2))

### The Classification Rule

Under **Article 6(2)**, an AI system is classified as **high-risk** if it is listed in **Annex III** of the Act. Annex III enumerates specific areas where AI systems pose particular risks to fundamental rights, health, safety, or access to opportunities.

### Why Your Tool Is High-Risk

**Annex III, Area 4** explicitly covers AI systems used in:

> *"Employment, workers management and access to self-employment"*

Specifically listed within Area 4 are AI systems intended to be used for:

- **Recruitment or selection of natural persons** — in particular for advertising vacancies, screening or filtering applications, and evaluating candidates in the course of recruitment or selection processes;
- **Making decisions on promotion and termination** of work-related contractual relationships;
- **Allocating tasks based on individual behaviour** or personal traits or characteristics.

Your CV screening and candidate ranking tool:

- **Filters job applications** (screening/filtering) — explicitly listed
- **Ranks candidates based on skills and predicted fit** (evaluating candidates) — explicitly listed

There is no ambiguity here. Your system falls within **Annex III, Area 4** and is therefore a **high-risk AI system** under **Article 6(2)**. This classification applies regardless of the sophistication of the AI, its accuracy, or the employer's intent to have humans make final decisions.

### Why This Classification Matters

High-risk classification triggers a comprehensive set of mandatory obligations under **Articles 9 through 17** of the Act — obligations that apply to you as the provider, as well as obligations on your deployer-customers under **Article 26**. These are not soft guidelines; non-compliance can result in fines of up to **€30 million or 6% of global annual turnover**, whichever is higher (Article 99).

---

## 3. Key Provider Obligations (Arts. 9–17)

As the provider of a high-risk AI system, you must satisfy the following obligations before placing your system on the EU market. All obligations must remain in force throughout the system's lifecycle.

### 3.1 Risk Management System (Article 9)

You must establish, implement, document, and maintain a **risk management system** throughout the lifecycle of your CV screening tool. This is an ongoing, iterative process — not a one-time exercise.

Your risk management system must:

- Identify and analyse all **known and reasonably foreseeable risks** that the system may pose to health, safety, or fundamental rights. For a CV screening tool, these risks include discriminatory outcomes (e.g., disparate impact on protected groups such as women, ethnic minorities, or older candidates), opaque decision-making, and automated exclusion from employment opportunities.
- Estimate and evaluate the risks that may materialise based on intended use and reasonably foreseeable misuse.
- Adopt and implement **appropriate risk mitigation measures** — including testing, bias audits, and safeguards in the system design.
- Carry out **post-market monitoring** to detect risks that emerge after deployment (Article 72 requires a post-market monitoring plan).

For employment AI, this is particularly important given the **potential for algorithmic bias** that could disadvantage protected groups. Article 9(7) specifically requires testing for bias against groups protected under EU and national law, including gender, race/ethnicity, and age.

### 3.2 Data and Data Governance (Article 10)

Training, validation, and testing datasets for your CV screening tool must meet strict **data governance requirements**:

- Datasets must be **relevant, representative, and free of errors** to the extent possible.
- You must implement **data governance practices** covering data collection processes, data preparation operations, and examination of possible biases.
- You must examine datasets for possible **biases** that could lead to discriminatory outcomes — particularly where the system ranks or filters candidates. Historical hiring data, if used for training, may encode past discrimination.
- Data must cover the **specific geographical, behavioural, or functional settings** in which the system will be used. Since you are launching in Germany and France, your training data must adequately represent those labour markets.
- Relevant **personal data protections** must be satisfied in conjunction with GDPR, which runs in parallel to the AI Act for employment-related personal data.

### 3.3 Technical Documentation (Article 11 + Annex IV)

Before market placement, you must prepare comprehensive **technical documentation** demonstrating your system's compliance with the AI Act. This documentation must be kept up to date throughout the product lifecycle.

Annex IV prescribes the required contents, including:

- A general description of the AI system and its intended purpose
- A description of the system's components, design, development, and training process
- Details of the training, validation, and testing data and methodology
- Monitoring, functioning, and control measures
- Description of capabilities, limitations, accuracy levels, and known risks
- Pre-determined changes and their anticipated impact

This documentation must be made available to national competent authorities upon request.

### 3.4 Automatic Logging and Record-Keeping (Article 12)

Your CV screening system must be designed to **automatically log events** (technical logs) throughout its operation to the extent technically feasible. This includes:

- Each time the system is used (period of use)
- The reference database against which candidates were compared
- Input data that led to specific outputs
- Identity of natural persons involved in result verification

These logs enable post-hoc audits, investigations of bias or errors, and enforcement by regulators. Logs must be retained for a period appropriate to the system's purpose — in employment contexts, this typically aligns with the data retention requirements applicable under GDPR and national labour law (often 6 months to several years depending on jurisdiction).

### 3.5 Transparency and Information to Deployers (Article 13)

Your high-risk AI system must be **transparent to deployers** (your employer-customers). You must provide deployers with:

- Clear and comprehensible **instructions for use** (Annex V specifies the required contents)
- Information about the system's **intended purpose**
- The level of **accuracy, robustness, and cybersecurity** the system was designed to achieve
- Known or foreseeable risks and the circumstances under which the system's performance may be affected
- Details on **human oversight measures** and what decisions deployers should not allow the system to make autonomously

This information obligation is critical for supporting your customers' compliance with their own obligations under Article 26.

### 3.6 Human Oversight (Article 14)

High-risk AI systems must be designed and developed so that **natural persons can effectively oversee** their operation. For a CV screening tool, this means:

- The system must be designed to allow deployers (employers or their HR staff) to **understand, intervene, and override** decisions before they have effect.
- The tool must enable deployers to decide **not to use the AI output**, or to disregard, override, or reverse it.
- Deployers must be able to **interrupt the system** via a halt function if anomalies are detected.
- The system must not be capable of making **final, binding employment decisions** without human review. Automated rejection of candidates without any human oversight in the loop would be non-compliant — and potentially also a violation of GDPR's Article 22 prohibition on solely automated decisions that significantly affect individuals.

Practically, this means your product design must build in mandatory human review steps, override capabilities, and flagging of low-confidence outputs. Marketing materials claiming the system "automatically shortlists" candidates with no human step would be problematic.

### 3.7 Accuracy, Robustness, and Cybersecurity (Article 15)

Your system must achieve an appropriate **level of accuracy, robustness, and cybersecurity** for its intended purpose throughout its lifecycle. Specifically:

- You must declare and document the **accuracy levels** the system was tested to achieve, using metrics appropriate to the task (e.g., precision, recall, false negative rate broken down by demographic group).
- The system must be **resilient against errors, faults, and inconsistencies** in input data.
- Technical measures must be in place to protect against adversarial inputs or attempts to manipulate outcomes.

### 3.8 Quality Management System (Article 17)

You must establish a **Quality Management System (QMS)** that documents and governs your compliance approach. The QMS must cover:

- A strategy for regulatory compliance, including conformity assessments
- Design and development procedures including data examination and testing protocols
- Post-market monitoring obligations
- Internal reporting, incident management, and correction procedures
- Record-keeping of documentation and communications with authorities
- Resource management and responsibility assignment

The QMS must be proportionate to the size of your company but must demonstrably cover all required elements. For a US SaaS company, this is typically embedded in your existing engineering and compliance processes, but must be formalized and documented for EU AI Act compliance.

---

## 4. Compliance Deadline: 2 December 2027

### The Deadline That Applies to Your System

The EU AI Act entered into force on 1 August 2024. Compliance obligations apply on a phased timeline:

| Obligation | Deadline |
|---|---|
| GPAI model obligations (Art. 53+) | 2 August 2025 (in force) |
| Art. 50 transparency obligations (deepfakes, chatbots) | 2 August 2026 |
| **Annex III standalone high-risk systems** | **2 December 2027** |
| Annex I embedded product high-risk systems | 2 August 2028 |

Your CV screening tool is an **Annex III standalone AI system** (it is not embedded as a safety component of a product regulated by other EU harmonisation legislation listed in Annex I). The applicable compliance deadline is therefore **2 December 2027**.

### Important: Digital Omnibus Extension

The original EU AI Act set 2 August 2026 as the deadline for Annex III standalone systems. However, the **Digital Omnibus regulation, adopted on 29 June 2026**, extended this deadline by approximately 16 months to **2 December 2027**.

This extension was adopted to give providers more time to adapt, particularly SMEs and companies based outside the EU. Given that the Digital Omnibus has now been adopted, your effective compliance deadline is **2 December 2027**.

### What This Means for Your Q1 Launch

You are planning to launch in Germany and France in Q1 of next year (Q1 2027). This launch falls **before** the 2 December 2027 compliance deadline.

You have two options:

1. **Launch early with a compliance roadmap in place**: You may launch before 2 December 2027 provided you are actively working toward full compliance by the deadline. However, you must be careful — launching a non-compliant high-risk AI system even before the deadline does not immunize you from enforcement if national authorities begin exercising jurisdiction.

2. **Full compliance before launch**: The safest path is to complete your conformity assessment and documentation requirements before your Q1 launch, particularly if you intend to scale across the EU beyond Germany and France.

Given that you are targeting Germany and France specifically, note that both countries have active AI and data protection regulators (the BNetzA/national AI authority in Germany and the CNIL/national AI authority in France) who may begin enforcement activity as the 2027 deadline approaches.

**Recommendation**: Treat 2 December 2027 as the hard outer limit, but aim to complete core compliance steps (risk management system, technical documentation, data governance, and conformity assessment) before your Q1 2027 launch. This protects you from reputational and regulatory risk and demonstrates good faith to your EU employer customers who have their own Art. 26 obligations.

---

## 5. Conformity Assessment: Self-Assessment Under Annex VI

### Which Conformity Assessment Path Applies?

The EU AI Act offers two conformity assessment routes for high-risk AI systems:

1. **Notified body (third-party) assessment** — mandatory only for systems in **Annex III, Point 1** (biometric identification, emotion recognition in critical contexts, etc.)
2. **Internal/self-assessment (Annex VI)** — available for all other Annex III systems, including **Points 2–8**

Your CV screening tool falls under **Annex III, Area 4** (Point 4 in the Annex III enumeration, covering employment). This is within **Points 2–8** of Annex III. Therefore, you may conduct a **self-assessment** using the procedure set out in **Annex VI** — no notified body (external auditor) is required, unless you voluntarily choose one.

### What Annex VI Self-Assessment Involves

The Annex VI conformity assessment procedure requires you to:

1. **Verify conformity** of your system with the requirements in Articles 9–15 (the obligations described above)
2. **Draw up** the technical documentation described in Annex IV
3. **Ensure** the quality management system in Article 17 is implemented
4. **Conduct** testing to verify that the system performs as intended and meets accuracy, robustness, and non-discrimination requirements

The self-assessment must be **documented** and must be completed **before** placing the system on the EU market.

Note: Even though you conduct the assessment yourself, it must be rigorous and defensible. National market surveillance authorities may audit your conformity assessment and technical documentation at any time. The documentation must show genuine, evidence-based testing and risk evaluation — not merely checkbox exercises.

---

## 6. CE Marking (Article 48)

Following a successful conformity assessment, you must **affix the CE marking** to your high-risk AI system before placing it on the EU market. For software products, this is typically achieved through:

- Including the CE marking in product documentation, user interfaces, and marketing materials
- The CE marking signals to deployers, users, and authorities that the system has undergone conformity assessment and meets EU AI Act requirements

The CE marking rules are governed by **Article 48** and by the relevant provisions of EU harmonisation legislation applicable to physical products. For pure software systems like a SaaS CV screening tool, the CE marking is affixed to the documentation and product interface rather than a physical label.

**Important**: Affixing CE marking on a non-compliant system is itself an offence under Article 99 of the Act. Do not mark your system until the conformity assessment is genuinely complete.

---

## 7. EU Declaration of Conformity (Article 47)

Alongside CE marking, you must draw up an **EU Declaration of Conformity** under **Article 47**. This is a formal written declaration in which you, as the provider, confirm that the high-risk AI system complies with the requirements of the EU AI Act.

The Declaration of Conformity must:

- Be drawn up in one of the official EU languages (or translated as required)
- Identify the AI system, its version, and its intended purpose
- State that the system conforms to the applicable provisions of the EU AI Act
- Identify the conformity assessment procedure followed (Annex VI)
- Carry the name, registered address, and signature of an authorized representative

**You must keep the Declaration of Conformity for 10 years** after the system is placed on the market (Article 47(4)). This 10-year retention period begins on the date of market placement.

---

## 8. EU AI Database Registration (Article 49)

Before placing your high-risk AI system on the EU market, you must **register it in the EU AI database** maintained by the European Commission under **Article 71**. The registration obligation for providers of standalone Annex III systems is set out in **Article 49**.

Registration requires you to submit:

- Your company name, address, and contact information
- The name, version, and description of the AI system
- The system's intended purpose and the specific area of Annex III under which it is classified
- A summary of the conformity assessment procedure followed
- A reference to the EU Declaration of Conformity
- Information on the post-market monitoring plan

The EU AI database is publicly accessible, providing transparency to the public, researchers, and regulatory authorities about which high-risk AI systems are on the EU market.

**Note for US companies**: You will need an EU-based authorized representative to manage regulatory communications and, where required, registration on your behalf. Article 22 of the AI Act (read alongside Product Safety and market surveillance rules) requires non-EU providers to designate an **EU representative** before market access. This representative can be a law firm, consulting firm, or any legal entity established in the EU.

---

## 9. Deployer Obligations (Article 26) — Your Customers' Responsibilities

While you as the provider bear the primary obligations described above, your EU employer-customers are **deployers** under the Act and have their own obligations under **Article 26**. Understanding these is important for your commercial relationships and contract drafting.

Key deployer obligations include:

- Implementing the **instructions for use** you provide
- Ensuring **human oversight** of the system's outputs by assigning oversight tasks to appropriately trained staff
- **Monitoring** the system's operation and reporting serious incidents or malfunctions to you (the provider) and to national authorities
- If they substantially modify the system, they may themselves become a provider with the full provider obligations
- **Public authorities** acting as deployers must also register their use in the EU AI database under Article 60

In your customer contracts (Data Processing Agreements, Terms of Service, and License Agreements), you should:

- Clearly allocate responsibilities between you (provider) and the employer (deployer)
- Require employers to use the system only for its intended purpose
- Require employers to implement human oversight measures and not make solely automated employment decisions
- Give employers adequate instructions for use meeting the Annex V requirements
- Establish a mechanism for employers to report malfunctions and anomalies to you

---

## 10. Interaction with GDPR

The EU AI Act explicitly operates alongside GDPR — it does not replace or supersede it. For a CV screening tool processing candidate personal data in Germany and France, both regimes apply simultaneously.

Key intersection points:

- **GDPR Article 22** prohibits solely automated decisions that produce legal or similarly significant effects on individuals — employment decisions fall squarely within this. Your employers must ensure human review before any rejection decision based on your system's output.
- **GDPR Article 13/14**: Candidates must be informed that their data is being processed by an AI system, including information about the logic involved and the consequences of that processing.
- **GDPR Article 9**: If your system processes special category data (e.g., inferred disability, ethnicity) you will need explicit consent or another Article 9(2) legal basis.
- **Data minimisation**: Your system should process only the personal data strictly necessary for the stated purpose.

Aligning your AI Act technical documentation and data governance practices with your GDPR Records of Processing Activities (RoPA) and Data Protection Impact Assessment (DPIA) will reduce duplication and demonstrate holistic compliance to both AI and data protection authorities.

---

## 11. Action Plan and Recommended Next Steps

Given your planned Q1 2027 launch, here is a prioritised action plan:

### Immediate (Now – 3 months)
1. **Engage EU legal counsel** and designate an EU authorized representative
2. **Initiate a gap analysis** against Articles 9–17 and identify remediation work needed
3. **Commission a bias and fairness audit** of your training data and model outputs, with demographic breakdowns
4. **Begin drafting technical documentation** per Annex IV

### Short-Term (3–6 months, pre-launch)
5. **Implement the risk management system** (Article 9) with documented processes
6. **Establish data governance policies** meeting Article 10 requirements
7. **Design and implement human oversight features** in the product UI (override controls, flagging, audit trails)
8. **Implement automatic logging** per Article 12
9. **Draft Instructions for Use** for employer-deployers (Annex V)
10. **Establish your QMS** (Article 17)

### Pre-Launch
11. **Complete the Annex VI self-assessment** and document results thoroughly
12. **Draw up the EU Declaration of Conformity** (Article 47)
13. **Affix CE marking** (Article 48)
14. **Register in the EU AI database** (Article 49)
15. **Update customer contracts** to address Art. 26 deployer obligations

### Ongoing (Post-Launch through 2 December 2027 and beyond)
16. **Monitor system performance** for accuracy and bias drift
17. **Maintain and update technical documentation** with each new version
18. **Report serious incidents** to national authorities as required by Article 73
19. **Conduct periodic audits** of your risk management system

---

## Summary Table

| Topic | Answer |
|---|---|
| Does EU AI Act apply? | Yes — extraterritorial scope covers US providers placing AI on EU market (Art. 2(1)(c)) |
| Risk classification | High-risk under Art. 6(2) via Annex III, Area 4 (recruitment / candidate selection) |
| Conformity assessment path | Self-assessment (Annex VI) — no notified body required for Annex III Points 2–8 |
| Compliance deadline | **2 December 2027** (extended from 2 August 2026 by Digital Omnibus, adopted 29 June 2026) |
| CE marking | Required before market placement (Art. 48) |
| Declaration of Conformity | Required; retain for 10 years (Art. 47) |
| EU AI database registration | Required for providers before market placement (Art. 49) |
| EU representative | Required for non-EU providers |
| Key obligations | Risk management (Art. 9), data governance (Art. 10), technical docs (Art. 11), logging (Art. 12), transparency (Art. 13), human oversight (Art. 14), accuracy/robustness (Art. 15), QMS (Art. 17) |
| Deployer obligations | Employer-customers must comply with Art. 26 — address in contracts |

---

*This analysis reflects the EU AI Act (Regulation (EU) 2024/1689) as amended by the Digital Omnibus regulation adopted 29 June 2026. It is provided for compliance planning purposes. You should obtain formal legal advice from EU-qualified counsel before market entry.*
