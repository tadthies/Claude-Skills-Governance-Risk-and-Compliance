Short answer: No — not as you've described it. Using health data and credit scores to build marketing profiles for personalized financial products is very likely unlawful under Brazil's LGPD (Lei Geral de Proteção de Dados, Law No. 13,709/2018) as currently planned. Health data is "sensitive personal data" with a restrictive legal basis regime, and using it for marketing/commercial profiling is one of the clearest LGPD red flags. Credit score data, while not "sensitive" under LGPD's closed list, is also tightly regulated (via LGPD plus the Cadastro Positivo law) and raises purpose-limitation and profiling concerns when repurposed for marketing.

Below is a breakdown of why, what legal bases could theoretically apply, and what safeguards would be required if you still want to pursue any part of this.

## 1. Classify the data correctly

**Health insurance data → "dado pessoal sensível" (sensitive personal data), Art. 5º, II**
LGPD explicitly lists "dado referente à saúde" (health-related data) as sensitive personal data, alongside racial/ethnic origin, religious belief, political opinion, genetic/biometric data, and data on sex life. Health insurance data (coverage, claims, pre-existing conditions, treatments) falls squarely in this category.

**Credit score data → regular personal data, but heavily regulated**
Credit scoring data isn't on LGPD's sensitive-data list, but it's still personal data subject to LGPD's general regime, and it's additionally governed by:
- The Cadastro Positivo law (Law No. 12,414/2011, as amended by LC 166/2019), which sets specific rules for credit scoring databases (transparency, right to explanation of methodology, correction rights).
- LGPD Art. 20, which gives data subjects the right to request review of decisions made solely by automated processing (including scoring/profiling) that affect their interests.

## 2. Why sensitive health data can't be used for marketing purposes

For sensitive personal data, LGPD Art. 11 provides an exhaustive (closed) list of legal bases — narrower than the general Art. 7 list for ordinary data. The available bases are essentially:
- Specific and highlighted ("destacado") consent, for one or more determined purposes;
- Compliance with a legal or regulatory obligation by the controller;
- Shared data processing by public administration for public policy execution;
- Studies by research bodies, with anonymization when possible;
- Regular exercise of rights in judicial, administrative, or arbitration proceedings;
- Protection of life or physical safety (of the data subject or a third party);
- Health protection, exclusively, in a procedure carried out by health professionals, health services, or health authorities;
- Fraud prevention and security of the data subject, in identification/authentication processes for registration systems (with limits).

**Marketing personalized financial products is not on this list.** There is no "legitimate interest" basis available for sensitive data — legitimate interest (Art. 10) applies only to ordinary personal data, not sensitive data. This is the single most important compliance point: you cannot rely on legitimate interest to justify using health data for marketing, no matter how compelling the business case.

That leaves **specific, highlighted, opt-in consent (Art. 11, I c/c Art. 8, §4º)** as essentially the only realistic path — and even then, several problems remain:

- **Purpose limitation (Art. 6º, I):** The health data was presumably collected for insurance/underwriting or administrative purposes, not marketing. Repurposing it requires a new, specific legal basis and, practically, fresh consent — you can't quietly extend the original purpose.
- **Necessity and non-excessiveness (Art. 6º, III):** Regulators (ANPD) and courts will ask whether health data is actually *necessary* to personalize a financial product, or whether less sensitive proxies would achieve the same goal. Marketing personalization is rarely considered "necessary" enough to justify using sensitive health data — this is treated as disproportionate.
- **Non-discrimination principle (Art. 6º, IX):** LGPD explicitly prohibits processing for "unlawful or abusive discriminatory purposes." Using health status to steer people toward or away from financial products (e.g., insurance, credit, loans) risks being seen as discriminatory — denying or upselling products based on health conditions is a classic red flag that regulators and courts treat harshly, especially for a financially vulnerable population.
- **ANPD and sectoral scrutiny:** The Brazilian Central Bank (BACEN) and CVM also regulate fintechs, and using health data to price or target financial products could trigger conduct-risk and consumer-protection issues under the Consumer Defense Code (CDC) in addition to LGPD — Brazilian courts have been aggressive on this front (e.g., cases involving insurers/banks improperly acquiring health data).

**Bottom line on health data:** using it for marketing is not a "find the right legal basis and safeguards" exercise — it is close to a per se violation absent a genuinely specific, freestanding, opt-in consent collected for that exact purpose, which is difficult to obtain and easy to challenge, and it will still fail the necessity/non-discrimination tests in most fintech marketing scenarios. Realistic recommendation: **do not use health insurance data for marketing personalized financial products.** Firewall it entirely from marketing/analytics systems.

## 3. Credit score data — more paths available, but still constrained

Credit score data is ordinary personal data, so more of the Art. 7 legal bases are theoretically available:

- **Consent (Art. 7º, I):** Freely given, informed, unambiguous, for a specific purpose. Pre-ticked boxes or bundled "accept all" consent won't qualify.
- **Legitimate interest (Art. 7º, IX / Art. 10):** Potentially available for using existing customer data to personalize offers to *existing customers*, but:
  - Must pass a documented Legitimate Interest Assessment (balancing test) weighing the controller's interest against the data subject's fundamental rights and reasonable expectations.
  - Cannot be used to justify sending marketing to *prospects* whose data you obtained from third parties (e.g., purchased credit bureau data) without their knowledge — that generally requires consent or another concrete basis, plus proper transparency (Art. 9).
  - Legitimate interest cannot be used for sensitive data, and cannot be used if it would be "abusive" — profiling based on credit score to push higher-cost products to financially strained consumers would likely fail the balancing test and could also violate CDC vulnerability protections.
- **Contract execution (Art. 7º, V):** Could justify using credit score data to determine eligibility/pricing for a product the customer actively requested, but not to justify unsolicited marketing of other products.

Credit score data also triggers **Art. 20 (automated decision-making rights):** if you use scores to algorithmically select who receives which offer, the data subject can request:
- Review of automated decisions that affect their interests (human review, though ANPD/legislative debate continues on whether this must be human or can be a "meaningful review");
- Clear and adequate information about the criteria and procedures used, subject to trade-secret limits (though ANPD's stance, echoing GDPR, is that "trade secret" cannot be used to block all transparency).

## 4. Legal bases summary table

| Data type | Usable for marketing personalization? | Applicable basis |
|---|---|---|
| Health insurance data (sensitive) | Practically no | Only specific, highlighted opt-in consent (Art. 11, I) — and even then fails necessity/non-discrimination tests in most cases |
| Credit score (ordinary, regulated) | Conditionally yes, with limits | Consent (preferred) or narrowly-scoped, documented legitimate interest for existing customers only; contract basis only for the specific product requested |

## 5. Required safeguards if you proceed with credit-score-based personalization only

1. **Drop health data from the marketing/personalization use case entirely.** Segregate it technically (separate systems/access controls) from marketing and analytics pipelines to avoid function creep.
2. **Specific, granular, opt-in consent** for marketing use of credit-related data — separate from consent for account opening/underwriting, written in clear language (Art. 8, §4º prohibits generic consent).
3. **Data Protection Impact Assessment (Relatório de Impacto à Proteção de Dados Pessoais, Art. 38 / ANPD Resolution)** — especially given profiling of financial/credit data and potential impact on vulnerable populations. ANPD has signaled increased scrutiny of profiling for financial services.
4. **Legitimate Interest Assessment documentation** if relying on Art. 7º, IX for existing customers — must be filed/available for ANPD upon request (Art. 10, §2º) and must not use sensitive data.
5. **Transparency (Art. 9):** Clear privacy notice disclosing that credit score is used for marketing personalization, the logic involved, and how to opt out.
6. **Right to object / easy opt-out** from marketing processing at any time (Art. 18, IV and general marketing best practice, reinforced by CDC).
7. **Non-discrimination safeguards:** Document that credit-based personalization does not result in predatory targeting (e.g., steering financially vulnerable customers to high-cost credit products), which would violate both Art. 6º, IX and CDC vulnerability protections, and could draw BACEN/PROCON scrutiny.
8. **Automated decision-making transparency (Art. 20):** Provide a mechanism for customers to request review/explanation of how credit-based offers/scores were generated.
9. **Data minimization:** Use the minimum data/derived features necessary (e.g., a risk tier rather than granular credit history) rather than raw credit bureau data for marketing purposes.
10. **DPO (encarregado) involvement and vendor/DPA review** if credit score data comes from or is shared with third-party bureaus or marketing platforms — requires data processing agreements compliant with Art. 39/Art. 42.
11. **Retention limits:** Marketing use of credit data should have a defined retention period tied to purpose (Art. 15/16), not indefinite retention.
12. **Regular audit trail:** Keep records of consent, LIA, and DPIA for ANPD accountability requirements (Art. 6º, X — accountability principle) — ANPD can and does request these in enforcement actions.

## 6. Practical recommendation

- **Health insurance data:** Exclude it from marketing personalization use cases altogether. The combination of "sensitive data" classification, the closed list of Art. 11 legal bases (no legitimate interest available), and the non-discrimination principle makes this a high-risk, low-viability path. If there's a genuine health-adjacent product need (e.g., a health-linked insurance product), that would need to be its own tightly scoped, separately consented flow — not folded into general marketing personalization.
- **Credit score data:** Feasible only with specific consent (preferred) or a well-documented, narrow legitimate-interest basis limited to existing customers, backed by a DPIA/LIA, strong transparency, opt-out rights, and non-discrimination safeguards.
- Given BACEN's parallel regulatory interest in fintech conduct and the Consumer Defense Code's heightened protection for vulnerable consumers, treat this as a cross-functional legal/compliance review (LGPD + financial regulation + consumer protection), not a pure privacy-team sign-off. Engage your DPO and outside counsel before launching, and consider consulting ANPD guidance/regulations on profiling and sensitive data, which continue to evolve.

*This is general compliance guidance, not legal advice. Given the sensitive-data and financial-services overlap, formal legal review by Brazilian counsel is strongly recommended before implementation.*
