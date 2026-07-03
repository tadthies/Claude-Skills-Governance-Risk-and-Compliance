## Short answer

**No — not as described.** Using health insurance data to profile customers for personalised financial-product marketing is very likely **unlawful under LGPD** unless you substantially change your legal basis and design. You are mixing two high-risk categories:

- **Health data** = **sensitive personal data** (Art. 5, II) — subject to the strict regime of **Art. 11**, where **legitimate interest is expressly prohibited** (Art. 10, §2º / recognised restriction under Art. 11).
- **Credit scores** = ordinary personal data, but Art. 7, X specifically contemplates a **"credit protection"** basis — which is about credit risk/analysis, **not marketing**.

Neither basis you'd naturally reach for is enough on its own to cover marketing personalised financial products off the back of health data. Below is the basis-by-basis analysis.

---

## Legal Basis Analysis

### 1. Health insurance data → Sensitive Personal Data (Art. 5, II; Art. 11)

Health data is explicitly listed as sensitive personal data under **Art. 5, II**. Under **Art. 11**, sensitive data may only be processed on one of these grounds:

| Art. 11 basis | Available for marketing use here? |
|---|---|
| Express, specific, highlighted consent | **Yes — only viable route**, but must be separate from any other consent and cannot be bundled with general T&Cs |
| Legal obligation | No |
| Public policy (by public entity) | No |
| Research by research bodies (anonymised) | No — not applicable to commercial marketing |
| Exercise of rights in judicial/administrative/arbitral proceedings | No |
| Protection of life/physical safety | No |
| Health care by health professionals/authorities/services | No — marketing is not health care provision |
| Fraud prevention / data subject's safety | No |
| Credit protection | **No — Art. 11 explicitly excludes legitimate interest, and "credit protection" as a ground for sensitive data is narrowly tied to credit risk analysis, not marketing** |

**Key point (Art. 10, §2º / Art. 11 structure):** Legitimate interest (Art. 7, IX) — which many companies default to for marketing — **cannot be used for sensitive data at all**. This closes off the most common marketing basis entirely for the health insurance component of your processing.

**Conclusion:** The *only* lawful basis for using health insurance data in marketing is **express, specific, and highlighted consent** (Art. 11, I, read with Art. 8). This consent:
- Must be **separate and distinguishable** from consent to other processing (e.g., cannot be folded into "accept our privacy policy" or account opening T&Cs)
- Must **specifically name** the use of health data for marketing/product personalisation purposes
- Must be **freely given** — cannot be a condition of using the core financial product/account (Art. 8, §2º-equivalent: cannot condition service on non-necessary consent)
- Must be **easily revocable**, with revocation not degrading the core service
- Carries the **burden of proof on the controller** — you must be able to demonstrate valid consent was obtained

### 2. Credit scores → Regular Personal Data, but purpose-limited

Credit score data is regular (non-sensitive) personal data, and Art. 7, X gives you a specific basis — **"credit protection, including credit analysis and risk of default"**. However:

- This basis is scoped to **credit risk/underwriting purposes**, not to marketing or cross-sell/upsell of financial products. Using it to justify targeted product marketing would likely fail the **purpose limitation** and **adequacy** principles (Art. 6, I–II) — processing must remain compatible with the purpose originally declared to the data subject.
- **Legitimate interest (Art. 7, IX)** is theoretically available for marketing of *non-sensitive* data such as credit scores (this is a common basis for direct marketing under LGPD, similar to GDPR), **but only if**:
  - A documented **balancing test** is conducted (Art. 10) showing the marketing interest does not override the data subject's fundamental rights
  - The processing is within the data subject's **reasonable expectation** — e.g., existing customers might reasonably expect product offers; prospects whose credit data was obtained from a bureau for scoring, then repurposed for marketing, likely would not
  - It is properly documented in the **Legitimate Interest Assessment (LIA)** and RoPA

### 3. The combination problem

Even if you had a valid legitimate-interest basis for the credit-score component, **you cannot use legitimate interest to "unlock" the health data half of the same profile**. Because health insurance data is sensitive, its inclusion in the profiling/targeting logic requires **Art. 11 express consent independently** — you cannot bootstrap sensitive data into a marketing use case via a non-sensitive basis. If your personalisation engine combines both data types (e.g., "customer has diabetes-related health coverage + high credit score → offer product X"), the **entire combined processing activity is governed by the stricter sensitive-data regime**, and consent becomes mandatory for the whole activity, not just the health field.

### 4. Additional risk: discrimination and profiling

- **Art. 6, IX (Non-discrimination principle):** Processing cannot be carried out for unlawful or abusive discriminatory purposes. Using health data (e.g., pre-existing conditions inferred from insurance data) to target or exclude customers from financial products/pricing raises serious non-discrimination exposure — and would likely also implicate Brazilian consumer protection law (Art. 45 LGPD explicitly preserves the Consumer Protection Code) and potentially anti-discrimination/insurance regulatory rules (SUSEP/BACEN oversight for fintechs).
- **Art. 20 (automated decisions):** If product personalisation/pricing is driven by automated profiling, customers have the right to request **review of automated decisions**, and you must be able to explain the criteria/logic used (including whether health/credit data influenced the outcome).

---

## Required Safeguards If You Proceed

If the business proceeds with this use case, the following controls are necessary as a minimum:

| Safeguard | Requirement |
|---|---|
| **Separate, granular consent for health data marketing use** | Art. 11, I / Art. 8 — highlighted, specific, opt-in, not bundled, freely revocable, documented (burden of proof on controller) |
| **Legitimate Interest Assessment (LIA) for credit-score-based marketing (non-sensitive component only)** | Art. 10 — documented balancing test; must show reasonable expectation and no override of data subject rights |
| **Strict purpose separation in RoPA** | Art. 37 — document health data (consent-based) and credit score (Art. 7,X / LI-based) as distinct processing activities with distinct bases, not commingled under one generic "marketing" entry |
| **DPIA / RIPD before launch** | Art. 38 — mandatory given sensitive data + profiling + financial products; ANPD can require disclosure |
| **Non-discrimination review** | Art. 6, IX — test personalisation/pricing logic for proxy discrimination based on health status |
| **Automated decision transparency + human review channel** | Art. 20 — disclose profiling logic; provide review mechanism |
| **DPO (Encarregado) sign-off** | Art. 41 — DPO should review this use case given sensitive-data + financial-services risk profile |
| **Privacy notice update** | Art. 9 — clearly disclose health data use, legal basis (consent), credit-score use, legal basis (Art. 7,X/LI), and any profiling/automated decision-making |
| **Security measures proportional to risk** | Art. 46 — sensitive financial + health data combined is high-risk; encryption, access controls, and audit logging expected |
| **Consent withdrawal must not degrade core banking/insurance service** | Art. 8 — marketing consent withdrawal cannot affect the customer's ability to use the core financial product |
| **Regulatory overlay** | Confirm alignment with BACEN (Central Bank) and, if applicable, SUSEP rules on data use in financial/insurance products, in addition to LGPD |

---

## Recommendation

1. **Do not use health insurance data for marketing personalisation without obtaining separate, express, highlighted consent** under Art. 11, I. Do not rely on legitimate interest for this component — it is not legally available.
2. For the **credit score** component alone, legitimate interest may be viable for existing customers with a documented LIA, but **cannot be blended with sensitive health data** in the same processing activity without triggering the consent requirement for the whole activity.
3. Conduct a **DPIA/RIPD** before launch given the sensitive-data + financial-profiling risk profile, and have your DPO formally review the use case.
4. Consider whether the marketing objective can be achieved with **less sensitive proxies** (e.g., product category interest, stated preferences) rather than raw health insurance data — this better aligns with the **necessity and data minimisation principles (Art. 6, III)** and substantially reduces regulatory and reputational risk.
