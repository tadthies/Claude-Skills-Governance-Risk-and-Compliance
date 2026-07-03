# EU AI Act Compliance Analysis: AI Diagnostic Imaging Tool (Class IIa MDR Device)

## Executive Summary

Your hospital is deploying an AI-powered diagnostic imaging tool that has been CE-marked as a Class IIa medical device under EU MDR (Regulation 2017/745). The vendor's characterization of it as a "safety component" for your radiology department is legally significant and triggers specific obligations under the EU AI Act (Regulation (EU) 2024/1689). To answer your core question directly: **CE marking under the MDR does NOT automatically satisfy AI Act requirements**, and your hospital has substantial obligations both as a deployer and, depending on circumstances, potentially as a co-developer.

---

## 1. High-Risk Classification via Annex I Path A (Article 6(1))

### Why This System Is Automatically High-Risk

Your AI diagnostic imaging tool qualifies as a **high-risk AI system** under the EU AI Act through what is known as **"Path A" classification** in Article 6(1). This path applies when:

1. The AI system is a **safety component** of a product, OR the AI system itself is the product; AND
2. That product is covered by **Union harmonisation legislation listed in Annex I** of the AI Act; AND
3. The product requires **third-party conformity assessment** under that sectoral legislation.

In your situation, all three criteria are satisfied:

- **Safety component criterion**: The vendor has confirmed the AI diagnostic imaging tool is a safety component for your radiology department. Diagnostic imaging AI tools that influence clinical decisions meet this threshold because errors in output could directly compromise patient safety.

- **Annex I coverage**: **EU MDR (Regulation 2017/745)** is explicitly listed in **Annex I, Section A** of the AI Act. This is a direct statutory cross-reference — any AI system that is a safety component of an MDR-regulated product is automatically captured.

- **Third-party conformity assessment**: A Class IIa medical device under the MDR requires **Notified Body involvement** in the conformity assessment procedure (Articles 52–54 of MDR). This satisfies the third-party assessment requirement.

### Practical Implication

There is no ambiguity here. The combination of (a) vendor confirmation of "safety component" status, (b) MDR Annex I listing, and (c) the Class IIa Notified Body requirement means this system is a **high-risk AI system as a matter of law**, regardless of any other characterisation. No separate risk assessment or threshold analysis is needed to reach this conclusion.

---

## 2. MDR CE Marking Does NOT Automatically Satisfy AI Act Requirements

This is one of the most important and commonly misunderstood points in AI Act compliance for medtech. The CE mark your vendor obtained under the MDR **demonstrates compliance with MDR requirements** — it says nothing about AI Act compliance.

### Why They Are Separate Regimes

The EU AI Act and the EU MDR are distinct regulatory instruments with different:

- **Regulatory focus**: MDR covers the safety and performance of medical devices broadly; the AI Act specifically governs AI system risks, transparency, human oversight, and data governance.
- **Competent authorities**: MDR is enforced by national medicines/medical device competent authorities; AI Act market surveillance authorities may be different bodies in your Member State.
- **Requirements**: The AI Act imposes obligations on AI systems (documentation, data governance, human oversight, accuracy, cybersecurity) that have no direct equivalent in the MDR's conformity assessment framework.

### The Integration Requirement

Critically, for Annex I Path A systems, the EU AI Act does not create a parallel conformity assessment process. Instead, **AI Act requirements (Articles 9–17) must be integrated into the existing MDR conformity assessment procedure**. This means the Notified Body conducting the MDR assessment must also verify AI Act compliance as part of that same assessment.

The core AI Act obligations that must be satisfied and verified are:

| Article | Requirement |
|---------|-------------|
| **Art. 9** | Risk management system specific to the AI system throughout its lifecycle |
| **Art. 10** | Data and data governance requirements (training, validation, testing datasets) |
| **Art. 11** | Technical documentation (detailed AI-specific documentation package) |
| **Art. 12** | Record-keeping and automatic logging capabilities |
| **Art. 13** | Transparency and provision of information to deployers |
| **Art. 14** | Human oversight measures (ability to override, interrupt, or stop the system) |
| **Art. 15** | Accuracy, robustness, and cybersecurity requirements |
| **Art. 17** | Quality management system |

Your vendor, as the AI system **provider**, bears primary responsibility for satisfying Articles 9–17 and for ensuring these are covered in the conformity assessment. However, as a hospital deployer, you must **verify that these obligations have been met** — and the CE mark alone is insufficient evidence of this.

**Action required**: Request from your vendor explicit documentation that their MDR conformity assessment incorporated the AI Act requirements under Articles 9–17. Ask specifically whether their Notified Body addressed AI Act compliance, and obtain copies of relevant technical documentation and the EU declaration of conformity covering AI Act requirements.

---

## 3. The 2 August 2028 Compliance Deadline

### Timeline for Annex I Safety Component Systems

The EU AI Act's compliance deadlines are staggered. For AI systems that are safety components of products covered by Annex I legislation (which is exactly your situation), the applicable deadline is:

**2 August 2028**

This deadline was **confirmed and extended** by the **Digital Omnibus** (adopted 29 June 2026), which moved the deadline from the originally planned 2 August 2027. This gives organizations deploying Annex I-embedded AI systems additional time to achieve full compliance.

### What the Deadline Means for You

- **Before 2 August 2028**: Your hospital and your vendor have time to integrate AI Act requirements into the existing MDR compliance framework, update technical documentation, and ensure the conformity assessment covers AI Act obligations.
- **After 2 August 2028**: Full compliance with the AI Act is mandatory. Non-compliant systems cannot lawfully remain in service.

### Do Not Treat This as Permission to Wait

The 2028 deadline is a compliance deadline, not a grace period for inaction. Several preparatory steps — particularly those requiring Notified Body involvement and technical documentation updates — have long lead times. You should begin engaging your vendor about their AI Act compliance roadmap immediately. If the vendor cannot demonstrate a credible path to AI Act compliance by 2028, this represents a procurement risk that should be escalated to hospital leadership.

---

## 4. Hospital Deployer Obligations Under Article 26

Even though the provider (your vendor) carries the primary burden of Articles 9–17 compliance, your hospital, as the **deployer** of this AI system in a professional context, has its own mandatory obligations under **Article 26** of the EU AI Act. These are not optional and apply independently of the vendor's compliance status.

### Article 26 Obligations in Detail

**1. Follow Vendor Instructions (Art. 26(1))**
You must deploy and use the AI diagnostic imaging tool strictly in accordance with the instructions for use provided by the vendor. This has practical implications:
- Do not use the system for clinical indications outside its approved/documented scope
- Do not integrate it into workflows in ways not contemplated by the vendor's instructions
- Ensure your radiology IT team does not modify the system in ways that deviate from vendor specifications

**2. Staff Competence (Art. 26(4))**
You must ensure that staff who operate the AI system or interact with its outputs have sufficient AI literacy and technical competence. For a diagnostic imaging AI tool, this means:
- Radiologists and radiology technicians must understand what the system does, its limitations, and the basis of its outputs
- Staff must understand when and how to apply clinical judgment independently of the AI's recommendations
- Training records documenting competence should be maintained
- AI literacy obligations under Article 4 apply to all staff in your organization who use AI systems

**3. Monitor the System (Art. 26(5))**
You must actively monitor the AI system's operation in your specific deployment context. This includes:
- Tracking clinical performance metrics (e.g., sensitivity/specificity in your patient population)
- Identifying cases where the system behaves unexpectedly or produces outputs inconsistent with clinical expectations
- Assessing whether your patient population, imaging equipment, or clinical workflows differ materially from the conditions under which the system was validated

**4. Notify Incidents (Art. 26(5))**
You must notify the vendor of any serious incidents or malfunctions discovered during your monitoring. "Serious incident" in this context aligns with MDR serious incident reporting requirements and includes cases where the AI system's output contributed to patient harm or near-miss events.

**5. Log Retention — 6 Months (Art. 26(6))**
You must retain logs generated by the AI system for a minimum of **6 months**. Practically, this means:
- Ensure your PACS/RIS integration preserves AI output logs (not just final radiologist reports)
- Configure your IT infrastructure to retain AI inference logs separately if the imaging system does not automatically preserve them
- Establish a log retrieval process for audit or regulatory inquiry purposes

**6. Notify Workers (Art. 26(7))**
Where the AI system's outputs affect workers (e.g., if the tool is used to assist radiographers or technicians), you must notify those workers that they are subject to AI system outputs. This applies in addition to any works council or employee representative consultation requirements under applicable employment law.

**7. Register with Public Authority (Art. 60)**
As a **public authority deployer** (a hospital operating under public law in most EU Member States), you have an additional obligation under **Article 60**: you must **register your use of this high-risk AI system in the EU AI database** before deploying it. This registration is a public transparency measure. Private hospitals should verify whether they fall within the scope of Art. 60 based on their legal status and national implementing guidance.

---

## 5. Summary of Recommended Actions

| Priority | Action | Responsible Party | Timeline |
|----------|--------|-------------------|----------|
| Immediate | Confirm with vendor whether their MDR conformity assessment covered AI Act Arts. 9–17 | Hospital procurement / legal | Within 30 days |
| Immediate | Verify EU AI database registration obligation (Art. 60) and register if required | Hospital compliance officer | Before go-live |
| Short-term | Develop and deliver AI literacy training for all radiology staff who interact with the system | Hospital HR / radiology department | Before go-live |
| Short-term | Establish log retention infrastructure (minimum 6 months) | Hospital IT | Before go-live |
| Short-term | Implement monitoring protocol to track AI system performance in your patient population | Radiology department lead | Before go-live |
| Ongoing | Document compliance with Art. 26 obligations (instructions adherence, staff competence, monitoring, incident reporting) | Hospital compliance officer | Continuous |
| By 2 August 2028 | Confirm vendor has integrated AI Act compliance into MDR conformity assessment | Vendor management / procurement | Before deadline |

---

## 6. Key Regulatory References

- **Regulation (EU) 2024/1689** (EU AI Act): Articles 6(1), 9–17, 26, 60; Annex I Section A
- **Regulation (EU) 2017/745** (EU MDR): Articles 52–54 (conformity assessment); listed in AI Act Annex I
- **Digital Omnibus** (adopted 29 June 2026): Extended Annex I safety component deadline to 2 August 2028
- **AI Act Article 4**: AI literacy obligations for deployer organizations

---

*This analysis reflects the EU AI Act (Regulation (EU) 2024/1689) and the Digital Omnibus as adopted on 29 June 2026. Organizations should consult qualified legal counsel and their national AI Act competent authority for jurisdiction-specific implementation guidance.*
