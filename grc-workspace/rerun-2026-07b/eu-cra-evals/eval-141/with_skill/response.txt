## CRA Scope and Classification — Consumer Smart-Home IoT Router

### 1. Does the CRA apply?

Yes. Regulation (EU) 2024/2847 (the Cyber Resilience Act) applies to any **Product with Digital Elements (PDE)** — hardware or software with at least one network interface — that is placed or made available on the EU market. A smart-home IoT router:

- Has network connectivity (Wi-Fi, Ethernet, WAN interface) by definition
- Is sold commercially in the EU
- Is not covered by any of the CRA's exclusions (medical devices, aviation, automotive type-approval, marine equipment, military/national security, or non-commercial open source)

So the product is squarely **in scope** as a PDE.

### 2. Product Classification

Routers intended for home use appear explicitly in **Annex III (Class I)** — the list of higher-risk product categories that includes "routers, modems, and network switches intended for home use," alongside smart home hubs/controllers and other network security/monitoring products.

**Classification: Class I (Annex III).**

This is a materially different (stricter) outcome than if the product were treated as a generic/Default consumer IoT device — being a home router pulls it into the enhanced-risk category regardless of how simple the feature set is.

### 3. Conformity Assessment Route

For Class I products, the CRA gives the manufacturer a choice:

- **Module A — Self-assessment**, or
- **Third-party assessment via a Notified Body**

The manufacturer decides; a Notified Body is not mandatory for Class I (unlike Class II). Practically, most consumer router manufacturers will use **Module A self-assessment**, provided they can produce genuine technical evidence of conformity (self-assessment is not self-certification without evidence — market surveillance authorities can inspect the technical file at any time).

Where a relevant EU harmonised standard has been published in the Official Journal (e.g., candidates such as ETSI EN 303 645 for consumer IoT), conformity with that standard gives a **presumption of conformity**, which can materially simplify the self-assessment process. Worth tracking as standards are finalised.

### 4. Key Obligations Summary

As the **manufacturer** of a Class I PDE, you must:

1. Design/develop/produce the router to meet all **Annex I Part I** (security properties) and **Part II** (vulnerability handling) essential requirements.
2. Conduct a cybersecurity risk assessment before placing the product on the market.
3. Prepare **Technical Documentation** (Annex VII) — architecture, threat model, risk assessment, test evidence, SBOM, vulnerability handling policy — and retain it for **10 years**.
4. Complete conformity assessment (Module A or Notified Body, your choice) and draw up the **EU Declaration of Conformity** (Annex V); retain for 10 years.
5. Affix **CE marking** (visibly, legibly, indelibly, on product/packaging/documentation).
6. **Register the product in the EU database for PDEs** before placing on the market — required for Class I products (registration expected to be operational around December 2027; Default-class products are exempt from this, but Class I is not).
7. Maintain a vulnerability handling programme throughout the support period: CVD/VDP policy, published contact point, SBOM, free security updates, and CERT/CSIRT information sharing.
8. Report actively exploited vulnerabilities and severe incidents to ENISA/national CSIRTs (24-hour early warning / 72-hour full report / final report).
9. Commit to and communicate a support period (minimum 5 years, or expected product lifetime if shorter).

### 5. Timeline Awareness (as of today, 3 July 2026)

- **Vulnerability and incident reporting obligations** to ENISA/CSIRTs become legally binding on **11 September 2026** — about 10 weeks from now. If you don't already have a 24/72-hour reporting pipeline, this should be an immediate priority.
- **Notified Body designation/operation** begins 11 December 2026.
- **Full CRA application** (all manufacturer, importer, distributor obligations, including CE marking, DoC, and EU database registration for Class I/II products) applies from **11 December 2027**.
- Products already on the market by that date, if unchanged, have until 11 December 2027 to come into compliance — but any new model or significant redesign placed on the market before then should already be built to the full standard, since the vulnerability-reporting clock starts in September 2026.

### Recommended Next Step

Given the router is Class I, I'd recommend running a full **Annex I gap assessment** against your current product (security-by-default configuration, authentication, update signing, VDP, SBOM, support period) well ahead of the December 2027 deadline, and treat the September 2026 vulnerability-reporting obligation as the more urgent near-term milestone.
