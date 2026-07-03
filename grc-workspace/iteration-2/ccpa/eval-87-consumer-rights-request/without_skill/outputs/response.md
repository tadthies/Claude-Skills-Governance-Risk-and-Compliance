# Handling CCPA/CPRA Consumer Rights Requests: Right to Know and Right to Delete

## Overview

When a California resident submits a combined Right to Know (access) and Right to Delete request, your organization must handle both simultaneously and in parallel. Under the California Consumer Privacy Act (CCPA) as amended by the California Privacy Rights Act (CPRA), these are two distinct rights with overlapping — but not identical — procedures, timelines, and exceptions. The following is a step-by-step operational guide.

---

## Step 1: Acknowledge Receipt Immediately

Upon receiving the request, send a written acknowledgment within **10 business days**. The acknowledgment must:

- Confirm you have received the request.
- Provide an expected timeline for response (up to 45 calendar days).
- Explain how you will verify the consumer's identity before proceeding.
- Provide a reference or confirmation number for tracking.

This 10-business-day acknowledgment deadline is a firm CPRA requirement — do not miss it.

---

## Step 2: Identity Verification

### Why Verification Matters

You are prohibited from disclosing personal information — or deleting records in ways that could be irreversible — unless you have reasonably verified that the person submitting the request is actually the consumer (or their authorized agent). Verification protects both the consumer and your organization.

### Matching the Verification Level to the Sensitivity of the Request

The CPRA and CCPA regulations (11 CCR § 7060 et seq.) require that the verification standard be commensurate with the **sensitivity and nature of the personal information** and the risk of harm from improper disclosure or deletion.

**For a Right to Know request:**

- *Two-piece verification* is generally required: match at least two data points the consumer provides (e.g., name + email, name + phone number, name + account ID) against personal information you already hold. For sensitive categories of information (financial records, health data, precise geolocation), require a higher standard — three data points or a signed declaration under penalty of perjury.

**For a Right to Delete request:**

- Deletion is generally less sensitive than disclosure (since you are removing rather than releasing data), but courts and regulators have noted it can be irreversible, so reasonable verification is still required. Typically, two-piece verification is sufficient unless you maintain a particularly sensitive dataset.

### Verification Methods (Password-Protected Accounts vs. Non-Account Holders)

**If the consumer has a password-protected account with you:**

- Direct them to submit the request through their authenticated account portal. Successful login constitutes one layer of verification. You may still send a confirmation email to the address on file to create an additional verification signal.

**If no account exists (unregistered consumer):**

- Email the consumer and ask them to provide specific data points (e.g., address on file, last purchase date/amount, or other identifiers in your system). Match what they provide against your records. If you cannot match, you must notify the consumer within the standard timeline that you were unable to verify.

### Authorized Agents

If an authorized agent is submitting on the consumer's behalf:

- The agent must provide written proof of authorization (a signed permission from the consumer, or a power of attorney document).
- You may still require the consumer to directly verify their identity with you unless a valid power of attorney is on file.
- Do not require the agent to provide more information than necessary to verify the authorization.

### What to Do if You Cannot Verify

If you cannot verify the consumer's identity after a reasonable attempt:

- Do NOT disclose or delete the information.
- Notify the consumer that you were unable to verify and explain (in general terms) what information you would need.
- Document your verification attempts in your internal records.
- You are not required to treat an unverified request as if it were from the consumer.

---

## Step 3: Handle the Right to Know Request

### What Must Be Disclosed

Upon verified request, you must disclose, for the **12 months preceding the date of the request** (baseline obligation), and under CPRA for all personal information held at the time of request (if the consumer asks for prospective access):

1. The categories of personal information collected about the consumer.
2. The categories of sources from which the personal information was collected.
3. The business or commercial purpose for collecting, selling, or sharing the personal information.
4. The categories of third parties to whom the personal information was disclosed.
5. The specific pieces of personal information collected about that consumer (the "specific pieces" request).

The consumer can ask for categories, specific pieces, or both. A combined request generally warrants responding to both.

### Format of Disclosure

- Deliver the information in a readily usable format. If the request was made electronically, the default format should be electronic (e.g., a machine-readable, portable format such as CSV or JSON, when feasible).
- Do not require the consumer to create an account to receive their disclosure.

### Response Deadline

You have **45 calendar days** from receipt of the verifiable consumer request to respond. If you need more time due to complexity or volume, you may extend by an additional **45 calendar days** (90 days total), but you must notify the consumer of the extension within the original 45-day window and explain the reason for the delay.

---

## Step 4: Handle the Right to Delete Request

### General Rule

Once verified, you must delete the consumer's personal information from your records and direct your **service providers and contractors** to delete as well (more on this below).

### Exceptions to the Right to Delete

You are not required to delete personal information if retaining it is necessary for one or more of the following enumerated purposes under Cal. Civ. Code § 1798.105(d):

1. **Complete the transaction** — Necessary to complete the transaction for which the personal information was collected, provide a good or service requested by the consumer, or perform a contract between you and the consumer.

2. **Security** — Detect security incidents, protect against malicious, deceptive, fraudulent, or illegal activity, or prosecute those responsible for such activity.

3. **Debug and repair** — Identify and repair errors that impair existing intended functionality.

4. **Free speech / other legal rights** — Exercise free speech, ensure the right of another consumer to exercise their free speech rights, or exercise another right provided by law.

5. **Research** — Engage in public or peer-reviewed scientific, historical, or statistical research in the public interest that adheres to all applicable ethics and privacy laws, when the deletion would likely render impossible or seriously impair the achievement of such research, provided you have obtained the consumer's informed consent.

6. **Solely internal uses** — Use the personal information internally, in a lawful manner that is compatible with the context in which the consumer provided the information (e.g., for internal analytics that do not result in external disclosure).

7. **Legal obligation** — Comply with a legal obligation (e.g., financial recordkeeping laws, HIPAA retention requirements, tax records, litigation hold).

8. **Other lawful internal uses** — Use the personal information internally to make other product or service communications with the consumer, provided such communications are reasonably expected given the consumer's relationship with you and are compatible with the context in which the consumer provided the information.

### Partial Deletion

If one or more exceptions apply, you should delete the portions of personal information that are not covered by an exception, and retain only what is necessary for the excepted purpose. Document which exception applies to which retained data.

### Documenting the Exception

For your records (and in the event of a CPPA enforcement investigation or a private right of action regarding a data breach), document:

- Which exception(s) you invoked.
- Which categories of data were retained under each exception.
- For how long the retained data must be kept to satisfy the excepted purpose.

---

## Step 5: Downstream Obligations — Service Providers and Contractors

### The Cascade Requirement

Upon receiving a verified deletion request, you must notify all **service providers** and **contractors** that have received that consumer's personal information and instruct them to delete it. This is not optional. Under CPRA regulations, service providers and contractors are themselves bound to delete upon such notification, unless an exception applies to their processing.

### What Counts as a Service Provider

A service provider is an entity that processes personal information on your behalf pursuant to a written contract that restricts the service provider from:

- Selling or sharing the personal information.
- Retaining, using, or disclosing it outside the scope of the services.
- Combining it with data from other sources (with limited exceptions).

### Practical Steps

1. **Maintain a data map / vendor inventory.** You need to know which service providers have received the specific consumer's personal information. If your data map is incomplete, this is your largest operational risk.

2. **Send deletion instructions via your standard service provider notification mechanism** — typically a written instruction referencing the contract's privacy terms. Keep a record of when the notice was sent.

3. **Obtain confirmation.** While CPRA does not prescribe a specific mechanism, best practice is to request written confirmation from service providers that deletion has been completed or that an exception applies.

4. **Third-party sellers/advertisers.** If you have sold the consumer's personal information to third parties, you must also notify those third parties of the deletion request. Under CCPA/CPRA, a consumer may also submit a deletion request directly to those third parties. Your obligation is to notify them; you are not liable for their independent failure to delete, but you should maintain records showing you provided the notice.

---

## Step 6: Confirm Deletion to the Consumer

Once deletion is complete (or you have determined an exception applies), you must **notify the consumer of your response**:

- If you deleted (or partially deleted): Confirm in writing that their personal information has been deleted and specify any categories that were retained, along with the reason.
- If you invoked an exception for all data: Explain clearly and specifically which exception applies and why, so the consumer understands why their request was not fulfilled.
- Do not simply say "we cannot fulfill your request" — specificity is required.

---

## Step 7: No Fee, No Discrimination

### Consumer Fee Prohibition

You may **not charge a fee** to a consumer for making a Right to Know or Right to Delete request. This is an absolute prohibition — no application fee, no processing fee, no fee for receiving the disclosure.

**Limited exception for excessive/manifestly unfounded requests:** If a consumer submits requests that are "manifestly unfounded or excessive" — particularly if repetitive — you may charge a reasonable fee to cover administrative costs OR refuse to act on the request. However, this is a high bar. Making two requests in 12 months is generally not considered excessive. You bear the burden of demonstrating the request qualifies.

### Non-Discrimination Requirement

You may not discriminate against a consumer for exercising their CCPA/CPRA rights by:

- Denying goods or services.
- Charging different prices.
- Providing a different level or quality of goods or services.
- Suggesting the consumer will receive a different price, quality, or level of service.

**Exception:** You may offer a different price, rate, level, or quality if it is reasonably related to the value provided by the consumer's personal information (e.g., a loyalty program with explicit consent). This must be disclosed in advance and is narrowly construed.

---

## Step 8: Record-Keeping

Under CPRA, businesses that receive 100,000 or more consumer requests per year must maintain records of all requests and responses for at least **24 months** and make them available to the California Privacy Protection Agency (CPPA) on request. Even below that threshold, maintaining records of individual requests — date received, date acknowledged, verification outcome, response date, exceptions invoked, and service provider notifications — is essential for demonstrating compliance.

---

## Summary Timeline

| Action | Deadline |
|---|---|
| Acknowledge receipt | Within 10 business days |
| Verify consumer identity | As soon as practicable, before responding |
| Respond to Right to Know | Within 45 calendar days (extendable to 90 days with notice) |
| Respond to Right to Delete | Within 45 calendar days (extendable to 90 days with notice) |
| Notify service providers of deletion | Promptly upon verification (no separate deadline, but should be concurrent with or immediately after responding to consumer) |
| Confirm deletion to consumer | Within same 45-day response window |
| Retain records of request | At least 24 months (mandatory for large businesses; best practice for all) |

---

## Key Operational Takeaways

1. **Do not delay verification.** The 45-day clock runs from when you receive the request, not when verification is complete. Start verification immediately.

2. **Data mapping is foundational.** You cannot fulfill a Right to Know or cascade deletion to service providers without knowing where the consumer's data lives. Invest in your data inventory.

3. **Document everything.** Exceptions to deletion must be documented and defensible. The CPPA can audit your practices.

4. **Train your staff.** Requests can arrive through any channel — your privacy inbox, customer service, social media. Intake staff must recognize a CCPA/CPRA request and route it immediately to the designated privacy team.

5. **Review your service provider contracts.** They must already contain the required contractual restrictions. If they do not, you are exposed to regulatory risk independent of this specific request.

6. **Treat partial deletion seriously.** Invoking an exception is not a license to keep everything — retain only what is strictly necessary for the excepted purpose and delete the rest.
