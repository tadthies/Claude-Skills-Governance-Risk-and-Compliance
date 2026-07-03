# EU AI Act Compliance Analysis: Open-Source GPAI Model (200B Parameters, 3×10^24 FLOPs)

**Scenario:** A 200-billion-parameter large language model trained on 15 trillion tokens with approximately 3×10^24 FLOPs of training compute, to be released under an open-source licence.

---

## 1. Classification as a GPAI Model Under Article 3(63)

Your model qualifies as a **General-Purpose AI (GPAI) model** under Article 3(63) of Regulation (EU) 2024/1689 (the EU AI Act). The definition covers a model that:

- Is trained with **large amounts of data** using **self-supervision at scale** — your model was trained on 15 trillion tokens, which far exceeds any threshold for "large" by current standards.
- Exhibits **significant generality** — a 200-billion-parameter GPT-class architecture is capable of a wide range of language tasks (text generation, summarisation, translation, question answering, code generation, and more).
- Is **capable of being used for multiple diverse tasks** — this is the defining characteristic of a GPAI model, as opposed to a narrow, task-specific AI system.

**Conclusion:** You are a **GPAI model provider** under the EU AI Act, and the obligations in Chapter V (Articles 51–56) apply to you as of **2 August 2025** (the GPAI obligations application date under Article 113).

---

## 2. Systemic Risk Assessment: 3×10^24 FLOPs Is Below the Article 51 Threshold

Article 51 of the EU AI Act establishes a **presumption of systemic risk** for GPAI models trained with **cumulative training compute exceeding 10^25 floating-point operations (FLOPs)**.

Your model's training compute is approximately **3×10^24 FLOPs**, which is:

- Roughly **3.3 times below** the 10^25 FLOPs systemic risk threshold.
- Therefore, your model does **not automatically fall within the systemic risk category** under Article 51(1).

This means the enhanced obligations of **Article 55** — which include adversarial testing and red-teaming, a Safety and Security Framework, serious incident reporting to the AI Office, and cybersecurity protections — do **not apply by default** to your model.

### Important Caveat: Commission Designation Power

However, Article 51 also grants the **European Commission the power to designate a GPAI model as presenting systemic risk independently of the FLOPs threshold**. This designation can occur on the basis of:

- Capabilities or impacts that suggest systemic risk, even if training compute is below 10^25 FLOPs.
- Market reach, downstream usage at scale, or multimodal capabilities that raise systemic risk concerns.
- A Commission implementing act following consultation with the AI Office and the Scientific Panel.

**Practical implication:** Even though your model is below the automatic threshold today, you should monitor Commission guidance and AI Office communications. If your model achieves very wide downstream adoption or demonstrates unexpected high-impact capabilities post-release, it could be designated as a systemic risk model in the future. Open-source release, in particular, can lead to rapid and unpredictable scaling of usage — a factor that may be weighed in any designation assessment.

---

## 3. Applicable Obligations: The Open-Source Exception Under Article 53

Because your model will be released under an **open-source licence**, a specific exception in Article 53 applies.

### Standard GPAI Obligations (Article 53, All Providers)

For all GPAI model providers, Article 53 normally requires:

1. **Technical documentation** as specified in **Annex XI** — covering model architecture, training methodology, training data characteristics, performance benchmarks, and intended use cases.
2. **Information for downstream providers** as specified in **Annex XII** — enabling deployers who build on your model to understand its capabilities, limitations, and how to use it responsibly.
3. A **copyright compliance policy** in accordance with **Directive (EU) 2019/790** on copyright in the Digital Single Market — specifically addressing obligations under Article 4 (text and data mining by commercial actors) and Article 3 (text and data mining for research purposes).
4. A **publicly available summary of training content** — a high-level, publicly accessible description of the data used to train the model.

### The Open-Source Exception

Under Article 53(2), GPAI model providers that release their model weights under a **free and open-source licence** that allows access to, use of, modification of, and distribution of the model are **exempt from the Annex XI technical documentation and Annex XII downstream provider information requirements**, provided the model does not present systemic risk.

Since your model:
- Is released under an open-source licence, AND
- Is below the 10^25 FLOPs systemic risk threshold AND has not been designated by the Commission as presenting systemic risk,

**your reduced obligations under Article 53 are:**

| Obligation | Required? |
|---|---|
| Annex XI technical documentation | **Exempt** (open-source exception) |
| Annex XII downstream provider information | **Exempt** (open-source exception) |
| Copyright compliance policy (Dir. 2019/790) | **Required** |
| Publicly available training content summary | **Required** |

### What You Must Do

**a) Copyright Compliance Policy (Directive 2019/790)**

You must establish and publicly document a policy demonstrating compliance with EU copyright law as it applies to your training data. This should address:

- How you identified and complied with text and data mining opt-outs under Article 4 of Directive 2019/790 (the machine-readable reservation mechanism).
- How you handled any research-purpose exemptions under Article 3.
- Your approach to rights clearance or fair use/fair dealing assessments for web-scraped content.
- How you will handle future takedown requests or copyright disputes related to training data.

This policy should be public-facing, reasonably detailed, and kept up to date.

**b) Publicly Available Training Content Summary**

You must publish a summary describing the data used to train your model. This does not need to be a full technical data sheet (that is only required for non-open-source providers), but it must give the public meaningful information about:

- The types of data sources used (e.g., web crawl, books, code repositories, academic papers).
- Approximate proportions or characterisation of data domains.
- Any filtering, deduplication, or quality-control steps applied.
- Languages represented in the training corpus.
- Any known limitations or gaps in the training data.

This summary is a transparency measure aimed at enabling downstream users, researchers, regulators, and the public to understand the provenance and nature of the model's training data.

---

## 4. What You Do NOT Need to Do (Absent Systemic Risk Designation)

For clarity, the following Article 55 systemic risk obligations do **not** apply to your model at this time:

- Adversarial testing and model evaluation (red-teaming) as required by the AI Office guidelines.
- Preparation and maintenance of a **Safety and Security Framework**.
- Reporting of **serious incidents** to the AI Office.
- Implementation of specific **cybersecurity protections** against model extraction, data poisoning, or adversarial attacks on the model weights.
- Participation in AI Office-led risk assessments or model evaluations.

---

## 5. Timeline and Enforcement

### 2 August 2025 — GPAI Obligations Apply

GPAI obligations under Chapter V (Articles 51–56) have been in force since **2 August 2025**. If your model is already in deployment or has been released to the public, you are currently subject to the copyright compliance policy and training content summary requirements. If your model is still under development, you should ensure these obligations are met prior to or at the point of public release.

### 2 August 2026 — AI Office Enforcement Powers Activate

Full enforcement powers for the AI Office — including the ability to conduct investigations, impose fines, and require compliance measures — activate on **2 August 2026**. However, the obligations themselves are already legally in force; the 2026 date relates to the enforcement architecture becoming fully operational.

### Digital Omnibus (Adopted 29 June 2026)

The Digital Omnibus, adopted on 29 June 2026, made certain adjustments to the EU AI Act framework. Providers should monitor any implementing acts or guidance issued by the AI Office following this legislative development, particularly regarding GPAI model obligations and any clarifications to the open-source exception scope.

---

## 6. Recommended Action Plan

| Priority | Action | Deadline |
|---|---|---|
| High | Publish a copyright compliance policy addressing Directive 2019/790 | Before or at release |
| High | Publish a training content summary covering your 15T token dataset | Before or at release |
| Medium | Monitor AI Office guidance on GPAI model obligations and open-source scope | Ongoing |
| Medium | Watch for any Commission designation proceedings that could reclassify your model as presenting systemic risk | Ongoing |
| Low | Consider voluntarily publishing Annex XI-style technical documentation (best practice, not required) | Within 6 months of release |
| Low | Prepare a capability assessment to understand if your model's downstream reach could trigger a systemic risk designation | Within 12 months of release |

---

## Summary

Your 200-billion-parameter open-source LLM is a **GPAI model** under Art. 3(63) of the EU AI Act. At 3×10^24 FLOPs, it sits **below the 10^25 FLOPs systemic risk threshold** in Art. 51, so the enhanced Art. 55 obligations do not apply by default. Thanks to the **open-source exception in Art. 53**, your obligations are reduced: you are exempt from the full Annex XI and Annex XII documentation requirements, but you **must** publish a copyright compliance policy (per Directive 2019/790) and a publicly available summary of your training content. These obligations have applied since **2 August 2025**. You should remain alert to the Commission's power to designate systemic risk independently of the FLOPs threshold, particularly as open-source adoption scales.
