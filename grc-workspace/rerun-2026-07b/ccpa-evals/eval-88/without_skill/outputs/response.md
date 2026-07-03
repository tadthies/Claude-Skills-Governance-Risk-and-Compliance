# Does Ad Tech Data Sharing Constitute a "Sale" or "Sharing" Under CCPA/CPRA?

## Short Answer

**Very likely yes — this almost certainly qualifies as "sharing" (and potentially also a "sale") under CPRA.** Sending cookie IDs and browsing data to an ad tech platform for targeted/cross-context behavioral advertising is the textbook scenario the CPRA's "sharing" concept was created to capture.

## Understanding the Definitions

### "Sale"
Under CCPA/CPRA, a "sale" is broadly defined as selling, renting, releasing, disclosing, disseminating, making available, transferring, or otherwise communicating a consumer's personal information to a third party **for monetary or other valuable consideration**. "Other valuable consideration" has been interpreted broadly — it doesn't require a direct cash payment. If you receive reciprocal advertising services, analytics, or any benefit in exchange for the data flow, this can qualify as a sale.

### "Sharing" (CPRA-added concept)
CPRA introduced "sharing" specifically to close a loophole: many ad tech arrangements didn't involve a traditional "sale" (no money changed hands) but still resulted in cross-context tracking. "Sharing" means disclosing or making available a consumer's personal information to a third party for purposes of **cross-context behavioral advertising** (i.e., targeted advertising based on the consumer's activity across businesses, distinctly-branded websites, applications, or services), whether or not for monetary consideration.

### Your Scenario
Sending cookie IDs and browsing data to an ad tech platform so it can serve **targeted ads** is a paradigm example of cross-context behavioral advertising. This means:

- It almost certainly constitutes **"sharing"** — regardless of whether money changes hands.
- It may also constitute a **"sale"** if there's any valuable consideration flowing back to you (e.g., free/discounted ad services, audience insights, revenue share).

The distinction matters less for compliance purposes than you'd think, because CCPA/CPRA requires you to offer opt-out rights for **both** sales and sharing, and the same "Do Not Sell or Share" mechanism covers both.

## Key Exception to Check: Service Provider Relationship

If the ad tech vendor is acting strictly as your **service provider** — processing data solely on your behalf, under a compliant contract, and not using the data for its own independent purposes (including not using it to serve ads to its other clients based on your data, and not combining your data with data from other sources) — then the transfer might not count as a sale/share.

However, in practice, most ad tech/adtech networks (DSPs, ad exchanges, retargeting platforms, social media ad pixels like Meta/Google ads) **do** use the data for their own purposes (building cross-site profiles, improving their ad models, serving ads across their network) — which disqualifies them from service-provider status and confirms this is a sale/share, not an internal processing arrangement. Carefully audit your specific contract and the vendor's actual data use — don't rely on the vendor's marketing claims alone.

## What You Need to Do

### 1. Update Your Privacy Policy
- Disclose the categories of personal information shared/sold (e.g., identifiers, internet/network activity information).
- Disclose the categories of third parties (ad tech/advertising networks) receiving this data.
- Disclose the business/commercial purpose (cross-context behavioral/targeted advertising).

### 2. Provide "Do Not Sell or Share My Personal Information" Opt-Out
- A clear and conspicuous link on your homepage (and app, if applicable) titled **"Do Not Sell or Share My Personal Information"** (or "Your Privacy Choices" using the recognizable CPPA-approved opt-out icon, if you combine multiple choices into one link).
- This must be a simple, functional mechanism — no dark patterns, no requiring account creation or login just to opt out.

### 3. Honor Global Privacy Control (GPC) Signals
- California regulations require businesses to treat a **Global Privacy Control** browser/device signal as a valid opt-out-of-sale/sharing request, automatically, without requiring additional steps from the consumer.
- Your ad tech/tag management setup needs to detect GPC signals and suppress the relevant tags/pixels (or instruct the platform not to use the data for targeted ads) for opted-out users in real time.

### 4. Implement Notice at Collection
- At or before the point of collection (e.g., when cookies are set), disclose that browsing/cookie data may be sold/shared for advertising purposes and link to your opt-out mechanism.

### 5. Contractual Requirements
- If treating the ad tech vendor as a **third party** (not a service provider), CPRA still requires a **written contract** that includes required terms: the third party must comply with applicable CCPA obligations, provide the same level of privacy protection, and you must have the right to take reasonable steps to ensure they use the data lawfully.
- If you're relying on **service-provider** classification, your contract needs specific CCPA-mandated restrictions (no use outside the specified business purpose, no combining with other clients' data, no independent use, deletion/return obligations, audit rights, sub-processor flow-down).

### 6. Sensitive Personal Information Considerations
- If cookie/browsing data reveals precise geolocation or other SPI categories, additional "Limit the Use of My Sensitive Personal Information" obligations may also apply.

### 7. Minor Protections
- If you have actual knowledge a consumer is under 16, opt-in consent (not just opt-out) is required before selling or sharing their data — verify your ad tech integration excludes or gates minors appropriately.

### 8. Vendor Due Diligence
- Confirm with your ad tech vendor whether they're operating as a service provider or a third party under your contract, and whether they in turn share data with other advertisers/exchanges (which would reinforce third-party/sale-share classification).
- Ask for their CCPA compliance representations and indemnification terms.

## Bottom Line
Treat this integration as a "sale/sharing" relationship: update your privacy policy, stand up a compliant opt-out mechanism (including GPC honoring), execute a CCPA-compliant contract with the ad tech vendor, and ensure notice-at-collection covers this use. Don't rely on labeling the vendor a "service provider" unless your contract and their actual practices genuinely restrict them from independent use of the data — this is a common area of regulatory scrutiny and enforcement.

*This is general compliance guidance; the service-provider vs. third-party analysis is fact-specific and benefits from a contract and technical-flow review by counsel or a privacy professional.*
