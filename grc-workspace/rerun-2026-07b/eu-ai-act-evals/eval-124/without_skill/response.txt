# AI as a Safety Component of a Medical Device (MDR) — EU AI Act Interaction

## Classification: High-risk under Article 6(1) (Annex I route), not Annex III

Because your AI system is a **safety component of a product covered by EU harmonisation legislation listed in Annex I** (the Medical Device Regulation, (EU) 2017/745, is listed in Annex I, Section A) **and** the product (or the AI safety component itself) is **required to undergo a third-party conformity assessment by a notified body** under that legislation, your AI system is classified as **high-risk under Article 6(1)** of the EU AI Act — this is the "Annex I product-safety route," distinct from the Annex III standalone use-case list.

This is an important distinction from a system like a CV-screening tool (Annex III route): Annex I high-risk systems are products/safety components already regulated by sectoral EU product safety law, and the AI Act obligations are designed to be **integrated into the existing conformity assessment process** rather than run as a separate, parallel process.

## How the AI Act interacts with MDR

1. **Single conformity assessment procedure**: Under Article 8 and related provisions, where a product is subject both to the AI Act (as high-risk under Annex I) and to sectoral legislation like the MDR requiring notified body assessment, the AI Act's high-risk requirements (Chapter III, Section 2 — risk management, data governance, technical documentation, record-keeping, transparency, human oversight, accuracy/robustness/cybersecurity) must be **built into the notified body's conformity assessment under the MDR**, rather than duplicated as a separate AI Act certificate. This is intended to avoid double certification burden.
2. **Same notified body, expanded scope**: The notified body assessing your device under MDR must also be designated/qualified (or coordinate with an AI-Act-designated body) to assess conformity with the AI Act's high-risk requirements as part of the single assessment. In practice, this means notified bodies need AI-specific competence, and the Commission/Member States have been working on ensuring MDR notified bodies can handle the added AI Act scope.
3. **Harmonised standards and technical documentation**: Your technical documentation should address both MDR requirements (safety, performance, clinical evaluation) and AI Act Annex IV requirements (risk management per Article 9, data governance per Article 10, human oversight per Article 14, etc.) in an integrated dossier where possible.
4. **CE marking**: A single CE marking process applies, but it now must reflect conformity with both frameworks. The declaration of conformity should cover both MDR and AI Act requirements.
5. **Quality management system (QMS)**: Your existing MDR QMS (e.g., ISO 13485-based) needs to be extended to incorporate the AI Act's QMS elements (Article 17) — e.g., risk management for AI-specific risks, data governance, post-market monitoring for AI performance drift, and human oversight design — rather than running two separate QMS regimes.
6. **Post-market surveillance**: MDR post-market surveillance/vigilance obligations and the AI Act's post-market monitoring (Article 72) and serious incident reporting (Article 73) obligations both apply and should be coordinated — note the AI Act generally allows reliance on equivalent sectoral reporting mechanisms where they meet AI Act requirements, to avoid duplicate reporting to different authorities.

## Compliance deadline

Because this is an **Annex I, Article 6(1) high-risk system** (product-safety route, requiring third-party/notified body conformity assessment under sectoral law like MDR), the applicable AI Act compliance deadline is **2 August 2027** — this is the later of the Act's staggered deadlines, specifically set aside for Annex I product-safety high-risk AI systems (as opposed to the 2 August 2026 deadline for most standalone Annex III high-risk systems).

As of today (3 July 2026), you have roughly 13 months until this deadline, in addition to your ongoing MDR obligations, which already apply.

**Important nuance**: even though the AI Act's substantive high-risk deadline for this category is 2 August 2027, if you place a new device on the market before then, you should already be considering AI Act requirements proactively, since:
- Notified bodies are increasingly expecting AI-readiness in dossiers submitted now, given lead times for certification.
- Some general AI Act obligations (like the prohibitions under Article 5, and AI literacy obligations under Article 4) already apply regardless of high-risk classification and have applied since 2 February 2025.

## Main obligations to prepare for (summary)

- Risk management system spanning both regulatory frameworks
- Data governance for training/validation/test data (representativeness, bias, especially important in a clinical population context)
- Integrated technical documentation (MDR technical file + AI Act Annex IV content)
- Automatic logging/record-keeping capability
- Instructions for use covering both frameworks
- Human oversight measures appropriate to clinical use
- Accuracy, robustness, and cybersecurity testing and evidence
- QMS extension (Article 17) integrated with your ISO 13485 system
- Coordination with your MDR notified body on the combined/single conformity assessment
- CE marking reflecting both regimes
- Registration in the EU database, to the extent applicable to Annex I systems (registration requirements are more limited for Annex I systems than for Annex III systems, but confirm current scope)

## Recommendation

Engage your notified body early to confirm they are AI-Act-qualified (or how they plan to coordinate with a qualified body) for the combined assessment, and start integrating AI Act Annex IV documentation requirements into your existing MDR technical file now, well ahead of the 2 August 2027 deadline, since certification lead times for MDR are already long and adding AI Act scope will extend them further.

*Disclaimer: This is general informational guidance, not legal or regulatory advice. Given the complexity of combined MDR/AI Act conformity assessment, consult qualified EU regulatory counsel and your notified body directly.*
