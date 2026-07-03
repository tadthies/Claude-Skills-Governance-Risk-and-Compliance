# Handling a CCPA/CPRA Right to Know and Right to Delete Request

A California resident has submitted both a Right to Know (§1798.110) and a Right to Delete (§1798.105) request simultaneously. Here is a complete, step-by-step walkthrough of your obligations under the CCPA as amended by the CPRA.

---

## Step 1: Acknowledge Receipt and Start the Clock

Upon receiving the requests, immediately log the date of receipt — this is Day 0 for your 45-calendar-day response window. Send the consumer an acknowledgment confirming you received both requests. This acknowledgment itself does not need to be a full response, but it signals that the process has begun and sets expectations.

Both the Right to Know and the Right to Delete run concurrently from the same receipt date. You do not need to handle them sequentially.

---

## Step 2: Identity Verification

Before disclosing any personal information or deleting any records, you must verify the consumer's identity. The CCPA requires that verification match at least two data points you already hold on file for the consumer. This protects against fraudulent requests and unauthorized disclosure or deletion.

**Standard verification process:**

- Ask the consumer to provide at least two pieces of identifying information that you already hold — for example:
  - Full name as it appears in your records
  - Email address associated with their account
  - Phone number on file
  - Account number, loyalty ID, or another unique identifier
  - Date of birth (if collected)
  - Address (billing or shipping)

- Cross-reference the provided data points against your existing records. Both data points must match before you proceed.

- Do not require the consumer to create an account if they do not already have one. If a consumer submits a request without an account, you may ask for data points but must still process the request to the extent feasible.

**Elevated verification for sensitive information:**

For a Right to Know request that involves disclosure of sensitive categories of personal information (e.g., Social Security numbers, financial account details, health information, precise geolocation), you should apply a higher standard of verification — potentially requiring a signed declaration under penalty of perjury or additional corroborating data points.

**If identity cannot be verified:**

If you are unable to verify the consumer's identity after a good-faith attempt, you must deny the request but inform the consumer of your inability to verify and that this is the reason for denial. Document this outcome.

---

## Step 3: Responding to the Right to Know Request (§1798.110)

Once identity is verified, compile and disclose the following for the preceding 12 months (or longer if required by the CPRA):

1. The categories of personal information you have collected about the consumer
2. The categories of sources from which the personal information was collected
3. The business or commercial purpose for collecting, selling, or sharing the personal information
4. The categories of third parties to whom you disclosed the personal information
5. The specific pieces of personal information you hold about the consumer

Prepare this disclosure in a portable, readily usable format where feasible (e.g., a structured CSV, JSON export, or a clearly formatted document).

---

## Step 4: Responding to the Right to Delete Request (§1798.105)

Evaluate whether any exceptions to deletion apply before proceeding. If no exceptions apply, initiate deletion. If exceptions apply to only some of the data, delete what is not covered and explain what was retained and why.

### Valid Exceptions to the Right to Delete

You are permitted to retain personal information — and must decline the deletion request with respect to that information — in the following circumstances (among others):

**Exception 1: Completing a Transaction or Fulfilling a Contract**
If the personal information is reasonably necessary to complete a transaction the consumer initiated, fulfill a contract, or provide a good or service that the consumer requested, you may retain it for that purpose. For example, if an order is still in transit, you may retain the shipping address and order details until fulfillment is complete.

**Exception 2: Detecting Security Incidents, Protecting Against Malicious, Deceptive, Fraudulent, or Illegal Activity**
You may retain personal information that is necessary to detect, prevent, investigate, or respond to security incidents or illegal activity. For example, if a consumer's account has been flagged in an active fraud investigation, deletion could impair your ability to pursue that investigation or comply with law enforcement obligations.

**Exception 3: Complying with a Legal Obligation**
If a federal, state, or local law requires you to retain certain records — such as tax records, financial transaction records under the Bank Secrecy Act, employment records, or healthcare records under HIPAA — you are not required to delete that information. Deletion would place you in violation of the conflicting legal mandate. Document the specific legal obligation as the basis for retaining that data.

**Additional exceptions (non-exhaustive):**
- Debugging to identify and repair errors that impair existing intended functionality
- Exercising free speech or ensuring another person's right to exercise free speech
- Scientific, historical, or statistical research in the public interest that adheres to ethical standards
- Internal uses reasonably aligned with the consumer's expectations based on the consumer's relationship with your business

---

## Step 5: Direct Service Providers AND Contractors to Delete

This is a critical and often overlooked obligation. Upon receiving a verified deletion request, you must direct **all service providers and contractors** that have received the consumer's personal information from you to also delete that information. This extends the deletion obligation downstream throughout your data supply chain.

**Practical steps:**

1. Identify every service provider and contractor that has received this consumer's personal information — cloud hosting vendors, analytics platforms, CRM providers, email service providers, advertising partners, etc.
2. Send deletion instructions to each. Most modern data processors accept deletion requests via API, support ticket, or formal written notice under the terms of your Data Processing Agreement (DPA).
3. Log each instruction sent and the response/confirmation received.
4. If a service provider or contractor has their own valid exception (e.g., a legal hold), they should notify you of that exception.

Note: You are not required to delete information a service provider holds solely for its own internal operational purposes consistent with the context in which you provided it — but you must still instruct them, and they must evaluate exceptions on their end.

---

## Step 6: Respond Within the Deadline

**45-calendar-day deadline:** You must respond substantively to both the Right to Know disclosure and the Right to Delete request within 45 calendar days of the date of receipt.

**45-day extension:** If you need additional time due to complexity or volume of requests, you may extend the response period by an additional 45 calendar days (for a total of 90 calendar days), but only if:
- You notify the consumer within the original 45-day window of the need for the extension, and
- You provide the reason for the extension in that notice.

Failure to respond within the deadline — without invoking the extension — constitutes a violation of the CCPA.

---

## Step 7: Confirm Deletion or Explain the Exception Invoked

Your final response to the Right to Delete request must do one of two things:

- **Confirm deletion:** Inform the consumer that their personal information has been deleted and that you have directed your service providers and contractors to delete it as well.
- **Explain the exception:** If you are retaining some or all of the personal information under an applicable exception, you must inform the consumer of the specific exception(s) you are invoking and explain why they apply. You do not have to disclose the retained information, but you must be transparent that retention is occurring and why.

For the Right to Know response, provide the compiled disclosure in a clear, accessible format.

---

## Step 8: No Fees — Free of Charge (Up to Twice Per 12-Month Period)

Both the Right to Know and the Right to Delete request must be fulfilled **free of charge** to the consumer. You may not charge a fee, create barriers to access, or impose costs for complying with these requests.

The CCPA entitles consumers to submit each type of request **up to twice per 12-month period** at no cost. If a consumer submits more than two requests of the same type within a 12-month period, you may charge a reasonable fee for additional requests or decline to respond, provided you notify the consumer that you will not be acting on the request and why.

---

## Summary Checklist

| Step | Action | Deadline |
|------|--------|----------|
| 1 | Acknowledge receipt; log Day 0 | Immediately |
| 2 | Verify identity (2+ matching data points) | Before any disclosure or deletion |
| 3 | Compile Right to Know disclosure | Within 45 days (extendable +45 with notice) |
| 4 | Evaluate deletion exceptions; delete non-exempt PI | Within 45 days (extendable +45 with notice) |
| 5 | Direct service providers AND contractors to delete | Concurrent with or immediately following your deletion |
| 6 | Send substantive response to both requests | Within 45 days (or 90 with timely extension notice) |
| 7 | Confirm deletion or invoke and explain exception | Part of Step 6 response |
| 8 | Charge no fee (free up to twice per 12-month period) | Ongoing obligation |

---

## Key Legal Citations

- Cal. Civ. Code §1798.110 — Right to Know
- Cal. Civ. Code §1798.105 — Right to Delete
- Cal. Civ. Code §1798.105(d) — Exceptions to deletion
- Cal. Civ. Code §1798.125 — Non-discrimination
- Cal. Code Regs. tit. 11, §§7100–7102 — CPRA verification and timing rules
