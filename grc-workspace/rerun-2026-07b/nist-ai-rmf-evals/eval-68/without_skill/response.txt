# AI Risk Register Template — Credit Scoring Model (Financial Services)

Below is a practical AI risk register template mapped to the NIST AI RMF core functions/categories, tailored for a credit scoring model. Each row represents a risk entry; the table structure and category list can be copied into Excel/GRC tooling.

## Register Structure

| Field | Description |
|---|---|
| Risk ID | Unique identifier (e.g., CS-001) |
| Risk Description | Plain-language statement of the risk |
| AI RMF Function | GOVERN / MAP / MEASURE / MANAGE |
| AI RMF Category | Specific subcategory (e.g., MAP 1.1, MEASURE 2.11) |
| Trustworthiness Characteristic | Fairness, Validity/Reliability, Explainability, Privacy, Safety, Security, Accountability |
| Likelihood | Low / Medium / High |
| Impact | Low / Medium / High / Critical |
| Inherent Risk Rating | Likelihood x Impact |
| Existing Controls | Current mitigations in place |
| Treatment Option | Mitigate / Transfer / Avoid / Accept |
| Residual Risk Rating | Post-treatment rating |
| Owner | Accountable role |
| Target Date | Remediation deadline |
| Status | Open / In Progress / Closed / Accepted |

## Sample Populated Risk Entries

### 1. Fair Lending / Disparate Impact Risk
- **Risk ID:** CS-001
- **Description:** Model produces statistically significant disparate impact on protected classes (race, national origin, sex, age) in credit approval or pricing decisions, violating ECOA/Regulation B and Fair Housing Act.
- **AI RMF Function/Category:** MEASURE 2.11 (fairness and bias), MAP 1.1 (context/purpose)
- **Trustworthiness Characteristic:** Fair with harmful bias managed
- **Likelihood:** Medium | **Impact:** Critical | **Inherent Risk:** High
- **Existing Controls:** Proxy variable review; disparate impact testing pre-launch
- **Treatment:** Mitigate — implement adverse impact ratio testing, remove/adjust proxy variables, add fairness constraints to model training
- **Residual Risk:** Medium
- **Owner:** Chief Model Risk Officer / Fair Lending Officer
- **Status:** In Progress

### 2. Adverse Action Notice / Explainability Gap
- **Risk ID:** CS-002
- **Description:** Model cannot generate legally sufficient, specific reasons for denial as required by ECOA/Reg B (adverse action notices) and FCRA.
- **AI RMF Function/Category:** MEASURE 2.9 (explainability/interpretability), GOVERN 1.1 (legal/regulatory alignment)
- **Trustworthiness Characteristic:** Explainable and Interpretable, Accountable and Transparent
- **Likelihood:** Medium | **Impact:** High | **Inherent Risk:** High
- **Existing Controls:** SHAP/feature-attribution reason-code generator
- **Treatment:** Mitigate — validate reason codes map to actual top model drivers; legal review of generated notice language
- **Residual Risk:** Low
- **Owner:** Model Risk Management / Compliance
- **Status:** Open

### 3. Model Drift / Degraded Predictive Validity
- **Risk ID:** CS-003
- **Description:** Model performance degrades over time due to changing economic conditions, applicant population shifts, or data drift, leading to inaccurate risk scoring.
- **AI RMF Function/Category:** MEASURE 2.5 (validity/reliability, ongoing monitoring), MANAGE 4.1 (continuous monitoring)
- **Trustworthiness Characteristic:** Valid and Reliable
- **Likelihood:** High | **Impact:** High | **Inherent Risk:** High
- **Existing Controls:** Quarterly back-testing against actual default rates
- **Treatment:** Mitigate — implement automated drift detection, define retraining triggers/thresholds, champion-challenger model framework
- **Residual Risk:** Medium
- **Owner:** Model Risk Management
- **Status:** In Progress

### 4. Third-Party/Vendor Model Risk
- **Risk ID:** CS-004
- **Description:** Credit scoring model or key data inputs are sourced from a third-party vendor whose model logic, training data, or validation practices are not fully transparent.
- **AI RMF Function/Category:** GOVERN 6.1 (third-party risk), MAP 1.5 (vendor/supply chain mapping)
- **Trustworthiness Characteristic:** Accountable and Transparent, Secure and Resilient
- **Likelihood:** Medium | **Impact:** High | **Inherent Risk:** High
- **Existing Controls:** Vendor due diligence questionnaire, SOC 2 report review
- **Treatment:** Mitigate — contractual audit rights, require vendor model documentation/model card, independent validation of vendor outputs
- **Residual Risk:** Medium
- **Owner:** Vendor Risk Management / Procurement
- **Status:** Open

### 5. Data Privacy / Unauthorized Data Use
- **Risk ID:** CS-005
- **Description:** Model uses alternative data sources (social media, utility payments, geolocation) that raise privacy concerns or exceed permissible use under FCRA/GLBA.
- **AI RMF Function/Category:** MAP 1.1 (data mapping), MEASURE 2.10 (privacy)
- **Trustworthiness Characteristic:** Privacy-Enhanced
- **Likelihood:** Low | **Impact:** High | **Inherent Risk:** Medium
- **Existing Controls:** Data source approval process, privacy legal review
- **Treatment:** Mitigate — data minimization review, consent verification, GLBA safeguards audit
- **Residual Risk:** Low
- **Owner:** Data Privacy Officer
- **Status:** Closed

### 6. Lack of Human Oversight / Over-Reliance
- **Risk ID:** CS-006
- **Description:** Loan officers rubber-stamp model outputs without meaningful review, creating automation bias and undermining human-in-the-loop safeguards.
- **AI RMF Function/Category:** GOVERN 3.2 (human-AI teaming/oversight), MANAGE 2.2 (mechanisms for human oversight)
- **Trustworthiness Characteristic:** Accountable and Transparent, Safe
- **Likelihood:** Medium | **Impact:** Medium | **Inherent Risk:** Medium
- **Existing Controls:** Manual review requirement for denials near threshold
- **Treatment:** Mitigate — training for loan officers, override tracking/audit, escalation path for edge cases
- **Residual Risk:** Low
- **Owner:** Credit Operations
- **Status:** In Progress

### 7. Model Security / Adversarial Manipulation
- **Risk ID:** CS-007
- **Description:** Applicants or bad actors reverse-engineer scoring logic to game the model (e.g., synthetic identity fraud, strategic application timing).
- **AI RMF Function/Category:** MEASURE 2.7 (security/resilience), MANAGE 4.2 (incident response)
- **Trustworthiness Characteristic:** Secure and Resilient
- **Likelihood:** Medium | **Impact:** Medium | **Inherent Risk:** Medium
- **Existing Controls:** Fraud detection layer, rate limiting on applications
- **Treatment:** Mitigate — adversarial testing, anomaly detection on application patterns
- **Residual Risk:** Low
- **Owner:** Fraud Risk / InfoSec
- **Status:** Open

### 8. Regulatory/Examination Risk
- **Risk ID:** CS-008
- **Description:** Model governance documentation is insufficient to satisfy regulatory exam requirements (OCC, Fed, CFPB, state regulators) under SR 11-7 model risk management guidance.
- **AI RMF Function/Category:** GOVERN 1.2 (policies/processes), GOVERN 4.1 (documentation)
- **Trustworthiness Characteristic:** Accountable and Transparent
- **Likelihood:** Medium | **Impact:** High | **Inherent Risk:** High
- **Existing Controls:** Model documentation standard in draft
- **Treatment:** Mitigate — complete model risk management documentation aligned to SR 11-7 and AI RMF, independent validation function
- **Residual Risk:** Medium
- **Owner:** Chief Model Risk Officer
- **Status:** Open

### 9. Concept/Definition Risk (What Counts as "Creditworthy")
- **Risk ID:** CS-009
- **Description:** Model's target variable (e.g., "default within 24 months") may not align with the business's actual risk tolerance or regulatory definition of creditworthiness, leading to misaligned decisions.
- **AI RMF Function/Category:** MAP 2.1 (context and purpose), MAP 1.2 (goals and objectives)
- **Trustworthiness Characteristic:** Valid and Reliable
- **Likelihood:** Low | **Impact:** Medium | **Inherent Risk:** Low
- **Existing Controls:** Business/risk committee sign-off on target variable definition
- **Treatment:** Accept (with periodic review)
- **Residual Risk:** Low
- **Owner:** Credit Risk Strategy
- **Status:** Closed

### 10. Incident Response Gap
- **Risk ID:** CS-010
- **Description:** No formal process exists to detect, escalate, and remediate an AI-driven credit decisioning incident (e.g., mass erroneous denials due to a data pipeline bug).
- **AI RMF Function/Category:** MANAGE 4.1, MANAGE 4.3 (incident response and recovery)
- **Trustworthiness Characteristic:** Safe, Accountable and Transparent
- **Likelihood:** Low | **Impact:** Critical | **Inherent Risk:** Medium
- **Existing Controls:** General IT incident response plan (not AI-specific)
- **Treatment:** Mitigate — build AI-specific incident playbook, define rollback procedures, customer remediation process
- **Residual Risk:** Low
- **Owner:** Model Risk Management / IT Operations
- **Status:** Open

## Treatment Option Definitions

- **Mitigate:** Reduce likelihood or impact through controls (most common for fairness, explainability, drift risks)
- **Transfer:** Shift risk via insurance, vendor contractual indemnification (relevant for third-party model risk)
- **Avoid:** Discontinue the risky practice entirely (e.g., avoid using a prohibited data source)
- **Accept:** Formally accept residual risk with sign-off from risk committee (appropriate only for low-impact, well-understood risks)

## Recommended Governance Cadence

- **Risk register review:** Quarterly by Model Risk Management Committee
- **Fairness/bias re-testing:** Quarterly or upon any model retraining
- **Full AI RMF GOVERN alignment review:** Annually
- **Regulatory mapping refresh:** Whenever ECOA/Reg B, FCRA, or state AI lending laws change

This register should be treated as a living document, updated whenever the model is retrained, new data sources are added, or new regulatory guidance is issued.
