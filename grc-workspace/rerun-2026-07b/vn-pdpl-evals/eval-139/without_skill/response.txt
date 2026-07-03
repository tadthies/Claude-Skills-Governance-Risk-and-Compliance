# Designing a PDPL-Compliant Consent Mechanism — Vietnamese E-Commerce App

## Core Principles of Valid Consent Under Vietnam's PDPL
Vietnam's data protection framework requires consent to be:
1. **Voluntary/Freely given** — not a condition of using the app unless the data is genuinely necessary for the service.
2. **Informed** — the data subject must understand what they're consenting to (what data, for what purpose, for how long, with whom it may be shared).
3. **Explicit/Affirmative** — a clear, unambiguous act, not inferred from silence, inactivity, or pre-selected options.
4. **Specific** — separate consent for separate, distinct purposes (e.g., order fulfillment vs. marketing vs. third-party data sharing) rather than one bundled blanket consent.
5. **Recorded/Evidenced** — the app must be able to demonstrate consent was given (what was shown, when, and by whom).
6. **Withdrawable** — the mechanism to withdraw must be as easy as the mechanism to give consent.

## Valid Forms of Consent

| Mechanism | Valid? | Notes |
|---|---|---|
| Unticked checkbox actively clicked by user | Yes | Must be a genuine opt-in action |
| Clicking "I Agree" / "Accept" button after viewing terms | Yes | Terms must be accessible, not buried |
| Toggle switch defaulted to "off," actively switched on | Yes | Must be visually clear |
| Digital signature or OTP-confirmed consent (for higher-risk data, e.g., payment/ID data) | Yes | Recommended for sensitive personal data |
| Layered consent (short notice + link to full policy, with explicit action) | Yes | Good practice for mobile UX |
| Separate, granular toggles per purpose (marketing, analytics, third-party sharing) | Yes | Required — bundled consent for unrelated purposes is problematic |

## Prohibited / Invalid Practices

| Practice | Why It's Prohibited |
|---|---|
| Pre-ticked checkboxes | Not an affirmative act; treated as no consent |
| Consent bundled with general Terms of Service (take-it-or-leave-it for unrelated processing) | Not "specific"; coerces consent for unnecessary purposes |
| Implied consent from continued use of the app ("by using this app you agree...") without an explicit action | Silence/inaction is not valid consent |
| Making core app functionality contingent on consenting to unrelated processing (e.g., forcing marketing consent to complete checkout) | Violates "freely given" — consent must not be coerced via service denial |
| Dark patterns (confusing language, hidden opt-outs, disproportionately hard withdrawal vs. easy sign-up) | Undermines informed/freely-given nature of consent; increasingly scrutinized by regulators globally and likely to be viewed unfavorably under Vietnam's framework |
| Consent obtained without clear disclosure of purpose, retention, and recipients | Fails the "informed" requirement |
| Using vague, generic, catch-all purposes ("to improve our services and for other purposes") | Fails specificity requirement |
| Failure to offer an equally simple withdrawal mechanism | Violates the requirement that withdrawal be as easy as consent |

## Recommended Consent Flow for Your E-Commerce App

### At Account Creation / Checkout
1. **Layered notice:** Short, plain-language summary of what data is collected (name, email, address, payment info) and core purpose (order fulfillment) — with a link to the full privacy policy.
2. **Primary consent action:** Unticked checkbox or "Accept & Continue" button for the data strictly necessary to complete a purchase (name, delivery address, payment processing). This should be treated as necessary for contract performance where possible, minimizing reliance on consent alone for core transactional processing.
3. **Separate, optional toggles (all defaulted OFF) for:**
   - Marketing emails/SMS/push notifications
   - Personalized advertising / profiling
   - Sharing data with third-party partners (e.g., logistics affiliates, ad networks) — beyond what's strictly needed to fulfill the order
   - Use of data for analytics beyond service improvement necessity

### For Sensitive Data (e.g., ID verification for high-value orders, payment card data)
- Use a heightened consent step: explicit confirmation (e.g., OTP verification, explicit "I consent to verification using my ID" click) separate from general account consent.
- Clearly state the specific, narrow purpose (fraud prevention, KYC) and retention period.

### Consent Record-Keeping
- Log: timestamp, version of privacy notice/policy shown, specific toggles enabled, method of consent (click/OTP/etc.), and user identifier.
- Store these records for the duration required to demonstrate compliance (commonly aligned with data retention/statute-of-limitations considerations).

### Withdrawal Mechanism
- Provide an in-app settings page where users can toggle off any previously given consent (marketing, profiling, third-party sharing) with one click — mirroring the ease of the original consent action.
- For consent tied to core account functionality, clearly explain the consequence of withdrawal (e.g., "You will no longer receive order-related SMS updates" vs. "Withdrawing this consent will prevent us from processing your orders").

## Summary Design Checklist
- [ ] No pre-ticked boxes anywhere in the flow
- [ ] Granular, purpose-specific consent toggles (not bundled)
- [ ] Clear, plain-language notice before consent is captured
- [ ] Separate heightened consent flow for sensitive data (payment, ID)
- [ ] Consent records logged with timestamp and notice version
- [ ] One-click (or equally easy) withdrawal mechanism
- [ ] Core service functionality not held hostage to non-essential consents
- [ ] Periodic review/refresh of consent if purposes change materially

## Important Caveat
This design reflects the general consent principles under Vietnam's PDPL framework (which builds on and extends the earlier Decree 13 approach). Specific procedural requirements — such as exact record-retention periods for consent evidence or any prescribed consent form language — should be confirmed against the PDPL's implementing decree and, ideally, reviewed by Vietnamese legal counsel before launch.
