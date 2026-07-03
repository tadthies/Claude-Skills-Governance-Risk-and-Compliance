Short answer: **No — ISO 27001:2022 certification does not automatically make you NIS2 compliant.** It's strong *evidence* toward compliance and covers a large share of the Art. 21 risk management measures, but it does not substitute for the formal legal obligations NIS2 imposes. NIS2 compliance is a legal/regulatory status determined by your entity classification and direct fulfilment of Articles 20, 21, 22, and 23 — not by holding a certificate.

Below is how the two frameworks relate and where the real gaps are.

## Why certification isn't the same as compliance

ISO 27001 is a voluntary, certifiable management-system standard. NIS2 is a binding EU legal instrument (Directive (EU) 2022/2555, transposed into national law) with its own scope-in criteria (Annex I/II sector + size thresholds under Art. 3), its own supervisory regime (Art. 32/33), and its own penalty regime (Art. 34: up to €10M / 2% global turnover for Essential Entities, €7M / 1.4% for Important Entities). You can be fully ISO 27001 certified and still be non-compliant with NIS2 if, for example, you haven't registered with your national competent authority, haven't documented management-body approval of your risk measures, or don't have an operational 24h/72h/1-month incident reporting workflow.

## Where ISO 27001 covers NIS2 well

ISO 27001:2022 Annex A controls map closely to most of the ten Art. 21(2) risk management measures:

| NIS2 Art. 21 Measure | ISO 27001:2022 Coverage |
|---|---|
| M1 Risk analysis & IS policies | A.5.1, A.6.1, A.8.8, Clause 6.1, Clause 8.2 |
| M2 Incident handling | A.5.24–A.5.28 |
| M3 BCP/DR/crisis management | A.5.29, A.5.30, A.8.13, A.8.14 |
| M4 Supply chain security | A.5.19–A.5.23 |
| M5 Secure acquisition & development | A.8.25–A.8.30, A.5.8 |
| M6 Effectiveness assessment | A.5.35, A.5.36, Clause 9.1–9.3 |
| M7 Cyber hygiene & training | A.6.3, A.5.7, A.6.8 |
| M8 Cryptography | A.8.24 |
| M9 HR, access control, asset mgmt | A.5.9–A.5.11, A.8.2–A.8.4, A.6.1, A.6.5 |
| M10 MFA & secure comms | A.8.5, A.8.20, A.8.26, A.8.24 (partial — see gap below) |

If your ISMS is well-implemented (not just certified on paper), most of the substantive control content for Art. 21 is likely already in place.

## Where the real gaps are

**1. Art. 20 — Governance and personal liability.** ISO 27001 has no equivalent to NIS2's requirement that management bodies *approve* cybersecurity risk management measures, *oversee* their implementation, and undergo *regular training* — with **personal liability** attaching under Member State law. Action: produce documented board/management approval minutes for your risk management measures, and maintain training records specifically for management body members (not just general staff awareness training).

**2. Art. 23 — Incident reporting timelines.** ISO 27001 A.5.24–A.5.26 cover incident management generally but have no prescriptive timeline. NIS2 requires:
- 24 hours: early warning to CSIRT/competent authority (is it malicious? cross-border impact?)
- 72 hours: incident notification with initial severity/impact/IoC assessment
- 1 month: final report with root cause, mitigations, cross-border impact

Action: build an explicit NIS2 notification track into your incident response plan — pre-drafted CSIRT templates, named notification owners, and timeline checkpoints baked into your runbook. This is usually the biggest operational gap for newly in-scope entities.

**3. Art. 21(2)(j) — MFA mandate.** ISO 27001 A.8.5 covers "secure authentication" but doesn't universally mandate MFA. NIS2 explicitly requires MFA/continuous authentication, secured communications, and secured emergency communications. Action: confirm MFA is deployed for all remote access, privileged/administrative accounts, and cloud management consoles — not just where your risk assessment happened to prioritize it.

**4. Art. 22 — Coordinated supply chain risk assessments.** ISO 27001 A.5.19–A.5.23 cover supplier relationships generally, but NIS2 ties supply chain security to ENISA/Cooperation Group coordinated risk assessments of *critical* ICT supply chains. Action: monitor ENISA and your national authority's supply chain advisories and feed relevant findings into your supplier risk register — this is a more dynamic, externally-driven process than standard ISO supplier reviews.

**5. Entity classification and registration.** This has no ISO 27001 analogue at all. You need to confirm whether you're an Essential or Important Entity under Art. 3 (Annex I/II sector plus the ≥50 employee / ≥€10M turnover threshold, as extended by your Member State's transposition law), and most Member States require self-registration with the national competent authority — a purely regulatory step with no certification counterpart.

## Recommended next steps

1. Confirm your entity classification (EE/IE) and registration status with the national competent authority.
2. Document Art. 20 management-body approval and maintain board-level training records.
3. Stand up an explicit Art. 23 notification workflow (24h/72h/1-month) layered on top of your existing ISO 27001 incident management process.
4. Audit MFA coverage against the Art. 21(2)(j) mandate specifically — don't rely on "authentication is covered" being equivalent to "MFA is universal."
5. Integrate ENISA/national supply chain risk assessment outputs into your supplier risk register (Art. 22 / Art. 21(2)(d)).
6. If you are a DNS/cloud/data-centre/MSP/MSSP/trust-service or similar digital infrastructure entity, don't stop at the ten-measure level — Commission Implementing Regulation (EU) 2024/2690 breaks Art. 21(2) into 13 technical Annex sections with audit-level sub-requirements and defines significant-incident thresholds (baseline: financial loss above €500,000 or 5% of annual turnover, whichever is lower). Real gaps for these entity types typically surface at that sub-measure level, not the high-level Art. 21 mapping shown above.

**Bottom line:** treat ISO 27001 certification as a strong technical and organizational foundation — probably 70-80% of the Art. 21 control substance — but NIS2 compliance additionally requires governance accountability (Art. 20), a prescriptive incident reporting workflow (Art. 23), universal MFA, active supply-chain risk coordination (Art. 22), and formal regulatory registration, none of which ISO 27001 certification alone demonstrates.
