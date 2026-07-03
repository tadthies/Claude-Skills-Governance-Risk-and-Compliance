# AI Risk Register — Credit Scoring Model (Financial Services)

Below is a ready-to-use AI risk register template for a credit scoring model, built on the NIST AI RMF structure (MAP for identification, MEASURE/TEVV for analysis, MANAGE for treatment). Each row cites the specific AI RMF category it maps to so you can trace every entry back to the framework and defend your methodology to auditors or regulators.

## Register Structure

| Column | Purpose |
|--------|---------|
| Risk ID | Unique identifier |
| AI System | Name/version of the model |
| Lifecycle Stage | Design / Development / Testing / Deployment / Monitoring / Decommission |
| AI RMF Category | Function + category (+ subcategory where useful) the risk maps to |
| TEVV Activity | The test/evaluation/verification/validation activity that surfaces or measures the risk |
| Characteristic at Risk | Which of the seven trustworthiness properties is implicated |
| Likelihood / Impact | Severity × breadth × reversibility scoring (MAP 4.1) |
| Treatment | Mitigate / Transfer / Avoid / Accept + specific action |
| Owner | Accountable individual/role |

## Populated Template

| Risk ID | AI System | Lifecycle Stage | AI RMF Category | TEVV Activity | Characteristic at Risk | Likelihood / Impact | Treatment | Owner |
|---------|-----------|------------------|-------------------|-----------------|---------------------------|------------------------|-----------|-------|
| AIR-001 | Credit Scoring Model v2 | Development | MAP 1.6 — Legal/regulatory constraints identified | Legal review of ECOA, Fair Housing Act, and state fair-lending requirements | Fair with Harmful Bias Managed | High likelihood / High impact — regulatory violation exposure | Mitigate — build compliance requirements into model design specs before training; legal sign-off gate before development proceeds | Chief Compliance Officer |
| AIR-002 | Credit Scoring Model v2 | Development | MAP 3.1 — Risks/benefits mapped to stakeholders | Stakeholder risk/benefit matrix (lender efficiency vs. applicant risk of unfair denial) | Fair with Harmful Bias Managed; Accountable & Transparent | Medium likelihood / High impact | Mitigate — require disaggregated testing plan approved before training data finalized | Head of Model Risk |
| AIR-003 | Credit Scoring Model v2 | Testing | MEASURE 2.2 — Bias/fairness testing across demographic groups | Disaggregated performance testing; demographic parity, equalized odds, disparate impact ratio calculation | Fair with Harmful Bias Managed | High likelihood / High impact — disparate impact ratio below 0.8 (4/5ths rule) on preliminary testing | Mitigate — retrain with rebalanced data, adjust feature set to remove proxy variables (zip code, etc.), re-test before proceeding | Data Science Lead; residual risk accepted by Chief Risk Officer |
| AIR-004 | Credit Scoring Model v2 | Testing | MEASURE 2.3 — Explainability testing | SHAP/LIME feature attribution testing sufficient to generate adverse-action notices under ECOA/Reg B | Explainable & Interpretable; Accountable & Transparent | High likelihood / High impact — inability to generate compliant adverse-action reasons blocks deployment | Mitigate — implement SHAP-based reason-code generation; validate reason codes map to ECOA-compliant categories | Model Risk / Compliance jointly |
| AIR-005 | Credit Scoring Model v2 | Testing | MEASURE 2.1 — Pre-deployment technical/safety evaluation | Accuracy, calibration, and AUC-ROC testing against validation dataset | Valid & Reliable | Medium likelihood / High impact — poor calibration leads to mispriced risk | Mitigate — set minimum calibration/accuracy thresholds as go/no-go gate | Data Science Lead |
| AIR-006 | Credit Scoring Model v2 | Testing | MEASURE 2.4 — Security and privacy assessment | Adversarial robustness test; PII handling and data minimization review | Secure & Resilient; Privacy-Enhanced | Low likelihood / High impact | Mitigate — apply data minimization, encrypt PII at rest/in transit, run adversarial input testing | InfoSec Lead |
| AIR-007 | Credit Scoring Model v2 | Deployment | MANAGE 2.1 — Treatment strategy for below-threshold subgroup performance | N/A (treatment action, not TEVV) | Fair with Harmful Bias Managed | High impact if unresolved | Mitigate — human review escalation for any application where model confidence is low or applicant is in an affected subgroup; do not permit fully automated denial | VP Credit Risk |
| AIR-008 | Credit Scoring Model v2 | Deployment | MANAGE 1.3 — Residual risk acceptance | N/A (governance action) | Accountable & Transparent | Depends on residual gap after mitigation | Accept (with conditions) — formal sign-off required from Chief Risk Officer documenting residual bias/accuracy gap and rationale | Chief Risk Officer |
| AIR-009 | Credit Scoring Model v2 | Monitoring | MEASURE 3.1 / 3.2 — Ongoing monitoring, drift detection | Monthly monitoring dashboard: accuracy drift, fairness metric drift (PSI/KS tests on score distribution by subgroup) | Fair with Harmful Bias Managed; Valid & Reliable | Medium likelihood / High impact — model drift as economic conditions shift | Mitigate — alert thresholds (e.g., disparate impact ratio drop >0.05, accuracy drop >5%) trigger mandatory human review and re-validation | Model Owner (monthly review) |
| AIR-010 | Credit Scoring Model v2 | Monitoring | MANAGE 3.2 — Incident response | Incident log for any bias threshold breach, regulatory complaint, or data drift event | Accountable & Transparent | Depends on incident severity | Mitigate — pre-defined incident severity classification and notification thresholds (internal escalation → regulatory disclosure) | Chief Compliance Officer |
| AIR-011 | Credit Scoring Model v2 | Design/Development | GOVERN 6.1 — Regulatory alignment | Regulatory register review (ECOA, FCRA, Fair Housing Act, state fair-lending laws, EU AI Act high-risk classification if applicable) | Accountable & Transparent | High likelihood / High impact | Mitigate — maintain living regulatory register, review at each model version | Legal/Compliance |
| AIR-012 | Credit Scoring Model v2 | Decommission | MANAGE 4.4 — Risk profile reviewed on major change | Review of legacy model retirement, ensure archived decisions remain explainable for record-retention/audit period | Accountable & Transparent | Low likelihood / Medium impact | Mitigate — retain model version, training data lineage, and decision logs per record-retention policy | Data Governance Lead |

## Treatment Options Reference (MANAGE 2.1)

For any risk above tolerance, choose from:

- **Mitigate** — Technical (retrain, rebalance data, remove proxy features, add human review gate), Operational (restrict automated decisioning to certain score bands only)
- **Transfer** — Contractual indemnification with model vendor if third-party model is used; insurance for regulatory/litigation exposure
- **Avoid** — Decommission the automated feature and revert to human underwriting for the affected segment
- **Accept** — Only with documented residual-risk sign-off from an accountable senior officer (MANAGE 1.3), and only where residual risk is within stated risk tolerance (GOVERN 1.3/5.1)

## Notes on Regulatory Context

This model sits in a high-scrutiny space: ECOA and Regulation B require specific adverse-action reasons, the Fair Housing Act prohibits discriminatory effects in credit related to housing, and if you have any EU exposure, credit scoring is explicitly classified as high-risk under the EU AI Act (Annex III), triggering Art. 9 risk management system and Art. 15 accuracy/robustness/cybersecurity obligations. Build AIR-011 out into its own compliance sub-tracker if you operate in multiple jurisdictions.

Populate "Characteristic at Risk" primarily with **Fair with Harmful Bias Managed** and **Accountable & Transparent** for this use case — those are the two properties regulators and auditors will scrutinize most closely for credit decisioning.

---
*This is general compliance guidance, not legal advice. Credit scoring AI carries direct regulatory exposure under fair lending law. Consult qualified counsel and your model risk management function before finalizing this register.*
