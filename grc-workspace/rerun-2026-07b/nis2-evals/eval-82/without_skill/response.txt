# NIS2 Applicability: B2B Cloud HR SaaS Provider

## Short Answer

**Yes, you are very likely directly in scope of NIS2** — not because of your size, but because of *what you are*: a provider of **cloud computing services**, which is a digital infrastructure/ICT service category listed in Annex I of the Directive, and one of the categories where the standard SME size-cap exemption does not apply in the way you might expect.

## Why Size Doesn't Save You Here

NIS2's general rule (Article 2) exempts micro and small enterprises (under 50 employees AND under €10M turnover/balance sheet) from scope. At 75 employees and €15M revenue, you would exceed the small-enterprise threshold anyway and qualify as a **medium-sized enterprise**, so the general size-cap exemption would not apply regardless.

But more importantly: **cloud computing service providers** are explicitly listed in **Annex I** under the "Digital Infrastructure" sector. This category — along with DNS providers, TLD registries, data centre service providers, content delivery networks, trust service providers, and providers of public electronic communications networks/services — is treated as a **digital infrastructure entity type**, and these entity types are generally captured with less regard to the standard size exemptions in certain Member State transpositions, because Article 2(2) allows Member States to bring in certain entities regardless of size if they are the sole provider of a critical service in a Member State, or if disruption could have significant impact on public safety/security, or if they are otherwise critical for sectoral or cross-border reasons.

That said, in the base-case scenario at 75 employees/€15M revenue, you clear the medium-enterprise threshold on ordinary size-cap grounds alone, so this is somewhat academic — **you are in scope by size regardless of the special digital infrastructure carve-outs.**

## Important Nuance: Are You "Cloud Computing Services" or Something Else?

This is the critical classification question, and the answer determines exactly how NIS2 treats you:

- If you are a HR **software** company that happens to deliver it via a multi-tenant cloud model, but you don't operate the underlying infrastructure (you build on top of AWS/Azure/GCP), you are technically a "digital service" — but the relevant Annex I category to check is **"providers of cloud computing services."** This is generally interpreted broadly to include SaaS providers, not just IaaS/PaaS hyperscalers, in most Member State guidance, because "cloud computing service" is defined in the Directive (referencing the EU's cloud computing definition) as a service enabling on-demand network access to a shared pool of configurable computing resources — SaaS falls within this definition explicitly in the recitals.

- **Practical conclusion: as a B2B cloud-based SaaS provider, you should assume you fall under the "cloud computing services" entity type in Annex I**, making you a **Digital Infrastructure sector entity**.

## Classification: Essential or Important Entity?

Cloud computing service providers are one of the entity types that, per Article 3, are classified as **Essential Entities regardless of size** once they exceed the small/micro exemption thresholds — digital infrastructure providers (cloud computing services, data centres, DNS, TLD registries, trust service providers, public electronic communication networks/services) are treated as Essential Entities in Annex I when they are medium or large, not merely Important Entities as would be the default for most other Annex I sectors at medium size.

**Conclusion: You are very likely an Essential Entity**, not an Important Entity, assuming your HR SaaS platform meets the "cloud computing services" definition (on-demand, scalable, shared resource pool delivered as a service).

## What You Need to Do: Article 21 Compliance

Article 21 requires "appropriate and proportionate" technical, operational, and organisational measures, proportionate to your risk exposure, cost, and size — this proportionality principle matters for a 75-person company, since your implementation should be right-sized, not identical to a Fortune 500 program. The required measures cover:

### 1. Risk Analysis & Information Security Policy
Document a formal risk assessment methodology and maintain an information security policy covering your HR SaaS platform, customer data, and corporate IT environment.

### 2. Incident Handling
Establish an incident response plan: detection, triage, containment, eradication, recovery, and — critically — the reporting workflow described below (Article 23).

### 3. Business Continuity & Crisis Management
Backup policies, disaster recovery plans, and crisis management procedures — especially important since customers rely on your platform for HR operations (payroll-adjacent data can be highly sensitive).

### 4. Supply Chain Security
Assess and manage security risks from your suppliers — your cloud infrastructure provider (AWS/Azure/GCP), any subprocessors, authentication providers, payment processors, etc. Article 21(2)(d) explicitly calls out supply chain security as a named measure, and this is often a major gap for SaaS companies that haven't formally assessed vendor risk.

### 5. Security in System Acquisition, Development & Maintenance
Secure SDLC practices, vulnerability management, patch management, and vulnerability disclosure policy.

### 6. Policies to Assess Effectiveness
Regular testing/auditing of your security measures — penetration testing, vulnerability scanning, security audits.

### 7. Cyber Hygiene & Training
Basic cyber hygiene practices (password policies, phishing awareness) and staff training, including mandatory training for management.

### 8. Cryptography and Encryption Policies
Formal policy on when/how encryption is applied — this matters directly for HR data (highly sensitive personal data: salaries, performance reviews, sometimes health/disability data).

### 9. Human Resources Security, Access Control, Asset Management
Access control policies (least privilege), asset inventory, HR security procedures for your own staff (onboarding/offboarding, background checks where lawful).

### 10. Multi-Factor Authentication
MFA for access to your systems, secure communications, and secure emergency communications where relevant.

### Governance Requirement
Your management body (board/leadership team) must formally **approve** the cybersecurity risk-management measures, **oversee** their implementation, and can be held liable for non-compliance arising from failure to oversee. Management must complete cybersecurity training.

## Incident Reporting Obligations (Article 23)

If you experience a "significant incident" (one causing severe operational disruption/financial loss, or affecting others through considerable damage), you must notify your national CSIRT/competent authority:
- **24 hours**: early warning
- **72 hours**: incident notification with initial assessment
- **1 month**: final report

## Practical Next Steps

1. **Confirm your exact classification** with the competent authority in your home Member State — the "cloud computing services" categorization is the crux of your direct-scope argument, so get this confirmed rather than assumed, since some national regulators interpret pure SaaS more narrowly than IaaS/PaaS.
2. **Register** with your national competent authority/CSIRT if confirmed in scope — most Member States require entities to self-identify and register within a defined window after transposition.
3. **Gap-assess** your current security posture against the Article 21 measures listed above — many SaaS companies already have SOC 2 or ISO 27001 programs that cover 70-80% of this; identify what's missing (formal supply chain risk assessments and management-level governance/training are common gaps).
4. **Build your 24/72-hour incident reporting capability** now, before an incident — this is the single most time-sensitive operational requirement and the hardest to stand up reactively.
5. **Review vendor/customer contracts**: your customer flagging this to you suggests they may also be in scope (directly or as part of their own supply chain risk management under their Article 21(2)(d) obligations) and may push contractual security requirements down to you regardless of your direct-scope status.

## Bottom Line

Even if there were any ambiguity about the "cloud computing services" classification, at 75 employees/€15M revenue you clear the standard medium-enterprise size threshold for many other potentially applicable categories, so the practical answer is: **treat yourself as in scope, likely as an Essential Entity via the digital infrastructure/cloud computing category, and begin Article 21 compliance work now.** Confirm final classification with your national competent authority.
