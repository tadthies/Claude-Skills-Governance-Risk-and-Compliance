## SBOM Programme Design — CRA Compliance

A Software Bill of Materials (SBOM) is required by the CRA both as a standalone artifact (Annex I, Part II) and as an input to your Technical Documentation (Annex VII). Below is a programme design covering content requirements, tooling, governance, and how it plugs into vulnerability handling.

### 1. What the SBOM Must Contain (Minimum, per CRA)

- **Product name and version**
- For **each component**:
  - Component name
  - Version
  - Supplier/author
  - Licence
- **Dependency relationships** — at minimum, top-level dependencies must be captured (deeper transitive mapping is strongly recommended for effective vulnerability triage, even though the CRA floor is top-level only)

**Format requirements:**
- Must be **machine-readable**
- Recommended standards: **SPDX** (ISO/IEC 5962:2021) or **CycloneDX** (security-focused, supports VEX)
- JSON or XML preferred for machine readability
- Must be provided **on request to national market surveillance authorities**
- Must be kept **current throughout the support period** — not a one-time snapshot at release

**Recommended addition — VEX:** Not mandated, but strongly recommended as a companion artifact. A Vulnerability Exploitability eXchange (VEX) document lets you state whether a specific CVE actually affects a specific product version, which reduces false-positive noise for customers and regulators scanning your SBOM against vulnerability databases.

### 2. Programme Architecture

**A. Generation — build it into CI/CD, not as an afterthought**
- Integrate automated SBOM generation tooling into the build pipeline (e.g., Syft, Trivy, SPDX tools, or language-specific generators such as `cyclonedx-npm`, `cyclonedx-maven-plugin`, `pip-audit`).
- Generate a new SBOM on every release build, and ideally on every merge to a release branch, so it's always traceable to a specific artifact/version.
- Capture both direct and transitive dependencies where feasible — even though CRA's floor is top-level, transitive visibility is what actually lets you answer "are we affected by CVE-X" quickly.

**B. Storage and versioning**
- Store SBOMs alongside build artifacts, tagged to the exact product version/release they describe.
- Retain historical SBOMs for the full support period (minimum 5 years) plus the 10-year technical documentation retention window that applies to your overall Annex VII file.

**C. Governance and ownership**
- Assign SBOM maintenance to a **named team or role** (e.g., product security / DevSecOps owner) — this is a specific expectation under CRA SBOM governance guidance.
- Define a review cadence: SBOM must be regenerated and reviewed with every release, and whenever a third-party/open-source component is updated, added, or removed outside of a release cycle (e.g., emergency patch).
- Include SBOM currency as a release gate — a release should not ship without an updated SBOM.

**D. Upstream/third-party component management**
- For every third-party and open-source component you integrate, track its own vulnerability disclosure and update posture.
- Where feasible, request SBOMs from your own upstream suppliers so your SBOM accurately reflects nested dependencies rather than being a black box at the third-party layer.
- Recognize the support-period interaction: if your product integrates a component with a *shorter* security-update lifecycle than your product's own support commitment, you must either extend your own support/patch coverage for that component independently, or substitute an alternative that can be supported for the full period. Your SBOM is the mechanism that makes this dependency visible in the first place.

### 3. How SBOM Fits Into Vulnerability Handling (Annex I, Part II)

The SBOM isn't a standalone compliance checkbox — it's the backbone of your entire vulnerability handling obligation:

1. **Vulnerability identification:** Your SBOM is the inventory that vulnerability scanning and CVE monitoring run against. Without an accurate, current SBOM, you cannot reliably know which of your shipped products are affected when a new CVE is published for a component you use.
2. **Remediation triage:** When a CVE affecting a component is disclosed, the SBOM tells you exactly which product versions/lines include that component, so you can scope the affected population precisely — critical for meeting "without undue delay" remediation and the 24-hour/72-hour ENISA/CSIRT reporting clocks if the vulnerability turns out to be actively exploited.
3. **CVD/VDP intake support:** When external researchers report a vulnerability via your published disclosure channel, your SBOM lets you quickly confirm whether the reported component/version is actually present in your product.
4. **CERT/CSIRT information sharing:** Accurate SBOM data supports meaningful information sharing with EU CERT/CSIRT networks — you can speak precisely about affected versions rather than in generalities.
5. **Regulatory production on request:** National market surveillance authorities can request your SBOM at any time; a stale or manually-maintained SBOM creates both a compliance gap and a practical scramble under time pressure.
6. **Technical documentation (Annex VII):** The SBOM (or equivalent) is an explicit required element of your Annex VII technical file, alongside architecture diagrams, risk assessment, and vulnerability handling policy documentation.

### 4. Recommended Rollout Plan

| Phase | Actions |
|---|---|
| **Phase 1 — Tooling** | Select SBOM format (SPDX or CycloneDX), select generation tooling per language/build stack, integrate into CI/CD |
| **Phase 2 — Baseline** | Generate an initial SBOM for every currently-shipping product line and version; identify components with unclear licensing/support status |
| **Phase 3 — Governance** | Assign named SBOM ownership; define update triggers (release, component change, emergency patch); set retention policy aligned to support period + 10-year technical file retention |
| **Phase 4 — Integration** | Wire SBOM data into your vulnerability scanning/CVE monitoring pipeline and your CVD/VDP intake process; add VEX generation for known-affected/known-unaffected CVE statements |
| **Phase 5 — Upstream** | Request SBOMs from key third-party/open-source suppliers to extend visibility into transitive dependencies; formalize support-period alignment checks |
| **Phase 6 — Regulatory readiness** | Build a documented process for producing the SBOM to a national market surveillance authority on request, and confirm it's referenced correctly in your Annex VII technical documentation |

### Timing Context (today: 3 July 2026)

The vulnerability and incident reporting obligations that your SBOM directly supports become legally binding on **11 September 2026** — roughly 10 weeks from now. Given that CVE triage speed depends entirely on SBOM accuracy, I'd prioritize Phases 1–4 immediately so the reporting pipeline has reliable data to work from when the obligation goes live. Full CRA application (all obligations, including EU database registration referencing SBOM-derived data for Class I/II products) applies from 11 December 2027.

### Bottom Line

Treat the SBOM not as a document you produce once for an audit, but as a living, CI/CD-generated artifact that is the operational foundation of your entire CRA vulnerability handling programme — identification, triage, disclosure, and regulatory reporting all depend on it being current and accurate.
