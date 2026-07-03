# Eval 96: Extraterritorial Scope — With Skill Response

## Prompt
We are a US-based SaaS company. We have customers in Brazil — we collect their name, email address, CPF (Brazilian tax ID), and purchase history. We have no physical presence in Brazil; all processing happens on US servers. Does LGPD apply to us?

---

## Answer

**Yes, LGPD applies to your company.** Your lack of physical presence in Brazil does not exempt you from compliance. Here is the full analysis.

---

### 1. LGPD's Extraterritorial Reach (Art. 3)

The Lei Geral de Proteção de Dados Pessoais (Law No. 13,709/2018) applies to any processing of personal data of individuals located in Brazil whenever **any** of the following conditions is met:

- **Art. 3, I** — Processing occurs in Brazil
- **Art. 3, II** — The purpose of processing is to offer goods or services to individuals in Brazil
- **Art. 3, III** — The personal data was collected in Brazil

In your case, at minimum **Art. 3, II** is satisfied: you actively offer SaaS services to Brazilian customers and collect their data in connection with those services. The fact that your servers are located in the US is irrelevant — LGPD's territorial trigger is the location of the **data subjects** and the offering of goods/services to them, not the location of the controller's infrastructure or offices.

This extraterritorial design mirrors the GDPR (Art. 3 GDPR) and was deliberate — Brazil sought broad protection for its residents regardless of where foreign companies are incorporated or where they process data.

---

### 2. Absence of Physical Presence Is Irrelevant

Unlike some older privacy regimes that relied on establishment-based jurisdiction, LGPD uses a **targeting/effects test**: if you are offering services to persons in Brazil (evidenced by accepting Brazilian customers, billing in BRL or accepting CPF numbers, translating your product for Brazilian users, etc.), LGPD applies. The fact that all processing occurs on US servers does not reduce your obligations.

The ANPD has authority under Art. 55-A to investigate foreign controllers and, where necessary, request cooperation with foreign authorities.

---

### 3. CPF as Personal (Potentially Sensitive) Data

The CPF (Cadastro de Pessoas Físicas) is Brazil's national tax identification number — a unique identifier directly tied to an individual's identity and financial history. Under LGPD:

- **CPF is unambiguously personal data** under Art. 5, I (any information relating to an identified or identifiable natural person)
- While CPF is not listed in Art. 11 as **sensitive personal data** (which covers racial/ethnic origin, religion, political opinion, union membership, health, sexual life, genetic and biometric data), collection of CPF at scale can create heightened exposure because:
  - It enables identity theft and financial fraud if breached
  - The ANPD evaluates **risk of harm** in assessing whether a breach triggers notification (Art. 48) — CPF exposure will almost certainly meet this threshold (see Eval 99)
  - Depending on context (e.g., linking CPF to health or financial profiles), secondary processing could implicate sensitive data rules

**Practical implication:** You need a clear legal basis for collecting CPF (most commonly Art. 7, V — contractual necessity, for billing/account verification, or Art. 7, X — credit protection, if used for fraud/credit purposes). If you are collecting CPF beyond what is strictly necessary, you may violate the **necessity principle** (Art. 6, III).

---

### 4. Key Obligations That Now Apply to You

As a controller subject to LGPD, the following obligations apply:

| Obligation | LGPD Basis | Key Requirement |
|-----------|-----------|-----------------|
| **Legal basis for processing** | Art. 7 (regular data); Art. 11 (sensitive data) | Identify and document a valid legal basis for each processing activity (consent, contract, legal obligation, legitimate interest, etc.) |
| **Privacy notice / transparency** | Art. 9 | Provide a clear, accessible notice in Portuguese covering: controller identity, DPO contact, purpose, legal basis, data sharing, international transfers, data subject rights, retention |
| **Data subject rights** | Art. 18–22 | Honor requests for access, correction, deletion, portability, revocation of consent; respond within ANPD-indicated timeframes (typically 15 days) |
| **DPO (Encarregado) appointment** | Art. 41 | Appoint a Data Protection Officer; publish name and contact publicly (no SME exemption under LGPD) |
| **Records of Processing Activities (RoPA)** | Art. 37 | Maintain records of your processing activities; ANPD may require disclosure |
| **Security measures** | Art. 46 | Implement technical and administrative measures to protect data; ANPD may set minimum standards |
| **Breach notification** | Art. 48 | Report incidents causing relevant risk to ANPD within 3 working days (preliminary) and 20 working days (full report) |
| **International transfer mechanism** | Art. 33–36 | Since you are transferring data to/storing data in the US (which lacks an adequacy decision from ANPD), you must use standard contractual clauses or another approved mechanism |
| **Data minimisation** | Art. 6, III | Collect only what is necessary; revisit whether collecting CPF is strictly necessary for your use case |

---

### 5. ANPD Enforcement and Penalties (Art. 52)

The ANPD is Brazil's supervisory authority with full enforcement powers over foreign controllers subject to LGPD. Penalties include:

- **Warning** with a remediation period
- **Simple fine:** Up to **2% of revenues in Brazil** (prior fiscal year, group basis), with a **cap of R$50 million per violation**
- **Daily fine** to compel compliance (same cap)
- **Publicisation** of the infraction
- **Blocking or deletion** of the personal data related to the violation
- **Suspension or prohibition** of processing activity

Each violation is assessed separately, so multiple non-compliant practices can result in multiple fines stacking up to the R$50M per-violation cap.

---

### 6. Recommended Immediate Actions

1. **Conduct a LGPD gap assessment** — map all data flows for Brazilian customer data against LGPD requirements
2. **Document legal bases** — confirm Art. 7 bases for each processing activity (name/email likely: Art. 7, V — contract; CPF: Art. 7, V or X; purchase history: Art. 7, V)
3. **Update your privacy notice** in Portuguese, covering all Art. 9 elements
4. **Appoint a DPO (Encarregado)** and publish contact details
5. **Establish international transfer safeguards** — since the US lacks ANPD adequacy, put in place standard contractual clauses (ANPD-approved) for data flows to US servers
6. **Build data subject rights workflows** — ensure you can respond to Brazilian customers exercising Art. 18 rights within 15 days
7. **Implement breach response procedures** — calibrate to the 3-working-day ANPD preliminary notification requirement

---

**Summary:** LGPD applies to your company by virtue of Art. 3, II — you offer services to individuals in Brazil and process their personal data in connection with those services. Physical presence is irrelevant. You must comply with all controller obligations, including DPO appointment, legal basis documentation, privacy notices, data subject rights, breach notification, and international transfer safeguards for US-stored data. ANPD fines can reach 2% of Brazilian revenue or R$50M per violation.
