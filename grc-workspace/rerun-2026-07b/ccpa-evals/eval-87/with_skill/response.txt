# Handling a Combined Right-to-Know and Right-to-Delete Request

A consumer submitting both requests simultaneously is common — you should process them as two coordinated workflows sharing a single identity verification step, since both requests answer to the same underlying consumer.

## Step 1: Receive and Log Both Requests

Log the date/time of receipt for each request type — this starts the clock on your **45-calendar-day** response deadline (extendable once by another 45 days, with notice to the consumer within the original window explaining the delay).

## Step 2: Verify Identity

Because these are non-sensitive PI requests (assuming no SSN/financial credentials are specifically implicated), standard verification applies:
- **Match 2 data points** the business already holds on file for this consumer (e.g., name + email, or account number + phone number)
- If the request also touches sensitive PI or financial account data, escalate to **3 data points plus a signed declaration under penalty of perjury**
- If submitted through an **authorized agent**, additionally require written permission from the consumer, verify the agent's identity, and consider direct verification with the consumer as well

Do not proceed with either fulfillment step until identity is verified — this protects you from wrongful disclosure or wrongful deletion, both of which carry their own liability exposure.

## Step 3: Right to Know — Fulfillment

**What you must disclose:**
- Specific pieces of PI collected about this consumer
- Categories of PI collected
- Categories of sources PI was collected from
- Business/commercial purpose for collecting, selling, or sharing their PI
- Categories of third parties the PI was disclosed to
- Categories of PI sold or shared, and to which categories of third parties

**Workflow:**
1. Search all PI systems using the verified identifying data (CRM, order management, analytics, support tickets, ad tech/marketing platforms — anywhere the consumer's data could reasonably live)
2. Compile the full response across all systems
3. Apply any applicable exceptions (see below) and remove/redact accordingly
4. Deliver the response in a **portable, readily usable format** (e.g., downloadable CSV/PDF) within the 45-day window

**Exceptions you can invoke to withhold specific disclosures (not the whole request):**
- Disclosure would reveal a third party's trade secrets
- Disclosure would conflict with federal or state law
- The PI was collected for a single one-time transaction and not retained
- The PI is used solely for internal operations consistent with the context of collection
- The PI is used solely to complete the transaction for which it was collected

Note: the 12-month lookback restriction that used to apply to Right to Know has been effectively eliminated for PI collected after January 1, 2022 under CPRA — so for a July 2026 request, you should generally provide full history since that date, not just the trailing 12 months, unless a specific record predates that and falls under the old cap.

## Step 4: Right to Delete — Fulfillment (Two-Step Confirmation)

**Before deleting, check whether any exception lets you retain some or all of the PI:**
1. Necessary to complete a transaction or perform a contract with the consumer
2. Necessary to detect security incidents or protect against malicious/fraudulent/illegal activity
3. Necessary to debug/fix errors that impair intended functionality
4. Necessary to exercise free speech or ensure another consumer's free-speech rights
5. Required to comply with a legal obligation (§1798.145(a)) — e.g., tax or accounting record retention
6. Used solely for internal purposes compatible with the context of collection (narrow CPRA exception)
7. Used for research, journalism, or statistical purposes in the public interest

**Document your reasoning** for any exception invoked — this record is your evidence of compliance if the CPPA or AG later questions the decision (see the Ford enforcement action, where inadequate handling of access/deletion timelines led to a $375K penalty).

**Two-step workflow:**
1. **Execute**: For all PI not covered by an exception, delete it from your own systems AND send deletion instructions to every service provider and contractor holding a copy
2. **Confirm**: Notify the consumer within 45 days that deletion is complete — or, for any PI retained under an exception, explain which exception was invoked and why

You may retain a record of the deletion request itself (e.g., "consumer X requested deletion on [date]") — this does not contradict the deletion, since it's needed to prove compliance and prevent re-collection of the same data without consent.

## Step 5: Coordinate Timing Between the Two Requests

Since both requests share the same 45-day clock and the same identity verification, a practical sequence is:
1. Verify identity once, covering both requests
2. Fulfill the Right to Know disclosure first (or simultaneously) — this gives the consumer visibility into exactly what will be deleted
3. Execute deletion, applying exceptions as needed
4. Send a single combined response confirming (a) the PI disclosed, and (b) the deletion outcome/exceptions invoked

## Step 6: Free-of-Charge Rule

Both requests must be fulfilled at no charge, provided this consumer hasn't already exercised each right twice in the trailing 12 months. If they have, you may charge a reasonable fee only if the request is manifestly unfounded or excessive — document that determination carefully, as it's a frequent source of consumer complaints.

## Step 7: Record-Keeping

If your business processes PI for 10 million or more consumers/households, retain records of this request, your response, and any disclosures for **24 months**. Even if you're below that threshold, retaining these records is good practice for demonstrating compliance in the event of a CPPA inquiry.

## Common Pitfalls to Avoid
- **Missing the 45-day deadline** is independently actionable — the Ford enforcement action ($375K) was specifically about failing to process access/deletion requests within required timeframes, not a technical violation
- Forgetting to propagate deletion/correction instructions to **service providers and contractors** downstream
- Applying an exception to the entire request rather than only to the specific PI it covers
- Insufficient identity verification (skipping it entirely, or applying too weak a standard for sensitive data)

---
*This is general compliance guidance, not legal advice. Consult qualified counsel for your specific circumstances.*
