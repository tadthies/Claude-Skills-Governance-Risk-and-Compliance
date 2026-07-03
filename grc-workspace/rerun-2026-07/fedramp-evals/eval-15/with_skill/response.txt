# FedRAMP Vulnerability Remediation Timeframes & POA&M Entry Guidance

## 1. FedRAMP Remediation SLAs

| Risk Rating | Remediation Deadline (from detection) |
|---|---|
| **Critical** | **30 calendar days** |
| **High** | **90 calendar days** |
| Moderate | 180 calendar days |
| Low | 365 calendar days |

> **Note on conflicting figures**: You may also see a shorter SLA table circulating (Critical = 15 days, High = 30 days, Moderate = 90 days) — this reflects an older/alternate framing of FedRAMP timeframes. The table above (30/90/180/365 days) is the one to use for POA&M vulnerability scan findings per current FedRAMP PMO guidance. **Confirm the exact figures against the current official FedRAMP POA&M template and your agency AO's guidance before finalizing**, since deadlines are a frequent point of scrutiny during 3PAO and ConMon review, and this is one of the most common areas where CSPs get dinged for using outdated SLA references.

Since your finding is a **Critical** vulnerability scan finding, it must be remediated within **30 calendar days of the original detection date** (i.e., the date the scan identified it) — not 30 days from when the POA&M entry was written.

---

## 2. Why This Happens (Root Cause Framing)

A POA&M item stating "vulnerability scan findings not remediated within required timeframes for Critical vulnerabilities" is itself a **finding about your vulnerability management process**, not just a single CVE. Before writing the entry, clarify:

- Is this a **single Critical CVE** that blew past its 30-day SLA, or a **systemic pattern** (e.g., recurring late remediation across multiple scan cycles)?
- If it's systemic, you likely need a POA&M item for the **process gap** (e.g., RA-5, SI-2 control weakness — patch/vulnerability management process) *in addition to* individual POA&M items for each unremediated CVE.
- Each individual vulnerability should still get **its own POA&M row** — do not bundle multiple CVEs into a single line item.

---

## 3. How to Write the POA&M Entry

### Required Fields (per FedRAMP POA&M template)

| Field | Guidance for This Finding |
|---|---|
| **POA&M Item ID** | Unique ID, e.g., `V-2026-041` (use your organization's existing numbering convention) |
| **Controls** | Typically **RA-5** (Vulnerability Scanning) and/or **SI-2** (Flaw Remediation); add others if the specific CVE maps to another control family |
| **Weakness Name** | Short, specific — e.g., "Critical vulnerability CVE-2026-XXXXX unremediated beyond 30-day SLA on [asset/component]" |
| **Weakness Description** | Detailed: CVE ID(s), affected asset(s)/host(s), CVSS score, what the vulnerability allows (e.g., RCE), scan tool/source, and confirmation that the 30-day Critical SLA was missed and by how many days |
| **Point of Contact** | Named individual/team owning remediation (e.g., patching/infra team lead) |
| **Resources Required** | What's needed to fix it — patch deployment window, maintenance approval, vendor patch, staff hours, testing environment |
| **Overall Remediation Plan** | Concrete steps: e.g., "Apply vendor patch X.Y.Z in next maintenance window; validate via rescan; if no vendor patch available, apply compensating control (WAF rule / network isolation) pending fix" |
| **Original Detection Date** | The date the scan first identified the vulnerability (this is the SLA clock start — critical to get right) |
| **Scheduled Completion Date** | Target remediation date. If already past the 30-day SLA, this must reflect a **revised, realistic date** with justification for the delay |
| **Milestone Changes** | Log every date change with a reason (e.g., "Original target 2026-06-15 missed due to vendor patch delay; revised to 2026-07-20") |
| **Status** | `Open` (or `Vendor Dependency` if a third-party patch is pending) |
| **Comments** | Explain the SLA miss, any interim compensating controls in place, and escalation status |
| **Risk Rating (Original)** | **Critical** |
| **Risk Adjustment** | Leave blank unless a formal Deviation Request (Risk Adjustment) has been approved by the AO — do not self-adjust risk to make the SLA miss look less severe |
| **False Positive** | No (unless you have evidence it's a false positive, in which case pursue a Deviation Request, not a standard POA&M closure) |
| **Operational Requirement** | No (unless remediation would break functionality and a documented OR deviation is being pursued) |

### Example Row (illustrative)

> **POA&M Item ID:** V-2026-041
> **Controls:** RA-5, SI-2
> **Weakness Name:** Critical vulnerability (CVE-2026-30112) unremediated beyond 30-day SLA — prod web app server WEB-03
> **Weakness Description:** Monthly vulnerability scan (Qualys, run 2026-05-28) identified CVE-2026-30112 (CVSS 9.8, remote code execution) on WEB-03. Vendor patch available since 2026-06-02 but not yet applied. Original 30-day remediation deadline (2026-06-27) was missed; as of 2026-07-03 the item is 6 days past SLA.
> **Point of Contact:** J. Alvarez, Infrastructure Team
> **Resources Required:** Change-approval for emergency patch window; 2 hours staff time; post-patch rescan
> **Overall Remediation Plan:** Deploy vendor patch during emergency maintenance window scheduled 2026-07-08; validate remediation via authenticated rescan within 48 hours; update POA&M with evidence upon closure
> **Original Detection Date:** 2026-05-28
> **Scheduled Completion Date:** 2026-07-08 (revised from 2026-06-27)
> **Milestone Changes:** 2026-06-27 → 2026-07-08: delayed due to change-freeze during Q2 close; escalated to CAB for expedited approval
> **Status:** Open
> **Comments:** SLA breach reported to AO per ConMon monthly submission; compensating control (WAF rule blocking known exploit pattern) applied 2026-06-20 pending patch
> **Risk Rating (Original):** Critical
> **Risk Adjustment:** N/A
> **False Positive:** No
> **Operational Requirement:** No

*(Use official FedRAMP templates from fedramp.gov — this content should be inserted into the appropriate template section.)*

---

## 4. Key Points to Flag to Your AO / Compliance Lead

1. **You are already past SLA** — this needs to be transparently disclosed in your next monthly ConMon submission, not hidden. Late Critical findings draw AO scrutiny and, if patterns persist, can jeopardize ATO status.
2. **Root-cause it** — if Critical findings are routinely missing the 30-day window, consider opening a separate POA&M item against your vulnerability/patch management process (RA-5/SI-2) to show you're addressing the systemic issue, not just the symptom.
3. **Consider a compensating control** — if the underlying patch can't be applied immediately, document an interim mitigation (network isolation, WAF rule, disabling the vulnerable service) and note it in Comments; this demonstrates active risk management even while the SLA clock has lapsed.
4. **If you believe the SLA doesn't apply** (false positive or the risk is genuinely lower) — that requires a formal **Deviation Request** with AO approval; you cannot just downgrade risk rating unilaterally in the POA&M.
5. **Confirm the authoritative SLA table** with your 3PAO/AO given the discrepancy noted above — using the wrong deadline in your remediation plan is itself a documentation error reviewers will catch.
