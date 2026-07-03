# Designing an SBOM Programme for CRA Compliance

## Why SBOM matters under the CRA

The CRA does not use the term "SBOM" as a standalone mandatory public artifact in the operative text the way some other frameworks imply, but Annex I Part II (vulnerability handling requirements) and the recitals explicitly require manufacturers to:
- Identify and document the components contained in the product, including making a **Software Bill of Materials** available, in a commonly used and machine-readable format, covering **at least the top-level dependencies**, upon request from a market surveillance authority, and to keep it for the purposes of vulnerability identification and handling.
- Address and remediate vulnerabilities in the product **and its components** without delay.

In practice, market surveillance authorities and CSIRTs can request your SBOM at any time, and you need it internally regardless to run your own vulnerability handling process. So treat the SBOM as both a compliance artifact and an operational necessity.

## 1. Programme objectives

1. Produce and maintain an accurate, machine-readable SBOM for every product with digital elements you manufacture.
2. Use the SBOM as the backbone of your continuous vulnerability monitoring process (Annex I Part II).
3. Be able to produce the SBOM to a market surveillance authority on request, in a standard format, without significant delay.
4. Support rapid impact analysis when a new vulnerability (e.g., a CVE in a common library) is disclosed — "which of our products/versions are affected?"

## 2. Format and standard

Choose one (or both, generated from the same source data) of the widely used machine-readable SBOM formats:
- **CycloneDX** (OWASP) — strong tooling support for software composition analysis and vulnerability correlation; increasingly the de facto standard referenced in EU cybersecurity policy discussions.
- **SPDX** (Linux Foundation / ISO/IEC 5962) — mature, ISO-standardized, strong license-compliance heritage, also widely supported.

Either is defensible as "commonly used and machine-readable." Pick based on your existing tooling (many CI/CD SBOM generators support both) and standardize across the organization so all products are comparable.

## 3. What the SBOM must contain

At minimum, per CRA expectations, your SBOM should capture **top-level dependencies**, but a robust programme should go deeper for your own vulnerability-handling capability:

**Required/expected fields:**
- Component name and supplier/author
- Version identifier
- Unique identifiers (e.g., CPE, PURL — package URL — for automated vulnerability database matching)
- Dependency relationships (direct/top-level vs. transitive, where feasible)
- License information (supports broader compliance, not CRA-specific but standard SBOM content)
- Component hash/checksum (for integrity verification)
- Timestamp and SBOM author/tool provenance (who/what generated it, when)

**Recommended for depth beyond the CRA floor:**
- Transitive dependencies (not just top-level) — needed to actually catch vulnerabilities buried several layers deep, which is the realistic attack surface (e.g., Log4Shell-style issues live in transitive dependencies)
- Firmware/OS-level components (bootloader, kernel, drivers) in addition to application-layer packages — critical for an IoT/embedded product
- Third-party/commercial-off-the-shelf (COTS) components and open-source components alike
- Build/toolchain metadata if relevant to provenance

## 4. Programme architecture

### a. Generation
- Integrate automated SBOM generation into your **CI/CD build pipeline** so every build/release produces a corresponding SBOM as a build artifact — do not rely on manual/periodic creation.
- Use language/ecosystem-appropriate tooling (e.g., dependency-tree extraction for the firmware build system, package manager introspection for any Linux-based BSP, container image scanning if applicable).
- For embedded/firmware builds specifically, ensure your build system captures binary-level components too (statically linked libraries, vendored code), not just what a package manager sees — this is a common blind spot for IoT devices.

### b. Storage and versioning
- Store one SBOM per product version/firmware release, versioned alongside the release itself, retained for the duration of your support commitment plus a reasonable buffer (align retention with your Annex I Part II support-period commitment).
- Maintain an internal inventory/index mapping product model + firmware version → SBOM, so you can quickly answer "which shipped products contain component X version Y."

### c. Vulnerability correlation
- Feed the SBOM into a **Software Composition Analysis (SCA)** tool or vulnerability database matching process (e.g., matching PURLs/CPEs against NVD, OSV, GitHub Advisory Database, or a commercial feed) on a continuous/scheduled basis — not just at release time.
- Set up alerting so that when a new CVE is published against a component in your SBOM inventory, your security/engineering team is notified automatically with the list of affected product lines/versions.
- This continuous matching process is what actually operationalizes the Annex I Part II obligation to "identify and remediate vulnerabilities without delay" — a static, one-time SBOM is not sufficient.

### d. Governance and ownership
- Assign clear ownership: typically a product security or engineering function owns SBOM generation quality; a security/compliance function owns the vulnerability correlation and response workflow.
- Define an SLA for triage once a vulnerability is identified in a component (e.g., critical/high severity triaged within X business days), feeding into your broader vulnerability handling and update/patch release process.
- Maintain a documented procedure describing how you generate, store, update, and respond to SBOM-derived findings — this procedure itself is something a market surveillance authority or notified body may want to review as evidence of your Annex I Part II process.

### e. Availability on request
- Ensure you can export/produce the SBOM in the chosen standard format promptly if a market surveillance authority requests it — this should be a near-immediate lookup against your version-indexed SBOM store, not a scramble to reconstruct dependency data after the fact.
- Decide internally whether you'll also make (a limited/top-level) SBOM available to customers or downstream integrators as a trust signal — not required by the CRA to be public, but increasingly expected by enterprise/B2B customers and aligns with transparency best practice.

## 5. How SBOM fits into vulnerability handling end-to-end

1. **Build time:** SBOM auto-generated and stored per release.
2. **Continuous monitoring:** SBOM components matched against vulnerability feeds on an ongoing basis (daily/weekly cadence at minimum).
3. **Triage:** New match triggers a ticket; security team assesses exploitability/severity/impact in the context of how the component is actually used in your product (not every listed CVE in a dependency is reachable/exploitable in your deployment).
4. **Remediation:** If confirmed applicable, patch or mitigate; this feeds your update mechanism (which must be capable of automatic/timely delivery per Annex I Part I #13).
5. **Disclosure:** If the vulnerability is significant, follows your coordinated vulnerability disclosure (CVD) policy and, if actively exploited, the CRA's 24hr/72hr/14-day reporting timeline to ENISA/CSIRT.
6. **Documentation:** Updated SBOM (reflecting the patched version) generated for the new release; vulnerability record closed out with reference to the fix.
7. **Auditability:** The full chain (original SBOM → vulnerability match → triage decision → remediation → updated SBOM) should be retrievable as evidence of your Annex I Part II compliance process.

## 6. Practical rollout plan

**Phase 1 (0–2 months):** Select SBOM format (CycloneDX and/or SPDX) and tooling; pilot automated generation on one product line's CI/CD pipeline, including firmware/binary-level components.
**Phase 2 (2–4 months):** Roll out SBOM generation across all product lines; stand up SBOM storage/version index.
**Phase 3 (4–6 months):** Integrate SCA/vulnerability correlation tooling with continuous scanning against the SBOM inventory; define triage SLAs and ownership.
**Phase 4 (ongoing):** Formalize the documented procedure, integrate with your CVD policy and CRA incident-reporting workflow, and rehearse the end-to-end flow (new CVE → SBOM match → triage → patch → updated SBOM → disclosure) periodically as a tabletop exercise.

## Bottom line

Your SBOM programme needs to do two things simultaneously: (1) satisfy the CRA's baseline requirement to document and produce top-level component information to authorities on request, and (2) function as the operational engine of your Annex I Part II vulnerability-handling obligations — continuous detection, triage, remediation, and update delivery. Building it only to the letter of "top-level dependencies, on request" will satisfy the paperwork but won't give you the depth (transitive dependencies, firmware-level components) needed to actually catch and fix the vulnerabilities that matter.
