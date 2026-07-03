How NIS2 and DORA Interact for a Large European Bank
=====================================================

Short answer: DORA takes precedence for your ICT/cyber risk management as a financial entity, because it is a *lex specialis* (sector-specific law) relative to NIS2's *lex generalis* (general/horizontal law). You will not need two full, parallel compliance programmes — but you will still have some NIS2-adjacent obligations that DORA does not fully absorb, so a single, DORA-led programme with a thin NIS2 "wrapper" is the right model.

1. The Legal Relationship: Lex Specialis vs Lex Generalis
-----------------------------------------------------------

- **NIS2 (Directive (EU) 2022/2555)** is the EU's general cybersecurity directive, covering "essential" and "important" entities across many sectors (energy, transport, health, digital infrastructure, banking, financial market infrastructure, etc.). It is a *directive*, transposed into national law by each Member State, so exact obligations vary slightly by country.

- **DORA (Regulation (EU) 2022/2554)** is a *regulation* — directly applicable, no national transposition needed — that sets out ICT risk management, incident reporting, resilience testing, and third-party risk requirements specifically for banks, insurers, investment firms, payment institutions, CCPs, and other financial entities.

- NIS2 itself explicitly addresses this overlap. **Article 4 of NIS2** (the "lex specialis clause") states that where sector-specific EU legal acts require essential or important entities to adopt cybersecurity risk-management measures or to report incidents, and those requirements are "at least equivalent in effect" to NIS2's obligations, the sector-specific act applies instead of the corresponding NIS2 provisions. **DORA is named directly in NIS2 Recital 28 as an example of such lex specialis.**

- The European Commission and ENISA have confirmed this reading: **DORA is deemed to satisfy the NIS2 requirements on cyber risk management (Art. 21) and incident reporting (Art. 23)** for entities in DORA's scope, because DORA's requirements are considered equivalent or more stringent.

**Practical conclusion:** As a bank, your ICT risk management framework, incident classification/reporting, resilience testing (including TLPT/threat-led penetration testing), and third-party/ICT vendor risk oversight should be built and run under **DORA**, not built twice under both regimes.

2. Where NIS2 Still Applies to You
------------------------------------

Even with the lex specialis carve-out, NIS2 doesn't disappear entirely for a bank. Watch for these residual touchpoints:

- **Scope/registration and governance obligations that DORA doesn't cover.** NIS2 has some horizontal requirements — e.g., national registration in the NIS2 entity registry, cooperation with national NIS2 competent authorities/CSIRTs, and certain supply-chain or national-security-flavored obligations — that may still apply in your Member State's transposition, particularly if you sit within scope as an "essential entity" and your national law didn't fully exempt DORA-covered entities from every NIS2 article (only from the risk-management and incident-reporting substance, per Article 4).

- **National transposition variance.** Because NIS2 is a directive, each Member State's transposing law may draw the DORA carve-out boundary slightly differently. Some Member States' laws exempt DORA entities from NIS2 almost entirely; others retain registration, general oversight, or penalty provisions. You need country-specific legal confirmation for every jurisdiction you operate in as a bank (home and host Member States), not just an EU-level reading.

- **Group/non-financial subsidiaries.** If your banking group includes entities that are *not* "financial entities" under DORA (e.g., a technology subsidiary, a non-regulated fintech arm, certain outsourcing/shared-service entities that don't independently qualify as DORA financial entities), those entities may fall under NIS2 in their own right, with no DORA carve-out available to them.

- **Critical ICT third-party providers.** DORA's Oversight Framework covers "critical" ICT third-party providers (CTPPs) designated by the ESAs. Some of your vendors may separately be in scope of NIS2 as "important" or "essential" entities in the digital infrastructure/ICT service categories (cloud providers, data centre providers, managed service providers, DNS providers, etc.) — meaning your vendor due diligence needs to track both regimes for different counterparties.

- **Penalties and enforcement channel.** Even where the substantive risk-management/incident-reporting rules are disapplied, the enforcement authority for a bank under DORA is your prudential/financial supervisor (in most Member States, the national competent authority designated for DORA — often the central bank or financial regulator), not the national NIS2/cybersecurity authority. Confirm which authority has jurisdiction for what, since dual notification obligations can arise in edge cases (e.g., if an incident also affects non-financial group entities in NIS2 scope).

3. Precedence Summary
------------------------

| Topic | Governing Regime | Notes |
|---|---|---|
| ICT/cyber risk management framework | **DORA** | Lex specialis under NIS2 Art. 4 |
| Major ICT-related incident reporting | **DORA** | DORA's incident classification & reporting timelines apply, not NIS2's |
| Digital operational resilience testing (incl. TLPT) | **DORA** | No equivalent NIS2 testing regime for you |
| ICT third-party risk / register of information | **DORA** | Register of Information, contractual requirements, CTPP oversight |
| National registration / general supervisory cooperation | **Possibly NIS2** | Depends on national transposition — verify per Member State |
| Non-financial-entity group subsidiaries | **NIS2** (if independently in scope) | DORA carve-out doesn't extend automatically to non-financial entities |
| Vendors who are themselves NIS2 "essential/important" entities | **NIS2** (for that vendor) | Relevant to your third-party risk assessments, not your own compliance |

4. Do You Need Two Separate Compliance Programmes?
------------------------------------------------------

No — and building two parallel programmes would be inefficient and create conflicting obligations/duplicate reporting. Recommended approach:

1. **Anchor your core ICT/cyber risk programme in DORA.** This becomes your primary framework for governance, risk management, incident response, resilience testing, and third-party/vendor oversight (RoI, contractual clauses, concentration risk, exit strategies).

2. **Run a jurisdiction-by-jurisdiction NIS2 applicability check.** For every Member State you operate/are headquartered in, confirm with local counsel (i) whether your national NIS2 transposition law fully exempts DORA-scoped financial entities from substantive obligations, and (ii) whether any residual registration, governance, or reporting duties remain.

3. **Map non-DORA-covered group entities separately.** Any subsidiary that isn't itself a "financial entity" under DORA should be assessed independently against NIS2 scope criteria (size thresholds, sector, essential/important classification) and, if in scope, given its own lightweight NIS2 compliance track (registration, risk measures, incident reporting to the national CSIRT) — ideally still using the same underlying security controls and incident response processes as the DORA programme, just with an additional reporting/registration layer bolted on.

4. **Extend third-party due diligence to cover both regimes.** Your vendor risk assessments should flag whether a critical ICT supplier is itself a NIS2 essential/important entity (relevant to their resilience and your concentration risk) and separately whether they qualify as a DORA CTPP subject to direct ESA oversight.

5. **Single incident response plan, dual notification logic where needed.** Build one incident detection/response/escalation process, with a decision tree that determines: (a) DORA major incident reporting to your competent authority (this will be the default for the bank itself), and (b) whether any NIS2 notification to a national CSIRT is also triggered — e.g., because a non-financial subsidiary or shared infrastructure is affected.

5. Recommended Next Steps
-----------------------------

- Obtain written confirmation from each relevant national competent authority/CSIRT on how your jurisdiction's NIS2 transposition treats DORA-regulated banks (the Article 4 carve-out is EU-level, but its practical application depends on national law).
- Inventory all group entities and classify each as "DORA financial entity," "NIS2 in-scope (non-financial)," "both" (rare, but possible for certain financial market infrastructure or dual-role entities), or "neither."
- Update your Register of Information (DORA) to flag any ICT third parties that are separately NIS2-regulated, and cross-reference this with any NIS2 supply-chain risk assessments you may still owe for non-DORA subsidiaries.
- Confirm with your DORA competent authority whether they coordinate directly with your national NIS2 authority/CSIRT, so you know if a single incident report satisfies both regimes or if parallel notification is still expected in edge cases.
- Document the Article 4 lex specialis rationale in your governance/compliance framework so auditors and regulators can see the legal basis for not running a duplicate NIS2 risk-management programme.

Bottom line: DORA governs your substantive cyber/ICT risk management and incident reporting as a bank; NIS2 recedes into a lex generalis backstop that mainly matters for non-financial group entities, certain national administrative obligations, and third-party entities that are themselves NIS2-regulated. One integrated, DORA-led programme — with a NIS2 applicability check layered on top for group scoping and vendor mapping — is the right structure, not two separate programmes.
