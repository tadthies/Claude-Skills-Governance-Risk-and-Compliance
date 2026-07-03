# NIST AI RMF ↔ EU AI Act: Mapping and Gap Analysis

The key thing to understand upfront: **the EU AI Act is mandatory law for in-scope providers/deployers; the NIST AI RMF is a voluntary methodology.** The AI RMF is an excellent operational framework for *satisfying* the EU AI Act's risk-management requirements, but it does not automatically make you compliant — the Act adds binding legal obligations (documentation, conformity assessment, registration, penalties) that the AI RMF doesn't itself specify.

## Function-Level Mapping

| AI RMF Function | EU AI Act Requirement |
|------------------|------------------------|
| GOVERN 1 (AI risk policies) | Art. 9 (Risk management system) for high-risk AI |
| GOVERN 2/3 (Accountability) | Art. 16 (Obligations of high-risk AI providers), Art. 26 (Deployer obligations) |
| MAP 1 (Intended use) | Art. 9(2) — risk management must cover intended and reasonably foreseeable misuse |
| MAP 3 (Stakeholder mapping) | Art. 9(2)(b) — identification and analysis of known and foreseeable risks |
| MEASURE 2 (System evaluation) | Art. 10 (Data governance), Art. 15 (Accuracy, robustness, cybersecurity) |
| MEASURE 3 (Ongoing monitoring) | Art. 72 (Post-market monitoring), Art. 26(5) — deployer monitoring obligations |
| MANAGE 3 (Incident response) | Art. 73 (Reporting of serious incidents to market surveillance) |
| All functions | Annex IX (Technical documentation requirements for high-risk AI systems) |

This mapping is close at the *process* level — both frameworks want you to establish risk management, understand context/intended use, evaluate systems pre-deployment, monitor post-deployment, and respond to incidents. If your AI RMF implementation is mature (Tier 3 "Repeatable" or higher), you already have the operational muscle the Act expects.

## Where the AI RMF Alone Leaves Gaps

The AI RMF is deliberately non-prescriptive and jurisdiction-agnostic — it tells you *what outcome* to achieve, not the *specific legal artifact* a regulator requires. These are the gaps you need to fill separately:

### 1. Risk-tiering and prohibited-use determination
The AI RMF doesn't classify systems into legal risk tiers. The EU AI Act has a defined taxonomy — **unacceptable risk (prohibited)**, **high-risk (Annex III)**, **limited risk (transparency obligations)**, **minimal risk**. You must run a separate classification exercise to determine which tier each system falls into; this determines which Act obligations even apply. AI RMF's MAP 1/GOVERN 6 gives you the process to *do* this classification, but you need EU AI Act legal expertise to get the tiering right.

### 2. Conformity assessment and CE marking
For high-risk systems, the Act requires a formal **conformity assessment** (Art. 43) and **CE marking** before market placement. Nothing in the AI RMF corresponds to this — it's a regulatory certification step layered on top of your risk management work.

### 3. EU database registration
High-risk AI systems (with limited exceptions) must be registered in the **EU database for high-risk AI systems** (Art. 71) before deployment. This is a pure compliance/legal action with no AI RMF analog.

### 4. Fundamental Rights Impact Assessment (FRIA)
Certain deployers of high-risk AI (notably public bodies and specific private-sector use cases like credit scoring, insurance) must conduct a **FRIA** (Art. 27). AI RMF's MAP 3 (stakeholder risk/benefit mapping) is a good foundation, but the FRIA has specific statutory content requirements (description of deployment process, categories of affected persons, specific risks of harm, human oversight measures) that go beyond a generic stakeholder matrix.

### 5. Annex IX technical documentation format
The Act specifies a detailed, prescriptive technical documentation structure (Annex IV/IX) for high-risk systems. AI RMF's MEASURE 2.6 says "document evaluation results" but doesn't specify format. You'll need to build a documentation template that satisfies the Annex IV content list specifically — general model/system cards from MAP 2 won't be sufficient on their own.

### 6. Serious incident reporting timelines and format
Art. 73 requires reporting serious incidents to market surveillance authorities within defined statutory timeframes. AI RMF MANAGE 3.2 says "document, report, and investigate incidents" but has no timeline or regulator-notification mechanics — you need an EU AI Act-specific incident reporting procedure layered on your MANAGE 3 process.

### 7. Provider vs. deployer obligation split
The Act imposes materially different obligations on **providers** (Art. 16) vs. **deployers** (Art. 26) of high-risk AI. AI RMF's GOVERN 3 talks generally about "developer/operator/deployer responsibilities" but doesn't legally distinguish the two roles the way the Act does. You need a role determination exercise to know which obligation set applies to you (this matters especially if you fine-tune or deploy a third-party foundation model).

### 8. General-purpose AI (GPAI) model obligations
The Act has a separate chapter (Chapter V) of obligations for providers of general-purpose AI models, including systemic-risk GPAI models — training data summaries, copyright compliance, model evaluation for systemic risk. This has no direct AI RMF category; if you build or fine-tune foundation models, you need this addressed separately, though NIST's Generative AI Profile (a companion resource) can help operationally.

### 9. Penalties and legal liability
The Act has statutory penalty tiers (up to €35M or 7% of global turnover for prohibited-practice violations). This creates a legal risk dimension that should elevate certain AI RMF risk-register entries (MAP 4.1 prioritization) to "automatic high priority regardless of technical severity" — a nuance the generic AI RMF scoring model doesn't capture on its own.

## Recommended Approach

1. **Use AI RMF as your operational risk management engine** — GOVERN for accountability, MAP/MEASURE/MANAGE for the technical and organizational risk lifecycle. This satisfies the *substance* of Art. 9's "appropriate risk management system" requirement.
2. **Layer EU AI Act legal requirements on top** as a compliance overlay: risk-tier classification, conformity assessment, EU database registration, FRIA (where applicable), Annex IV/IX documentation format, Art. 73 incident timelines, and provider/deployer role determination.
3. **Assign legal/compliance ownership** (GOVERN 6.1/6.3) specifically for tracking EU AI Act statutory deadlines — the Act's obligations phase in over time (prohibited practices, GPAI obligations, and high-risk obligations have different applicability dates), and AI RMF's general "track applicable regulations" guidance won't catch this on its own.
4. **Build one unified technical documentation package per high-risk system** that satisfies both AI RMF MEASURE 2.6 documentation and Annex IV's specific content requirements, so you're not maintaining duplicate artifacts.

## Bottom Line

AI RMF gets you 70-80% of the way to EU AI Act operational readiness because both frameworks share the same risk-management DNA. The remaining gap is almost entirely **legal/regulatory-specific**: classification, certification, registration, statutory documentation format, and incident-reporting mechanics. Close that gap with dedicated EU AI Act legal review rather than assuming AI RMF maturity alone satisfies it.

---
*This is general compliance guidance, not legal advice. EU AI Act obligations are complex, jurisdiction-specific, and phase in on a statutory timeline. Consult qualified EU regulatory counsel to confirm your risk classification and specific obligations.*
