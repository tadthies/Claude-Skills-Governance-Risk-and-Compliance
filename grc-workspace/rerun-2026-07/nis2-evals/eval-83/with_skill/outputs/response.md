# NIS2 Incident Reporting: Ransomware Attack (Monday 09:00, Core OPS Systems Encrypted)

First, a scoping caveat, then the timeline.

## 0. Threshold question you must answer first

NIS2 Art. 23 obligations only bite if this qualifies as a **"significant incident."** A ransomware attack that has encrypted core operational systems almost certainly clears the bar, because a significant incident is one that:

- has caused, or is capable of causing, **severe operational disruption** to the services provided, or financial loss to the entity; or
- has affected, or is capable of affecting, **other natural or legal persons** by causing considerable material or non-material damage.

Encryption of core operational systems is a strong presumptive "yes" on the first limb alone (operational disruption). You do not need to wait for a precise financial-loss figure to trigger the clock — "capable of causing" severe disruption is enough, and you're already past that.

If you are one of the entity types bound by **Implementing Regulation (EU) 2024/2690** (DNS, TLD registry, cloud, data centre, CDN, MSP, MSSP, online marketplace/search/social platform, or trust service provider), the fast test is: **direct financial loss above EUR 500,000 or 5% of annual turnover, whichever is lower**, plus any entity-specific threshold (e.g., cloud providers: impact on 5% of users or 1 million users, whichever is smaller). For all other sectors (energy, transport, health, manufacturing, etc.), that threshold isn't directly binding on you, but it's the de facto benchmark your competent authority will informally reason from — and a ransomware encryption of core operational systems will likely meet it regardless.

**Working assumption for the rest of this answer: this is a significant incident and the clock is running from 09:00 Monday.**

## 1. The three-stage reporting timeline (Art. 23)

The clock starts at the moment you became **aware** of the incident — not when it started, not when you've finished investigating. If detection was at or near 09:00 Monday, that's T0.

| Stage | Deadline from awareness (T0) | Due by | What you submit |
|---|---|---|---|
| **Early warning** | 24 hours | **Tuesday 09:00** | Notify your CSIRT or competent authority. Flag whether the incident is suspected to be caused by unlawful/malicious action, and whether it could have cross-border impact. |
| **Incident notification** | 72 hours | **Thursday 09:00** | Update/confirm the early warning. Provide an initial assessment: severity, impact, and — critically for ransomware — indicators of compromise (IoCs) if available. |
| **Final report** | 1 month | **Monday, August 3** | Detailed description of the incident, type of threat/root cause, severity and impact, mitigation measures applied and ongoing, and any cross-border impact. |

Notes on mechanics:
- If the incident is still ongoing at the 1-month mark, you submit a **progress report** at that point and the final report follows once resolved.
- The early warning and 72-hour notification obligations run in parallel with, not instead of, your internal incident response — you should already be in containment/eradication mode by the time you're drafting the 24-hour notice.

## 2. Who you report to

- **National CSIRT or competent authority** in the Member State(s) where you are established/operate — this is who receives all three reports (early warning, notification, final report).
- If the incident has **cross-border impact** (e.g., affects users, supply chain partners, or operations in other Member States), say so explicitly in the 24-hour early warning — this triggers cross-Member-State coordination obligations on the authority's side, not yours, but you need to flag it so they can act.
- **Recipients of your service** — separate from the regulator-facing obligations, if the incident is likely to adversely affect the provision of your service, you (or the competent authority, depending on Member State transposition) may need to notify affected recipients of the service directly, especially where they need to take protective measures.
- Ransomware-specific overlay: depending on jurisdiction and sector, you may have **parallel notification duties** outside NIS2 — e.g., GDPR Art. 33/34 if personal data was exposed or exfiltrated (72-hour clock to the data protection authority, separate from the CSIRT), sector regulators (e.g., financial services, health), and potentially law enforcement for a ransomware/extortion crime report. NIS2 does not replace these; treat the 24h/72h/1-month NIS2 track as one lane among several that may run concurrently.

## 3. What each report should contain (practical drafting checklist)

**24-hour early warning:**
- Time of detection (09:00 Monday) and time of this notification
- Brief description: ransomware encryption event affecting core operational systems
- Suspected malicious/unlawful origin: yes (ransomware is by definition malicious)
- Possible cross-border impact: yes/no, with brief reasoning
- Point of contact for follow-up

**72-hour notification:**
- Updated severity and impact assessment (which systems, which services, scope of operational disruption)
- Initial IoCs if your team/incident responders have identified the ransomware variant, C2 infrastructure, entry vector, etc.
- Estimated business impact (downtime, affected services, any customer/user impact)
- Whether recipients of your service have been or will be notified

**1-month final report:**
- Full incident narrative and root cause (initial access vector — phishing, exposed RDP, vulnerable VPN appliance, etc.)
- Type of threat (ransomware family/strain if attributable)
- Severity and actual impact (systems down, duration, data impacted, financial loss)
- Mitigations applied (containment, eradication, recovery, restoration from backup vs. ransom decision)
- Ongoing mitigations/remediation roadmap
- Cross-border impact confirmation
- If the incident is not yet closed at the 1-month mark: submit a progress report instead, with a final report to follow

## 4. Immediate action items, right now

1. **Confirm awareness timestamp precisely** — the 24h/72h/1-month clock is anchored to it. If different teams noticed at different times, use the earliest credible detection time as a defensible T0.
2. **Notify your CSIRT/competent authority within 24 hours of T0** — do not wait for full root-cause analysis; the early warning is deliberately lightweight.
3. **Stand up (or activate) your incident response and crisis management process** under your Art. 21(2)(b)/(c) measures — incident handling and business continuity/backup/DR — since NIS2 expects these to be operating in parallel with reporting, not as an afterthought.
4. **Check for parallel GDPR/sector/law-enforcement notification duties** if any personal data was on the encrypted systems or exfiltrated.
5. **Log everything from T0 forward** — detection time, containment actions, systems affected, communications sent — you will need this for the 72-hour and 1-month submissions, and for any post-incident review under Art. 21(2)(b) (post-incident reviews).

## 5. Governance note (Art. 20)

Your management body should be briefed now, not just operationally but because Art. 20 places personal accountability on management for overseeing the organisation's cybersecurity risk management, which includes making sure this reporting timeline is actually met. A missed 24-hour or 72-hour deadline is itself a compliance failure independent of the ransomware event, and factors into penalty exposure (up to €10,000,000 or 2% of global annual turnover for essential entities; €7,000,000 or 1.4% for important entities, whichever is higher in each case).

---

**Bottom line:** Report to your national CSIRT/competent authority at 24h (Tue 09:00), 72h (Thu 09:00), and 1 month (Mon Aug 3) from the 09:00 Monday detection time. Treat this as a significant incident given the operational disruption to core systems. Run GDPR and sector-specific notifications in parallel if applicable. If you can tell me your Member State and sector, I can point you to the specific national CSIRT contact channel and confirm whether Implementing Regulation (EU) 2024/2690's binding thresholds apply to your entity type.
