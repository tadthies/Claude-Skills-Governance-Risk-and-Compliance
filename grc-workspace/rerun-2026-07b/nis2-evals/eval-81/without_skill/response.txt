# NIS2 Applicability Assessment: European Electricity Distribution Operator

## Short Answer

**Yes**, your company almost certainly falls under the NIS2 Directive, and it would be classified as an **Essential Entity**.

## Why You Are In Scope

NIS2 (Directive (EU) 2022/2555) applies to entities operating in sectors listed in Annexes I and II that meet the size-cap criteria (medium or large enterprise), unless a specific exemption applies.

**Sector test:** Energy — specifically electricity — is listed in **Annex I (Sectors of High Criticality)**. Electricity distribution system operators (DSOs) are explicitly named as a sub-sector entity type within the energy sector, alongside electricity producers, suppliers, transmission system operators (TSOs), nominated electricity market operators, and (in the electricity sub-sector) certain other market participants.

**Size-cap test:** The general rule under Article 2 is that NIS2 applies to medium and large entities:
- Medium: ≥50 employees OR ≥€10M annual turnover/balance sheet (and below large thresholds)
- Large: ≥250 employees OR >€50M turnover / >€43M balance sheet

At 200 employees and €50M turnover, you qualify as a **medium-sized enterprise** at minimum (some interpretations may push you toward "large" depending on balance sheet figures, but medium is sufficient to be in scope).

**Important nuance for electricity DSOs:** Because electricity is deemed a highly critical sub-sector, many Member States — and Germany in particular — apply special rules. Under German transposition (the NIS2UmsuCG, implementing the amended BSI-Gesetz), operators of "critical facilities" in the energy sector, including electricity distribution grid operators, can be captured **regardless of the standard size-cap thresholds** if they meet sector-specific criticality thresholds (e.g., supplying a minimum number of connected customers/end users, typically referencing thresholds analogous to the KRITIS regulation, around 500,000 or more connected customers historically, though NIS2 transposition may adjust this). Even setting that aside, at 200 employees / €50M turnover you clearly clear the standard medium-enterprise threshold, so size-cap exemption does not help you avoid scope.

## Classification: Essential vs. Important Entity

Given that:
1. Electricity is an Annex I (high-criticality) sector, and
2. Electricity distribution operators are explicitly identified as one of the entity types automatically treated as **Essential Entities** in the energy sector (this designation typically does not depend on size for DSOs and TSOs specifically, since grid operators are often designated as essential regardless of size under both the Directive's logic and German implementation practice),

You should expect to be classified as an **Essential Entity (wesentliche Einrichtung)** rather than an Important Entity. Essential Entities face the strictest regulatory treatment: proactive supervision (ex ante) rather than reactive/complaint-driven supervision (ex post), and higher potential fines.

## Key Obligations

### 1. Registration
You must register with the competent national authority — in Germany, the **BSI (Bundesamt für Sicherheit in der Informationstechnik)** — providing company name, address, contact details, relevant sub-sector, and Member States where you provide services. This must be kept up to date.

### 2. Cybersecurity Risk Management Measures (Article 21)
You must implement "appropriate and proportionate technical, operational and organisational measures" to manage risks to network and information systems, covering at minimum:
- Risk analysis and information system security policies
- Incident handling
- Business continuity and crisis management (backups, disaster recovery)
- Supply chain security, including relationships with direct suppliers/service providers
- Security in network and information systems acquisition, development, and maintenance, including vulnerability handling and disclosure
- Policies and procedures to assess the effectiveness of cybersecurity risk-management measures
- Basic cyber hygiene practices and cybersecurity training
- Policies on the use of cryptography and encryption
- Human resources security, access control policies, and asset management
- Use of multi-factor authentication (MFA), secured voice/video/text communications, and secured emergency communication systems where appropriate

Management bodies must **approve** these risk management measures, oversee their implementation, and can be held personally liable for non-compliance. Management must also undergo cybersecurity training.

### 3. Incident Reporting (Article 23)
For significant incidents, a strict multi-stage reporting timeline to the German CSIRT/BSI applies:
- **Early warning within 24 hours** of becoming aware
- **Incident notification within 72 hours** (updating the early warning, with initial assessment, severity, indicators of compromise)
- **Final report within one month** of the incident notification (detailed description, root cause, mitigation measures)

An incident is "significant" if it has caused or is capable of causing severe operational disruption or financial loss, or if it affects other persons through considerable material or non-material damage.

### 4. Supply Chain and Third-Party Risk
As an Essential Entity operating critical infrastructure, you must specifically assess the cybersecurity posture of key suppliers and service providers, particularly OT/ICS vendors, SCADA system suppliers, and grid management software providers.

### 5. Governance and Accountability
- Management bodies must approve and oversee cybersecurity measures and attend training
- Personal liability for management for gross negligence in oversight
- Regular internal risk assessments and audits

### 6. Supervision and Enforcement
As an Essential Entity, you are subject to **proactive/ex ante supervision** by BSI — including on-site inspections, off-site supervision, security audits, and requests for evidence of compliance — even absent any specific incident or complaint.

### 7. Sanctions
Non-compliance for Essential Entities can result in administrative fines of up to **€10 million or 2% of total worldwide annual turnover**, whichever is higher. Germany's implementing law also provides for personal management liability and potential temporary suspension of authorization to carry out managerial responsibilities in cases of serious/repeated breaches.

## Recommended Next Steps

1. Confirm exact classification (Essential Entity) and registration deadline/status directly with BSI, since Germany's specific transposition thresholds for the energy sector may layer additional criteria on top of the Directive's general size caps.
2. Conduct a gap assessment against Article 21 measures — many energy operators already have some coverage via IT-SiG 2.0 / prior KRITIS obligations, but NIS2 raises the bar (especially on supply chain and governance).
3. Establish a 24-hour incident detection and early-warning reporting capability tied into BSI's reporting channels.
4. Brief the management board on personal liability exposure and ensure formal approval/oversight of the cybersecurity risk management framework, plus completion of required training.
5. Review contracts with OT/SCADA vendors and IT suppliers for NIS2-aligned security requirements.

**Caveat:** Germany's national NIS2 transposition law had a protracted legislative process; you should verify the current status and exact German-specific criticality thresholds and deadlines with BSI or qualified German counsel, as national implementation details (especially sector-specific thresholds for energy/electricity) can differ from the baseline Directive text.
