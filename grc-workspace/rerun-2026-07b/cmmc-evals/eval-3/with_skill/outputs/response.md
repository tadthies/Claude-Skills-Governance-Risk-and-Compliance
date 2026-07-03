# System Security Plan — IA.L2-3.5.3 (Multifactor Authentication)

## Practice ID
**IA.L2-3.5.3**

## Requirement Statement
Use multifactor authentication (MFA) for local and network access to privileged accounts and for network access to non-privileged accounts.

## Implementation Description

[Organization Name] implements multifactor authentication across its hybrid Microsoft 365 GCC High / on-premises environment using a layered approach tailored to each access path into systems that process, store, or transmit CUI:

**Cloud identity and productivity environment (Microsoft 365 GCC High / Entra ID):**
All user access to Microsoft 365 GCC High resources — including email, SharePoint, Teams, and OneDrive locations where CUI is stored or transmitted — is authenticated through Entra ID (Azure AD Government) Conditional Access policies. MFA is enforced for:
- All privileged accounts (Global Administrators, Exchange Administrators, SharePoint Administrators, and any role with elevated permissions in the GCC High tenant), for both local (console/portal) and network (remote) access.
- All non-privileged (standard) user accounts for network access to GCC High services.

Entra ID Conditional Access policies require a second factor (Microsoft Authenticator with number matching, or FIDO2 security key for privileged roles) in addition to password, and enforce this consistently regardless of device or location, with policies configured to block legacy authentication protocols that do not support MFA.

**Remote network access (VPN):**
Remote access to the internal network — including access to legacy CAD systems and any network segment where CUI resides — is brokered through the organization's VPN gateway, which is integrated with **Duo MFA**. All users, privileged and non-privileged, must complete Duo MFA (push notification, TOTP, or hardware token) before a VPN session is established. This satisfies the network-access MFA requirement independent of the identity source (Entra ID or on-prem AD) being authenticated against.

**On-premises Active Directory (legacy CAD workstations):**
On-prem Active Directory governs authentication for legacy CAD workstations. [Organization Name] enforces MFA for this population as follows:
- **Network access** to AD-joined resources (e.g., remote sessions, RDP into CAD systems from outside the local segment) is required to traverse the VPN, and therefore inherits Duo MFA enforcement described above — network access is never granted to AD resources without first passing through the MFA-gated VPN.
- **Local access** to privileged (administrative) accounts on the on-prem AD domain — including Domain Admins and local admin accounts on CAD workstations — [state actual implementation, e.g.: "requires MFA via Duo Authentication for Windows Logon (RDP/console) enforced on all domain controllers and privileged workstation logons"]. *(If this control is not yet deployed, see Gap Note below — this is the practice's most common failure point.)*
- **Local access to non-privileged CAD workstation accounts** is not in scope for this requirement per NIST SP 800-171 (the practice requires MFA for local/network access to *privileged* accounts, and *network* access for non-privileged accounts — local logon for standard users is not mandated by 3.5.3 itself, though compensating physical/access controls under PE and AC domains still apply).

## Gap Note (include if applicable — remove if fully implemented)
> **Action required:** Confirm whether Duo (or an equivalent MFA solution) is deployed for **local console/RDP logon to privileged accounts on the on-prem AD domain** (domain controllers, CAD workstation local admins). If MFA is enforced only at the VPN/network perimeter and not for local privileged logons on legacy CAD systems, this practice should be marked **PARTIAL**, not MET, and requires remediation before it can be included in an SSP submission as fully implemented. IA.L2-3.5.3 is one of the **critical practices that can never be POA&M'd at certification** — it must be fully MET, so this gap should be treated as top priority.

## Responsible Roles
- **ISSO/ISSM** — policy ownership, Conditional Access policy configuration and review
- **IT Systems Administrator** — Duo MFA deployment and VPN gateway configuration
- **Domain Administrator** — on-prem AD group policy and privileged account MFA enforcement
- **Security Operations** — MFA enrollment monitoring, exception handling

## Associated Systems
- Microsoft 365 GCC High tenant (Entra ID / Azure AD Government)
- Duo MFA (VPN integration)
- On-premises Active Directory domain controllers
- Legacy CAD workstations (domain-joined)
- VPN gateway/concentrator

## Evidence/Artifacts
- Entra ID Conditional Access policy export showing MFA enforcement for all users and privileged roles
- Duo MFA administration console configuration and enrollment report (all VPN users)
- Screenshot/export of Duo Authentication for Windows Logon policy applied to domain controllers and privileged CAD workstation accounts (or remediation POA&M if not yet deployed)
- Active Directory Group Policy Object (GPO) settings restricting local logon and enforcing MFA integration for privileged groups
- MFA enrollment report showing 100% coverage for privileged accounts across both cloud and on-prem environments
- Sample access logs demonstrating MFA challenge on VPN connection and Entra ID sign-in

---
*This SSP section is a drafting aid based on general CMMC/NIST SP 800-171 guidance, not legal advice. Verify actual configuration state against the environment before finalizing — particularly the on-prem AD local privileged-access MFA gap noted above — and have the final SSP reviewed by your ISSO and, where applicable, your C3PAO.*
