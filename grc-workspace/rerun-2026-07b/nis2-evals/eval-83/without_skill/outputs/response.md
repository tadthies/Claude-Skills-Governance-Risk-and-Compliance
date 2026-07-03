# NIS2 Incident Reporting Walkthrough: Ransomware Attack Encrypting Core Operational Systems

## Step 0: Determine If This Is a "Significant Incident" (Do This Immediately)

Before anything else, assess whether this meets the NIS2 threshold for mandatory reporting under Article 23. An incident is **significant** if:

(a) It has caused, or is capable of causing, **severe operational disruption** of the services or **financial loss** for the entity concerned; or

(b) It has affected, or is capable of affecting, **other natural or legal persons** by causing considerable material or non-material damage.

**A ransomware attack that has encrypted your core operational systems almost certainly meets this threshold** — encryption of core operational systems is close to a textbook example of "severe operational disruption." Proceed on the assumption this is reportable. Do not wait for full confirmation of scope/impact before starting the clock — the clock starts when you become "aware" of the incident, not when you've finished investigating it.

## The Reporting Clock: When Does It Start?

The clock starts at the moment you **become aware** of the significant incident — i.e., roughly 09:00 Monday, when the encryption was discovered/detected, not when the attack technically began (which may have been earlier, e.g., initial access days/weeks prior) and not when your investigation concludes. Document precisely when your team became aware, as this timestamp is itself something regulators will ask about.

## Stage 1: Early Warning — Within 24 Hours (by 09:00 Tuesday)

**Deadline:** No later than 24 hours after becoming aware.

**To whom:** Your national CSIRT (Computer Security Incident Response Team) or the competent authority designated under your Member State's NIS2 transposition law (e.g., BSI in Germany, ANSSI in France, NCSC in various countries — send to whichever authority is designated for your sector/Member State).

**What to include:**
- Whether the incident is suspected of being caused by unlawful or malicious action (yes, in this case — ransomware)
- Whether it could have a cross-border impact (relevant if you operate in multiple Member States or your operational disruption affects customers/supply chains across borders)
- Basic identifying information: your entity, contact point, nature/type of incident (ransomware)

This is a lightweight, fast notification — you are not expected to have full details yet. The purpose is to get the incident on the regulator's radar immediately so they can offer assistance and track cross-sector patterns.

## Stage 2: Incident Notification — Within 72 Hours (by 09:00 Thursday)

**Deadline:** No later than 72 hours after becoming aware.

**What it must contain (updating the early warning):**
- An **initial assessment** of the incident, including its severity and impact
- **Indicators of compromise (IoCs)** where available — file hashes, ransomware variant/family if identified, C2 infrastructure, TTPs observed
- Where possible at this stage, request for assistance from the CSIRT if needed

By this point you should be able to characterize: which systems were encrypted, the ransomware family (if identified via forensic triage), initial entry vector hypothesis, scope of operational impact, and whether data exfiltration is suspected (increasingly common in modern ransomware — "double extortion").

## Stage 3: Intermediate Report (If Requested)

If the competent authority or CSIRT requests it, or if the incident is still ongoing, you may need to provide a status update — this is not always mandatory in every transposition but is common practice, especially for incidents that remain unresolved (recovery from operational-system encryption often takes days to weeks).

## Stage 4: Final Report — Within One Month

**Deadline:** No later than one month after the submission of the 72-hour incident notification (i.e., roughly one month after Thursday, not one month after the original incident).

**What it must contain:**
- A **detailed description** of the incident, including its severity and impact
- The **type of threat or root cause** likely to have triggered the incident (e.g., specific ransomware strain, initial access vector — phishing, exploited vulnerability, compromised credentials, exposed RDP, etc.)
- **Mitigation measures applied and ongoing**
- Where applicable, the **cross-border impact** of the incident

If the incident is still ongoing at the one-month mark, you submit a progress report at that point and a final report once it is actually resolved.

## Who Specifically Gets Notified

1. **National CSIRT / competent authority** — the mandatory regulatory recipient under Articles 23 and 27. Which specific body depends on your Member State and sector (e.g., in Germany: BSI; the specific channel is usually a dedicated reporting portal/platform).
2. **Recipients of your service, potentially** — Article 23(1) also requires that, where appropriate, you notify the recipients of your services of significant incidents likely to adversely affect the provision of that service, and, where relevant, inform them of any measures they can take in response to the threat. If your operational disruption affects customers' ability to receive your service, you likely need to notify them directly, separate from the regulatory reporting.
3. **The public**, in some cases — the competent authority (or you, at their direction) may need to inform the public where public awareness is necessary to prevent a significant incident or deal with an ongoing one, or where disclosure is otherwise in the public interest.
4. **Other affected Member States' authorities**, if there is a cross-border dimension (e.g., if you provide services in multiple Member States, or if the incident could impact other Member States).

## Parallel Obligations to Track Simultaneously

Ransomware incidents frequently trigger **multiple overlapping reporting regimes** — don't let NIS2 tunnel-vision cause you to miss others:

- **GDPR (Article 33/34):** If any personal data was encrypted, exfiltrated, or otherwise compromised (ransomware often involves data theft before encryption), you likely have a **72-hour breach notification obligation to your Data Protection Authority** as well — this is a separate legal basis and separate clock (though also 72 hours, conveniently often aligned).
- **Sector-specific regulators:** If you're in energy, finance (DORA), healthcare, transport, etc., you may have additional incident reporting obligations under sector-specific frameworks running in parallel to NIS2.
- **Contractual/customer notification obligations:** Check customer contracts and SLAs for breach/incident notification clauses that may have shorter deadlines than the regulatory ones.
- **Law enforcement:** Consider reporting to national police/cybercrime units — ransomware is a crime, and many CSIRTs coordinate with law enforcement, but this is generally a separate, voluntary-but-recommended track (mandatory in some Member States for certain sectors).
- **Insurance:** If you carry cyber insurance, most policies have notification deadlines (often 24-72 hours) that must be met to preserve coverage — check this immediately, in parallel with regulatory reporting.

## Practical Timeline Summary (Assuming Awareness at 09:00 Monday)

| Deadline | Action | Target Time |
|---|---|---|
| T+24h | Early warning to CSIRT/competent authority | Tue 09:00 |
| T+72h | Incident notification (initial assessment, IoCs) | Thu 09:00 |
| Ongoing | Notify affected customers/service recipients if service impacted | As soon as practicable |
| Ongoing | Assess GDPR personal data breach notification (separate 72h clock from data-breach awareness) | Parallel track |
| T + 1 month from notification | Final report (root cause, impact, mitigation) | ~Early August |

## Immediate Practical Recommendations

1. **Do not pay the ransom** as a first move — this doesn't stop your reporting obligations and creates its own legal/sanctions risk (paying threat actors that may be subject to international sanctions is a real concern); consult law enforcement and legal counsel first.
2. **Preserve evidence** — forensic images, logs — before remediation destroys evidence needed for the root-cause analysis required in your final report.
3. **Activate your incident response plan and legal counsel simultaneously** with technical containment — the reporting clock does not pause for investigation, so someone (legal/compliance) should own the regulatory notification workstream in parallel with the technical team's containment/recovery workstream.
4. **Identify the correct competent authority/CSIRT and reporting channel now** (before you need it) — most Member States have a specific online portal; know the URL and login/registration status of your organization before an incident, not during one.
5. **Assume you need to notify your DPA under GDPR as well** unless you can affirmatively rule out personal data involvement — ransomware groups increasingly exfiltrate data before encrypting, so don't assume "just encryption, no exfiltration" without forensic confirmation.

**Caveat:** Exact procedural details (specific reporting portal, precise competent authority, any additional national-level requirements or reporting templates) depend on your specific Member State's NIS2 transposition law — confirm the exact mechanics with your national CSIRT's published guidance before the 24-hour deadline arrives.
