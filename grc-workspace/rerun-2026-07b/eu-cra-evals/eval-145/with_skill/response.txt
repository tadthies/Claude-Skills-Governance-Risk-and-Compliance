## CRA Obligations — Importer/Distributor vs. Manufacturer

Since you import devices manufactured in Asia and distribute them in the EU, the CRA assigns you distinct legal roles and obligations that are separate from — but dependent on — the manufacturer's obligations. It's important to note your organisation may hold **both** the importer and distributor role simultaneously if you both bring the product into the EU and make it available on the market yourselves.

### Role Definitions

| Role | Definition |
|---|---|
| **Manufacturer** | The Asia-based entity that designs, develops, or produces the PDE (or has it designed/developed/produced) under its own name |
| **Importer** | You, if you bring the products from outside the EU into the EU market |
| **Distributor** | You (or another party), if you make the product available on the EU market other than as the manufacturer or importer |

If you are the first entity placing these Asian-manufactured devices onto the EU market, you are the **importer**. If you then also sell/supply them further down the chain within the EU, you may simultaneously be acting in a **distributor** capacity for those transactions.

### Manufacturer's Obligations (Article 13) — Not Yours, But You Depend on Them

The manufacturer (in Asia) remains responsible for:
1. Designing, developing, and producing the PDE to meet all Annex I essential requirements (security properties + vulnerability handling)
2. Conducting a cybersecurity risk assessment before market placement
3. Preparing and retaining Technical Documentation (Annex VII) for 10 years
4. Conducting the conformity assessment (Module A self-assessment or Notified Body, depending on product class)
5. Drawing up the EU Declaration of Conformity (Annex V) and retaining it for 10 years
6. Affixing CE marking
7. Registering Class I/Class II products in the EU database before market placement
8. Operating the ongoing vulnerability handling programme (VDP, SBOM, free security updates) throughout the support period
9. Reporting actively exploited vulnerabilities and severe incidents to ENISA/CSIRTs
10. Providing a point of contact address for the product
11. Cooperating with market surveillance authorities
12. Taking corrective action or recalls if non-compliance is found

**Critical implication for you:** since the manufacturer is outside the EU, you should check whether they have appointed an **EU Authorised Representative** — an EU-based entity that holds the DoC and technical documentation on the manufacturer's behalf for EU authorities. This is common (and practically necessary) for non-EU manufacturers, and its existence affects how quickly you (and EU authorities) can obtain compliance documentation.

### Your Obligations as Importer (Article 19)

As importer, you must:
1. **Only place on the EU market products accompanied by a valid Declaration of Conformity and technical documentation** — you cannot import products where the manufacturer hasn't completed conformity assessment.
2. **Verify CE marking is affixed and legible.**
3. **Verify the manufacturer is identified on the product** (name, registered trade name, or trademark, and contact address).
4. **Add your own name, registered trade name or mark, and postal/electronic address** to the product, packaging, or accompanying documentation.
5. **Ensure the product carries vulnerability-reporting contact information in a Union language** relevant to the market(s) where you place it.
6. **Not place on the market any product you know (or should reasonably know) is non-compliant.**
7. **Notify the manufacturer and the relevant market surveillance authority** if you believe or have reason to believe a product poses a cybersecurity risk.
8. **Retain copies of the DoC and technical documentation for 10 years.**
9. **Cooperate with market surveillance authorities** on request (providing documentation, information, or corrective action).

### Your Obligations as Distributor (Article 20) — If Also Applicable

If you (or a downstream party) also distribute after import, distributor obligations are lighter but still real:
1. **Verify CE marking, DoC availability, and that instructions/information are provided in a Union language** before making the product available.
2. **Not make available products you know are non-compliant.**
3. **Notify the manufacturer and market surveillance authority** of any risk.
4. **Cooperate with market surveillance authorities** on request.

### Key Differences: Manufacturer vs. You

| Dimension | Manufacturer (Asia) | You (Importer/Distributor) |
|---|---|---|
| Product design/development to Annex I requirements | **Yes — full responsibility** | No — you rely on manufacturer's compliance |
| Conformity assessment (self-assessment or Notified Body) | **Yes** | No — you verify it was done |
| Technical documentation authorship | **Yes** | No — you retain a copy, don't author it |
| Declaration of Conformity | **Drafts and signs** | Verifies it exists and is valid; retains copy |
| CE marking | **Affixes it** | Verifies it's present and legible |
| Vulnerability handling programme (VDP, SBOM, updates) | **Yes — operates it** | No — but must forward risk reports to manufacturer |
| ENISA/CSIRT reporting of exploited vulnerabilities | **Yes — primary obligation** | Not primary, but must notify manufacturer/authorities if you become aware of a risk |
| Adding own identification to the product | N/A | **Yes — required** |
| Retention period for compliance records | 10 years | 10 years (DoC + technical documentation copies) |

### Practical Risk for Your Organisation

Even though you are not responsible for designing the product to meet Annex I, the CRA creates real exposure for importers/distributors:

- **If you place a product on the EU market without valid DoC/technical documentation/CE marking, you are non-compliant** — even though you didn't build the product. Penalties for other-obligations non-compliance (which importer/distributor duties fall under) run up to **€10 million or 2% of global annual turnover**.
- If you have reason to believe a product is non-compliant or poses a risk and you fail to notify the manufacturer and market surveillance authority, that failure is itself a violation.
- Given the manufacturer is based in Asia (outside the EU), due diligence before import is essential: confirm product class (Default/Class I/Class II), confirm conformity assessment route taken, obtain and review the DoC and a summary of the technical documentation, and confirm an EU Authorised Representative is in place if you cannot otherwise obtain compliance records quickly on request from EU authorities.

### Recommended Immediate Actions

1. **Classify the product** (Default/Class I/Class II) using the manufacturer's documentation or your own Annex III/IV review — this determines what conformity evidence should exist.
2. **Request and verify** the DoC, technical documentation summary, and CE marking from the manufacturer before each import shipment/model.
3. **Confirm an EU Authorised Representative** is appointed if the manufacturer has no EU presence.
4. **Add your own identification** (name, address) to products/packaging/documentation as required.
5. **Establish an internal process** to escalate any suspected non-compliance or security risk to both the manufacturer and the relevant national market surveillance authority.
6. **Set up 10-year records retention** for all DoC and technical documentation copies you receive.

### Timing Context (today: 3 July 2026)

Full application of manufacturer, importer, and distributor obligations under the CRA is **11 December 2027**. However, the manufacturer's vulnerability/incident reporting obligations to ENISA/CSIRTs become binding **11 September 2026** — if you become aware of a security risk in an imported product after that date, your obligation to notify the manufacturer and the market surveillance authority "without delay" becomes operationally urgent, since the manufacturer will be under a live 24-hour reporting clock once you flag it to them.

### Bottom Line

The manufacturer in Asia owns product design compliance, conformity assessment, CE marking, and the ongoing vulnerability handling programme. You, as importer (and possibly distributor), own **verification, identification, and risk escalation** — you must confirm the manufacturer's compliance evidence exists before import, add your own traceability information, and act as a safety-net checkpoint that flags non-compliance or risk to both the manufacturer and EU market surveillance authorities. You cannot simply pass through non-compliant products and disclaim responsibility — CRA imposes independent, directly enforceable obligations on you.
