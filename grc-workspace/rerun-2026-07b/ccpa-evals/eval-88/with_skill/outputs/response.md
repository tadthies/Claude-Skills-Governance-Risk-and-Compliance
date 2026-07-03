# Is Passing Cookie IDs/Browsing Data to Your Ad Tech Platform a "Sale" or "Sharing"?

## Short Answer

**Almost certainly yes — this is "sharing" under CPRA, and it may also independently qualify as a "sale."** Either classification triggers the same core obligation: you must offer consumers an opt-out and honor it.

## Why This Qualifies

### It's "Sharing" (CPRA-specific concept)
"Sharing" is defined as disclosing PI to a third party for **cross-context behavioral advertising** — using data collected in one context to serve targeted ads in another context — **even without any monetary payment changing hands**. Passing cookie IDs and browsing data to an ad tech platform to serve targeted ads is the textbook example of cross-context behavioral advertising. The skill's guidance is direct on this point: "any pipeline that passes PI (cookie IDs, device fingerprints, hashed emails, IP addresses) to ad exchanges, DMPs, or ad tech partners for cross-context behavioral advertising is 'sharing' even absent monetary payment, and must be covered by the opt-out mechanism."

### It May Also Be a "Sale"
"Sale" is defined broadly as disclosure of PI to a third party for **monetary or other valuable consideration**. If your ad tech platform provides value in return for receiving this data — better ad rates, free/discounted ad services, revenue share, or any other non-cash benefit — this could independently qualify as a sale. Given how broadly "valuable consideration" is interpreted, you should assume this analysis applies unless your ad tech relationship is a pure vendor arrangement (fee-for-service, no data monetization by the vendor) under a contract that meets the service provider criteria below.

### Ruling Out the Service Provider Exception
The disclosure would NOT be a sale/sharing only if the ad tech platform qualifies as a **Service Provider** or **Contractor** — meaning it processes the PI *solely* on your behalf, under a written contract that prohibits it from using the data for any purpose beyond the specific business purpose you've defined (i.e., it can't use your visitor data to build its own audience profiles or serve ads for other clients).

In practice, most third-party ad exchanges, demand-side platforms (DSPs), and ad networks fail this test because their business model depends on aggregating data across multiple clients' websites to build cross-site behavioral profiles. If your ad tech platform:
- Uses the data only to serve your ads back to your own visitors, under contractual restriction, and doesn't repurpose it — it might qualify as a service provider
- Uses the data to build audience segments, enrich its own data assets, or serve ads across other advertisers' inventory — it is a **third party**, and the disclosure is sharing (and likely a sale)

You should pull the actual contract with this ad tech platform and check for: purpose limitation language, a prohibition on the vendor's independent use of the data, deletion obligations, and audit rights. If those aren't present, the vendor defaults to "third party" status regardless of what either side calls the relationship — contractual labels don't override actual data flows and actual contract terms.

## What You Need to Do

### 1. Confirm and Document the Classification
Formally document whether this ad tech relationship is a sale, sharing, or both. Don't leave this informal — a mismatch between assumed classification and actual data flow is a common (and costly) gap-assessment finding, and it's exactly the kind of issue that surfaced in the Disney enforcement action ($2.75M, the largest CCPA fine to date), which specifically cited **third-party ad tech data sharing** and **opt-out mechanism deficiencies**.

### 2. Add/Verify the "Do Not Sell or Share My Personal Information" Link
This link must be prominently placed on your homepage and referenced in your privacy policy. If you don't already have one, this is now a required control, not optional.

### 3. Honor Global Privacy Control (GPC) Signals
The CPPA has confirmed that GPC must be honored as a valid opt-out — equivalent to a consumer manually clicking your opt-out link. If your ad tech integration doesn't currently check for and respect GPC signals before firing tracking pixels/cookies, this is a gap. No separate identity verification is required to act on a GPC signal — only reasonable confirmation the requester is the consumer (which the browser signal itself effectively provides).

### 4. Build the Opt-Out Propagation Workflow

| Step | Action |
|---|---|
| 1 | Consumer opts out via link, form, or GPC signal |
| 2 | No identity verification required beyond reasonable confirmation |
| 3 | Update your consent/preference management platform within **15 business days** |
| 4 | Propagate the opt-out instruction to the ad tech platform so it stops receiving this consumer's cookie ID/browsing data |
| 5 | Do not re-solicit consent from this consumer for **12 months** |

Technically, this usually means suppressing the ad tech pixel/tag or cookie sync for opted-out users at the tag-management or consent-management-platform (CMP) layer before any data reaches the ad tech vendor — not just labeling the data "opted out" after the fact.

### 5. Update Your Privacy Policy and At-Collection Notice
Disclose that PI is shared with third parties for cross-context behavioral advertising, name the categories of third parties involved (ad tech/advertising partners), and describe the opt-out mechanism.

### 6. Update or Re-Negotiate the Vendor Contract
If you want to argue the ad tech platform is a service provider (avoiding sale/sharing classification), the contract needs explicit purpose-limitation language prohibiting the vendor from using your visitor data for any purpose other than serving your ads, plus deletion and audit rights. If the vendor's business model won't accept those terms (common with major ad exchanges/DSPs), you should assume third-party/sale-sharing treatment and build your opt-out accordingly rather than relying on a contractual fix that doesn't reflect reality.

### 7. First-Party Analytics Carve-Out
If you separately use first-party analytics tools that do **not** disclose PI to third parties, those are typically unaffected by this analysis — the concern here is specifically about disclosure to the external ad tech platform, not internal measurement.

## Bottom Line
Treat this data flow as "sharing" (and potentially "sale") now, stand up the opt-out link and GPC honoring, and audit the vendor contract for service-provider-qualifying language. Given the direct precedent in the Disney enforcement action for nearly this exact fact pattern, this is a near-term priority, not a lower-tier gap.

---
*This is general compliance guidance, not legal advice. Consult qualified counsel for your specific circumstances.*
