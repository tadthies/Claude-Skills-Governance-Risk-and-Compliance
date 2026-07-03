# Precise Geolocation, Health/Wearable Data, and Biometric Facial Recognition Under CPRA

## Classification: This Is All Sensitive Personal Information (SPI)

All three data types you describe fall squarely within CPRA's **Sensitive Personal Information** category, and each independently triggers heightened obligations:

| Data Type | SPI Category | Notes |
|---|---|---|
| **Precise geolocation** | Precise geolocation (within 1/4 mile) | Triggers SPI status specifically because of the *precision* — coarse/approximate location (e.g., city-level) is not SPI |
| **Health metrics from wearable integration** | Health/medical information | Any physiological or health-related data synced from a wearable qualifies |
| **Biometric facial recognition for authentication** | Biometric data used to uniquely identify a person | Facial recognition used for identity verification is a textbook example — this is the clearest-cut SPI category of the three |

Because you're collecting **multiple, high-sensitivity SPI categories simultaneously**, this app should be treated as presenting **significant risk** to consumers for purposes of the CPRA risk-assessment and cybersecurity-audit obligations (see below) — this combination (precise location + health + biometric identity data) is exactly the kind of profile regulators scrutinize most closely.

## Special Obligations That Apply

### 1. Right to Limit Use of Sensitive Personal Information (§1798.121)
Consumers have the right to restrict your use of this SPI to only the "permitted purposes" listed below. You must:
- Provide a **"Limit the Use of My Sensitive Personal Information"** link (can be combined with your "Do Not Sell or Share" link) — likely within the app itself given this is a mobile-first product, plus on your website/privacy policy
- Process limitation requests within **15 business days**
- No identity verification required beyond reasonable confirmation of consumer identity
- Propagate the limitation instruction to any service providers/contractors who touch this data (e.g., your wearable-integration vendor, cloud biometric processing vendor, analytics providers)

**Permitted purposes** where you can still use SPI even after a consumer invokes the limit right:
- Performing the service reasonably expected by the consumer (e.g., using facial recognition specifically for the authentication feature they signed up for)
- Safety, security, and integrity of services
- Short-term, transient use (e.g., a one-time contextual purpose)
- Services performed on your behalf by a service provider
- Verifying/maintaining quality of services
- Activities for which the SPI was specifically provided

Practical read: if facial recognition is used *only* for the authentication feature the consumer opted into, and geolocation/health data are used *only* for the specific features they signed up for (e.g., workout tracking, location-based reminders), a consumer's "limit" request may not change much operationally — you're likely already within the permitted-purpose exceptions for the core use case. But if you're using any of this data for secondary purposes (e.g., ad targeting, analytics beyond the feature itself, sharing with third parties for other purposes), the limitation right will materially restrict those secondary uses once invoked.

### 2. Consent and Disclosure Requirements
- **At-collection notice**: before or at the point you collect geolocation, health, or biometric data, disclose the categories collected, the purpose, whether it's sold/shared, and retention periods — this needs to be presented clearly within the app flow (e.g., at the permission prompt for location/camera/wearable access), not buried only in a privacy policy
- **Privacy policy**: must specifically enumerate these SPI categories, your purposes for each, any third parties they're disclosed to, and retention criteria — update at least annually

### 3. Right to Know, Delete, Correct — Same Mechanics, Heightened Verification
Standard consumer rights apply, but because this involves SPI:
- **Identity verification escalates**: for requests touching this SPI, match **3 data points** plus a **signed declaration under penalty of perjury** (rather than the standard 2-point match)
- **Right to Know**: disclose specific pieces of geolocation/health/biometric data collected, sources, purposes, and any third parties it was shared with
- **Right to Delete**: delete this data and instruct service providers/contractors (wearable vendor, biometric processing vendor) to do the same — but check for exceptions (e.g., fraud prevention needs for the authentication data, or a legal retention obligation)
- **Right to Correct**: applies especially to health metrics, which are more likely to contain errors a consumer would want corrected

### 4. Sale/Sharing Analysis
If any of this SPI is disclosed to third parties — for example, if the wearable integration partner or facial-recognition vendor isn't strictly bound as a service provider/contractor, or if any of this data feeds into advertising — it could constitute a "sale" or "sharing," requiring the separate "Do Not Sell or Share" opt-out mechanism and GPC honoring, on top of the SPI limitation right. Given the sensitivity of this data, confirm your biometric and health-data vendors are contractually bound as **service providers or contractors** (purpose-limited, no independent use, deletion obligations) — using SPI-category vendors as loosely defined "third parties" is a high-risk configuration both legally and reputationally.

### 5. Cybersecurity Audit and Risk Assessment (effective January 1, 2026 — live now)
Given the combination of precise geolocation, health data, and biometric identifiers, this app almost certainly meets the "significant risk" threshold that triggers:
- **Annual cybersecurity audit** — regulations are finalized and in effect
- **Documented risk assessment** conducted before processing that presents significant risk, and available to the CPPA upon request

Treat this as a near-term compliance action, not optional. Document the risk assessment specifically addressing the biometric authentication use case, since facial recognition for authentication is a common focus of both CPPA scrutiny and separate state biometric privacy statutes (note: some states, e.g., Illinois' BIPA, impose additional/separate biometric-specific requirements not covered by CCPA/CPRA — worth flagging for separate review if you operate outside California too).

### 6. Retention Limits
CPRA requires that you disclose retention periods or criteria for each SPI category and not retain longer than reasonably necessary. For biometric templates in particular, define and disclose a specific retention/deletion policy (e.g., deleted upon account closure, or after a defined period of inactivity) rather than indefinite retention.

## What You Need to Disclose (Consolidated Checklist)

In your privacy policy and at-collection notices, for each of the three SPI categories:
- [ ] That the category is collected (precise geolocation / health data via wearable / biometric facial data)
- [ ] The specific purpose(s) of collection and use
- [ ] Whether it is sold or shared with third parties, and to which categories of third parties
- [ ] Retention period or criteria
- [ ] That consumers have a right to limit its use, with a link/mechanism to exercise that right
- [ ] Standard rights: know, delete, correct, non-discrimination
- [ ] Contact information / intake channels for exercising these rights (at least two methods)

## Priority Action Items
1. Confirm and document all vendors touching this SPI as service providers/contractors under compliant contracts (purpose limitation, no independent use, deletion obligations, audit rights)
2. Build the SPI limitation link/flow with a 15-business-day processing commitment
3. Escalate identity verification to the 3-data-point + signed declaration standard for any rights request touching this SPI
4. Conduct and document a risk assessment covering the biometric authentication and health/location data processing; schedule your first annual cybersecurity audit
5. Define and disclose specific retention periods for biometric templates, health data, and geolocation history
6. Review at-collection consent flows (permission prompts within the app) to ensure they meet CPRA disclosure requirements, not just the OS-level permission dialog

---
*This is general compliance guidance, not legal advice. Consult qualified counsel for your specific circumstances, and consider a specialized biometric-privacy-law review given the facial recognition component.*
