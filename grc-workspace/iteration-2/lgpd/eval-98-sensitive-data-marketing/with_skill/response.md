# Eval 98: Sensitive Data Marketing — With Skill Response

## Prompt
We are a São Paulo-based fintech. We want to use customers' health insurance data and credit scores to build personalized product recommendations and target marketing campaigns. Is this lawful under LGPD?

---

## Answer

**Short answer:** Using health insurance data for marketing is **not lawful under LGPD without explicit, specific consent** — and even with consent, the bar is high. Using credit scores for marketing is **legally uncertain and likely requires a legitimate interest assessment** that marketing purposes will often fail. A compliant path is possible but requires restructuring your approach.

---

### 1. Health Insurance Data Is Sensitive Personal Data (Art. 11)

Health insurance data is a subset of **health data**, which LGPD Art. 11 explicitly classifies as **sensitive personal data** (dado pessoal sensível). Sensitive personal data receives heightened protection and can only be processed under one of the following exhaustive bases under Art. 11:

**Art. 11, I — Express, specific consent:**
- The data subject must give **express consent** (affirmative, highlighted separately from other consents)
- Consent must be **specific to the processing purpose** — general terms-of-service consent is insufficient
- The purpose of "personalized product recommendations and targeted marketing" must be explicitly described and separately consented to

**Art. 11, II — Strict legal exceptions (no consent required):**
- (a) Compliance with a legal/regulatory obligation
- (b) Shared data by the data subject themselves with unrestricted publicity
- (c) Protection of the data subject's life or physical safety or that of a third party
- (d) Fraud prevention and data subject protection in credit operations
- (e) Health protection, in a procedure by a health professional or entity subject to professional secrecy
- (f) Scientific/historical research or statistical study (anonymised where possible)
- (g) Exercise of rights in judicial, administrative, or arbitration proceedings

**Marketing is not among the Art. 11, II exceptions.** There is no exception for "commercial product recommendation" or "targeted advertising." Therefore, **the only available legal basis for using health insurance data in marketing is express, specific consent (Art. 11, I).**

**Conclusion on health data:** You **cannot** use health insurance data for marketing without first obtaining express, highlighted, purpose-specific consent from each customer for that specific use. If you have not collected such consent, the planned use is **unlawful under LGPD Art. 11**.

---

### 2. Credit Scores Are Regular Personal Data — but Marketing Is Not the Right Fit

Credit scores are not listed among Art. 11 sensitive data categories, so they are processed as **regular personal data under Art. 7**. However, the applicable legal basis matters enormously:

**Art. 7, X — Credit protection:**
This legal basis authorises processing for **credit analysis and fraud/credit risk assessment**. The credit protection basis has a **specific and narrow purpose**: evaluating creditworthiness, preventing default, and protecting lenders/creditors. Using credit scores for **marketing personalisation** is a **purpose incompatible** with the credit protection legal basis under Art. 6, I (purpose limitation principle). You cannot rely on Art. 7, X for marketing.

**Art. 7, IX — Legitimate interest:**
The most likely alternative basis for using credit scores in marketing is **legitimate interest**. However, under LGPD Art. 7, §2º (applicable to online services) and Art. 6, IX, this requires a **balancing test**:

- **Controller's interest:** Personalising product recommendations to increase revenue
- **Data subject's interest and fundamental rights:** Privacy, autonomy over financial data, protection against discriminatory or intrusive profiling
- **Assessment:** Using financial data (credit scores) to build marketing profiles is generally considered **intrusive** and can cause harm (e.g., predatory targeting of financially vulnerable customers, discriminatory exclusion). The ANPD is likely to scrutinise this carefully, and the legitimate interest test is **not easy to pass** for marketing uses of financial data

**Legitimate interest assessment (LIA) is mandatory** before relying on this basis, and you must be able to demonstrate the balancing was conducted and the outcome favours processing. Many fintechs find that credit-score-based marketing fails this test.

---

### 3. Consent for Health Data: What "Express and Specific" Requires

If you decide to pursue the consent path for health data (Art. 11, I), LGPD Art. 8 and Art. 11 require:

| Requirement | What It Means in Practice |
|-------------|--------------------------|
| **Express** | Affirmative action (checkbox, signature, explicit confirmation) — no pre-ticked boxes, no implied consent |
| **Specific** | Consent for "health data use for product recommendation marketing" must be a **separate, highlighted consent** from your general privacy consent — Art. 11, §3º (consent must be highlighted separately) |
| **Free** | Customers cannot be denied the service if they refuse consent for marketing use |
| **Informed** | The consent must clearly explain what health data, for what marketing purposes, shared with whom |
| **Revocable** | Customers must be able to withdraw consent at any time at no cost; withdrawal triggers deletion (Art. 18, VI) |

**Bundled consent is invalid.** If your sign-up flow includes a single "I agree to the privacy policy" checkbox, that does not constitute valid express consent for health data marketing use.

---

### 4. Purpose Limitation: Credit Protection Legal Basis Cannot Extend to Marketing

To be explicit: Art. 7, X (credit protection) authorises processing for credit analysis. If you collected credit scores under this basis (e.g., for creditworthiness assessment for a loan product), you **cannot repurpose that data for marketing** without a separate legal basis. LGPD's purpose principle (Art. 6, I) requires that processing be limited to the declared, specific, legitimate purpose for which data was collected.

Using credit data collected for Art. 7, X purposes in marketing campaigns constitutes **secondary processing incompatible with the original purpose** — a violation of Art. 6, I.

---

### 5. Compliant Path Forward

Here is how to structure a lawful approach:

**Option A — Consent-based (health data):**
1. Design a **separate, highlighted consent request** specifically for "use of health insurance information for personalised product recommendations and targeted marketing campaigns"
2. Ensure consent is freely given — not conditioning core fintech services on this consent
3. Collect express opt-in before any health-data-based marketing processing begins
4. Implement consent management to record, timestamp, and support withdrawal
5. Build a deletion/suppression flow for customers who withdraw consent

**Option B — Redesign the recommendation engine (health data):**
- Exclude health insurance data from the recommendation and marketing logic entirely
- Use non-sensitive signals (product usage, purchase history, stated preferences) for personalisation
- This removes the Art. 11 compliance complexity entirely

**Option C — Credit scores (legitimate interest):**
1. Conduct a documented **Legitimate Interest Assessment (LIA)**
2. Define the specific marketing purpose and assess whether it is proportionate to the privacy intrusion
3. Implement an **opt-out mechanism** for data subjects (right to object under Art. 18, if applicable)
4. If the LIA shows the interest is not proportionate (likely for vulnerable customer segments), do not proceed on this basis; fall back to consent

**Option D — Anonymisation:**
- If health or credit data can be **genuinely anonymised** before use in recommendation models (i.e., re-identification is not reasonably possible), the processed output falls outside LGPD scope
- This is technically complex and must be validated — pseudonymisation is insufficient

---

### Risk Summary

| Activity | Lawful? | Required Action |
|----------|---------|-----------------|
| Using health insurance data for marketing **without consent** | **No** — Art. 11 violation | Stop immediately; obtain express specific consent before resuming |
| Using health insurance data for marketing **with express, specific, highlighted consent** | **Yes** (Art. 11, I) | Redesign consent flow; build consent management |
| Using credit scores for marketing under Art. 7, X (credit protection) | **No** — purpose mismatch | Cannot rely on this basis for marketing |
| Using credit scores for marketing under Art. 7, IX (legitimate interest) after a documented LIA | **Possibly** | Conduct LIA; implement opt-out; document; review with legal counsel |
| Anonymised aggregates of health/credit data for marketing models | **Possibly** | Validate true anonymisation; document process |

ANPD fines for unlawful processing of sensitive data (Art. 11 violation) are the same as general LGPD penalties — up to 2% of Brazilian revenue or R$50M per violation — but the reputational and regulatory exposure is heightened given the sensitivity of health data.
