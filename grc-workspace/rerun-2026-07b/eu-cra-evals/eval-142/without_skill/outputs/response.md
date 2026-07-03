# CRA Annex I Gap Assessment — Consumer IoT Router

**Scope:** Consumer smart-home IoT router. Current state: default password "admin"; no automatic update mechanism; telnet management port open by default; no vulnerability disclosure policy; 2-year support commitment.

Annex I of the CRA has two parts: **Part I** (security requirements relating to the properties of the product) and **Part II** (vulnerability handling requirements). Below is a gap-by-gap assessment.

---

## Part I — Product Security Properties

| # | Annex I Requirement (paraphrased) | Current State | Gap | Severity |
|---|---|---|---|---|
| 1 | Products shall be designed, developed, and produced to ensure an appropriate level of cybersecurity based on risk | No evidence of a documented risk assessment | No formal risk assessment process | High |
| 2 | Products shall be delivered **without any known exploitable vulnerabilities** | Unknown — no stated vulnerability scanning | Cannot confirm; needs assessment before CE marking | High |
| 3 | Products shall be delivered with a **secure by default configuration**, including the possibility to reset to original state | **Default password "admin"** violates this directly | Critical gap — hard-coded/default weak credentials are explicitly called out in Annex I as unacceptable | Critical |
| 4 | Ensure protection from unauthorized access via appropriate control mechanisms (authentication, identity/access management) | Default admin password + **telnet open by default** (unencrypted, weak-auth-friendly protocol) | Two compounding failures: weak default credentials AND an insecure, legacy management protocol exposed by default | Critical |
| 5 | Protect confidentiality of stored, transmitted, or processed data (encryption at rest/in transit) | Telnet is unencrypted by design; any credentials or session data sent over telnet are exposed in cleartext | Direct violation of confidentiality requirement for the management interface | Critical |
| 6 | Protect integrity of data, commands, programs, configuration against unauthorized manipulation | Telnet management + weak auth = high risk of unauthorized configuration changes | Gap tied directly to #4/#5 | High |
| 7 | Process only data that is adequate, relevant, and limited (minimization) | Not enough information provided to assess | Needs data flow review | Unknown |
| 8 | Protect availability of essential functions, including resilience against DoS | Not assessed | Needs testing | Unknown |
| 9 | Minimize the negative impact of products/services on availability of other services | Not assessed | Needs testing | Unknown |
| 10 | **Minimize attack surface**, including external interfaces | Telnet enabled by default is an unnecessary, high-risk, legacy interface — direct violation of "minimize attack surface" | Should be disabled by default and replaced with SSH/HTTPS-based management, or not exposed at all without explicit user opt-in | Critical |
| 11 | Reduce impact of an incident using exploitation-mitigation mechanisms (e.g., safe fallback, rollback) | No automatic update mechanism means no rollback/patch delivery capability | Gap — cannot remediate incidents in the field at scale | High |
| 12 | Provide security-related information via logging/monitoring of internal activity (where appropriate, with an opt-out) | Not stated | Needs implementation review | Unknown |
| 13 | Provide the possibility to **remediate vulnerabilities through security updates**, including automatic updates where appropriate, with user notification and opt-out, and a mechanism to notify users when a product reaches end of support | **No automatic update mechanism at all** | Critical, explicit gap — this is one of the most heavily weighted requirements in Annex I Part I | Critical |

### Part I Summary
- **Critical failures:** default weak password, telnet exposed by default, no encrypted management channel, no automatic update mechanism, excessive attack surface.
- These are not edge-case gaps — hard-coded default credentials and lack of update capability are the two failure modes the CRA was explicitly designed to eliminate (directly echoing lessons from Mirai-style botnets exploiting default-credential IoT devices).
- **This product cannot be placed on the EU market in its current state.** It would fail conformity assessment under Module A self-assessment and would very likely fail a notified body review as well.

---

## Part II — Vulnerability Handling Requirements

| # | Annex I Part II Requirement | Current State | Gap | Severity |
|---|---|---|---|---|
| 1 | Identify and document vulnerabilities/components (implies SBOM) | Not stated | Assume gap — needs SBOM programme | High |
| 2 | Address and remediate vulnerabilities without delay, including through security updates | No auto-update mechanism | Same critical gap as above | Critical |
| 3 | Apply effective and regular testing/review of product security (e.g., fuzzing, code review) | Not stated | Needs a defined secure development/testing programme | Unknown/likely gap |
| 4 | Publicly disclose information about fixed vulnerabilities, including description, affected products, impact, severity, and remediation guidance | No vulnerability disclosure policy exists | Direct, explicit gap | Critical |
| 5 | Put in place and enforce a **coordinated vulnerability disclosure policy**, including a way for security researchers to report | **"No vulnerability disclosure policy" stated explicitly** | Direct, explicit gap — this is a named Annex I Part II requirement | Critical |
| 6 | Provide a **contact address** for vulnerability reporting | Not stated, but tied to lack of a disclosure policy | Gap | Critical |
| 7 | Provide mechanisms to securely distribute updates without delay, free of charge, with advisory information (severity, description, remediation) | No automatic update mechanism | Critical, repeated gap | Critical |
| 8 | Ensure that, where security patches are available, they are disseminated without undue delay | Same as above | Critical | Critical |
| 9 | (Where applicable) support period must reflect the expected product lifetime | **2-year support commitment stated** | The CRA does not fix a specific minimum number of years, but requires the support period to reflect the expected use/lifetime of the product, and in general guidance/expectations point to a **minimum baseline of 5 years unless a shorter period is objectively justified** by the nature of the product | Likely gap — 2 years is short for a home networking device with a typical expected life of 5+ years; you will need to document objective justification if you keep this, or extend it |

### Part II Summary
- **No vulnerability disclosure policy** is an explicit, named non-conformity.
- **No automatic update mechanism** blocks your ability to meet nearly every remediation-related obligation in Part II.
- **2-year support period** is a likely-insufficient justification gap — routers are typically expected to remain in service well beyond 2 years; you should document the rationale or extend the commitment.

---

## Prioritized Remediation Roadmap

**Immediate / Critical (must-fix before any CE marking activity):**
1. Eliminate the default "admin" password — require unique per-device credentials or forced setup of a strong password on first use (satisfies Annex I Part I #3, #4).
2. Disable telnet by default; if remote/local management is needed, use an encrypted alternative (SSH, HTTPS with TLS) (satisfies #4, #5, #10).
3. Build an automatic update mechanism with signed firmware, user notification, and opt-out where appropriate (satisfies Part I #11, #13, and nearly all of Part II).
4. Publish a coordinated vulnerability disclosure policy (CVD policy) with a dedicated reporting contact/email and a defined triage SLA (satisfies Part II #4, #5, #6).

**High priority (needed for documentation and ongoing conformance):**
5. Conduct and document a formal product cybersecurity risk assessment (Part I #1, #2).
6. Build/acquire an SBOM for the firmware and maintain it as vulnerabilities are tracked (Part II #1).
7. Establish a security testing programme (static/dynamic analysis, fuzzing of network-facing services) (Part II #3).
8. Re-evaluate and likely extend the support period beyond 2 years, or formally document why 2 years is appropriate given the product's expected lifetime (Part II #9).

**Medium priority (verify/complete):**
9. Confirm logging/monitoring capabilities and data minimization practices (Part I #7, #12).
10. Perform resilience/availability testing (DoS resistance) (Part I #8, #9).

## Bottom Line

The product in its current state would fail a CRA conformity assessment on at least five explicit, high-severity grounds: default weak credentials, an unencrypted legacy management protocol open by default, absence of an automatic update capability, absence of a vulnerability disclosure policy, and a support period that likely does not reflect the expected product lifetime. These must be remediated before the product can be placed on the EU market under the CRA (main obligations apply from 11 December 2027), and the vulnerability-handling gaps (disclosure policy, update mechanism) should be treated as urgent given the CRA's reporting obligations already apply from 11 September 2026.
