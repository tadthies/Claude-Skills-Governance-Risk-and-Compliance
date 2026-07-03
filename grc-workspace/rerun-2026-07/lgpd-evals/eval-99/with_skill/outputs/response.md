# LGPD Breach Notification Obligations — Database Breach (50,000 Brazilian Customers)

Note: the facts below (names, emails, encrypted passwords, 50,000 data subjects) drive the analysis. Confirm the details in **bold** with your incident response and legal teams as they firm up — they change the specific ANPD notification content and risk determination.

## 1. Does This Trigger LGPD Breach Notification? (Art. 48)

Under **Art. 48**, controllers must notify the ANPD and affected data subjects when a security incident **may cause relevant risk or harm** to data subjects. Relevant factors here:

| Factor | Assessment |
|--------|-----------|
| Data types exposed | Names, emails, **encrypted** passwords — regular (non-sensitive) personal data under Art. 5 |
| Encryption status | Passwords encrypted reduces (but does not eliminate) risk — confirm algorithm strength, whether keys/salts were also exposed, and whether encryption is reversible or a proper hash |
| Volume | 50,000 data subjects — large-scale, a factor ANPD explicitly prioritizes for enforcement |
| Likely harm | Credential-stuffing risk if encryption is weak/reversible; phishing risk from exposed names + emails |

**Conclusion:** This is very likely a notifiable incident under Art. 48. Even with encrypted passwords, the exposure of names + emails at 50,000-subject scale creates a reasonable risk of harm (phishing, identity-linkage, credential attacks if encryption is weak). Treat this as **notifiable** unless your security team can affirmatively demonstrate the encryption renders the passwords unusable and no other risk vector exists — and document that determination either way for accountability (Art. 6, X).

---

## 2. Notification Timeline (ANPD Resolution CD/ANPD No. 15/2024)

LGPD's breach timeline differs from GDPR's 72-hour rule — Brazil uses **working days**, not calendar hours:

| Milestone | Deadline | Notes |
|-----------|----------|-------|
| **Preliminary ANPD notification** | **3 working days** from awareness of the incident | Initial notice; can be updated as facts develop |
| **Data subject notification** | Without undue delay, where high risk of harm | Assess in parallel with ANPD notice |
| **Full incident report to ANPD** | **20 working days** from confirmation | Complete details once investigation matures |

Since the user asked about the "next 72 hours," note the important distinction: **LGPD's clock is 3 *working* days, not 72 calendar hours** (that's the GDPR standard, which would also apply in parallel if any of the 50,000 individuals are also EU residents or the breach otherwise touches GDPR-scoped data). If your breach also has an EU nexus, run both clocks simultaneously — GDPR is stricter (72 hours, calendar) and LGPD is separate (3 working days). Confirm with counsel whether any EU-resident data subjects are in this dataset.

---

## 3. Incident Timeline & Action Checklist — Next 72 Hours

### Hour 0–24: Detect, Contain, Assess
- [ ] **Contain** — isolate affected database/systems, revoke compromised credentials, patch the exploited vulnerability, preserve forensic evidence (logs, snapshots) before remediation destroys evidence
- [ ] **Confirm scope** — verify the 50,000-record figure; identify exact data fields exposed (confirm no CPF, financial, or sensitive-category data under Art. 5/Art. 11 is also involved)
- [ ] **Assess encryption strength** — determine algorithm, whether salted/hashed vs. reversibly encrypted, and whether keys were exposed; this materially affects the risk rating
- [ ] **Engage DPO (Encarregado)** — LGPD requires the appointed DPO to be the point of contact for this process (Art. 41); loop in legal, security, and executive stakeholders
- [ ] **Open incident record** — start the accountability documentation required by Art. 6, X and Art. 47 (governance obligation); this record supports your defense if ANPD investigates

### Hour 24–48: Risk Determination & Notification Prep
- [ ] **Make the Art. 48 risk determination** — document the "relevant risk or harm" analysis (volume, data sensitivity, likelihood of misuse, encryption efficacy)
- [ ] **Draft preliminary ANPD notification**, including (per Art. 48 content requirements):
  - Nature and category of affected data (names, emails, encrypted passwords)
  - Number/categories of data subjects affected (~50,000)
  - Technical and security measures used to protect the data (including encryption)
  - Risks related to the incident
  - Measures taken or planned to reverse/mitigate the effects
  - Reason for any delay, if notification is not immediate
- [ ] **Draft data subject notification** (plain language) — likely required given email/credential exposure; should include what happened, data involved, recommended actions (password reset, monitor for phishing), and contact channel (DPO)
- [ ] **Check parallel obligations** — GDPR 72-hour clock if EU nexus exists; sector regulators (e.g., Banco Central if financial services); state consumer protection (CDC/SENACON) notice triggers

### Hour 48–72: Notify & Begin Remediation
- [ ] **Submit preliminary notification to ANPD** — must occur within **3 working days** of awareness (note: working days, so weekends don't count toward this deadline — confirm your actual deadline based on the awareness date)
- [ ] **Notify affected data subjects** where high risk of harm is present — via email is appropriate here since email addresses are the compromised contact channel (verify a clean/unaffected channel if email deliverability itself is compromised)
- [ ] **Force password resets** for all 50,000 affected accounts as a mitigation measure; recommend MFA enrollment
- [ ] **Monitor for exploitation** — credential-stuffing attempts, phishing campaigns targeting exposed emails
- [ ] **Begin root-cause remediation** — vulnerability patching, access control review, security control gap-fix plan

### Beyond 72 Hours (upcoming milestones — do not lose track)
- [ ] **Full incident report to ANPD within 20 working days** of confirmation, with complete forensic findings, root cause, and remediation plan
- [ ] **Post-incident review** — update RoPA, security measures (Art. 46), and RIPD/DPIA if this processing activity now qualifies as high-risk
- [ ] **Board/leadership briefing** and, if applicable, securities/public disclosure obligations (separate from LGPD)

---

## 4. Key Risk Exposure to Flag Internally

| Risk Area | LGPD Basis | Exposure |
|-----------|-----------|----------|
| Missed/late ANPD notification | Art. 48 + Res. CD/ANPD 15/2024 | Warning up to simple fine (Art. 52, II) — **up to 2% of Brazilian revenue, capped at R$50M per violation** |
| Inadequate security measures (Art. 46) if breach reveals control gaps | Art. 46, Art. 52 | Fine, publicisation, possible processing suspension |
| Failure to notify data subjects despite high risk | Art. 48 | Aggravating factor in any ANPD penalty calculation (Art. 52, §1º) |
| Large-scale breach | N/A (enforcement priority) | ANPD has explicitly flagged **large-scale data breaches** as a strategic enforcement priority — expect scrutiny at this volume (50,000 subjects) |

**Mitigating factors you can build now:** promptness of notification, cooperation with ANPD, good-faith remediation, and existing internal controls all reduce fine severity under Art. 52, §1º. Acting within the 3-working-day window and documenting thoroughness works directly in your favor.

---

## 5. Immediate Recommendations

1. **Do not wait for full forensic certainty** — the 3-working-day clock runs from *awareness* of the incident, not from completed investigation. Send the preliminary notification with the information you have and flag that a full report will follow within 20 working days (Art. 48 expressly allows this phased approach).
2. **Verify DPO is engaged and named publicly** (Art. 41) — ANPD will expect the DPO to be the process owner.
3. **Confirm whether any exposed customers are also EU residents** — if so, GDPR's 72-*hour* (calendar) clock is stricter than LGPD's and will control your fastest deadline.
4. **Treat "encrypted passwords" claim carefully** — do not understate risk in your ANPD notice; ANPD scrutinizes whether encryption was actually adequate (Art. 46) at the time of the incident, not just its existence.
5. **Document everything now** — the accountability principle (Art. 6, X) means your ability to demonstrate a timely, good-faith, well-documented response is itself a mitigating factor if ANPD investigates.
