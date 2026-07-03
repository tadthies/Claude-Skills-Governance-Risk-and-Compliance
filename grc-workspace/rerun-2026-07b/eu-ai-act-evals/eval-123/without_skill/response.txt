# Open-Source LLM (~8×10^23 FLOPs) — GPAI Obligations

## Step 1: Is this a "general-purpose AI model" (GPAI)?

Yes. An LLM with broad capability to perform a wide range of tasks, trained on large-scale data, is a General-Purpose AI Model under Article 3(63) of the EU AI Act. GPAI obligations (Chapter V) have applied since **2 August 2025**, so they are already in force.

## Step 2: Does the open-source exemption apply?

The Act provides a **partial exemption for free and open-source GPAI models** (Article 53(2)): providers of GPAI models released under a free and open-source licence that allows access, usage, modification, and distribution of the model, and whose parameters (including weights), model architecture, and model use are made publicly available, are **exempt from**:
- Article 53(1)(a) — maintaining technical documentation for the AI Office/national authorities, and
- Article 53(1)(b) — providing documentation/information to downstream providers who integrate the model

**However, this exemption does NOT apply to GPAI models with systemic risk.** Since your model appears open-source (weights, architecture, and usage documentation public, free license) it would normally qualify for the light-touch open-source carve-out — **except** that training compute is a key trigger for "systemic risk" classification, which overrides the open-source exemption.

## Step 3: Systemic risk threshold — this is the critical fact here

Under **Article 51** and the associated methodology, a GPAI model is **presumed to have systemic risk** if the cumulative amount of computation used for its training, measured in floating point operations (FLOPs), is **greater than 10^25 FLOPs**.

Your model was trained with **~8 × 10^23 FLOPs**, which is **below** the 10^25 FLOPs systemic-risk presumption threshold (by roughly two orders of magnitude). So, absent a specific AI Office designation based on other criteria (e.g., reach, number of users, or a decision under Article 51(1)(b)/(3)), your model would **not** be presumed to be a GPAI model with systemic risk.

**Conclusion on classification**: Your LLM is a GPAI model **without** systemic risk, and it meets the open-source criteria, so the **open-source exemption applies**.

## Step 4: Obligations that still apply to you (even as open-source, non-systemic-risk)

Even with the exemption from Article 53(1)(a) and (b), open-source non-systemic providers must still:

1. **Draw up and make publicly available a policy to comply with EU copyright law**, including identifying and complying with rights reservations under Article 4(3) of the DSM Copyright Directive (Article 53(1)(c)) — this obligation is **not** waived by the open-source exemption.
2. **Publish a sufficiently detailed summary of the content used for training** the GPAI model, using the template provided/approved by the AI Office (Article 53(1)(d)) — this is also **not** waived by the open-source exemption.
3. If you appoint an authorised representative or engage in commercial activity in relevant ways, comply with any applicable general obligations.

So in short: you're exempt from the two documentation-provision duties (53(1)(a)-(b)), but still must comply with the **copyright policy** and **training data summary** obligations (53(1)(c)-(d)).

## Step 5: Does the GPAI Code of Practice help?

Yes. The **General-Purpose AI Code of Practice** (finalized in 2025, developed by independent experts with multi-stakeholder input, facilitated by the AI Office) is designed as a voluntary tool to help providers demonstrate compliance with the GPAI obligations under Articles 53 and 55, pending harmonised standards. It has three chapters: **Transparency**, **Copyright**, and **Safety and Security** (the latter mainly relevant to systemic-risk models).

Benefits for you:
- **Signing/adhering to the Code** creates a presumption of conformity with the relevant Chapter V obligations (particularly transparency/documentation and copyright), reducing regulatory uncertainty, since it operationalizes vague statutory requirements (like what "sufficiently detailed summary" of training content means) into concrete templates and practices.
- Since the Safety and Security chapter is primarily aimed at systemic-risk model providers, and your model falls below the systemic-risk threshold, that chapter is largely **not directly relevant** to you, though the Transparency and Copyright chapters are useful and directly applicable to your remaining obligations (53(1)(c) and (d)).
- Non-signatories aren't penalized for not signing, but they bear the burden of demonstrating compliance through "other adequate means," which is more burdensome than following the Code's pre-vetted templates (e.g., the AI Office's training data summary template).

## Practical recommendations

1. Publish a public copyright compliance policy (rights-reservation detection/compliance process).
2. Publish a training data summary using the AI Office's official template.
3. Consider formally adhering to the GPAI Code of Practice's Transparency and Copyright chapters to benefit from the compliance presumption and reduce ambiguity/audit risk.
4. Monitor your compute if you plan further training runs or fine-tuning — cumulative FLOPs approaching 10^25 would trigger systemic-risk obligations (systemic risk model notification to the Commission within 2 weeks of meeting the threshold, adversarial testing, incident reporting, cybersecurity, etc.), plus you'd lose part of the open-source carve-out.
5. Keep the model genuinely open (weights, architecture, and usage terms public under a free/open license) to preserve exemption eligibility — restricting any of these elements could jeopardize the Article 53(2) exemption.

*Disclaimer: This is general informational guidance based on the EU AI Act text and the GPAI Code of Practice as publicly known; not legal advice. Confirm your FLOPs calculation methodology and final classification with qualified counsel or the AI Office guidance.*
