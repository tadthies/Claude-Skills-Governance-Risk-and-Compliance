# Subcontractors Without CMMC Certification: Flow-Down Obligations and Action Plan Under DFARS 252.204-7021

## Bottom line up front

If two of your subcontractors handle CUI and lack the CMMC certification level required for their portion of the work, you have a **flow-down compliance gap** that creates real risk to your prime contract — including False Claims Act exposure — and it needs to be resolved (or credibly on a remediation path with documented mitigation) **before you exercise the next option period**. Below is the legal basis, the verification obligation, the risk picture, and a concrete action plan.

---

## 1. What DFARS 252.204-7021 actually requires

DFARS 252.204-7021, *Cybersecurity Maturity Model Certification Requirements*, is the contract clause that operationalizes CMMC 2.0 in DoD contracts. Key obligations it imposes on you as the prime:

- **Maintain your own required CMMC certificate level** for the duration of the contract (not just at time of award).
- **Flow down the CMMC requirement to subcontractors "at all tiers"** — this is not optional and is not limited to first-tier subs. If a sub (or a sub's sub) will process, store, or transmit CUI in performance of the contract, the CMMC requirement flows down to them.
- **The required CMMC level flows down based on the information the subcontractor handles**, not automatically the prime's level:
  - Subs handling only Federal Contract Information (FCI) generally need **CMMC Level 1 (self-assessment)**.
  - Subs handling **CUI** generally need **CMMC Level 2** (self-assessment or third-party certification depending on the specific CUI/program requirements) or, for a defined subset of critical programs, **Level 3**.
- **Certification (or self-assessment, as applicable) must be current at the time of award and maintained throughout performance** — critically, this includes **at the time of exercising an option period**, which DoD and CMMC guidance treat as a triggering event requiring the status to be re-verified, not merely a continuation of prior status.
- You, the prime, are contractually responsible for **ensuring flow-down occurs** — i.e., inserting the clause (or its substantive requirements) into applicable subcontracts and confirming subcontractor compliance before allowing them to perform on CUI-related work.

In short: the clause does not let you say "that's the subcontractor's problem." The prime bears contractual responsibility for the *integrity of the supply chain's* CMMC posture as it relates to your prime contract.

---

## 2. Subcontractors must have the appropriate CMMC status *before* award/option exercise — not "in progress"

A common misconception is that a sub can be "working toward" certification. Under CMMC 2.0 as implemented via 252.204-7021:

- The applicable CMMC level (self-assessment score for Level 1/Level 2 self-assess scope, or a current, non-expired **C3PAO certification** for Level 2 certification-required scope or Level 3) generally must be **in place — not merely in process — at the point of award or contract action** (including option exercise, which DoD treats as a new contractual action for eligibility purposes).
- For Level 2 self-assessments, the score must be posted in **SPRS (Supplier Performance Risk System)** and be no older than the currency window (generally not older than 3 years, consistent with the affirmation/annual affirmation requirement).
- If your subs are handling CUI and have **no certification of any kind** — not even a self-assessment posted to SPRS — they do not currently meet the threshold to be awarded CUI-scope work, let alone to continue on it into a new option period.

This means: if you exercise the option period with these subs still performing CUI-related work without the required status, you are exercising a contract action while **out of compliance with a flow-down requirement your prime contract obligates you to enforce.**

---

## 3. Your obligation to verify — SPRS and beyond

The clause requires more than flowing down the contract language; it requires you to have a **reasonable basis to know your subs are actually compliant**. Practical verification steps that DoD auditors, DCMA, and your own contracts/legal team will expect to see documented:

- **Check SPRS** for the subcontractor's CAGE code to confirm a current, valid Level 1 self-assessment, Level 2 self-assessment, or Level 2/3 C3PAO certification is on file and unexpired.
- **Request written confirmation/attestation** from each subcontractor of their current CMMC status, including:
  - CMMC level achieved
  - Assessment/certification date and expiration
  - Scope of the assessed environment (does it actually cover the systems/boundary handling *your* CUI?)
  - POC and assessor/C3PAO information if applicable
- **Confirm the annual affirmation** has been submitted in SPRS (a separate requirement layered on top of the underlying assessment).
- **Review subcontract flow-down language** to confirm the CMMC clause (or a conforming equivalent) was actually included in the subcontract instrument — not just assumed.
- Maintain this verification as part of your **supply chain risk management (SCRM) file** — this documentation is exactly what you'll be asked to produce if DCMA, the DoD Office of Inspector General, or a qui tam relator's counsel comes asking.

Since you've discovered two subs with **no certification at all**, verification has clearly failed to date — which is itself a finding you need to address in your corrective action, not just the underlying gap.

---

## 4. Risk of proceeding without resolving this

### False Claims Act (FCA) exposure
This is the sharpest edge of the risk. Under the DoD's Civil Cyber-Fraud Initiative (CCFI), knowingly:
- Misrepresenting your (or your supply chain's) cybersecurity compliance status,
- Submitting invoices/certifications for work performed under a contract where required flow-down cyber requirements were not met, or
- Failing to disclose known non-compliance once discovered ("knowing" includes reckless disregard or deliberate ignorance — willful blindness does not protect you),

...can constitute a **false certification** giving rise to FCA liability (treble damages + per-claim penalties), and potentially qui tam exposure if a subcontractor employee or competitor reports it. **The fact that you have now discovered this gap is legally significant** — continuing to bill/perform without remediation or disclosure after actual knowledge substantially increases FCA risk compared to an undiscovered gap.

### Contract compliance / performance risk
- Exercising the option period without resolving the gap could constitute a **breach of your prime contract's flow-down clause obligations**, independent of FCA exposure.
- DCMA or the contracting officer could find this during a CMMC status review, audit, or CPARS assessment, resulting in negative past performance ratings.
- **Cure notices, show-cause letters, or default termination** are realistic possibilities if the government concludes CUI was handled by non-compliant subs and you knew or should have known.

### Termination / award risk
- The contracting officer may decline to exercise the option, or may exercise it with conditions (e.g., requiring immediate remediation, restricting the subs from CUI access).
- In egregious or unremediated cases, this could support a **termination for default** or **termination for convenience with cost consequences**, and potential referral for suspension/debarment consideration for the subs (and reputational/relationship risk for you as prime).

### Reputational/business risk
- Loss of trust with the contracting officer and program office.
- Risk to future awards if flagged as a systemic SCRM control failure.

---

## 5. Practical action plan before the next option period

Treat this as an active compliance incident with a remediation timeline, not a routine to-do item. Suggested sequence:

### Immediate (this week)
1. **Escalate internally** — notify contracts, legal/compliance, and program management now. Do not let this sit with a single program manager. Open a formal internal tracking record (this becomes your remediation evidence file).
2. **Determine actual CUI exposure** — precisely scope what CUI (if any) each subcontractor currently has access to, what systems/environments it touches, and since when. This determines urgency and whether interim containment is needed.
3. **Notify the two subcontractors formally**, in writing, that:
   - They are required under the flow-down clause to hold [Level 1 self-assessment / Level 2 self-assessment or certification / Level 3, as applicable to their scope] before continuing CUI-handling work.
   - They must immediately begin (or complete, if in progress) the appropriate CMMC path and provide evidence.
   - Provide a hard deadline tied to your option decision date.

### Short-term (before option decision)
4. **Consider interim risk mitigation / containment** for CUI while certification is pending:
   - Suspend or restrict the subs' access to CUI systems/data until they can demonstrate at least a compliant Level 1/Level 2 self-assessment posted in SPRS, if operationally feasible.
   - Route CUI-related tasks temporarily to a certified sub or in-house team, if available, to keep the prime contract compliant while the two subs catch up.
   - If full suspension isn't operationally possible, document a **risk-based rationale** for continued limited access (e.g., compensating controls, reduced scope) — this is defensible only if genuinely reasonable and documented, not a workaround.
5. **Verify and document current status via SPRS** for both subs now, and re-check immediately before the option decision date — don't rely on self-reported claims alone.
6. **Update/confirm subcontract flow-down language** — confirm the CMMC clause is explicitly and correctly incorporated in both subcontract agreements; amend if it was omitted or outdated (e.g., referencing interim CMMC rules rather than the current 2.0 framework).
7. **Require a remediation plan with milestones** from each subcontractor (assessment scheduling, C3PAO engagement if Level 2 certification-required, target completion date), and get it in writing.

### Before exercising the option
8. **Make a documented go/no-go decision**:
   - If both subs achieve the required status (self-assessment posted in SPRS, or C3PAO certification as applicable) before the option date — proceed, with the verification documented in the file.
   - If not fully resolved, consult legal/contracts on whether to: delay option exercise, exercise with a corrective action plan and interim mitigations documented and potentially disclosed to the contracting officer, or replace the non-compliant subs for the CUI-scope work.
9. **Consider proactive disclosure to the contracting officer** if remediation won't be complete by the option date. Voluntary, timely disclosure is viewed far more favorably (and reduces FCA "knowing" exposure) than the government discovering the gap independently. Loop in legal counsel before making this call — there are strategic and legal-privilege considerations in how disclosure is framed.
10. **Document everything** — the discovery, notifications, SPRS checks, subcontractor responses, mitigation steps, and final decision. This file is your best defense if later scrutinized, and demonstrates good-faith diligence rather than willful blindness.

### Ongoing
11. **Build a recurring SPRS verification cadence** (e.g., quarterly, and specifically before every option exercise or contract modification) into your subcontractor management/SCRM process so this doesn't recur.
12. **Update your subcontractor onboarding and periodic review process** to require CMMC status verification as a gating condition before any sub is granted CUI access, not just at initial award.

---

## Key takeaway

You now have actual knowledge of a flow-down compliance gap on a contract involving CUI. The clock that matters isn't just the option period — it's the fact that continued performance/billing with known non-compliance is where FCA risk accelerates. Prioritize: (1) containing CUI exposure now, (2) getting the subs moving on the correct CMMC path with documented deadlines, (3) verifying through SPRS rather than taking their word for it, and (4) looping in legal/contracts early enough to make a deliberate, documented decision — including possible proactive disclosure — before you exercise the option.

*This is general compliance guidance based on DFARS 252.204-7021 and CMMC 2.0 program requirements as generally understood; it is not legal advice. Given the FCA exposure and option-period timing, engage your government contracts counsel promptly to evaluate disclosure obligations and option-exercise strategy specific to your contract's terms.*
