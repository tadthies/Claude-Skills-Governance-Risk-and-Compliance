## CRA Reporting Obligations — Actively Exploited Vulnerability

An actively exploited vulnerability (one you have become aware is being exploited in the wild, based on confirmed or credible intelligence) triggers a specific, time-boxed reporting obligation under CRA Annex I, Part II(8).

### Important timing note (as of today, 3 July 2026)

The CRA's vulnerability and incident reporting obligations to ENISA/CSIRTs become **legally binding on 11 September 2026**. If this discovery happens before that date, the formal statutory reporting duty as such is not yet in force — but you should treat it as best practice to follow the same process now regardless, since:
- The obligation is imminent (about 10 weeks away from today), and building the muscle memory/pipeline now avoids scrambling later.
- Your product's Coordinated Vulnerability Disclosure (CVD) policy and general Annex I Part II duty to address vulnerabilities "without undue delay" and issue free security updates already apply as a matter of good practice and contractual/market expectation, independent of the formal ENISA deadline.

If the discovery is on or after 11 September 2026, the obligations below are mandatory and enforceable (penalties up to €15M or 2.5% of global turnover for essential-requirement non-compliance).

### Who to report to

1. **ENISA** (EU Agency for Cybersecurity) — the central reporting point; ENISA forwards to relevant national CSIRTs.
2. **The relevant national CSIRT(s)** — the designated CSIRT(s) in the member state(s) where the product is on the market (e.g., BSI/CERT-Bund in Germany, ANSSI in France).
3. **Affected users** — direct notification as soon as practicable, in parallel with the regulatory reporting.

### Reporting timeline

| Deadline | Action Required |
|---|---|
| **T+24 hours** from becoming aware | **Early warning** to ENISA and the relevant national CSIRT: vulnerability identifier, affected product versions, brief description of the exploitation |
| **T+72 hours** from becoming aware | **Full notification**: nature of the vulnerability, severity/CVSS, affected product versions, available workarounds, and current remediation status |
| **T+14 days** after a fix becomes available | **Final report**: fix details, patch release notes, and lessons learned |
| As soon as practicable | **Notify affected users** of the vulnerability and remediation steps (this runs in parallel with the regulatory notifications, not after them) |

"Becoming aware" is the trigger — the clock starts when your organization has confirmed or credible intelligence that the vulnerability is being actively exploited, not necessarily when the vulnerability itself was first identified internally.

### What each report must contain

- **24-hour early warning:** vulnerability identifier (CVE if assigned), affected product(s) and version(s), a brief description of the nature of exploitation observed.
- **72-hour full notification:** all of the above plus severity/CVSS scoring, full list of affected versions, any available workarounds or mitigations, and the current status of your remediation effort.
- **14-day final report:** confirmation of the fix, patch release notes, and a summary of lessons learned / root cause.

### Practical steps to take right now

1. **Confirm exploitation** — validate the "actively exploited" determination (confirmed or credible threat intelligence) since this is what triggers the CRA clock, as opposed to a routine vulnerability disclosure.
2. **Start the 24-hour clock immediately** — file the early warning with ENISA and the applicable national CSIRT(s) covering every member state where the affected product is sold.
3. **Activate your internal vulnerability handling process** — pull from your SBOM/component inventory to scope exactly which product lines and versions are affected.
4. **Prepare the 72-hour full notification** in parallel — severity assessment, affected version list, workaround guidance, remediation plan and timeline.
5. **Notify affected users** as soon as practicable, using your published vulnerability/security contact channel — this should not wait for the regulatory deadlines.
6. **Develop and test the fix**, then release it as a free-of-charge, signed security update (per Annex I Part II) — bundle it independently of feature updates so users aren't forced to accept unrelated changes to get the security fix.
7. **File the 14-day final report** with ENISA/CSIRT once the fix is released, including patch notes and root-cause/lessons-learned summary.
8. **Cross-check your CVD/VDP policy** — if this vulnerability was originally reported by an external researcher, ensure your coordinated disclosure process and public point of contact were followed correctly; if you don't yet have a published VDP, this incident is a strong forcing function to stand one up immediately.
9. **Document everything** in your technical file — regulators can request evidence of the timeline and actions taken, and this record supports both compliance and any future market surveillance inquiry.

### If this also qualifies as a "severe security incident"

Separately from vulnerability reporting, if the exploitation has caused (or could cause) significant impact at scale — e.g., a supply-chain compromise, cryptographic key exposure, or large-scale unauthorised access — that is treated as a **severe security incident** under CRA, with its own (parallel, similarly-timed) reporting track: 24-hour early warning, 72-hour full notification, and a **1-month** post-incident report to ENISA and the national CSIRT. Assess whether both tracks apply; they are not mutually exclusive.

### Bottom line

Report to **ENISA and the relevant national CSIRT(s)** within **24 hours** (early warning), **72 hours** (full notification), and **14 days after the fix ships** (final report), while notifying affected users as soon as practicable throughout. This obligation becomes formally binding on 11 September 2026, but given how close that date is, I'd recommend operating as if the clock is already running.
