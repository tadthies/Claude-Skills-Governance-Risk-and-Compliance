# GOVERN Function Gap Assessment

Based on what you've described — an AI ethics statement but no formal AI risk policy, no cross-functional AI team, no defined risk tolerance, and legal not involved in AI deployments — you're at an early stage across nearly all of GOVERN's six categories. This is a common and fixable starting point. Below is a category-by-category rating with gap notes, followed by a prioritized remediation roadmap.

## GOVERN Category Ratings

| Category | Status | Gap Notes |
|----------|--------|-----------|
| **GOVERN 1** — Policies, processes, procedures in place | 🔴 Not Started | You have an AI ethics *statement* but not a formal AI risk management *policy*. An ethics statement expresses values; it doesn't establish risk tolerance, ERM integration, or a review cadence. No evidence of AI risk being integrated into enterprise risk management (GOVERN 1.1) or a periodic policy review process (GOVERN 1.5). |
| **GOVERN 2** — Accountability structures | 🔴 Not Started | No indication of a designated senior official accountable for AI risk outcomes (GOVERN 2.2). Without a named accountable owner, GOVERN 5 (risk tolerance) and MANAGE 1.3 (residual risk acceptance) have no one authorized to approve decisions. |
| **GOVERN 3** — Roles and responsibilities | 🔴 Not Started | No AI roles register described. Unclear who is responsible for AI risk management at each lifecycle stage (design, development, deployment, monitoring) or for third-party/vendor AI models. |
| **GOVERN 4** — Cross-functional team collaboration | 🔴 Not Started | Explicitly stated: no cross-functional AI team. Legal is not involved in deployments — this is a critical gap since GOVERN 4.1 requires AI/ML, legal, privacy, security, HR, and ethics functions to collaborate on AI risk. |
| **GOVERN 5** — Organizational risk tolerance | 🔴 Not Started | Explicitly stated: no defined risk tolerance for AI. Without this, there's no way to make go/no-go deployment decisions (GOVERN 5.3) or set bias/accuracy thresholds for testing. |
| **GOVERN 6** — Alignment with laws, regulations, principles | 🟡 Partial | The AI ethics statement suggests some engagement with ethical principles (GOVERN 6.2), but legal's absence from AI deployments (GOVERN 6.1) means legal/regulatory tracking is not integrated into the process. No evidence of a regulatory register or proactive engagement (GOVERN 6.3). |

**Overall GOVERN maturity: Tier 1 (Partial)** on the AI RMF implementation tier scale — ad hoc practices, limited formal awareness, reactive rather than proactive posture. The ethics statement is a values artifact, not an operationalized risk management structure; this is the classic "GOVERN complete on paper but not operationalized" pattern in its earliest form — except here, GOVERN isn't even complete on paper yet, only ethics is.

## Prioritized Remediation Roadmap

### Quick Wins (0–3 months)

1. **Appoint an accountable AI Risk Owner** (GOVERN 2.2) — even an interim assignment (e.g., CISO, Chief Risk Officer, or a newly named AI governance lead) unblocks every other GOVERN activity. This is the single highest-leverage action.
2. **Add legal/compliance to any AI deployment decision immediately** (GOVERN 6.1) — this doesn't require a fully built program; simply mandate legal sign-off before any new AI system goes live, effective now, as an interim control.
3. **Draft a one-page AI risk tolerance statement** (GOVERN 5.1) — distinguish low-stakes AI (e.g., internal productivity tools) from high-stakes AI (systems affecting individuals' legal rights, employment, credit, health, safety). This doesn't need to be perfect; it needs to exist so GOVERN 5.3 go/no-go decisions have a reference point.
4. **Convert the AI ethics statement into policy language** (GOVERN 1.2) — map each ethical principle to a concrete, testable organizational practice (e.g., "we value fairness" becomes "disaggregated bias testing required before deployment of any system affecting individuals").

### Medium Term (3–6 months)

5. **Publish a formal AI Risk Management Policy** (GOVERN 1.1/1.3/1.6) signed by senior leadership — integrate AI risk into existing ERM processes rather than creating a parallel program; define risk appetite statements (acceptable bias thresholds, accuracy floors) explicitly.
6. **Stand up a cross-functional AI Risk Working Group** (GOVERN 4.1) — mandatory members: AI/engineering, legal, privacy, security, HR, and ethics. Meet quarterly at minimum; more frequently while the program is new. This directly closes the "legal not involved" gap on an ongoing basis rather than case-by-case.
7. **Build an AI roles register** (GOVERN 3.1/3.2) — map every lifecycle stage (design, development, testing, deployment, monitoring, decommission) to a responsible team or individual, including responsibilities for third-party/vendor AI models.
8. **Define an escalation path** (GOVERN 4.3) — from development/deployment teams up to the AI Risk Owner and executive leadership, so risk concerns surface before deployment rather than after an incident.

### Long Term (6–12 months)

9. **Formalize the policy review cadence** (GOVERN 1.5, 1.7) — minimum annual review, with a defined trigger for interim review (new regulation, major incident, new high-risk system category).
10. **Build a regulatory register** (GOVERN 6.1/6.3) — track EU AI Act, sector-specific rules, and emerging state AI laws relevant to your systems; assign legal/compliance ownership for keeping it current.
11. **Move from Tier 1 (Partial) to Tier 2/3** (Risk Informed → Repeatable) — by this point, policies should be consistently applied and reviewed, not just approved on paper. Validate this by checking whether MAP/MEASURE/MANAGE activity on your actual deployed AI systems reflects the GOVERN policies — if not, you've re-created the "complete on paper, not operationalized" gap pattern and need to close it.
12. **Consider external validation** — a third-party review of your AI governance program once the above is in place, both to pressure-test the program and to produce evidence for customers, auditors, or regulators.

## Critical Path Note

GOVERN gaps typically block progress in MAP, MEASURE, and MANAGE — without an accountable owner (GOVERN 2), a defined risk tolerance (GOVERN 5), and legal involvement (GOVERN 6), you cannot meaningfully prioritize risks in MAP 4, set measurement thresholds in MEASURE 1, or get authoritative sign-off on residual risk in MANAGE 1.3. **Do not proceed to building out MAP/MEASURE/MANAGE processes for specific AI systems until at minimum the Quick Wins above are complete** — otherwise you risk producing technical risk assessments with no one authorized to act on the findings.

---
*This is general compliance guidance, not legal advice. Verify current requirements against the official NIST AI 100-1 publication and consult qualified counsel for decisions specific to your organization's regulatory exposure.*
