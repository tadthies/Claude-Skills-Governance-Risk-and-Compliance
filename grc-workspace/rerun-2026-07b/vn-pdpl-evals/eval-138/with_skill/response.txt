# Do PDPL's DPIA and DPO Obligations Apply to a 15-Person Hanoi Startup?

Short answer: **it depends on what data you process, not just your headcount.** Vietnam's PDPL (Law No. 91/2025/QH15, effective 1 January 2026) gives small and micro enterprises a time-bound opt-out from certain obligations, but that exemption has an important carve-out that can apply even to very small companies.

## The SME Exemption — What It Actually Covers

Small and micro enterprises may opt out of three specific obligations for **5 years from 1 January 2026** (i.e., until 1 January 2031):
- **Article 21** — the domestic Data Protection Impact Assessment (DPIA)
- **Article 22** — certain security measures requirements
- **Article 33(2)** — certain processor obligations

At 15 people, you likely qualify as a small enterprise (and possibly micro, depending on Vietnam's official size thresholds by revenue/headcount, which you should confirm against current SME classification rules).

## The Carve-Out That Matters Most for You

**The exemption does NOT apply if you process sensitive personal data or process data at large scale.** This is the critical question for your startup — headcount alone doesn't decide it.

Sensitive personal data under Decree 356 Article 4 includes 13 categories: health data, biometric/genetic data, financial/banking/transaction data, location/movement data, political/religious views, criminal records, sexual orientation, social media behavioural tracking, and more.

**Practical implication for a 15-person startup:**
- If you only collect basic data (names, emails, phone numbers for a B2B SaaS product, for example) and you're not processing at large scale, you likely **can** claim the SME exemption from the DPIA (Article 21) and from certain security/processor obligations (Articles 22, 33(2)) for the next five years.
- If your product touches health data, biometric data (e.g., facial recognition, fingerprint auth), financial/payment data, precise location tracking, or similar sensitive categories — or if you process personal data at large scale even without being "sensitive" — **the exemption does not apply to you**, regardless of your 15-person headcount. You would need to conduct the DPIA within 60 days of first processing (a deadline that, if you started processing before today, 3 July 2026, may already be running or passed).

## What About the DPO Requirement?

The DPO requirement is a **separate obligation from the DPIA exemption** — the SME exemption list (Articles 21, 22, 33(2)) does not include the DPO appointment requirement. Under Decree 356 Article 13, a DPO is required for organisations processing personal data **at large scale or processing sensitive personal data** — this threshold-based trigger applies regardless of company size or the SME opt-out.

So even if you validly claim the SME exemption for your DPIA, you may still need a DPO if:
- You process sensitive personal data (see the 13 categories above), or
- You process data at large scale (even if all "basic" data)

For a 15-person startup that is neither processing sensitive data nor operating at scale, a DPO would likely not yet be required — but you should still designate a responsible individual for data protection matters as a matter of good practice, since you'll need a contact point for data subject requests and breach handling regardless.

## Recommended Next Steps

1. **Inventory your data:** Map exactly what personal data you collect. Basic vs. sensitive is the pivotal distinction — not your headcount.
2. **Assess scale:** Even basic data processed at "large scale" removes the exemption. Consider your total user/customer base and processing volume.
3. **If exempt:** Document your SME exemption election (Decree 356 requires this to be documented) — don't just assume it applies; formally record the basis for it.
4. **If not exempt (sensitive data or large scale):** Conduct the domestic DPIA within 60 days of first processing (Article 21) and appoint a qualified DPO (degree + 2 years' relevant experience per Decree 356 Article 13) — internal or outsourced.
5. **Regardless of exemption status**, you still must comply with baseline obligations that are NOT exempted: valid consent (Article 9), data subject rights response timelines (2/10/15/20 working days), 72-hour breach notification (Article 23), and privacy notice requirements. The SME opt-out is narrow — it only covers Articles 21, 22, and 33(2), not the whole law.

## Bottom Line

There is no blanket "small business exemption" from PDPL as a whole. The exemption is narrowly scoped to the DPIA and specific security/processor obligations, is time-limited to 5 years, and is void the moment you touch sensitive personal data or operate at large scale. A 15-person Hanoi startup doing ordinary B2B data processing with only basic personal data will likely benefit from the exemption; one building anything involving health, biometric, financial, or location data will not, regardless of size.

*This is general compliance guidance, not legal advice. Confirm your specific SME classification and "large scale" thresholds with qualified Vietnamese counsel, since precise numerical thresholds may be clarified through Ministry of Public Security guidance.*
