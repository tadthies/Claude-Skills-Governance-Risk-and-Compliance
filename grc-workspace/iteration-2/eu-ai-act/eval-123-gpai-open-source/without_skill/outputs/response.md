# EU AI Act Compliance Analysis: GPAI Model Provider Obligations

## Executive Summary

You are developing a large language model (LLM) with 200 billion parameters, trained on 15 trillion tokens using approximately 3×10^24 FLOPs of compute, and plan to release it under an open-source licence. Under Regulation (EU) 2024/1689 (the EU AI Act), this model qualifies as a **General-Purpose AI (GPAI) model** and almost certainly as a **GPAI model with systemic risk** due to the compute threshold. Open-source release provides some relief from obligations but does not eliminate them entirely — and the systemic-risk designation imposes obligations that the open-source exemption does not waive.

This analysis walks through the applicable legal framework, your specific classification, the obligations that apply, the scope of the open-source exemption, and practical compliance steps.

---

## 1. Legal Framework: GPAI Models Under the EU AI Act

### 1.1 What Is a GPAI Model?

Article 3(63) of the EU AI Act defines a **general-purpose AI model** as an AI model that:

- Is trained on large amounts of data using self-supervised learning at scale;
- Displays significant generality;
- Is capable of competently performing a wide range of distinct tasks; and
- Can be integrated into a variety of downstream systems or applications.

A 200-billion-parameter LLM trained on 15 trillion tokens clearly satisfies all four elements. The model is self-supervised (next-token prediction), operates at scale, is capable of a broad range of language tasks (coding, summarisation, reasoning, translation, etc.), and is designed to be integrated into downstream applications by third parties.

### 1.2 Title VIII: GPAI-Specific Rules

The EU AI Act dedicates Title VIII (Articles 51–56) exclusively to GPAI models. These rules sit alongside — and are distinct from — the risk-based obligations for AI systems in Articles 6–50. GPAI model providers must comply with Title VIII regardless of whether any particular downstream use of the model is high-risk.

### 1.3 The Two-Tier Structure

Title VIII creates two tiers:

| Tier | Criteria | Key Obligations |
|------|----------|-----------------|
| **Standard GPAI model** | Trained with ≥10^23 FLOPs | Technical documentation, copyright transparency, policy for downstream deployers |
| **GPAI model with systemic risk** | Trained with ≥10^25 FLOPs (or designated by Commission) | All standard obligations PLUS adversarial testing, incident reporting, cybersecurity measures, model evaluation |

---

## 2. Classification of Your Model

### 2.1 Standard GPAI Threshold

Article 51(1)(a) establishes that a GPAI model is presumed to have been trained using **at least 10^23 FLOPs** if it was trained on significant compute. All GPAI models meeting this threshold must comply with the baseline obligations in Article 53.

Your model was trained with approximately **3×10^24 FLOPs** — roughly 30 times the baseline threshold. You are clearly a standard GPAI model provider.

### 2.2 Systemic Risk Threshold

Article 51(1)(b) designates a GPAI model as having **systemic risk** if it was trained using a total compute of more than **10^25 FLOPs**.

Your compute of **3×10^24 FLOPs** is approximately **one-third** of the 10^25 FLOPs threshold. This means:

- **You do not automatically qualify as a GPAI model with systemic risk** under the compute-based bright-line rule.
- However, the European Commission retains authority under Article 51(2) to designate additional models as having systemic risk based on qualitative criteria (e.g., capabilities, reach, societal impact). A 200B-parameter model with demonstrated frontier capabilities could be subject to such designation.
- You should monitor Commission guidance and any Delegated Acts or Codes of Practice that may adjust this threshold or add qualitative criteria.

**Practical implication:** At this compute level, you sit in a zone of uncertainty. You face the standard GPAI obligations with certainty, and should be prepared for potential systemic-risk classification. Proactively implementing systemic-risk measures is advisable as a risk management strategy.

---

## 3. The Open-Source Exemption: Scope and Limits

### 3.1 What the Open-Source Exemption Covers

Article 53(2) provides that providers of **GPAI models released under a free and open-source licence** are exempt from two specific standard obligations:

1. **Technical documentation** requirements under Article 53(1)(a); and
2. **Information and documentation for downstream providers** requirements under Article 53(1)(b).

The rationale is that open release of model weights, architecture, and training details is considered a sufficient substitute for formal documentation mandates.

### 3.2 What the Open-Source Exemption Does NOT Cover

The open-source exemption is narrowly scoped. It does **not** exempt you from:

- **Article 53(1)(c):** Establishing a policy to comply with Union copyright law, including the Text and Data Mining (TDM) exception under the Copyright Directive (Directive 2019/790).
- **Article 53(1)(d):** Publishing a sufficiently detailed summary of the content used to train the GPAI model.
- **Any systemic-risk obligations** if the model is designated as having systemic risk (Article 53(2) expressly excludes Article 55 obligations from the open-source exemption).

### 3.3 Definition of "Free and Open-Source Licence"

The Act does not define "free and open-source licence" with precision. To qualify, the licence must make weights, parameters, and model architecture publicly available. Licences that impose material use restrictions (e.g., restrictions on commercial use, deployment scale limits, or field-of-use exclusions) may not qualify as "open-source" for purposes of the exemption. You should ensure your chosen licence genuinely permits freedom to use, study, modify, and distribute, consistent with OSI-approved definitions or equivalent interpretive guidance from the AI Office.

---

## 4. Your Specific Obligations

### 4.1 Obligations Applicable to All Standard GPAI Models (Article 53)

Even with an open-source licence, the following obligations apply to you:

#### 4.1.1 Copyright Compliance Policy (Article 53(1)(c))

You must put in place and maintain a **policy to comply with Union law on copyright and related rights**, specifically:

- Compliance with the TDM exception in Article 4 of Directive 2019/790;
- Honouring rightsholders' **opt-out reservations** (Article 4(3) of the Copyright Directive) — i.e., if a website or publisher has reserved their rights via machine-readable means (e.g., robots.txt, HTTP headers), you must not have crawled and trained on that content;
- Documentation of your data sourcing process demonstrating copyright compliance.

This is a substantive obligation even for open-source models. If your 15-trillion-token dataset includes web crawl data, you will need to demonstrate that you processed opt-out signals and that your training data sourcing was legally compliant.

#### 4.1.2 Training Data Summary Publication (Article 53(1)(d))

You must **publish a sufficiently detailed summary** of the content used to train the GPAI model. This summary must be made publicly available.

The Act does not specify exact detail requirements; the AI Office is expected to provide guidance through a Code of Practice. Practically, this will likely require:

- Categories of data sources (e.g., web crawl, books, code repositories, curated datasets);
- Approximate proportions of each data type;
- Languages represented;
- Known limitations or gaps in training data.

This is a transparency obligation intended to enable rightsholders, researchers, and regulators to assess copyright compliance and model capabilities.

### 4.2 Obligations If Classified as Having Systemic Risk (Article 55)

If the European Commission designates your model as having systemic risk — which is plausible given the model's scale — the following additional obligations apply, and the open-source exemption does NOT shield you from them:

#### 4.2.1 Model Evaluation (Article 55(1)(a))

You must perform **model evaluations** in accordance with standardised protocols and tools, including:

- Adversarial testing, commonly referred to as **red-teaming**;
- Evaluation covering at minimum: CSAM generation, bioweapon-related capabilities, cyberattack facilitation, and other categories specified in the Act or by the Commission;
- Evaluations conducted before release and periodically thereafter.

#### 4.2.2 Incident Reporting (Article 55(1)(b))

You must **assess and mitigate possible systemic risks**, including:

- Identifying and monitoring known and reasonably foreseeable risks at Union level;
- Reporting any **serious incidents** to the AI Office without undue delay;
- Maintaining records of incidents and corrective actions taken.

#### 4.2.3 Cybersecurity Measures (Article 55(1)(c))

You must implement **adequate cybersecurity protection** for the model, its infrastructure, and (where applicable) physical infrastructure. This includes protecting model weights from unauthorised access, manipulation, or theft.

#### 4.2.4 Energy Efficiency Reporting (Article 55(1)(d))

You must **report to the AI Office** on the energy consumption of your model. This includes training compute and, where measurable, inference energy use. The AI Office is expected to develop templates and standards for this reporting.

---

## 5. Registration and Notification Requirements

### 5.1 EU Database Registration (Article 71)

GPAI model providers are required to register in the **EU database for high-risk AI systems and GPAI models**. The specific registration requirements and timeline for GPAI models will be established through implementing acts. You should monitor the AI Office's guidance on when and how to register.

### 5.2 Notifying the AI Office of Systemic Risk

Under Article 52, if you have reason to believe your GPAI model could have systemic risk (even absent a formal designation), you are encouraged — and in some circumstances required — to notify the **EU AI Office**. The AI Office, established within the European Commission's DG CONNECT, is the primary supervisory body for GPAI models at the Union level.

---

## 6. Interaction with Downstream Providers and Deployers

### 6.1 Your Role as a GPAI Model Provider

The Act distinguishes between:

- **GPAI model providers** (you): entities that develop and make a GPAI model available;
- **Providers of AI systems** built on top of GPAI models: downstream developers who integrate your model into products;
- **Deployers**: entities that deploy AI systems to end users.

As the upstream GPAI model provider, your obligations run directly under Title VIII, while downstream system providers must comply with Articles 6–50 (including any high-risk system obligations) based on how they use your model.

### 6.2 Technical Documentation for Downstream Providers

Although the open-source exemption waives the formal Article 53(1)(b) documentation obligation, you should still provide **practical technical information** to downstream system providers so they can comply with their own obligations. This includes:

- Intended uses and known limitations;
- Performance benchmarks;
- Known failure modes and biases;
- Recommended safeguards.

Releasing a **model card** and **system card** consistent with current AI transparency best practices will serve both compliance and reputational purposes.

### 6.3 Model Cards and Acceptable Use Policies

Many frontier model providers pair open-source releases with an **Acceptable Use Policy (AUP)** that restricts certain downstream applications (weapons development, CSAM, etc.). While not strictly mandated by the EU AI Act, such policies reduce legal and reputational risk and signal good-faith compliance.

---

## 7. The EU AI Office and Code of Practice

### 7.1 Role of the AI Office

The **EU AI Office** (established under Commission Decision 2024/1565) is the central body responsible for:

- Supervising GPAI model providers at the Union level;
- Developing and maintaining Codes of Practice;
- Conducting evaluations and investigations;
- Imposing penalties via national market surveillance authorities.

You should engage with the AI Office, participate in the Code of Practice process, and assign a designated point of contact for regulatory interactions.

### 7.2 Code of Practice

The EU AI Act mandates that the AI Office facilitate development of a **Code of Practice** for GPAI model providers (Article 56). This Code is developed through a multi-stakeholder process involving model providers, civil society, academics, and Member State authorities. The Code of Practice is intended to:

- Operationalise the Article 53 and 55 obligations;
- Establish templates for the training data summary;
- Set standards for adversarial testing methodologies;
- Define cybersecurity baseline expectations.

Participation in the Code of Practice drafting process is voluntary but strategically important. Compliance with an adopted Code of Practice will be presumed to satisfy corresponding legal obligations. As of mid-2025, the first general-purpose AI Code of Practice was under active development.

---

## 8. Timeline and Applicability

### 8.1 Phased Entry Into Force

The EU AI Act entered into force on **1 August 2024**. GPAI-specific obligations under Title VIII apply from **2 August 2025** (12 months after entry into force).

- If you release the model **before 2 August 2025**: obligations may apply from that date to models already placed on the market (with a transition period).
- If you release the model **after 2 August 2025**: full Title VIII obligations apply immediately upon making the model available in the Union market.

### 8.2 Existing Models

For GPAI models already placed on the market before 2 August 2025, providers have until **2 August 2027** to bring them into compliance, unless significant modifications are made.

---

## 9. Penalties

### 9.1 Fines for GPAI Model Providers

Non-compliance with GPAI obligations under Articles 53 and 55 is subject to **administrative fines** imposed by the AI Office or national competent authorities:

- Violations of Articles 53 and 55: up to **EUR 15 million or 3% of worldwide annual turnover**, whichever is higher.
- Providing false, incomplete, or misleading information: up to **EUR 7.5 million or 1% of worldwide annual turnover**, whichever is higher.

For large organisations, the turnover-based caps can far exceed the absolute figures.

---

## 10. Summary of Your Obligations

| Obligation | Applies to You? | Open-Source Exemption? |
|------------|-----------------|------------------------|
| Technical documentation (Art. 53(1)(a)) | Yes | **Exempted** for open-source |
| Information for downstream providers (Art. 53(1)(b)) | Yes | **Exempted** for open-source |
| Copyright compliance policy (Art. 53(1)(c)) | **Yes — mandatory** | No exemption |
| Training data summary publication (Art. 53(1)(d)) | **Yes — mandatory** | No exemption |
| EU database registration (Art. 71) | **Yes** | No exemption |
| AI Office notification | **Yes** | No exemption |
| Model evaluation / red-teaming (Art. 55(1)(a)) | If systemic risk designated | No exemption applies to Art. 55 |
| Serious incident reporting (Art. 55(1)(b)) | If systemic risk designated | No exemption applies to Art. 55 |
| Cybersecurity measures (Art. 55(1)(c)) | If systemic risk designated | No exemption applies to Art. 55 |
| Energy consumption reporting (Art. 55(1)(d)) | If systemic risk designated | No exemption applies to Art. 55 |

---

## 11. Practical Compliance Recommendations

1. **Audit your training data** for copyright compliance now. Document the datasets used, the data sourcing methodology, robots.txt and opt-out signal processing, and any licences obtained. This work underpins both the copyright policy (Art. 53(1)(c)) and the training data summary (Art. 53(1)(d)).

2. **Draft and publish a training data summary** covering categories, proportions, languages, and known gaps. Engage with the AI Office's Code of Practice process to calibrate detail requirements.

3. **Implement a copyright compliance policy** as a formal internal document signed off by legal counsel. Ensure it addresses TDM opt-outs and is updated as you train future model versions.

4. **Verify your open-source licence** genuinely meets the Act's requirements. Use an OSI-approved licence or seek legal advice on whether your chosen licence qualifies for the exemption.

5. **Monitor Commission classification activity** — if your model is designated as having systemic risk, you will need to implement red-teaming, incident reporting, and cybersecurity measures rapidly.

6. **Proactively implement adversarial testing** regardless of formal classification. Red-teaming is best practice, demonstrates good faith to regulators, and will likely be required if the Commission designates your model.

7. **Assign an EU AI Act compliance lead** and establish a point of contact for the AI Office.

8. **Register in the EU database** when the registration portal opens for GPAI models.

9. **Participate in the Code of Practice** process to influence implementation standards and gain presumption of compliance upon adoption.

10. **Document everything.** Even where the open-source exemption waives formal submission requirements, maintaining internal records of compliance activities is essential for demonstrating good faith in any regulatory inquiry.

---

## 12. Conclusion

As a GPAI model provider releasing under an open-source licence, you benefit from exemptions from formal technical documentation and downstream information obligations. However, your core obligations — a copyright compliance policy and a training data summary — are non-negotiable and directly applicable. At 3×10^24 FLOPs, you fall below the automatic systemic-risk threshold but are in a range where Commission designation is plausible; proactive preparation for systemic-risk obligations is strongly advisable. Engage with the EU AI Office and the Code of Practice process early, and treat the open-source exemption as a documentation relief rather than a licence to avoid compliance work. The Act's transparency and safety objectives still apply to you in full.

---

*This analysis is based on Regulation (EU) 2024/1689 as published in the Official Journal of the European Union on 12 July 2024. It reflects general knowledge as of mid-2026 and does not constitute legal advice. Interpretive guidance from the EU AI Office and any adopted Codes of Practice should be consulted for up-to-date requirements.*
