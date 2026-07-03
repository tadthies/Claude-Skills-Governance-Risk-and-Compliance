Database Breach — LGPD Notification Obligations and 72-Hour Action Plan
=========================================================================

Facts as understood: A database breach exposed names, emails, and encrypted (hashed/encrypted) passwords of 50,000 Brazilian customers.

1. DOES LGPD APPLY?
--------------------
Yes. The Lei Geral de Proteção de Dados (Law No. 13,709/2018) applies because the personal data of natural persons located in Brazil was processed and compromised, regardless of where your company is headquartered (LGPD has extraterritorial reach similar to GDPR — Art. 3). Names and emails are personal data; account credentials (even encrypted) are also personal data whose confidentiality has been breached.

2. NOTIFICATION OBLIGATIONS UNDER LGPD
---------------------------------------
Key provision: LGPD Article 48.

- **Who must be notified:** (a) the ANPD (Autoridade Nacional de Proteção de Dados) — Brazil's data protection authority, and (b) the affected data subjects (titulares), when the incident may create risk or relevant damage to them.
- **Timing:** Unlike GDPR's fixed 72-hour deadline, LGPD Article 48 requires notification within a "reasonable period of time" (prazo razoável), as further defined by ANPD regulation. However, ANPD Resolution CD/ANPD No. 15/2024 (Regulamento de Comunicação de Incidente de Segurança) sets an expectation of notifying the ANPD within 3 business days (72 hours) of the controller becoming aware of the incident for incidents likely to result in relevant risk or damage to data subjects — effectively converging with GDPR practice. Treat 72 hours as your operative internal deadline even if the letter of the law says "reasonable."
- **Threshold/materiality test:** Notification is required when the incident may cause "risco ou dano relevante" (relevant risk or damage) to titulares. A breach of names, emails, and passwords (even encrypted) for 50,000 individuals almost certainly meets this threshold because:
  - Emails + names enable phishing/credential-stuffing and identity-adjacent fraud.
  - Encrypted passwords are not risk-free — if the encryption/hashing is weak (e.g., unsalted MD5/SHA1) or the encryption key was also exposed, passwords could be crackable. Reused passwords across services create account-takeover risk elsewhere.
  - Scale (50,000 individuals) itself is an aggravating factor ANPD considers.
- **What must be included in the ANPD/data subject notification (Art. 48, §1):**
  1. Description of the nature and category of personal data affected.
  2. The data subjects involved (number, categories).
  3. The technical and security measures used to protect the data (prior to and following the incident), observing trade secrets.
  4. The risks related to the incident.
  5. Reasons for any delay in notification, if applicable.
  6. Measures that were or will be adopted to reverse or mitigate the effects of the incident.
- **How to notify data subjects:** Communication must be clear, direct, and in plain language (not just buried in a policy). Typical channels: email to the affected email addresses, in-app/website notice, and potentially a public notice if individual contact isn't feasible for all 50,000 people.
- **Encrypted passwords consideration:** LGPD/ANPD guidance recognizes that adequate encryption can reduce (but not eliminate) risk and may factor into the "reasonable period" and severity assessment — but it does NOT exempt you from notifying if names/emails were also exposed in the clear, since that alone creates relevant risk (phishing, spam, targeted fraud, secondary exposure).

3. OTHER APPLICABLE LEGAL CONSIDERATIONS
------------------------------------------
- If any affected individuals are consumers, the Marco Civil da Internet (Law 12,965/2014) and Consumer Defense Code (CDC) may impose parallel duties of transparency and security.
- If your company operates in regulated sectors (finance, health, telecom), sector regulators (e.g., BACEN, ANS, ANATEL) may have their own breach-notification rules layered on top of LGPD.
- If any of the 50,000 individuals are also EU residents or the company has EU nexus, GDPR's strict 72-hour supervisory-authority deadline runs in parallel — don't assume LGPD's more flexible timeline gives you extra room under GDPR.
- Contractual obligations: check DPAs/contracts with B2B customers or partners requiring you to notify them of breaches affecting their end users, often with tighter deadlines (24–48 hours) than LGPD itself.

4. WHAT TO DO IN THE NEXT 72 HOURS — ACTION PLAN
---------------------------------------------------

**Hour 0–4: Contain and Confirm**
- Activate your incident response plan; convene IR team, legal/DPO (encarregado), security, and executive sponsor.
- Contain the breach: revoke exposed credentials/access, patch the vulnerability, isolate affected systems, rotate database/API keys and admin credentials.
- Preserve forensic evidence (logs, snapshots) before remediating — you'll need this for the ANPD report and any litigation defense.
- Confirm scope: verify the 50,000-record figure, exact data fields exposed, whether the encryption/hashing algorithm and any keys/salts were also exposed, and the exposure window (start/end dates).

**Hour 4–24: Assess and Engage Experts**
- Engage/activate outside breach counsel and a forensic incident response firm if not already retained.
- Assess the encryption strength of the exposed passwords (algorithm, salting, key exposure) — this materially affects risk rating and your notification narrative.
- Determine if this is a reportable incident under Art. 48 (very likely "yes" given scale and data types) and document the risk assessment/decision rationale (needed even if you ultimately argue lower risk).
- Identify your Encarregado (DPO) of record — they typically lead/coordinate the ANPD communication.
- Draft the ANPD notification and the data-subject notification in parallel; get legal sign-off.
- Force a password reset for all 50,000 affected accounts (and consider forcing reset broadly if you can't isolate exposure with certainty). Invalidate active sessions/tokens.
- Begin monitoring for credential-stuffing / anomalous login attempts using the exposed emails.

**Hour 24–72: Notify and Communicate**
- Submit notification to the ANPD via its official channel (petição eletrônica / Sistema de Peticionamento Eletrônico or the specific incident-report form once available), including all Art. 48 §1 elements listed above.
- Send direct notice to affected individuals in plain language: what happened, what data was involved, what you've done, what they should do (reset passwords, enable MFA, watch for phishing, avoid reusing the exposed password elsewhere), and a contact point/support channel.
- Prepare a public-facing statement/FAQ if the incident may become public or press-worthy, coordinated with comms/PR and legal.
- Notify any B2B partners/processors/sub-processors whose data or systems were implicated, per contractual timelines.
- If credit/financial exposure risk exists for any subset of users, consider offering credit monitoring or equivalent support (not strictly required by LGPD but a common risk-mitigation and goodwill measure).
- Log every action, decision, and timestamp — ANPD can request the full incident timeline and your reasoning for timing/scope decisions later.

**Ongoing (beyond 72 hours)**
- Complete root-cause analysis and remediation (patch vulnerabilities, review access controls, add monitoring/alerting).
- Be prepared for ANPD follow-up requests or an administrative sanction process; cooperate and keep documentation organized.
- Conduct a post-incident review and update your incident response plan, data retention practices, and encryption standards.
- Consider whether this incident, given the affected population and data categories, warrants updating your Data Protection Impact Assessment (Relatório de Impacto à Proteção de Dados Pessoais / RIPD) for the underlying processing activity.

5. KEY TAKEAWAYS
-----------------
- Treat 72 hours as your working deadline for notifying the ANPD, consistent with current ANPD regulation, even though the LGPD statutory text says "reasonable period."
- Notify affected data subjects directly and in plain language — don't rely solely on the ANPD filing.
- Encryption on passwords helps your risk narrative but does not eliminate the obligation to notify, especially since names and emails were exposed unencrypted.
- Document everything: your risk assessment, the rationale for your notification timing and scope, and the mitigation steps taken — this documentation is your primary defense in any ANPD inquiry.
- Loop in outside counsel with LGPD/ANPD experience quickly; breach-notification drafting and ANPD engagement have nuances (e.g., what counts as "relevant risk," format of the filing) best handled with specialized support.

Disclaimer: This is general guidance based on LGPD and publicly known ANPD regulatory practice, not formal legal advice. Confirm current ANPD procedural requirements (forms/portal, current resolution numbers) and get sign-off from qualified Brazilian data protection counsel before acting, given the regulatory and factual specifics of your case.
