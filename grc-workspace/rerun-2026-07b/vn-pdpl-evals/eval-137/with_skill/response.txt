# Breach Notification Workflow — Vietnam PDPL (Fintech, Ho Chi Minh City)

As a fintech handling customer personal data — including financial/banking data, which is classified as **sensitive personal data** under Decree 356 Article 4(7) — you are subject to both the general VN-PDPL breach rules (Law No. 91/2025/QH15, Article 23) and the finance-sector-specific overlay in Decree 356 Article 8. Here is the full workflow.

## 1. Contain (Immediate)

- Isolate affected systems, revoke compromised credentials, and stop the ongoing exposure before anything else.
- Preserve forensic evidence (logs, timestamps, access records) — you will need this for both notification content and your internal breach register.

## 2. Assess (Immediately, in parallel with containment)

Determine:
- **Scope:** number of data subjects affected (approximate is acceptable initially)
- **Data categories affected:** distinguish basic personal data (name, email, phone, etc.) from **sensitive personal data** (bank account numbers, credit card details, transaction/credit history, biometric data if applicable). Given this is a fintech breach, assume sensitive financial data is involved unless confirmed otherwise — this raises the severity and notification obligations.
- **Number of records** affected
- **Root cause** (to the extent known at this stage)

## 3. Notify — Who and By When

### A. Notify the Ministry of Public Security (the PDPL authority)
- **Deadline: within 72 hours of your organisation becoming aware of the breach.** The clock starts at the point of awareness, not confirmation of full scope — do not wait for a complete investigation to make the initial notification.
- This is a hard deadline under Article 23 of the Law and applies to your organisation as the personal data controller.

### B. Notify affected data subjects — Finance Sector Rule (Decree 356 Article 8)
- Under the **general** VN-PDPL rule, data subject notification should happen "simultaneously with or as soon as practicable after" authority notification.
- **However, as a finance/banking-sector entity, Decree 356 Article 8 imposes a stricter, dual-track requirement: you must notify affected data subjects within the same 72-hour window, simultaneously with the authority notification** — this is not "as soon as practicable," it is mandatory and concurrent for finance sector breaches.
- Practically: prepare both notifications together and issue them within the same 72-hour window.

### What to include in the notification (to both the authority and, in substance, data subjects):
1. Nature/description of the breach
2. Categories and approximate number of data subjects affected
3. Categories and approximate number of records affected
4. Name and contact details of your DPO or responsible officer
5. Likely consequences of the breach
6. Measures taken or proposed to address the breach (containment, remediation, support for affected customers)

If you do not yet have a DPO, name the responsible officer handling the incident — but note that as a fintech processing sensitive financial data, you are very likely required to have appointed a DPO under Decree 356 Article 13; if you have not, this itself is a separate compliance gap to remediate urgently.

## 4. Document

- Maintain (or create immediately if it doesn't exist) an **internal breach register**. This is mandatory under Article 23 regardless of whether the breach met the notification threshold — log this incident even as you're still investigating.
- Record: discovery date/time, containment actions, assessment findings, notifications sent (to whom, when, content), and remediation steps.
- This register and your notification records are your primary audit trail if the Ministry of Public Security follows up or if data subjects pursue complaints/compensation under their Article 4 rights.

## 5. Remediate

- Patch the root cause (technical vulnerability, process failure, third-party processor failure, etc.).
- If a third-party processor was involved, confirm they notified you immediately per their Article 5 processor obligations, and review/tighten your data processing agreement with them.
- Update security controls consistent with Decree 356 Article 8 finance-sector requirements: audit logging of access to personal data systems (who, when, what, purpose), and consider whether this incident triggers the need to accelerate your next annual compliance assessment.

## 6. Review

- Conduct a post-incident review: lessons learned, control gaps, and whether additional safeguards (encryption, MFA, access controls, monitoring) are needed.
- Update your breach response plan and DPIA/security documentation to reflect findings.

## Practical Timeline Summary

| Action | Deadline |
|---|---|
| Containment | Immediate, ongoing |
| Notify Ministry of Public Security | Within 72 hours of awareness |
| Notify affected data subjects | Within 72 hours, **simultaneous** with authority notification (finance-sector rule) |
| Internal breach register entry | Immediate, regardless of notification threshold |
| Root-cause remediation | As soon as practicable following containment |
| Post-incident review | Following remediation |

## Key Risk Note

Because the breach involves customer personal data at a fintech, assume financial/sensitive data exposure until proven otherwise, which increases both regulatory scrutiny and potential penalties. Failure to meet the 72-hour deadline, or treating data subject notification as merely "as soon as practicable" instead of simultaneous (the finance-sector standard), would itself be a separate compliance violation on top of the breach.

*This is general compliance guidance, not legal advice. Given the regulatory deadlines and potential financial-sector penalties involved, engage qualified Vietnamese counsel immediately to manage the notification process and any regulatory interaction.*
