# Predictive Criminal Risk Tool for Police Procurement — Prohibited Under Art. 5

## Short Answer
**No — this system cannot be lawfully placed on the market or used in the EU.** It falls directly within a Prohibited AI Practice under **Article 5(1)(d)** of the EU AI Act. This is not a high-risk classification question; the prohibition takes precedence and forecloses lawful deployment entirely, regardless of any conformity assessment, documentation, or human-oversight measures you might otherwise implement.

## 1. AI System Definition Check
The system infers from inputs (personality traits, past behaviour data) to generate an output (a predicted likelihood of future offending) — this meets the Art. 3(1) AI system definition.

## 2. Prohibited Practices Screen (Art. 5) — This Is Where the Analysis Ends

> **Art. 5(1)(d) — Predictive Criminal Risk Assessment:** AI systems assessing the risk of natural persons committing criminal offences based **solely on profiling** or the assessment of **personality traits and characteristics**.

Your system is described as predicting "the likelihood of individuals committing future criminal offences based on personality traits and past behaviour" — this is a near word-for-word match to the prohibited category. Using personality-trait profiling as the basis for predicting future (not yet committed) criminal conduct is exactly what Art. 5(1)(d) bans.

### The narrow exception — and why it does not save this system
Art. 5(1)(d) contains one exception: systems that **support a human assessment based on objective, verifiable facts directly linked to a criminal activity** are not prohibited. This exception is narrow and does not apply here because:
- Your system's inputs are **personality traits and past behaviour** — not objective, verifiable facts tied to a *specific, already-occurring* criminal activity.
- "Past behaviour" framed as a general predictor of future propensity is character/personality-based profiling, which is precisely what the article targets — it is not the same as evidence directly linking a person to a specific offence under investigation.
- The system predicts a *general likelihood* of future offending (a profiling-based propensity score), not an assessment of a *specific* individual's involvement in a *specific* criminal act based on verifiable facts.

**Conclusion: the exception does not apply. The system is prohibited as designed.**

## 3. Consequence for Procurement
Because this is a **Prohibited Practice under Art. 5**, not merely a high-risk (Annex III, Area 6 — Law Enforcement) system:
- It **cannot** be brought into lawful use in the EU by placing safeguards, conformity assessments, or documentation around it — prohibition means the activity itself is banned, not just regulated.
- The national police force **cannot lawfully procure or deploy it** for this stated purpose.
- As the would-be provider, you **cannot place it on the market or put it into service** in the EU for this use case.

This prohibition has applied since **2 February 2025** — it is already fully in force, well before today's date of 3 July 2026.

## 4. Penalties Exposure (Art. 99)
Prohibited-practice violations carry the highest tier of AI Act fines:

> **Up to €35,000,000 or 7% of total worldwide annual turnover, whichever is higher.**

This applies to both the provider (you) and the deploying entity (the police force) if the system were deployed despite the prohibition.

## 5. What Would Need to Change
If the police force's actual need is to support human investigators in evaluating a **specific individual's connection to a specific, already-committed offence**, using **objective, verifiable facts** (e.g., forensic evidence, documented prior convictions directly tied to modus operandi, corroborated witness statements) — rather than personality-trait or general-propensity profiling — that narrower use case might fall under the Art. 5(1)(d) exception and instead be evaluated as a potential **high-risk Annex III Area 6(d) system** (assessing risk of offending/reoffending) or Area 6(c) (evaluating reliability of evidence). That would trigger the full high-risk conformity regime (Arts. 9–17, 43–49) rather than an outright ban — but this would require a fundamentally different system design, not a repackaging of the current personality/behaviour-based predictive tool.

I'd also flag: even a redesigned "supports human assessment" tool operating in the law-enforcement context should be checked against Art. 5(1)(g) (biometric categorisation for sensitive attributes) and Art. 5(1)(c) (social scoring) to make sure no other prohibition is triggered by the broader system design.

## Bottom Line
- **Permitted? No.** Prohibited under Art. 5(1)(d) — predictive criminal risk assessment based on personality traits/profiling.
- **Exception applies? No** — inputs are trait/behaviour-based profiling, not objective facts tied to a specific offence.
- **Action:** Do not proceed with procurement or deployment of the system as described. Any viable path forward requires redesigning around objective, verifiable, offence-specific facts and would then need full Annex III Area 6 high-risk compliance, not just an Art. 5 workaround.

*This is general compliance information, not legal advice. Given the fundamental-rights and criminal-justice stakes here, consult qualified counsel before any further steps.*
