# NIS2 and DORA: How They Interact for a Large European Bank

## Short Answer

Your regulator is correct: **both NIS2 and DORA apply to you conceptually, but DORA takes precedence as the "lex specialis" (specific law) for your ICT and operational resilience requirements.** You do not need two fully separate, duplicative compliance programmes — DORA is designed specifically to displace NIS2's substantive requirements for financial entities, while NIS2 continues to operate "around" you at the ecosystem level (national supervisory cooperation, cross-sector coordination, and for certain financial market infrastructure not otherwise captured by DORA).

## The Legal Basis for Precedence: DORA as Lex Specialis

The NIS2 Directive **itself** provides for this outcome. Article 4 of NIS2, headed "Sector-specific Union legal acts," states that where sector-specific Union legal acts require essential or important entities to adopt cybersecurity risk-management measures or to notify significant incidents, and where those requirements are **at least equivalent in effect** to the corresponding NIS2 obligations, the relevant provisions of the sector-specific act (including its supervision and enforcement provisions) apply instead of NIS2's equivalent provisions.

DORA (Regulation (EU) 2022/2554, the Digital Operational Resilience Act) was explicitly designed and negotiated as this "lex specialis" for the financial sector. **Recital 28 of DORA** and corresponding NIS2 recitals confirm this legislative intent directly: DORA's ICT risk management, incident reporting, digital operational resilience testing, and third-party risk provisions are deemed to satisfy the equivalent NIS2 obligations for financial entities within DORA's scope.

**Practical result:** For a bank (a "credit institution," explicitly listed as a DORA "financial entity" under Article 2 of DORA), your substantive cybersecurity risk management and incident reporting obligations are governed by **DORA, not NIS2**, even though the banking/financial sector also appears in NIS2 Annex I as "Banking."

## Where the Two Regimes Actually Interact

### 1. Risk Management: DORA Governs
DORA Chapter II (Articles 5-16) sets out ICT risk management requirements that are more granular and finance-specific than NIS2 Article 21 — covering ICT governance, risk management framework, ICT systems/protocols/tools, identification of ICT-supported business functions, protection and prevention, detection, response and recovery, backup/restoration procedures, learning and evolving, and communication. You comply with DORA's framework; you do not need to separately satisfy NIS2 Article 21's parallel (but less detailed) list, because Article 4 NIS2 disapplies the NIS2 version in favor of the equivalent, more specific DORA regime.

### 2. Incident Reporting: DORA's Timeline and Channel Apply
DORA has its own major ICT-related incident classification and reporting regime (Articles 17-23) — reportable to your **financial sector competent authority** (in the EU/Eurozone context, typically your national competent authority coordinating with the ECB/EBA/ESMA/EIOPA via the Joint Examination Teams and the future centralized EU reporting hub), not to the NIS2 national CSIRT. DORA's incident classification criteria and reporting deadlines (initial notification, intermediate report, final report — a similar but distinct three-stage structure to NIS2's 24h/72h/1-month) supersede NIS2's Article 23 reporting obligations for you as a bank.

### 3. Third-Party/ICT Supplier Risk: DORA Governs, With Its Own Oversight Regime
DORA Chapter V introduces a dedicated regime for **critical ICT third-party providers (CTPPs)**, including a direct EU-level oversight framework (Lead Overseer designation by the ESAs) for systemically important ICT providers (major cloud providers, etc.). This goes beyond NIS2's supply-chain security provisions and is the applicable regime for your vendor risk management, contractual requirements (DORA-mandated contractual clauses for ICT third-party arrangements), and register of information obligations.

### 4. Digital Operational Resilience Testing: DORA-Only
DORA introduces mandatory resilience testing, including **Threat-Led Penetration Testing (TLPT)** for significant entities (large banks like yours are very likely in scope for TLPT under the DORA RTS). NIS2 has no direct equivalent requirement — this is purely a DORA obligation.

### 5. Supervision: Your Financial Regulator, Not the NIS2 Competent Authority
Because Article 4 NIS2 disapplies NIS2's substantive provisions in favor of DORA, your day-to-day supervision for cyber/operational resilience matters runs through your **prudential/financial supervisor** (national central bank/financial authority, and for significant institutions the ECB under the Single Supervisory Mechanism) — not the national NIS2 competent authority/CSIRT. This avoids the dual-regulator burden you might otherwise fear.

### 6. Where NIS2 Still Matters to You
NIS2 does not disappear entirely:
- **Ecosystem/cross-sector coordination**: NIS2 establishes the Cooperation Group, CSIRTs network, and cross-border coordination mechanisms. Systemic incidents affecting multiple sectors (e.g., a major cloud outage affecting banks, energy, and healthcare simultaneously) will still involve NIS2-designated CSIRTs at a national/EU coordination level, even if your direct reporting line is via DORA.
- **National transposition edge cases**: Some Member States' NIS2 transposition laws retain limited residual obligations or registration touchpoints for financial entities pending full DORA implementation clarity — worth confirming with local counsel, as transposition quality varies by Member State.
- **Group/subsidiary structures**: If your banking group includes non-financial-entity subsidiaries or services not squarely within DORA's "financial entity" definitions (e.g., a technology subsidiary providing services outside the regulated financial activities), those entities could fall under NIS2 directly rather than benefiting from the DORA carve-out — worth mapping your corporate structure against both regulations' scope definitions.
- **Non-DORA financial infrastructure**: Certain entities in the broader financial ecosystem not captured by DORA's "financial entity" list might remain under NIS2's Banking or Financial Market Infrastructure sub-sectors — not directly relevant to a bank itself, but relevant if you're assessing counterparties.

## Do You Need Two Separate Compliance Programmes?

**No — and you should actively avoid building two parallel programmes.** The correct architecture is:

1. **One integrated ICT/cyber risk and operational resilience programme, built to DORA's requirements as the primary framework** (since DORA is both more specific and legally takes precedence for your substantive obligations).
2. **A NIS2-awareness layer on top**, ensuring:
   - Your legal/compliance team understands NIS2 Article 4's lex specialis mechanism and can articulate to any regulator (or auditor) why DORA compliance satisfies the equivalent NIS2 obligations
   - You monitor whether any non-DORA-covered entities in your group need direct NIS2 compliance
   - You stay engaged with any residual national NIS2 registration/notification touchpoints your Member State transposition may still require, even if substantively superseded
   - You track ENISA/Cooperation Group guidance for systemic cross-sector incidents, since coordination mechanisms may still route through NIS2 structures during major cross-sector events

## Practical Recommendations for Your CISO Function

1. **Confirm entity-by-entity DORA scope** across your banking group — DORA's "financial entity" definition is broad but not universal; map every legal entity against both DORA Article 2 and NIS2 Annex I/II to identify any gaps where NIS2 might apply directly.
2. **Build your programme DORA-first**: risk management framework (Ch. II), incident classification/reporting (Ch. III), resilience testing including TLPT (Ch. IV), and third-party risk management with contractual register (Ch. V) as your primary compliance architecture.
3. **Document the Article 4 NIS2 equivalence rationale** formally — auditors, regulators, and your board will want to see a clear, documented basis for why you're not running a separate NIS2 programme, rather than simply assuming it.
4. **Engage directly with your prudential supervisor** (national authority / ECB-SSM if significant institution) to confirm their expectations on the DORA-NIS2 interface — supervisory practice is still maturing, and getting explicit confirmation from your actual supervisor is more valuable than relying solely on the legislative text.
5. **Maintain a lightweight NIS2 monitoring function** — not a parallel programme — to track group-structure changes, non-financial-entity subsidiaries, and any national transposition nuances that could reintroduce direct NIS2 obligations.
6. **Align incident reporting workflows carefully**: even though DORA is your primary reporting regime, ensure your incident response playbooks correctly route notifications to the right authority (financial supervisor under DORA) and don't default staff to NIS2-era CSIRT contacts from pre-DORA planning.

## Bottom Line

DORA takes precedence over NIS2 for your bank by explicit design (NIS2 Article 4's lex specialis provision, reinforced by DORA's own recitals). Build one unified ICT risk and operational resilience programme around DORA's more detailed and finance-specific requirements, supervised by your financial regulator — not two parallel compliance tracks. Retain a thin layer of NIS2 awareness for group-structure edge cases, cross-sector coordination scenarios, and any residual national transposition nuances, but do not duplicate your core risk-management and incident-reporting build-out under both frameworks.
