# NIS2 and DORA for a European Bank: How They Interact

## Short answer
DORA takes precedence for you. DORA (Regulation (EU) 2022/2554) operates as **lex specialis relative to NIS2** under NIS2's own Art. 4: for financial entities, DORA's ICT risk-management and incident-reporting rules apply **instead of** NIS2 Arts. 21 and 23. You do not need two parallel substantive compliance programmes — you need one programme built to DORA, with a thinner NIS2 layer for the parts DORA doesn't cover.

## The legal mechanism: lex specialis under NIS2 Art. 4

NIS2 was drafted anticipating exactly this overlap. Where a sector-specific EU legal act (DORA, for financial entities) imposes requirements "at least equivalent in effect" to NIS2's, that sector-specific act displaces the corresponding NIS2 provisions. For banks, this means:

- **DORA replaces NIS2 Art. 21** (risk management measures) — your ICT risk management framework, third-party risk management, and digital operational resilience testing are built to DORA's Chapters II–IV, not to the general Art. 21(2)(a)–(j) measure list.
- **DORA replaces NIS2 Art. 23** (incident reporting) — major ICT-related incidents are reported under DORA's incident classification and reporting framework, not the NIS2 24h/72h/1-month CSIRT workflow.

## What NIS2 still does apply to you

Lex specialis displaces the *substantive* risk-management and incident-reporting articles — it does not remove you from the NIS2 regime entirely. As a bank, you are in Annex I (banking, financial market infrastructure) and, being a large institution, you remain:

- **Registered/listed as a NIS2 entity** under your Member State's transposition — banks stay on the NIS2 register even though the substantive obligations run through DORA.
- Subject to the **general NIS2 framework provisions** that DORA doesn't specifically override (jurisdictional/scope provisions, cooperation mechanisms) to the extent national transposition preserves them.
- Still relevant for classification purposes: as an Annex I financial market entity of significant scale, you would independently qualify as Essential or Important Entity under NIS2's Art. 3 tests — this classification remains on record even though it doesn't drive your day-to-day compliance obligations.

## Where reports actually go

This is the operational point your regulator is most likely testing: **incident reports go to your financial supervisor (e.g., national competent authority under DORA, potentially the ECB/EBA framework depending on your classification), not to the national CSIRT.** Do not build a parallel CSIRT notification track for the same ICT incidents — DORA's reporting channel is the one that matters for you. Confirm the specific competent authority designated under your Member State's DORA implementation, since this may differ from your NIS2 CSIRT contact.

## Do you need two compliance programmes?

**No — build one programme to DORA, with a light NIS2 registration/coordination layer**, not two duplicate substantive programmes. Concretely:

| Function | Which regime governs |
|---|---|
| ICT risk management framework | **DORA** (Chapters II) |
| ICT third-party risk management (incl. critical ICT provider oversight) | **DORA** (Chapter V) |
| Digital operational resilience testing (incl. threat-led penetration testing) | **DORA** (Chapter IV) |
| Major ICT-incident classification and reporting | **DORA** (Chapter III) |
| Entity registration/listing | **NIS2** (national register, Art. 27-equivalent, via transposition) |
| Governance-level board accountability | Both regimes have governance requirements (NIS2 Art. 20; DORA Art. 5) — align them into one governance framework rather than running two, since both require management-body approval and oversight of the ICT/cyber risk programme |
| GDPR breach notification (if personal data affected) | Runs in parallel regardless — independent 72-hour DPA clock under GDPR Art. 33 |

**Practical recommendation:**
1. Build your core ICT risk management, third-party oversight, resilience testing, and incident reporting programme entirely to **DORA's** requirements — this is your substantive compliance backbone.
2. Confirm and maintain your NIS2 registration status with the national competent authority so you remain correctly listed, but do not duplicate the Art. 21/Art. 23 substantive controls — DORA compliance satisfies the equivalent NIS2 obligations by design.
3. Unify governance evidence (board approval, training, oversight cadence) into a single board reporting line rather than maintaining separate NIS2 and DORA governance tracks — both regimes want to see the same kind of management-body accountability.
4. Confirm the exact DORA competent authority and reporting channel for your Member State and institution type (this can vary — banking supervisors, ECB for significant institutions, or a designated national DORA authority) so your incident response runbook points to the right recipient, not the CSIRT.
5. Keep GDPR Art. 33 as a fully separate, parallel track if personal data (customer PII) is implicated in an incident — DORA and NIS2 coordination doesn't touch this obligation.

## Bottom line
DORA takes precedence for the substance of your programme (risk management and incident reporting); NIS2 keeps you registered and in scope at a framework level but does not require you to run its Art. 21/23 obligations in parallel. One unified ICT risk and resilience programme built to DORA — not two — is both the compliant and the practical answer.

*This is general compliance information, not legal advice. Confirm your institution's specific DORA competent authority and any residual national NIS2 transposition requirements with qualified counsel.*
