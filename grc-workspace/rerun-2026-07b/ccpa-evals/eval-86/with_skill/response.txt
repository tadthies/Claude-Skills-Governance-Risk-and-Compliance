# CCPA/CPRA Applicability Analysis

## Short Answer

**Yes, you are almost certainly subject to CCPA/CPRA.** Your $30M annual revenue alone exceeds the $25 million threshold, which is enough on its own to trigger coverage — you don't even need to look at the data-volume test, though it's worth confirming for completeness.

## Step 1: Confirm Entity Type

CCPA/CPRA applies to **for-profit businesses** doing business in California. As a US-based e-commerce company selling to California customers, you meet this threshold.

## Step 2: Test the Three Thresholds (only one needs to be met)

| # | Threshold | Your Numbers | Met? |
|---|---|---|---|
| 1 | Annual gross revenue exceeds **$25 million** | $30M | **Yes** |
| 2 | Buys, sells, receives, or shares PI of **100,000+** consumers/households annually | ~80,000 CA customers/year | No (on its own — but note this counts *all* consumers/households, not just California ones, and any data brokering activity could push you over) |
| 3 | **50%+** of annual revenue from selling/sharing consumers' PI | Not indicated — assume no, as an e-commerce business | Likely No |

Because you meet Threshold #1 (revenue), you are a covered business under CCPA/CPRA regardless of the outcome of the other two tests.

## Core Obligations Now That You're Covered

### 1. Classify Your Data Recipients
Before anything else, map every third party, vendor, and platform you share customer PI with (payment processors, shipping providers, email marketing tools, analytics, ad tech) and classify each as:
- **Service Provider** — processes PI under contract restricting use to your specified business purpose; not a sale
- **Contractor** (CPRA) — similar restriction, must certify compliance; not a sale
- **Third Party** — anyone else; disclosure to them may constitute a "sale" or "sharing"

A mismatch between what your contracts say and what your data flows actually do is one of the most common gap-assessment findings — worth auditing now.

### 2. Build Consumer Rights Fulfillment Processes
You must be able to honor, within **45 days** (extendable once by 45 days):
- **Right to Know** — specific pieces and categories of PI collected, sources, purposes, and third parties it was disclosed to
- **Right to Delete** — delete PI and direct service providers/contractors to do the same (subject to standard exceptions)
- **Right to Correct** — correct inaccurate PI
- **Right to Opt-Out of Sale/Sharing** — immediate effect, propagated to vendors within 15 business days
- **Right to Limit SPI** (if applicable) — 15 business days
- **Right to Non-Discrimination** — can't penalize customers for exercising rights

Identity verification: 2 data-point match for standard requests; 3 data points + signed declaration for sensitive/financial data requests.

### 3. Provide Required Intake Channels
At least two methods for submitting requests (e.g., a web form and an email address; online-only businesses can use email as one channel).

### 4. Publish Required Notices
- **Privacy notice at collection** — categories collected, purposes, whether PI is sold/shared, retention periods
- **Privacy policy** — updated annually, covering categories of PI, purposes, third-party disclosures, consumer rights, and contact info
- **"Do Not Sell or Share My Personal Information" link** on your homepage — required if you engage in any sale or sharing (check your ad tech and marketing pixels; cross-context behavioral advertising counts as "sharing" even without payment)
- Honor **Global Privacy Control (GPC)** signals as a valid opt-out

### 5. Update Vendor Contracts
Contracts with service providers/contractors must include purpose limitations, a prohibition on further sale/sharing, an obligation to comply with consumer requests, audit rights, and deletion obligations.

### 6. Cybersecurity Audits & Risk Assessments (new as of Jan 1, 2026)
If your processing of PI presents "significant risk" to consumers (this determination itself should be documented), you now need:
- **Annual cybersecurity audits** (regulations effective January 1, 2026)
- **Documented risk assessments** before processing that carries significant risk, available to the CPPA on request

Given that e-commerce inherently involves payment data, browsing/behavioral tracking, and potentially ad tech sharing, you should assume this obligation applies and scope an audit now rather than wait for a CPPA inquiry.

### 7. Prepare for ADMT Obligations (deadline Jan 1, 2027)
If you use automated decision-making (e.g., automated fraud scoring, personalized pricing, or credit-like decisions) that produces legal or similarly significant effects, you'll need an opt-out mechanism, disclosure of the logic, and a human review option by January 1, 2027.

## Practical Next Steps
1. Document your threshold determination (revenue-based) and reassess annually
2. Conduct a data-mapping exercise covering all vendors that touch CA customer PI
3. Classify every vendor as service provider / contractor / third party and reconcile against actual data flows
4. Stand up (or verify) your two-plus-channel request intake process and 45-day response workflow
5. Audit your website for the "Do Not Sell or Share" link and GPC honoring — this is a frequent, cheap enforcement target (see Disney's $2.75M penalty, which included opt-out mechanism deficiencies)
6. Scope whether a cybersecurity audit and risk assessment are required given your data processing profile
7. Update your privacy policy and at-collection notices to reflect all CPRA-required disclosures

## Penalty Exposure If You Don't Act
- Unintentional violations: up to $2,500 per violation
- Intentional violations: up to $7,500 per violation
- A 30-day cure period applies to AG actions
- Private right of action exists for data-breach scenarios ($100–$750 per consumer per incident), so reasonable security measures are not optional

Given your revenue tier and consumer volume, you're squarely within the range where the CPPA and AG have pursued enforcement in 2026 (e.g., Ford's $375K penalty was specifically for missing access/deletion deadlines) — the fundamentals (rights fulfillment timelines, opt-out mechanisms, vendor contracts) should be treated as immediate priorities, not a future project.

---
*This is general compliance guidance, not legal advice. Consult qualified counsel for your specific circumstances.*
