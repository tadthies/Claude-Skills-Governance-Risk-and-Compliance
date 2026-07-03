# From GDPR to CCPA/CPRA: What You Still Need to Add

## Good News First

GDPR is generally the more demanding law, and a mature GDPR program already covers most of what CCPA/CPRA requires:
- Privacy notices (at-collection and policy-level)
- Data subject/consumer rights processes (access, delete, correct, portability)
- Processor agreements (map closely to service provider/contractor contracts)
- Data minimization and purpose limitation
- Retention schedules
- Security measures

You are not starting from zero. But CCPA/CPRA has several **US-specific mechanics that GDPR doesn't require**, and those gaps are exactly where enforcement has landed in 2026 (Disney $2.75M, PlayOn $1.1M, Ford $375K). Below is the concrete punch list.

## CCPA/CPRA-Specific Additions You Need

### 1. "Do Not Sell or Share My Personal Information" Link + Opt-Out Workflow
GDPR has no direct equivalent to CCPA's "sale"/"sharing" concept or the opt-out model — GDPR relies on consent/legitimate-interest mechanisms instead. You need:
- A prominent link on your homepage and in your privacy policy
- A workflow that updates your consent/preference platform within **15 business days** of an opt-out
- Propagation of the opt-out to all service providers/contractors involved in sale/sharing
- A rule not to re-solicit consent from an opted-out consumer for **12 months**

If you engage in any cross-context behavioral advertising (passing cookie IDs/browsing data to ad exchanges or ad tech partners), that's "sharing" under CPRA even without payment — this needs opt-out coverage regardless of whether you'd call it a "sale."

### 2. Honor Global Privacy Control (GPC) Signals
The CPPA has confirmed GPC must be treated as a valid opt-out, equivalent to a manual click on the "Do Not Sell or Share" link. GDPR/ePrivacy frameworks don't have a precise equivalent requirement in the same form. No separate identity verification is needed to act on GPC — only reasonable confirmation the requester is the consumer.

### 3. "Limit the Use of My Sensitive Personal Information" Link + 15-Day Workflow
GDPR requires **explicit consent** for special category data upfront (opt-in model). CCPA/CPRA instead uses an **opt-out model** for Sensitive Personal Information (SPI) via the right to limit — a structurally different mechanism, so your GDPR consent flows won't automatically satisfy this.

SPI categories under CPRA: SSN/government ID, financial account credentials, precise geolocation (within 1/4 mile), racial/ethnic origin, religious beliefs, union membership, contents of communications, genetic data, biometric data, health/medical information, sexual orientation.

You need:
- A "Limit the Use of My Sensitive Personal Information" link (can be combined with the sale/share opt-out link)
- Processing of limitation requests within **15 business days**
- Restriction of SPI use to only the permitted purposes (service delivery, security, short-term/transient use, quality verification, etc.) once a consumer exercises this right
- Propagation to service providers/contractors

### 4. Confirm Vendor Classification Maps Correctly
Your GDPR "processors" need to be re-evaluated specifically against CCPA's **service provider** and **contractor** definitions:
- Service Provider: processes PI under contract restricting use to your specified business purpose — not a sale
- Contractor (CPRA addition): similar restriction, must additionally certify compliance
- Third Party: anyone who doesn't meet either bar — disclosure to them may be a sale/sharing

A GDPR-compliant DPA (Art. 28) doesn't automatically satisfy the CCPA service-provider contract requirements — check for purpose limitation, prohibition on further sale/sharing, consumer-request cooperation obligations, audit rights, and deletion obligations specifically. Mismatches here (contract says "service provider," data flow says "third party") are a very common gap-assessment finding.

### 5. Minors' Opt-In for Sale/Sharing
CCPA/CPRA requires **opt-in consent** for the sale/sharing of minors' PI (consumers under 16), with parental consent required under 13. GDPR's age-of-consent rules vary by EU member state (13–16) and apply to a different trigger (processing based on consent generally, not sale/sharing specifically) — so this needs a distinct compliance check if you serve any California minors.

### 6. Financial Incentive / Loyalty Program Disclosures
If you run loyalty programs, discounts, or other incentives in exchange for PI, CCPA/CPRA requires specific disclosures: the incentive must be reasonably related to the value of the PI, require opt-in consent with a clear description of material terms, and allow withdrawal at any time. GDPR doesn't have a directly equivalent structured framework for this.

### 7. Annual Reconfirmation of the Three Business Thresholds
CCPA/CPRA applicability is threshold-based (unlike GDPR, which applies regardless of size):
- Revenue exceeds $25 million, OR
- Buys/sells/receives/shares PI of 100,000+ consumers/households annually, OR
- 50%+ of revenue derived from selling/sharing PI

Reassess these annually — GDPR has no equivalent applicability test to maintain.

### 8. Cybersecurity Audits and Risk Assessments (effective January 1, 2026 — already live)
CPRA now requires **annual cybersecurity audits** and **documented risk assessments** for any processing that presents significant risk to consumers, submittable to the CPPA on request. These regulations are live as of this year. While GDPR has its own risk-based obligations (DPIAs under Art. 35), the CCPA versions have distinct scope, documentation, and audit requirements — don't assume your DPIA process automatically satisfies this.

### 9. ADMT Opt-Out (deadline January 1, 2027)
If you use automated decision-making producing legal or similarly significant effects (employment, credit, housing, insurance, education decisions), CPPA's ADMT regulations (effective January 1, 2026) require an opt-out mechanism, disclosure of the automated logic, and a human review option, with a compliance deadline of **January 1, 2027**. GDPR Art. 22 covers similar ground but with different mechanics (right not to be subject to solely automated decisions) — treat this as a parallel build, not a reuse of your GDPR Art. 22 process.

## Where the Two Laws Differ Most Significantly

| Dimension | GDPR | CCPA/CPRA |
|---|---|---|
| **Applicability** | Any org processing EU personal data, no size threshold | Threshold-based ($25M revenue / 100K+ consumers / 50%+ revenue from PI sale) |
| **Lawful basis** | Requires one of six lawful bases before processing | No lawful basis requirement for most processing |
| **Model for consent** | Primarily opt-in (freely given, specific, informed) | Primarily opt-out (consumer must affirmatively act) |
| **Sale/sharing concept** | No equivalent | Central concept driving the opt-out link and GPC obligations |
| **Cross-border transfers** | Restricted — requires adequacy decision or transfer mechanism (SCCs, BCRs) | No transfer restriction mechanism |
| **Penalties** | Up to €20M or 4% of global annual turnover, no formal cure period in most cases | $2,500 (unintentional) / $7,500 (intentional) per violation, with a 30-day AG cure period |
| **Private right of action** | Limited, varies by member state | Limited to data breaches only: $100–$750 per consumer per incident |

## Recommended Sequence
1. Run a vendor reclassification exercise (service provider/contractor/third party) against your existing GDPR processor list
2. Stand up the "Do Not Sell or Share" and "Limit SPI" links, wired to a 15-business-day workflow, with GPC signal detection
3. Confirm your three-threshold applicability determination and document it
4. Scope and schedule your first cybersecurity audit and risk assessment if your processing carries significant risk
5. Build the minors' opt-in flow if you have any California users under 16
6. Start ADMT opt-out design now, targeting the January 1, 2027 deadline

---
*This is general compliance guidance, not legal advice. Consult qualified counsel for your specific circumstances.*
