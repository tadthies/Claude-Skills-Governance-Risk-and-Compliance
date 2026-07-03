# EU AI Act Compliance Analysis: E-Commerce Customer Chatbot

## Scenario Summary

You are building a customer-facing chatbot for an e-commerce website that:
- Answers product questions
- Processes return requests
- Recommends products based on browsing history
- Is powered by a third-party General Purpose AI (GPAI) model via API

This analysis examines your obligations under **Regulation (EU) 2024/1689 (the EU AI Act)**, which entered into force on 1 August 2024, with provisions applying on a phased schedule through 2027.

---

## 1. Role Classification: Are You a Deployer?

Under the EU AI Act, you are a **deployer** — an entity that puts an AI system into service under its own name or trademark for use by end-users (Article 3(4)). You are not the **provider** (that is the company supplying the GPAI model via API), nor are you placing a product on the market yourself. This role distinction is critical because the Act assigns different obligations to providers vs. deployers.

However, the line between "deployer" and "provider" can blur. Under **Article 25**, a deployer becomes a provider — and assumes all provider obligations — if they:
- Put their name or trademark on a high-risk AI system supplied by another provider
- Make a substantial modification to a high-risk AI system
- Change the intended purpose of a system in a way that triggers a higher risk classification

You should carefully assess whether your customisation of the GPAI model (via system prompts, fine-tuning, or RAG pipelines) constitutes a "substantial modification."

---

## 2. Risk Classification of the Chatbot

The EU AI Act categorises AI systems into four tiers: **unacceptable risk** (banned), **high risk**, **limited risk**, and **minimal risk**. Determining your tier is the most important compliance step.

### 2.1 Is This a High-Risk System?

High-risk AI systems are listed in **Annex III** of the Act. The relevant categories to check for an e-commerce chatbot are:

- **Annex III(4) — Employment and workers management**: Not applicable; this chatbot does not assess employees.
- **Annex III(5) — Access to essential private services**: This covers AI used for credit scoring or insurance risk assessment. A product recommendation engine is not covered here unless it influences credit or pricing in a discriminatory way.
- **Annex III(1) — Biometric identification**: Not applicable unless the chatbot uses biometric data.
- **Annex III(6) — Law enforcement / migration / justice**: Not applicable.

**Preliminary conclusion**: A standard e-commerce chatbot that answers questions, processes returns, and recommends products does **not** fall into Annex III and is therefore **not classified as high-risk** under the current Act.

**Important caveat**: If the chatbot is also used to make credit decisions, assess the creditworthiness of users for buy-now-pay-later schemes, or make automated decisions that significantly affect users' access to services, the risk classification could change.

### 2.2 Limited Risk: Transparency Obligations Apply

Under **Article 50**, AI systems that interact directly with natural persons (i.e., conversational AI and chatbots) are subject to **transparency obligations**, regardless of their risk tier. These are mandatory for your system.

---

## 3. Core Obligations as a Deployer

### 3.1 Transparency to Users (Article 50)

This is your most immediate obligation. You must ensure that users are informed they are interacting with an AI system — **before the interaction begins** or at least at the start. Specifically:

- The chatbot must **disclose its AI nature** in a clear, unambiguous way. A statement such as "You are chatting with an AI assistant" at the outset satisfies this requirement.
- You may not design the chatbot to **deceive users into thinking they are speaking with a human**, unless the human illusion is obvious from context or the user has explicitly requested a human-like persona.
- If the chatbot generates synthetic content (e.g., product descriptions or personalised text), consideration must be given to whether AI-generated content labelling rules apply (Article 50(4) covers deep fakes and synthetic media, but product recommendation text is not typically in scope).

**Practical steps:**
- Add a visible AI disclosure banner or opening message.
- Ensure the chatbot does not claim to be human when sincerely asked.
- Review UX/UI designs to avoid dark patterns that obscure the AI nature.

### 3.2 Human Oversight (Article 26(1))

Deployers must implement appropriate human oversight measures. For a customer service chatbot, this means:

- Having escalation paths to human agents, particularly for complex complaints, return disputes, or sensitive matters.
- Monitoring chatbot outputs for accuracy, bias, and safety.
- Establishing protocols for identifying and acting on chatbot errors or failures.

### 3.3 Intended Use and Monitoring (Article 26)

You must use the AI system only within the **intended purpose** defined by the provider of the GPAI model. If your use case deviates from what the provider has documented, you may need to conduct a conformity assessment yourself.

You are also responsible for:
- **Monitoring the AI system** during operation for risks that were not anticipated at deployment.
- **Reporting serious incidents** to the relevant national market surveillance authority and to the AI provider if the system causes — or is at risk of causing — harm to users (Article 73).

### 3.4 Fundamental Rights and Non-Discrimination

Even for limited-risk systems, the Act reflects broader EU legal principles. The product recommendation feature (which uses browsing history) should be reviewed to ensure:

- It does not create **discriminatory outcomes** (e.g., offering different prices or product ranges based on protected characteristics such as ethnicity, gender, age, or disability status).
- Compliance with **GDPR** regarding the processing of personal data and the use of profiling for recommendations. Personalised recommendations based on browsing history constitute profiling under GDPR and require a lawful basis (typically legitimate interest or consent, with appropriate disclosures).

The EU AI Act does not replace GDPR — both apply in parallel.

### 3.5 Data Governance

As a deployer processing personal data (browsing history, return requests, user queries), you must:

- Ensure data inputs to the AI model comply with GDPR (Articles 5, 6, 9 of GDPR).
- Assess whether personal data sent to the third-party GPAI API is covered by an adequate data processing agreement (DPA) with the model provider.
- Consider whether data is transferred outside the EU/EEA, which triggers additional GDPR obligations (Chapter V of GDPR).

---

## 4. GPAI Model Provider Obligations (What Your Vendor Must Do)

You are using a **General Purpose AI (GPAI) model** — defined in Article 3(63) as a model trained on large amounts of data that can serve a wide variety of purposes. The provider of that model has obligations under **Chapter V (Articles 51–56)** of the EU AI Act, including:

- Maintaining technical documentation.
- Complying with EU copyright law.
- Publishing a sufficiently detailed summary of training data.

If the GPAI model is classified as a **systemic risk model** (those trained with more than 10^25 FLOPs of compute — Article 51), the provider has additional obligations including adversarial testing and incident reporting.

**Your obligation as deployer**: Review your contract and terms of service with the GPAI provider. The Act requires providers to cooperate with deployers and provide sufficient information for deployers to meet their own obligations. Specifically, you should obtain from your vendor:

- Documentation on the model's capabilities and limitations (Article 52(1)(a)).
- Information on the model's intended use cases and known risks.
- Any relevant codes of practice the provider has committed to.

If the vendor cannot provide adequate documentation, this is a legal and operational risk.

---

## 5. Return Processing and Automated Decision-Making

The return processing feature deserves particular attention. If the chatbot **automatically approves or rejects return requests** without human review, this constitutes automated individual decision-making. While the EU AI Act does not directly regulate this aspect, **GDPR Article 22** restricts fully automated decisions that produce legal or similarly significant effects on individuals.

- If the chatbot auto-rejects a return without human review, this could violate GDPR Article 22.
- Users must be informed of automated decision-making and, where applicable, have the right to obtain human review.

**Recommendation**: Ensure that consequential decisions (rejecting returns, flagging accounts for fraud) are subject to human review, or that appropriate GDPR Article 22 safeguards are in place.

---

## 6. Prohibited Practices Check (Article 5)

The Act bans certain AI practices outright. You should confirm none of the following apply to your chatbot:

| Prohibited Practice | Applicable? |
|---|---|
| Subliminal manipulation below conscious awareness | Review if dark patterns are used in recommendations |
| Exploiting vulnerabilities (age, disability) | Ensure chatbot does not exploit vulnerable shoppers |
| Social scoring by public authorities | Not applicable |
| Real-time biometric identification in public spaces | Not applicable |
| Emotion inference in workplace/education | Not applicable |
| Biometric categorisation by protected characteristics | Not applicable |

**Key area**: Personalised recommendations using browsing history could, in extreme cases, be construed as exploitation of user vulnerabilities if the system identifies and targets users with compulsive shopping tendencies or financial vulnerability. This is a low risk for a standard e-commerce site but worth noting in your risk assessment.

---

## 7. Applicability Timeline

| Provision | Applies From |
|---|---|
| Prohibited practices (Article 5) | 2 February 2025 |
| GPAI model rules (Chapter V) | 2 August 2025 |
| Transparency obligations (Article 50) | 2 August 2026 |
| High-risk system obligations (Annex III) | 2 August 2026 |
| High-risk obligations (Annex I products) | 2 August 2027 |

As of mid-2026, **Article 50 transparency obligations are now in force**. If you have already deployed or are about to deploy the chatbot, transparency disclosures are legally required now.

---

## 8. Practical Compliance Checklist

### Immediate Actions (Transparency — Article 50, now in force)
- [ ] Add an AI disclosure at the start of every chat session
- [ ] Ensure the chatbot does not claim to be human
- [ ] Review UX for dark patterns that obscure the AI nature

### Governance and Oversight (Article 26)
- [ ] Document the intended use of the AI system
- [ ] Establish monitoring procedures for accuracy and bias
- [ ] Create escalation paths to human agents for sensitive cases
- [ ] Define an incident response process for AI-related harm

### Vendor Due Diligence
- [ ] Obtain model documentation from the GPAI provider
- [ ] Confirm data processing agreement covers EU AI Act compliance cooperation
- [ ] Assess data transfer risks if the API is outside the EU/EEA
- [ ] Check whether the GPAI model is subject to systemic risk rules

### Data and Privacy (GDPR Intersection)
- [ ] Confirm lawful basis for personalised recommendations (profiling)
- [ ] Update privacy notice to disclose AI-based recommendations
- [ ] Assess GDPR Article 22 compliance for automated return decisions
- [ ] Review data minimisation: what personal data is sent to the API?

### Risk Assessment
- [ ] Conduct a lightweight AI risk assessment documenting the system's purpose, data flows, risk level determination, and mitigation measures
- [ ] Confirm the chatbot does not meet any Annex III high-risk criteria

---

## 9. Summary

Your e-commerce chatbot is most likely a **limited-risk AI system** subject primarily to **Article 50 transparency obligations**, which are currently in force. The key obligations are:

1. **Disclose the AI nature** of the chatbot to users before or at the start of interactions.
2. **Do not impersonate a human** or deceive users about the AI's nature.
3. **Implement human oversight** and escalation pathways, particularly for return processing decisions.
4. **Monitor for harm** and report serious incidents.
5. **Conduct vendor due diligence** on your GPAI model provider to obtain required documentation and ensure contractual protections.
6. **Comply with GDPR in parallel** — particularly for personalised recommendations (profiling) and automated return decisions (Article 22).

The chatbot does not appear to be high-risk under current Annex III classifications, but this should be formally documented in a risk assessment. As the Act's regulatory framework matures and product recommendation AI comes under closer scrutiny, it is advisable to build a governance framework now that can adapt to future guidance from the EU AI Office.

---

*Analysis based on Regulation (EU) 2024/1689 (EU AI Act), applicable as of July 2026. This does not constitute legal advice. Consult qualified EU legal counsel for jurisdiction-specific guidance.*
