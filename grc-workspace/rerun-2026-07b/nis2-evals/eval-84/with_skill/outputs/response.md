# ISO 27001:2022 vs. NIS2: Does Certification Equal Compliance?

## Short answer
No. ISO 27001:2022 certification is a **strong implementation vehicle** for much of NIS2's Art. 21(2) risk-management measures — but it is **not a safe harbor**. Certification evidences substantial coverage of several Art. 21(2) sub-measures, but it does not, by itself, satisfy NIS2's Art. 23 incident-reporting timelines, Art. 20 governance/personal-accountability requirements, Art. 27 registration, or the explicit MFA and cryptography expectations in Art. 21(2)(h) and (j). You remain independently responsible for meeting NIS2 obligations directly.

## Where ISO 27001 gives you strong coverage

| NIS2 Art. 21(2) Measure | ISO 27001:2022 Annex A Controls Covering It |
|---|---|
| (a) Risk analysis & InfoSec policies | A.5.1 Policies; A.6.1 IS roles; A.8.8 Vulnerability management; Clause 6.1 Risk assessment; Clause 8.2 IS risk assessment |
| (b) Incident handling | A.5.24 IS incident planning; A.5.25 Assessment of IS events; A.5.26 Response; A.5.27 Post-incident review; A.5.28 Evidence collection |
| (c) Business continuity / DR / crisis | A.5.29 IS during disruption; A.5.30 ICT readiness; A.8.13 Backup; A.8.14 Redundancy |
| (e) Secure acquisition/development | A.8.25–A.8.30 (Secure dev lifecycle, app security, secure architecture, secure coding, testing, outsourced dev); A.5.8 IS in project management |
| (f) Effectiveness assessment | A.5.35 Independent IS review; A.5.36 Policy compliance; Clause 9.1 Monitoring; Clause 9.2 Internal audit; Clause 9.3 Management review |
| (i) HR security, access control, asset management | A.5.9–A.5.11 Asset inventory/use/return; A.8.2–A.8.4 Privileged access, restriction, source code; A.6.1 Screening; A.6.5 Termination responsibilities |

This is genuinely useful — a well-run ISMS gives you documented policies, tested processes, and audit evidence across roughly six of the ten Art. 21(2) measures.

## Where real gaps remain

### 1. Art. 20 — Governance and personal liability (no ISO 27001 equivalent)
ISO 27001 has no construct for the **personal liability of management body members** that NIS2 introduces. NIS2 requires your management body to formally **approve** the Art. 21 risk-management measures, **oversee** their implementation, and undergo (and offer staff) cybersecurity **training** — with infringement exposing individuals to personal liability under national law, and for essential entities, potential temporary suspension from managerial duties.
- **Gap:** ISO 27001's Clause 5 (Leadership) covers organizational commitment but not this specific accountability/liability regime.
- **Action:** produce board-level approval minutes for your risk-management measures, maintain management-body training records, and add cyber oversight as a standing board agenda item. This is the single most commonly missing piece of evidence in ISO-certified organizations approaching NIS2.

### 2. Art. 23 — Incident reporting timelines (more prescriptive than ISO 27001)
ISO 27001 A.5.24–A.5.28 cover incident management as a *process*, but say nothing about NIS2's specific clock: **24-hour early warning, 72-hour notification, on-request intermediate reports, and a final report within 1 month.**
- **Gap:** your ISMS incident response plan almost certainly lacks a NIS2-specific notification track to your national CSIRT/competent authority with these exact checkpoints.
- **Action:** build pre-drafted CSIRT notification templates for each of the four report types, define the "significant incident" threshold per Art. 23(3) (or the 2024/2690 quantitative thresholds if you're a covered digital-infrastructure entity), and add explicit timeline checkpoints to your incident runbooks. If personal data may be involved, also build the parallel GDPR Art. 33 track — different report, different recipient, different clock, and ISO 27001 doesn't address this coordination either.

### 3. Art. 27 — Registration (no ISO 27001 equivalent)
ISO 27001 has no registration construct at all. NIS2 requires most in-scope entities to register with their national competent authority; digital-infrastructure-type entities (DNS, cloud, MSP/MSSP, etc.) must additionally submit identifying details (name, sector, address, IP ranges, contact) for onward submission to ENISA's registry.
- **Action:** confirm you are registered with your national authority under Art. 27. Certification does nothing here — this is a standalone administrative obligation.

### 4. Art. 21(2)(d) — Supply chain security tied to EU coordinated risk assessments (Art. 22)
ISO 27001 A.5.19–A.5.23 cover supplier relationships, agreements, ICT supply chain, monitoring, and cloud services generally — solid foundational coverage. But NIS2 explicitly ties supply chain security to **EU-level coordinated risk assessments** conducted by the Cooperation Group, Commission, and ENISA under Art. 22 (these have targeted specific technology/sector risks, e.g., telecom equipment).
- **Gap:** ISO 27001 doesn't require you to monitor or act on ENISA/Cooperation Group coordinated risk assessment outputs.
- **Action:** add a process to track ENISA and national-authority supply chain risk advisories and feed them into your existing supplier risk register.

### 5. Art. 21(2)(j) — MFA is explicitly mandated, not just referenced
ISO 27001 A.8.5 (Secure authentication) covers authentication generally, but MFA is not universally required under ISO 27001 — it's a risk-based decision under the ISMS. NIS2 is explicit: multi-factor or continuous authentication, secured voice/video/text communications, and secured emergency communication systems are named requirements.
- **Gap:** if your ISMS risk-accepted MFA gaps anywhere (legacy systems, certain admin paths), that's an ISO-compliant decision but a potential NIS2 gap.
- **Action:** deploy MFA as a floor for all remote access, privileged accounts, and cloud management consoles — treat this as non-negotiable rather than risk-based. Also stand up a documented emergency/out-of-band communications plan for use if primary systems are compromised (this typically doesn't exist even in mature ISMS programmes).

### 6. Art. 21(2)(h) — Cryptography policy specificity
A.8.24 (Use of cryptography) exists in ISO 27001, but confirm your policy is specific enough to withstand NIS2-level audit scrutiny (approved algorithms, key management lifecycle, defined triggers for when encryption is mandatory) rather than a general statement of intent.

## Controls with no direct NIS2 mapping (still useful, but don't expect audit credit)
A.5.2 (IS roles), A.5.31 (legal/regulatory requirements), A.5.32 (IP rights), A.5.33 (protection of records), A.5.34 (privacy/PII — relevant to GDPR rather than NIS2 directly), A.6.4 (disciplinary process), A.8.1 (endpoint devices), A.8.9 (configuration management), A.8.10 (information deletion).

## Recommended path forward for an ISO 27001-certified entity

1. **Confirm your entity classification** — verify Essential vs. Important Entity status under Art. 3 and your Member State's transposition law; this determines supervisory intensity and fine exposure, and ISO 27001 doesn't touch this at all.
2. **Close the Art. 20 governance gap** — board approval documentation and training records, now.
3. **Build the Art. 23 reporting workflow** as an explicit overlay on your existing IR plan, with CSIRT-specific templates and timeline checkpoints.
4. **Extend supply chain security** to incorporate Art. 22 coordinated risk assessment monitoring.
5. **Mandate MFA** universally rather than risk-basing it, and document an emergency communications plan.
6. **Register under Art. 27** with your national competent authority if not already done.
7. Run a formal gap assessment scoring each Art. 21(2) sub-measure (✅ Compliant / 🟡 Partial / 🔴 Gap) against your existing ISO 27001 evidence, prioritizing quick wins (governance documentation, MFA enforcement) within 30 days and structural items (CSIRT reporting workflow, supply chain process) within 6 months.

**Bottom line:** treat your ISO 27001 ISMS as the backbone of your NIS2 programme, not the finish line. The gaps above are precisely where auditors and competent authorities will focus, because they are the areas NIS2 added beyond standard information security management practice.

*This is general compliance information, not legal advice. Consult qualified counsel or an accredited assessor to confirm your specific compliance status.*
