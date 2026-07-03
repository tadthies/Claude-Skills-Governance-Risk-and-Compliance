# FedRAMP Authorization: Process, Path Types, and Recommendation for a First Authorization

Welcome to the federal cloud market. Here's the end-to-end picture as of **July 2026**, under the **CR26 (FedRAMP Consolidated Rules for 2026)** framework, which changed some terminology and pathways you'll see referenced in older articles.

---

## Important Context Up Front: The Landscape Has Changed

Two things materially affect the "start to finish" answer for you as a *new* entrant:

1. **JAB P-ATO is fully suspended.** The FedRAMP PMO is now the sole authorization body. There is no longer a "JAB path" to choose — this changes the classic two-path framing you may have read about elsewhere.
2. **FedRAMP 20x is now the primary, preferred authorization pathway** — a continuous-authorization, API-driven, automated-evidence model. Traditional SSP/SAP/SAR-based Agency Authorization packages still exist and remain available, particularly for complex systems, during the CR26 transition.
3. **FedRAMP Ready is retiring July 28, 2026** — practically immediately from where you're standing today. Do not start down a "get FedRAMP Ready first" plan; pivot straight to FedRAMP 20x or a full authorization package.
4. Baseline labels have also changed: Low/Moderate/High/LI-SaaS are now **Certification Classes A–D** (NTC-0004), with old and new labels linked during the transition period (through Dec 31, 2028).

---

## Part 1: The FedRAMP Authorization Process, Start to Finish

### Step 1 — Define Scope and Target Certification Class
- Identify your Cloud Service Offering (CSO) type: IaaS / PaaS / SaaS.
- Determine what federal data (including CUI) the system will process, store, or transmit.
- Map that to a **CR26 Certification Class**:
  - **Class A** — Pilot/transitional; entry via external frameworks (e.g., SOC 2 Type II) through Program Certification; 2-year window to reach B/C/D.
  - **Class B** — Replaces LI-SaaS + Low; non-sensitive federal information, limited harm if breached.
  - **Class C** — Replaces Moderate; the majority of federal deployments, including CUI. Most likely target for a typical SaaS vendor.
  - **Class D** — Replaces High; severe/catastrophic impact systems (law enforcement, financial, health data).

### Step 2 — Choose Your Authorization Pathway
- **FedRAMP 20x (preferred/primary path)**: continuous authorization model, modular API-driven submissions, automated evidence collection. This is where FedRAMP is steering all new entrants.
- **Legacy Agency Authorization package**: the traditional SSP/SAP/SAR/POA&M model, still available — particularly suited to complex systems during the CR26 transition period.
- Note: there is **no JAB pathway option anymore** — it's fully suspended.

### Step 3 — Readiness / Gap Assessment
Before engaging a 3PAO or agency sponsor, assess readiness across:
- Authorization boundary definition and network/data-flow diagrams
- Security policies and procedures (IR, CP, access control, config management, etc.)
- MFA, RBAC, least privilege
- FIPS 140-2/3 validated encryption at rest and in transit
- Vulnerability scanning coverage (OS, database, web app, containers)
- Audit logging and centralized SIEM
- Personnel security and privacy training (Rev 5 requirement)
- Supply chain risk management (SBOM, third-party inventory — Rev 5 requirement)
- OSCAL readiness (mandatory for submissions by **September 30, 2026**)

*(Full 75+ item checklist available on request — organized by control domain.)*

### Step 4 — Secure a Path to Authorization
This is the step that differs most by pathway:
- **Legacy Agency Authorization**: You need a **federal agency sponsor** willing to be your Authorizing Official (AO). Without an agency partner actively wanting to use your product, this path stalls — agency sponsorship is typically the single biggest bottleneck for new CSPs.
- **FedRAMP 20x**: Designed to reduce dependency on finding a sponsoring agency first, using automated, continuous evidence submission to the PMO. (Confirm current program mechanics directly on fedramp.gov, since 20x processes continue to evolve rapidly.)

### Step 5 — Independent Assessment (3PAO)
- Engage a FedRAMP-recognized **Third Party Assessment Organization (3PAO)**.
- If a 3PAO helped author your SSP, a *different* 3PAO must perform the independent assessment (per A2LA R311).
- The 3PAO produces the **Security Assessment Plan (SAP)** and, after testing, the **Security Assessment Report (SAR)**.
- Your system must be "frozen" from changes during the assessment window.

### Step 6 — Authorization Package Assembly
The full package consists of:
```
Authorization Package
├── System Security Plan (SSP) + Appendices A–Q
├── Security Assessment Plan (SAP) + Appendices A–D   [3PAO-prepared]
├── Security Assessment Report (SAR) + Appendices A–F [3PAO-prepared]
└── Plan of Action & Milestones (POA&M)               [SSP Appendix O]
```
- Must use official FedRAMP PMO templates (fedramp.gov/documents-templates).
- **OSCAL machine-readable format is mandatory for all submissions by September 30, 2026** — worth building toward now rather than retrofitting later.

### Step 7 — Authorization Decision
- Legacy path: the sponsoring agency's AO reviews the package and issues an **Agency ATO (Authority to Operate)**.
- FedRAMP 20x: authorization is issued through the PMO's continuous/automated model.

### Step 8 — Continuous Monitoring (ConMon)
Authorization is not a one-time event — it's maintained:
- **Monthly**: vulnerability scan submissions, POA&M updates, inventory updates, ConMon Executive Summary.
- **Annually**: full 3PAO reassessment, updated SSP/appendices, tested IRP and CP, updated SAR/POA&M.
- **POA&M remediation SLAs**: Critical = 15 days, High = 30 days, Moderate = 90 days, Low = 365 days.
- Maintain a dedicated **Security Inbox** (no CAPTCHA/barriers) for urgent vulnerability directives — required since January 5, 2026.

---

## Part 2: Agency ATO vs. JAB P-ATO — What's the Real Difference (and Does It Still Matter)?

| | **Agency ATO** | **JAB P-ATO** |
|---|---|---|
| **Status today (CR26)** | Active — the standard legacy path | **Fully suspended** — no longer obtainable |
| **Sponsor** | A single federal agency acts as the Authorizing Official | Previously: the Joint Authorization Board (DoD, DHS, GSA) reviewed and granted a provisional authorization |
| **Reusability** | Other agencies can reuse the package, but each must do their own risk-acceptance review before granting their own ATO | Was intended to be a pre-vetted "provisional" stamp that agencies could adopt with lighter-weight review |
| **Effort profile** | Requires finding and working closely with one committed agency sponsor from day one | Was higher-bar upfront but theoretically opened the door to easier multi-agency reuse afterward |
| **Relevance to you** | This is your only "traditional" option today | Not available — do not plan around this path |

**Bottom line: the JAB P-ATO path no longer exists.** Any comparison you find in older guides, vendor blog posts, or consultant materials describing "JAB vs. Agency" as two live choices is outdated under CR26. The FedRAMP PMO is now the sole authorization body, and the practical choice for you is between:
1. **Agency ATO** (legacy SSP/SAP/SAR model, agency-sponsored), or
2. **FedRAMP 20x** (the new primary/preferred continuous authorization pathway)

---

## Part 3: Which Path Should You Consider for a First Authorization?

Given you're a cloud software vendor entering the federal market for the first time, here's the practical recommendation:

### Primary recommendation: Pursue FedRAMP 20x
- It's explicitly the pathway FedRAMP is steering all new/pilot entrants toward.
- **Class A** entry is specifically designed for companies like yours coming from an existing compliance baseline (e.g., if you already have or are pursuing **SOC 2 Type II** — that's a recognized on-ramp into Program Certification under Class A).
- Class A gives you a **2-year window** to mature into a full Class B, C, or D certification through complete assessment — letting you get initial market access faster while building out the deeper control set.
- It's less dependent on landing an agency sponsor before you can even start, which is historically the biggest chokepoint for first-time CSPs.
- It invests you early in OSCAL-native tooling and automated evidence collection, which will be **mandatory for everyone by September 30, 2026** anyway — so it's not wasted effort even if you eventually need a higher class.

### When the legacy Agency ATO path still makes sense
- If your product is architecturally complex (e.g., not a straightforward SaaS layered on an already-authorized IaaS/PaaS) and doesn't fit cleanly into the 20x automated-evidence model yet.
- If you already have a committed agency champion who wants to sponsor you and is comfortable running the traditional SSP/SAP/SAR review.
- If your target data sensitivity clearly requires **Class C (Moderate)** or **Class D (High)** from day one and you have the resources (typically $150K–$1M+ and 6–18 months) to run a full assessment immediately rather than incrementally.

### Do NOT pursue:
- **FedRAMP Ready** — retiring July 28, 2026; essentially closed to you already.
- **JAB P-ATO** — fully suspended; not obtainable.

### Suggested next steps for you specifically
1. Determine your target Certification Class (most SaaS vendors handling CUI land at **Class C**).
2. If you have or can quickly obtain **SOC 2 Type II**, seriously evaluate **Class A entry via FedRAMP 20x** as your fastest path to initial federal market access.
3. In parallel, run a readiness/gap assessment against the boundary, encryption, logging, vulnerability management, and identity control domains — these are the most common blockers and findings regardless of which path you choose.
4. Start building OSCAL-compatible documentation now rather than retrofitting before the September 30, 2026 mandate.
5. If leaning toward the legacy Agency ATO path, begin agency relationship-building in parallel with technical readiness work, since sponsor acquisition is often the longest lead-time item.

---

*Use official FedRAMP templates from fedramp.gov for all authorization package documents — this guidance should inform, not replace, the appropriate template sections. Given how fast CR26 mechanics are still being finalized by the PMO, confirm current program specifics (especially FedRAMP 20x submission mechanics) directly on fedramp.gov before finalizing your path decision.*
