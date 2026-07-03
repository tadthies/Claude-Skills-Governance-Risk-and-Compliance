# CCPA/CPRA Compliance: Ad Tech Platforms, Cookie IDs, and Browsing Data

## Short Answer

Yes — passing your website visitors' cookie IDs and browsing data to an ad tech platform to serve targeted ads almost certainly constitutes both **"sharing"** under the CPRA and likely a **"sale"** under the CCPA/CPRA. You have specific legal obligations to fulfill, starting immediately.

---

## 1. This Is "Sharing" Under the CPRA

The CPRA (effective January 1, 2023) added the concept of **"sharing"** to California privacy law precisely to capture the ad tech use case you describe.

**Definition of "sharing" (Cal. Civ. Code § 1798.140(ah)):**
> Disclosing, selling, renting, releasing, disseminating, making available, transferring, or otherwise communicating orally, in writing, or by electronic or other means, a consumer's personal information by the business to a third party for cross-context behavioral advertising, whether or not for monetary or other valuable consideration.

Your fact pattern maps directly onto this definition:

- **"Disclosing… personal information"** — Cookie IDs and browsing data are personal information under the CCPA (§ 1798.140(v)). Cookie IDs are specifically enumerated as unique personal identifiers. Browsing history is explicitly listed as a category of personal information.
- **"To a third party"** — Unless the ad tech platform qualifies as a service provider or contractor (addressed below), it is a third party.
- **"For cross-context behavioral advertising"** — Serving targeted ads based on a consumer's activity across different websites, apps, or contexts is the textbook definition of cross-context behavioral advertising (§ 1798.140(k)).
- **"Whether or not for monetary or other valuable consideration"** — This is the key CPRA innovation. Even if you pay the ad tech platform (rather than receive payment), sharing still occurs. Money does not have to change hands in any particular direction.

**Conclusion on sharing:** The disclosure of cookie IDs and browsing data to an ad tech platform for behavioral targeting is sharing, full stop.

---

## 2. This Is Also Likely a "Sale"

In addition to sharing, the same activity may independently constitute a **"sale"** under § 1798.140(ad), which covers disclosures for "monetary **or other valuable consideration**."

The "valuable consideration" element is interpreted broadly. Ask yourself whether the ad tech platform provides any of the following in exchange for receiving your visitors' data:

- **Access to advertising inventory** (your ads run on their network or on publisher sites they control)
- **Data enrichment or audience insights** (they append demographic or behavioral attributes to your customer records)
- **Reduced platform fees** (your use of their platform is subsidized by the data you contribute)
- **Audience matching or lookalike modeling** (they use your visitors' data to improve targeting across other advertisers)
- **Attribution reporting** (they tell you which ads led to conversions using data collected about your visitors)

If the answer to any of these is yes — and it almost always is in a typical ad tech relationship — the exchange meets the "valuable consideration" threshold and constitutes a sale in addition to sharing.

The California Attorney General and the CPPA have taken the position that the modern ad tech ecosystem is structured precisely so that publishers and advertisers provide data as consideration for services, making most standard ad tech integrations sales under the statute.

---

## 3. Your Legal Obligations: The "Do Not Sell or Share" Link and GPC

Because this activity constitutes sharing (and likely a sale), California law imposes mandatory opt-out rights and disclosure requirements.

### 3a. "Do Not Sell or Share My Personal Information" Link

You must post a clear and conspicuous link titled **"Do Not Sell or Share My Personal Information"** on your homepage (and in your privacy policy). This is required by § 1798.135(a)(1).

- The link must be on the homepage of your website and any mobile app.
- It must lead to a page or mechanism through which consumers can submit an opt-out request.
- The link text must be exactly "Do Not Sell or Share My Personal Information" or an approved equivalent. You may combine the sale and sharing opt-out into a single link.
- You may use an opt-out preference signal (GPC) in lieu of — or in addition to — the link mechanism.

### 3b. Honoring Global Privacy Control (GPC) Signals

This is a hard legal requirement many businesses overlook. Under § 1798.135(b), if a consumer's browser or device sends a **Global Privacy Control signal**, you must treat it as a valid opt-out of both sale and sharing of that consumer's personal information, effective immediately upon receipt.

Practically, this means:

- Your website must detect incoming GPC signals (a standard HTTP header: `Sec-GPC: 1`).
- When a GPC signal is detected, you must **not** send that visitor's PI to the ad tech platform in a way that constitutes a sale or sharing.
- You cannot require the consumer to separately submit an opt-out request — GPC alone is sufficient.
- The CPPA has stated that businesses that fail to honor GPC are in violation of the CCPA/CPRA. The AG has already cited GPC non-compliance in enforcement actions.

---

## 4. Third Party vs. Service Provider: The Classification Problem

The classification of your ad tech platform is critical. If it qualifies as a **service provider**, the disclosure is not a sale or sharing. If it is a **third party**, it is.

### Service Provider Requirements (§ 1798.140(ag))

For an ad tech platform to qualify as a service provider, you must have a written contract with it that:

1. **Prohibits the service provider from selling or sharing the PI it receives from you.**
2. **Prohibits retaining, using, or disclosing the PI for any purpose other than performing the services specified in the contract** — including for the service provider's own commercial purposes.
3. **Prohibits combining the PI received from you with PI received from other sources**, except as permitted by narrow exceptions.
4. Includes a certification that the service provider understands and will comply with these restrictions.

### The Problem With Ad Tech Platforms

Standard ad tech platforms almost never qualify as service providers because their business model depends on doing exactly what the service provider definition prohibits:

- They use your visitors' data to build audience profiles that serve other advertisers.
- They combine your data with data from across their network (other publishers, data brokers, identity graphs).
- They sell or license audience segments derived from your visitors' data.
- Their contracts typically include broad licenses to use data for "improving their services" — which the CPPA has indicated can take them outside the service provider definition.

Even if a contract contains the required service provider language on its face, if the platform's actual practices involve using your visitors' data for its own targeting network, attribution modeling, or audience extension, the CPPA can look through the contract to the actual data flows and reclassify the relationship.

**Practical test:** Does the ad tech platform use your visitors' data in any way that benefits the platform beyond performing the specific service you contracted for? If yes, it is a third party, not a service provider, and the disclosure is a sale and/or sharing.

---

## 5. Practical Steps You Must Take

### Step 1: Audit Your Ad Tech Contracts

Review every contract with ad tech vendors. Determine whether it contains the required service provider restrictions. If it does not, the vendor is a third party and you are currently engaged in unnoticed sale/sharing of PI.

### Step 2: Update Your Privacy Policy

Your privacy policy must:
- Disclose that you sell and/or share personal information (and describe the categories sold/shared).
- Identify the categories of third parties to whom you sell or share PI (e.g., advertising networks, analytics providers).
- Describe the opt-out rights available to California consumers.
- Include a link or instructions for submitting a Do Not Sell or Share request.

Failure to disclose sale/sharing in your privacy policy is a separate violation from failing to provide the opt-out link.

### Step 3: Implement a Consent Management Platform (CMP)

To operationalize opt-out rights and GPC compliance, implement a CMP that:
- Detects GPC signals and automatically suppresses PI transmission to ad tech vendors for those visitors.
- Stores opt-out preferences and persists them across sessions.
- Integrates with your tag management system (Google Tag Manager, Tealium, etc.) to conditionally fire or suppress ad tech tags based on consent status.
- Provides a mechanism for consumers to submit opt-out requests manually (for browsers without GPC support).

### Step 4: Configure Ad Tech Platforms to Respect Opt-Outs

For consumers who have opted out (either via GPC or manual request):
- Do not load ad tech scripts or pixels that transmit cookie IDs or browsing data.
- Do not pass cookie IDs or browsing data server-side (if using server-side tagging).
- If the platform has a consent mode or restricted data processing mode, enable it — but recognize this may not fully eliminate the sale/sharing if the platform still receives any PI.
- The safest approach for opted-out consumers: do not send any PI to the ad tech platform at all.

### Step 5: Post the Required Link

Add the "Do Not Sell or Share My Personal Information" link to the footer of every page of your website (not just the homepage, as a best practice, though the statute requires it on the homepage). The link must be conspicuous — same size and style as similar links on the page, not hidden in small print.

### Step 6: Honor Opt-Outs Within 15 Business Days

Once a consumer submits an opt-out request (or you detect a GPC signal), you must stop the sale or sharing of their PI within **15 business days** (§ 1798.135(c)). Document your process for ensuring this timeline is met.

---

## Summary of Key Points

| Issue | Conclusion |
|---|---|
| Passing cookie IDs + browsing data to ad tech for targeted ads | Constitutes "sharing" under CPRA regardless of money changing hands |
| Ad tech providing inventory access, enrichment, or other value | Also constitutes "sale" under CCPA/CPRA |
| Ad tech platform classification | Likely a "third party," not a service provider, unless contract prohibits ALL other uses |
| Required disclosures | "Do Not Sell or Share My Personal Information" link on homepage |
| GPC signals | Must be honored as valid opt-outs — no separate request required from consumer |
| Timeframe to comply with opt-out | 15 business days from receipt of request or GPC signal |
| Privacy policy update required | Yes — must disclose categories of PI sold/shared and identify third party categories |

---

## Bottom Line

Your current ad tech integration is almost certainly a sale and sharing of personal information under California law. You should treat it as such immediately. The required steps — posting the opt-out link, honoring GPC signals, updating your privacy policy, and configuring your CMP to suppress PI transmission for opted-out consumers — are not optional. The CPPA has demonstrated willingness to pursue enforcement actions for exactly this type of ad tech non-compliance, and violations can carry penalties of up to $7,500 per intentional violation.

Engage legal counsel with CCPA/CPRA expertise to review your specific ad tech contracts and data flows, as the service provider analysis is highly fact-specific and the stakes for misclassification are significant.
