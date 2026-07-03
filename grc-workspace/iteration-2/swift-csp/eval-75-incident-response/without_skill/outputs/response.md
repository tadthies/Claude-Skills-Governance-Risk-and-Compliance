# SWIFT CSP Control 7.1 — Cyber Incident Response Obligations

## Immediate Situation

Malware on a SWIFT-connected server with suspected fraudulent transactions is a critical incident. Every minute matters. Begin incident response immediately.

---

## Immediate Containment Actions

Before addressing reporting obligations, take these containment steps:

1. **Isolate the affected server(s)** from the SWIFT network and internal network — remove network connectivity but do NOT power off the server (preserve forensic evidence)
2. **Suspend SWIFT transaction processing** to prevent further potential fraud
3. **Revoke credentials** of any SWIFT operators who accessed the affected system
4. **Activate your incident response team** — CISO, Treasury, IT Security, Legal

---

## Notification Obligations Under SWIFT Control 7.1

### SWIFT Notification

SWIFT requires that you notify them promptly when a cyber incident affects your SWIFT environment or SWIFT messaging.

**Who to notify:** SWIFT security team
**Contact:** security@swift.com
**Timing:** SWIFT expects **initial notification within 24 hours** of discovering/confirming a cyber incident affecting your SWIFT environment

The initial notification should include:
- Nature of the incident (malware found, suspected fraudulent transactions)
- Systems affected
- Whether the incident is contained or ongoing
- Any initial findings

**Follow-up report:** A more detailed incident report is typically required within approximately **30 days**, covering the full investigation findings, root cause, impact, and remediation.

### Other Notifications to Consider

| Party | Timing |
|------|--------|
| Your banking regulator / central bank | Per local requirements — often 24–72 hours |
| Affected counterparties (if fraudulent transactions confirmed) | As soon as possible |
| SWIFT Relationship Manager | Concurrent with or immediately after security@swift.com |
| Law enforcement | As appropriate for fraud investigation |
| Cyber insurer | Per policy requirements |

---

## Evidence to Preserve

Do not modify or delete any evidence. Preserve:

| Evidence | Description |
|----------|-------------|
| **Memory dumps** | Capture RAM from affected server(s) before any reboot — malware often runs only in memory |
| **SWIFT transaction logs** | All Alliance Access message logs — identify potentially fraudulent transactions |
| **System event logs** | Windows Event Logs or syslog from affected server(s) |
| **Network logs** | Firewall logs and network flow data from the SWIFT zone for the incident period |
| **SIEM/log aggregator data** | Export relevant time period from your log management platform |
| **Disk images** | Forensic images of affected servers (using FTK Imager or equivalent) |
| **Authentication logs** | SWIFT operator logon events and session records |
| **Malware files** | Quarantine but preserve malware samples — do not delete |
| **Network captures** | PCAP files if network capture capability is available in the SWIFT zone |

Use documented chain of custody for all evidence collection.

---

## Immediate Containment Steps Summary

1. Isolate affected systems from the SWIFT zone (firewall isolation or physical disconnection)
2. Revoke compromised SWIFT operator credentials and hardware tokens
3. Notify your SWIFT Relationship Manager
4. Engage your forensic incident response team
5. Notify SWIFT at security@swift.com (target within first few hours to meet 24-hour obligation)
6. Review all SWIFT transactions in the preceding 24–72 hours for anomalies
7. Contact correspondent banks if fraudulent transactions are confirmed

---

## What a SWIFT-Specific IRP Must Contain

CSCF Control 7.1 requires a SWIFT-specific Incident Response Plan. A generic IT IRP is not sufficient. Your SWIFT-specific IRP should include:

### Required Elements

1. **SWIFT-specific detection triggers**
   - Anomalous transaction volumes, values, or destination BICs
   - Malware alerts on SWIFT-connected systems
   - Unauthorized operator access attempts
   - Alliance Access integrity failures

2. **Escalation to SWIFT within 24 hours**
   - Named contact responsible for SWIFT notification
   - security@swift.com as the mandatory notification contact
   - Template email for initial SWIFT notification
   - SWIFT Relationship Manager contact details

3. **Fraud scenario playbooks**
   - Playbook: suspected unauthorized SWIFT message transmission
   - Playbook: compromised SWIFT operator credentials
   - Playbook: malware on SWIFT-connected endpoint
   - Decision criteria for invoking transaction recall

4. **Communication with correspondent banks**
   - Process for notifying counterparties of potential fraudulent messages
   - Contact list for key correspondent security teams

5. **Evidence preservation procedures**
   - Specific list of evidence types to preserve
   - Responsible individuals and storage locations
   - Chain of custody documentation requirements

6. **Recovery and return to service**
   - Security criteria before reconnecting to SWIFT
   - Testing requirements before resuming live transactions
   - SWIFT approval process for return to service after significant incidents

---

## Key Takeaways

- **24-hour notification**: Notify SWIFT at security@swift.com within 24 hours of confirmed incident
- **30-day follow-up**: Full incident report due to SWIFT within approximately 30 days
- **Preserve evidence before remediation**: Do not reimage or power off servers until memory and disk images are captured
- **Do not delay**: The notification clock starts at the point of discovery/confirmation

If you do not currently have a SWIFT-specific IRP, this incident underscores the need to develop one. Engage SWIFT and your SWIFT Relationship Manager for guidance on incident handling procedures specific to your connectivity type.
