# NIS2 and DORA: How They Interact for a Large European Bank

Short answer: **DORA takes precedence over NIS2 for your bank, by design — not by accident.** You do not need two parallel, competing compliance programmes. You need one integrated digital-resilience/cybersecurity programme built primarily on DORA, with NIS2 sitting alongside it as a backstop for anything DORA doesn't cover, plus a small number of NIS2-only obligations you still have to satisfy directly.

## 1. Why both apply to you

Banking is an **Annex I ("essential entity") sector under NIS2** — financial market infrastructure and banking are explicitly listed as critical sectors. On size alone, a "large" bank is automatically in scope (well above the ≥50 employees / ≥€10M turnover threshold in Art. 3).

At the same time, **DORA (Regulation (EU) 2022/2554)** applies directly to banks as a category of "financial entity," covering ICT risk management, incident reporting, digital operational resilience testing, and third-party ICT risk.

So both instruments name you as in-scope. The overlap is intentional — EU lawmakers built a coordination mechanism directly into the legislation rather than leaving firms to reconcile two competing regimes themselves.

## 2. The precedence rule: NIS2's *lex specialis* carve-out

NIS2 contains an explicit **sector-specific *lex specialis* clause** (Art. 4 of the NIS2 Directive, read together with Recital 28 and Art. 1(2) of DORA): where a sector-specific EU legal act requires entities to adopt cybersecurity risk-management measures or to report incidents, and those requirements are **at least equivalent in effect** to the corresponding NIS2 obligations, the sector-specific act applies instead of the NIS2 provisions it displaces. DORA is named as exactly such an act for the financial sector.

Practically, this means:

- **Art. 21 risk management measures** — DORA's ICT risk management framework (governance, protection/detection, response/recovery, learning, communication) is deemed equivalent and **displaces** NIS2 Art. 21 for you. You comply through DORA, not NIS2, on this point.
- **Art. 23 incident reporting** — DORA's major ICT-related incident reporting regime (its own timelines and templates to your competent authority, not the NIS2 24h/72h/1-month CSIRT track) **displaces** NIS2 Art. 23. You report ICT incidents the DORA way.
- **Governance obligations (NIS2 Art. 20)** and **supply chain security (NIS2 Art. 21(2)(d) / Art. 22)** are likewise substantially covered by DORA's management-body accountability provisions and its detailed ICT third-party risk regime (register of information, concentration risk, critical ICT third-party provider oversight) — which go further than NIS2 in this area.

Where DORA is silent or doesn't reach as far as NIS2 (this is narrower than it sounds, since DORA is comprehensive for financial entities), NIS2 obligations continue to apply. In practice, for a bank, the "gap" NIS2 fills is usually thin — but you should not assume it's zero without a clause-by-clause check, since transposition details vary by Member State and your national competent authority may take its own view on residual scope.

## 3. What this means operationally: one programme, not two

**You need one integrated compliance programme, anchored in DORA, with a NIS2 gap-check layered on top** — not two parallel programmes. Recommended structure:

| Workstream | Primary framework | NIS2 relevance |
|---|---|---|
| ICT risk management framework | DORA (RTS/ITS under Arts. 5–16) | Displaced — DORA governs |
| Incident classification & reporting | DORA (major ICT incident reporting) | Displaced — DORA governs, not NIS2's 24h/72h/1-month track |
| Digital operational resilience testing (incl. TLPT) | DORA (Arts. 24–27) | No NIS2 equivalent requirement |
| ICT third-party / concentration risk | DORA (Arts. 28–30, Oversight Framework) | Displaced — DORA is more detailed |
| Management body accountability | DORA (Art. 5) | Displaced — DORA governs |
| National critical-infrastructure registration, CSIRT liaison, Member State-specific NIS2 transposition duties | NIS2 (as transposed nationally) | **Still applies** — this is not an ICT risk-management or incident-reporting obligation per se, so it isn't displaced |
| Sector interdependency / cross-sector supply chain coordination (Art. 22 coordinated risk assessments run by the Cooperation Group/ENISA) | NIS2 | **Still applies** — DORA doesn't replicate this cross-sector coordination mechanism |
| Penalty exposure | DORA supervisory regime (competent authority-specific) | NIS2 Art. 34 penalties (up to €10M / 2% global turnover) apply only to the residual NIS2 obligations that survive the carve-out |

**Practical recommendation:**
1. **Build your core programme against DORA** — it is more detailed, more prescriptive (via RTS/ITS), and already deemed to satisfy NIS2's equivalent provisions.
2. **Run a one-time (then periodic) mapping exercise**: for each NIS2 Art. 21 measure and Art. 20/22/23 obligation, document which DORA provision displaces it, citing the *lex specialis* clause. This mapping is your audit evidence that you're not non-compliant with NIS2 merely because you're following DORA instead.
3. **Identify and separately track the residual NIS2-only items** — national registration/notification duties to your NIS2 competent authority or CSIRT, any Member State gold-plating in transposition, and participation in Art. 22 coordinated supply-chain risk assessments where invited.
4. **Confirm your national competent authority's view.** Because NIS2 is transposed at Member State level, some national regulators have issued (or may issue) guidance on exactly where they consider DORA equivalence to end. Since your regulator has proactively told you NIS2 applies alongside DORA, ask them directly which specific NIS2 obligations they consider *not* displaced — this closes the single biggest ambiguity in the *lex specialis* test and should be documented as regulator correspondence in your compliance file.
5. **Keep governance unified.** Report both DORA and residual-NIS2 status to the same board-level risk committee under a single risk register line, rather than standing up a separate NIS2 governance track — this avoids duplicated (and potentially conflicting) control ownership.

## 4. Bottom line

- **DORA takes precedence** for ICT risk management, incident reporting, resilience testing, and third-party ICT risk, via NIS2's own *lex specialis* mechanism.
- **NIS2 still applies** to you as a matter of law (you're in scope as an essential entity), but most of its substantive content is satisfied by demonstrating DORA compliance.
- **You do not need two separate compliance programmes.** You need one DORA-anchored programme, a documented equivalence mapping to NIS2 Art. 20/21/22/23, and a thin, explicitly tracked layer of residual NIS2-only obligations (national registration, CSIRT liaison, Art. 22 coordinated assessments) confirmed against your regulator's stated expectations.

**Recommended next step:** commission a formal Art. 21-to-DORA equivalence mapping (I can help draft this) and put the residual-obligations question to your regulator in writing so you have a documented basis for your scoping decisions — this is the artifact examiners and auditors will ask for first.
