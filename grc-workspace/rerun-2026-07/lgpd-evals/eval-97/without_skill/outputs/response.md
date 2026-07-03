Handling a Data Subject's Deletion Request Under LGPD (Lei Geral de Proteção de Dados)

When a Brazilian data subject (titular) emails a request to delete all their personal data, this is an exercise of their rights under Article 18 of the LGPD (Law No. 13.709/2018), specifically the right to deletion/elimination of personal data (Art. 18, VI). Here is how to handle it end-to-end.

## 1. Acknowledge and Authenticate the Request

- Acknowledge receipt promptly (best practice: within a few business days).
- Verify the requester's identity before acting. LGPD does not prescribe a specific method, but you must take reasonable steps to confirm the person emailing is actually the data subject (or their legally authorized representative) — e.g., verify the email matches the account of record, or request additional confirming information. This prevents unauthorized deletion triggered by a third party impersonating the user.
- Log the request (date received, channel, requester identity, scope) — you'll need this to demonstrate compliance (accountability principle, Art. 6, X).

## 2. Determine Scope and Applicable Legal Bases

Deletion under LGPD is not always absolute. Before deleting, assess:

- **What personal data exists and where** — in your case: CRM, email marketing platform, and analytics tool. Map all locations, including backups, logs, and any data shared with third-party processors (operadores).
- **The legal basis under which each category of data was originally processed** (Art. 7). This matters because:
  - If data was processed based on **consent** (Art. 7, I), the data subject can revoke consent and request deletion, and you generally must comply (Art. 18, VI combined with Art. 8, §5).
  - If data is being retained for **compliance with a legal or regulatory obligation** (Art. 16, I) — e.g., tax, accounting, or consumer protection retention requirements — you may need to retain certain records even after a deletion request, but should delete or anonymize everything not covered by that exception.
  - If data is necessary for the **regular exercise of rights in judicial, administrative, or arbitration proceedings** (Art. 16, II), or for the controller's **legitimate interests** where still applicable and not overridden by the request, some retention may be justified.
  - Marketing/analytics data typically has no such retention exception once consent is withdrawn or objection is raised, and should be deleted.

## 3. Execute Deletion Across All Systems

Because your data lives in three systems, coordinate deletion (or anonymization, where deletion isn't feasible) across all of them:

- **CRM**: Delete or anonymize the contact record and associated activity history (notes, deal records, support tickets) unless specific fields must be retained under a legal obligation (e.g., invoicing/tax records tied to a completed transaction — in which case, consider partial deletion/anonymization of non-essential fields while retaining only what's legally required).
- **Email platform**: Remove the individual from all lists/segments and delete their contact record, including engagement history (opens/clicks tied to their identity), and suppress future sends. Simply "unsubscribing" is not sufficient — the underlying personal data record should be deleted.
- **Analytics tool**: Delete or anonymize any user-level identifiers (user IDs, device IDs, IP addresses, email hashes) associated with this individual. Many analytics platforms (e.g., Google Analytics, Mixpanel, Amplitude) provide user-deletion APIs for exactly this purpose — use them rather than manual deletion where available.
- **Backups**: You are not typically required to purge encrypted backups immediately, but you should ensure deleted data is not restored and is purged according to your normal backup rotation/retention schedule, and is not used for any purpose in the interim.
- **Third-party processors (operadores)**: If any of these three tools qualify as processors acting on your behalf (which they generally do), you as the controller (controlador) are responsible for instructing them to delete the data too. Check your data processing agreements/contracts with these vendors for how deletion requests are handled and confirm completion.

## 4. Anonymization as an Alternative

Where full deletion isn't possible due to legitimate retention needs (e.g., financial/tax records), consider **anonymization** (Art. 12) instead — stripping identifying elements so the data can no longer be linked to the individual, while preserving aggregate data you're legally required to keep (e.g., for accounting purposes).

## 5. Respond to the Data Subject

- Confirm what was deleted, what (if anything) was retained and why (citing the specific legal basis, e.g., tax retention obligations), and the timeframe in which action was taken.
- LGPD does not set a hard statutory deadline for responding to rights requests (unlike GDPR's 30 days), but the ANPD (Autoridade Nacional de Proteção de Dados) expects controllers to respond within a reasonable period, and many organizations align with a ~15-day target as a matter of good practice. Check if your privacy policy or internal SLA commits to a specific timeframe, and honor it.
- Provide the response in a clear, accessible, and (if the request came in Portuguese or the user is Brazilian) appropriately localized format.

## 6. Document the Process

- Maintain a record of the request, verification steps, systems affected, actions taken, any data retained with justification, and the response sent to the data subject. This is essential for accountability (Art. 6, X) and to demonstrate compliance if the ANPD ever asks.

## 7. Preventive/Process Improvements

- If you don't already have one, establish a documented Data Subject Rights Request (DSR) procedure covering identity verification, cross-system deletion workflows (CRM, ESP, analytics, and any other tools), timelines, and exception-handling for legal retention obligations.
- Confirm your vendor contracts (CRM, email platform, analytics) include LGPD-appropriate data processing terms obligating them to support deletion requests within a reasonable timeframe.

### Summary Checklist
1. Acknowledge the request and verify identity.
2. Map data across CRM, email platform, and analytics tool.
3. Check for legal retention obligations (tax, legal claims) that limit full deletion.
4. Delete/anonymize data in each system, including with sub-processors.
5. Handle backups appropriately (no restoration, normal purge cycle).
6. Respond to the user confirming action taken and any retained data with justification.
7. Document everything for accountability purposes.

This approach satisfies the data subject's Art. 18, VI deletion right while respecting any legitimate, narrowly-scoped retention obligations you may have under Brazilian law.
