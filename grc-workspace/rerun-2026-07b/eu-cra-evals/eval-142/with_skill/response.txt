## CRA Annex I Gap Assessment — Consumer IoT Router

**Scope note:** Home-use consumer routers fall under **Annex III (Class I)** of the CRA, so this product is subject to the full Annex I essential requirements (Part I security properties and Part II vulnerability handling), with a Class I conformity route (self-assessment or Notified Body, manufacturer's choice).

Assessed against the current state you described: default password "admin"; no automatic update mechanism; telnet management port open by default; no vulnerability disclosure policy; 2-year support commitment.

---

### Part I — Security Properties (Annex I, Part I)

| # | Requirement | Current State | Status | Risk |
|---|---|---|---|---|
| 1 | No known exploitable vulnerabilities at market placement | Not assessed here, but default creds + open telnet are themselves exploitable-by-design issues | **Gap** | High |
| 2 | Secure by default — minimal attack surface, unnecessary functions/ports disabled | Telnet management port **open by default** | **Gap** | Critical |
| 2 | Secure default settings — no easily guessable/common factory passwords | Default password is literally **"admin"** | **Gap** | Critical |
| 2 | User can reset to a secure factory state | Not stated — verify | Unknown | Medium |
| 3 | Protection against unauthorised access (authentication, least privilege, MFA where feasible) | Single shared static default password; telnet has no encryption or strong auth by nature | **Gap** | Critical |
| 4 | Confidentiality — encryption at rest/in transit | Not stated — telnet itself transmits credentials/traffic in **cleartext**, which is a direct violation for the management channel | **Gap** | High |
| 5 | Integrity — signed firmware/software updates, protection against tampering | No automatic update mechanism means no established update integrity pipeline at all | **Gap** | High |
| 6 | Data minimisation / privacy by design | Not assessed — needs separate review | Unknown | Low/Medium |
| 7 | Availability — resilience against DoS | Not assessed | Unknown | Medium |
| 8 | Limited negative impact on other devices/networks | An unpatched router with open telnet and default creds is a classic botnet recruitment vector (e.g., Mirai-style) — this is a direct compliance risk | **Gap** | Critical |
| 9 | Exploit mitigation mechanisms (ASLR, stack canaries, etc.) | Not stated — verify firmware build flags | Unknown | Medium |
| 10 | Security information transparency to users; published contact for reporting | No VDP means no published vulnerability contact — fails this requirement too | **Gap** | High |

### Part II — Vulnerability Handling (Annex I, Part II)

| # | Requirement | Current State | Status | Risk |
|---|---|---|---|---|
| 1 | Vulnerability identification — inventory of components, CVE monitoring | Not described — presumed absent given no VDP/no update mechanism | **Gap** | High |
| 2 | Remediation without undue delay, free security updates | No automatic update mechanism = no reliable remediation path | **Gap** | Critical |
| 3 | Coordinated Vulnerability Disclosure (CVD/VDP) policy, published, with named contact | Explicitly stated: **none exists** | **Gap** | Critical |
| 4 | Published point of contact for vulnerability reports | None (follows from #3) | **Gap** | Critical |
| 5 | Information sharing with CERT/CSIRT network | No process in place | **Gap** | High |
| 6 | SBOM available on request (minimum: top-level dependencies) | Not mentioned — assume absent; must be built | **Gap** | High |
| 7 | Free-of-charge security updates throughout support period, delivered via secure/signed mechanism | No automatic update mechanism at all | **Gap** | Critical |
| 8 | 24-hour/72-hour ENISA + CSIRT reporting for actively exploited vulnerabilities | No pipeline described | **Gap** | Critical (mandatory from 11 Sept 2026) |
| 9 | Prompt user notification of security issues/remediation | No update mechanism = no notification channel | **Gap** | High |

### Support Period

- **Requirement:** minimum 5 years (or expected product lifetime if shorter), clearly communicated to users.
- **Current state:** 2-year support commitment.
- **Status: Gap.** Unless you can substantiate that the router's expected product lifetime is genuinely under 5 years (difficult to argue for a router — typical expected lifetime is 5–7+ years), a 2-year commitment falls short of the CRA minimum and must be extended, along with a clear pre-purchase disclosure of the support window and an end-of-support notice process (≥1 year advance notice, final cumulative security update).

---

### Consolidated Gap Summary

| Risk Rating | Count | Items |
|---|---|---|
| **Critical** | 6 | Default password "admin"; telnet open by default; no auth/access control beyond default password; no automatic update mechanism; no VDP/no published contact; no ENISA/CSIRT reporting pipeline |
| **High** | 6 | Cleartext management channel (telnet); no signed-update integrity pipeline; botnet/network-impact risk; no vulnerability identification process; no CERT/CSIRT info sharing; no SBOM; no user notification channel |
| **Medium** | 3 | Factory reset capability unverified; DoS resilience unverified; exploit mitigations unverified |
| **Support period gap** | 1 | 2 years vs. 5-year minimum |

### Recommended Remediation Roadmap

**Immediate / pre-market blockers (must fix before any new units can lawfully be placed on the EU market post-transition):**
1. Remove "admin" as a shipped default password. Require unique per-device credentials or forced first-boot password setup.
2. Disable telnet by default; if remote/local management is needed, replace with an encrypted, authenticated alternative (SSH with key-based auth, or HTTPS-based admin UI with MFA where feasible).
3. Build and ship an **automatic, signed update mechanism** that cannot be disabled by the user and separates security patches from feature updates.
4. Publish a **Coordinated Vulnerability Disclosure (CVD/VDP) policy** with a named contact (security.txt, email alias, or portal) and a defined acknowledgement/response SLA.
5. Extend the **support commitment to a minimum of 5 years** from date of market placement, and disclose it clearly in product documentation/packaging before purchase.

**Near-term (needed to operate compliantly, and specifically ahead of the 11 September 2026 reporting deadline):**
6. Stand up an internal vulnerability identification process (component inventory, CVE monitoring, scanning in the build pipeline).
7. Build the **24-hour/72-hour/14-day ENISA and national CSIRT reporting pipeline** for actively exploited vulnerabilities — this obligation is legally binding from **11 September 2026**, roughly 10 weeks from today.
8. Generate a machine-readable **SBOM** (SPDX or CycloneDX) covering at least top-level dependencies, and integrate it into your release/CI process.

**Structural (ahead of full application on 11 December 2027):**
9. Complete a cybersecurity risk assessment and threat model for the router.
10. Assemble Annex VII technical documentation (architecture diagrams, risk assessment, test evidence, SBOM, vulnerability handling policy).
11. Complete Module A self-assessment (or opt for Notified Body review) and draw up the EU Declaration of Conformity; affix CE marking; register the product in the EU database (mandatory for Class I products).

### Bottom Line

This product currently fails the majority of Annex I Part I and Part II requirements outright — default credentials, an open unencrypted management protocol, and the absence of any update or disclosure mechanism are exactly the combination of issues CRA Annex I was designed to eliminate. None of these are edge-case interpretive gaps; they are core, unambiguous non-conformities that would block CE marking today. Given the router's Class I status and the September 2026 reporting deadline, I'd prioritize the update mechanism, VDP, and default-credential/telnet fixes immediately, and treat the 5-year support extension as a parallel-track commercial and documentation change.
