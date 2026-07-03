# ISO 27001:2022 vs. NIS2: Does Certification Equal Compliance?

## Short Answer

**No.** ISO 27001:2022 certification is an excellent foundation and covers a substantial portion of what NIS2 requires, but it does **not** automatically make you NIS2 compliant. ISO 27001 is a voluntary, internationally-scoped information security management standard; NIS2 is an EU legal obligation with specific, mandatory requirements — some of which go beyond, or differ in nature from, what ISO 27001 certification verifies. Think of ISO 27001 as covering roughly 70-80% of the substance of Article 21, but NIS2 adds legal, procedural, and governance obligations that no ISMS certification, by itself, satisfies.

## Where ISO 27001:2022 Gives You Strong Coverage

Your existing ISMS likely already substantially addresses several NIS2 Article 21 measures:

- **Risk analysis and information security policies** — core to ISO 27001 Clause 6 (risk assessment/treatment) and Annex A controls
- **Asset management** — Annex A 5.9-5.14 (2022 version) covers asset inventory, acceptable use, return of assets
- **Access control** — Annex A 5.15-5.18, 8.2-8.5 (identity management, access rights, authentication)
- **Cryptography** — Annex A 8.24 explicitly covers policy on use of cryptography
- **Human resources security** — Annex A 6.1-6.8 (screening, terms of employment, awareness/training, disciplinary process)
- **Business continuity** — Annex A 5.29-5.30, 8.13-8.14 (ICT readiness for business continuity, redundancy)
- **Supplier relationships** — Annex A 5.19-5.22 (information security in supplier relationships, monitoring, change management)
- **System acquisition, development and maintenance** — Annex A 8.25-8.34 (secure development lifecycle, vulnerability management, testing)
- **Cyber hygiene / awareness** — Annex A 6.3 (awareness training)
- **Incident management** — Annex A 5.24-5.28 (incident management planning, assessment, response, learning)

This is genuinely strong overlap — ISO 27001:2022's Annex A structure maps closely onto the Article 21(2) list of minimum measures, which is not a coincidence, since both frameworks draw on similar risk-management best practices.

## Where Gaps Are Likely to Exist

### 1. Scope Mismatch
ISO 27001 certification scope is **self-defined** — you choose the boundary (e.g., "our SaaS platform" or "our London office"). NIS2 applies to your **entire entity** as a legal person providing the relevant essential/important service. If your ISO 27001 certificate covers only part of the organization or a specific product line, you have an immediate scope gap: NIS2 doesn't care about your certification boundary, it cares about the systems/networks supporting your regulated service.

### 2. No Direct Legal Reporting Obligation
ISO 27001 requires you to have an incident management *process*, but it does not require — or verify — that you report significant incidents to a **government CSIRT/competent authority within 24 hours (early warning), 72 hours (notification), and one month (final report)**. This specific, externally-facing regulatory reporting workflow is a NIS2-only obligation. Most organizations have to build this notification capability from scratch, including knowing exactly which authority to contact and via what channel, and training staff on the "significant incident" threshold test under Article 23 (which is a different test than ISO 27001's internal incident severity classification).

### 3. Governance and Management Liability
NIS2 Article 20 imposes **direct, personal accountability on management bodies** — they must approve the cybersecurity risk-management measures, oversee implementation, and can face liability (and in some Member State transpositions, temporary bans from managerial roles) for non-compliance due to inadequate oversight. Management must also complete cybersecurity training. ISO 27001 requires "top management commitment" (Clause 5) but this is far softer than NIS2's statutory personal liability regime — an ISO audit does not test whether your board has formally approved a risk-management framework in the way a NIS2 regulator will expect to see documented.

### 4. Supply Chain Security — Different Depth
ISO 27001:2022 added supplier relationship controls, but NIS2's Article 21(2)(d) requirement for supply chain security is more expansive — it explicitly expects entities to assess the cybersecurity practices of their suppliers and service providers, and in some cases follow sector/EU-level coordinated risk assessments (as have been done for 5G and other critical supply chains). NIS2 supply chain expectations are evolving via ENISA and Cooperation Group guidance and may exceed what a standard ISO 27001 supplier-risk process covers, particularly for direct suppliers of ICT products/services critical to your essential/important service.

### 5. Registration with National Competent Authority
There is no ISO 27001 equivalent to NIS2's requirement to **register** with your national competent authority (providing entity details, contact points, sub-sector, Member States of operation) and keep this registration current. This is a purely regulatory administrative obligation.

### 6. Jurisdiction-Specific Legal Requirements
NIS2 is transposed into **national law** by each Member State, and national transpositions can add extra requirements beyond the Directive's text (e.g., Germany's BSI-Gesetz amendments, specific national reporting portals, additional sector thresholds). ISO 27001 is the same standard everywhere; NIS2 compliance is jurisdiction-specific and depends on where you're established/operating and which national law applies to you.

### 7. Sanctions/Enforcement Exposure Is Different in Kind
Failing an ISO 27001 surveillance audit risks losing your certificate (a commercial/reputational consequence). Failing NIS2 compliance risks **statutory administrative fines** (up to €10M or 2% of global turnover for Essential Entities; up to €7M or 1.4% for Important Entities), potential **binding instructions from the regulator**, and possible **personal liability for management**. The consequence structure is fundamentally different — legal/regulatory rather than purely commercial.

### 8. "Appropriate and Proportionate" Is a Regulatory Judgment, Not a Certification
ISO 27001 gives you a certificate saying your ISMS conforms to the standard as audited by your certification body. NIS2 compliance is ultimately judged by your **national competent authority**, potentially through inspections, audits, and information requests — a different evaluator, applying a different (statutory) standard of "appropriate and proportionate to the risk," not the ISO auditor's conformance checklist. You could be ISO 27001 certified and still receive an enforcement finding if the regulator judges your measures disproportionate to your actual risk profile.

### 9. Business Continuity / Crisis Management at the Entity Level
NIS2 explicitly requires business continuity measures including backup management, disaster recovery, and **crisis management** — ISO 27001 covers ICT readiness for business continuity but doesn't mandate an organization-wide crisis management structure (e.g., a defined crisis team, escalation to executives/board, coordination with external stakeholders and regulators during a live incident) in the same explicit way.

### 10. Vulnerability Handling and Disclosure
Article 21(2)(e) explicitly calls out "vulnerability handling and disclosure" — ISO 27001:2022 added technological controls around vulnerability management (Annex A 8.8), but a formal **coordinated vulnerability disclosure policy** (how external researchers report vulnerabilities to you) is a more specific expectation under NIS2/ENISA guidance than what a typical ISO 27001 implementation includes by default.

## Recommended Gap Assessment Approach

1. **Scope reconciliation**: Map your ISO 27001 ISMS scope against your full legal entity and all systems/networks supporting your NIS2-regulated service(s). Extend scope if needed.
2. **Control-by-control crosswalk**: Map each NIS2 Article 21(2) measure (a) through (j) against specific ISO 27001:2022 Annex A controls and your Statement of Applicability, flagging partial or missing coverage.
3. **Build the regulatory reporting workflow**: Stand up the 24h/72h/1-month CSIRT notification process as a distinct capability, separate from your internal ISO 27001 incident management procedure, with clear ownership (likely legal/compliance + security operations jointly).
4. **Formalize governance**: Get explicit, documented management body approval of your cybersecurity risk-management framework; deliver management-specific cybersecurity training; document oversight activities (e.g., board/exec reporting cadence on cyber risk).
5. **Register with your competent authority** and confirm your entity classification (Essential vs. Important) and applicable sub-sector.
6. **Uplift supply chain risk management**: Move beyond ISO 27001's supplier controls to a documented, risk-tiered assessment of critical ICT suppliers specifically through a NIS2/cybersecurity lens.
7. **Legal review of national transposition**: Have local counsel confirm your specific Member State's implementing law for any jurisdiction-specific additions beyond the Directive baseline.

## Bottom Line

ISO 27001:2022 certification puts you well ahead of organizations starting from zero — you likely have 70-80% of the technical and organizational substance already in place. But NIS2 compliance requires: (1) confirming your full entity is in scope, not just your certified boundary; (2) building an external regulatory incident-reporting capability that ISO 27001 doesn't test; (3) formal governance/management liability documentation; (4) registration with your national authority; and (5) treating supply chain risk and vulnerability disclosure with NIS2-specific rigor. Treat ISO 27001 as your foundation and starting point for a formal NIS2 gap assessment — not as a substitute for one.
