# PDPL Gap Analysis — Singapore SaaS Company Serving Vietnamese Customers

Below is a gap analysis against Vietnam's Personal Data Protection Law (PDPL, Law No. 91/2025/QH15, effective 1 January 2026) and its implementing decree (which builds on the earlier Decree 13/2023/ND-CP framework), based on the facts you've described.

## Scope Trigger

Vietnam's data protection framework applies extraterritorially. Because you process personal data of individuals in Vietnam (your Vietnamese customers) even though your company is based in Singapore and data is stored in Singapore, you are very likely in scope. Location of storage/processing does not exempt you — what matters is that data subjects are in Vietnam.

## Gap-by-Gap Analysis

### 1. Data Collected: Names, Emails, Payment Data
- Names and emails are "personal data."
- Payment data may qualify as, or be linked to, "sensitive personal data" under Vietnamese rules (financial information is generally treated as sensitive, similar to Decree 13's categorization of financial/banking data as sensitive personal data).
- **Gap:** Sensitive personal data typically requires a heightened basis for processing, and may require notifying/registering impact assessment dossiers with the Ministry of Public Security (MPS) — the primary regulator for data protection in Vietnam.
- **Action:** Classify payment data explicitly as sensitive personal data and apply enhanced safeguards (encryption, access controls, tokenization) and reassess your lawful basis.

### 2. Consent via Pre-Ticked Checkbox
- **Major Gap.** Vietnamese law requires consent to be a clear, affirmative, freely given, specific, and informed act. Pre-ticked boxes (i.e., default opt-in / passive consent) are not considered valid consent — this mirrors GDPR-style standards that Vietnam's regime has adopted.
- Silence or inaction also does not constitute consent.
- **Action:** Replace pre-ticked checkboxes with an unticked, opt-in mechanism requiring an active step (click, signature, verbal confirmation logged appropriately). Ensure consent is granular (separate consents for marketing vs. core service processing) and that you can produce evidence of consent (timestamp, version of notice shown, IP/device where feasible).

### 3. Data Stored in Singapore (Cross-Border Transfer)
- **Gap.** Transferring/storing Vietnamese citizens' personal data outside Vietnam is a regulated cross-border transfer. Vietnam's framework (carried over from Decree 13 and expanded under the PDPL) requires a Transfer Impact Assessment (TIA) dossier to be prepared and, in many cases, filed with the Ministry of Public Security within a specified period after processing begins (historically 60 days under Decree 13), and made available upon request.
- The dossier must cover: description of the data, purpose, recipient organization, safeguards, and a self-assessment of the receiving jurisdiction's protections.
- **Action:** Prepare and file a cross-border transfer impact assessment dossier with the MPS (or the successor authority under the PDPL). Maintain it as a living document. Consider whether a local processing/storage option is needed for high-risk data categories.

### 4. No DPO
- **Gap.** Depending on the scale and sensitivity of processing, Vietnam's regime requires appointment of a Data Protection Officer or a specialized data protection department/personnel, particularly where sensitive personal data (like payment data) is processed at scale or where the entity is a data controller/processor handling significant volumes of personal data. Foreign entities offering services to individuals in Vietnam are also generally expected to identify a responsible contact for data protection matters in Vietnam.
- **Action:** Appoint a DPO or designated data protection contact person, and consider whether a local representative in Vietnam is needed given you have no local establishment.

### 5. No Data Protection Impact Assessment (DPIA)
- **Gap.** Both a general Data Protection Impact Assessment (covering your overall processing activities) and — separately — a Cross-Border Data Transfer Impact Assessment are required documents under the Vietnamese framework. These are expected to be prepared before processing begins (or promptly thereafter) and kept updated, with the MPS able to request them for review.
- **Action:** Conduct and document a DPIA covering: categories of data, purposes, legal basis, retention periods, security measures, and risks to data subjects. File/register as required and retain for regulator inspection.

## Summary Table

| Area | Current State | Requirement | Gap Severity |
|---|---|---|---|
| Consent | Pre-ticked checkbox | Explicit, opt-in, granular, evidenced | High |
| Sensitive data handling (payment) | Not specifically classified | Enhanced safeguards + possible MPS notification | High |
| Cross-border storage (Singapore) | No transfer assessment | TIA dossier prepared/filed with MPS | High |
| DPO / responsible person | None | Appointment required for qualifying processing | Medium-High |
| DPIA | Never conducted | Required before/at start of processing | High |
| Local representative | Unclear | Likely needed for extraterritorial offering of services | Medium |

## Recommended Immediate Priorities
1. Fix consent mechanism (quick win, high risk reduction).
2. Conduct a DPIA and cross-border transfer impact assessment.
3. Classify payment data as sensitive and apply additional controls.
4. Appoint a DPO/data protection contact and evaluate need for a Vietnam-based representative.
5. Build a data inventory/register mapping data flows from Vietnamese customers into your Singapore systems.

## Important Caveat
Vietnam's PDPL and its implementing decree are newly in force as of 2026, and specific procedural details (exact filing deadlines, thresholds, forms) may be refined by subsequent guidance from the Ministry of Public Security. This analysis reflects the general framework and principles as understood; you should confirm current procedural specifics (e.g., exact TIA filing deadlines, DPO appointment thresholds) with qualified Vietnamese legal counsel before finalizing your compliance program.
