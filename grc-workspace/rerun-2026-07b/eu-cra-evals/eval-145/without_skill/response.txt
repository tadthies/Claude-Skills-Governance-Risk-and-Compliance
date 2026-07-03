# CRA Obligations — Importer and Distributor vs. Manufacturer

Scenario: you import and distribute connected devices manufactured in Asia into the EU.

The CRA (Regulation (EU) 2024/2847) follows the same tiered "economic operator" structure used across EU product legislation (the "New Legislative Framework" model, similar to the Radio Equipment Directive, Machinery Regulation, etc.): **manufacturer, authorised representative, importer, distributor**, each with distinct but complementary obligations. Critically, **an economic operator can be reclassified as a manufacturer** under certain conditions — this is a key risk area for importers/distributors to understand.

## 1. Manufacturer's obligations (the Asia-based factory/brand owner)

The manufacturer bears the primary and most extensive burden:
- Design and develop the product to meet Annex I essential requirements (secure by design/default, no known exploitable vulnerabilities, vulnerability handling processes, etc.).
- Conduct the cybersecurity risk assessment and maintain technical documentation (Annex VII).
- Carry out the applicable conformity assessment procedure (self-assessment or notified body route, depending on product class).
- Draw up the EU Declaration of Conformity and affix CE marking.
- Provide the SBOM and maintain vulnerability-handling processes (security updates, CVD policy, contact point).
- Report actively exploited vulnerabilities/severe incidents to ENISA/CSIRT (24hr/72hr/14-day timeline).
- Ensure instructions and safety/security information accompany the product, in a language easily understood by end users, and appropriately translated for each EU market where sold.
- Keep technical documentation and the Declaration of Conformity for at least 10 years (or the support period, whichever is longer) after the product is placed on the market.
- If not established in the EU, **appoint an authorised representative** established in the Union with a mandate to act on the manufacturer's behalf for CRA matters (technical documentation access, cooperation with authorities, etc.).

Since your device is manufactured in Asia, the manufacturer will almost certainly need an EU-based authorised representative unless the manufacturer itself has an EU establishment.

## 2. Your obligations as Importer

As the entity placing an Asia-manufactured product on the EU market under your own import/distribution activity, you are the **importer** under the CRA, with obligations including:

- **Due diligence before placing on the market:** verify that the manufacturer has carried out the appropriate conformity assessment procedure, drawn up the technical documentation, and that the product bears CE marking and is accompanied by the required documentation (Declaration of Conformity or a clear reference to it, instructions, contact information).
- **Verify the manufacturer's identity and contact details** are on the product or its packaging/documentation, and that the manufacturer has appointed an authorised representative if required.
- **Not place a product on the market if you have reason to believe it does not conform** to the essential requirements — you must not import/distribute if you know or suspect non-conformity.
- **Indicate your own name, registered trade name/trademark, and contact address** on the product, packaging, or accompanying documentation.
- **Ensure storage/transport conditions** you control do not jeopardize the product's compliance with essential requirements while it is under your responsibility.
- **Cooperate with market surveillance authorities**, including providing all information/documentation necessary to demonstrate conformity, in a language they can easily understand, upon reasoned request.
- **Sample-check / market surveillance duty:** where you consider or have reason to believe a product presents a cybersecurity risk or is non-conforming, inform the manufacturer and the relevant market surveillance authorities without delay.
- **Support the manufacturer's vulnerability handling and update obligations** to the extent relevant — e.g., ensuring you don't disrupt the update supply chain, and forwarding vulnerability reports/complaints you receive to the manufacturer.
- **Keep a copy of the technical documentation and Declaration of Conformity** available for market surveillance authorities for the same retention period (generally 10 years or the support period).
- **Inform the manufacturer** of any actively exploited vulnerability or severe incident you become aware of relating to the product.

## 3. Your obligations as Distributor (if distinct from your importer role, e.g., downstream resellers)

If you also act as a distributor (or if some of your channel partners are pure distributors buying from you rather than from the Asian manufacturer directly), distributor obligations apply — lighter than importer obligations but still binding:

- **Act with due care**: before making a product available on the market, verify it bears CE marking, is accompanied by required documentation/instructions in an appropriate language, and that the manufacturer and importer (where applicable) have complied with their respective identification obligations (names/contact details on the product).
- **Do not make available** a product you know or believe to be non-conforming; inform the manufacturer or importer, and the relevant market surveillance authority, if you identify a risk.
- **Maintain storage/transport conditions** that do not jeopardize compliance while the product is under your responsibility.
- **Cooperate with market surveillance authorities** on request, providing relevant information.

## 4. Critical risk: when you (importer/distributor) become a "manufacturer"

Under the CRA, an importer or distributor is **deemed to be a manufacturer** and assumes full manufacturer obligations if you:
- Place the product on the market **under your own name or trademark**, or
- Make a **substantial modification** to a product already placed on the market in a way that affects its compliance with the essential requirements, or
- Modify the intended purpose of the product in a way not intended by the original manufacturer.

**This is highly relevant to you if you white-label, rebrand, or private-label these Asia-manufactured devices** — if the router/device ships under your brand rather than the original manufacturer's brand, you likely become the "manufacturer" for CRA purposes, inheriting the full set of manufacturer obligations described in section 1 (technical documentation, conformity assessment, CE marking, SBOM, vulnerability handling, incident reporting, EU declaration of conformity), regardless of who actually designed/built the hardware and firmware.

## 5. Practical action items for your organization

1. **Determine your precise role for each product line**: pure importer/distributor of manufacturer-branded goods, versus rebranding/private-label (which triggers manufacturer status).
2. **Confirm the Asian manufacturer has (or will appoint) an EU authorised representative** and obtain their contact details and mandate documentation.
3. **Request and retain the technical documentation, Declaration of Conformity, and evidence of conformity assessment** from the manufacturer before you import — do not rely on CE marking alone as sufficient verification.
4. **Verify manufacturer contact information and (if applicable) authorised representative details** are present on the product/packaging/documentation; add your own importer identification details.
5. **Build a documented due-diligence checklist** you run before each new product/shipment is placed on the EU market, and retain records for at least 10 years.
6. **Establish a channel to relay vulnerability reports and market surveillance findings** back to the manufacturer promptly, and to cooperate with authorities directly since you are the EU-facing party for many practical enforcement purposes.
7. **If private-labeling**, budget for full manufacturer-level compliance (risk assessment, technical documentation, conformity assessment route matching the product's class, SBOM programme, vulnerability handling, incident reporting) — treat the product as if you designed it, even though it is OEM/ODM-sourced.
8. **Track timelines**: vulnerability/incident reporting obligations under the CRA are already applicable (11 September 2026); main conformity assessment/CE marking obligations become applicable 11 December 2027 — your due diligence obligations as importer/distributor apply from the point the product is placed/made available on the market once the CRA is fully in force.

## Bottom line

As a pure importer/distributor of someone else's branded product, your obligations center on **due diligence, verification, identification, and cooperation** — you check the manufacturer did its job, add your own contact details, and don't knowingly pass on non-conforming products. The manufacturer bears the heavy compliance lift (risk assessment, technical file, conformity assessment, CE marking, SBOM, vulnerability handling, incident reporting). However, if you rebrand/private-label these Asia-manufactured devices under your own name, **you legally become the manufacturer** under the CRA and inherit its full obligation set — this distinction should be confirmed for every product line before you finalize your compliance approach.
