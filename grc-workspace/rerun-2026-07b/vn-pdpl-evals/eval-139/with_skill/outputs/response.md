# Designing a PDPL-Compliant Consent Mechanism for a Vietnamese E-Commerce App

Under Vietnam's PDPL (Law No. 91/2025/QH15, Article 9) and its implementing Decree 356/2025/ND-CP (Article 6), consent is the primary lawful basis you'll rely on for most e-commerce processing (account creation, marketing, personalisation, payment data, loyalty programmes). Here's how to design it correctly.

## Core Validity Requirements (Article 9)

Every consent you collect must be:
- **Voluntary** — never made a mandatory condition for using the app where not actually necessary for that function
- **Explicit** — a clear affirmative action by the user
- **Specific** — separate consent for each distinct purpose (no bundling unrelated purposes into one consent)
- **Informed** — the user must understand exactly what they're consenting to
- **Recorded** — you must keep verifiable proof of consent (who, when, what was consented to, via what method)

Consent must specify: the type of personal data, the purpose of processing, the identity of the organisation processing it, and the data subject's rights.

## Valid Consent Methods (Decree 356 Article 6)

For an e-commerce app, your practical options are:

1. **Website/application form** — checkboxes or confirmation flows, but the box must start **unticked**; the user must actively tick/click to consent.
2. **Email** — consent expressed via email from the user's registered address (useful for confirming account-level preferences).
3. **SMS/text message** — specific consent syntax from the user's registered mobile number (e.g., for order/delivery notifications).
4. **Written/electronic signature** — for higher-stakes agreements (e.g., BNPL/credit terms if you offer them).
5. **Recorded telephone call** — less common for e-commerce, but valid if you have a call-based onboarding or support flow.
6. Any other electronic format that lets you verifiably identify the data subject and the specific consent given.

## Recommended Consent Architecture for Your App

Design **layered, purpose-specific consent** rather than one blanket checkbox:

| Consent Layer | Data Involved | Method | Notes |
|---|---|---|---|
| Account registration (basic data: name, email, phone) | Basic personal data | Active checkbox at signup, unticked by default | Tie to account creation purpose only |
| Payment processing (card/bank details, transaction history) | **Sensitive** personal data (Decree 356 Art. 4) | Separate, explicit checkbox/confirmation distinct from account consent | Must be visually and functionally separate — cannot be bundled with general T&Cs |
| Marketing communications (email/SMS/push) | Basic personal data | Separate opt-in checkbox, unticked by default | Must be revocable independently of transactional consent |
| Loyalty/rewards programme | Basic (and possibly behavioural) data | Separate consent at enrolment | Per Decree 356 sector guidance: loyalty data requires separate consent from transactional data |
| Cookies / on-site tracking, personalisation | May include sensitive behavioural tracking data (social media/behavioural tracking is a sensitive category) | Cookie consent banner with granular accept/reject — no pre-ticked categories | Essential cookies can be exempt if clearly disclosed; non-essential tracking needs active opt-in |
| Automated recommendations / profiling (AI-driven product suggestions, credit/BNPL scoring) | N/A | Notice + opt-out mechanism | Decree 356 Article 10: inform users their data feeds automated processing and give a simple opt-out, especially where it significantly affects them (e.g., credit decisions) |

## Sensitive Data — Extra Requirements (Article 10)

Payment/financial data (bank accounts, cards, transaction and credit history) is classified as **sensitive personal data** under Decree 356 Article 4(7). This means:
- You need **explicit, separate consent** distinct from your general consent — do not fold it into the account T&Cs.
- Clearly label and visually separate the sensitive-data consent request from other consents.
- Retain proof of this consent distinctly (e.g., a separate consent record entry with its own timestamp/version).

## Practices That Are Prohibited

Under Article 9 and Decree 356 Article 6, the following do **not** constitute valid consent and must be avoided:
- **Silence or inaction** — e.g., "if you don't opt out within 7 days, we assume consent"
- **Pre-ticked checkboxes** — any box that defaults to checked
- **Continued use of the service as implied consent**, unless that use *is* the disclosed purpose itself and this is made explicitly clear at the point of collection (a narrow exception — don't rely on it broadly)
- **Bundled consent** — combining consent for unrelated purposes (e.g., "I agree to the Terms of Service, marketing emails, and data sharing with partners" as a single checkbox)
- **Consent obtained through deception, coercion, or undue influence** — e.g., dark patterns, confusing toggle labels, disproportionately difficult opt-out flows relative to opt-in
- **Making non-essential processing a condition of using the app** — e.g., refusing app access unless the user agrees to marketing data sharing that isn't necessary for the core service

## Withdrawal Mechanism (Build This In From Day One)

- Users must be able to withdraw consent at any time, as easily as they gave it.
- Withdrawal requests must be honoured within **15 working days** (Decree 356 Article 5) for consent withdrawal/restriction of processing.
- Withdrawal does not retroactively invalidate processing that occurred before withdrawal — but you must stop the relevant processing going forward.
- Provide a self-service settings page (preferred) alongside a formal request channel, since this reduces operational burden and demonstrates "as easy to withdraw as to give."

## Recordkeeping

For each consent event, log at minimum: user identifier, purpose consented to, data categories covered, method used (e.g., app checkbox), timestamp, consent text/version shown to the user, and IP/device metadata if available. This is your evidence in the event of a dispute, audit, or Ministry of Public Security inquiry.

## Practical Build Checklist

- [ ] Replace any pre-ticked boxes across signup, checkout, and marketing preference screens
- [ ] Split consent into distinct, purpose-specific toggles (account, payment/sensitive data, marketing, cookies, loyalty)
- [ ] Add a visible, plain-language explanation of each purpose next to its consent control
- [ ] Build a consent log/audit trail in your backend
- [ ] Build a self-service withdrawal/preference centre with a 15-working-day SLA for anything requiring manual processing
- [ ] Add opt-out controls for any AI-driven recommendation/profiling features
- [ ] Review cookie banner for granular, non-pre-ticked category consent

*This is general compliance guidance, not legal advice. Have your final consent flows and privacy notice reviewed by qualified Vietnamese counsel before launch, particularly around the sensitive-data (payment) consent flow.*
