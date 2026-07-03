# CPRA Sensitive Personal Information (SPI): Classification, Obligations, and Disclosure Requirements

## Overview

Your mobile app — which collects precise geolocation, health metrics from wearable integration, and biometric facial recognition for authentication — processes three distinct categories of **Sensitive Personal Information (SPI)** under the California Privacy Rights Act (CPRA). Each category carries heightened obligations that go beyond standard personal information requirements. Below is a thorough analysis.

---

## 1. Classification: All Three Data Types Are SPI

### Precise Geolocation
CPRA defines precise geolocation as data that reveals a consumer's location within a radius of **1/4 mile (approximately 400 meters)**. Mobile apps that use GPS or other high-precision signals to determine a user's location almost universally meet this threshold. If your app collects coordinates, route data, or real-time position at any meaningful precision, it is collecting SPI.

### Health/Medical Data from Wearables
Health metrics collected through wearable device integration — including but not limited to heart rate, blood oxygen levels, sleep patterns, step counts, menstrual cycle tracking, glucose readings, or ECG data — constitute **health or medical information** under CPRA and are classified as SPI. The statutory language expressly covers health data collected from "consumer devices" and "health-related applications," which includes third-party wearable integrations (e.g., Apple Health, Fitbit, Garmin).

### Biometric Data for Facial Recognition Authentication
Biometric data used to **identify or authenticate** a consumer — such as facial recognition templates, fingerprint scans, voiceprints, or iris scans — is SPI under CPRA. The key trigger is use for identification or authentication purposes. Because your app uses facial recognition specifically to authenticate users, this data is unambiguously SPI, regardless of whether the raw image is retained or only the derived mathematical representation (template) is stored.

**Summary:** All three data types your app collects are SPI. Your organization must apply the full suite of CPRA SPI obligations to each.

---

## 2. Obligation: "Limit the Use of My Sensitive Personal Information" Mechanism

CPRA grants California consumers the right to **direct businesses to limit the use and disclosure of their SPI** to what is strictly necessary for the purposes for which it was collected (or for certain permitted purposes — see Section 4 below).

### What You Must Provide
You must offer consumers a clear and conspicuous method to exercise this right. Acceptable implementations include:

- **A dedicated "Limit the Use of My Sensitive Personal Information" link** placed on your app's homepage or settings screen
- **A combined opt-out page** that consolidates both "Do Not Sell or Share My Personal Information" and "Limit the Use of My Sensitive Personal Information" options into a single consumer-facing mechanism

This link or mechanism must be:
- Clearly labeled using the CPRA-mandated or substantially similar language
- Accessible without requiring the consumer to create an account or log in (where feasible)
- Available at the point of collection or via a persistent, discoverable location in your app's interface and website (if one exists)

Failure to provide this mechanism is a direct CPRA violation and is subject to enforcement by the California Privacy Protection Agency (CPPA) and the California Attorney General.

---

## 3. Processing Deadline: 15 Business Days for SPI Limitation Requests

When a consumer submits a request to limit the use of their SPI, you must **honor that request within 15 business days** of receipt. This is a materially shorter timeline than the 45-calendar-day response period applicable to most other consumer privacy rights requests (e.g., access, deletion, correction) under CPRA.

### Practical Implications
- Your intake and fulfillment workflows for SPI limitation requests must be separate from (or prioritized within) your general privacy request queue
- The 15-business-day clock starts upon **receipt** of the request, not upon verification of consumer identity
- You may still verify identity as part of processing, but processing delays caused by verification do not pause the 15-business-day clock
- If you need additional time, CPRA does not provide a formal extension for SPI limitation requests (unlike the 45-day period, which allows a 45-day extension with notice)
- Systems and vendors processing SPI on your behalf must be capable of honoring limitation signals within this window; include contractual timelines in your Data Processing Agreements (DPAs) with service providers

---

## 4. Permitted Uses of SPI Without Triggering Limitation Rights

Not all SPI processing is subject to consumer limitation rights. CPRA recognizes several **permitted purposes** under which a business may use SPI without being required to honor limitation requests:

### Permitted Purpose Categories
1. **Core service delivery** — SPI may be used to perform the services or provide the goods a consumer has reasonably requested. For your app:
   - Precise geolocation used to deliver location-based features the user explicitly enabled (e.g., find nearby locations) qualifies
   - Health metrics used to display health dashboards or provide the fitness insights the user signed up for qualify
   - Biometric data used exclusively to authenticate the consumer to their account qualifies

2. **Security and integrity purposes** — SPI may be used to detect, prevent, and investigate security incidents, fraud, and other harmful or illegal activity

3. **Short-term, transient use** — SPI processed solely during a single interaction that is not disclosed to third parties and is not used to build a consumer profile

4. **Legal obligations** — SPI may be processed to comply with applicable law or respond to legal process

### Documentation Requirement
This is critical: for **each SPI processing activity**, you must clearly document which permitted purpose applies. Generic or blanket assertions ("we use data for security") are insufficient. Your records of processing activities (RoPA) or equivalent internal documentation should map:

| SPI Category | Processing Activity | Applicable Permitted Purpose |
|---|---|---|
| Precise geolocation | Real-time location display | Core service delivery |
| Precise geolocation | Location history logging | Requires consumer limitation opt-in unless tied to a reasonably expected feature |
| Health metrics (wearable) | Health dashboard rendering | Core service delivery |
| Health metrics (wearable) | Sharing with analytics vendors | NOT a permitted use — limitation rights apply |
| Biometric (facial recognition) | User authentication | Core service delivery / security and integrity |

If you cannot clearly assign a recognized permitted purpose to an SPI processing activity, that activity is subject to consumer limitation rights, and you must stop or restrict it upon receiving a valid limitation request.

---

## 5. Privacy Notice Requirements: Dual Disclosure Obligations

CPRA imposes SPI disclosure requirements in **two places**: the at-collection notice and the full privacy policy. Both must be updated to reflect your SPI processing.

### A. At-Collection Notice (Notice at Collection)
At or before the point of collecting SPI, you must disclose:

- **Each category of SPI being collected** (e.g., "We collect precise geolocation data, health and fitness metrics from linked wearable devices, and biometric identifiers used for facial recognition authentication")
- **The purpose for which each SPI category is collected** (e.g., "Geolocation is collected to provide location-based features; biometric data is collected for account authentication")
- **Whether the SPI is sold or shared** with third parties (if it is, this must be prominently stated; if it is not, you should affirmatively say so)
- A **link or reference** to your full privacy policy where consumers can obtain more detail

For a mobile app, the at-collection notice is typically presented:
- During onboarding, before the relevant permission is requested (e.g., before the location permission dialog, before biometric enrollment)
- Via an in-context disclosure banner or modal at the moment each SPI type is first collected

### B. Privacy Policy
Your comprehensive privacy policy must include a dedicated section for SPI that covers:

1. **Categories of SPI collected** — list all three (geolocation, health data, biometrics) explicitly; "personal information" alone is insufficient
2. **Purpose of collection for each SPI category** — describe the specific business or service purpose
3. **Retention period** (or criteria for determining retention) for each SPI category
4. **Whether SPI is sold, shared, or disclosed to third parties**, and if so, for what purpose and to what categories of recipients
5. **Whether SPI is used beyond the necessary purpose** — if SPI is used for secondary purposes (e.g., health data used for targeted advertising in addition to core service delivery), this must be disclosed and is likely subject to consumer limitation rights
6. **Consumer rights regarding SPI** — explain the right to limit use, how to submit a request, and the 15-business-day processing timeline
7. **Link to the limitation mechanism** — include or reference the "Limit the Use of My Sensitive Personal Information" link directly in the privacy policy

### Critical Alignment Requirement
The disclosures in your at-collection notice and your privacy policy must be **consistent**. CPRA does not permit disclosures in the privacy policy that contradict or expand what was stated at collection. If your at-collection notice states that biometric data is used only for authentication, your privacy policy cannot later reveal that it is also shared with a third-party identity vendor — that would be a material inconsistency and a separate CPRA violation.

---

## Summary of Key Action Items

| Obligation | Requirement | Applies To |
|---|---|---|
| SPI classification | All three data types are SPI | Geolocation, health metrics, biometrics |
| Limitation mechanism | "Limit the Use of My SPI" link on app/homepage | All SPI categories |
| Response timeline | 15 business days for limitation requests | All SPI categories |
| Permitted use documentation | Document permitted purpose for each SPI activity in internal records | All SPI processing activities |
| At-collection notice | Disclose each SPI category, purpose, and sale/sharing status | Before or at collection |
| Privacy policy | Full SPI section covering categories, purposes, retention, sale/sharing, consumer rights | Published policy |

---

## Recommended Next Steps

1. **Audit each SPI data flow** — map where geolocation, health, and biometric data are collected, processed, stored, and shared; assign a permitted purpose to each or flag for limitation compliance
2. **Implement the limitation mechanism** — add a "Limit the Use of My Sensitive Personal Information" option to your app settings and, if applicable, your web homepage
3. **Build a 15-business-day SPI request fulfillment workflow** — distinct from or prioritized over your standard 45-day privacy request queue
4. **Update at-collection disclosures** — review your location permission dialog, biometric enrollment flow, and wearable integration screens for CPRA-compliant SPI disclosures
5. **Revise your privacy policy** — add a dedicated SPI section covering all five required disclosure elements
6. **Review vendor contracts** — ensure DPAs with third parties who process SPI include appropriate use restrictions and 15-business-day limitation fulfillment timelines
7. **Document permitted purposes** — maintain a records-of-processing document that maps each SPI processing activity to its applicable permitted use justification
