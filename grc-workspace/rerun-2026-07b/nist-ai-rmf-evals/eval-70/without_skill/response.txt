# GOVERN Function Gap Assessment

Based on the information provided, here is a gap assessment against the NIST AI RMF GOVERN function's six categories, with maturity ratings and a prioritized remediation plan.

## Current State Summary

- Have: AI ethics statement
- Missing: formal AI risk policy, cross-functional AI team, defined risk tolerance, legal team involvement in AI deployments

## GOVERN Category Ratings

### GOVERN 1: Policies, processes, procedures, and practices are in place, transparent, and implemented effectively
**Rating: Initial / Ad Hoc (1 out of 5)**

You have an AI ethics statement, which is a positive starting signal, but ethics statements are aspirational, not operational. Without a formal AI risk policy, there's no documented process for how risk is identified, escalated, or governed day-to-day. This category also covers legal/regulatory mapping — the absence of legal involvement means you likely don't have a clear picture of your regulatory obligations (state AI laws, sector-specific rules, EU AI Act exposure if applicable).

**Gap:** No formal policy translating ethics principles into operational requirements (e.g., what risk assessments are required before deployment, what documentation must exist, what approval gates apply).

### GOVERN 2: Accountability structures are in place
**Rating: Non-Existent / Initial (1 out of 5)**

No cross-functional AI team means there's no clear ownership of AI risk decisions. It's unclear who is accountable when an AI system causes harm, who approves deployments, or who has authority to halt a rollout.

**Gap:** No designated accountable owner(s), no committee or governance body, no defined escalation path for AI risk issues.

### GOVERN 3: Workforce diversity, equity, inclusion, and accessibility processes are prioritized; and processes support human-AI teaming
**Rating: Unknown / Not Assessed (insufficient information — treat as gap until verified)**

Not enough detail was provided to rate this fully, but given the absence of a cross-functional team, it's likely that diverse perspectives (legal, security, ethics, impacted-community representation) aren't systematically incorporated into AI decisions.

**Gap:** No evidence of structured process to incorporate diverse stakeholder input or human oversight design into AI deployments.

### GOVERN 4: Organizational teams are committed to a culture that considers and communicates AI risk
**Rating: Initial (1-2 out of 5)**

An ethics statement suggests some cultural intent, but without a cross-functional team or policy, risk communication is likely informal and inconsistent. There's no indication of training, risk communication channels, or documentation practices.

**Gap:** No structured risk communication process; unclear if teams outside of whoever authored the ethics statement are even aware of AI risk expectations.

### GOVERN 5: Processes are in place for robust engagement with relevant AI actors
**Rating: Non-Existent (0-1 out of 5)**

No mention of external stakeholder engagement (customers, impacted individuals, regulators, auditors). This is a significant gap especially if any AI systems affect external parties.

**Gap:** No mechanism for gathering feedback from those affected by AI systems, no engagement with external experts or auditors.

### GOVERN 6: Policies and procedures are in place to address AI risks and benefits arising from third-party software and data and other supply chain issues
**Rating: Non-Existent / Unknown (0-1 out of 5)**

No information provided, but given the absence of a formal risk policy overall, it's reasonable to assume third-party/vendor AI risk (e.g., AI embedded in SaaS tools, vendor models) is not being systematically assessed either.

**Gap:** No vendor AI risk assessment process, no contractual requirements for third-party AI transparency or liability.

## Additional Critical Gap: Risk Tolerance
NIST AI RMF treats defining organizational risk tolerance as foundational to GOVERN (it underpins how all other categories are operationalized). Without a defined risk tolerance, you have no consistent basis for deciding what risk level is acceptable, which directly undermines every other GOVERN category and blocks meaningful MAP/MEASURE/MANAGE work downstream (you can't decide when to "accept" vs. "mitigate" a measured risk without a tolerance baseline).

## Overall GOVERN Maturity: Initial (Level 1 of 5)

You have a values-level artifact (ethics statement) but no operational governance infrastructure. This is a common starting point, but it means virtually all AI deployments today are happening without a formal risk gate.

## Prioritized Remediation Plan

### Priority 1 (0-30 days): Stop the bleeding
1. **Establish an interim AI governance committee** — even informally, pull together legal, security, data/ML, HR/compliance, and a business sponsor. This doesn't need to be perfect; it needs to exist and start meeting.
2. **Mandate legal review as a gate for any new AI deployment** — until formal policy exists, require legal sign-off before any AI system touching customer data, employment decisions, or regulated activity goes live.
3. **Inventory existing AI systems** — you likely don't have a complete list of what AI is already deployed. This is prerequisite information for everything else.

### Priority 2 (30-90 days): Build the foundation
4. **Draft and approve a formal AI risk policy** — translate the ethics statement into operational requirements: what triggers a risk assessment, what documentation is required, who approves what risk level.
5. **Define organizational risk tolerance** — work with legal, executive leadership, and risk/compliance to explicitly define acceptable risk thresholds by AI use case category (e.g., consequential decisions like hiring/credit require higher scrutiny than internal productivity tools).
6. **Formalize the cross-functional AI team** — move from informal committee to a chartered governance body with defined roles, decision rights, and meeting cadence. Include legal permanently, not ad hoc.

### Priority 3 (90-180 days): Operationalize and extend
7. **Build a third-party/vendor AI risk assessment process** — questionnaire and contractual requirements for any vendor providing AI-enabled tools or models.
8. **Establish external stakeholder engagement mechanisms** — feedback channels for individuals affected by AI decisions (e.g., an appeals process if you have any consequential-decision AI systems).
9. **Develop AI risk training** — roll out training for teams building, deploying, or using AI systems so the culture shift (GOVERN 4) has substance behind it.
10. **Document escalation and incident response procedures** — define what happens when an AI system causes harm or behaves unexpectedly, including who's notified and how quickly.

### Priority 4 (180+ days): Mature and sustain
11. **Move from ad hoc to scheduled governance reviews** — quarterly reviews of the AI inventory, risk register, and policy effectiveness.
12. **Formalize diversity/inclusion input mechanisms** (GOVERN 3) — ensure AI design and review processes incorporate diverse perspectives systematically, not just when convenient.
13. **Pursue external validation** — consider an independent audit or maturity assessment against AI RMF or a certifiable standard (e.g., ISO/IEC 42001) once foundational governance is in place.

## Key Message

The single highest-leverage fix is **getting legal into the room and defining risk tolerance** — nearly every other gap (accountability, policy, vendor risk, stakeholder engagement) becomes easier to close once you have (a) a cross-functional body with legal authority in the room and (b) an agreed definition of what risk is acceptable. Until risk tolerance is defined, GOVERN work elsewhere risks being directionless.
