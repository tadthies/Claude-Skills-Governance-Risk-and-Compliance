# Handling a Brazilian Data Deletion Request Under LGPD

A user in Brazil emailing to request deletion of "all their personal data" is exercising rights under **LGPD Art. 18, IV and VI**. Here's how to handle it, from intake to closure.

---

## Step-by-Step Workflow

### Step 1 — Verify Identity
Before acting on the request, confirm the requestor is who they claim to be (e.g., verify via the email address on file, or request additional confirmation such as a login/account verification). This protects against fraudulent deletion requests and is implicit in the controller's accountability duty (Art. 6, X — Accountability).

**Timeline:** Do this immediately upon receipt; don't let verification delay eat into your response clock unnecessarily.

### Step 2 — Classify the Request
This is a deletion request under:
- **Art. 18, IV** — deletion of unnecessary, excessive, or non-compliant data, and
- **Art. 18, VI** — deletion of data processed with the data subject's **consent**, upon revocation.

Note: if any of the data was processed under a *different* legal basis (e.g., **Art. 7, V — contract**, or **Art. 7, II — legal obligation**), the Art. 18, VI deletion right does not automatically apply to that data — see Step 3.

### Step 3 — Check for Retention Exceptions (Art. 16)
Not all data must be deleted just because the subject asked. LGPD permits retention despite a deletion request where necessary for:
- **Art. 16, I** — compliance with a legal or regulatory obligation by the controller
- **Art. 16, II** — study by a research body (with anonymisation where possible)
- **Art. 16, III** — transfer to a third party, provided LGPD data protection requirements are respected
- **Art. 16, IV** — exclusive use of the controller, access by third parties barred, and the data is anonymised

Practically, for a CRM/email/analytics stack, this means:
- Financial or tax records tied to invoices (if any exist in the CRM) may need to be retained per Brazilian legal/regulatory obligations (Art. 16, I) — delete the marketing/profile data but retain only what's legally mandated, and inform the user of this partial exception.
- Data kept purely for legitimate interest or contract performance that has since ended should generally be deleted along with the consent-based data, unless another Art. 7 basis with a lawful retention need still applies.

**Timeline:** Complete this assessment before responding — ideally within the first few days, since it determines the scope of what you can promise to delete.

### Step 4 — Locate the Data Across All Systems
Map the data subject's personal data across every system you named:

| System | Likely Data Categories | Action |
|--------|------------------------|--------|
| **CRM** | Name, email, phone, deal/interaction history, notes | Delete or anonymise subject record; check for legal-hold/financial records exception (Art. 16, I) |
| **Email platform** (e.g., marketing/ESP) | Email address, campaign engagement history, subscription status | Delete/suppress from all lists; remove from send history where feasible; ensure suppression doesn't itself retain more data than necessary |
| **Analytics tool** | Behavioral/usage data tied to identifiers (cookies, user ID, IP) | Delete or anonymise identifiers; if data is already aggregated/anonymised such that the individual is no longer identifiable, LGPD no longer applies to it (Art. 5, III definition of personal data requires identifiability) |

Also check for **any processors** acting on your behalf (Art. 39) — as controller, you are responsible for instructing your processors (CRM vendor, ESP, analytics vendor) to also delete the data per your instructions, per your data processing agreements.

### Step 5 — Execute Deletion (or Anonymisation) and Instruct Processors
- Delete/anonymise the data in each system identified in Step 4.
- Send deletion instructions to any third-party processors or sub-processors holding the data on your behalf (Art. 39 — processors must act only per controller instructions).
- If full deletion isn't possible for a given data element due to an Art. 16 exception, **anonymise** it instead where feasible, so it no longer constitutes "personal data."

### Step 6 — Respond to the Data Subject
Reply to the user confirming:
- What was deleted and from which systems
- Any data retained under an Art. 16 exception, and the specific legal basis for retention (be transparent — this is required by the Transparency principle, Art. 6, VI)
- Confirmation that instructions were sent to relevant processors/vendors

**Timeline:** LGPD requires response **"without undue delay"** for deletion requests (Art. 18, IV/VI). ANPD guidance and practice generally treat this consistently with the **15-day** benchmark set for full access reports (Art. 19) — best practice is to complete deletion and respond within **15 days**, sooner if operationally feasible.

### Step 7 — Log the Request for Accountability
Record in your request log (per the Accountability principle, Art. 6, X):
- Date of request and identity verification method
- Systems affected and actions taken
- Any data retained and the Art. 16 basis cited
- Date of response to data subject

This record demonstrates compliance if ANPD later asks the controller to justify how the request was handled (Art. 18, §3º/§4º allows refusal only where LGPD permits, and controllers must be able to justify any refusal to ANPD).

---

## Summary Table

| Step | Action | Timeline |
|------|--------|----------|
| 1 | Verify requestor identity | Immediately on receipt |
| 2 | Classify request (Art. 18, IV/VI) | Same day |
| 3 | Check Art. 16 retention exceptions | Within first few days |
| 4 | Locate data in CRM, email platform, analytics tool | Within first week |
| 5 | Delete/anonymise data; instruct processors (Art. 39) | Within first week |
| 6 | Respond to data subject with confirmation/exceptions | Without undue delay — target 15 days |
| 7 | Log request and actions taken (Art. 6, X) | Upon completion |

---

## Key Notes
- **No fee** may be charged for exercising this right (Art. 19).
- If any data is genuinely needed for an ongoing legal obligation (e.g., Brazilian tax/invoice retention rules), delete everything else and clearly explain the narrower retention to the user — do not use this as a blanket excuse to retain more than necessary (Necessity principle, Art. 6, III).
- If your CRM, email platform, or analytics tool are third-party vendors acting as **processors**, review your contracts/DPAs now to confirm they support deletion-on-instruction — this is a good moment to close any gaps.
- If the analytics tool only holds pseudonymous/aggregated data where the individual cannot reasonably be re-identified, it may already fall outside the definition of "personal data" (Art. 5, III) — but if any identifier (user ID, device ID, IP) ties back to the individual, it is in scope and must be deleted or anonymised.
