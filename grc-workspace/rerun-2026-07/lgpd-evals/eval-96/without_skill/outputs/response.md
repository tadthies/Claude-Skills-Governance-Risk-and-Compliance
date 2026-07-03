Yes — LGPD almost certainly applies to your company, even though you are a US-based SaaS provider. Here is the analysis.

## 1. Does LGPD apply to you?

LGPD (Lei Geral de Proteção de Dados, Brazil's Law No. 13,709/2018) has extraterritorial reach similar to GDPR. Under **Article 3**, LGPD applies to any processing operation:

- carried out in Brazil, **or**
- where the purpose of the processing is to offer or supply goods or services to individuals located in Brazil (Art. 3, II), **or**
- where the personal data being processed was collected in Brazil (Art. 3, III).

Because your app has Brazilian customers and you are actively collecting their name, email, CPF, and purchase history in connection with offering them a service, you fall squarely within Art. 3, II and III. Your company's location in the US, and the absence of a Brazilian legal entity, does not exempt you — LGPD, like GDPR, is triggered by whose data you process and where those individuals are, not where your company is incorporated or hosted.

A few implications that follow from this:

- **CPF is a significant risk factor.** CPF (Cadastro de Pessoas Físicas) is a Brazilian national taxpayer/individual ID number, functionally similar to a US SSN. It is a high-sensitivity identifier frequently targeted by fraud, and Brazilian regulators (ANPD) and courts treat mishandling of CPF numbers seriously. While CPF is not automatically classified as "sensitive personal data" under Art. 5, II (that category is reserved for racial/ethnic origin, religious belief, political opinion, health data, biometric data, genetic data, sexual orientation, union membership, etc.), it is still a high-risk identifier that warrants strong security controls, minimization, and careful legal-basis justification because of its use in identity theft and financial fraud.
- **You likely need a representative in Brazil.** Art. 27 requires foreign controllers/processors that process data covered by Art. 3 to appoint a representative in Brazil for communications with data subjects and the ANPD (Autoridade Nacional de Proteção de Dados). This is analogous to the GDPR Art. 27 EU representative requirement.
- **You need a legal basis for every processing activity**, a lawful, documented retention policy, security safeguards (Art. 46-49), and mechanisms to honor data subject rights (Art. 18: confirmation, access, correction, anonymization/blocking/deletion, portability, information about sharing, information about the possibility of not consenting, and revocation of consent).
- **International transfers matter.** Since your infrastructure and company are US-based, you are transferring Brazilian personal data outside Brazil. Under Art. 33, this requires one of: an ANPD-recognized adequacy decision for the destination country (the US does not currently have one), standard contractual clauses/ANPD-approved contractual clauses, binding corporate rules, specific consent from the data subject for the transfer (Art. 33, VIII), or another Art. 33 mechanism. In practice, many US companies rely on specific, informed consent for the international transfer, or ANPD standard contractual clauses once finalized/adopted, combined with a DPA with any subprocessors.

## 2. Which legal bases apply?

LGPD Art. 7 lists ten legal bases for processing ordinary personal data. For a SaaS platform collecting name, email, CPF, and purchase history, the realistic bases are:

- **Art. 7, V — Contract performance (execução de contrato):** This is your primary basis for name, email, and purchase history where processing is necessary to perform the contract with the customer (account creation, service delivery, billing, order fulfillment, customer support). This mirrors GDPR Art. 6(1)(b) and is generally the cleanest basis for core account and transaction data.
- **Art. 7, I — Consent (consentimento):** Required for processing that goes beyond what's strictly necessary to perform the contract — e.g., marketing emails, behavioral profiling for advertising, sharing data with third parties for purposes unrelated to service delivery, or any secondary use. LGPD consent must be freely given, informed, unambiguous, and for a specific purpose (Art. 8) — pre-ticked boxes or bundled consent are not valid. CPF collected for purposes beyond the core contract (e.g., optional marketing profiling) would need separate consent.
- **Art. 7, IX — Legitimate interests (legítimo interesse):** Can support certain internal purposes like fraud prevention, security monitoring, or service improvement, but Art. 10 requires a documented balancing test (similar to GDPR's LIA), and legitimate interest is explicitly **not available to public authorities** and is subject to closer scrutiny by ANPD for consumer-facing services. It is a weaker basis for CPF specifically, given the fraud-sensitivity of that identifier — most companies default to contract necessity or consent for CPF rather than legitimate interest.
- **Art. 7, II / VI — Legal or regulatory obligation, or compliance with a legal obligation:** If Brazilian tax, consumer protection, or invoicing rules require you to collect and retain CPF (e.g., for issuing valid Brazilian tax invoices/nota fiscal, or complying with Brazilian consumer/tax law when billing Brazilian customers), this becomes an independent legal basis specifically for the CPF collection and retention, separate from contract necessity.

### Practical mapping for your four data elements

| Data element | Most likely legal basis | Notes |
|---|---|---|
| Name | Art. 7, V (contract) | Core to account/service delivery |
| Email | Art. 7, V (contract); Art. 7, I (consent) for marketing use | Split basis if email is also used for marketing |
| CPF | Art. 7, V (contract) and/or Art. 7, II (legal obligation) | Justify why CPF is necessary — if it's for Brazilian tax/invoicing compliance, document that; avoid collecting CPF "just in case" — minimize to what's necessary |
| Purchase history | Art. 7, V (contract); Art. 7, IX (legitimate interest) for analytics | Consent needed if used for ad targeting/profiling beyond service purposes |

## 3. Recommended next steps

1. **Map the data flows** — confirm exactly why CPF is collected and whether it's truly necessary (data minimization, Art. 6, III).
2. **Appoint a Brazil representative** (Art. 27) and, if processing volume/risk warrants it, designate a DPO (Encarregado) under Art. 41 — note that unlike GDPR, LGPD does not have a strict numeric/risk threshold, so ANPD guidance should be checked.
3. **Update your privacy notice** to include LGPD-required disclosures (purpose, legal basis, retention, data subject rights, international transfer mechanism, and how to exercise Art. 18 rights).
4. **Document your international transfer mechanism** (Art. 33) — this is one of the most commonly missed items for US companies serving Brazilian customers.
5. **Run a legal basis assessment (similar to a GDPR Records of Processing/LIA)** for each processing purpose, and separate consent flows from contract-necessity processing so you aren't over-relying on consent for things that are actually contractually necessary (a common LGPD compliance error).
6. **Apply enhanced security controls to CPF** given its sensitivity to fraud, even though it isn't a "sensitive data" category under Art. 5, II.

**Bottom line:** Yes, you need to comply with LGPD due to extraterritorial application under Art. 3. Your primary legal basis will be contract performance (Art. 7, V) for core account/transaction data, supplemented by consent (Art. 7, I) for any marketing/secondary use, possible legal obligation (Art. 7, II) for CPF if tied to Brazilian tax/invoicing requirements, and legitimate interest (Art. 7, IX) only for narrow, well-documented internal purposes like fraud prevention — not as a default basis for CPF.

*This is general compliance guidance, not legal advice. Given the sensitivity of CPF and the international transfer requirements, consult Brazilian data protection counsel to finalize your legal basis documentation and transfer mechanism.*
