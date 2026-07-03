# Open-Source LLM (~8×10²³ FLOPs) — GPAI Obligations

## 1. GPAI Classification Check
Your model is trained "at scale" using self-supervision and displays significant generality across a wide range of tasks (an LLM) — it meets the **Art. 3(63) GPAI model** definition.

**Compute threshold check:** The Commission's GPAI scope guidelines (July 2025) set the applicability threshold at **≥10²³ FLOPs** cumulative training compute. Your model was trained with **~8×10²³ FLOPs** — this is above that threshold (8×10²³ > 1×10²³), so **GPAI obligations under Arts. 53–55 apply to you.**

**Systemic risk check:** The presumption of systemic risk under Art. 51 triggers at **≥10²⁵ FLOPs**. At 8×10²³ FLOPs, you are roughly two orders of magnitude below that threshold, so your model is **not presumed to have systemic risk** (absent a separate Commission designation based on Annex XIII criteria such as reach, capabilities, or downstream impact — which is possible but not the default outcome here).

**Conclusion: GPAI provider, non-systemic-risk tier.**

## 2. Open-Source Exception — Applies, But Is Narrower Than It Might Seem

Because you release the weights, architecture, and usage documentation publicly under a free licence, you qualify for the **open-source/free-license exception**. Under this exception, you are relieved of two of the four universal Art. 53 obligations and only need to comply with the other two:

| Art. 53 Obligation | Open-source exception status |
|---|---|
| 1. Technical documentation (Annex XI) — for the AI Office/authorities | **Exempted** |
| 2. Downstream provider information (Annex XII) | **Exempted** |
| 3. **Copyright compliance policy** (Directive 2019/790) | **Still required** |
| 4. **Public training content summary** | **Still required** |

So your live obligation list as an open-source, non-systemic-risk GPAI provider is:

- **Copyright policy (Art. 53(1)(c)):** Implement and publicly describe a policy for complying with EU copyright/related-rights law — specifically, technically enforceable mechanisms that respect text-and-data-mining (TDM) opt-outs reserved by rightsholders under Art. 4(3) of Directive 2019/790 (e.g., honouring robots.txt and other machine-readable opt-out signals used during data collection/training).
- **Public training content summary (Art. 53(1)(d)):** Publish a sufficiently detailed summary of the content used to train the model, following the Commission's published template, so downstream providers and the public can understand what data went into it.

**Important caveat:** If your model is later designated as having systemic risk (whether by crossing 10²⁵ FLOPs in a future training run, or by Commission designation on other Annex XIII grounds), the open-source exception **falls away entirely** and full Art. 53 + Art. 55 obligations apply — including the technical documentation and downstream information duties you're currently exempt from.

## 3. Does the GPAI Code of Practice Help?

**Yes — the CoP is the primary compliance pathway, and it maps directly onto your open-source obligations.** Key points:

- Published 10 July 2025; endorsed by the Commission and AI Board 1 August 2025; operative since 2 August 2025.
- Structured in three chapters: (i) Transparency, (ii) Copyright, (iii) Safety and Security (systemic-risk models only — **not applicable to you** at your current compute level).
- For your obligations specifically, the **Copyright chapter** is directly relevant: it operationalises a written copyright policy, compliance with robots.txt and technical opt-out protocols, a rightsholder complaints mechanism, and a prohibition on infringing uses in your acceptable use policy.
- The **Transparency chapter** provides the Model Documentation Form template — useful for structuring your public training content summary even though you're exempt from the full Annex XI/XII documentation, since the training summary still needs to be "sufficiently detailed" per the Commission template.
- Signing the CoP gives you a **presumption of conformity** pathway with reduced ambiguity about what "sufficiently detailed" or "technically enforceable" means in practice — major signatories include Anthropic, Google, Microsoft, OpenAI, Amazon, IBM, and Mistral, so tooling and shared practice around CoP compliance is relatively mature.
- If you don't sign, you must **demonstrate compliance by alternative means** and explain your approach to the AI Office — this is more work, not less, so signing is generally the lower-friction path for a provider your size.

## 4. Enforcement and Timing Context (today: 3 July 2026)
- Your GPAI obligations have been **in force since 2 August 2025** — this is not a future deadline for you, it is a current, live obligation.
- **AI Office enforcement powers over GPAI providers activate 2 August 2026** — roughly one month from today. From that date, the AI Office gains full powers (information requests, model evaluations, fines) to check GPAI providers' compliance, including yours. You should have your copyright policy and training summary in place and demonstrably compliant well before that date, not scrambling afterward.
- The legacy-model grace period (deadline 2 August 2027) only applies to models placed on the market **before** 2 August 2025 — if your model was released after that date, this grace period does not apply to you and your obligations are already active.

## Bottom Line

| Item | Status |
|---|---|
| GPAI obligations apply? | Yes — 8×10²³ FLOPs exceeds the 10²³ threshold |
| Systemic risk presumption? | No — well below the 10²⁵ FLOPs threshold |
| Full Art. 53 documentation (Annex XI/XII)? | Exempt — open-source/free-license |
| Copyright policy required? | Yes |
| Public training summary required? | Yes |
| Art. 55 systemic-risk obligations? | Not applicable at current scale |
| CoP helps? | Yes — primary compliance pathway, Copyright + Transparency chapters map to your exact remaining obligations |
| Enforcement exposure | AI Office enforcement activates 2 Aug 2026 — get compliant now |

*This is general compliance guidance, not legal advice. Verify your FLOPs calculation methodology and licence terms against the Commission's official GPAI scope guidelines, and consult qualified counsel for a formal compliance opinion.*
