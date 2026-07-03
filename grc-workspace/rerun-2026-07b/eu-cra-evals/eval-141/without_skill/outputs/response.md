# CRA Applicability, Classification, and Conformity Assessment — Consumer Smart-Home IoT Router

## 1. Does the CRA apply?

Yes. The EU Cyber Resilience Act (Regulation (EU) 2024/2847) applies to "products with digital elements" (PDEs) — hardware or software products whose intended or reasonably foreseeable use includes a direct or indirect logical or data connection to a device or network. A consumer smart-home IoT router:

- Is a physical hardware product with embedded software (firmware) that connects to a network by definition — this falls squarely within the CRA's definition of a "product with digital elements."
- Is placed on the EU market commercially, so the CRA's obligations attach to whoever places it on the market (in this case, you as manufacturer).
- Is not covered by one of the CRA's carve-outs (e.g., products already regulated under sector-specific rules like medical devices (MDR), aviation, automotive type approval, or products developed exclusively for national security/defense purposes, or non-commercial open-source software developed outside the course of a commercial activity). A commercial consumer router does not qualify for any of these exclusions.

Since the router also incorporates radio functionality (Wi-Fi, possibly cellular), it is very likely also in scope of the Radio Equipment Directive (RED) 2014/53/EU, specifically the cybersecurity-related delegated act provisions (Articles 3(3)(d), (e), (f)). Where RED's cybersecurity provisions apply to a category of radio equipment, CRA compliance for the essential requirements largely supersedes/aligns with those RED provisions to avoid duplicate assessment — but you need to confirm which regime's conformity assessment route governs, since the CRA explicitly carves out overlap with RED for radio equipment to avoid double regulation once the relevant harmonized rules take effect.

## 2. Product classification

The CRA creates three tiers of products with digital elements:

- **Default (non-critical) category** — the majority of products, subject to self-assessment (Module A / internal control) unless they fall into Class I or Class II.
- **Important products with digital elements — Class I** (Annex III, Part I): lower-risk "important" products, e.g., standalone/embedded firewalls, network management systems, password managers, boot managers, VPNs, and — highly relevant here — **network interfaces, routers, modems intended for connection to the internet, and switches**.
- **Important products with digital elements — Class II** (Annex III, Part II): higher-risk important products, e.g., hypervisors, firewalls/intrusion detection intended for industrial/critical use, smart meters, and industrial-grade/critical routers and network switches used in industrial settings.

A **consumer smart-home router intended for internet connectivity** falls under **Annex III, Part I, Class I** ("routers, modems intended for the connection to the internet, and switches, other than those covered under Class II"). Unless the router is specifically marketed/intended for critical infrastructure or industrial control environments (which would push it to Class II), a standard consumer smart-home router is Class I.

## 3. Conformity assessment route

Under the CRA, the conformity assessment procedure depends on the classification:

- **Default category products:** Manufacturer self-assessment (Module A — internal production control) is sufficient; no third-party (notified body) involvement is required, provided the manufacturer applies harmonized standards or common specifications.
- **Class I important products (where this router sits):**
  - If the manufacturer has applied **harmonized European standards** (or common specifications/European cybersecurity certification schemes at "substantial" assurance level or above) covering all applicable essential requirements, the manufacturer may still use **self-assessment (Module A)**.
  - If harmonized standards do not exist, are only partially applied, or the manufacturer chooses not to rely on them, the manufacturer must involve a **notified body** via one of: **Module B + C (EU-type examination plus conformity to type)** or **Module H (full quality assurance)**.
- **Class II important products:** Third-party conformity assessment by a notified body is mandatory regardless of standards used (Module B+C or Module H).
- **Critical products with digital elements:** Subject to European cybersecurity certification under the Cybersecurity Act where a relevant scheme exists and the Commission mandates it.

**Practical answer for your router:** As a Class I important product, you can likely still self-assess (Module A) *if* you fully apply the relevant harmonized standards once published by CEN/CENELEC (these are still being developed as of mid-2026, so watch for their availability). If harmonized standards are not yet available or you cannot demonstrate full conformity through them, you will need to engage a notified body under Module B+C or Module H.

## 4. Other obligations to plan for

Regardless of route chosen, as manufacturer you must also:
- Perform and document a cybersecurity risk assessment covering the product's entire lifecycle.
- Meet the Annex I essential requirements (secure by design/default, no known exploitable vulnerabilities at placing on market, secure default configuration, protection against unauthorized access, confidentiality/integrity/availability protections, minimized attack surface, vulnerability handling processes, etc.).
- Draw up technical documentation (Annex VII), an EU Declaration of Conformity, and affix CE marking.
- Provide a Software Bill of Materials (SBOM) internally (not necessarily published, but must be available to market surveillance authorities/CSIRTs on request) and maintain it in a machine-readable format covering top-level dependencies at minimum.
- Establish a coordinated vulnerability disclosure policy and a single point of contact (POC) for reporting vulnerabilities.
- Commit to a **support period** reflecting expected product use (minimum 5 years unless the product's expected lifetime is shorter, in which case it must be justified and disclosed) during which security updates must be provided.
- Report actively exploited vulnerabilities and severe incidents to ENISA/CSIRT within the CRA's tight timelines (24-hour early warning, 72-hour notification, 14-day final report) once the reporting obligations become applicable.

## 5. Key open items to confirm internally

- Confirm the specific product's intended use case is purely consumer/home — not marketed for critical infrastructure — to lock in Class I rather than Class II.
- Track the harmonized standards status for routers/network equipment; if unavailable at your CE marking date, budget time and cost for notified body engagement (Module B+C or H).
- Check overlap with RED cybersecurity delegated act requirements if the router includes radio functionality, and confirm which assessment satisfies both regimes.
- Note transitional timelines: the CRA's main obligations (conformity assessment, CE marking) become applicable **11 December 2027**, while the vulnerability/incident reporting obligations to ENISA became applicable earlier, **11 September 2026**. Given today's date, you should already be preparing your vulnerability handling and reporting processes.
