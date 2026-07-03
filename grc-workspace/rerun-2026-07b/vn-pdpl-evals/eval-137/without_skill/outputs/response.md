# Breach Notification Workflow — Vietnam PDPL (Fintech, Ho Chi Minh City)

Here is a step-by-step walkthrough of the breach notification process under Vietnam's data protection framework (PDPL, and the Decree 13-style implementing rules it builds on) for a fintech that has just discovered a breach of customer personal data.

## Step 1: Internal Triage (Hour 0)
- Activate your incident response plan immediately.
- Contain the breach (isolate affected systems, revoke compromised credentials, patch the vulnerability).
- Assemble a cross-functional response team: security/IT, legal/compliance, DPO (if appointed), and executive sponsor.
- Begin a breach log capturing: discovery time, nature of the incident, systems/data affected, and actions taken — this record itself is often a regulatory expectation.

## Step 2: Assess Scope and Severity
- Determine what personal data was involved. As a fintech, you likely hold financial/payment data, which is treated as **sensitive personal data** under Vietnamese rules — this raises the stakes and triggers stricter notification expectations.
- Estimate number of data subjects affected, whether data was exfiltrated vs. merely exposed, and likely harm (financial fraud, identity theft).

## Step 3: Notify the Regulator — Ministry of Public Security (MPS)
- **Who:** The Ministry of Public Security (specifically its Cybersecurity and Hi-Tech Crime Prevention unit, A05, which has traditionally been the enforcement body for Vietnam's data protection rules) is the primary authority to notify.
- **When:** Notification is expected **as soon as possible after discovery**, with Vietnam's framework historically requiring notification without undue delay — reported informally within 72 hours is the benchmark practitioners use (aligned with the standard also used under Decree 13's breach provisions and consistent with international norms like GDPR's 72-hour rule). An initial notification can be made with preliminary information, followed by a fuller report as the investigation progresses.
- **What to include in the notification:**
  - Description of the breach (nature, categories and approximate number of data subjects/records affected)
  - Contact point for further information (your DPO or designated contact)
  - Likely consequences of the breach
  - Measures taken or proposed to address the breach and mitigate harm
  - Timeline of discovery and response

## Step 4: Notify Affected Data Subjects
- Vietnamese customers whose personal data was compromised should be notified where the breach poses a risk to their rights and interests — this is especially true for a fintech, since compromised payment/financial data creates direct fraud risk.
- Notification should be timely (ideally concurrent with or shortly after the regulator notification) and should include:
  - What happened and what data was involved
  - Potential risks/consequences (e.g., fraud, unauthorized transactions)
  - Steps the company is taking
  - Recommended actions for the customer (e.g., change passwords, monitor statements, watch for phishing)
  - A contact channel for questions

## Step 5: Sector Regulator Coordination (Fintech-Specific)
- As a fintech in Vietnam, you likely also fall under State Bank of Vietnam (SBV) oversight for payment/financial services. Depending on your license type (e-wallet, payment intermediary, etc.), SBV may have its own incident reporting obligations that run in parallel to the MPS/PDPL notification — check your SBV licensing conditions for breach/incident reporting timelines, as these are often stricter (sometimes same-day or 24-hour reporting for serious incidents).

## Step 6: Document Everything
- Maintain a full incident record: detection method, root cause, data categories/volumes affected, notifications sent (to whom, when, content), remediation steps, and post-incident review outcomes. Regulators can request this documentation even after initial notification is complete.

## Step 7: Post-Incident Remediation and Review
- Implement corrective actions (e.g., patch vulnerabilities, strengthen access controls, encrypt data at rest/in transit).
- Update your DPIA/risk assessment to reflect lessons learned.
- Consider whether the incident reveals a broader gap (e.g., inadequate encryption of payment data, insufficient monitoring) that needs a structural fix, not just a patch.
- Brief leadership and, if applicable, your board/audit committee.

## Quick-Reference Timeline

| Action | Target Timing |
|---|---|
| Contain breach | Immediately upon discovery |
| Internal escalation to response team | Within hours |
| Notify Ministry of Public Security | As soon as possible — treat 72 hours as the outer bound |
| Notify SBV (if applicable to your license) | Per your SBV licensing terms — often faster than 72 hours |
| Notify affected customers | Promptly, especially where fraud risk exists |
| Full incident report/documentation | Follow-up after initial notification, as investigation concludes |

## Important Caveat
Exact statutory deadlines, the precise designated authority/unit, and required notification forms are set by the PDPL's implementing decree and by sector-specific rules from the State Bank of Vietnam, and these details can be updated by government guidance. Given the seriousness of this incident and the fact that you're a regulated fintech, engage Vietnamese legal counsel and, if you have one, your DPO immediately to confirm current exact deadlines and forms before your notifications go out.
