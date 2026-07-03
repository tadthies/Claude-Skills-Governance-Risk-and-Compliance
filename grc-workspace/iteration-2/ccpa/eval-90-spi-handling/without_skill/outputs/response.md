# CPRA Sensitive Personal Information: Mobile App Compliance Guide

## Overview

The California Privacy Rights Act (CPRA), effective January 1, 2023, created a new statutory category called **Sensitive Personal Information (SPI)** — a subset of personal information subject to heightened obligations. Your mobile app collects three data types that squarely fall within this category: precise geolocation, health/medical data from wearable integration, and biometric information used for facial recognition authentication. This guide covers classification, obligations, opt-out mechanisms, deadlines, and disclosure requirements for each.

---

## 1. Classification of Each Data Type Under CPRA

### 1.1 Precise Geolocation

**Classification: Sensitive Personal Information — Cal. Civ. Code § 1798.140(ae)(1)(G)**

CPRA defines "precise geolocation" as any data that is derived from a device and that is used or intended to be used to locate a consumer within a geographic area that is equal to or less than the area of a circle with a radius of 1,850 feet (approximately 1/3 of a mile). This is explicitly enumerated as SPI.

- GPS coordinates, latitude/longitude data, and cell tower triangulation accurate to within ~1,850 feet all qualify.
- Coarser location (e.g., city-level or ZIP code) does not qualify as SPI under this definition, though it remains "personal information."
- Health app integrations that log workout routes or location-stamped health events would capture precise geolocation as SPI.

**Key point:** The triggering criterion is the *capability* to locate within 1,850 feet, not whether you actually use it to locate the consumer at that precision.

---

### 1.2 Health Metrics from Wearable Integration

**Classification: Sensitive Personal Information — Cal. Civ. Code § 1798.140(ae)(1)(C)**

CPRA enumerates as SPI: "Personal information collected and analyzed concerning a consumer's health." Data received from wearable integrations (e.g., Apple Health, Google Fit, Fitbit, Garmin Connect) that includes heart rate, blood oxygen, sleep patterns, step counts, caloric burn, menstrual cycle tracking, stress indicators, or any other physiological measurement constitutes SPI.

- The statute uses "health" broadly, encompassing both diagnostic data and wellness/fitness metrics.
- Integration via HealthKit, Health Connect, or similar APIs that surfaces individual-level physiological readings creates SPI obligations even if the data originates from a third-party device.
- Aggregate or de-identified health data may fall outside SPI, but only if it meets the CPRA de-identification standard (not reasonably identifiable even with indirect means).

**Note:** If your wearable integration also captures mental health indicators (e.g., stress scores, mood tracking), these may additionally qualify under the "mental or physical health diagnosis" prong of § 1798.140(ae)(1)(C).

---

### 1.3 Biometric Facial Recognition for Authentication

**Classification: Sensitive Personal Information — Cal. Civ. Code § 1798.140(ae)(1)(E)**

CPRA defines biometric information as SPI when it can be used to identify an individual, including "faceprints" alongside fingerprints, retinal scans, voiceprints, and similar physiological measurements. Facial recognition used for app authentication generates faceprints and/or facial geometry data that is explicitly listed as SPI.

- This applies regardless of whether you store the raw biometric image or only a derived mathematical template/feature vector — the feature vector itself constitutes biometric SPI.
- On-device processing (e.g., using Apple Face ID or Android BiometricPrompt without transmitting data to your servers) may limit your exposure if you never receive or process the biometric data yourself. However, if your app captures and processes facial geometry on your infrastructure, full SPI obligations apply.
- Biometric data also overlaps with California's other biometric law — the California Consumer Privacy Act (CCPA) biometric data definition — as well as broader definitions under BIPA (Illinois), though BIPA has separate requirements.

---

## 2. Special Obligations for Sensitive Personal Information

CPRA imposes obligations on SPI that go beyond what applies to ordinary personal information. These apply both to businesses that "use" SPI and to those that "disclose" it to third parties.

### 2.1 Purpose Limitation

Under Cal. Civ. Code § 1798.121, businesses may only use or disclose SPI for:

1. **Permitted purposes** (no opt-out required):
   - Performing services or providing goods reasonably expected by an average consumer who requests those services/goods
   - Preventing, detecting, or investigating security incidents, fraud, illegal activity, or liability
   - Ensuring the physical safety of persons
   - Short-term, transient use (including non-personalized advertising in a current session)
   - Performing services on behalf of a business (service provider context)
   - Verifying or maintaining the quality/safety of a service or device
   - Activities that are required by law

2. **Any use or disclosure BEYOND these permitted purposes** requires offering consumers the right to limit use and disclosure (see Section 3 below).

**Practical implication:** If you use precise geolocation for purposes beyond core app navigation (e.g., targeted advertising based on visited locations), or share health metrics with advertising partners, or use biometric data for analytics beyond authentication, you must offer a limitation right.

### 2.2 Data Minimization and Purpose Binding

CPRA's new data minimization principle (§ 1798.100(a)(3)) requires that collection, use, retention, and sharing of personal information — including SPI — be reasonably necessary and proportionate to the disclosed purpose. For SPI specifically:

- You may not collect more precise geolocation data than necessary for the stated feature.
- Health metrics must be used only for the disclosed wellness/health feature; repurposing for marketing profiles triggers SPI limitation rights.
- Biometric data must be retained only as long as necessary for authentication and then securely deleted.

### 2.3 Contractual Requirements with Service Providers and Contractors

Businesses sharing SPI with service providers, contractors, or third parties must:

- Execute written contracts (data processing agreements) that restrict the recipient from using SPI for purposes other than those specified.
- Prohibit recipients from selling or sharing SPI without authorization.
- Require recipients to flow down these obligations to their own subprocessors.
- Grant the business audit/assessment rights over the recipient's processing practices.

### 2.4 Risk Assessments (for Certain Processing)

Under CPRA, the California Privacy Protection Agency (CPPA) may issue regulations requiring businesses to conduct and submit risk assessments before processing that presents significant risk to consumers. Biometric data used for mass authentication and precise location tracking are among the highest-risk categories likely to be subject to forthcoming CPPA regulations on risk assessments and cybersecurity audits.

Even before mandatory regulations, best practice is to conduct a Privacy Impact Assessment (PIA) for your biometric facial recognition and geolocation processing.

---

## 3. Opt-Out Mechanisms Required

### 3.1 Right to Limit Use and Disclosure of SPI

Cal. Civ. Code § 1798.121 creates a consumer right to direct a business to limit its use of their SPI to the permitted purposes listed in Section 2.1 above.

**Trigger:** This right applies if — and only if — you use or disclose SPI for purposes beyond the enumerated permitted purposes.

**Required mechanism:**

- You must provide a **"Limit the Use of My Sensitive Personal Information"** link (or equivalent) in your privacy notice and on your homepage.
- The CPPA has authorized the use of a **combined opt-out link** that serves both the "Do Not Sell or Share" right and the "Limit SPI" right, using the title **"Your Privacy Choices"** or **"Your California Privacy Choices"** accompanied by the opt-out icon (the eye-with-line icon specified in CPPA regulations).
- If you use or share all SPI only for permitted purposes (e.g., location is used only to provide the service the consumer requested, biometrics only for authentication, health data only to display health summaries to the user), you may state this in your privacy policy and are **not required** to provide the limitation link — but you must affirmatively disclose that no further use occurs.

**Implementation options:**
1. Standalone "Limit the Use of My Sensitive Personal Information" link
2. Combined "Your Privacy Choices" / "Your California Privacy Choices" link (CPPA-approved combined opt-out)
3. A privacy preference center accessible via these links where consumers can manage both SPI limitation and data sale/sharing opt-out in one place

**For your specific data types:**
- **Geolocation:** If you use location data for targeted advertising or share it with ad networks, you must offer limitation. If it is solely used to provide the in-app service, you may be exempt — but document this clearly.
- **Health metrics:** If health data is shared with any third party for advertising or analytics, limitation opt-out is required. Internal use for the wearable feature alone may qualify as a permitted purpose.
- **Biometric facial recognition:** Authentication-only use likely qualifies as a permitted purpose. Any secondary use (analytics, improving ML models, fraud scoring beyond authentication) triggers the limitation right.

### 3.2 Do Not Sell or Share (Interaction with SPI)

The existing "Do Not Sell or Share My Personal Information" right under § 1798.120 applies to all personal information, including SPI. If you sell or share (for cross-context behavioral advertising) any of these three data types, you must also honor this right separately and distinctly. The combined "Your Privacy Choices" link can address both simultaneously.

---

## 4. Response Deadlines for SPI Limitation Requests

### 4.1 Standard Response Timeline

Under Cal. Civ. Code § 1798.125 and associated CPPA regulations, businesses must respond to consumer SPI limitation requests within:

- **45 calendar days** of receiving the request (initial response deadline)
- **One 45-day extension** (90 days total) is permitted if the business notifies the consumer of the extension and the reason within the initial 45-day window

### 4.2 What "Responding" Means

A compliant response to an SPI limitation request requires:

1. **Acknowledging** receipt of the request (recommended within a few business days)
2. **Verifying** the consumer's identity (to a reasonable degree, without requiring unnecessary disclosure of additional personal information)
3. **Confirming** that limitation has been applied within the 45-day deadline
4. **Notifying service providers and contractors** who received the SPI so they can likewise limit processing (businesses must pass the limitation through to recipients)

### 4.3 Service Provider Pass-Through Obligation

Once a consumer submits a valid SPI limitation request, you must notify all service providers and contractors that received the consumer's SPI within a **commercially reasonable time** — the CPPA has interpreted this as promptly and before the next processing cycle that would use the SPI for non-permitted purposes.

### 4.4 No Discrimination for Exercising Rights

You may not deny, charge different prices, or provide a lower quality of service to consumers who exercise their SPI limitation right (§ 1798.125). However, you may explain if a requested limitation makes it technically impossible to provide a specific feature (e.g., you cannot provide location-based routing if the consumer limits geolocation processing).

---

## 5. Privacy Notice and Disclosure Requirements

### 5.1 Privacy Policy Disclosures for SPI

Cal. Civ. Code § 1798.100(a)(2) and CPPA regulations require your privacy policy (updated at least once every 12 months) to include specific SPI disclosures:

**For each category of SPI collected, disclose:**

1. **The categories of SPI collected** — specifically identify precise geolocation, biometric information, and health/medical information using language that mirrors CPRA statutory categories.
2. **The purposes for which each SPI category is collected or used** — be specific (e.g., "precise geolocation is collected to provide turn-by-turn navigation features" rather than "to improve your experience").
3. **Whether SPI is disclosed to third parties** — identify the categories of third parties and the business/commercial purpose for each disclosure.
4. **Whether SPI is sold or shared** — if so, for what purpose and to which categories of recipients.
5. **The retention period** for each category of SPI, or if not possible, the criteria used to determine the retention period.

### 5.2 Notice at Collection

Beyond the general privacy policy, CPRA requires a **Notice at Collection** — a shorter, just-in-time notice presented to consumers at or before the point of SPI collection. For your app:

- **Precise geolocation:** The notice must appear before or at the moment the app first requests location permissions. It must identify that precise location is collected, the purposes, and whether it is sold or shared.
- **Health metrics:** Disclosed at the point of wearable integration setup or HealthKit/Health Connect permission request.
- **Biometric facial recognition:** Disclosed before the consumer enrolls their face for authentication, including whether the biometric template is stored on-device or transmitted to your servers.

The Notice at Collection must include:
- Categories of personal information (including SPI) to be collected
- Purposes for collection
- A link to the full privacy policy
- A link to "Do Not Sell or Share My Personal Information" / "Limit the Use of My Sensitive Personal Information" if applicable

### 5.3 "Limit SPI" Disclosure in the Privacy Policy

Your privacy policy must include a dedicated section explaining:

- The categories of SPI you collect (geolocation, biometric, health)
- Whether you use or disclose SPI beyond permitted purposes
- If you do not: an affirmative statement that SPI is used only for the enumerated permitted purposes (this exempts you from providing the limitation link)
- If you do: instructions for submitting a limitation request and a link to the request mechanism

### 5.4 Biometric-Specific Disclosures

For biometric facial recognition specifically, best practice (and in some jurisdictions, legal requirement) includes disclosing:

- The specific biometric identifier collected (facial geometry/faceprint)
- Whether raw images or only derived mathematical templates are stored
- The retention schedule (how long biometric data is kept and criteria for deletion)
- Whether biometric data is shared with any third party and for what purpose
- The security measures protecting the biometric data

### 5.5 Required Links and Accessibility

- The "Limit the Use of My Sensitive Personal Information" link (or combined "Your Privacy Choices" link) must appear in the app's settings, on the company website's homepage, and within the privacy policy.
- For mobile apps, a commonly compliant approach is a **Privacy** or **Data Preferences** option in the app's main settings menu that surfaces both the opt-out and limitation controls.
- The link/mechanism must be **accessible to consumers with disabilities** (meeting WCAG 2.1 AA standards where feasible).

---

## 6. Practical Compliance Checklist

### Immediate Actions

- [ ] Audit all three SPI data flows: what is collected, where it goes, how long it is retained, and who has access
- [ ] Determine whether any SPI is used or disclosed beyond permitted purposes (this drives whether limitation opt-out is required)
- [ ] Update your privacy policy to add SPI-specific disclosures for all three categories
- [ ] Add Notice at Collection screens before location permission prompts, wearable integration, and biometric enrollment
- [ ] If SPI is used beyond permitted purposes: implement "Limit the Use of My Sensitive Personal Information" or combined "Your Privacy Choices" link/control in the app settings and website

### Ongoing Obligations

- [ ] Process SPI limitation requests within 45 days (with one possible 45-day extension)
- [ ] Notify service providers and contractors of limitation requests promptly
- [ ] Review data processing agreements with all vendors receiving SPI to ensure contractual restrictions are in place
- [ ] Conduct annual privacy policy updates
- [ ] Monitor CPPA regulations for forthcoming risk assessment requirements that will likely apply to biometric and geolocation processing

---

## 7. Summary Table

| Data Type | CPRA SPI Category | Code Section | Limitation Right Triggered? | Notice at Collection Required? |
|---|---|---|---|---|
| Precise geolocation | Precise geolocation | § 1798.140(ae)(1)(G) | If used beyond navigation/service | Yes — before location permission |
| Health metrics (wearables) | Health information | § 1798.140(ae)(1)(C) | If shared with third parties or used for ads | Yes — before wearable sync permission |
| Biometric facial recognition | Biometric information | § 1798.140(ae)(1)(E) | If used beyond authentication | Yes — before biometric enrollment |

**Response deadline for limitation requests:** 45 days, extendable by 45 days with notice (90 days maximum).

---

*This response reflects CPRA as effective January 1, 2023, and CPPA implementing regulations. Businesses should monitor ongoing CPPA rulemaking, as regulations on cybersecurity audits, risk assessments, and automated decision-making technology are still being finalized and may impose additional requirements on biometric and geolocation processing.*
