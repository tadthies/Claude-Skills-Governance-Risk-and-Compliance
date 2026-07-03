# International Data Transfer to the US — LGPD Compliance Analysis

Transferring Brazilian customer data to your parent company's US servers is an **international data transfer** under LGPD Chapter V (Arts. 33–36). Because the **United States has no ANPD adequacy decision**, the adequacy pathway (available for EU/EEA transfers since the January 2026 Brazil-EU mutual adequacy recognition) is **not available to you**. You must rely on one of the other Art. 33 mechanisms.

---

## 1. Available Transfer Mechanisms (Art. 33)

| Mechanism | LGPD Basis | Fit for US Parent-Company Transfer |
|-----------|-----------|-------------------------------------|
| **Adequacy decision** | Art. 33, I / Art. 34 | **Not available** — US has no ANPD adequacy decision |
| **Standard/specific contractual clauses (SCCs)** | Art. 33, II / Art. 35 | **Recommended** — most common mechanism for intragroup transfers to non-adequate countries |
| **Global corporate standards / Binding Corporate Rules (BCRs)** | Art. 33, II / Art. 35, I | **Strong fit** — designed for intragroup/intercompany transfers like this one; requires ANPD authorization |
| **Specific consent** | Art. 33, VIII | Usable as a supplementary or fallback basis, but **not scalable** — must be specific to the transfer, separate from other consents, and freely revocable |
| **Legal/regulatory cooperation** | Art. 33, IV–VII | Not applicable — this is a private intragroup commercial transfer |
| **Vital interests** | Art. 33, VII | Not applicable — emergency-only basis |
| **ANPD case-by-case authorization** | Art. 33, IX | Fallback only if no other mechanism fits |

**Recommendation:** For an intragroup, ongoing, systematic transfer of customer data from a Brazilian subsidiary to a US parent, the two realistic mechanisms are:

- **Standard Contractual Clauses (SCCs)** under Art. 35 — faster to implement, especially if ANPD has not yet published its own standard clauses (in which case controller-drafted specific clauses providing adequate protection can be used); or
- **Binding Corporate Rules (BCRs)** under Art. 35, I — better suited to your situation since this is an intercompany/intragroup transfer, but requires ANPD review and authorization, which adds lead time.

Note: As of the ANPD's published guidance, ANPD has not yet issued its own standard contractual clause templates — controllers may need to use specific contractual clauses that demonstrably provide an adequate level of protection consistent with LGPD principles (Art. 35), often modeled on GDPR-style SCC provisions since GDPR SCCs are the market-accepted template, adapted for LGPD requirements.

---

## 2. What You Need to Implement

### A. Choose and execute the legal transfer mechanism
1. **Contractual clauses (fastest path):**
   - Draft or adopt intragroup data transfer clauses covering: categories of data transferred, purposes, security obligations, data subject rights guarantees, sub-processing restrictions, audit rights, and liability allocation.
   - Ensure clauses guarantee a level of protection equivalent to LGPD (Art. 35) — not just US law, since the US offers no equivalent statutory baseline.
   - Execute between the Brazilian entity (as controller/exporter) and the US parent (as importer — controller or processor depending on the role it plays).
2. **BCRs (if group-wide, recurring transfers):**
   - Draft binding corporate rules covering all intragroup transfers of personal data (not just Brazil→US).
   - Submit to ANPD for authorization — build this lead time into your rollout plan, as ANPD review timelines are not guaranteed to be short.
   - BCRs are the more durable/scalable solution if the US parent will be a recurring or permanent recipient of data from multiple Brazilian data flows.

### B. Governance and documentation
3. **Update the Record of Processing Activities (RoPA — Art. 37):** Add the Brazil→US transfer as a distinct processing activity, noting the legal basis for transfer (contractual clauses/BCRs), data categories, recipients, and purpose.
4. **Update the privacy notice (Art. 9):** Disclose that data is transferred internationally to the US, name the mechanism used (contractual clauses/BCRs — not adequacy), and identify the recipient (parent company).
5. **Conduct a transfer risk assessment / DPIA (RIPD, Art. 38):** Given the US has no adequacy decision and US surveillance/access laws are a known ANPD concern area, document the risk assessment, especially if sensitive personal data (Art. 11) is involved — sensitive data transfers may draw additional ANPD scrutiny (Art. 36 complementary requirements).
6. **Confirm the legal basis for the underlying processing (Art. 7):** The transfer mechanism (Art. 33) is separate from — and additional to — the Art. 7 legal basis for processing the data itself (e.g., contract, legitimate interest, consent). Both must be satisfied.

### C. Security and accountability
7. **Security measures (Art. 46):** Ensure the US parent implements technical and administrative safeguards equivalent to what would be required in Brazil (encryption in transit/at rest, access controls, logging). The Brazilian controller remains responsible for the processor's/recipient's security posture.
8. **DPO involvement (Art. 41):** The Encarregado should review and sign off on the transfer mechanism and be listed as the contact point in the updated privacy notice.
9. **Complementary safeguards for sensitive data (Art. 36):** If any transferred data qualifies as sensitive personal data (health, biometric, etc.), expect ANPD to potentially require additional safeguards beyond the base contractual clauses.

### D. If none of the above is feasible in the short term
10. **Specific consent (Art. 33, VIII)** can serve as an interim/fallback mechanism: it must be captured separately from other consents, clearly inform the data subject that data will be transferred internationally to the US, name the recipient, and be freely revocable. This is generally not recommended as your primary long-term mechanism due to scalability and revocability risk (a wave of revocations could disrupt data flows), but can bridge the gap while SCCs/BCRs are finalized.

---

## 3. Practical Sequencing Recommendation

| Step | Action | Priority |
|------|--------|----------|
| 1 | Legal/DPO review to select contractual clauses vs. BCRs based on transfer scope and duration | High |
| 2 | Draft and execute intragroup contractual clauses (Art. 35) as the near-term mechanism | High |
| 3 | Update RoPA and privacy notice to reflect the US transfer and mechanism used | High |
| 4 | Conduct DPIA/RIPD for the transfer, especially if sensitive data is included | Medium |
| 5 | Evaluate long-term BCR submission to ANPD if transfers will be recurring/group-wide | Medium |
| 6 | Verify US parent's security controls match Art. 46 expectations | High |
| 7 | Train relevant staff and document accountability measures (Art. 47) | Medium |

---

## Key Takeaway

Because the US lacks an ANPD adequacy decision, you **cannot rely on adequacy** (unlike the Brazil-EU pathway now available since January 2026). You must implement **contractual clauses or BCRs** (Art. 35) as your primary mechanism, backed by RoPA/privacy notice updates, a transfer risk assessment, and verified security controls at the US recipient — with specific consent as only a limited, non-scalable fallback (Art. 33, VIII).
