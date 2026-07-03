Ransomware Attack — NIS2 Reporting Walkthrough
================================================

IMPORTANT FIRST STEP: Confirm whether your organization is actually in scope for NIS2 as an "essential" or "important" entity in the Member State(s) where you operate/are registered. NIS2 obligations (Article 23 reporting) only apply to entities designated in scope (per Annexes I and II, sector-based, plus size-cap thresholds, unless a specific exemption/designation applies). If you're not sure, treat the below as the default and confirm with your national CSIRT/competent authority in parallel — do not delay reporting while you figure this out.

Assuming you are an in-scope essential or important entity, and the ransomware attack encrypting your core operational systems qualifies as a "significant incident" (it almost certainly does, given operational disruption and encryption of core systems — this meets the NIS2 bar of causing or being capable of causing severe operational disruption or financial loss, or affecting other persons through considerable material/non-material damage):

## The three-stage reporting timeline (Article 23)

Your clock starts at the moment you become aware of the incident — not at 09:00 Monday necessarily, but whenever your team detected/confirmed it. If detection was at 09:00 Monday, use that as T0.

**1. Early warning — within 24 hours of becoming aware (T0 + 24h)**
- Submit to your national CSIRT (Computer Security Incident Response Team) or competent authority (whichever your Member State designates as the reporting channel).
- Content required: indicate whether the incident is suspected to be caused by unlawful or malicious action, and whether it could have a cross-border impact.
- This can be brief — it's a heads-up, not a full report. For your case: "Ransomware incident detected [timestamp], encrypting core operational systems, suspected malicious/unlawful action, cross-border impact [assess: do you operate in other EU states / do the affected systems serve customers in other Member States?]."

**2. Incident notification — within 72 hours of becoming aware (T0 + 72h)**
- Update/follow-up submission to the same authority.
- Content required: an assessment of the incident including severity, impact, and indicators of compromise (IoCs) where available.
- For a ransomware case, include: ransomware family/variant if identified, encryption scope (which systems/OT vs IT), initial access vector if known, IoCs (hashes, C2 domains/IPs, ransom note details), and updated severity/impact assessment (systems down, data at risk, operational disruption scale).

**3. Final report — within one month (1 month) of the incident notification (i.e., one month from the 72-hour submission, not from T0)**
- Must include:
  - A detailed description of the incident, its severity and impact.
  - The type of threat or root cause likely to have triggered the incident (e.g., initial access method, exploited vulnerability, phishing, RDP compromise, etc.).
  - Applied and ongoing mitigation measures.
  - Where applicable, the cross-border impact of the incident.
- If the incident is still ongoing at the one-month mark, you submit a progress report at that point and the final report is due one month after you handle the incident (i.e., after resolution).

## Who to notify

- **National CSIRT and/or competent authority** — as designated by the Member State(s) where you are established/in scope. If you operate in multiple EU Member States, you may need to notify authorities in each relevant state — check for cross-border/multi-state reporting rules and any "single point of contact" mechanisms.
- **Recipients of your service** (your customers) — you must inform service recipients of the significant incident without undue delay, where the incident is likely to adversely affect the provision of that service. Since your core operational systems are encrypted, customer-facing service disruption likely triggers this.
- **Recipients potentially affected by a significant cyber threat** — if there's an ongoing threat (e.g., you learn the ransomware group has stolen and threatens to leak data, or the same campaign is targeting your customers/supply chain), you must inform affected recipients of the threat and any mitigating measures they can take.
- **The public**, in certain cases — the competent authority or CSIRT may require or itself make public disclosure if in the public interest, or may direct you to inform the public.
- **Sector-specific/other regulators** — don't treat NIS2 as your only obligation. In parallel, assess:
  - GDPR (Article 33/34) — if personal data was encrypted/exfiltrated/compromised, you may have a separate 72-hour breach notification duty to your Data Protection Authority, and to affected individuals if high risk.
  - DORA — if you're a financial entity or ICT third-party provider in scope.
  - Sector regulators (energy, health, transport, etc.) with their own incident reporting rules.
  - Law enforcement — ransomware is a crime; consider reporting to national police/cybercrime unit, and Europol if cross-border.
  - Cyber insurance carrier — check policy notification deadlines (often much shorter, e.g., 24-48h).
  - Contractual notification duties to key customers/partners under SLAs.

## Practical action checklist for your Monday 09:00 incident

1. **Now**: Confirm detection/awareness time — this is your T0 for all deadlines.
2. **Immediately**: Activate incident response plan — containment and isolation of affected systems (don't wipe/rebuild before forensic evidence is captured).
3. **Within 24h of T0**: File the early warning with your national CSIRT/competent authority, noting suspected malicious action and preliminary cross-border assessment.
4. **In parallel within 24-72h**: Determine if this is a "significant incident" under the quantitative/qualitative NIS2 criteria (severe operational disruption, financial loss thresholds, or damage to others) — document your reasoning even if you conclude it's in scope, since you may be asked to justify it.
5. **Within 72h of T0**: Submit the incident notification with severity/impact assessment and any available IoCs.
6. **Ongoing**: Notify affected customers "without undue delay" once you know the service impact — don't wait for the 72-hour regulatory deadline if customer impact is already clear.
7. **Within 1 month of the 72-hour notification**: Submit the final report (or progress report if still unresolved) with root cause, impact, and mitigation measures.
8. **Cross-check in parallel**: GDPR breach notification (if personal data involved) — this has its own independent 72-hour clock from GDPR awareness, don't assume NIS2 reporting satisfies it.
9. **Do not pay or negotiate with the ransomware actor** without legal/law enforcement consultation — and note this may affect your sanctions-compliance obligations (OFAC-style designated actors) if operating with any EU/US nexus.
10. **Preserve evidence and maintain a timeline log** — regulators will expect a clear incident timeline in the final report, and this also supports any insurance claim, law enforcement referral, and litigation-hold requirements.

## Caveats

- Exact CSIRT/authority contact points, submission portals/forms, and language requirements are Member-State-specific — you need to identify your actual national competent authority (e.g., in Germany: BSI; in France: ANSSI; in Ireland: NCSC-IE, etc.) since NIS2 is a directive transposed into national law, and specifics (forms, extensions, thresholds) vary by country.
- The "significant incident" threshold and "considerable disruption" definitions may have further national-level technical guidance/thresholds — confirm against your national implementing legislation.
- If you are only a supplier/vendor to an in-scope entity rather than in-scope yourself, your notification obligations may instead run through contractual flow-down clauses rather than directly to the CSIRT — check your customer contracts.

This response is general guidance based on the NIS2 Directive (EU 2022/2555) framework and is not a substitute for advice from your legal counsel or your national CSIRT, who can confirm your specific scope status, exact deadlines from your true T0, and the correct national reporting channel and forms.
