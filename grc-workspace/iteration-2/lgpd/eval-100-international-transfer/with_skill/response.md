# Eval 100: International Transfer — With Skill Response

## Prompt
We need to transfer personal data of Brazilian customers to our parent company's servers in the EU (Germany). What transfer mechanism do we need under LGPD? Also, we want to also transfer some data to our US-based analytics vendor. What do we need for that?

---

## Answer

These two transfers require fundamentally different mechanisms under LGPD — the EU transfer has been dramatically simplified by the January 2026 mutual adequacy decision, while the US transfer still requires contractual safeguards. Here is the full analysis.

---

### 1. Brazil → EU (Germany): Adequacy Decision — No SCCs or BCRs Required

**On January 26–27, 2026**, Brazil and the European Union established **mutual adequacy recognition**:

- Brazil's ANPD adopted an **adequacy decision recognising the EU/EEA** as a jurisdiction that provides equivalent protection to LGPD — meaning the EU's data protection framework (GDPR) meets LGPD's adequacy standard
- Simultaneously, the European Commission adopted a **reciprocal adequacy decision for Brazil** under GDPR Art. 45

**Practical consequence for your Germany transfer:**

Under LGPD Art. 33, I, personal data may be transferred internationally to a **country or international body that provides an adequate level of protection** as recognised by the ANPD. Since the EU/EEA is now on the ANPD's adequate jurisdictions list, **no additional transfer mechanism is required** for Brazil → Germany (or any EU/EEA member state) data flows.

**You do NOT need:**
- Standard Contractual Clauses (SCCs)
- Binding Corporate Rules (BCRs)
- Specific data subject consent for the transfer
- ANPD case-by-case approval

**The transfer is lawful simply by virtue of the adequacy decision.** The transfer mechanism in your Records of Processing Activities (RoPA) and privacy notice should be updated to reference "adequacy decision" for EU recipients.

---

### 2. Required Compliance Updates for the EU Adequacy Transfer

While the adequacy decision eliminates SCCs/BCRs, you still need to update your compliance documentation:

| Update Required | What to Do |
|----------------|-----------|
| **Records of Processing Activities (RoPA)** | Update the "transfer mechanism" column for all EU/EEA recipients from "SCCs" or "BCRs" to "ANPD adequacy decision (EU/EEA, as of January 2026)" |
| **Privacy notice / política de privacidade** | Update the international transfers section to state that data transferred to EU/EEA recipients is covered by the ANPD adequacy decision — remove any references to SCCs or BCRs for EU transfers |
| **Existing transfer agreements** | Review and remove (or annotate as superseded) any SCCs or BCRs in contracts with your EU parent company — these are no longer required and maintaining them alongside the adequacy mechanism creates unnecessary complexity |
| **Intragroup transfer agreements** | Update to reflect that the Brazil → EU transfer relies on adequacy; keep the agreements in place as good governance documents but remove SCC annexes |

**Do not discard the underlying data sharing / intragroup agreement** with your parent company — it is still good practice and may be required under LGPD Art. 37 for RoPA documentation purposes. Simply update it to remove SCC schedules.

---

### 3. Brazil → US (Analytics Vendor): No Adequacy — SCCs or Other Mechanism Required

The United States does **not** have an adequacy decision from Brazil's ANPD. Therefore, the Brazil → US transfer to your analytics vendor **requires a transfer mechanism** under LGPD Art. 33–35.

**Available mechanisms for non-adequate countries (LGPD Art. 33–35):**

| Mechanism | Art. | Applicable to Your US Analytics Transfer? |
|-----------|------|------------------------------------------|
| **Standard contractual clauses** | Art. 35, I | **Yes — primary recommended mechanism** for controller → processor transfers |
| **Binding corporate rules (BCRs)** | Art. 35, II | Yes, if the analytics vendor is part of your group — uncommon for external vendors |
| **Specific data subject consent** | Art. 33, VIII | Technically available but impractical for routine analytics transfers; consent must be specific and informed about the international transfer |
| **ANPD authorisation** | Art. 33, IX | Case-by-case approval from ANPD; reserved for unusual situations |
| **Vital interests** | Art. 33, VII | Emergency situations only; not applicable here |

**For a Brazil → US analytics vendor transfer, the practical mechanism is standard contractual clauses (Art. 35, I).**

---

### 4. Standard Contractual Clauses for US Transfers: What They Must Cover

LGPD Art. 35 specifies that contractual clauses used as transfer mechanisms must **guarantee a level of protection of personal data equivalent to that provided by LGPD**. ANPD has issued (or is expected to issue) approved clause templates, but you may also negotiate bespoke contractual protections.

Your Data Processing Agreement (DPA) with the US analytics vendor should include:

| Clause | Requirement |
|--------|------------|
| **Processing purpose limitation** | Vendor may only process data for the specified analytics purpose; no secondary use |
| **Sub-processor controls** | Vendor must obtain controller approval before engaging sub-processors; sub-processors must be bound by equivalent obligations |
| **Data subject rights support** | Vendor must assist controller in responding to Art. 18 data subject requests (access, deletion, portability) |
| **Security measures** | Vendor must maintain technical and administrative security measures appropriate to the risk |
| **Breach notification** | Vendor must notify controller of any security incidents without undue delay so controller can meet its 3-working-day ANPD notification obligation |
| **Return/deletion on termination** | On contract termination, vendor must return or delete all personal data |
| **Audit rights** | Controller must have the right to audit or request certifications regarding vendor's data protection practices |
| **Governing law / liability** | Clauses must be governed and enforceable; vendor must agree to jurisdiction for LGPD compliance purposes |

**Use ANPD-approved clause templates where available** — check anpd.gov.br for the current approved templates. Where templates are not yet published for your specific scenario, negotiate contractual protections that meet the LGPD equivalence standard.

---

### 5. Review Existing EU Transfer Agreements

As a practical action item following the January 2026 adequacy decision:

1. **Identify all existing contracts with EU/EEA entities** that contain SCC schedules or BCR references for Brazil → EU transfers
2. **Amend or annotate** those agreements to reflect that the transfer now relies on the ANPD adequacy decision rather than SCCs/BCRs
3. **Update your RoPA** to reflect the mechanism change
4. **Update your privacy notice** — particularly any disclosures to Brazilian data subjects about where their data is transferred and under what mechanism
5. **Retain the base data sharing agreements** (without the SCC schedules) as underlying governance documents

This cleanup avoids the confusion of having stale SCC language that may impose unnecessary obligations (e.g., data subject third-party beneficiary rights under SCCs) that are no longer necessary.

---

### Summary Table

| Transfer | Destination | Adequacy? | Required Mechanism | Action Needed |
|----------|------------|-----------|-------------------|---------------|
| Brazil → Germany (parent company) | EU/EEA | **Yes** (ANPD decision, Jan 2026) | **None** — adequacy applies | Update RoPA and privacy notice; remove SCC/BCR from transfer agreements |
| Brazil → US (analytics vendor) | United States | **No** | **Standard contractual clauses** (Art. 35, I) or BCRs, specific consent, or ANPD authorisation | Ensure DPA with vendor contains LGPD-equivalent contractual protections; use ANPD-approved clause templates |

The January 2026 Brazil-EU mutual adequacy decision is a significant simplification for companies with EU-based infrastructure or parent companies — you can now transfer data to Germany freely, provided you have a lawful legal basis for the underlying processing. For the US, contractual safeguards remain essential.
