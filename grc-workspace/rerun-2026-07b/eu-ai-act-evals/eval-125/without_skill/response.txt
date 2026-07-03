# Article 50 Transparency Obligations — Chatbot & AI-Generated Product Images

## When do Article 50 obligations apply?

Article 50 (transparency obligations for certain AI systems) has applied since **2 August 2026**... actually, to be precise: Article 50 obligations apply from **2 August 2026**, which is the general application date for most of the Act's operative provisions beyond the earlier-applicable prohibitions (2 February 2025) and GPAI rules (2 August 2025).

Since today's date is 3 July 2026, this means these obligations take effect in about one month, so you should be finalizing implementation now.

## Obligation 1: Customer service chatbot (Article 50(1))

Providers (and by extension, deployers using such systems to interact with people) must ensure that natural persons are informed that they are interacting with an AI system, **unless it is obvious from the circumstances and context of use to a reasonably well-informed person**.

Practically, for your chatbot:
- You must clearly disclose to users that they are chatting with an AI system, not a human agent — e.g., a persistent label like "You're chatting with an AI assistant" at the start of the conversation, or a similarly clear and timely indicator.
- The disclosure must be made **at the latest at the time of the first interaction**, in a clear and distinguishable manner, and accessible to persons with disabilities as relevant.
- The "obvious from context" exception is narrow — a customer service chatbot is unlikely to qualify as "obvious" by default unless the interface unmistakably signals it's automated (e.g., a widget explicitly named/branded as a bot with no ambiguity). Best practice is to disclose explicitly regardless, since regulators are expected to interpret this narrowly at first.
- Note: this obligation applies to the **provider** of the AI system, but if you built/deployed the chatbot for your own e-commerce site, you are effectively both provider and deployer, so the obligation falls on you directly.

## Obligation 2: AI-generated product images (Article 50(4), synthetic content labelling)

Providers of AI systems, including GPAI systems, generating synthetic image (and audio/video/text) content must ensure outputs are **marked in a machine-readable format and detectable as artificially generated or manipulated** (e.g., via watermarking, metadata, cryptographic provenance signals, or similar technical means), to the extent technically feasible, considering the specificities and limitations of various content types, costs, and generally acknowledged state of the art.

Additionally, under Article 50(4) (deployer-facing transparency for deep fakes), **deployers** of an AI system that generates or manipulates image, audio, or video content constituting a **"deep fake"** must disclose that the content has been artificially generated or manipulated.

For your AI-generated product images specifically:
- **Technical marking**: the AI system generating the images (whether built in-house or a third-party tool you use) should embed machine-readable markers (e.g., C2PA-style metadata/watermarking) identifying the image as AI-generated, to the extent technically feasible. If you're using a third-party image generation tool/API, check whether it already embeds this marking — if not, you may need to add your own.
- **Deep fake disclosure**: product images are less likely to constitute "deep fakes" in the classic sense (which typically involves realistic depictions of real people, places, or events that could mislead someone into believing they are authentic/real-world captures) — generic product photography-style images are less likely to trigger this specific disclosure duty compared to, say, a fake image of a real event or person. However, if your AI-generated images depict realistic scenes that could be mistaken for authentic photographs (e.g., a "real" model wearing the product, a "real" location), caution favors labelling them as AI-generated to avoid consumer deception concerns, which also intersects with **unfair commercial practices / consumer protection law** (separate from but related to Article 50).
- There is also a general good-practice/consumer-trust rationale (and increasingly, may be expected as a matter of EU consumer protection enforcement) to label AI-generated marketing imagery even outside strict "deep fake" scope, since misleading customers about product appearance is also actionable under EU consumer protection rules independent of the AI Act.

## Exemptions to be aware of

- Article 50 includes some exemptions/limitations for content that is subject to human review/editorial responsibility, or authorized by law for law enforcement purposes — generally not relevant to your e-commerce/chatbot context.
- Purely assistive AI functions with no impact on the depicted content's substance may have lighter marking expectations, but general product image generation would not qualify for such a narrow carve-out.

## Practical checklist for 2 August 2026

1. Add a clear, persistent AI-disclosure notice to the chatbot interface (before/at first interaction).
2. Confirm whether your image generation tool embeds machine-readable AI-generated content markers; if not, implement watermarking/metadata tagging yourself.
3. Consider visible labelling ("AI-generated image") on product images where realism could mislead customers, both for AI Act alignment and consumer-protection risk mitigation.
4. Document your transparency measures as part of your AI governance/compliance file, since regulators and market surveillance authorities may request evidence of compliance.
5. Train customer-facing and marketing teams on these disclosure requirements ahead of the deadline.

*Disclaimer: This is general informational guidance based on the EU AI Act text as publicly known; not legal advice. Confirm specific implementation approaches (e.g., watermarking standards, disclosure UI patterns) with qualified EU legal/compliance counsel.*
