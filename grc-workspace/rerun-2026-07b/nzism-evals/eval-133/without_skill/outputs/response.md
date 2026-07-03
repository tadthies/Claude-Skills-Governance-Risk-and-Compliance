# Access Control Policy

**Agency:** [Agency Name]
**Classification:** [UNCLASSIFIED / IN-CONFIDENCE / RESTRICTED — set per document]
**Effective Date:** 3 July 2026
**Owner:** IT Security Manager (ITSM) / Chief Information Security Officer
**Review Cycle:** Annual, or upon significant system/organisational change

---

## 1. Purpose

This policy establishes the requirements for controlling access to [Agency Name]'s information systems, applications, and data, in alignment with the New Zealand Information Security Manual (NZISM). It ensures that access is granted based on identified business need, appropriately authenticated, authorised, and subject to enhanced controls for privileged accounts.

## 2. Scope

This policy applies to all employees, contractors, third parties, and system accounts that access [Agency Name]'s information systems and data, across all classification levels.

## 3. Policy Statements

### 3.1 Identification

- All users and system accounts must be uniquely identified before being granted access to any agency system. Shared or generic accounts are prohibited except where explicitly risk-assessed and approved (e.g., emergency/break-glass accounts), consistent with the NZISM's identification and authentication principles (NZISM Chapter on Access Control / Identification and Authentication controls).
- User identities must be established through a formal registration process, verified against HR or contract records prior to account creation.
- Unique identifiers must not be reused or reassigned to a different individual.
- All accounts must be traceable to a specific individual or system function to support accountability and audit requirements.

### 3.2 Authentication

- Authentication mechanisms must be commensurate with the classification of the information being accessed, per NZISM guidance on authentication strength.
- Multi-factor authentication (MFA) must be used for:
  - Remote access to agency systems
  - Access to systems processing RESTRICTED or higher classified information
  - All privileged/administrative accounts
- Passwords/passphrases, where used as a factor, must meet NZISM-aligned complexity, length, and rotation requirements, and must never be transmitted or stored in clear text.
- Authentication credentials must be protected using approved cryptographic controls in line with NZISM cryptographic guidance.
- Default vendor credentials must be changed prior to system deployment.
- Account lockout mechanisms must be implemented to mitigate brute-force authentication attempts.

### 3.3 Authorisation

- Access must be granted according to the principles of **least privilege** and **need-to-know**, consistent with NZISM access control requirements.
- Role-based access control (RBAC) must be used wherever practicable to standardise and simplify permission assignment.
- All access requests must be formally approved by the relevant data/system owner before provisioning.
- Access rights must be reviewed at least [quarterly/biannually] to confirm continued business need, with formal sign-off retained as evidence.
- Access must be promptly revoked upon role change, contract end, or termination, with a defined maximum timeframe (e.g., same day for terminations).
- Segregation of duties must be enforced for sensitive functions (e.g., system administration, financial transactions, security configuration changes) to reduce the risk of fraud or error.

### 3.4 Privileged Access Management

- Privileged accounts (system administrators, database administrators, security administrators, and similar elevated roles) must be:
  - Separate from standard user accounts (no dual-use accounts for daily business and administrative functions)
  - Individually identifiable and attributable to a specific person
  - Subject to MFA for all access
  - Granted only for as long as required, with periodic (at minimum quarterly) review and re-approval
  - Logged and monitored, with all privileged actions captured in audit logs that are protected from tampering and retained per agency/NZISM record-keeping requirements
- Use of privileged accounts must be limited to tasks that specifically require elevated privileges; routine activities (e.g., email, web browsing) must not be performed using privileged credentials.
- Emergency/break-glass access procedures must be documented, restricted, logged, and subject to post-use review.
- Remote privileged access must be subject to additional controls (e.g., jump hosts/bastion systems, session recording) where the system classification warrants it.

### 3.5 Account and Access Lifecycle Management

- Formal joiner-mover-leaver (JML) processes must govern account creation, modification, and deletion.
- Access provisioning and de-provisioning must be auditable, with records retained in accordance with agency retention schedules.
- Inactive accounts must be disabled after a defined period of inactivity (e.g., 45–90 days) and removed if not reactivated within a further defined period.
- System owners must maintain a current register of accounts and access levels for their systems.

### 3.6 Monitoring, Logging, and Audit

- All authentication attempts (successful and failed), authorisation changes, and privileged account activity must be logged.
- Logs must be protected against unauthorised modification or deletion and retained for a period consistent with NZISM logging/audit retention guidance and agency policy.
- Anomalous access patterns (e.g., repeated failed logins, access outside business hours, access from unexpected locations) must be monitored and investigated.

### 3.7 Third-Party and Remote Access

- Third-party access to agency systems must be governed by contractual security requirements, time-limited, and subject to the same identification, authentication, and authorisation controls as internal users.
- Remote access must use agency-approved, encrypted connection methods (e.g., VPN with MFA) consistent with NZISM network security and remote access guidance.

## 4. Roles and Responsibilities

| Role | Responsibility |
|---|---|
| IT Security Manager (ITSM) | Owns this policy, oversees compliance, reports exceptions to the Accreditation Authority |
| System/Data Owners | Approve access requests, conduct periodic access reviews |
| IT Operations | Provision/de-provision accounts, maintain logging and monitoring infrastructure |
| All Staff and Contractors | Comply with this policy; protect credentials; report suspected compromise immediately |

## 5. Exceptions

Any exception to this policy must be formally documented, risk-assessed, and approved by the ITSM, with compensating controls identified and a defined review/expiry date.

## 6. Related NZISM Reference Areas

This policy is aligned to the NZISM's guidance on:
- Access control principles (least privilege, need-to-know, segregation of duties)
- Identification and authentication requirements (including multi-factor authentication)
- Privileged access management and administrator account controls
- Audit logging and monitoring requirements
- Personnel security and system use obligations

*Note: Specific NZISM chapter/control numbers should be cross-referenced against the current published version of the NZISM at the time of policy finalisation, as section numbering and control identifiers can change between NZISM releases. This draft reflects the substantive requirements typically found in those areas but should be validated against the current controlling document before formal adoption.*

## 7. Policy Review

This policy will be reviewed annually by the ITSM, or earlier following a significant security incident, system change, or update to the NZISM.

---
**Approved by:** [Accreditation Authority / CE Delegate]
**Date:** [ ]
