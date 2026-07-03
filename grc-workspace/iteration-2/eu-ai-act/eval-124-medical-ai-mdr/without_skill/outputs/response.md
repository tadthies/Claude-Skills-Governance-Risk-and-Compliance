# EU AI Act Compliance Analysis: AI Diagnostic Imaging Tool with CE Marking Under EU MDR

## Executive Summary

Your hospital faces a nuanced but critically important regulatory situation. The CE marking obtained under the EU Medical Device Regulation (MDR, Regulation 2017/745) does **not** automatically satisfy EU AI Act requirements. Your AI diagnostic imaging tool is almost certainly classified as a **high-risk AI system** under the EU AI Act, and while there is a partial "deemed compliance" mechanism for medical devices, significant additional obligations apply — particularly for you as the **deployer** of the system.

---

## 1. Classification of the AI System Under the EU AI Act

### 1.1 High-Risk Classification

Under the EU AI Act (Regulation (EU) 2024/1689), AI systems intended to be used as safety components of medical devices, or which are themselves medical devices regulated under EU MDR, are explicitly listed as **high-risk AI systems** in **Annex I, Section 5** of the Act:

> "AI systems intended to be used as safety components in the management and operation of critical infrastructure... AI systems intended to be used as safety components of products, or which are themselves products, covered by Union harmonisation legislation listed in Annex II..."

Annex II of the EU AI Act specifically lists EU MDR (Regulation 2017/745) among the harmonisation legislation whose products, when using AI as a safety component, trigger the high-risk classification.

Because your vendor has explicitly stated this tool functions as a **safety component** for your radiology department, and because it holds CE marking under EU MDR Class IIa, **both criteria are satisfied simultaneously**:
- It is an AI system used as a safety component of an MDR-covered product; AND
- It is itself a Class IIa medical device under EU MDR

This places the system squarely in the **high-risk AI system** category under Article 6 and Annex I of the EU AI Act.

### 1.2 Prohibited Practices

Before proceeding, confirm the system does not use any techniques that would render it prohibited under Article 5 of the EU AI Act, such as subliminal manipulation or exploitation of vulnerabilities. For a diagnostic imaging tool, this is unlikely but worth a formal check.

---

## 2. The MDR/EU AI Act Relationship: "Deemed Compliance" and Its Limits

### 2.1 The Partial Alignment Mechanism

The EU AI Act contains a specific provision in **Article 9** and related recitals for medical devices already subject to EU MDR conformity assessment. Under **Article 9(2)**, where products are already covered by Union harmonisation legislation in Annex II, the conformity assessment obligations under Chapter III, Section 2 of the AI Act (Articles 43–44) may be fulfilled through the existing MDR conformity assessment procedure — but only for requirements that the MDR procedure already addresses.

More specifically, the EU AI Act establishes a **single conformity assessment** approach for products that are both AI systems and medical devices: the manufacturer conducts one integrated assessment rather than two entirely separate processes.

### 2.2 What MDR CE Marking Does Cover

MDR Class IIa conformity assessment (typically via a Notified Body) addresses:
- Safety and performance of the device
- Clinical evaluation and evidence of effectiveness
- Quality management systems (EN ISO 13485)
- Post-market surveillance
- Technical documentation

These overlap with some EU AI Act requirements for high-risk systems, particularly around:
- Risk management (Article 9 of the AI Act)
- Technical documentation (Article 11)
- Post-market monitoring (Article 72)
- Logging and record-keeping

### 2.3 Critical Gap: What MDR CE Marking Does NOT Cover

The MDR conformity assessment was designed before the EU AI Act existed and does **not** address AI-specific requirements, including:

1. **Data Governance (Article 10)**: Requirements for training, validation, and testing datasets — including bias assessment, data quality, representativeness across demographic groups, and dataset relevance to the intended use in EU patient populations.

2. **Transparency and Instructions for Use for Deployers (Article 13)**: AI Act-specific transparency obligations require that deployers like your hospital receive specific information enabling them to properly oversee and interpret the AI system's outputs.

3. **Human Oversight Mechanisms (Article 14)**: The AI Act mandates that high-risk AI systems be designed with built-in mechanisms enabling humans to oversee, intervene, override, or disable the system. MDR does not impose equivalent AI-specific oversight requirements.

4. **Accuracy, Robustness, and Cybersecurity (Article 15)**: While MDR addresses safety and performance, the AI Act's specific standards for AI accuracy (including metrics across different conditions), resilience against adversarial inputs, and AI-specific cybersecurity requirements go beyond MDR.

5. **Conformity Declaration Under the AI Act (Article 47)**: A separate EU Declaration of Conformity referencing the AI Act must be issued and registered.

6. **EU Database Registration (Article 49 and Annex VIII)**: High-risk AI systems must be registered in the EU AI Act database at eu.ai.act (the EUDAMED equivalent for AI), distinct from EUDAMED registration under MDR.

**Bottom line**: The CE marking under MDR provides a partial foundation and may streamline some elements of AI Act compliance, but it does not serve as a blanket substitution.

---

## 3. Obligations Under the EU AI Act: Provider vs. Deployer

The EU AI Act assigns obligations to two distinct parties: the **provider** (the vendor who developed and placed the system on the market) and the **deployer** (your hospital, which uses the system in a professional context). Both have distinct obligations.

### 3.1 Provider Obligations (Primarily the Vendor's Responsibility)

The AI diagnostic imaging vendor, as the **provider** under Article 3(3), is responsible for:

- Establishing and maintaining a **quality management system** (Article 17) covering the full AI lifecycle
- Preparing and maintaining **technical documentation** (Article 11 and Annex IV) specifically addressing AI system architecture, training data, validation results, and performance metrics
- Conducting a **conformity assessment** under Article 43 (with Notified Body involvement for Class IIa, which already applies under MDR)
- Issuing the **EU Declaration of Conformity** under the AI Act (Article 47)
- Affixing the **CE marking** specifically citing AI Act compliance (this is in addition to the MDR CE mark)
- **Registering** the system in the EU AI Act database (Article 49)
- Implementing **post-market monitoring** (Article 72) with AI-specific performance tracking
- Reporting **serious incidents** to the relevant national competent authority under Article 73
- Implementing **automatic logging** capabilities (Article 12) to enable incident investigation

### 3.2 Deployer Obligations: Your Hospital's Responsibilities

This is the section most critical for your hospital's immediate action. As a **deployer** of a high-risk AI system under Article 26, your hospital must:

#### a) Use the System as Instructed (Article 26(1))
You must use the AI system only in accordance with the provider's instructions for use. Any use outside the intended purpose — including applying it to patient populations, imaging modalities, or clinical conditions not validated in the system — may violate both the EU AI Act and MDR.

#### b) Human Oversight (Article 26(2) and Article 14)
You must assign qualified individuals to perform oversight of the AI system's operation. For a diagnostic imaging tool, this means radiologists or other qualified clinicians must:
- Review AI outputs before clinical decisions are made
- Be able to override or disregard the AI's recommendations
- Understand the system's limitations and error modes
- Not treat the AI output as a definitive diagnosis without independent clinical judgment

**Practical implication**: Establish and document a clinical workflow where AI-assisted diagnoses are always reviewed and confirmed by a qualified radiologist before being acted upon.

#### c) Monitoring (Article 26(5))
Deployers must **monitor the operation** of the AI system on the basis of the instructions for use and report any serious incidents or malfunctions to the provider and, where required, to the national competent authority.

#### d) Data Protection Impact Assessment (Article 26(9))
Where processing involves personal data (which diagnostic imaging always does), you may need to conduct a **Data Protection Impact Assessment (DPIA)** under GDPR in conjunction with your AI Act obligations — particularly given the sensitivity of health data (special category data under GDPR Article 9).

#### e) Record-Keeping (Article 26(6) and Article 12)
You must keep **logs** of the AI system's operation to the extent you have control over them. For a diagnostic imaging tool, this means retaining records of:
- Which images were processed by the AI
- What outputs the AI produced
- What clinical decision was made in relation to that output
- Which clinician reviewed and acted on the AI output

Retention periods should align with medical record requirements under MDR, GDPR, and applicable national health law — but must be at minimum **6 months** post-deployment for the AI-specific logs (longer for medical records).

#### f) Transparency to Patients (Article 50(1) and Recital 134)
Where the AI system interacts with or produces outputs that affect patients, deployers must inform patients that they are subject to an AI-assisted diagnostic process. This obligation is nuanced — it does not require disclosing commercially sensitive implementation details, but patients have a right to know that AI is involved in their care.

**Practical implication**: Update patient consent forms, privacy notices, and information leaflets to disclose AI use in diagnostic imaging.

#### g) Fundamental Rights Impact Assessment (Article 27)
**Bodies governed by public law** (which many hospitals are) and **private entities providing public services** must conduct a **Fundamental Rights Impact Assessment (FRIA)** before deploying high-risk AI systems. This assessment must evaluate:
- The purpose of the AI system and its geographic and temporal scope
- The categories of persons affected (patients, staff)
- The specific fundamental rights at risk (right to health, non-discrimination, data protection)
- The severity of impact and likelihood of harm
- Measures to mitigate identified risks

If your hospital is publicly funded or provides services under public mandate, this FRIA is **mandatory** and must be notified to the relevant national market surveillance authority.

---

## 4. Specific Considerations for AI Diagnostic Imaging

### 4.1 Bias and Fairness in Training Data

AI diagnostic imaging tools are known to exhibit performance disparities across patient demographics — particularly across age groups, biological sex, skin tone (where relevant), and ethnicity. Article 10 of the EU AI Act requires that training datasets be "relevant, representative, free of errors and complete" with due regard to characteristics of the specific geographic setting.

Your hospital should request from the vendor:
- Documentation of the training dataset composition
- Validation performance metrics stratified by relevant demographic groups
- Any known performance limitations or contraindications by patient population

If the system was validated on datasets not representative of your patient population, you may need to conduct additional local validation before full deployment.

### 4.2 Integration with EUDAMED and AI Act Registration

The system should already be registered in **EUDAMED** (European Database on Medical Devices) under MDR. Under the EU AI Act, it must additionally be registered in the **EU AI Act database** maintained by the European AI Office. Verify with your vendor that this registration is complete or in progress.

### 4.3 Notified Body Role

For Class IIa medical devices under MDR, a Notified Body conducts conformity assessment. Under the EU AI Act, for products already subject to Notified Body review under the legislation listed in Annex II, **the same Notified Body** is expected to verify AI Act compliance as part of the integrated assessment (where technically feasible). Confirm with your vendor that their Notified Body has reviewed the AI-specific requirements of the EU AI Act, not just the MDR requirements.

---

## 5. Timeline and Transitional Provisions

### 5.1 Entry into Force

The EU AI Act entered into force on **1 August 2024**, with provisions applying in phases:
- **August 2024**: Prohibited AI practices (Chapter II) — immediately applicable
- **August 2025**: Governance obligations, general-purpose AI rules
- **August 2026**: High-risk AI system requirements (Chapter III) become fully applicable
- **August 2027**: Extended transitional period ends for some Annex I products

### 5.2 Transitional Period for Medical Devices

AI systems that are medical devices and already hold valid MDR CE marking before the AI Act's high-risk requirements apply (August 2026) may benefit from a transitional period under **Article 111** of the AI Act, allowing continued use until **August 2027** or until the current CE certificate expires (whichever is earlier), provided no substantial modifications are made to the AI system.

**Important**: "Substantial modification" under the AI Act (Article 3(23)) includes significant changes to the AI model, training data, or intended purpose. Each update the vendor pushes to the diagnostic algorithm must be assessed to determine if it constitutes a substantial modification triggering re-assessment.

---

## 6. Action Plan for Your Hospital

### Immediate Actions (Before Full Deployment)

1. **Request AI Act compliance documentation from the vendor**: Ask specifically for confirmation that they have conducted or are conducting an EU AI Act conformity assessment, in addition to MDR compliance. Request their EU Declaration of Conformity under the AI Act when available.

2. **Confirm EU AI Act database registration**: Verify the vendor has registered or will register the system in the EU AI Act high-risk AI database.

3. **Review instructions for use**: Ensure you have the AI Act-compliant instructions for use (Article 13), which must include information on capabilities, limitations, accuracy levels, and intended deployment conditions.

4. **Conduct a Fundamental Rights Impact Assessment (FRIA)**: If your hospital is a public body or public service provider, this is mandatory. Begin drafting this assessment now.

5. **Update patient information and consent**: Add disclosure of AI-assisted diagnostics to relevant patient-facing documents.

### Short-Term Actions (Within 3–6 Months)

6. **Establish human oversight protocols**: Document and implement clinical workflows ensuring every AI output is reviewed by a qualified radiologist before being acted upon.

7. **Implement logging and record-keeping**: Ensure your IT systems capture AI-specific logs as required by Article 12 and Article 26(6).

8. **Train relevant staff**: Article 26(4) requires that deployers ensure staff using high-risk AI systems have sufficient AI literacy and relevant training.

9. **DPIA under GDPR**: If not already done, complete a DPIA for the AI processing of patient imaging data.

10. **Establish incident reporting procedures**: Define internal procedures for identifying, documenting, and escalating serious incidents involving the AI system.

### Ongoing Obligations

11. **Monitor system performance**: Track whether the AI system's real-world performance in your hospital matches the performance documented by the vendor. Report deviations.

12. **Review substantial modifications**: Each software update from the vendor should be assessed for whether it constitutes a substantial modification under Article 3(23).

13. **Annual review**: Review compliance status annually, especially as national competent authorities publish further guidance.

---

## 7. Key Conclusions

| Question | Answer |
|---|---|
| Does MDR CE marking automatically satisfy EU AI Act requirements? | **No** — it addresses overlapping areas but is not a complete substitution |
| Is the system high-risk under the AI Act? | **Yes** — it falls under Annex I, Section 5 (safety component of MDR device) |
| Does your hospital have AI Act obligations as deployer? | **Yes** — significant obligations under Article 26 |
| Is a FRIA required? | **Yes, if hospital is a public body or public service provider** |
| Is patient disclosure of AI use required? | **Yes** |
| Must vendor separately register under AI Act? | **Yes** — in the EU AI Act database |

The EU AI Act does not create an entirely new burden from scratch given the MDR overlap, but it adds meaningful, enforceable obligations that your hospital must address independently from the vendor's compliance. The most important near-term step is engaging your vendor to understand their AI Act compliance roadmap and simultaneously initiating your own deployer-side obligations, particularly the FRIA and human oversight protocols.

---

*This analysis is based on Regulation (EU) 2024/1689 (the EU AI Act) and Regulation (EU) 2017/745 (EU MDR) as published. Specific implementation guidance from the European AI Office and national competent authorities should be monitored as it develops.*
