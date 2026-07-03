# SWIFT Incident Response Obligations — Malware on SWIFT-Connected Server

## Situation Assessment

You have discovered malware on a SWIFT-connected server and suspect fraudulent transactions may have been sent. This constitutes a **confirmed cyber incident affecting the SWIFT environment** and triggers mandatory obligations under CSCF v2026 Control 7.1 — Cyber Incident Response Planning.

Act immediately. Every hour of delay increases potential financial exposure and may constitute a breach of your SWIFT notification obligations.

---

## Immediate Actions (First 2 Hours)

### Priority 1: Containment — Do This Now

1. **Isolate the affected server(s) from the SWIFT zone** — remove network connectivity (physically unplug or apply firewall rules) to stop further unauthorized SWIFT message transmission. Do NOT power off the server — preserve volatile memory for forensic analysis.

2. **Revoke all SWIFT operator credentials on the affected system** — assume any credentials cached on or accessible from the affected server are compromised. Immediately revoke all hardware tokens and passwords for operators who accessed the system.

3. **Halt transaction processing** — suspend automated message sending until you can verify transaction integrity. Contact your SWIFT Relationship Manager to flag potential fraudulent traffic.

4. **Preserve volatile state** — before any remediation, capture system memory dumps (RAM) from the affected server(s). This is time-critical — volatile memory is lost on reboot.

5. **Convene your SWIFT Incident Response Team** — activate your SWIFT-specific IRP. Notify your CISO, Head of Treasury Operations, and your SWIFT Relationship Manager.

---

## Notification Obligations Under Control 7.1

### Obligation 1: SWIFT Notification Within 24 Hours

**You must notify SWIFT within 24 hours of confirming a cyber incident affecting your SWIFT environment.**

| Notification | Detail |
|-------------|--------|
| Recipient | SWIFT CISO team |
| Contact | **security@swift.com** |
| Deadline | **24 hours from confirmation of the incident** |
| What to include | Nature of incident, affected systems, whether fraudulent transactions are suspected, current containment status |

> "Confirmation" means you have reasonable grounds to believe a cyber incident has occurred — not that you have completed your forensic investigation. Do not wait for full forensic confirmation before notifying.

### Obligation 2: Full Incident Report Within 30 Days

Within **30 days** of the initial notification, you must provide SWIFT with a full incident report covering:
- Root cause analysis
- Attack vector and timeline
- All affected systems and data
- Transaction impact (confirmed fraudulent messages, if any)
- Remediation actions taken
- Preventive measures implemented

This report is submitted through the KYC-SA portal or directly to your SWIFT Relationship Manager.

### Additional Notifications to Consider

| Party | Timing | Basis |
|------|--------|-------|
| **SWIFT Relationship Manager** | Immediately (concurrent with security@swift.com) | Operational disruption management |
| **Your regulators** (central bank, financial regulator) | Per local regulations — often 24–72 hours | Regulatory obligation (varies by jurisdiction) |
| **Correspondent banks** | As soon as fraudulent transactions are identified | Commercial obligation; counterparty fraud risk |
| **Law enforcement** (national cybercrime unit) | As appropriate | Fraud investigation |
| **Cyber insurer** | Per policy terms — typically 24–72 hours | Insurance notification requirement |

---

## Evidence to Preserve

Preserve the following before any remediation or system rebuilding. Failure to preserve evidence may impede your forensic investigation and regulatory response.

| Evidence Type | Description | Priority |
|--------------|-------------|---------|
| **System memory dumps** | Full RAM capture from affected SWIFT server(s) before any reboot — captures malware running in memory, process lists, network connections | IMMEDIATE |
| **SWIFT transaction logs** | All Alliance Access message logs (MT/MX) from the affected period — identify all outgoing messages, sender reference numbers, transaction amounts | IMMEDIATE |
| **SWIFT zone firewall/network logs** | Network flow data and firewall logs covering the period of infection — trace attacker lateral movement and exfiltration | HIGH |
| **Authentication logs** | All operator logon events, failed authentication attempts, and session records from SWIFT systems | HIGH |
| **SIEM / log aggregator data** | Export and preserve all SWIFT-related events from your SIEM covering at least 30 days prior to incident discovery | HIGH |
| **Endpoint forensic images** | Full disk images of affected SWIFT server(s) using forensic imaging tools (e.g., FTK Imager, dd) — create write-protected copies | HIGH |
| **Malware samples** | Capture and quarantine (do not delete) the malware files found — provide to your forensic team and SWIFT if requested | MEDIUM |
| **Network captures** | If network tap/capture capability exists, preserve PCAP files from the SWIFT zone network for the incident period | MEDIUM |
| **Change records** | Recent change management records for affected systems — help establish baseline and identify unauthorized changes | MEDIUM |
| **Email and communication records** | Internal communications discussing the incident (preserve for legal/regulatory response) | MEDIUM |

**Chain of custody:** All evidence should be collected with documented chain of custody. Note who collected what, when, from which system, and where it is stored.

---

## What Your SWIFT-Specific IRP Must Contain

Control 7.1 requires a SWIFT-specific Incident Response Plan distinct from your general IT IRP. If your IRP does not yet contain these elements, document them now and incorporate them into a formal plan:

### Required IRP Elements

1. **SWIFT-specific detection triggers**
   - Anomalous SWIFT transaction volumes or amounts
   - Unusual BIC destination patterns
   - Unauthorized operator logon to Alliance Access
   - Malware alerts on SWIFT-connected servers
   - Failed integrity checks on SWIFT software (Control 6.2)

2. **Escalation to SWIFT within 24 hours**
   - Explicit procedure naming security@swift.com as the notification contact
   - Named individuals responsible for making the notification
   - Template for the initial SWIFT notification email
   - Escalation path if primary contact is unavailable

3. **Fraud scenario playbooks**
   - Specific playbook for: suspected unauthorized SWIFT transaction
   - Specific playbook for: malware on SWIFT-connected endpoint
   - Specific playbook for: compromised SWIFT operator credentials
   - Each playbook should include decision points for transaction recall initiation

4. **Transaction recall procedures**
   - Procedure for contacting correspondent banks to request transaction recalls
   - Named contacts at SWIFT Operations for emergency assistance
   - Process for gpi tracker investigation (if on SWIFT gpi)

5. **Communication with correspondent banks**
   - Template communications for notifying counterparties of potential fraudulent messages
   - Contact list for key correspondent bank security teams
   - Guidance on which counterparties to notify based on transaction destination

6. **Evidence preservation procedures**
   - The specific list of evidence types above
   - Named individuals responsible for evidence collection
   - Storage location and access controls for preserved evidence

7. **Recovery and return-to-service criteria**
   - Security criteria that must be met before reconnecting to SWIFT
   - SWIFT approval process for return to service after a significant incident
   - Testing requirements before resuming live transaction processing

---

## Immediate Next Steps Checklist

- [ ] Isolate affected server(s) from SWIFT network — do NOT power off
- [ ] Capture system memory dumps immediately
- [ ] Revoke all operator credentials and hardware tokens on affected systems
- [ ] Notify security@swift.com — target within the next few hours to ensure 24-hour deadline is met
- [ ] Notify your SWIFT Relationship Manager
- [ ] Engage your forensic incident response vendor (external IR firm if needed)
- [ ] Begin preserving all log and forensic evidence listed above
- [ ] Review all SWIFT transactions sent in the past 24–72 hours for anomalies
- [ ] Notify your regulators per local requirements
- [ ] Contact cyber insurer
- [ ] Convene crisis management team for ongoing coordination

The 24-hour SWIFT notification clock is running. Make the notification to security@swift.com your first external action after containment steps are underway.
