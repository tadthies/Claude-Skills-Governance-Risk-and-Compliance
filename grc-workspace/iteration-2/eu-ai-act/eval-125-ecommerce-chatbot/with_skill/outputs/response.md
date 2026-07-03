# EU AI Act Obligations for an E-Commerce Customer-Facing Chatbot

## Executive Summary

Your e-commerce chatbot — handling product questions, returns, and personalized recommendations via a third-party GPAI API — falls under the **limited-risk** tier of the EU AI Act (Regulation (EU) 2024/1689). It is **not** high-risk under Annex III. As the deployer (not the provider or GPAI provider), your primary obligations arise under **Article 50** (transparency) and **Article 26** (deployer duties). The most pressing deadline is **2 August 2026**, when Art. 50 transparency requirements become applicable — giving you approximately one month to prepare.

---

## 1. Risk Classification: Limited Risk, Not High-Risk

The first step in any EU AI Act analysis is correctly classifying the system. High-risk AI systems are exhaustively listed in **Annex III** of the Regulation. Annex III covers systems used in:

- Biometric identification and categorisation
- Critical infrastructure management
- Education and vocational training
- Employment and worker management
- Access to essential private and public services
- Law enforcement
- Migration and border control
- Administration of justice and democratic processes

A customer-facing e-commerce chatbot — even one that processes returns and makes product recommendations based on browsing history — does **not** fall into any of these categories. It is a commercial, consumer-facing conversational tool operating in a retail context with no material impact on individuals' access to fundamental rights or services of critical importance.

**Your chatbot is a limited-risk AI system under Article 50** of the EU AI Act. This means:

- You are **not** subject to the extensive Annex III high-risk obligations (conformity assessments, technical documentation under Annex IV, registration in the EU database, etc.)
- Your obligations are focused primarily on **transparency toward users**
- The compliance burden is substantially lighter than for high-risk systems

If your chatbot's functionality evolves — for example, if it begins making automated credit decisions, screening employment applications, or interacting with systems that affect access to public services — you would need to re-evaluate this classification.

---

## 2. Article 50(1): The Core Transparency Obligation

**Article 50(1)** is your central compliance requirement. It states that providers and deployers of AI systems intended to interact with natural persons must ensure that those persons are **informed that they are interacting with an AI system**, unless this is obvious from the context.

### Does the Disclosure Obligation Apply to Your Chatbot?

Yes — unambiguously. The "obvious from context" exception is narrow and does not apply here. The legal standard is whether it would be obvious to a **reasonably well-informed user**. An e-commerce chatbot does not meet this standard for several reasons:

- Many consumers still expect live human agents in customer service contexts
- The interface of a chat widget on a product page does not inherently signal AI
- The chatbot's ability to handle returns, answer nuanced product questions, and personalise recommendations can make it appear more human-like, not less
- A "reasonably well-informed" person browsing an e-commerce site has no basis to assume, without disclosure, that they are talking to an AI rather than a human support agent

The obligation therefore **does apply**. You must disclose, clearly and at the start of each interaction, that the user is interacting with an AI system. Buried disclosures in terms of service or privacy policies are unlikely to satisfy this requirement — the disclosure must be contemporaneous with the interaction.

### Practical Implementation

- Display a clear, prominent notice at the start of each chat session (e.g., "You are chatting with an AI assistant")
- The notice should appear before the user submits their first message
- The language must be clear and understandable — avoid technical jargon
- The disclosure should be visible in the chat interface itself, not only in peripheral legal documents

---

## 3. Your Obligations as Deployer Under Article 26

As an organisation that deploys a third-party AI system rather than developing one from scratch, you are a **deployer** under the EU AI Act. Article 26 sets out deployer obligations. While Article 26's full weight applies to high-risk systems, several principles extend to deployers of all AI systems and represent baseline good practice:

### Article 26 Obligations Relevant to Your Context

| Obligation | Description | Applicability to Your Chatbot |
|---|---|---|
| Follow provider instructions | Use the AI system in accordance with the provider's instructions for use and purpose | Ensure your use of the GPAI API aligns with the API provider's stated permitted uses |
| Staff competence | Ensure staff operating or overseeing the system have sufficient AI literacy and competence | Train customer service and technical teams on how the chatbot works and its limitations |
| Monitor the system | Monitor operation of the system and report concerns to the provider | Establish logging and monitoring for chatbot outputs; review for errors, bias, or harmful outputs |
| Report serious incidents | Report serious incidents or malfunctions to the provider and relevant market surveillance authorities | Establish an internal escalation process and understand your reporting obligations |
| Data governance | Implement appropriate controls over data used in conjunction with the system | Manage browsing history and personal data used for recommendations in line with GDPR and AI Act requirements |

For limited-risk systems, Article 26 obligations are less prescriptive than for high-risk systems, but the deployer still bears responsibility for appropriate use. You cannot simply deploy the chatbot and disclaim all responsibility by pointing to the GPAI provider.

---

## 4. Distinguishing Your Obligations From the GPAI Provider's Obligations

This distinction is critical and frequently misunderstood. There are **three distinct roles** in your scenario:

### Role 1: You — the Deployer

You are integrating a third-party GPAI model via API to build a customer-facing product. Your obligations:

- **Article 50(1)**: Disclose to users that they are interacting with an AI system
- **Article 26**: Follow the provider's instructions; ensure staff competence; monitor; report incidents
- **GDPR**: Handle personal data (browsing history, user queries) lawfully — the AI Act does not replace GDPR obligations

### Role 2: The Third-Party API Provider — the GPAI Provider

The company whose model you access via API (e.g., a large foundation model provider) is a **General Purpose AI (GPAI) model provider** under **Article 53**. Their obligations include:

- Preparing and maintaining technical documentation
- Complying with EU copyright law and providing summaries of training data
- Publishing and maintaining policies on acceptable use
- Cooperating with the AI Office
- Implementing a cybersecurity policy proportionate to systemic risk (if the model exceeds the systemic risk threshold under Art. 51)

**These obligations fall on the GPAI provider, not on you.** You are not responsible for training data documentation or GPAI model compliance. However, you should:

- Review the GPAI provider's terms of service and acceptable use policies
- Ensure your use case is within the permitted scope
- Obtain and review any available technical documentation or model cards

### Role 3: No Provider Role for You

You are **not** a provider of the AI system in the sense of Article 6 and related provisions (which govern those who place AI systems on the market or put them into service for others). You are putting the system into service for your own customers, which makes you a deployer. You do not bear provider obligations such as filing conformity assessments or registering in the EU database — those apply to the GPAI provider and to high-risk AI system providers.

---

## 5. Application Date: 2 August 2026

The EU AI Act has a phased application schedule. **Article 50 transparency obligations** — including the Art. 50(1) disclosure requirement for human-interacting AI systems — become applicable on **2 August 2026**.

As of today (2 July 2026), this deadline is **approximately one month away**. You have very limited time to achieve compliance.

### Immediate Action Checklist

| Action | Deadline | Priority |
|---|---|---|
| Implement Art. 50(1) AI disclosure in the chatbot UI | Before 2 August 2026 | Critical |
| Review GPAI API provider's terms and acceptable use policy | Immediately | High |
| Establish monitoring and logging for chatbot outputs | Before 2 August 2026 | High |
| Train relevant staff on AI literacy and chatbot limitations | Before 2 August 2026 | Medium |
| Update privacy policy / user-facing documentation to reference AI use | Before 2 August 2026 | Medium |
| Establish incident escalation and reporting process | Before 2 August 2026 | Medium |
| Review data flows for GDPR alignment (browsing history for recommendations) | Immediately (ongoing GDPR obligation) | High |

---

## 6. Additional Considerations

### Personalized Recommendations and Profiling

Your chatbot uses browsing history to recommend products. This is not a factor that elevates the system to high-risk under Annex III, but it does raise **GDPR considerations** independent of the AI Act:

- Personalisation based on browsing history may require a lawful basis under GDPR Art. 6 (typically legitimate interests or consent)
- If recommendations constitute solely automated decision-making with significant effects on individuals, Art. 22 GDPR may apply — though product recommendations in an e-commerce context rarely meet the "significant effects" threshold
- Ensure your privacy notice discloses the use of browsing data for AI-powered recommendations

### Return Processing

If the chatbot can autonomously process returns (e.g., approve refunds, issue credits) without human review, consider establishing human oversight mechanisms for edge cases. This is good practice regardless of the AI Act classification and reduces operational risk.

### Future-Proofing

The EU AI Act is a living regulatory framework. Monitor guidance from the European AI Office, particularly on:

- Clarifications to the "obvious from context" exception in Art. 50(1)
- Any sectoral guidance on retail and e-commerce AI
- Updates to Annex III that could reclassify systems in the future

---

## Summary of Your Obligations

| Obligation | Source | Status |
|---|---|---|
| Disclose AI interaction to users at start of each chat | Art. 50(1) EU AI Act | Required by 2 August 2026 |
| Follow GPAI provider's instructions for use | Art. 26 EU AI Act | Ongoing |
| Ensure staff competence and AI literacy | Art. 26 EU AI Act | Required by 2 August 2026 |
| Monitor chatbot outputs and report incidents | Art. 26 EU AI Act | Ongoing |
| GPAI technical documentation and copyright compliance | Art. 53 EU AI Act | Provider's obligation, not yours |
| Conformity assessment / Annex III registration | Annex III, Art. 16 EU AI Act | Not applicable (not high-risk) |
| GDPR compliance for browsing data and personal data | GDPR | Ongoing (separate obligation) |

Your compliance path is achievable within the available timeframe. The disclosure requirement is the most urgent and concrete action: implement a clear, upfront notice in your chatbot interface before 2 August 2026. Everything else can be built out as part of a responsible AI governance programme in the weeks that follow.
