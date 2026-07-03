# Eval 97: Deletion Request — With Skill Response

## Prompt
A Brazilian customer has requested deletion of all their personal data from our CRM system, email marketing platform, and analytics tool. How do we handle this under LGPD? Are there any exceptions?

---

## Answer

Handling a deletion request under LGPD requires a structured workflow that spans your internal systems and any processors (vendors) you use. Below is a complete step-by-step guide with timelines, downstream obligations, exceptions, and documentation requirements.

---

### 1. Controller → Processor Downstream Obligation

As the **controller**, you bear the primary obligation to respond to the data subject's deletion request. Crucially, this obligation extends to your **processors (operadors)**:

- **CRM system** — if operated by a third-party SaaS vendor, you must instruct them to delete the individual's records
- **Email marketing platform** — you must trigger deletion (or unsubscription + data erasure) through the platform's admin interface or API; deletion of consent-based data when consent is revoked is specifically mandated under Art. 18, VI
- **Analytics tool** — you must identify and delete (or anonymise) any personal data held there; note that truly anonymous data (irreversibly de-identified) falls outside LGPD scope, so anonymisation can be an alternative to deletion where full deletion is technically infeasible

Under Art. 42, §1º, processors who fail to follow controller instructions can be jointly liable. Your **Data Processing Agreements (DPAs)** with these vendors should already obligate them to support deletion requests — if they do not, update them.

**Practical step:** Send written deletion instructions to each processor contemporaneously with processing the request, retain confirmation from each processor that deletion was completed.

---

### 2. Response Timeframe: 15 Business Days

LGPD Art. 18 specifies that data subject rights must be honoured "without undue delay." ANPD guidance and resolutions indicate a **15-business-day** response window for deletion and access-type requests (consistent with the timeframe specified for full access reports).

| Milestone | Deadline |
|-----------|----------|
| Acknowledge the deletion request | As soon as possible (best practice: within 2–3 business days) |
| Verify identity of the requestor | Before processing; do not delete without confirming identity |
| Complete deletion across all systems (CRM, email, analytics) | Within **15 business days** of the verified request |
| Notify requestor of completion (or of any exceptions applied) | Within the 15-business-day window |

---

### 3. Exceptions to Deletion (Art. 16 LGPD)

LGPD does not require deletion in all circumstances. Art. 16 lists the cases where personal data may be **retained even after a deletion request**:

| Exception | Art. 16 Reference | Examples in Your Context |
|-----------|------------------|--------------------------|
| **Compliance with a legal or regulatory obligation** | Art. 16, I | Tax records, invoices, transaction records required by Brazilian tax law (Lei das Obrigações Tributárias) or anti-money laundering rules |
| **Transfer to third parties permitted by LGPD** | Art. 16, II | Sharing data with authorities pursuant to a lawful request |
| **Use by research entity, anonymised** | Art. 16, III | Anonymised analytics retained for statistical analysis (note: must be truly anonymised) |
| **Protection of the data subject's life or physical safety or that of a third party** | Art. 16, IV | Rare; not typically applicable to SaaS/CRM context |
| **Fraud prevention and credit protection** | Art. 16, V | Retention of fraud signals or blacklist records for fraud prevention purposes |
| **Protection through judicial, administrative, or arbitration proceedings** | Art. 16, VI | Retaining data needed to defend legal claims or comply with litigation holds |

**Practical notes:**
- For each exception you invoke, document **which specific article applies** and **why** it applies to the data in question
- Retain only the **minimum data necessary** for the excepted purpose; delete everything else
- Where you are retaining data under a legal obligation (e.g., financial records for 5 years under Brazilian tax law), inform the data subject of this in your response

---

### 4. Consent-Based vs. Other Legal Bases

The legal basis originally used to process the data affects the deletion obligation:

| Original Legal Basis | Deletion Obligation |
|---------------------|-------------------|
| **Consent (Art. 7, I)** | When consent is revoked (Art. 18, VI / Art. 8, §5º), personal data must be deleted without undue delay — this is a categorical right with very limited exceptions |
| **Contract (Art. 7, V)** | Data may be retained for as long as the contract requires (including post-contract legal retention periods); once those periods expire, deletion is required |
| **Legal obligation (Art. 7, II)** | Data must be retained for the duration of the legal obligation; deletion request creates no override of the legal duty |
| **Legitimate interest (Art. 7, IX)** | Must balance the data subject's interest in deletion against the controller's legitimate interest; in most cases, the data subject's right prevails absent a compelling overriding interest |
| **Credit protection (Art. 7, X)** | Data may be retained for fraud/credit purposes (Art. 16, V exception); duration must be proportionate |

**Key principle:** Consent-based marketing data is the clearest case for deletion — once the customer withdraws consent or requests deletion of consent-collected data, you must delete it from your CRM and email marketing platform. Data retained for legal obligations (e.g., invoices) can lawfully be kept.

---

### 5. Documenting the Request for ANPD Accountability

Under LGPD's accountability principle (Art. 6, X and Art. 50), controllers must be able to **demonstrate compliance**. For each deletion request:

1. **Log the request** — timestamp, channel received, identity verification steps taken
2. **Record the action taken** — which data was deleted, from which systems, on which dates
3. **Record any exceptions applied** — which Art. 16 exception, what data was retained and why
4. **Record processor confirmations** — written confirmation from CRM, email platform, analytics vendor that deletion was completed
5. **Record the response sent to the data subject** — what you told them and when

This documentation is your evidence file if the ANPD investigates a complaint from this data subject. Retain the documentation record for at least as long as is required by applicable record-keeping obligations (typically 5 years for Brazilian commercial records).

---

### Summary Workflow

```
1. Receive deletion request
2. Verify requestor identity
3. Identify all personal data in scope (CRM, email platform, analytics)
4. Apply Art. 16 exceptions test — what, if anything, must be retained?
5. Issue deletion instructions to processors (CRM vendor, email platform, analytics tool)
6. Delete (or anonymise) remaining data
7. Confirm deletion with processors
8. Respond to data subject within 15 business days:
   - Confirm what was deleted
   - Explain any Art. 16 exceptions invoked and what data was retained
9. Log everything in your accountability records
```

Under LGPD, the right to deletion applies most forcefully to consent-based processing. Where you process under a legal obligation or contract, the Art. 16 exceptions protect you — but only for the minimum data and duration necessary.
