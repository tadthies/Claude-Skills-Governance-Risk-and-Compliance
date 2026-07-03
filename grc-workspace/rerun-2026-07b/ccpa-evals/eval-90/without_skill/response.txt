# CPRA Classification and Obligations for Geolocation, Health, and Biometric Data

Your mobile app collects three distinct categories of data that CPRA treats with heightened protection. All three fall within **Sensitive Personal Information (SPI)** — a category CPRA created that triggers obligations beyond ordinary personal information.

## 1. How CPRA Classifies Each Data Type

### Precise Geolocation
- CPRA's SPI definition explicitly includes **"precise geolocation"**, generally defined as geolocation data that identifies a consumer's or device's location within a radius of **1,850 feet (approximately 1/3 mile)** or less.
- This is one of the enumerated SPI categories under Cal. Civ. Code § 1798.140.

### Health Metrics from Wearable Integration
- Health data generally qualifies as SPI. The statute references **"personal information collected and analyzed concerning a consumer's health"**.
- Depending on exactly what's collected (heart rate, sleep patterns, activity levels, menstrual cycle tracking, etc.), this may also implicate California's separate **Confidentiality of Medical Information Act (CMIA)** and/or the **California Consumer Health Data Act (part of the broader "My Health My Data" trend)**, which can impose obligations independent of and sometimes stricter than CCPA/CPRA — verify applicability given your specific wearable data types, as health-adjacent consumer data laws have been an active area of California and state-level lawmaking.
- Health data is treated as SPI regardless of whether it meets HIPAA's PHI definition — CCPA/CPRA's health data category is broader and not limited to HIPAA-covered entities.

### Biometric Data for Facial Recognition
- CPRA's SPI definition explicitly includes **"the processing of biometric information for the purpose of uniquely identifying a consumer."**
- Facial recognition data used for authentication is a direct, unambiguous match to this category — biometric identifiers used to uniquely identify an individual are a core enumerated example.
- Note: California also has other biometric-specific considerations (e.g., biometric information is also separately referenced in the state's data breach notification statute, Cal. Civ. Code § 1798.82, as a category triggering breach notice obligations). If your facial recognition data could also be considered "biometric information" under Illinois BIPA or other state biometric privacy laws (if you have users in those states), those separate statutes with their own consent/retention schedule requirements would apply independently of CCPA/CPRA.

## 2. Special Obligations That Apply to Sensitive Personal Information

Because all three data types are SPI, you have obligations beyond the baseline CCPA/CPRA requirements for ordinary PI:

### Right to Limit Use and Disclosure of SPI
- Consumers have the right to direct you to **limit your use of SPI** to only what is necessary to perform the services reasonably expected by an average consumer requesting those services, or as otherwise permitted by regulations (e.g., for security, fraud prevention, or short-term transient use not for profiling).
- If you use SPI for additional purposes — e.g., building advertising profiles, cross-app tracking, or secondary analytics — you must provide a clear **"Limit the Use of My Sensitive Personal Information"** link (or fold it into a combined "Your Privacy Choices" link using the CPPA-approved toggle/icon) and honor consumer requests to restrict that use.
- If your use of the SPI is strictly limited to providing the core service the consumer requested (e.g., using geolocation only to show nearby stores, using health metrics only to power the fitness feature itself, using facial biometric data only to authenticate the account holder) and you don't use it for secondary purposes like advertising, you may not need to offer the limit-use link — but you must still disclose the collection and generally cannot use SPI beyond what's "reasonably necessary and proportionate" for the disclosed purpose.

### Purpose and Retention Limitations
- Under CPRA's general data minimization and storage limitation principles (heightened for SPI), collection, use, retention, and sharing of SPI must be **reasonably necessary and proportionate** to achieve the purposes for which it was collected or processed, or another compatible purpose.
- Retention periods for biometric and health data should be tied to active need (e.g., delete facial recognition templates when the account is closed or authentication method is changed; don't indefinitely retain raw geolocation trails beyond the operational purpose).

### Elevated Security Requirements
- SPI (especially biometric templates and health data) warrants **heightened security measures** — encryption at rest and in transit, strict access controls, and specific safeguards for biometric templates given their immutability (you can't "reset" a face the way you reset a password).
- A breach involving unencrypted biometric or health data carries **higher regulatory and litigation risk**, including potential exposure under CCPA's private right of action (statutory damages for breaches involving certain categories, and biometric data is separately called out in California's breach notification statute as sensitive).

### Risk Assessments and Cybersecurity Audits
- Given you're processing SPI at scale (precise geolocation + health + biometric identifiers across your user base), you likely fall within the scope of CPRA's **risk assessment** and potentially **annual cybersecurity audit** requirements administered by the California Privacy Protection Agency (CPPA), which apply to businesses whose processing presents significant risk to consumers' privacy or security. Confirm current CPPA regulatory thresholds, as these requirements have been phased in with specific applicability criteria and effective dates.
- Risk assessments generally require documenting: the purpose of processing, categories of SPI involved, benefits to the business/consumers/public, potential risks, and safeguards — and must be updated periodically and made available to the CPPA upon request.

### Notice Obligations
- **Notice at Collection**: must specifically disclose that you collect precise geolocation, health information, and biometric information, list the specific purposes, and indicate whether this SPI is used beyond what's necessary to provide the requested service (which triggers the limit-use right).
- **Privacy Policy**: must enumerate these SPI categories among your disclosed categories of personal information, describe retention criteria/periods, and confirm whether SPI is sold, shared, or disclosed to third parties (e.g., a wearable integration partner, cloud biometric-matching vendor, or analytics provider).

### Opt-In Requirements for Minors
- If you have actual knowledge any users are under 16, selling or sharing their SPI (including geolocation, health, or biometric data) requires **opt-in consent**, not just an opt-out mechanism. Given wearable/fitness and facial-recognition-enabled apps often attract broad age ranges, confirm your age-gating and consent flows account for this.

### Vendor/Third-Party Contracts
- If a third-party facial recognition/biometric-matching vendor, wearable device manufacturer, or health analytics platform processes this SPI on your behalf, your contracts must include CCPA/CPRA-mandated service provider or contractor restrictions: no independent use, no combining with other clients' data, deletion/return obligations at contract end, and audit rights.
- Determine whether these vendors are true service providers or independent "third parties" — if the biometric vendor uses facial data for its own model training or cross-client purposes, that could constitute a sale/share of SPI, triggering opt-in-level scrutiny given SPI's heightened protections.

## 3. What You Need to Disclose

At minimum, your privacy policy and notice-at-collection should specify:

1. **Categories of SPI collected**: precise geolocation; health information (specify wearable-sourced metrics, e.g., heart rate, activity, sleep, or other biometric-adjacent health signals); biometric information (facial recognition data used for authentication).
2. **Purposes**: e.g., "to authenticate your identity via facial recognition," "to provide location-based features," "to sync and display fitness/health metrics from your connected wearable device."
3. **Whether SPI is used beyond what's necessary for the service** (if yes, offer the Limit Use link and honor GPC-adjacent signals where applicable; if no, state that use is limited to providing the requested functionality).
4. **Retention criteria** for each SPI category — particularly important for biometric templates given their sensitivity and immutability.
5. **Categories of third parties** receiving this SPI (e.g., cloud biometric processing vendor, wearable device API partner, analytics providers) and whether any of these relationships constitute a sale/share.
6. **Consumer rights specific to SPI**: right to limit use, right to know/delete/correct as applied to SPI, and confirmation of opt-in requirements for any minors.
7. **Security measures** in place to protect this heightened-risk data (helps demonstrate "reasonable security" posture).

## Practical Recommendations
1. **Map the exact data flows**: which vendor processes facial recognition (on-device vs. cloud-based matching matters significantly for both compliance and security risk), and how wearable data is ingested, stored, and used.
2. **Default to purpose limitation**: use SPI strictly for the disclosed functional purpose (authentication, fitness features, location-based service) to minimize the need for opt-in/limit-use complexity, unless your business model depends on secondary uses like advertising or analytics — in which case, build the Limit Use mechanism now.
3. **Evaluate biometric-specific state laws** beyond CCPA/CPRA (e.g., Illinois BIPA, Texas CUBI, Washington biometric law) if your app has users outside California, since biometric authentication features often trigger multi-state compliance obligations with consent and retention-schedule requirements more stringent than CCPA/CPRA.
4. **Evaluate health-data-specific California and multi-state consumer health laws** given the wearable health metrics, as several states have enacted consumer health data statutes with broader scope than HIPAA that could apply here independent of CCPA/CPRA.
5. **Prepare for a risk assessment / cybersecurity audit** given the scale and sensitivity of SPI processed — confirm current CPPA applicability thresholds.
6. **Implement biometric-specific security safeguards**: store facial recognition data as encrypted templates (not raw images) where feasible, apply strict access controls, and define a clear deletion trigger (e.g., account closure or authentication method change).

*This is general compliance guidance based on the CCPA/CPRA statutory framework's treatment of sensitive personal information. Given the overlap with biometric-specific state laws and emerging consumer health data statutes, and the evolving CPPA regulations on risk assessments/audits, consult counsel for a tailored compliance review of this specific app's data flows.*
