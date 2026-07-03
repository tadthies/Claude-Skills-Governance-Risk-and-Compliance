# From GDPR to CCPA/CPRA: Gap Analysis and Key Differences

Having a mature GDPR program gives you a strong head start — much of the underlying data governance (data mapping, security controls, DPAs with vendors, breach response) is reusable. But CCPA/CPRA is a **different legal architecture** built on different foundational concepts, so you cannot simply relabel your GDPR documents. Below is what's genuinely additive and where the two regimes diverge.

## Foundational Difference: Opt-Out vs. Opt-In

This is the single biggest conceptual gap:

- **GDPR** is built on **lawful bases for processing** — you generally need an affirmative legal basis (consent, contract, legitimate interest, etc.) *before* processing personal data, especially for anything like advertising, which typically requires opt-in consent.
- **CCPA/CPRA** is fundamentally an **opt-out** regime for most processing. Businesses can collect, use, sell, and share personal information by default, subject to notice, and consumers must affirmatively exercise rights to stop it (e.g., opt out of sale/sharing, limit use of sensitive PI). Opt-in consent is only required in narrower circumstances (e.g., known minors under 16 for sale/share, or reusing data for a materially different purpose than disclosed).

**Action needed:** You cannot rely on your GDPR consent banners/consent management platform logic as-is. You need a CCPA-specific opt-out mechanism: a "Do Not Sell or Share My Personal Information" link (or combined "Your Privacy Choices" link), plus honoring the **Global Privacy Control (GPC)** browser signal as a valid opt-out — GPC has no GDPR equivalent requirement.

## Key Additional Steps You Need

### 1. Sale/Sharing Opt-Out Infrastructure
- Determine whether any of your data flows (especially ad tech, analytics, data enrichment vendors) constitute a "sale" or "sharing" (cross-context behavioral advertising) under CCPA's broad definitions — these concepts don't exist in GDPR.
- Build the opt-out link, GPC signal detection, and downstream suppression of ad tags/vendor calls for opted-out consumers.

### 2. California-Specific Notices
- **Notice at Collection**: required at or before collection, distinct from a GDPR Article 13/14 notice in structure and required content (categories of PI, purposes, whether sold/shared, retention criteria).
- **Privacy Policy**: must include CCPA-specific disclosures (categories of PI collected/sold/shared in the past 12 months, consumer rights, retention periods) — supplement your existing GDPR-oriented policy or maintain a jurisdiction-specific version/addendum.
- **"Right to Limit Use of Sensitive Personal Information"** notice and link, if you use SPI beyond what's necessary to provide the service — a CCPA-specific right with no direct GDPR equivalent (GDPR instead relies on "special category data" requiring explicit consent or another Article 9 condition upfront).

### 3. Revise Consumer Rights Workflows
While GDPR and CCPA both offer access, deletion, correction, and portability rights, the **mechanics differ**:
- CCPA requires **at least two designated methods** for submitting requests (e.g., toll-free number + web form) — GDPR has no such prescriptive requirement.
- CCPA response deadline is **45 days** (extendable by another 45 with notice) vs. GDPR's **one month** (extendable by two additional months for complex requests).
- CCPA's Right to Know includes a **"specific pieces of PI"** disclosure option with a higher identity-verification bar, distinct from GDPR's Subject Access Request format.
- CCPA deletion has **different statutory exceptions** than GDPR Article 17(3) — review and reconcile your exception logic (e.g., CCPA's "complete the transaction," "debugging," and "internal use aligned with consumer expectations" exceptions don't map 1:1 to GDPR's exceptions).
- **Household-level requests**: CCPA covers "households" in some contexts (e.g., certain connected-device/joint-account data), a concept absent from GDPR, which is individual-only.

### 4. Non-Discrimination Provision
- CCPA has an explicit **non-discrimination requirement** — you cannot deny service, charge different prices, or provide a different quality of service because a consumer exercised a CCPA right (with an allowance for legitimate financial-incentive/loyalty programs if properly disclosed). This is more prescriptive than GDPR's general principle against detriment.

### 5. Financial Incentive Disclosures
- If you run loyalty programs, discounts, or rewards tied to data collection, CCPA requires specific **financial incentive notices** explaining the material terms, value of the data, and how to opt in/out — a CCPA-specific requirement with no direct GDPR counterpart.

### 6. Vendor Contract Overhaul
- GDPR Data Processing Agreements (DPAs) satisfy Article 28 requirements but **do not automatically satisfy CCPA's service provider/contractor contract requirements**. CCPA contracts need specific clauses: prohibition on selling/sharing the PI further, prohibition on combining with other clients' data, prohibition on using data outside the specified business purpose, and required flow-down obligations.
- You'll likely need a **CCPA-specific addendum or updated contract template** for U.S. vendors, layered on top of (not replacing) your GDPR DPA terms.
- Reassess vendor classifications: GDPR's "processor" doesn't map cleanly to CCPA's "service provider" vs. "contractor" vs. "third party" trichotomy — a vendor could be a GDPR processor but a CCPA "third party" if it uses data for its own purposes.

### 7. Recordkeeping Threshold
- CCPA requires maintaining records of consumer requests and how they were handled for **24 months** — confirm your existing GDPR RoPA (Records of Processing Activities) practices extend to cover this, since GDPR doesn't mandate the same request-log retention period.

### 8. Employee Training
- CCPA specifically mandates that individuals handling consumer inquiries or compliance be **informed of CCPA requirements** — build this into existing GDPR-driven privacy training rather than assuming it's covered generically.

### 9. Risk Assessments and Cybersecurity Audits (CPRA additions)
- CPRA regulations introduce (with phased effective dates) requirements for **annual cybersecurity audits** and **risk assessments** submitted to the California Privacy Protection Agency (CPPA) for businesses engaged in significant processing of sensitive PI or high-risk automated decision-making. These are structurally similar to GDPR's DPIA (Data Protection Impact Assessment) requirement but have distinct triggers, content requirements, and a regulator-facing submission element that DPIAs (generally) don't have. Don't assume your DPIA process automatically satisfies this — confirm current CPPA thresholds and formats.

### 10. Automated Decision-Making Technology (ADMT)
- Both regimes address automated decision-making, but CPRA's ADMT rules (opt-out/access rights, pre-use notice for significant decisions) have their own regulatory definitions and triggers distinct from GDPR Article 22 — map your existing profiling/automated-decision inventory against the CPRA-specific rules rather than assuming Article 22 compliance suffices.

## Where the Two Laws Differ Most Significantly (Summary Table)

| Dimension | GDPR | CCPA/CPRA |
|---|---|---|
| Default posture | Opt-in (lawful basis required) | Opt-out (process by default, opt-out rights) |
| Territorial trigger | Processing data of EU data subjects | Revenue/volume/data-sale thresholds + doing business in CA |
| Core "special" concept | Special category data (Art. 9) | Sensitive personal information + Sale/Sharing constructs |
| Advertising data sharing | Requires consent (ePrivacy + GDPR) | Opt-out of "sale/sharing" + GPC signal honoring |
| Access/deletion timeline | 1 month (+2 month extension) | 45 days (+45 day extension) |
| Vendor relationship categories | Controller / Processor | Business / Service Provider / Contractor / Third Party |
| Non-discrimination | General principle | Explicit statutory right |
| Regulator | Data Protection Authorities (per member state) + EDPB | California Privacy Protection Agency (CPPA) + CA Attorney General |
| Private right of action | Limited (mainly via national implementing law) | Explicit for certain data breaches (statutory damages) |
| Minors | Parental consent under 16 (or lower per member state, min 13) for information society services | Opt-in required for sale/share of minors' data under 16; under-13 requires verifiable parental consent (COPPA-aligned) |
| Household concept | Not applicable | Applies in limited contexts (e.g., connected devices) |

## Practical Roadmap
1. **Gap-map** your existing GDPR RoPA/data inventory against CCPA's categories and confirm sale/share classifications for each data flow.
2. **Stand up** the opt-out/GPC infrastructure — this is usually the largest net-new technical lift.
3. **Draft California-specific notices** (notice at collection, CCPA privacy policy sections, SPI limitation notice if applicable).
4. **Update vendor contracts** with CCPA-specific clauses layered onto existing GDPR DPAs.
5. **Adjust rights-request workflows** for CCPA-specific timelines, verification tiers, and exceptions.
6. **Train staff** specifically on CCPA obligations, not just GDPR.
7. **Assess CPRA risk assessment/cybersecurity audit and ADMT applicability** given your processing activities, and confirm current CPPA regulatory thresholds.

## Bottom Line
Your GDPR program gives you the data governance foundation (inventory, security, breach response, vendor diligence culture), but CCPA/CPRA requires **new opt-out mechanics, California-specific notices, a different vendor contract framework, and distinct rights-request timelines/exceptions**. Treat CCPA/CPRA as a parallel compliance track that reuses your GDPR infrastructure rather than one that's automatically satisfied by it.

*This is general comparative guidance; consult counsel to confirm current CPPA regulatory requirements (especially risk assessment/audit/ADMT rules) and to tailor the gap analysis to your specific data flows.*
