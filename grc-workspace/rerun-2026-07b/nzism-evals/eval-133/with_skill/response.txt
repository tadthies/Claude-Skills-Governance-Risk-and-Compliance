# Access Control Policy

**Classification:** IN-CONFIDENCE (policy document itself; classify per agency standard)
**Document Owner:** Chief Information Security Officer (CISO) / Information Security Officer (ISO)
**Approved By:** [Chief Executive or delegate]
**Version:** 1.0
**Review Cycle:** Annual, or upon significant change to systems, threat environment, or organisational structure

---

## 1. Purpose

This policy establishes the requirements for controlling access to [Agency Name]'s information systems and information assets, in line with the New Zealand Information Security Manual (NZISM) and the agency's Information Security Policy. It ensures that access to systems and information is granted only to authorised individuals, based on legitimate business need, and is managed throughout the access lifecycle.

## 2. Scope

This policy applies to all [Agency Name] employees, contractors, third-party suppliers, and any other individuals granted access to agency information systems, applications, networks, or data, across all classification levels from Unclassified through to the highest classification level processed by the agency. Default assumption for control baseline in this policy is **Restricted**; agencies handling Confidential or above must apply the additional controls specified in Section 8.

## 3. Policy Statements

### 3.1 Identification (NZISM Section 8 — Identification and Authentication)

- Every user, system, and service account must be uniquely identified. Shared or generic accounts are prohibited except where formally approved with compensating controls (e.g., break-glass accounts with enhanced logging).
- All accounts must be provisioned through a formal request and approval process, tied to a verified identity and a documented business need.
- Service accounts must have unique credentials per system/application — no credential reuse across services.
- Identity records must be maintained in an authoritative source (e.g., central directory service) and kept current.

**Evidence for assessment:** Account provisioning records, unique account listing, service account inventory.

### 3.2 Authentication (NZISM Section 8 — Identification and Authentication)

- Passwords must meet minimum complexity and length requirements aligned with NIST SP 800-63B guidance as referenced by the NZISM.
- **Multi-Factor Authentication (MFA) is mandatory** for:
  - All remote access to agency systems
  - All privileged/administrative accounts, regardless of access method
- Account lockout must be enforced after a defined number of failed login attempts.
- Session timeout and automatic screen/session lock must be configured for all systems processing Restricted and above information.
- Federation/Single Sign-On (SSO), where deployed, must meet the same authentication assurance requirements as direct authentication.
- Biometric authentication, where used, must be supplemented by an additional factor for privileged or Confidential+ access.

**Evidence for assessment:** Password policy configuration, MFA enrolment records, session timeout configuration, lockout policy settings.

### 3.3 Authorisation (NZISM Section 7 — Access Control)

- Access must be granted on the principle of **least privilege** — users receive the minimum access required to perform their role.
- Access must be granted on a **need-to-know** basis, in addition to role-based entitlement.
- **Separation of duties** must be enforced for critical or high-risk functions (e.g., system changes, financial transactions, security administration) — no single individual should be able to execute a complete sensitive process end-to-end without independent oversight.
- **Temporary and time-limited access** requires a formal request and approval, with automatic expiry configured at time of grant — no indefinite temporary access.
- **Access reviews** must be conducted at least annually (more frequently for privileged and Confidential+ access) to re-certify that existing access remains appropriate; access no longer required must be revoked promptly.
- Access must be revoked immediately upon role change (adjusted to new role) or termination of employment/contract.

**Evidence for assessment:** Role-based access control matrix, access review records/sign-offs, access request and approval logs, termination/offboarding checklist with revocation timestamps.

### 3.4 Privileged Access Management (NZISM Section 7 — Access Control)

- Privileged accounts (system administrators, database administrators, security administrators, etc.) must be:
  - Logically separated from standard user accounts (no privileged access via a general daily-use account)
  - Individually identifiable — no shared administrative credentials
  - Subject to enhanced logging of all privileged actions, reviewed periodically
  - Reviewed and re-certified at least annually, with more frequent review recommended for Restricted+ environments
- Remote privileged access must use additional controls such as jump servers/bastion hosts and session recording.
- Privileged access to systems handling **Confidential** information requires background vetting for all administrators, and consideration of biometric or hardware token authentication.
- Break-glass/emergency access procedures must be documented, require post-use justification, and trigger automatic notification to the ISO/CISO.

**Evidence for assessment:** Privileged account inventory (separate from standard accounts), privileged action logs, jump server/bastion configuration, session recording samples, background vetting records for administrators (Confidential+).

### 3.5 Additional Requirements by Classification

Higher classification levels inherit all controls above plus the following:

| Classification | Additional Access Control Requirements |
|---|---|
| Restricted | MFA for all remote access (mandatory); privileged account separation |
| Confidential | Background vetting required for all administrators; biometric or hardware token authentication |
| Secret / Top Secret | Full security vetting to Secret/Top Secret level for all users and administrators; direct GCSB/NCSC NZ involvement in access model design |

## 4. Roles and Responsibilities

- **CISO / ISO**: owns this policy, approves exceptions, oversees compliance monitoring
- **System/Application Owners**: define role-based access models for their systems, approve access requests, participate in access reviews
- **Line Managers**: initiate access requests and terminations for their staff, confirm ongoing need-to-know at review points
- **IT Operations / Identity Team**: provision and de-provision accounts, maintain the identity directory, configure MFA and lockout settings
- **All Users**: safeguard credentials, do not share accounts, report suspected compromise immediately

## 5. Exceptions

Any deviation from this policy (e.g., a shared account, an exemption from MFA) must be formally requested, documented with compensating controls, risk-assessed, and approved by the CISO/ISO. Exceptions must be time-bound and reviewed at renewal.

## 6. Non-Compliance

Failure to comply with this policy may result in access suspension, disciplinary action, or contract termination for third parties, in accordance with agency HR and procurement policies.

## 7. Related Documents

- Information Security Policy
- Acceptable Use Policy
- System Security Plan(s)
- Incident Response Plan
- Third-Party Supplier Security Requirements

## 8. NZISM Control Reference Summary

| Policy Section | NZISM Domain |
|---|---|
| 3.1 Identification | Section 8 — Identification and Authentication |
| 3.2 Authentication | Section 8 — Identification and Authentication |
| 3.3 Authorisation | Section 7 — Access Control |
| 3.4 Privileged Access | Section 7 — Access Control |

## Version History

| Version | Date | Author | Summary of Changes |
|---|---|---|---|
| 1.0 | 2026-07-03 | [CISO/ISO name] | Initial issue |

---
*This policy template provides general compliance guidance aligned to the NZISM, not legal advice. Verify current control requirements against official NZISM/NCSC NZ publications and tailor to your agency's specific classification levels and risk profile before formal adoption.*
