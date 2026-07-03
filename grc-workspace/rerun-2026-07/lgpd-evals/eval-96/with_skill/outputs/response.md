## Does LGPD apply to you?

**Yes.** LGPD applies to your company even though you're a US-based SaaS provider with no physical presence in Brazil.

Under **Art. 3**, LGPD applies to any processing of personal data of individuals located in Brazil, regardless of where the controller is established, when any of the following is true:
- Processing occurs in Brazil
- The purpose is to offer goods/services to individuals in Brazil
- Personal data was collected in Brazil

You have Brazilian customers using your app — meaning you're offering services to individuals in Brazil and collecting their personal data. This is **extraterritorial reach**, similar to GDPR Art. 3, and it applies squarely to your situation. None of the Art. 4 exemptions (personal/household use, journalistic/artistic/academic, national security, public safety, criminal investigation) apply to a commercial SaaS product.

**Bottom line:** As a foreign company targeting/serving Brazilian users, you are subject to LGPD as a **controller** for the personal data of your Brazilian customers.

---

## Data inventory and classification

| Data Element | Classification |
|---|---|
| Name | Regular personal data |
| Email | Regular personal data |
| CPF (Cadastro de Pessoas Físicas — Brazilian taxpayer ID) | Regular personal data (a unique national identifier — treat with heightened care operationally, but it is **not** "sensitive data" under Art. 11's closed list) |
| Purchase history | Regular personal data |

Note: LGPD's sensitive data category (Art. 11) is limited to racial/ethnic origin, religion, political opinion, trade union membership, health/sexual life data, and genetic/biometric data. CPF and purchase history don't fall into that list, so **Art. 7** (not the stricter Art. 11) governs your legal basis analysis. That said, CPF is a high-value identifier for fraud/identity theft, so it merits strong security controls even though it isn't legally "sensitive" under LGPD.

---

## Legal basis analysis (Art. 7)

Since none of this is sensitive data, you map each processing activity to one of the **10 legal bases in Art. 7**. For a typical SaaS billing/account relationship, the following bases are most likely applicable:

### 1. Contract — Art. 7, V (primary basis for most of your processing)
**Key requirement:** Processing necessary for the performance of a contract or pre-contractual procedures at the data subject's request.

- **Name, email:** Necessary to create an account, authenticate the user, and deliver the service — squarely contract-based.
- **CPF:** If CPF is collected because Brazilian tax/invoicing law or payment processors require it to bill Brazilian customers, this is also justified under **Contract (Art. 7, V)**, and potentially reinforced by **Legal obligation (Art. 7, II)** if a specific regulation mandates CPF collection for invoicing (e.g., Nota Fiscal requirements).
- **Purchase history:** Necessary to fulfill the contract (order records, subscription management, support) — Contract basis applies.

### 2. Legal obligation — Art. 7, II (supporting basis, likely for CPF)
**Key requirement:** Processing required by law or regulation.

- Brazilian tax and consumer protection rules often require CPF on invoices/receipts for B2C transactions. If that's why you collect CPF, document this as a **secondary/reinforcing basis** alongside Contract.

### 3. Legitimate interest — Art. 7, IX (for ancillary purposes only)
**Key requirement:** Controller's legitimate interest, provided it doesn't override the data subject's fundamental rights and freedoms; requires a documented balancing test (LIA).

- Could support secondary uses like fraud prevention, service improvement analytics on purchase history, or churn analysis — but **not** as the primary basis for core account/billing data, since Contract already covers that more cleanly.
- If used, you must conduct and document a legitimate interest balancing test.

### 4. Consent — Art. 7, I (only where processing exceeds contract necessity)
**Key requirement:** Free, informed, unambiguous, specific, documented, and revocable at any time.

- Only needed for processing that goes **beyond** what's necessary to perform the contract — e.g., marketing emails using purchase history to build product recommendations shared with third parties, or cross-selling communications. Don't rely on consent for core account operation; Contract is the cleaner, more defensible basis and avoids the operational burden of consent withdrawal disrupting service delivery.

### What does NOT apply here
Public policy execution (III), research (IV), judicial/regulatory proceedings (VI), vital interests (VII), health protection (VIII), and credit protection (X) are not relevant to a standard SaaS billing/account data flow.

---

## Recommended basis mapping

| Data Element | Primary Purpose | Recommended Legal Basis | Article |
|---|---|---|---|
| Name, email | Account creation, service delivery | Contract | Art. 7, V |
| CPF | Invoicing/tax compliance | Contract + Legal obligation | Art. 7, V (+ II if mandated by tax law) |
| Purchase history | Order fulfillment, billing, support | Contract | Art. 7, V |
| Purchase history (if used for marketing/analytics/profiling) | Product recommendations, marketing | Legitimate interest (with LIA) or Consent | Art. 7, IX or Art. 7, I |

---

## Practical next steps

1. **Document each basis in your Records of Processing Activities (RoPA)** and reflect it in your privacy notice (Art. 9), including basis, purpose, retention period, and whether data is shared with third parties.
2. **Appoint or designate a DPO/Encarregado (Art. 41)** — publish name and contact info. Small-scale operators may be exempt from formal appointment under ANPD Resolution CD/ANPD 2/2022 but must still provide a contact channel; assess whether your Brazilian customer volume qualifies.
3. **Confirm international transfer mechanism (Art. 33–36)** — since you're a US company, personal data flowing from Brazil to your US infrastructure is an international transfer to a **non-adequate country** (the January 2026 Brazil-EU mutual adequacy decision does not cover the US). You'll need **standard contractual clauses (SCCs)** or another Art. 33 mechanism for Brazil→US transfers — this is a distinct compliance gap from the legal basis question and should be addressed in your data processing agreements and privacy notice.
4. **If relying on legitimate interest** for any secondary use of purchase history, complete and document a balancing test (LIA).
5. **Update your privacy notice** to disclose purpose, legal basis, CPF handling, retention, and the US transfer mechanism to Brazilian customers per Art. 9.

---

*LGPD vs. GDPR note: LGPD's legal basis list (10 bases, Art. 7) is broader than GDPR's 6 (Art. 6) — notably adding credit protection and public policy execution — but Contract, Legal Obligation, Legitimate Interest, and Consent operate analogously to their GDPR counterparts, so if you already have a GDPR Art. 6 mapping for this data, it will closely mirror the Art. 7 mapping above.*
