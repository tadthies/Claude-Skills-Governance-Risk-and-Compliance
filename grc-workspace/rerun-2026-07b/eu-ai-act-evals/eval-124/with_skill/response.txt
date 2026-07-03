# AI Safety Component of an MDR Medical Device — AI Act / MDR Interaction

## 1. Classification: High-Risk via Path A (Art. 6(1)) — Annex I, Not Annex III

Your AI software is a **safety component of a product** (the medical device) that is covered by **Annex I harmonisation legislation** — specifically item 11 in Annex I, Section A: **Medical Devices Regulation, Regulation (EU) 2017/745 (MDR)**. Because your device requires **notified-body conformity assessment** under the MDR, both limbs of the Art. 6(1) test are met:

1. It is a safety component of a product covered by Annex I harmonisation legislation (MDR); **AND**
2. That product requires third-party (notified body) conformity assessment under the MDR.

**Conclusion: this is a high-risk AI system under Art. 6(1), Path A — the Annex I "embedded product safety component" route — not the Annex III standalone-system route.** This distinction matters because it changes both your compliance deadline and your conformity assessment mechanism.

## 2. How the AI Act Interacts with MDR — Integrated, Not Parallel, Compliance

The key design principle here is **integration, not duplication**:

- **Conformity assessment is integrated into the existing MDR procedure.** Rather than running a separate AI Act conformity assessment process, the AI Act requirements (Arts. 9–15) are assessed **as part of** your existing MDR notified-body conformity assessment. Your MDR notified body needs to be designated/qualified to also assess AI Act requirements (or coordinate with an AI-Act-scoped assessment), but you do not go through two entirely separate certification tracks.
- **Quality management system (Art. 17):** Your existing MDR QMS (e.g., ISO 13485-based) can be **adapted and integrated** to cover the AI Act's 13 QMS components rather than building a parallel system from scratch — regulatory compliance strategy, design/development controls, data management, risk management, post-market monitoring, and incident reporting can largely map onto processes you already have for MDR.
- **Risk management (Art. 9):** Your MDR risk management file (ISO 14971) should be extended to explicitly cover the AI Act's 5-step process (identify, estimate/evaluate, evaluate from post-market data, mitigate per the hierarchy in Art. 9(4), assess residual risk) — again, integration rather than a second, disconnected risk file.
- **Post-market monitoring (Art. 72):** Existing post-market monitoring systems under sectoral legislation like the MDR **may be adapted and integrated** to avoid duplication — you do not need a separate AI Act post-market surveillance system running alongside your MDR vigilance system.
- **Technical documentation (Art. 11, Annex IV):** This is additive — your MDR technical file will need AI-Act-specific content added (training data description, algorithm/design choices, validation metrics, human oversight design) that MDR technical documentation does not already capture.
- **CE marking (Art. 48):** A single CE mark is affixed once both MDR and AI Act conformity requirements are satisfied through the integrated assessment — you are not affixing two separate marks.

**Practical implication:** Talk to your MDR notified body now about their AI Act assessment capability/designation, and start mapping your existing MDR risk file, QMS, and post-market surveillance system against the AI Act's Arts. 9, 10, 12, 14, 15, and 17 requirements to identify gaps rather than building fresh AI Act infrastructure in parallel.

## 3. Compliance Deadline

Because this is an **Annex I embedded-product safety component** (not an Annex III standalone system), the applicable deadline is the Annex I timeline, which the Digital Omnibus (adopted 29 June 2026) confirmed as:

> **2 August 2028**

This is later than the Annex III standalone-system deadline of 2 December 2027 — embedded product safety components got the longer runway, reflecting the additional complexity of coordinating with sectoral regimes like the MDR. As of today (3 July 2026), you have just over two years to complete integration of the AI Act requirements into your MDR conformity assessment and QMS.

**Note:** GPAI-specific obligations (Arts. 53–55) are unrelated to this Annex I/product classification and would only apply separately if your AI software were itself built on a general-purpose AI model meeting the Art. 3(63) definition — unlikely for a narrow medical-device safety component, but worth a quick check if any underlying foundation model is involved.

## 4. Your Core Obligations as Provider (Arts. 9–17, integrated with MDR)

| Requirement | Article | MDR Integration Point |
|---|---|---|
| Risk management system | Art. 9 | Extend ISO 14971 risk file with AI-specific risk identification (bias, robustness, foreseeable misuse) |
| Data governance | Art. 10 | Document training/validation/test data provenance, representativeness, bias examination |
| Technical documentation | Art. 11 | Add AI-Act-specific content to MDR technical file (Annex IV items) |
| Record-keeping/logging | Art. 12 | Build automatic event logging into the device software |
| Transparency to deployers | Art. 13 | Extend IFU/labelling with AI system characteristics, accuracy metrics, human oversight measures |
| Human oversight | Art. 14 | Design for clinician override/disregard capability; guard against automation bias |
| Accuracy, robustness, cybersecurity | Art. 15 | Declared accuracy in IFU; resilience to adversarial inputs, data/model poisoning |
| QMS | Art. 17 | Integrate into existing ISO 13485 MDR QMS |
| Conformity assessment | Art. 43 | Integrated into existing MDR notified-body procedure (no separate AI Act assessment track) |
| EU Declaration of Conformity / CE marking | Arts. 47–48 | Single, combined declaration/marking once both regimes' requirements are satisfied |

## Bottom Line
- **Classification:** High-risk under Art. 6(1) (Path A) as an Annex I safety component of an MDR-regulated medical device — not Annex III.
- **Interaction with MDR:** Integrated compliance — one conformity assessment procedure, one QMS, one post-market monitoring system, extended to cover both regimes rather than run in parallel.
- **Deadline:** **2 August 2028** (Digital Omnibus-confirmed Annex I timeline).
- **Immediate action:** Engage your MDR notified body on AI Act assessment scope, and gap-map your existing MDR risk/QMS/PMS documentation against Arts. 9–17.

*This is general compliance guidance, not legal advice. Given the combined medical-device and AI Act regulatory stakes, confirm your specific classification and integration approach with your notified body and qualified regulatory counsel.*
