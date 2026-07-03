# NIST AI RMF: The Four Core Functions and Where to Start

Great timing to build this in from the start rather than retrofit it later. The NIST AI Risk Management Framework (AI RMF 1.0 / NIST AI 100-1) is voluntary and non-prescriptive, structured around four functions that work together as a continuous cycle rather than a linear checklist.

## The Four Functions

### GOVERN — Organizational Accountability (6 categories, ~21 subcategories)
GOVERN establishes the culture, policies, accountability structures, and risk tolerance for AI across your organization. It is the foundation: every MAP, MEASURE, and MANAGE activity should operate inside the accountability structures GOVERN establishes.

Key categories:
- **GOVERN 1** — AI risk policies, processes, and practices in place (ERM integration, risk tolerance, regulatory alignment)
- **GOVERN 2** — Accountability structures (senior officials accountable for AI risk outcomes)
- **GOVERN 3** — Roles and responsibilities defined across the AI lifecycle
- **GOVERN 4** — Cross-functional collaboration (AI/ML, legal, privacy, security, HR, ethics)
- **GOVERN 5** — Risk tolerance communicated and reflected in go/no-go deployment decisions
- **GOVERN 6** — Alignment with applicable laws, regulations, and ethical principles

### MAP — Risk Identification (5 categories, ~20 subcategories)
MAP establishes context — intended use, deployment environment, affected stakeholders — before a system is measured or managed. A well-executed MAP phase prevents you from spending MEASURE/MANAGE resources chasing the wrong risks.

Key categories: context of intended use (MAP 1), scientific understanding of capabilities/limitations (MAP 2), risks/benefits mapped to stakeholders (MAP 3), risk prioritization (MAP 4), and likelihood/impact characterization (MAP 5).

### MEASURE — Risk Analysis (4 categories, ~16 subcategories)
MEASURE applies quantitative, qualitative, and mixed-method tools — collectively called **TEVV** (Test, Evaluation, Verification, and Validation) — to assess the risks MAP identified.

Key categories: measurement approaches identified (MEASURE 1), trustworthiness evaluation across the lifecycle including bias, explainability, and security testing (MEASURE 2), ongoing tracking for drift/degradation (MEASURE 3), and feedback loops into MANAGE (MEASURE 4).

### MANAGE — Risk Response (4 categories, ~18 subcategories)
MANAGE is where you act — prioritizing, treating, monitoring, and closing the loop on AI risks back into GOVERN.

Key categories: risks prioritized/documented for treatment (MANAGE 1), treatment strategies planned and resourced (MANAGE 2), responses monitored with incident response in place (MANAGE 3), and lessons learned feeding back into policy (MANAGE 4).

## How the Four Functions Relate

```
        ┌─────────────────────────────────────────┐
        │              GOVERN (foundation)          │
        │   policies · accountability · risk        │
        │   tolerance · cross-functional teams       │
        └─────────────────────────────────────────┘
                 ▲                        │
                 │                        ▼
        ┌─────────────┐          ┌─────────────┐
        │   MANAGE     │◄─────────│     MAP      │
        │  (respond)   │          │  (identify)  │
        └─────────────┘          └─────────────┘
                 ▲                        │
                 │                        ▼
                 └────────────┌─────────────┐
                               │   MEASURE    │
                               │  (analyze)   │
                               └─────────────┘
```

GOVERN is drawn as the base of the AI RMF diagram because it is cross-cutting — it isn't a phase you complete once, it's the continuous accountability layer everything else operates inside. MAP, MEASURE, and MANAGE then form an iterative loop for each AI system: you MAP the context and risks, MEASURE them with TEVV activities, MANAGE the response, and feed lessons learned back into both GOVERN (policy updates) and MAP (revised context as the system or its environment changes).

## What to Implement First

**Start with GOVERN.** Specifically, in this order:

1. **GOVERN 1** — Publish an org-wide AI Risk Management Policy signed by senior leadership, and define your AI risk appetite (e.g., acceptable bias thresholds, accuracy floors)
2. **GOVERN 2** — Appoint an accountable owner (AI Risk Owner or similar) with real authority and board/executive visibility
3. **GOVERN 4** — Stand up a cross-functional AI Risk Working Group (legal, privacy, security, HR, engineering) — you will need this group's input immediately once you start MAPping individual systems
4. **GOVERN 5/6** — Define risk tolerance tiers (low-stakes vs. high-stakes systems affecting individuals) and identify applicable regulations now, since this will drive how deep your MAP/MEASURE work needs to go per system

Only after these accountability structures exist should you move to **MAP** on a system-by-system basis: document each AI system's intended use, affected populations, and prohibited use cases (MAP 1), then flow into MEASURE (TEVV testing) and MANAGE (treatment) for that system.

A common failure pattern to avoid: organizations write GOVERN policies but never operationalize them — MAP/MEASURE/MANAGE activity on actual deployed systems doesn't reflect the policy. Treat GOVERN as continuous and revisit it as you learn from each system's MAP/MEASURE/MANAGE cycle, not as a one-time gate you pass through.

## Suggested Next Step

Once GOVERN's foundational pieces are in place, I'd recommend picking your highest-risk or highest-visibility AI system first and running it through a full MAP → MEASURE → MANAGE cycle as a pilot. That gives you a template and demonstrates value before you scale the process organization-wide.

---
*This is general compliance guidance, not legal advice. Verify current requirements against the official NIST AI 100-1 publication and consult qualified counsel for regulatory decisions specific to your organization.*
