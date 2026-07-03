# NIS2 Applicability — B2B Cloud HR SaaS (75 employees, €15M revenue)

## Short answer
Yes, you are very likely directly subject to NIS2 — not because a customer told you so, but because B2B cloud-hosted software typically qualifies as a **cloud computing service** under Annex I digital infrastructure, and you clear the size threshold. Your customer's compliance obligations do not create your NIS2 obligation; your own service model does.

## Step-by-step analysis

### Step 1 — Sector scope (Annex I)
Don't classify based on the "HR software" label — analyse the actual service model. NIS2 Art. 6(30) defines a **cloud computing service** as one enabling on-demand administration and broad remote access to a scalable and elastic pool of shareable computing resources. A B2B SaaS platform that is:
- multi-tenant or elastically provisioned,
- remotely accessed on demand,
- centrally administered by you rather than deployed on customer infrastructure,

...generally meets this definition and falls under **Annex I, digital infrastructure — cloud computing service provider**, regardless of the "HR" vertical label.

**Action item:** confirm your architecture matches this definition (elastic/scalable resource pooling, on-demand self-service, broad network access). If yes, you are Annex I. If your product is genuinely single-tenant, fixed-capacity hosted software with no on-demand elasticity, the analysis would differ — but most modern B2B SaaS platforms meet the cloud computing service definition.

### Step 2 — Size threshold (Art. 2(1))
In scope if medium-sized or larger: ≥50 employees, OR turnover and balance sheet both above €10M.

- Your company: 75 employees, €15M revenue → exceeds the medium-sized threshold on both employee count and revenue.
- **Conclusion: in scope on size grounds**, independent of what any customer says.

Note also: certain digital-infrastructure sub-categories (qualified trust service providers, TLD registries, DNS providers) are in scope **regardless of size** — this doesn't change your outcome since you already clear the threshold, but it's worth knowing this exists as a category.

### Step 3 — Essential vs. Important Entity (Art. 3)
- **Essential Entity (EE):** requires exceeding the large-enterprise ceiling — ≥250 employees, or turnover >€50M and balance sheet >€43M — plus a few automatic categories (qualified trust service providers, TLD/DNS providers, public electronic comms networks, CER-designated entities). You meet none of the automatic categories and don't clear the large-enterprise ceiling (75 employees, €15M revenue).
- **Important Entity (IE):** everything else in scope — this is your default classification. Medium-sized Annex I entities (like cloud service providers below the EE ceiling) land here unless a Member State designates you essential.

**Conclusion: Important Entity (IE)**, subject to reactive (ex-post) supervision rather than proactive audits, and the lower fine ceiling.

### Step 4 — Jurisdiction and registration
- **Jurisdiction (Art. 26):** cloud, data centre, CDN, MSP/MSSP, DNS, TLD, and online marketplace/search/social entities are governed by the Member State of their **main establishment** in the EU — not necessarily each customer's country. If your main EU establishment is in one Member State, that state's competent authority and CSIRT govern you.
- If you are **not established in the EU** but offer cloud services into the EU, you must designate an **EU representative** (Art. 26(3)).
- **Registration (Art. 27):** as a digital-infrastructure-type entity, you must submit identifying details (name, sector, address, IP ranges, contact) to your national authority for onward submission to ENISA's registry. This is a mandatory, near-term action item.

## What you need to do to comply with Art. 21

Art. 21(2) requires 10 categories of "appropriate and proportionate" technical, operational, and organisational measures. Proportionality is judged against your size, risk exposure, and the severity of potential incidents — as a 75-person company you are not expected to match a hyperscaler's control depth, but the measures below still apply substantively:

| # | Measure | What this means for a B2B HR SaaS provider |
|---|---|---|
| a | Risk analysis & InfoSec policies | Formal risk methodology (ISO 27005/NIST RMF), asset inventory of production systems, management-approved InfoSec policy |
| b | Incident handling | Written IR plan with detection→containment→recovery steps; must support the 24h/72h/1-month reporting clock (below) |
| c | Business continuity | Backup/DR for the HR data you process (this is sensitive employee PII — treat RTO/RPO seriously); tested restores; crisis management roles |
| d | Supply chain security | Register of your own critical vendors (cloud hosting provider, payroll integrations, auth providers); contractual security/incident-notification clauses; track EU coordinated risk assessments (Art. 22) relevant to your supply chain |
| e | Secure acquisition/development | Secure SDLC, vulnerability management with patch SLAs, coordinated vulnerability disclosure channel |
| f | Effectiveness assessment | Internal audits, pentests, metrics reported to leadership |
| g | Cyber hygiene & training | Company-wide security awareness training, phishing simulations, extended to your management body |
| h | Cryptography | Encryption at rest and in transit for HR/employee data (this is precisely the kind of sensitive personal data cryptography measures are meant to protect) |
| i | HR security, access control, asset management | Least-privilege/RBAC for your own staff accessing customer HR data, joiner/mover/leaver process, asset inventory |
| j | MFA & secured comms | **MFA is explicitly required** — enforce it on customer-facing admin consoles, your internal privileged access, and cloud infrastructure management; secured emergency communications channel if primary systems are compromised |

**Additional binding technical layer:** because you likely qualify as a cloud computing service provider, **Commission Implementing Regulation (EU) 2024/2690** applies directly to you. It decomposes the 10 Art. 21(2) measures into 13 detailed Annex sections with audit-level sub-requirements, and it sets quantitative "significant incident" thresholds (baseline: direct financial loss above €500,000 or 5% of annual turnover, whichever is lower) that you must use instead of general judgment when deciding whether an incident is reportable. Review the technical sub-requirements before your gap assessment — this is more prescriptive than the general Art. 21(2) text and is the actual audit standard your national authority will apply.

### Governance (Art. 20) — don't skip this
Your management body (founders/leadership team) must formally **approve** the Art. 21 risk-management measures and **oversee** their implementation, and must undergo (and offer staff) cybersecurity training. This creates **personal liability exposure** for leadership under national law if obligations are breached — board/leadership approval minutes and training records are the evidence an auditor will ask for first.

### Incident reporting readiness (Art. 23)
Build the reporting workflow now, before an incident forces you to improvise: 24-hour early warning, 72-hour notification with initial severity assessment, final report within 1 month, all to your national CSIRT/competent authority. Because you hold employee PII, also build the parallel **GDPR Art. 33** breach-notification track (72 clock-hours to the DPA) — different report, different recipient, same underlying incident.

## Penalty exposure (Important Entity)
Maximum administrative fine: **at least €7,000,000 or 1.4% of total worldwide annual turnover**, whichever is higher (Art. 34) — Member States may set this higher in national law.

## Recommended next steps
1. Confirm your service model meets the Art. 6(30) cloud computing service definition (near-certain for elastic, multi-tenant B2B SaaS).
2. Identify your main EU establishment to determine which Member State/CSIRT governs you, and register under Art. 27.
3. Run a gap assessment against the 2024/2690 technical sub-requirements (not just the general Art. 21(2) text) since these bind you directly as a digital-infrastructure entity.
4. Stand up Art. 20 governance evidence (board approval, training) and the Art. 23 reporting workflow in parallel.
5. Do not treat your customer's compliance request as the trigger — you have an independent, direct NIS2 obligation regardless of what any single customer asks.

*This is general compliance information, not legal advice. Confirm your exact service classification and Member State of main establishment with qualified counsel.*
