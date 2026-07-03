# C3PAO Assessment — 8 Practices NOT MET: Can You Still Get Certified?

Short answer: **it depends entirely on which 8 practices they are.** Whether certification is still achievable hinges on whether any of the findings fall into the small set of "critical" practices that can never be left open, and on how many *non-critical* NOT MET findings a C3PAO/CMMC-AB will allow into a Plan of Action & Milestones (POA&M) at certification.

## Step 1: Check Whether Any Critical Practices Are Among the 8

The following practices **must be fully MET before any certification (conditional or final) can be issued** — they are never POA&M-eligible, regardless of your overall score:

| Practice ID | Domain | Requirement |
|---|---|---|
| AC.L2-3.1.3 | Access Control | Control the flow of CUI in accordance with approved authorizations |
| IA.L2-3.5.3 | Identification & Authentication | Multifactor authentication |
| SC.L2-3.13.8 | System & Communications Protection | Encryption of CUI in transit (FIPS-validated) |
| SC.L2-3.13.11 | System & Communications Protection | FIPS-validated cryptography |
| SI.L2-3.14.6 | System & Information Integrity | Monitor systems to detect attacks |
| AU.L2-3.3.1 | Audit & Accountability | Audit logging capability |
| IR.L2-3.6.1 | Incident Response | Operational incident-handling capability |

**If any of your 8 NOT MET findings are on this list, certification cannot be issued until those specific items are remediated and re-verified** — no conditional certification path exists for them. You would need to remediate, provide evidence of closure, and go back to the C3PAO for re-assessment of those specific practices (the scope of a re-assessment for isolated findings is typically narrower than a full initial assessment, but it is still a formal C3PAO activity, not a self-certification).

## Step 2: For Non-Critical Findings — Conditional Certification Is Possible

If none (or only some) of your 8 findings are on the critical list above, **conditional certification is a realistic path**:

- **Conditional certification** = CMMC-AB issues certification with the *non-critical* NOT MET practices documented in an approved POA&M, while critical practices are all MET.
- **Final certification** = all 110 practices MET, no open POA&M items, valid for **3 years**.

There is a **limit on how many non-critical practices can remain open** in a POA&M at certification — this is not unlimited. The exact numeric cap is set by CMMC-AB policy; treat any large number of open findings (8 is on the higher end) as a signal to push hard on remediating as many as possible *before* the POA&M is finalized, since assessors and CMMC-AB reviewers scrutinize POA&M volume as a proxy for overall program maturity. A cluster of 8 findings, even if all non-critical, may also prompt the C3PAO to ask harder questions about whether your SSP and remediation plan are realistic.

## Step 3: Minimum Score Requirement

Certification is not purely a pass/fail on individual practices — your **SPRS score** matters too:
- Starting score: 110 (all practices MET)
- Each NOT MET practice deducts its assigned weight: **5, 3, or 1 points**, with the highest-impact practices (including several of the critical ones listed above) carrying 5-point deductions
- **There is no partial credit** — a practice is either fully MET or it takes the full deduction
- Estimate your resulting score by mapping each of the 8 findings to its point value. If several of your findings are 5-point practices, your score could be pulled down substantially even if none are on the "never POA&M" critical list — a low score combined with a large POA&M is a weaker certification package and increases the odds of a "no certification, remediate and reschedule" outcome from the C3PAO.
- Action: get the specific point value for each of the 8 findings from your C3PAO's Findings Report and calculate your actual resulting score before deciding on strategy.

## Step 4: POA&M Closeout Timeline

If conditional certification is granted:
- **180-day clock** starts on the certification date.
- All POA&M items must be fully remediated, with evidence, within that window.
- **Failure to close out within 180 days triggers certification revocation** — this is a hard deadline, not a target.
- POA&M items should be updated monthly (stale POA&M entries raise assessor/CMMC-AB concern even before the deadline).
- Each POA&M entry should document root cause (not just the symptom), remediation steps, milestones, scheduled completion, resources, and evidence of closure — this format is what CMMC-AB will expect to see when you report closure.

## Recommended Immediate Actions

1. **Get the full Findings Report** from your C3PAO and map each of the 8 NOT MET items against the critical-practice list above. This single step determines your realistic path.
2. **If any critical practices are among the 8**: prioritize those for immediate remediation — MFA and FIPS-validated encryption gaps in particular are common, fast-to-fix items (deploy MFA broadly, verify actual FIPS 140-2/3 module usage rather than generic "AES-256" claims). You will need re-verification by the C3PAO before certification of any kind is issued.
3. **If all 8 are non-critical**: build a POA&M immediately, with realistic milestones inside the 180-day window, and calculate your resulting SPRS score to understand how the C3PAO/CMMC-AB is likely to view the package.
4. **Either way**, do not treat "conditional certification" as a finish line — the 180-day closeout is a hard compliance deadline with revocation as the consequence of missing it. Assign an owner and set monthly check-ins now.
5. Confirm with your C3PAO directly on the current numeric cap for POA&M-eligible items and their specific process for re-verifying closed items — this is administered by CMMC-AB policy and your C3PAO's engagement letter should reflect current requirements at time of assessment.

---
*This is general compliance guidance, not legal advice. Final determinations on certification eligibility rest with the C3PAO and CMMC-AB. Engage your C3PAO's lead assessor directly to confirm findings classification and available paths forward.*
