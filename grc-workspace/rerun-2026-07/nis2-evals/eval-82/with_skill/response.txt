## Short answer

Probably **not directly** in scope as a NIS2 "essential" or "important" entity in your own right — but this needs a real sector check, and even if you're out of scope, your customer's request is a strong signal that you'll be pulled in **indirectly via their supply chain obligations (Art. 21(2)(d))**. Don't dismiss this as "not our problem."

---

## 1. Are you directly subject to NIS2?

NIS2 scope is a two-part test: **(a) sector** (Annex I or Annex II) **and (b) size** (Art. 3).

### Size threshold — you clear it
Medium+ entities (≥50 employees **OR** ≥€10M annual turnover) are automatically in scope if their sector qualifies. At 75 employees and €15M revenue, you exceed both thresholds. Size is not what would exclude you — sector is the question.

### Sector — this is the determining question
"B2B cloud-based HR software" is a SaaS application, not cloud infrastructure. That distinction matters a lot under NIS2:

- **Annex I "Digital infrastructure"** and the Implementing Regulation's "relevant entity" list (cloud computing service providers, data centre providers, CDN, DNS, MSP, MSSP, online marketplaces/search/social platforms, trust services) are aimed at providers of the **underlying infrastructure and platform layer** — IaaS/PaaS cloud providers, data centres, DNS, CDNs, managed infrastructure/security services. A vertical SaaS application (HR software) sitting on top of someone else's cloud (e.g., AWS/Azure) does **not** itself meet the "cloud computing service provider" definition just because it's delivered "as a service" over the internet.
- **Annex I "ICT service management (B2B)"** covers managed service providers and managed security service providers — i.e., companies that manage *other organisations'* IT/security infrastructure, networks, or systems on their behalf. Providing an HR SaaS product is not the same as managing a customer's IT environment.
- **Annex II "Digital providers"** (in the original Annex II text) is narrower than it sounds — it corresponds to the old NIS1 "digital service providers" category (online marketplaces, online search engines, social networking platforms), not general B2B software vendors.
- HR software doesn't fall into any of the other Annex I/II sectors (energy, transport, banking, financial infrastructure, health, water, public administration, space, postal, waste, chemicals, food, manufacturing of specific goods, research).

**Conclusion:** Based on the facts given, a generic B2B HR SaaS platform does not fit the Annex I/II sector definitions and is very likely **out of direct scope** of NIS2 as currently drafted — regardless of size. This is a preliminary read; two things could change it:

1. **Member State transposition variance.** Some Member States have gold-plated the Annex I/II lists or added sector-specific criticality criteria in national transposition law. If you operate in (or have significant customers/infrastructure in) a specific EU Member State, that state's transposing legislation is the authoritative source — the Directive is a floor, not a ceiling.
2. **What your infrastructure actually is.** If you also directly operate the underlying cloud/hosting infrastructure yourself (rather than deploying on AWS/Azure/GCP), or if you provide any managed IT/security service alongside the HR product, re-run this analysis — you could cross into "cloud computing service provider" or "MSP" territory.

**Recommendation:** confirm with counsel in the specific Member State(s) where you're established/operating, since transposition details vary and only national law is legally binding.

---

## 2. Why your customer is asking anyway — supply chain security (Art. 21(2)(d))

Even if you are out of direct scope, your customer almost certainly **is** in scope (or believes they might be), and NIS2 Art. 21(2)(d) requires in-scope entities to manage **supply chain security**, including their relationships with suppliers and service providers like you. In practice this means:

- Your customer's own Art. 21 compliance program requires them to assess and manage risk from vendors who touch their data/systems — and HR software touches sensitive personal and organisational data.
- They will likely push NIS2-flavored requirements down contractually: security questionnaires, right-to-audit clauses, incident notification SLAs (often faster than what NIS2 itself requires, e.g., 24–72 hours to *them*, not just to a CSIRT), minimum security baselines (MFA, encryption, access control), and possibly a requirement to demonstrate ISO 27001 or SOC 2 as evidence.
- This is the **most common way non-obligated SaaS vendors experience "NIS2 compliance" in practice** — not as a direct regulatory target, but as a flow-down contractual requirement from essential/important entity customers doing Art. 22 coordinated/Art. 21(2)(d) supply chain risk assessments.

So: treat this customer ask as a **procurement/contractual security requirement**, not a direct regulatory filing obligation — but the underlying control set you'd stand up is the same either way.

---

## 3. What to actually do — Art. 21's 10 measures, applied to you

Whether you're directly obligated or complying voluntarily to satisfy customer contracts, here's the practical build-out mapped to Art. 21(2), sized for a 75-person SaaS company:

| # | Measure | What it looks like at your scale |
|---|---|---|
| 1 | Risk analysis & InfoSec policy | Adopt a lightweight risk methodology (ISO 27005-aligned is fine); maintain an asset inventory of your SaaS systems, databases, and customer data stores; get management sign-off |
| 2 | Incident handling | Written IR plan with detection → response → recovery steps; define what counts as a "significant incident" for reporting to customers contractually; tabletop test annually |
| 3 | Business continuity / backup / DR | RTO/RPO defined for the HR platform; automated encrypted backups with quarterly restore tests; DR runbook |
| 4 | **Supply chain security** | This is the one your customer cares about most. Inventory your own critical vendors (cloud host, payroll integrations, auth providers); push security requirements into your own vendor contracts; be ready to answer your customers' security questionnaires |
| 5 | Secure SDLC | Code review, SAST/DAST, patching SLAs (critical ≤7 days), vulnerability disclosure policy |
| 6 | Effectiveness assessment | Annual internal review or third-party pen test; track basic KPIs (patch compliance, MTTD) |
| 7 | Cyber hygiene & training | Annual security awareness training for all staff; phishing simulations |
| 8 | Cryptography | Encrypt HR/PII data at rest (AES-256) and in transit (TLS 1.2+); key management process |
| 9 | HR security, access control, asset mgmt | RBAC with quarterly access reviews, joiners/movers/leavers process with same-day revocation for a company handling customers' employee PII |
| 10 | MFA & secure comms | MFA on all admin/privileged accounts and customer-facing login where feasible; encrypted internal comms for incident coordination |

**Priority order given your situation:**
1. Supply chain security (#4) and access control/MFA (#9–10) — these are what customers' security questionnaires and Art. 21(2)(d) flow-downs will probe first.
2. Incident handling (#2) with a customer-facing notification SLA — customers will want contractual breach/incident notice, separate from any CSIRT reporting.
3. Cryptography (#8) and secure SDLC (#5) — expected baseline for any vendor holding employee PII.
4. The remainder (governance documentation, training, effectiveness assessment) rounds out a credible program and maps well to ISO 27001/SOC 2 if you pursue either as evidence for customers.

**A note on framing:** if you already have or are pursuing **SOC 2** or **ISO 27001**, most of this control set overlaps significantly — ISO 27001:2022 Annex A maps closely to Art. 21, and either certification is strong evidence to hand your customer even though it doesn't constitute formal "NIS2 compliance" (since you're not a directly regulated entity).

---

## Bottom line

- **Direct NIS2 obligation:** unlikely, based on sector — B2B HR SaaS doesn't fit Annex I/II or the Implementing Regulation's "relevant entity" list (cloud/MSP/MSSP/etc.), though you clear the size threshold. Verify against the specific Member State transposition your customer/you operate under.
- **Practical exposure:** high — your customer is very likely pushing Art. 21(2)(d) supply-chain-security requirements down to you contractually, which is why they raised it.
- **What to do:** build the Art. 21 control set proportionate to a 75-person SaaS vendor (table above), prioritizing supply chain security, access control/MFA, and incident notification terms, and be ready to respond to customer security questionnaires and contract riders referencing NIS2.
