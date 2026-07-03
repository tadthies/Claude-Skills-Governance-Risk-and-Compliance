# SWIFT-Connected Malware Incident — Immediate Response Obligations (Control 7.1)

**Note on framework version:** You asked about CSCF v2025. The current governing version as of today is **CSCF v2026** (effective July 2026; v2025 was valid only through June 2026). Control 7.1 — Cyber Incident Response Planning — is **unchanged in substance between v2025 and v2026** (notification timelines and requirements carried forward), so the obligations below apply regardless of which version label you're tracking against. I'll flag the one relevant v2026 scoping note at the end.

This scenario — confirmed malware on a SWIFT-connected server with suspected fraudulent transaction submission — is a textbook **Control 7.1 notifiable cyber incident**, and it also intersects with **Control 6.1 (Malware Protection)**, which explicitly states malware found on SWIFT systems must be treated as a security incident under 7.1.

---

## Step-by-Step Incident Response Procedure

### 1. Immediate Internal Escalation (T+0, upon confirmation)
- Escalate to senior management / CISO **immediately** upon confirming the malware and suspected fraud — this must happen before or in parallel with external notification, not after.
- Activate your SWIFT-specific Incident Response Plan (IRP) under Control 7.1.
- Convene the incident response team (security, SWIFT operations, treasury/payments, legal, communications).

### 2. Containment (T+0 to T+few hours)
- Isolate the affected server from the network — but **do not power it off** if avoidable; preserve volatile memory where possible (see evidence section below).
- Suspend or revoke credentials/tokens for any operator accounts associated with the affected server (Control 5.1 / 5.2 response actions).
- Place a hold on outbound SWIFT message processing from the affected environment if fraud is suspected, pending verification.
- Notify your correspondent banks / counterparties on the receiving end of any suspected fraudulent messages so they can hold or recall payments — this is time-critical and separate from the SWIFT notification below.

### 3. Notify SWIFT — 24-Hour Deadline
- **Deadline: within 24 hours of confirming the cyber incident.**
- Notify via the **SWIFT CISO office** (security@swift.com) and your **SWIFT relationship manager**, and log the notification through the **KYC-SA portal**.
- This is a hard, mandatory obligation under Control 7.1 — malware on a SWIFT-connected system with suspected fraudulent transactions clearly meets SWIFT's definition of a notifiable incident (unauthorised access, compromised credentials, fraudulent/anomalous transactions, and malware on SWIFT systems are all independently listed triggers — you have at least two of them here).

### 4. Regulatory and Law Enforcement Notification
- Notify your financial regulator and law enforcement **per local jurisdictional requirements** — timelines vary (e.g., this may also trigger separate obligations under DORA, NY DFS 23 NYCRR 500, MAS TRM, HKMA CFI, or APRA CPS 234 depending on jurisdiction — SWIFT CSP compliance is cross-referenced in several of these regimes).
- Coordinate legal/compliance on any customer or public disclosure obligations tied to suspected fraud.

### 5. Investigation and Full Report to SWIFT — 30-Day Deadline
- **Deadline: full incident report to SWIFT within 30 days** of the initial notification.
- Cooperate with any SWIFT-led investigation into the incident.
- Conduct root-cause analysis: how the malware entered the environment, dwell time, whether Controls 1.1 (environment protection), 1.4 (internet restriction), 2.2 (patching), 6.1 (malware protection), or 6.4 (log/monitoring) had gaps that enabled this.

### 6. Recovery
- Rebuild the affected server from known-clean images rather than remediating in place.
- Re-verify SWIFT software integrity (Control 6.2) — compare hashes against SWIFT-published checksums before returning the system to service.
- Rotate all credentials, tokens, and keys associated with the affected environment.
- Confirm with counterparties that any held/suspect payments have been resolved (cancelled, recalled, or confirmed legitimate) before resuming normal processing.

### 7. Lessons Learned
- Formal post-incident review, feeding back into the IRP and control environment.
- Document remediation actions and target dates for any control gaps identified — this becomes evidence for your next KYC-SA attestation cycle.

---

## Evidence to Preserve

Preserve evidence **before** remediation actions destroy it:

| Evidence Type | Detail |
|---|---|
| Forensic disk/memory images | Full forensic image of the affected server, including volatile memory if malware may be memory-resident |
| Malware sample | Isolated copy of the malware binary/artifact for analysis |
| SWIFT application logs | Alliance Access/Gateway logs covering the incident window and preceding weeks |
| Network logs | Firewall, IDS/IPS, and SIEM logs for the SWIFT zone and connected back-office segments |
| Authentication logs | Operator login events, MFA/token usage, privileged account activity around the incident window |
| Transaction records | Full detail of all SWIFT messages sent/received from the affected system, with timestamps, to identify which (if any) are fraudulent |
| Chain of custody documentation | Who collected what evidence, when, and how it was stored — required if this proceeds to law enforcement or litigation |
| Timeline log | Contemporaneous incident timeline: detection time, containment actions, notification times (internal, SWIFT, regulator) |

---

## What Your SWIFT-Specific Incident Response Plan Must Contain (Control 7.1 Compliance)

A generic corporate IRP is **not sufficient** — "no SWIFT-specific IRP" is one of the most common CSCF non-compliance findings. Your SWIFT-specific IRP (or SWIFT addendum to your general IRP) must document:

1. **Detection triggers specific to SWIFT** — malware alerts on SWIFT systems, anomalous transaction patterns, unauthorized access attempts, credential compromise indicators
2. **Triage and severity classification** — criteria for what constitutes a SWIFT-notifiable incident
3. **Containment procedures** — including the ability to isolate SWIFT infrastructure and suspend message processing
4. **Notification matrix** with named roles and deadlines:
   - Internal senior management — immediate
   - SWIFT (CISO office / KYC-SA portal) — within 24 hours
   - Full report to SWIFT — within 30 days
   - Regulators/law enforcement — per local jurisdiction
   - Correspondent banks/counterparties — as needed for fraud containment
5. **SWIFT contact list** — security@swift.com, your SWIFT relationship manager, kept current and tested
6. **Investigation procedures** — including cooperation obligations with SWIFT-led investigations
7. **Evidence preservation requirements** — forensic imaging, log retention/preservation holds, chain of custody
8. **Recovery procedures** — rebuild standards, software integrity re-verification (Control 6.2), credential rotation
9. **Fraud-specific scenarios** — SWIFT explicitly expects coverage of Bangladesh Bank-style attack scenarios (compromised credentials used to send fraudulent payment instructions) as part of Control 7.2 training and 7.1 planning
10. **Annual test requirement** — the IRP must be tested annually via tabletop exercise or live drill, with a dated test report retained as evidence

**Evidence artifacts an assessor will expect to see:**
- Dated, approved SWIFT Incident Response Plan document
- Last annual tabletop/drill test record
- SWIFT notification contact list (current)
- Sample incident log, if any incidents have occurred

---

## v2026 Scoping Note

Since you referenced v2025: the substantive change entering v2026 is **Control 2.4 (Back-Office Data Flow Security)** moving from Advisory to Mandatory. If the malware reached this server via an unencrypted/unauthenticated back-office connection (e.g., from a payment hub or core banking system into the SWIFT secure zone), that pathway is now itself a compliance gap you'll need to remediate and disclose as part of your root-cause analysis and next attestation — implement mutual TLS 1.2+ and network segmentation on that data flow per Control 2.4 (see remediation steps in the main control reference).
