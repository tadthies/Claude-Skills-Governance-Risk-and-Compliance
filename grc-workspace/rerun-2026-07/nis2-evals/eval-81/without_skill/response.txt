Short answer: Yes, you almost certainly fall under NIS2 — and given that you operate electricity distribution networks in Germany, you likely qualify regardless of your size, because energy distribution is one of the sectors where NIS2 disapplies the normal size-cap rule for certain entity types.

## 1. Do you fall under NIS2?

NIS2 (Directive (EU) 2022/2555) applies to entities operating in the sectors listed in Annex I ("sectors of high criticality") and Annex II ("other critical sectors") that meet the size-cap criteria, UNLESS a specific exemption applies that removes the size cap.

**Energy — and specifically electricity — is an Annex I "highly critical" sector.** Within the energy sector, NIS2 explicitly names subsectors including electricity, district heating/cooling, oil, gas, and hydrogen. Electricity distribution system operators (DSOs) are specifically and explicitly listed as an entity type in Annex I.

Critically, Article 2 of NIS2 states that **electricity undertakings performing the function of distribution** (i.e., DSOs, as defined in the EU's Electricity Market Directive 2019/944) are covered **regardless of their size** — this is one of the explicit carve-outs from the standard small/medium enterprise exemption in Article 2(2)(b) and the recitals. In other words, unlike most sectors where you need to hit 50+ employees AND €10M+ turnover to be in scope, electricity DSOs are captured even if they are small or micro enterprises, because grid distribution is deemed critical infrastructure regardless of the operator's size.

Your company (200 employees, €50M turnover) comfortably exceeds the general medium-enterprise threshold anyway (≥50 staff, >€10M turnover), so you are in scope on ordinary size-cap grounds as well — but it's worth knowing that even a much smaller DSO would still be caught.

**Conclusion: Yes, you fall under NIS2.**

## 2. What type of entity are you?

NIS2 splits in-scope organizations into two tiers: **Essential Entities (EE)** and **Important Entities (IE)**. The classification depends on sector, sub-sector, entity type, and size.

For the energy sector, electricity, Annex I designates several entity types as automatically **Essential Entities**, including:
- Electricity undertakings (as defined in Directive 2019/944) that carry out the function of **distribution** (i.e., DSOs)
- Electricity undertakings performing the function of **supply**
- Distribution system operators
- Transmission system operators
- Nominated Electricity Market Operators (NEMOs)
- Producers
- The Regional Coordination Centres (RCCs)

**As a distribution system operator, you are classified as an Essential Entity (EE)**, not merely an Important Entity. This is one of the categories where the Directive designates the entity type as "essential" outright — largely independent of the normal size-based EE/IE split — because grid distribution is considered indispensable critical infrastructure.

Being an Essential Entity carries the strictest regime under NIS2: EEs are subject to **proactive supervision** (i.e., your national competent authority — in Germany, the BSI, Bundesamt für Sicherheit in der Informationstechnik, potentially alongside the Bundesnetzagentur for sector-specific energy regulation) can conduct ex-ante audits, inspections, and security scans even without a prior indication of an incident. Important Entities, by contrast, are only subject to reactive/ex-post supervision (triggered after an incident or evidence of non-compliance).

## 3. Your key obligations under NIS2

As an Essential Entity operating electricity distribution in Germany, your key obligations fall into several buckets:

### a. Cybersecurity risk-management measures (Article 21)
You must implement "appropriate and proportionate" technical, operational, and organizational measures to manage risks to network and information systems, based on an **all-hazards approach**. NIS2 lists a minimum baseline that must be covered, including:
- Risk analysis and information system security policies
- Incident handling (prevention, detection, response)
- Business continuity and crisis management (backups, disaster recovery)
- Supply chain security, including security-related aspects of relationships with direct suppliers/service providers
- Security in network and information systems acquisition, development, and maintenance, including vulnerability handling and disclosure
- Policies and procedures to assess the effectiveness of cybersecurity risk-management measures
- Basic cyber hygiene practices and cybersecurity training
- Policies on the use of cryptography and encryption
- Human resources security, access control policies, and asset management
- Use of multi-factor authentication (MFA), secure communications, and secured emergency communication systems

Management bodies (your board/executive leadership) must **approve** these risk-management measures, **oversee implementation**, and can be held **personally liable** for non-compliance. Management must also undergo specific cybersecurity training.

### b. Incident reporting (Article 23)
For "significant incidents" you must notify your national CSIRT or competent authority (in Germany, the BSI) on a tight timeline:
- **Early warning within 24 hours** of becoming aware of the incident
- **Incident notification within 72 hours**, updating the early warning with an assessment of severity and impact
- **Final report within one month** of the incident notification (or a progress report if the incident is ongoing)

A "significant incident" is one that has caused or is capable of causing severe operational disruption/financial loss, or that affects other natural/legal persons by causing considerable material or non-material damage.

### c. Registration (Article 3 / national transposition)
Essential and important entities must register with the competent authority / national CSIRT, providing details such as company name, address, sector, contact information, and IP ranges. In Germany, this happens via the BSI.

### d. Supply chain risk management
You must assess and manage cybersecurity risks posed by direct suppliers and service providers, including the security practices of your ICT/OT vendors — highly relevant given the operational technology (SCADA, grid control systems) typical of a DSO.

### e. Supervision, audits, and enforcement
As an Essential Entity, you should expect:
- **Proactive** supervisory measures: on-site inspections, off-site supervision, regular and targeted security audits, security scans, requests for information/evidence
- Enforcement powers for authorities including binding instructions, orders to implement recommendations from a security audit, orders to bring measures into compliance, and administrative fines
- **Maximum administrative fines** for Essential Entities of at least **€10 million or 2% of total worldwide annual turnover, whichever is higher**
- Possible temporary suspension of authorizations or, for management, temporary bans from exercising managerial functions, in cases of persistent non-compliance

### f. Germany-specific transposition
Germany is transposing NIS2 primarily through the **NIS2UmsuCG** (NIS-2-Umsetzungs- und Cybersicherheitsstärkungsgesetz), which amends the BSI Act (BSIG). Note that Germany's transposition has been delayed relative to the EU's original October 2024 deadline, but national transposition does not change your underlying obligations once the German law enters into force — and the direction of national implementation (BSI as the competent authority, similar Essential/Important classification, similar reporting timelines) is expected to closely track the Directive. You should also expect interplay with existing German critical infrastructure (KRITIS) regulation and energy-sector-specific rules (e.g., IT-Sicherheitskatalog obligations under the EnWG, overseen by the Bundesnetzagentur), which may impose additional or overlapping requirements alongside NIS2.

## Practical next steps

1. **Confirm classification** with the BSI/relevant German authority once national transposition is finalized, since exact thresholds and registration mechanics are set at the national level.
2. **Register** as an Essential Entity with the BSI.
3. **Gap-assess** your current cybersecurity program (especially OT/SCADA security, supply chain, and incident response) against Article 21's baseline measures.
4. **Stand up a 24-hour/72-hour/1-month incident reporting process** tied into BSI notification channels.
5. **Brief and train your management board** — given personal liability exposure, this is not optional.
6. **Review vendor and supply chain contracts** for security requirements consistent with NIS2 expectations.
7. **Track interaction with parallel German/EU regimes** (KRITIS, EnWG IT-Sicherheitskatalog, GDPR where personal data is involved) to avoid duplicated or conflicting compliance work.

This assessment is based on the text and structure of the NIS2 Directive and general knowledge of Germany's transposition approach; because German national implementing legislation and BSI guidance govern the precise procedural details (exact registration process, specific national thresholds, and enforcement practice), you should confirm current status with qualified German legal/regulatory counsel or directly with the BSI.
