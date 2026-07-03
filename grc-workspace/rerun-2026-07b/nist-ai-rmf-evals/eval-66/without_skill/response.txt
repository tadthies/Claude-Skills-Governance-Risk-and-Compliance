# NIST AI RMF: The Four Core Functions

The NIST AI Risk Management Framework (AI RMF 1.0), released in January 2023, organizes AI risk management around four core functions: **GOVERN, MAP, MEASURE, and MANAGE**. Together they form a continuous, iterative lifecycle rather than a one-time checklist.

## The Four Functions

### GOVERN
GOVERN is the foundation that cultivates and permeates a culture of risk management across the organization. It covers:
- Establishing policies, processes, procedures, and practices for AI risk management
- Defining roles, responsibilities, and accountability structures (including executive sponsorship)
- Setting organizational risk tolerance and risk appetite
- Legal and regulatory compliance mapping
- Workforce diversity and training on AI risks
- Third-party/supply chain risk management for AI

GOVERN is unique among the four functions because it's not sequential — it operates across and underneath the other three, informing and being informed by MAP, MEASURE, and MANAGE activities continuously.

### MAP
MAP establishes the context to frame risks related to an AI system. Activities include:
- Understanding intended purpose, use cases, and reasonably foreseeable misuse
- Identifying stakeholders and their interests (impacted individuals, operators, deployers)
- Categorizing the AI system (e.g., is it a "high-risk" application affecting rights, safety, or access to opportunities?)
- Mapping the AI system's capabilities, data, and third-party components
- Documenting benefits and costs across the system lifecycle

MAP essentially answers: "What is this system, who does it affect, and what could go wrong?" It sets up the context that MEASURE and MANAGE depend on.

### MEASURE
MEASURE employs quantitative, qualitative, or mixed-method tools and techniques to analyze, assess, benchmark, and monitor AI risk and related impacts. It includes:
- Testing for trustworthiness characteristics: validity/reliability, safety, security/resilience, accountability/transparency, explainability/interpretability, privacy, and fairness (bias management)
- Tracking metrics over time, including post-deployment monitoring
- Independent/third-party evaluation and red-teaming
- Documenting known limitations, uncertainty, and error rates

MEASURE turns the risks identified in MAP into evidence — data you can actually act on.

### MANAGE
MANAGE allocates risk resources to mapped and measured risks on a regular basis and as defined by GOVERN. It involves:
- Prioritizing risks based on MAP and MEASURE outputs
- Deciding on risk response: mitigate, transfer, avoid, or accept
- Implementing incident response and recovery plans for AI-related incidents
- Ongoing monitoring and communication with affected stakeholders
- Documenting residual risk and decisions for accountability

## How They Relate

Think of it as: **GOVERN wraps around everything** (culture, accountability, policy), while **MAP → MEASURE → MANAGE** form a cycle that typically flows in that order for a given AI system or use case, but loops back continuously as systems change, new risks emerge, or context shifts. A system might cycle through MAP-MEASURE-MANAGE multiple times across its lifecycle (design, development, deployment, monitoring, decommissioning).

NIST also publishes a companion **AI RMF Playbook** with suggested actions for each function/category, and a **Generative AI Profile (NIST AI 600-1)** that applies the four functions specifically to generative AI risks.

## What to Implement First

For an organization just starting out, **start with GOVERN**, specifically:

1. **Establish executive sponsorship and accountability** — designate who owns AI risk (often a cross-functional AI governance committee involving legal, security, data science, and business units).
2. **Define your organization's AI risk tolerance** — what risk levels are acceptable given your industry, regulatory exposure, and use cases?
3. **Create an AI inventory/use-case register** — you can't manage what you don't know exists. This bridges GOVERN into MAP.
4. **Draft initial AI policies** — acceptable use, vendor/third-party AI review requirements, and escalation procedures.

Once GOVERN foundations exist, apply **MAP** to your highest-risk or highest-visibility AI use case first (e.g., anything touching hiring, credit, healthcare, or other consequential decisions), then move into MEASURE and MANAGE for that use case as a pilot before scaling the process organization-wide.

**Practical sequencing tip:** Don't wait for GOVERN to be "perfect" before starting MAP on a pilot system — in practice, organizations iterate GOVERN policies based on lessons learned from mapping and measuring real systems. Start GOVERN foundational work and a MAP pilot in parallel.
