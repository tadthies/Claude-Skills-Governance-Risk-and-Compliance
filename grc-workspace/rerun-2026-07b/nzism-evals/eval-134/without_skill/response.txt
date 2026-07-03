# Supplier Ransomware Incident — NZISM-Aligned Incident Response Obligations

## Immediate Context

A ransomware attack against a supplier holding your agency's data is a **third-party/supply-chain security incident** that still falls within your agency's incident response obligations, because the data compromised is your agency's information, regardless of where it was hosted or processed. You cannot delegate your notification and response obligations to the supplier — the agency remains accountable.

## 1. Immediate Actions

1. **Activate your incident response plan** — treat this as a confirmed/suspected data security incident, not merely a "vendor issue." Convene your incident response team (ITSM/CISO, legal, communications, business owners of the affected data).
2. **Contain and assess** — work with the supplier to understand:
   - What agency data was held/accessed by the affected systems
   - Whether the ransomware involved data exfiltration (double extortion) or encryption only
   - The classification of the data involved (this materially changes the severity and notification obligations — RESTRICTED or higher data is treated with much greater urgency)
   - Timeline of the incident and when the supplier became aware
3. **Preserve evidence** — ensure the supplier preserves logs and forensic evidence; do not allow premature remediation that destroys evidence needed for investigation.
4. **Review your contract** with the supplier for its incident notification and cooperation obligations (breach notification timeframes, audit rights, liability provisions) — invoke these immediately.

## 2. NZISM-Aligned Incident Response Obligations

The NZISM requires agencies to have a documented incident management process, including:
- **Detection and reporting** — incidents must be identified, logged, and escalated promptly
- **Categorisation/severity assessment** — based on classification of data involved and potential impact
- **Containment, eradication, and recovery** — coordinated response to limit damage and restore normal operations
- **Root cause analysis and lessons learned** — post-incident review to prevent recurrence
- **Notification to appropriate authorities** — depending on severity and data classification, this includes national cyber security authorities as outlined below

Because this incident involves a **third-party supplier**, you should also review whether your supplier/vendor risk management and contractual security obligations (which the NZISM expects agencies to have in place for third parties handling classified or sensitive information) were adhered to, and whether the supplier met their contractual security and notification obligations.

## 3. Who You Must / Should Notify in New Zealand

### a. National Cyber Security Centre (NCSC), part of the GCSB
The NCSC is New Zealand's lead technical authority for cyber security incidents affecting government agencies and nationally significant organisations. Any significant cyber incident affecting an NZ government agency — particularly one involving ransomware, third-party compromise, or classified/sensitive data — should be reported to the NCSC as a priority. The NCSC can provide technical assistance, threat intelligence correlation with other incidents, and coordination support.

### b. CERT NZ
CERT NZ is New Zealand's national computer emergency response team providing incident response support and coordination, historically for a broader range of organisations including businesses and the public. Depending on current organisational arrangements (CERT NZ's functions and how they interface with the NCSC may evolve over time), you should report the incident to whichever of NCSC/CERT NZ is the current designated channel for government agency incidents — check current guidance, as functions have been consolidating.

### c. Government Chief Digital Officer (GCDO) / Department of Internal Affairs
For a government agency, significant security incidents (especially those affecting service delivery or involving classified data) are typically expected to be reported through whole-of-government reporting channels, potentially including the GCDO, consistent with NZ government's cyber security and digital service expectations.

### d. Privacy Commissioner (Office of the Privacy Commissioner)
If the compromised data includes **personal information**, this is very likely a **notifiable privacy breach** under the Privacy Act 2020. New Zealand's mandatory breach notification regime requires notification to:
- The **Privacy Commissioner**, and
- **Affected individuals**

where the breach has caused, or is likely to cause, **serious harm**. Given ransomware groups increasingly exfiltrate data before encrypting it, you must assess whether personal information was exposed and treat this notification obligation with urgency — it operates on its own statutory timeframe ("as soon as practicable" after becoming aware) independent of your NZISM-based technical incident response.

### e. Your Agency's Own Governance Chain
- **Accreditation Authority / Chief Executive** — significant incidents affecting an accredited system should be reported up to the Accreditation Authority, as it may affect the ongoing validity of the system's accreditation.
- **Minister's Office** (via your agency's usual protocols), if the incident is likely to attract public, political, or media attention — common for government agency data breaches.
- **Internal audit and risk committees**, per your agency's governance requirements.

### f. Law Enforcement (NZ Police)
Ransomware is a criminal act. Consider reporting to **NZ Police** (particularly if there is a fraud, extortion, or ransom demand element), in coordination with the NCSC.

### g. Insurance Provider
If the agency or supplier holds cyber insurance, notify the insurer promptly, as many policies have strict notification windows and may dictate the use of specific incident response/forensic providers.

## 4. Ransom Payment Considerations

NZ Government guidance (via NCSC/CERT NZ) generally **discourages paying ransoms**, as it does not guarantee data recovery or deletion, funds further criminal activity, and may mark the organisation as a repeat target. This decision would primarily fall to the supplier as the entity directly compromised, but your agency should make clear its expectations and may need to factor this into its own risk assessment and communications.

## 5. Post-Incident Actions

1. **Formal post-incident review** — document root cause, supplier's response adequacy, and your agency's own response effectiveness.
2. **Reassess the supplier relationship** — determine whether the supplier's security controls met contractual obligations, and whether continued use of the supplier (or specific remediations) is warranted.
3. **Update your Security Risk Management Plan and vendor risk assessments** to reflect lessons learned.
4. **Consider whether the incident affects your system's accreditation status**, particularly if it involved a system handling RESTRICTED or higher classified information.
5. **Communicate with affected individuals/stakeholders** as required by the Privacy Act and any sector-specific obligations.

## Summary — Notification Checklist

- [ ] Internal incident response team activated (ITSM/CISO, legal, comms)
- [ ] NCSC (GCSB) notified
- [ ] CERT NZ notified (or current equivalent government incident reporting channel — verify current arrangements)
- [ ] Privacy Commissioner notified if personal information involved (mandatory under Privacy Act 2020 if serious harm threshold met)
- [ ] Affected individuals notified if required
- [ ] Agency Accreditation Authority / Chief Executive briefed
- [ ] NZ Police notified if appropriate
- [ ] Insurer notified
- [ ] Supplier contractual notification/cooperation obligations invoked
- [ ] Post-incident review scheduled

*Note: Specific reporting channels, statutory thresholds, and the current division of responsibilities between NCSC and CERT NZ should be verified against current published guidance, as government incident-reporting arrangements are periodically restructured. This response reflects general knowledge of the NZ incident notification landscape and should not be treated as a substitute for consulting current official guidance during an active incident.*
