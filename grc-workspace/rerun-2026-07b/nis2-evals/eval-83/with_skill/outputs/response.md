# NIS2 Incident Reporting Walk-Through — Ransomware Attack, Monday 09:00

I'll treat Monday 09:00 as your moment of **awareness** (the trigger for all NIS2 clocks) and walk through exactly what's owed, to whom, and by when.

## Step 0 — Is this a "significant incident"? (Art. 23(3))

Before anything else, confirm the reporting obligation is triggered. An incident is "significant" if it:
- (a) has caused or can cause **severe operational disruption** of your services or **financial loss** to your entity, or
- (b) has affected or can affect other natural or legal persons by causing **considerable material or non-material damage**.

Ransomware that has **encrypted your core operational systems** almost certainly clears this bar on criterion (a) alone — severe operational disruption is exactly what this scenario describes. Treat this as significant and start the clock now; do not wait to fully scope the incident before triggering the 24-hour report.

**If you are a digital-infrastructure entity** (DNS, TLD, cloud, data centre, CDN, MSP/MSSP, trust service provider, online marketplace/search/social platform) covered by Commission Implementing Regulation (EU) 2024/2690, use its quantitative thresholds instead of judgment alone (baseline: direct financial loss above €500,000 or 5% of annual turnover, whichever is lower) to confirm significance.

## Step 1 — Recipient

Report to your **national CSIRT or competent authority** — the single entry point designated under your Member State's NIS2 transposition law. (If you are a financial entity subject to DORA, incident reports go to your financial supervisor instead under the DORA lex specialis — see the note at the end.)

## Step 2 — The reporting timeline, computed from Monday 09:00 awareness

| Deadline | Report type | Due by | What must be included (Art. 23(4)) |
|---|---|---|---|
| **≤24 hours** | Early warning | **Tuesday 09:00** | Whether the incident is suspected to be caused by unlawful/malicious action (state: yes — ransomware); whether cross-border impact is possible |
| **≤72 hours** | Incident notification | **Thursday 09:00** | Update to the early warning; initial assessment of severity and impact; indicators of compromise (IoCs) — e.g., ransomware variant/family, encryption indicators, affected system scope |
| **On request** | Intermediate report | As requested by the authority | Status updates while handling is ongoing |
| **≤1 month after the 72h notification** | Final report | **Thursday, one month after the 72h report** (i.e., roughly one month + 3 days after Monday 09:00) | Detailed description including severity and impact; threat type/root cause; applied and ongoing mitigation measures; cross-border impact |
| **If still unresolved at the 1-month mark** | Progress report, then final report | Progress report at 1 month; final report within **1 month of handling completion** | Same required fields as above |

### What to actually put in each report
- **Tuesday 09:00 (early warning):** "Ransomware encryption of core operational systems detected/confirmed at Monday 09:00. Suspected malicious action: yes. Cross-border impact: [assess — does this affect services delivered into other Member States?]." This is a fast, minimal-content report — do not delay it to gather more facts.
- **Thursday 09:00 (72h notification):** severity and impact assessment (which systems/services affected, estimated scope of disruption), initial IoCs (ransomware family if identified, entry vector if known, affected hosts/hashes), and an update on whether the situation has changed since the early warning.
- **Final report (within 1 month of the 72h notification, or within 1 month of resolution if still ongoing):** full root cause analysis, mitigation steps taken and remaining, confirmed impact and severity, and cross-border impact assessment.

## Step 3 — Parallel obligations to run alongside the CSIRT reports

1. **Notify affected service recipients (Art. 23(1)):** if the incident is likely to adversely affect delivery of your services to customers, you must notify those recipients of the significant incident without undue delay — this is separate from, and in addition to, the CSIRT report.
2. **GDPR Art. 33, if personal data was accessed or exfiltrated:** ransomware incidents frequently involve data exfiltration as well as encryption. If any personal data was affected, you have a **separate 72-clock-hour deadline to your Data Protection Authority** — different report, different recipient, different clock, running from the point you became aware personal data was compromised (which may not be the same moment as Monday 09:00 if exfiltration is discovered later). Do not conflate the NIS2 CSIRT report with the GDPR breach notification — prepare both in parallel if personal data is implicated.
3. **Public disclosure:** your competent authority can order public disclosure of the incident where public awareness is deemed necessary (Art. 23(7)) — be prepared for this possibility, particularly given the operational severity described.

## Step 4 — Governance and evidentiary trail (Art. 20 link)

Your management body should be looped into incident response now, not just informed after the fact — Art. 20 requires the management body to oversee implementation of your Art. 21(2)(b) incident-handling measures, and regulators will expect to see this oversight reflected (e.g., a documented crisis management decision log) if this becomes a supervised incident.

## Immediate action checklist (next few hours)

1. Confirm significance under Art. 23(3) — done above (yes).
2. Identify your national CSIRT/competent authority's reporting channel now if you haven't already (most Member States provide a web portal or dedicated incident hotline).
3. Draft and submit the early warning **before Tuesday 09:00** — keep it brief; malicious-action suspicion and possible cross-border impact are the two required data points.
4. Stand up IoC collection and severity/impact assessment work now so the 72-hour notification (Thursday 09:00) has real content.
5. In parallel, assess whether personal data was exfiltrated or accessed — if yes, start the independent GDPR Art. 33 clock and involve your DPO.
6. Assess whether any customers/service recipients need direct notification under Art. 23(1) because service delivery is impacted.
7. Preserve forensic evidence and begin root-cause analysis now — you'll need it for the final report within 1 month of the 72-hour notification.

*This is general compliance information, not legal advice. Confirm your national CSIRT reporting channel and any Member-State-specific timing/format requirements, and consult qualified counsel given the operational severity described.*
