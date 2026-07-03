# CV Screening Tool — EU AI Act Classification

## 1. AI System Definition Check
An AI-powered CV screening tool that ranks job applicants qualifies as an **AI system** under Art. 3(1) — it is a machine-based system that infers from inputs (CVs/applications) to generate outputs (rankings/recommendations) affecting real-world outcomes (hiring decisions).

## 2. Prohibited Practices Screen (Art. 5)
A ranking/screening tool of this kind does not, on its face, match any of the 9 prohibited categories (subliminal manipulation, vulnerability exploitation, social scoring, predictive criminal risk, untargeted biometric scraping, workplace/education emotion inference, sensitive biometric categorisation, real-time RBI, or nudification/CSAM). No prohibition applies — proceed to risk-tier classification.

## 3. Risk Tier Determination — High-Risk (Annex III, Area 4)

**Yes, this is high-risk.** It falls squarely within:

> **Annex III, Area 4 — Employment, Workers Management, and Self-Employment**, sub-point (a): recruitment and selection, specifically **application filtering/screening and candidate evaluation and selection**.

Ranking applicants for employers is exactly the trigger activity for this area — filtering, screening, evaluating, or deciding on candidates (not passive aggregation of job postings, which would be out of scope).

**Art. 6(3) exceptions test:** None of the narrow non-high-risk exceptions (narrow procedural task, improving a prior human result, pattern-deviation detection only, or preparatory task) plausibly apply to a tool whose core function is to rank and thereby influence candidate selection.

**Profiling override (Art. 6(3), final subparagraph):** Even if you attempted to argue an exception, a CV-ranking tool almost certainly performs **profiling** (Art. 3(52)) — it evaluates aspects of a person's suitability/reliability/behaviour from their data to produce a score. Profiling is **always high-risk** regardless of any exception claim. This closes off any argument that the tool is "merely preparatory" or "improving a human's prior result."

**Conclusion: High-risk, Annex III Area 4(a). No documentation-based exemption is realistically available here — proceed directly to full high-risk compliance.**

## 4. Compliance Deadline
Under the Digital Omnibus (adopted 29 June 2026), the Annex III standalone high-risk deadline has been deferred:

> **Annex III high-risk obligations apply from 2 December 2027.**

You have until that date to complete the full conformity regime before the tool can be lawfully placed on the market or put into service in the EU. (This is later than the originally-legislated 2 August 2026 date — the Digital Omnibus pushed it back.)

## 5. Main Obligations as Provider (Arts. 9–17, 43–49)

As the entity developing and placing the tool on the market under your own name, you are the **provider** (Art. 3(3)). Your core obligations:

| Requirement | Article | What it means for a CV-screening tool |
|---|---|---|
| Risk management system | Art. 9 | Continuous 5-step process: identify risks (e.g., discriminatory ranking against protected groups), estimate/evaluate, monitor post-market, mitigate, document residual risk |
| Data governance | Art. 10 | Training/validation/test data for the ranking model must be relevant, representative, and error-free; bias examination is mandatory given the discrimination risk inherent in hiring AI |
| Technical documentation | Art. 11 | Annex IV file: intended purpose, development methodology, training data description, validation/testing results, risk management documentation — retained 10 years |
| Record-keeping / logging | Art. 12 | Build in automatic event logging so ranking decisions can be reconstructed later |
| Transparency to deployers | Art. 13 | Instructions for use: accuracy/robustness metrics, known risks, input data specs, human oversight measures, logging description |
| Human oversight | Art. 14 | Design the tool so employers (deployers) can understand, override, or disregard rankings — not treat them as automatic decisions; guard against automation bias |
| Accuracy, robustness, cybersecurity | Art. 15 | Declared accuracy levels in instructions for use; resilience to adversarial manipulation (e.g., CV keyword-stuffing attacks) |
| Provider checklist | Art. 16 | Full 12-item list: name/contact on system, QMS, technical documentation, logs, conformity assessment, EU Declaration of Conformity, CE marking, EU database registration, corrective action process, etc. |
| Quality management system | Art. 17 | 13-component QMS covering design, testing, data management, post-market monitoring, incident reporting |
| Conformity assessment | Art. 43 | Annex III Area 4 (Points 2–8) is **self-assessment only** — no notified body required, unlike biometrics (Area 1) |
| EU Declaration of Conformity & CE marking | Arts. 47–48 | Draw up before market placement; retain 10 years; affix CE mark |
| EU AI database registration | Art. 49 | Register the system in the EU database before placing it on the market |

**Also flag for your employer-customers (deployers):** They will carry independent Art. 26 obligations — using the tool per your instructions, assigning competent human oversight, controlling input data quality, monitoring and suspending use if risks emerge, retaining logs ≥6 months, **notifying workers/candidates before use** (Art. 26(7) and Art. 26(11) — informing affected individuals that an AI system is used in the decision), and conducting a GDPR DPIA. Since recruitment tools are not in the FRIA-mandatory list (that's limited to public bodies/services and Art. 27's 5(b)/5(c) financial use cases), a private employer deploying this tool is not automatically required to run a FRIA — but should still coordinate with you on the Art. 13 instructions that its oversight and worker-notification duties depend on.

## Bottom Line
- **High-risk: Yes** — Annex III, Area 4(a) (recruitment/candidate screening), reinforced by the profiling override.
- **Deadline:** 2 December 2027 (Digital Omnibus-confirmed).
- **Path:** Self-assessment conformity route (no notified body needed for Area 4), but full Arts. 9–17 substantive obligations, technical documentation, CE marking, and EU database registration all apply.

*This is general compliance guidance, not legal advice — confirm your specific classification and readiness plan with qualified counsel or an accredited assessor.*
