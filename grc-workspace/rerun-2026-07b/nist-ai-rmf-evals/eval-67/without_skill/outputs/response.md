# AI Hiring Tool: NIST AI RMF Risk Assessment

An AI resume-screening and candidate-ranking tool is a textbook "consequential decision" AI system — it directly affects people's access to employment opportunities. This puts it squarely in higher-risk territory under NIST AI RMF, and likely subject to additional regulation (e.g., EEOC guidance, Illinois AI Video Interview Act, NYC Local Law 144, EU AI Act if applicable to your operations).

## Key Risks to Assess

**1. Bias and discriminatory outcomes**
- Disparate impact on protected classes (race, sex, age, disability, national origin) — even without explicit protected-class features, proxies (zip code, name, school, employment gaps) can encode bias
- Historical bias baked into training data (e.g., a model trained on past hiring decisions that reflect historical discrimination)
- Bias against non-traditional candidates (career changers, gaps for caregiving, non-traditional education)

**2. Validity and reliability**
- Does the model actually predict job performance, or just correlate with superficial resume features (keywords, formatting, university prestige)?
- Performance degradation across different resume formats, languages, or resume-writing styles
- Generalization failure for roles or candidate pools not well-represented in training data

**3. Explainability and transparency**
- Can you explain to a rejected candidate why they were screened out?
- Can recruiters/hiring managers understand and meaningfully override the tool's rankings (avoiding "automation bias" / rubber-stamping)?
- Is it clear to candidates that AI is being used (disclosure obligations)?

**4. Privacy**
- What resume/application data is collected, stored, and for how long?
- Are third-party data enrichment sources being used (social media scraping, data brokers)?
- Data minimization — is the tool inferring sensitive attributes (age from graduation year, disability from gaps, pregnancy, etc.) that shouldn't factor into decisions?

**5. Accountability and human oversight**
- Is there a meaningful human-in-the-loop, or is the tool making de facto final decisions?
- Clear ownership for monitoring, auditing, and responding to complaints

**6. Security**
- Resistance to adversarial manipulation (e.g., keyword-stuffing/prompt injection resumes designed to game the ranking)
- Data security for sensitive applicant PII

**7. Legal/regulatory risk**
- EEOC disparate impact liability under Title VII
- State/local AI hiring laws requiring bias audits and candidate notice (NYC Local Law 144 is the most prescriptive example)
- Multi-jurisdictional complexity if hiring across states/countries

## Most Relevant Trustworthiness Properties

Per the AI RMF's trustworthiness characteristics, prioritize (in rough order for this use case):

1. **Fair — with harmful bias managed** — the single highest-priority property given disparate impact risk
2. **Accountable and transparent** — you need documentation and explainability to defend decisions and satisfy disclosure laws
3. **Valid and reliable** — the tool must actually measure job-relevant criteria
4. **Explainable and interpretable** — both for candidates and for internal reviewers/auditors
5. **Privacy-enhanced** — minimize and protect applicant data
6. **Safe** — lower emphasis here vs. physical-safety AI systems, but still relevant to psychological/economic harm from unfair rejection
7. **Secure and resilient** — protect against gaming/manipulation and data breaches

## Specific MEASURE-Function Actions Before Deployment

1. **Conduct a bias/disparate impact audit** using standard statistical tests (e.g., four-fifths rule / adverse impact ratio analysis) across protected classes before go-live, and establish a cadence (at least annually, or per NYC LL144 — annually and before deployment) for ongoing audits by an independent auditor if required by local law.

2. **Validate against job-relevant outcomes** — run a validation study correlating tool outputs with actual on-the-job performance or interview/hiring outcomes for a pilot cohort, not just resume-keyword matching accuracy.

3. **Benchmark performance across subgroups** — measure false positive/negative rates, ranking distributions, and pass-through rates disaggregated by gender, race/ethnicity, age bracket, and disability status (where lawfully collectible, e.g., via voluntary self-ID).

4. **Test robustness to adversarial/edge-case inputs** — resumes with unconventional formatting, non-native English phrasing, employment gaps, career changes, and keyword-stuffed resumes.

5. **Establish explainability tooling** — generate feature-importance or reason codes for each ranking decision that can be reviewed by recruiters and, if needed, disclosed to candidates or regulators.

6. **Red-team the tool** — have an internal or third-party team attempt to identify failure modes, gaming techniques, and biased outcomes before launch.

7. **Set and document acceptable thresholds** — define in advance what adverse-impact ratio, error rate, or accuracy threshold would block deployment or trigger remediation (this connects MEASURE outputs to MANAGE decisions).

8. **Pilot with human oversight and shadow-mode testing** — run the tool in parallel with existing human screening for a period, comparing outcomes before fully automating any part of the pipeline.

9. **Document known limitations** — maintain a model card or system card capturing training data provenance, known weaknesses, and populations where performance hasn't been validated.

10. **Set up post-deployment monitoring** — track ranking/selection-rate metrics on an ongoing basis (not just pre-launch) since data drift and candidate-pool changes can introduce new bias over time — this feeds into MANAGE's continuous monitoring activities.

## Bottom Line

Before deployment, you should be able to answer: "Can we prove, with statistical evidence, that this tool does not produce disparate impact on protected groups, actually predicts job-relevant performance, and can be explained to a rejected candidate or regulator?" If you can't answer yes to all three, MEASURE-function work isn't done yet.
