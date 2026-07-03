# CRA Reporting Obligations — Actively Exploited Vulnerability

If you have discovered an **actively exploited vulnerability** in a product with digital elements you manufacture, the CRA (Regulation (EU) 2024/2847) imposes mandatory, time-bound reporting obligations. These obligations are already in force (applicable since **11 September 2026**), ahead of the main conformity-assessment obligations (11 December 2027).

## Who you report to

- **ENISA** (via the future **single reporting platform**, which National CSIRTs and ENISA jointly operate) — this is the primary reporting channel. In practice, until the fully harmonized platform is live, reports are submitted to the **CSIRT designated as coordinator** for your Member State (typically your home/main-establishment Member State's CSIRT) or directly to ENISA where the platform is available, which then relays to relevant national CSIRTs.
- You should also assess whether the vulnerability triggers **notification obligations to affected users/customers** (see below) — this is a separate but related obligation.
- If the product also falls under other frameworks (e.g., NIS2 for the manufacturer as an "essential/important entity," GDPR if personal data is affected, or sector rules like medical devices), parallel notifications may be required — but the CRA notification itself goes to ENISA/CSIRT.

## What triggers the obligation

Two distinct triggers exist under CRA Article 14:
1. **Actively exploited vulnerability** in a product with digital elements (your scenario).
2. **Severe incident** having an impact on the security of the product with digital elements.

An actively exploited vulnerability means you have evidence (or credible reports) that the vulnerability is being exploited in the wild — not merely theoretical or newly discovered through internal testing.

## Timeline — the three-stage notification

The CRA requires a phased notification process, all timed from the moment the manufacturer **becomes aware** of the actively exploited vulnerability:

1. **Early warning — within 24 hours** of becoming aware. A brief notification containing:
   - The Member State(s) where the product is placed/available (if known)
   - General information about the vulnerability and the product(s) affected
   - Where applicable, general information on the nature/scale of exploitation

2. **Vulnerability/incident notification — within 72 hours** of becoming aware. This update must include:
   - General information about the vulnerability, its severity, and impact
   - Available compromise indicators, if any
   - Where applicable, information about how it is being actively exploited
   - Any corrective or mitigating measures taken or planned

3. **Final report — within 14 days** after a corrective/mitigating measure becomes available (or, if no measure is yet available, a report is still due at a defined point and must be followed by a final report once remediation is available). The final report must include:
   - A detailed description of the vulnerability, including severity and impact
   - Information about who has exploited or is exploiting it, if known
   - Details of the security update or other corrective measures made available to remedy the vulnerability

*(Note: for severe incidents affecting the product's security, there is an analogous obligation with an additional intermediate progress report if resolution is not achieved within the initial timeframes — but for a discovered actively exploited vulnerability specifically, the 24hr / 72hr / 14-day structure above applies.)*

## Obligation to notify affected users

In parallel to the regulatory notification, the CRA requires manufacturers to inform **affected users** of the actively exploited vulnerability, without undue delay, and after (or alongside) the regulatory notifications, including:
- Information about the vulnerability
- Where appropriate, corrective measures the user can take (mitigations, workarounds)
- Once available, the security update needed to remediate the issue

This user notification obligation exists independently and should not be delayed simply because the 14-day final report to ENISA/CSIRT has not yet been filed — users need actionable mitigation information as soon as it's responsibly available, balanced against the risk of premature public disclosure aiding further exploitation.

## What you should do right now, practically

1. **Establish "awareness" timestamp** — document precisely when your organization became aware of active exploitation; this starts the clock for all three deadlines.
2. **File the 24-hour early warning immediately** with your national CSIRT/ENISA reporting channel, even with incomplete information — the CRA expects an initial notification with best-available information, to be supplemented later.
3. **Activate your incident response and vulnerability handling process** (which you are required to have under Annex I Part II) to investigate scope, root cause, and affected product versions.
4. **Prepare the 72-hour follow-up** with severity/impact assessment and any interim mitigations (e.g., a configuration workaround) you can offer to customers immediately, even before a permanent fix is ready.
5. **Develop and ship the security update or corrective action**, then file the **14-day final report** once that corrective measure is available.
6. **Notify affected customers/users directly** in parallel — through your product's update channel, direct communication, or public advisory — with practical mitigation guidance.
7. **Coordinate with any relevant CSIRT/researcher** if the vulnerability was originally reported through your coordinated vulnerability disclosure (CVD) process, to align on responsible disclosure timing.
8. Cross-check whether this also triggers obligations under other regimes you may be subject to (e.g., NIS2 incident reporting if you or your customers are also regulated entities, or product liability/safety reporting requirements).

## Key takeaway

For an actively exploited vulnerability, you owe ENISA/your national CSIRT a notification within **24 hours** (early warning), **72 hours** (detailed notification), and a **14-day final report** after a fix is available — plus a separate, timely obligation to inform affected users with mitigation guidance. Missing these deadlines is itself a compliance failure independent of the underlying vulnerability, so your internal incident response process needs a clock that starts the moment anyone in the organization becomes aware of active exploitation, not when it's "confirmed" or "fully investigated."
