# Supplier Ransomware Incident — NZISM-Aligned Incident Response Obligations

This is a live incident involving a third-party supplier holding your agency's data, so treat this as urgent. Here is your NZISM-aligned response pathway.

## 1. Immediate Framing: Your Agency Is Still Accountable

Under the NZISM's Third-Party Supplier controls, **agencies remain responsible for information security even when systems or data are hosted by a third party.** The fact that the ransomware hit the supplier's environment, not yours directly, does not reduce your obligations — you must treat this as an incident affecting your agency's information.

## 2. Activate Your Incident Response Plan

- Invoke your documented Incident Response Plan immediately (NZISM Section 14 — Incident Management requires this plan to exist and be tested at least annually).
- Classify the incident severity based on your defined severity levels — a ransomware event affecting agency data at a supplier should generally be treated as high/significant severity until scope is established.
- Stand up your incident response team, including the CISO/ISO, and engage the supplier's incident response contacts per your contract's incident notification clauses.

## 3. Confirm What the Supplier Owes You Contractually

Per NZISM third-party supplier controls, your contract with this supplier should already require:
- **Incident notification within a defined timeframe** — check the contract for the specific notification window (this should have been triggered already; if the supplier is late notifying you, that is itself a contractual breach to log).
- **Right to audit** their security controls and response.
- Contractual NZISM-equivalent security obligations that you can now assess were/weren't met.

Immediately request from the supplier:
- Scope of the compromise (systems affected, data types and volumes involved, whether your agency's data was specifically accessed, exfiltrated, or only encrypted)
- Timeline of detection and containment actions taken
- Evidence preservation status (has forensic evidence been preserved, chain of custody maintained)
- Whether other agency/government clients are affected

## 4. Determine Classification of the Affected Data

Your notification and handling obligations scale with the classification of the data the supplier held:
- If the data is **Restricted or above**, this significantly raises the stakes — mandatory NCSC NZ reporting applies.
- If the data includes **Confidential** information, the NZISM requires **immediate NCSC NZ notification** for any incident involving Confidential data — this is not discretionary and not delayed pending full scoping.
- If the data includes **personal information** (regardless of government classification level), Privacy Act 2020 obligations run in parallel (see below).

## 5. Who You Must Notify in New Zealand

| Notify | When / Why |
|---|---|
| **NCSC NZ (National Cyber Security Centre)** | Mandatory reporting of significant security incidents per NZISM Incident Management controls. Ransomware affecting agency data at a supplier is a significant incident and should be reported promptly — immediately if any Confidential-level data is involved. NCSC NZ can also provide incident response support and threat intelligence relevant to the ransomware variant/actor. |
| **Your Accrediting Authority** | The individual who accepted residual risk for the system(s)/data now needs to be briefed, since this incident affects the risk position they signed off on. |
| **Office of the Privacy Commissioner (OPC)** | If personal information is involved, the Privacy Act 2020 mandatory breach notification regime applies. Notify OPC (and affected individuals, where required) if the breach has caused or is likely to cause serious harm. This is a separate, parallel legal obligation to NZISM/NCSC NZ reporting, not a substitute for it. |
| **Agency Chief Executive / Senior Leadership** | Per your governance escalation procedures — a supplier ransomware event involving agency data is a CE-level risk item. |
| **GCSB** (via NCSC NZ) | For nationally significant incidents, NCSC NZ may escalate within GCSB; you don't need to contact GCSB separately, but be aware NCSC NZ is GCSB's operational cybersecurity arm. |
| **New Zealand Police** | Ransomware is a criminal act; consider a Police report, particularly if extortion demands were made or if law enforcement engagement is needed for the investigation. |
| **Other affected agencies/third parties** | If the compromised supplier serves multiple agencies or your data flows to downstream parties, you may have a duty to alert them too — check your data-sharing agreements. |
| **Affected individuals** | If personal information about specific individuals was compromised and serious harm is likely, direct notification to those individuals is required under the Privacy Act 2020, in addition to OPC notification. |

**Do not wait for full scoping to make the NCSC NZ and OPC notifications** if there is a reasonable indication that Confidential-level or personal data is involved — both regimes expect prompt/early notification with updates as facts emerge, not a single notification after full investigation.

## 6. Evidence Preservation and Forensic Readiness

- Ensure the supplier (and your own team, for any agency-side systems) preserves logs, forensic images, and other evidence rather than immediately rebuilding/restoring systems — this matters both for root cause analysis and for any Police/regulatory investigation.
- Maintain a chain of custody for any evidence or artefacts your agency receives from the supplier.

## 7. Containment and Recovery Considerations

- Confirm whether your agency has any direct connectivity or credentials shared with the compromised supplier environment — if so, treat those as potentially compromised and rotate credentials/certificates as a precaution, even before the supplier's investigation concludes.
- Validate the integrity of any data restored from the supplier post-incident before trusting it for operational use.
- Check your Business Continuity Plan for the affected service — if the supplier's system is unavailable during recovery, this may trigger your BCP/DRP.

## 8. Post-Incident Actions

- Conduct a post-incident review once the situation is resolved: root cause, lessons learned, and control improvements — required under NZISM Incident Management controls.
- Reassess the supplier relationship: did the contract's security obligations hold up? Was notification timely? This should feed into your Third-Party Supplier risk register and potentially trigger a re-assessment of the supplier's security posture or contract terms (including possibly invoking your right-to-audit clause).
- Update your Security Risk Assessment / SSP for any agency system that depended on this supplier, reflecting the realised risk and any new compensating controls.

## Summary — Notification Checklist

- [ ] Activate agency Incident Response Plan
- [ ] Engage supplier per contractual incident notification clause; request full scope and timeline
- [ ] Determine classification of affected data
- [ ] Notify NCSC NZ (mandatory; immediate if Confidential+ data involved)
- [ ] Brief Accrediting Authority
- [ ] Assess Privacy Act 2020 applicability; notify Office of the Privacy Commissioner and affected individuals if personal information and serious harm threshold met
- [ ] Notify agency CE/senior leadership
- [ ] Consider NZ Police report
- [ ] Preserve evidence; maintain chain of custody
- [ ] Assess and contain any shared connectivity/credential exposure
- [ ] Conduct post-incident review and update SSP/risk register/supplier contract terms

---
*This is general compliance guidance, not legal advice. Given the active nature of this incident and the parallel Privacy Act 2020 obligations, consult your legal counsel, Privacy Officer, and NCSC NZ directly for authoritative, time-sensitive guidance specific to this event.*
