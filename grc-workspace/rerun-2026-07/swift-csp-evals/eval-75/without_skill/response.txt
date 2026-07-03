Malware on a SWIFT-connected server with suspected fraudulent transactions is a severe incident. Below is guidance on immediate obligations under CSCF Control 7.1, notification requirements, evidence preservation, and what a compliant SWIFT-specific incident response plan should contain.

## 1. Immediate Obligations Under CSCF Control 7.1 (Cyber Incident Response Planning)

Control 7.1 is an advisory (not mandatory in all architecture types, but strongly expected and increasingly treated as a baseline) control requiring a documented incident response plan and its execution. When an actual or suspected compromise of the secure zone / SWIFT infrastructure occurs, the immediate obligations generally are:

- **Activate your incident response plan (IRP) immediately** — treat this as a confirmed cyber incident affecting SWIFT-related infrastructure, not a routine malware cleanup event.
- **Contain the threat** — isolate the affected server(s) from the network (including from the SWIFT secure zone, jump servers, HSMs/tokens, and messaging interfaces) without destroying volatile evidence. Do not simply wipe/reimage before evidence capture.
- **Assess scope** — determine whether the malware had access to or interacted with SWIFT messaging components (Alliance Access/Entry, SWIFTNet Link, RMA, HSM, or operator credentials), and whether fraudulent MT/MX messages (e.g., MT103, MT202) may have been generated or altered.
- **Preserve the ability to stop/recall payments** — engage your correspondent/counterparty banks immediately to request payment holds, cancellations, or recalls (MT192/MT292, or SWIFT gpi Stop and Recall functionality where applicable) before funds are irrevocably settled.
- **Engage internal stakeholders** — CISO, fraud/financial crime team, treasury/payments operations, legal, and executive management should be looped in within hours, not days.

## 2. Who to Notify, and By When

Given suspected fraudulent transactions, notification obligations layer across SWIFT, regulators, and counterparties:

**a) SWIFT itself**
- SWIFT requires customers to report security incidents that could impact SWIFT or its community. Under the SWIFT Customer Security Programme, you are expected to notify your SWIFT Customer Support / Financial Crime Team **as soon as possible** — SWIFT's guidance is generally within **24 hours** of confirming an incident that has a potential impact on the secure zone, SWIFT-related systems, or messaging integrity. Use SWIFT's incident reporting channel (Case Management / Financial Crime team) and, where relevant, your SWIFT-certified Customer Security Officer (CSO) or Chief Security Officer contact.
- If the malware or compromise could plausibly have affected other SWIFT users (e.g., malware propagated via a shared service bureau, or attacker used your credentials to send fraudulent traffic to counterparties), SWIFT's Customer Security Programme expects transparency because of the community-wide fraud risk (as emphasized after incidents like Bangladesh Bank).

**b) Counterparty / correspondent banks**
- Notify immediately (within hours) — request they place a hold on any suspect payment messages, do not process/settle them, and attempt recall via MT192/MT292 or gpi Stop and Recall.

**c) Regulators**
- Your home regulator/central bank (and host country regulators if a branch/subsidiary is involved) typically require notification of a material cyber incident or suspected fraud within a short window — commonly **24–72 hours**, depending on jurisdiction (e.g., many banking supervisors expect initial notice within 24-72 hours, with detailed follow-up reports afterward). If this involves EU entities, DORA incident reporting timelines apply (initial notification within 4 hours of classifying it as major, intermediate report within 72 hours). If personal data is affected, GDPR's 72-hour breach notification to the DPA may also apply.
- Financial Intelligence Unit / law enforcement — suspected fraud typically triggers a Suspicious Activity Report (SAR) or Suspicious Transaction Report (STR) obligation, often within statutory deadlines (varies by country, but commonly a few days).

**d) Internal governance**
- Board/senior management and internal audit should be notified per your incident severity matrix, typically within 24 hours for a critical incident.

**e) Your local SWIFT National Member Group / User Group**, where applicable, and your third-party service bureau (if one is used) should also be notified promptly.

Document every notification with timestamp, recipient, channel, and content — the timeliness of notification is itself scrutinized during CSP assessments and by regulators.

## 3. Evidence to Preserve

Preserve evidence before remediation destroys it. At minimum:

- **Forensic disk/memory images** of the compromised server(s) (full disk image plus RAM capture before shutdown, since malware analysis often needs volatile memory).
- **Network logs**: firewall, IDS/IPS, proxy, DNS, and netflow data covering the suspected dwell time of the malware (extend lookback as far as retention allows).
- **SWIFT application logs**: Alliance Access/Entry logs, SWIFTNet Link logs, RMA logs, message audit trails, and Relationship Management Application changes.
- **Authentication/access logs**: operator login records, HSM/token usage logs, privileged access management logs, jump server session recordings.
- **Message-level evidence**: full text of any suspect MT/MX messages sent or received, including timestamps, originator/operator IDs, and authorization/approval trail (maker-checker records).
- **Malware artifacts**: samples of the malware binary/hashes, any C2 (command-and-control) indicators, persistence mechanisms found.
- **Chain of custody documentation** for all collected evidence — critical if this leads to law enforcement involvement or litigation/insurance claims.
- **System configuration snapshots** at time of incident (patch levels, running processes, scheduled tasks, installed software) to support root-cause analysis.
- **Backup copies** of relevant databases/logs before any remediation or reimaging occurs.

Engage a qualified digital forensics team (internal or external) before altering the affected systems, and consider whether local law requires preserving evidence in a specific manner for admissibility.

## 4. What a CSCF v2025-Compliant SWIFT-Specific Incident Response Plan Should Contain

To satisfy Control 7.1 under CSCF v2025 (and hold up under a CSP self-attestation / independent assessment), the plan should include:

1. **Scope and applicability** — explicitly covers the SWIFT secure zone: messaging interfaces, communication interfaces, HSMs, jump servers, operator PCs, RMA, and any connected service bureau.
2. **Incident classification/severity matrix** — criteria for what constitutes a SWIFT-related security incident (including malware detection, unauthorized message creation, credential compromise, suspected fraud).
3. **Roles and responsibilities** — a named incident response team with clear ownership: CISO, SWIFT Security Officer, payments operations, legal, communications, and executive escalation path, plus 24/7 contact list.
4. **Detection and triage procedures** — how anomalies (e.g., malware alerts, unusual MT/MX traffic, off-hours transactions) are identified and escalated, ideally tied to your Control 6.4/6.5A fraud/anomaly detection tooling.
5. **Containment and eradication procedures** — specific steps for isolating SWIFT infrastructure without destroying evidence, including a "kill switch" procedure to disconnect from SWIFTNet if necessary.
6. **Payment recall/hold procedures** — pre-defined process and templates for issuing MT192/MT292 recall requests or using gpi Stop and Recall, and contacts at key correspondent banks.
7. **Notification procedures and timelines** — explicit, pre-agreed contact list and SLA for notifying SWIFT (Customer Support/Financial Crime team), regulators, correspondent banks, law enforcement, and internal stakeholders, with template notification forms.
8. **Evidence preservation and forensics procedures** — chain-of-custody process, designated forensics provider/retainer, log retention requirements sufficient to support investigation.
9. **Communication plan** — internal (board, staff) and external (customers, media, regulators) messaging protocols, including a designated spokesperson.
10. **Recovery and restoration procedures** — validated clean rebuild process for SWIFT infrastructure, re-attestation of integrity before reconnecting to SWIFTNet, and confirmation from SWIFT/vendor that systems are safe to resume.
11. **Post-incident review** — root-cause analysis, lessons-learned process, and a mechanism to feed improvements back into controls (e.g., updates to Control 2.x patching, 5.x credential management, 6.x detection).
12. **Testing and maintenance** — the plan must be tested at least annually (tabletop exercises or simulations) and updated after each test or real incident; testing evidence should be retained for CSP attestation/assessment purposes.
13. **Integration with the broader corporate incident response/BCP/DR plans**, so the SWIFT-specific plan isn't siloed from enterprise-wide response.
14. **Reference to CSCF v2025 control mapping** — explicitly map plan sections back to relevant controls (7.1, and related controls like 2.4 logging, 6.4 anomaly detection) so the plan can serve as evidence during your annual CSP self-attestation or independent assessment.

## Important Caveat

This is general guidance based on the structure and intent of the SWIFT CSP framework (CSCF) and common regulatory practice — it is not a substitute for legal advice or direct confirmation with SWIFT. Given a suspected fraud event is in progress, you should **in parallel** to reading this: (a) contact SWIFT's Customer Security Programme / Financial Crime team directly for authoritative, incident-specific guidance, (b) engage outside counsel and a forensics firm immediately, and (c) confirm exact regulatory notification deadlines with your compliance/legal team, since these vary by jurisdiction and may be shorter than general benchmarks cited above.
