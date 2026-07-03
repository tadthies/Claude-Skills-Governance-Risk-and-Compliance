# FedRAMP Impact Levels: Low vs. Moderate vs. High — and What Applies to Law Enforcement Sensitive Data

## Important context first: terminology is changing under CR26

As of today, FedRAMP is in the middle of a transition under **CR26 (FedRAMP Consolidated Rules for 2026)**. The historical FIPS 199-based impact levels — **Low / Moderate / High** (plus **LI-SaaS**) — are being replaced with **Certification Classes A–D** (per notice NTC-0004, in effect through December 31, 2028). The class labels change the *names* of the baselines, not the underlying control requirements. During the transition, old and new labels are linked, and most existing FedRAMP documentation, marketplace listings, and vendor conversations still use the legacy Low/Moderate/High terms — so it's worth knowing both.

| Legacy Impact Level | CR26 Certification Class | NIST 800-53 Rev 5 Controls |
|---|---|---|
| LI-SaaS | **Class B** (partial) | ~54 (subset of Low) |
| Low | **Class B** | ~156 |
| Moderate | **Class C** | 323 |
| High | **Class D** | 421 |
| *(no legacy equivalent)* | **Class A** (new pilot/transitional) | Entry via external frameworks (e.g., SOC 2 Type II) through Program Certification; 2-year window to reach B/C/D |

## What differentiates the three levels

The levels are based on the **potential impact to federal operations, assets, or individuals if the confidentiality, integrity, or availability of the system's data were compromised** (a FIPS 199 categorization — "limited," "serious," or "severe/catastrophic" harm).

### Low (Class B)
- **Impact if breached:** Limited adverse effect on federal operations/assets or individuals
- **Typical data:** Non-sensitive federal information — e.g., public-facing informational systems, low-risk SaaS tools with no PII and no sensitive federal data
- **Control burden:** ~156 controls/enhancements (lightest)
- **LI-SaaS** is a lighter-weight sub-path under this class for low-risk SaaS with minimal data sensitivity

### Moderate (Class C)
- **Impact if breached:** Serious adverse effect on federal operations/assets or individuals
- **Typical data:** The most common baseline — covers the majority of federal cloud deployments, **including systems handling Controlled Unclassified Information (CUI)**
- **Control burden:** 323 controls/enhancements
- This is where most general-purpose federal SaaS/PaaS/IaaS products land

### High (Class D)
- **Impact if breached:** Severe or catastrophic effect on federal operations/assets or individuals — potential for loss of life, major financial loss, or major mission failure
- **Typical data:** Law enforcement data, financial data, health data, and other categories where compromise has the most severe consequences
- **Control burden:** 421 controls/enhancements (heaviest) — includes stricter requirements such as functional (not just tabletop) Contingency Plan testing, annual penetration testing, and phishing-resistant MFA strongly preferred for privileged accounts

## Which level applies to you: Law Enforcement Sensitive (LES) data → High / Class D

Based on your description — a product that handles **law enforcement sensitive data** — this points squarely at the **High impact level, i.e., Class D under CR26**. Law enforcement data is explicitly called out as a category where a confidentiality, integrity, or availability compromise would have a **severe or catastrophic effect** (e.g., compromising investigations, endangering personnel, or undermining prosecutions), which is the defining criterion for High/Class D.

### Why this matters practically
- **Control count nearly triples** vs. Moderate (421 vs. 323) — expect materially more implementation and documentation effort
- **Stricter parameters** apply across families: e.g., IA-2(1) strongly prefers phishing-resistant MFA for privileged accounts, CP-4 contingency plan testing should be functional (not just tabletop), CA-8 penetration testing is required annually
- **Cloud platform choice matters**: If you're building on AWS GovCloud or Azure Government, both are FedRAMP High-authorized, so PE and much of SC can be inherited — this significantly reduces your build burden versus building High-impact infrastructure from scratch
- **FedRAMP 20x** is now the primary authorization pathway (continuous authorization, modular API-driven submissions) — but confirm with FedRAMP PMO whether High/Class D systems are fully supported under 20x yet or still require a legacy Agency Authorization package for now, since High-impact systems have historically had a smaller pool of authorization paths
- **FedRAMP Ready retires July 28, 2026** — if you were planning to pursue FedRAMP Ready as an interim step, pivot now to either FedRAMP 20x or a full authorization package

### Recommended next steps
1. **Confirm the categorization formally** — don't rely solely on "law enforcement sensitive" as a label; work through a FIPS 199 categorization exercise (confidentiality/integrity/availability impact ratings) with your ISSO or a 3PAO to validate High/Class D is correct, and document the rationale (this maps to control **PL-10**, baseline selection)
2. **Confirm data handling scope** — clarify whether the data is CUI-adjacent, contains PII (triggers the new **PT** family), or has any specialized handling requirements (e.g., CJIS if this touches criminal justice information specifically — note CJIS and FedRAMP are related but distinct programs, and law enforcement data may need to satisfy both)
3. **Engage a 3PAO early** — High-impact assessments are the most rigorous; early engagement helps surface architectural gaps before a costly failed assessment
4. **Plan for OSCAL** — machine-readable OSCAL package submission is mandatory by September 30, 2026, so build this into your authorization package planning now rather than retrofitting later

---
*Use official FedRAMP templates and the FIPS 199 categorization guidance from fedramp.gov — this guidance should inform, not replace, formal categorization performed with your Authorizing Official (AO) or 3PAO. Given the sensitivity of law enforcement data, also verify whether CJIS Security Policy requirements apply in parallel to FedRAMP.*
