# AI Hiring Tool: NIST AI RMF Risk Assessment for Resume Screening/Ranking

Resume screening and candidate ranking is one of the highest-scrutiny AI use cases — it's explicitly called out as high-risk under the EU AI Act (Annex III, employment) and is directly subject to EEOC disparate impact analysis and NYC Local Law 144 (if any candidates are NYC-based). Here's how to work through it using the AI RMF's GOVERN/MAP/MEASURE/MANAGE structure.

## Key Risks to Assess (MAP Function)

Before measuring anything, MAP the context:

- **MAP 1.2 / 1.4** — Document the intended use precisely (initial screening vs. final decision-making authority) and identify affected populations: all applicants, not just hired candidates, plus current employees if the tool is also used for internal mobility
- **MAP 1.5** — Explicitly scope potential harms and misuse: disparate impact against protected classes (race, gender, age, disability, national origin), penalizing employment gaps (which correlates with caregiving/disability status), proxy discrimination via zip code or school name, and over-reliance without human review
- **MAP 3.1** — Build a stakeholder risk/benefit matrix: your organization gets efficiency/cost benefits; applicants bear the risk of unfair rejection, often with no visibility into why
- **MAP 4.1** — Prioritize: disparate impact against a protected class is automatically high-priority because it creates legal exposure and is difficult to reverse once candidates have been screened out

## Most Relevant Trustworthiness Properties

Of the seven trustworthiness characteristics, four are central to a hiring tool:

1. **Fair with Harmful Bias Managed** — the dominant risk. You need disaggregated performance by demographic subgroup and a disparate impact ratio at or above the EEOC "4/5ths rule" (0.8) for every protected group
2. **Explainable & Interpretable** — candidates and hiring managers need to understand why someone was ranked low; this also supports any adverse-action or "right to explanation" obligations
3. **Accountable & Transparent** — decisions must be traceable to a responsible party, and you need a model/system card documenting purpose, training data, and known limitations
4. **Valid & Reliable** — has the tool been tested against your actual applicant pool and job requirements, not just a generic benchmark?

Safety, Security & Resilience, and Privacy-Enhanced still matter (resumes contain PII) but are secondary to fairness and explainability for this use case.

## Specific MEASURE-Function Actions Before Deployment

Following **MEASURE 2** (trustworthiness evaluation across the lifecycle):

| Action | AI RMF Citation |
|--------|-----------------|
| Run disaggregated performance and disparate-impact-ratio testing across protected classes (race, gender, age, disability status) using historical or synthetic applicant data | MEASURE 2.2 |
| Calculate disparate impact ratio per group; flag any ratio below 0.8 (4/5ths rule) as a blocking issue | MEASURE 2.2 |
| Generate SHAP or LIME explanations for a sample of ranking decisions, especially rejections, and document them in a form a non-technical hiring manager (and, if challenged, a regulator) can understand | MEASURE 2.3 |
| Conduct a pre-deployment technical/safety evaluation covering accuracy against job-relevant criteria (not just resume-keyword matching) | MEASURE 2.1 |
| Assess privacy/security handling of applicant PII within the model pipeline | MEASURE 2.4 |
| Validate that a human-in-the-loop review step exists and is actually used — test that human oversight isn't rubber-stamping | MEASURE 2.5 |
| Document all evaluation results (metrics, methodology, limitations) in an evaluation report shared with legal, HR leadership, and the AI governance function | MEASURE 2.6 |
| Define ongoing monitoring metrics (fairness drift, subgroup performance) to catch degradation post-deployment, since applicant pools and job requirements change over time | MEASURE 3.1 |

## Before You Deploy: Non-Negotiables

1. **No fully automated rejection without human review** — bake this into the MAP 1.2 documented intended use and enforce it as a system control, not just policy
2. **Disparate impact ratio ≥ 0.8** for every protected subgroup you can measure — if any group falls below this, MANAGE 2.1 treatment (retrain, rebalance, or restrict use with human review gate) is required before go-live, with residual risk sign-off from an accountable officer per MANAGE 1.3
3. **Regulatory cross-check** — confirm compliance with EEOC guidance, NYC Local Law 144 (independent bias audit + public posting requirements, if applicable), and EU AI Act high-risk obligations (Annex IX technical documentation) if you have EU candidates or operations

## Suggested Risk Register Entry (Worked Example)

| AI System | Lifecycle Stage | TEVV Activity | Characteristic at Risk | Likelihood/Impact | Treatment | Owner |
|-----------|-----------------|----------------|--------------------------|----------------------|-----------|-------|
| Resume Screening Model | Deployment | Disaggregated performance testing by demographic subgroup (MEASURE 2.2) | Fair with Harmful Bias Managed | To be determined by testing — treat as High/High until proven otherwise | Mitigate — human review gate for all rejections; retrain if disparate impact ratio < 0.8 | Head of Talent Acquisition (treatment); Chief AI Officer or equivalent (residual risk acceptance) |

This should be one row of many — add entries for explainability gaps, PII handling, and monitoring drift as MAP and MEASURE surface them.

---
*This is general compliance guidance, not legal advice. Employment AI carries direct legal exposure (EEOC, state/local laws, EU AI Act). Consult employment counsel before finalizing deployment.*
