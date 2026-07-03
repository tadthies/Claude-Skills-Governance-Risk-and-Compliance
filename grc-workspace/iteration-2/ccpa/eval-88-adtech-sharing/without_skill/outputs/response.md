# CCPA/CPRA: Ad Tech Platforms, Cookie IDs, and Sale/Sharing Obligations

## Is This a "Sale" or "Sharing" Under CCPA/CPRA?

### Short Answer

Yes — almost certainly both a "sale" and "sharing" under CCPA/CPRA. Sharing cookie IDs and browsing data with an ad tech platform for targeted advertising is the paradigmatic example that CPRA's "sharing" definition was specifically enacted to capture.

---

### Definitions Under CCPA/CPRA

**"Sale" (Cal. Civ. Code § 1798.140(ad)):**
A "sale" means selling, renting, releasing, disclosing, disseminating, making available, transferring, or otherwise communicating a consumer's personal information to a third party for monetary or other valuable consideration.

Cookie IDs and browsing data are personal information (they can be linked or reasonably linkable to a consumer or device). If you receive targeted advertising services in exchange for providing that data, the "other valuable consideration" prong is met — you are receiving advertising value (targeted impressions, audience optimization, reduced CPM waste) in exchange for the data. This has consistently been the California Attorney General's and the California Privacy Protection Agency's (CPPA) interpretation.

**"Sharing" (Cal. Civ. Code § 1798.140(ah)):**
CPRA added "sharing" as a separate, distinct category. "Sharing" means communicating personal information to a third party for cross-context behavioral advertising, whether or not for monetary or other valuable consideration. This is a technology-neutral definition that explicitly covers the free flow of data for behavioral advertising, so even if you argue there is no monetary exchange, the sharing definition still applies.

**Key takeaway:** You do not need to establish monetary consideration to trigger CPRA obligations — the cross-context behavioral advertising purpose alone is sufficient to constitute "sharing."

---

## Service Provider vs. Third Party: The Critical Distinction

### Why It Matters

If your ad tech platform qualifies as a **service provider**, disclosures to it are exempt from the sale/sharing definitions, you have no opt-out obligation, and you do not need a "Do Not Sell or Share" link for that relationship. If it is a **third party**, you must honor opt-out rights, respect GPC signals, and disclose the data relationship.

### Service Provider Requirements

To qualify as a service provider under CPRA (§ 1798.140(ag)), ALL of the following must be true:

1. **Written contract:** You must have a contract with the vendor that contains specific CCPA/CPRA-required terms.
2. **Business purpose limitation:** The vendor may only process the personal information for the specific business purposes listed in the contract — not for its own purposes.
3. **No selling or sharing:** The vendor is prohibited from selling or sharing the personal information it receives from you.
4. **No retaining, using, or disclosing for other purposes:** The vendor cannot retain, use, or disclose the data outside the service relationship or to combine it with data from other clients.
5. **No combining data across clients:** The vendor cannot combine the personal information it receives from you with data it receives from other businesses or collects from its own interactions with consumers, except as permitted (e.g., fraud prevention, security).

### Why Most Ad Tech Platforms Are Third Parties, Not Service Providers

Ad tech platforms — DSPs, DMPs, SSPs, pixel providers, retargeting networks, data clean rooms operating as ad exchanges — almost universally do not meet the service provider definition because their core business model depends on doing exactly what service providers are prohibited from doing:

- **They build cross-client audience profiles.** They combine data from hundreds or thousands of publishers and advertisers to build audience segments. This is combining data across clients — prohibited for service providers.
- **They use data for their own modeling.** Ad tech platforms use your visitors' browsing data to improve their own algorithms, audience models, and inventory pricing — not just to serve your ads.
- **They share data downstream.** In the programmatic advertising ecosystem, cookie IDs and bid-stream data flow to multiple parties (DSPs, ad exchanges, verification vendors). The platform is not acting solely on your behalf.
- **Their contracts do not restrict cross-client use.** Even when vendors label themselves "service providers" in their contracts or DPAs, if they actually combine data across clients, the contractual label is irrelevant — the CPPA evaluates actual data practices, not just contract language.

**Practical test:** Ask yourself — does this vendor use the data it gets from my website to build audiences, train models, or provide value to other clients? If yes, it is a third party, not a service provider.

**Common ad tech scenarios:**
| Platform Type | Service Provider? | Notes |
|---|---|---|
| Google Ads (conversion tracking only, no display targeting) | Potentially | Requires restricted data processing mode |
| Google Ads (audience targeting, display, remarketing) | No — Third Party | Cross-client data use |
| Meta Pixel (for conversion optimization, no Custom Audiences) | Potentially | Requires Limited Data Use flag |
| Meta Pixel (Custom Audiences, Lookalikes) | No — Third Party | Combines across Meta's graph |
| Trade Desk, DV360, Xandr | No — Third Party | Programmatic; cross-client profiling |
| Adobe Audience Manager / DMP | No — Third Party | Built for cross-client audience building |
| Criteo, AdRoll (retargeting) | No — Third Party | Cross-client network pools |
| Analytics-only (Google Analytics 4, configured correctly) | Potentially | Must disable advertising features |

---

## Opt-Out Obligations

### What CCPA/CPRA Requires

If you sell or share personal information with third parties (which, as established above, your ad tech platform almost certainly is), you must:

1. **Disclose the sale/sharing in your privacy policy.** Your privacy policy must include:
   - Categories of personal information sold or shared
   - Categories of third parties to whom the information is sold or shared
   - Consumer rights to opt out
   - How to submit an opt-out request

2. **Provide a "Do Not Sell or Share My Personal Information" link.** This link must be conspicuously placed on your homepage and any page where personal information is collected. The link can use the shorthand **"Do Not Sell or Share"** as of CPRA.

3. **Honor opt-out requests within 15 business days.** Once a consumer opts out, you must stop selling/sharing their data within 15 business days and instruct your third-party recipients to do the same.

4. **Do not re-engage an opted-out consumer for 12 months.** You cannot ask an opted-out consumer to consent to sale/sharing again for at least 12 months.

5. **Do not require account creation to opt out.** The opt-out mechanism must be available without requiring consumers to create an account.

### Technical Implementation of Opt-Out

When a consumer opts out of sale/sharing, you must stop passing their data to third-party ad platforms. Practically, this means:

- **Suppressing pixel fires** for opted-out users (conditional pixel loading based on consent state)
- **Not passing opted-out users' IDs** to ad tech platforms in server-side calls
- **Configuring platform-side controls:** Google's Restricted Data Processing (RDP) mode, Meta's Limited Data Use (LDU) flag, IAB U.S. Privacy String (CCPA) with opt-out signal
- **Maintaining an opt-out list** server-side so the suppression persists across sessions

---

## Global Privacy Control (GPC) Requirements

### What GPC Is

The Global Privacy Control (GPC) is a browser-level signal — a header (`Sec-GPC: 1`) or JavaScript property (`navigator.globalPrivacyControl === true`) — that consumers can set in their browser or extension to communicate opt-out preferences automatically without clicking a "Do Not Sell" link on each site.

### CPRA Requirements for GPC

CPRA **explicitly requires** businesses to honor the GPC signal as a valid opt-out of sale and sharing. Cal. Civ. Code § 1798.135(b) states that businesses must treat the GPC signal as a valid consumer request to opt out of the sale or sharing of personal information.

The CPPA has confirmed this in its enforcement priorities. Sephora was fined $1.2 million in 2022 partly for failing to honor GPC signals while claiming to not sell data.

### GPC Implementation Steps

1. **Detect the GPC signal** on your website. Check for the HTTP header `Sec-GPC: 1` on server-side requests or `navigator.globalPrivacyControl` in client-side JavaScript.

2. **Treat GPC as an opt-out.** If a user sends a GPC signal, treat them as having opted out of sale and sharing. You should not load third-party ad tech scripts for that user, or you must configure those scripts to operate in a data-restricted mode.

3. **Do not override GPC with a consent banner.** You cannot use a cookie consent banner to ask a GPC-signal user to "opt in" to sale/sharing. The GPC signal takes precedence for opt-out of sale/sharing (though it does not necessarily apply to all privacy rights — a consumer can still have a separate consent for a non-sale purpose).

4. **Log GPC compliance.** Maintain records of how GPC signals are detected and honored as part of your compliance documentation.

**Implementation example (JavaScript):**
```javascript
if (navigator.globalPrivacyControl) {
  // Do not load ad tech scripts
  // Set restricted data processing flags if already loaded
} else {
  // Load ad tech scripts normally (subject to other consent requirements)
}
```

---

## Practical Compliance Steps

### Step 1: Audit Your Ad Tech Stack

- List every vendor that receives cookie IDs, device IDs, or browsing behavior from your website
- For each vendor, determine: Does their contract meet service provider requirements? Do their actual data practices align with service provider restrictions?
- Classify each as service provider or third party based on actual practices, not just contract labels
- Request Data Processing Agreements (DPAs) or Service Provider Agreements (SPAs) with proper CPRA language from any vendor you want to claim as a service provider

### Step 2: Update Your Privacy Policy

Your privacy policy must accurately disclose:
- That you sell/share personal information (if you do)
- Categories of personal information: identifiers (cookie IDs, device IDs), internet or other electronic network activity (browsing history, interaction data)
- Categories of third parties: advertising networks, data analytics providers
- Consumer rights: right to opt out of sale/sharing, right to know, right to delete, right to correct, right to limit use of sensitive PI
- How to exercise rights (opt-out link, email, form)
- That you honor GPC signals

### Step 3: Implement a "Do Not Sell or Share" Mechanism

- Add a "Do Not Sell or Share My Personal Information" link to your website footer and homepage
- Build or integrate a preference center that records opt-out choices
- Store opt-out status server-side (do not rely solely on a cookie — consumers who clear cookies lose their opt-out, which is non-compliant)
- When a user opts out, suppress all data flows to third-party ad platforms for that user

### Step 4: Implement GPC Detection and Honoring

- Add GPC detection to your tag management system or directly in your website code
- Ensure that GPC-signal users are automatically treated as opted out of sale/sharing without requiring them to also click "Do Not Sell or Share"
- Test GPC detection using the GPC browser extension or a Brave browser (which sends GPC by default)

### Step 5: Configure Ad Tech Platform Controls

Even after opting a user out, ensure your ad tech platforms respect the opt-out:

- **Google:** Enable Restricted Data Processing (RDP) for California users (can be passed via gtag or the Ads Data Hub)
- **Meta:** Set Limited Data Use (LDU) flag for California users in your Meta Pixel base code
- **IAB CCPA Framework:** Implement the IAB U.S. Privacy String (`__uspapi`) and set the opt-out bit for opted-out users — many ad tech vendors read this string automatically
- **IAB TCF/GPP:** Consider implementing the IAB Global Privacy Platform (GPP) string, which is the evolving successor standard and supports multiple U.S. state privacy laws simultaneously

### Step 6: Contractual Remediation

- Review all ad tech vendor contracts and ensure they include required CCPA/CPRA terms
- For vendors you want to treat as service providers, ensure contracts prohibit cross-client data use and require them to flow down service provider obligations to sub-processors
- For vendors classified as third parties, your obligations are disclosure and opt-out — you cannot contractually convert a third party into a service provider if their actual practices do not comply

### Step 7: Respond to Consumer Requests

- Implement a process to receive and honor opt-out requests within 15 business days
- When you receive an opt-out request, notify your third-party recipients so they also stop using or selling the data
- Do not ask consumers to re-consent to sale/sharing within 12 months of opting out
- Train your customer service and privacy team on how to handle CCPA/CPRA rights requests

### Step 8: Document Your Compliance

- Maintain records of processing activities (ROPA equivalent for CCPA)
- Document how you detect and honor GPC signals
- Keep records of opt-out requests and how they were honored
- Conduct annual privacy policy reviews and update disclosures when your ad tech stack changes

---

## Applicability Threshold Reminder

CCPA/CPRA applies to for-profit businesses that:
- Do business in California (serving California residents is sufficient — you do not need a physical presence), AND
- Meet at least one of:
  - Annual gross revenues exceeding $25 million
  - Annually buys, sells, or shares personal information of 100,000 or more California consumers or households
  - Derives 50% or more of annual revenues from selling or sharing personal information

If you run any meaningful ad-supported website and are a for-profit entity, the 100,000 consumer threshold is very likely met — even if you are a small business. Cookie-based ad tech processes data from a very large number of visitors quickly.

---

## Summary Table

| Topic | Requirement |
|---|---|
| Classification | Almost certainly "sharing" (CPRA §1798.140(ah)); likely also "sale" |
| Ad tech platforms | Almost universally third parties, not service providers |
| Opt-out link | "Do Not Sell or Share My Personal Information" — required on homepage |
| GPC signal | Must be honored as automatic opt-out; cannot override with consent banner |
| Opt-out response time | 15 business days |
| Re-engagement moratorium | 12 months after opt-out |
| Privacy policy | Must disclose categories of PI, third parties, and consumer rights |
| Platform controls | Implement RDP (Google), LDU (Meta), IAB U.S. Privacy String |
| Contracts | Audit for service provider language; reclassify vendors as needed |
| Enforcement risk | High — CPPA has signaled ad tech as a priority enforcement area |
