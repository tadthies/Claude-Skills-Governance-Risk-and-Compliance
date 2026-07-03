# Predictive Policing AI Based on Personality Traits — Permitted?

## Short answer: No, this is prohibited (or extremely close to a prohibited practice) under the EU AI Act.

## Why

The EU AI Act, at **Article 5(1)(d)**, prohibits placing on the market, putting into service, or using an AI system for making **risk assessments of natural persons** in order to assess or predict the risk of a natural person committing a criminal offence, **when that assessment is based solely on profiling of a natural person or on assessing their personality traits and characteristics**.

The system you describe — predicting the likelihood of individuals committing future criminal offences based on **personality traits and past behaviour** — matches this prohibition almost exactly. This is one of the Act's enumerated "unacceptable risk" practices, banned outright regardless of context, including for law enforcement use.

### Key elements of the prohibition
1. **Purpose**: predicting/assessing risk of a natural person committing a criminal offence.
2. **Basis**: profiling or personality trait/characteristic assessment (as opposed to objective, verifiable facts directly linked to criminal activity).
3. **Scope**: applies to AI systems used by any actor, but is particularly targeted at law enforcement and public authority use cases like the one described.

### The narrow carve-out
Article 5(1)(d) includes an exception: the prohibition does **not** apply to AI systems used to support the human assessment of the involvement of a person in a criminal activity that is **already based on objective and verifiable facts directly linked to a criminal activity**. In other words, an investigative tool that helps connect a specific individual to an actual, factual criminal activity (e.g., linking evidence) may fall outside the ban.

Your described use case does not fit this exception because:
- It is a **predictive/actuarial risk score** about *future* offending, not an aid to investigating an existing, factual criminal activity.
- It explicitly relies on **personality traits and past behaviour profiling**, which is the exact basis the prohibition targets.

## What this means practically

- You should **not** market, sell, or deploy this system for use by the police force as described. Doing so would expose both you (as provider) and the police force (as deployer) to the Act's most severe enforcement consequences.
- **Penalties for prohibited practices** are the highest tier under the Act: fines of up to **€35 million or 7% of total worldwide annual turnover** for the preceding financial year, whichever is higher (Article 99).
- This prohibition has applied since **2 February 2025** (six months after entry into force), so it is already in full legal effect as of today (July 2026).

## Related but distinct: predictive policing generally

Note that not all "predictive policing" is banned — the prohibition is specifically about **individual risk prediction based on profiling/personality traits**. Location-based or crime-pattern analytics (e.g., predicting where crimes are more likely to occur, not who will commit them) are treated differently and may instead fall under **Annex III high-risk categories** (e.g., point 6, law enforcement) rather than the outright prohibition — though such systems still carry substantial risk-assessment and human-rights concerns and would need to be carefully assessed against Annex III and other prohibitions (e.g., Article 5 also bans certain biometric categorisation and untargeted facial recognition scraping).

## Recommendation

- Do not proceed with development/sale of this specific product for this use case.
- If there is a genuine investigative need, consider redesigning the tool to support human analysts in linking objective, verifiable facts to specific known criminal activity, rather than producing predictive risk scores based on personality/behavioural profiling — and even then, obtain qualified EU legal review, since law-enforcement AI is one of the most heavily scrutinized areas of the Act.

*Disclaimer: This is general informational guidance, not legal advice. Given the severity of prohibited-practice consequences, engage EU AI Act legal counsel before any further development or procurement discussions.*
