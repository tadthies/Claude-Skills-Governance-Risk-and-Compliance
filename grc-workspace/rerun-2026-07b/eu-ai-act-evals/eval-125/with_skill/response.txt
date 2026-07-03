# E-Commerce Chatbot + AI-Generated Product Images — Art. 50 Transparency Obligations

You have two distinct AI touchpoints, and Art. 50 treats them differently. Let's take each in turn.

## 1. Customer Service Chatbot — Art. 50(1)

**Obligation:** As the provider (and effectively also the deployer, if you operate it yourselves) of the chatbot, you must ensure that users are informed they are interacting with an AI system.

**Exceptions (neither likely applies to a typical e-commerce chatbot):**
- It is obvious to a reasonably well-informed user from context and circumstances that they're talking to an AI (a generic customer-service chat window is not automatically "obvious" — most implementations will need an explicit disclosure)
- The system is authorised by law for detecting criminal offences (not applicable here)

**Practical requirement:** Disclose clearly at the outset — e.g., "You're chatting with an AI assistant" at the start of the conversation, or a persistent label on the chat widget. This is a straightforward, low-burden obligation but it is not optional simply because chatbots are common.

## 2. AI-Generated Product Images — Art. 50(2) and Art. 50(4)

This is the deepfake/synthetic-media transparency obligation, and it falls on **you as deployer** of the image-generation system (the entity putting the AI-generated content into the world in your marketing/listings).

**Obligation:** Where you generate synthetic image content, you must disclose in a **machine-readable format** that the content is artificially generated or manipulated.

**Does it apply to your product images?** Almost certainly yes if the images are photorealistic and could be mistaken for real photographs of products, settings, or (importantly) any depicted people. The obligation is triggered by synthetic image/video/audio/text that resembles real persons, places, or events — stylised/obviously-illustrative product renders are lower risk, but photorealistic AI-generated product photography (especially any showing people, e.g., AI-generated models wearing your products) squarely triggers this.

**Format requirement:** The disclosure must be:
- **Machine-readable** (e.g., embedded metadata/watermarking, not just a visible text label, though a visible label can supplement it)
- Clear and distinguishable
- Provided at the latest at first exposure to the content
- Accessible per Directive 2019/882 accessibility standards

**Exceptions:** Authorised-by-law criminal detection use (not applicable), or artistic/satirical/fictional works with appropriate disclosure that doesn't impair enjoyment (a stretch for standard product photography — unlikely to apply to routine e-commerce imagery).

**Practical note:** If your product images are generated using third-party GPAI-based tools, check whether those tools already embed machine-readable provenance markers (e.g., C2PA-style metadata) — you may be able to rely on tooling-level compliance rather than building your own watermarking, but as deployer you remain responsible for ensuring the disclosure is actually present and functioning.

## 3. From When Do These Obligations Apply?

> **Art. 50 transparency obligations apply from 2 August 2026** for new systems placed on the market — about one month from today (3 July 2026).

For **pre-existing systems already on the market before 2 August 2026**, there is a **grace period until 2 December 2026** specifically for the **machine-readable marking requirement** (Art. 50(2)) — so if your chatbot or image-generation setup is already live today, you have a short additional runway on the technical marking piece, but the general "inform users they're interacting with AI" duty (Art. 50(1)) for the chatbot should be treated as applying from the 2 August 2026 date without a separate grace period.

**Regulatory context to flag:** As of the current date, formal implementing guidance is still developing — the AI Office opened consultation on **draft Art. 50 transparency guidelines in May 2026**, and a **Code of Practice on Marking and Labelling of AI-generated Content** has been through two drafts (December 2025, 5 March 2026) with finalisation expected around Q2 2026. No formal implementing act has been adopted yet as of today, so treat the guidelines/CoP as the best current interpretive source, but stay alert for the finalised version, since implementation specifics (e.g., exact watermarking technical standards) may still shift before your compliance deadline.

## Bottom Line — Action Checklist

| Touchpoint | Obligation | Article | Deadline |
|---|---|---|---|
| Customer service chatbot | Disclose AI interaction to users, clearly, at first interaction | Art. 50(1) | 2 Aug 2026 |
| AI-generated product images (photorealistic / resembling real persons or scenes) | Machine-readable "AI-generated" disclosure | Art. 50(2)/(4) | 2 Aug 2026 (new); grace to 2 Dec 2026 for marking on pre-existing systems |

Neither obligation makes your chatbot or image tool high-risk — both remain in the **limited-risk / transparency-only** tier, so you are not looking at the Annex III conformity regime here, just these disclosure duties. Given you're an e-commerce operator (not primarily an AI provider), you'll typically sit in the **deployer** role for both, though if you built the chatbot in-house you're also its provider for Art. 50(1) purposes.

*This is general compliance guidance, not legal advice. Confirm final implementation details against the finalised Code of Practice on Marking and Labelling once published, and consult qualified counsel for your specific product-image use case.*
