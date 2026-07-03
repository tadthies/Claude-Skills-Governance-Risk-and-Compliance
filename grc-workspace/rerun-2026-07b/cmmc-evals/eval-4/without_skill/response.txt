# 8 Practices NOT MET on Your CMMC Level 2 C3PAO Assessment — Can You Still Get Certified?

Short answer: **Possibly yes** — CMMC Level 2 has a mechanism called **conditional certification** that allows an Organization Seeking Certification (OSC) to receive a conditional Level 2 certification even with some practices NOT MET, *if* those deficiencies qualify for a Plan of Action & Milestones (POA&M) and your score meets the minimum threshold. Whether your specific 8 NOT MET practices qualify depends on which practices they are and what your resulting SPRS score is. Below is the full framework.

---

## 1. The Conditional Certification Concept

Under the CMMC Level 2 assessment scheme (32 CFR Part 170), an OSC does **not** need a perfect 110/110 score to become certified. Instead, there are three possible outcomes of a C3PAO assessment:

- **Final (Full) Certification** — all 110 practices assessed as MET (or the applicable subset for a scoped environment), no open POA&M items.
- **Conditional Certification** — some practices are NOT MET, but they are POA&M-eligible, the resulting score meets the minimum threshold, and the OSC commits to closing out the deficiencies within the allowed window (POA&M closeout assessment).
- **Not Certified** — either the score falls below the minimum threshold, or one or more NOT MET practices are not POA&M-eligible (i.e., they are practices the rule requires to be MET at the time of the initial assessment, with no conditional path).

Conditional certification exists specifically to give organizations a bridge: it recognizes that they have a documented, time-bound plan to remediate remaining gaps, while still allowing them to be awarded contracts/maintain eligibility in the interim — but it is **not indefinite**. It converts to Final Certification only after a successful POA&M closeout assessment, or it lapses if the deadline is missed.

---

## 2. Minimum SPRS Score Requirement to be POA&M-Eligible

CMMC Level 2 scoring is based on the DoD Assessment Methodology (the same 110-point scale used for NIST SP 800-171 self-assessments reported to SPRS):

- **Total possible points: 110** (each of the 110 security requirements is assigned a weight of 1, 3, or 5 points based on criticality; you start at 110 and points are subtracted for each NOT MET practice).
- **Minimum score to be eligible for conditional certification (POA&M path): 88 points.**
  - This reflects a maximum point deficit of 22 points — i.e., no more than roughly 20% of total achievable points can be missing.
  - If your score is below 88, you are **not eligible** for conditional certification regardless of which practices are open — you must remediate first and be reassessed before a certification decision can be issued.
- Your 8 NOT MET practices will each carry a weight of 1, 3, or 5 points depending on which specific control is affected. You'll need to total the point deductions from your assessment report to confirm whether your score lands at or above 88.

**Practical check:** Ask your C3PAO/Lead Assessor for the exact SPRS score calculated from your assessment (they should provide this as part of the assessment results package). If your 8 gaps are all low-weight (1-point) practices, you could still be well above 88. If several are 5-point practices, you may be close to or below the threshold.

---

## 3. Practices That Are NOT POA&M-Eligible

Not every NOT MET practice can go on a POA&M — this is the critical gate most organizations miss. The CMMC rule designates certain high-criticality practices as **ineligible for POA&M treatment**, meaning they must be MET at the time of the assessment for you to receive *any* certification (conditional or final). These are generally the practices identified as foundational/highest-risk controls — historically referenced as the "NOT ELIGIBLE FOR POA&M" list published alongside the DoD Assessment Methodology, and they map to:

- **All 5-point weighted practices** are treated as ineligible for POA&M in the CMMC scheme — these represent the practices considered most critical to protecting CUI (e.g., controls central to access control enforcement, boundary protection, and multifactor authentication—type requirements). If any of your 8 NOT MET practices fall into the 5-point category, that finding **cannot** be POA&M'd — it must be remediated and verified MET before certification (conditional or final) can be issued.
- **3-point and 1-point weighted practices** are generally POA&M-eligible, subject to the overall 88-point minimum and the cap on total number of open POA&M items (commonly limited — check your assessment package, as CMMC guidance also constrains how many practices total may remain open, not just the score).

**Action item:** Go through your assessment findings and identify the point value assigned to each of the 8 NOT MET practices. Any practice at the 5-point tier is a hard blocker for conditional certification until remediated. Your C3PAO/Lead Assessor is required to tell you which findings are POA&M-eligible versus which are not — request this breakdown explicitly if it wasn't included in your results package.

---

## 4. The 180-Day POA&M Closeout Timeline

If your 8 NOT MET practices are all POA&M-eligible and your score is at or above 88:

- You will be issued a **conditional Level 2 certification**, valid for **180 days** from the date of the conditional certification decision.
- During this window, you must remediate each open POA&M item and undergo a **POA&M closeout assessment** conducted by the same C3PAO (or as otherwise arranged) to verify that the previously NOT MET practices are now MET.
- The closeout assessment is narrower in scope than the original assessment — it focuses specifically on the practices that were open on the POA&M, not a full re-assessment of all 110 practices.
- Upon successful closeout (all POA&M items verified MET), your status converts from **conditional** to **Final Certification**, and the standard 3-year certification period is generally counted from the original assessment/conditional certification date (confirm exact anchor date with your C3PAO, as this can be a point of nuance).

---

## 5. What Happens If Closeout Isn't Achieved Within 180 Days

This is a hard deadline, not a soft target:

- If the POA&M items are **not** closed out (remediated and verified) within the 180-day window, the **conditional certification lapses/expires**.
- The OSC reverts to **not certified** status.
- You would need to restart the certification process — typically requiring a new assessment (full or significant re-assessment, at the C3PAO's discretion) rather than simply extending the clock. There is no automatic extension built into the scheme.
- Depending on your contract requirements, losing conditional status before closeout could jeopardize contract eligibility, award decisions, or option period exercises tied to a CMMC certification requirement — so treat the 180 days as a hard compliance deadline, not a planning buffer.

**Practical tip:** Don't wait until day 170 to request your closeout assessment. Build in scheduling lead time with your C3PAO (they have their own capacity constraints), and target internal remediation completion by roughly day 120–140 so you have buffer for evidence collection, internal validation, and the closeout assessment itself.

---

## 6. Practical Next Steps for Your 8 NOT MET Practices

1. **Get the full findings detail from your C3PAO.** For each of the 8 practices, confirm: (a) the specific NIST SP 800-171 control ID, (b) the point weight (1/3/5), (c) whether it's flagged as POA&M-eligible, and (d) the specific deficiency cited (what evidence was missing or what was observed).
2. **Calculate your actual SPRS score.** Sum the deducted points across all 8 findings and confirm you're at or above 88. If you're below 88, focus immediately on the fastest, highest-point-value remediations to get above threshold before any certification decision is finalized — talk to your C3PAO about timing.
3. **Isolate any 5-point (non-POA&M-eligible) findings.** These must be fixed and re-evidenced before the assessor can issue even a conditional certification. Prioritize these first, as they're a hard gate.
4. **Build a POA&M for the remaining eligible items** with: responsible owner, remediation action, target completion date (well inside 180 days), and interim risk mitigation if applicable. CMMC POA&Ms generally require a completion date within 180 days of the conditional certification — plan backward from that.
5. **Remediate and self-validate before requesting closeout.** Don't request the closeout assessment until you have internal evidence (screenshots, configs, policy docs, logs) proving each item is now MET — this reduces the risk of a failed closeout assessment.
6. **Schedule the closeout assessment early**, ideally with buffer before day 180, accounting for your C3PAO's scheduling availability.
7. **Track everything in a POA&M management log** — assessors will expect a clear audit trail showing when each gap was identified, the remediation steps taken, evidence of closure, and verification date.
8. **Loop in your prime contractor/contracting officer if relevant**, especially if a certification deadline is tied to a proposal, award, or option period — transparency here avoids surprises if closeout timing gets tight.

---

## Bottom Line

Yes, you can likely still get certified via the **conditional certification (POA&M) pathway** — but it hinges on two gates: (1) your SPRS score must be **≥ 88 points**, and (2) **none of your 8 NOT MET practices can be a non-POA&M-eligible (typically 5-point) practice**. If both conditions hold, you'll receive conditional certification with a strict **180-day clock** to close out the POA&M via a follow-up assessment — miss that window and the conditional certification lapses, reverting you to not-certified status. Get the point-weight and POA&M-eligibility breakdown from your C3PAO immediately so you know exactly which of the two gates apply to your situation.

*Note: This guidance reflects the general CMMC Level 2 conditional certification framework as established under 32 CFR Part 170 and the DoD Assessment Methodology. Confirm current specifics (exact ineligible-practice list, any interim rule updates, and your C3PAO's procedural requirements) directly with your C3PAO or via the official CMMC Accreditation Body (Cyber AB) guidance, as implementation details can be refined over time.*
