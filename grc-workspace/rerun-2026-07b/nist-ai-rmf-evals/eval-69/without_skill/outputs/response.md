# Mapping NIST AI RMF to the EU AI Act — and the Gaps That Remain

NIST AI RMF and the EU AI Act share a common risk-based philosophy, and NIST itself (along with organizations like ISO and various crosswalk publications) has worked to align AI RMF concepts with the AI Act. However, they are fundamentally different types of instruments: **AI RMF is a voluntary, flexible framework; the EU AI Act is binding law with specific mandatory obligations, deadlines, and penalties.** This distinction drives most of the gaps.

## High-Level Conceptual Mapping

| NIST AI RMF | EU AI Act Equivalent |
|---|---|
| GOVERN | Risk management system (Art. 9), quality management system (Art. 17), governance/accountability provisions for providers and deployers |
| MAP | Risk categorization (prohibited/high-risk/limited-risk/minimal-risk tiers under Art. 5-6, Annex III), intended purpose documentation |
| MEASURE | Conformity assessment (Art. 43), testing/validation requirements (Art. 9), accuracy/robustness/cybersecurity requirements (Art. 15) |
| MANAGE | Post-market monitoring (Art. 72), incident reporting (Art. 73), corrective actions (Art. 20) |
| Trustworthiness characteristics (fair, explainable, privacy-enhanced, etc.) | Specific high-risk system requirements: data governance (Art. 10), transparency (Art. 13), human oversight (Art. 14), accuracy/robustness/cybersecurity (Art. 15) |

## Function-by-Function Comparison

### GOVERN ↔ Risk & Quality Management System
- AI RMF's GOVERN function (policies, accountability, risk tolerance, culture) maps closely to the EU AI Act's mandatory **risk management system** (Article 9) and **quality management system** (Article 17) for high-risk AI providers.
- Where AI RMF says "establish roles and responsibilities," the AI Act mandates specific roles: an **EU-based authorized representative** for non-EU providers, and eventually **fundamental rights impact assessments** for certain deployers (Article 27).
- The AI Act also requires **conformity assessment** and **CE marking** for high-risk systems — there's no AI RMF equivalent since AI RMF has no certification mechanism.

### MAP ↔ Risk Classification
- AI RMF's MAP function (context, categorization, stakeholder identification) aligns with the AI Act's risk-tiering exercise: determining whether a system is **prohibited** (Art. 5 — e.g., social scoring, certain biometric categorization), **high-risk** (Art. 6/Annex III — e.g., employment, credit, law enforcement, education), **limited risk** (transparency obligations, e.g., chatbots, deepfakes), or **minimal risk**.
- Gap: AI RMF doesn't have a legally defined risk taxonomy. The Act's Annex III list of high-risk use cases is prescriptive and binding — AI RMF leaves risk categorization to organizational judgment.

### MEASURE ↔ Technical Requirements & Conformity Assessment
- AI RMF's MEASURE activities (testing trustworthiness characteristics, bias testing, red-teaming) map to the Act's substantive high-risk requirements under Articles 9-15: data governance, technical documentation, record-keeping, transparency, human oversight, and accuracy/robustness/cybersecurity.
- Gap: The AI Act requires **conformity assessment** — either self-assessment or third-party (notified body) assessment depending on the use case — before market placement. AI RMF has no equivalent formal pre-market assessment or certification step.
- Gap: The Act mandates specific **technical documentation** (Annex IV) with prescribed content. AI RMF's MEASURE documentation is more flexible/less prescriptive.

### MANAGE ↔ Post-Market Monitoring & Incident Reporting
- AI RMF's MANAGE (risk response, monitoring, incident handling) aligns with the Act's **post-market monitoring system** (Art. 72) and **serious incident reporting** obligations (Art. 73), which require reporting to market surveillance authorities within specific timeframes (as short as 2 days for certain serious incidents).
- Gap: AI RMF has no mandatory regulatory reporting timeline or authority to report to. The Act's incident reporting is time-bound and legally enforceable.

## Trustworthiness Characteristics ↔ Substantive Requirements

| AI RMF Characteristic | EU AI Act Article |
|---|---|
| Valid and Reliable | Art. 15 (accuracy, robustness) |
| Safe | Art. 9 (risk management), Art. 15 |
| Secure and Resilient | Art. 15 (cybersecurity) |
| Accountable and Transparent | Art. 13 (transparency), Art. 26 (deployer obligations) |
| Explainable and Interpretable | Art. 13 (instructions for use), Art. 86 (right to explanation for individual decisions) |
| Privacy-Enhanced | Art. 10 (data governance) — though GDPR remains the primary privacy law, not the AI Act itself |
| Fair (bias managed) | Art. 10 (data governance — bias examination/mitigation in training data) |

## Key Gaps to Fill If You Implement AI RMF but Must Also Comply with EU AI Act

1. **Legal risk classification is mandatory, not optional.** You must formally determine if your system falls under Art. 5 prohibited practices, Annex III high-risk categories, Art. 50 limited-risk transparency triggers, or minimal risk — and document that determination. AI RMF's MAP function doesn't force this legal determination; you'll need a dedicated legal/compliance overlay.

2. **Conformity assessment and CE marking.** For high-risk systems, you need a conformity assessment procedure (internal control per Annex VI, or third-party via notified body per Annex VII depending on the system type), registration in the **EU database for high-risk AI systems** (Art. 71), and CE marking. AI RMF has no analog — this must be added entirely.

3. **Fundamental Rights Impact Assessment (FRIA).** Certain deployers of high-risk AI (notably public bodies and certain private entities like banks/insurers) must conduct an FRIA under Article 27. This is more specific and legally mandatory compared to AI RMF's general stakeholder-impact mapping in MAP.

4. **Prescribed technical documentation (Annex IV).** The Act specifies exact required contents for technical documentation. AI RMF documentation practices should be mapped against this checklist to ensure nothing is missing.

5. **Mandatory incident reporting with strict deadlines.** Build a formal serious-incident reporting process to national market surveillance authorities (deadlines can be as short as 2-15 days depending on severity) — AI RMF's MANAGE function doesn't specify this.

6. **Transparency obligations for specific system types.** Chatbots, emotion recognition, biometric categorization, and deepfake/synthetic content generation have **specific disclosure requirements** (Art. 50) that go beyond AI RMF's general transparency principle — e.g., labeling AI-generated content, informing users they're interacting with AI.

7. **Prohibited practices screening.** You must affirmatively screen against Article 5's prohibited AI practices (e.g., social scoring, real-time remote biometric identification in public spaces for law enforcement with narrow exceptions, manipulative/subliminal techniques, exploiting vulnerabilities). AI RMF has no prohibited-use list — this is a pure compliance gap that must be added.

8. **General-Purpose AI (GPAI) model obligations.** If you develop or use foundation/GPAI models, Chapter V of the Act imposes specific obligations (technical documentation, copyright compliance summaries, systemic-risk model requirements for the most capable models) that have no direct AI RMF counterpart — though the NIST Generative AI Profile (AI 600-1) helps partially bridge this.

9. **Designated roles and legal representatives.** The Act requires specific legal roles (EU authorized representative, importer, distributor obligations) tied to the AI value chain — GOVERN doesn't specify these role types since it's jurisdiction-agnostic.

10. **Penalties and enforcement.** AI RMF has no enforcement mechanism. You need a compliance program that tracks the Act's tiered penalty structure (up to 7% of global annual turnover for prohibited practice violations, up to 3% for other high-risk violations) to properly prioritize remediation investment — this should heavily influence your MANAGE-function risk prioritization.

## Recommended Approach

Use **AI RMF as your overarching risk management operating model** (culture, process, continuous improvement) and **layer the EU AI Act's specific legal requirements as a compliance checklist** on top of it — particularly for classification, conformity assessment, documentation, and incident reporting. Many organizations build a crosswalk matrix mapping each AI RMF subcategory to specific AI Act articles (similar tables exist from ISO 42001 crosswalks) to avoid duplicating effort while ensuring nothing legally mandatory is missed. Treat GOVERN as the natural home for AI Act program ownership, since it already covers policy, accountability, and regulatory alignment.
