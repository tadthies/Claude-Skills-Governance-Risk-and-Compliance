# System Security Plan Section: IA.L2-3.5.3 — Multifactor Authentication

## Practice Information

| Field | Value |
|---|---|
| **Practice ID** | IA.L2-3.5.3 |
| **CMMC Level** | Level 2 |
| **NIST SP 800-171 Rev 2 Reference** | 3.5.3 |
| **Family** | Identification and Authentication (IA) |
| **Practice Statement** | Use multifactor authentication (MFA) for local and network access to privileged accounts and for network access to non-privileged accounts. |
| **Practice Objective** | Ensure that authentication to organizational systems cannot be achieved through a single factor (e.g., password alone), reducing the risk of unauthorized access due to credential compromise, phishing, or credential-stuffing attacks. |
| **Implementation Status** | **Partially Met** |
| **Responsible Role** | IT Systems Administrator / IT Security Manager (Cloud Identity: M365 GCC High Administrator; Network/Remote Access: VPN Administrator; On-Prem Directory: Active Directory Administrator) |
| **Control Applicability** | CUI Environment — applies to all systems in scope that process, store, or transmit CUI, including cloud collaboration systems, remote access infrastructure, and on-premises engineering workstations |

---

## Discussion

NIST SP 800-171 Rev 2 (§3.5.3) and the associated CMMC assessment guide require multifactor authentication (something you know, something you have, or something you are — using at least two distinct factors) for:

1. **All local access to privileged accounts**
2. **All network access to privileged accounts**
3. **All network access to non-privileged accounts**

"Network access" is defined as any access to an organizational system where the communication occurs through a network (including local and wide-area networks and the internet). "Local access" is any access to an organizational system by a user communicating through a direct connection without the use of a network. Privileged accounts include, at minimum, domain/enterprise administrators, local administrators, cloud tenant/global administrators, and any account with elevated rights to configure, manage, or bypass security controls.

Our organization's environment consists of three distinct authentication surfaces, each with a different MFA implementation maturity:

- **Microsoft 365 GCC High tenant (Entra ID)** — governs identity for cloud collaboration, email, SharePoint/OneDrive, and Teams where CUI is processed and stored.
- **VPN remote access** — governs remote network access into the corporate environment, including access paths that reach legacy on-premises resources.
- **On-premises Active Directory (legacy CAD workstation domain)** — governs authentication for engineering/CAD workstations that have not yet been migrated to modern identity or that require local domain authentication for CAD licensing and file-share dependencies.

---

## Implementation Description

### A. Microsoft 365 GCC High / Entra ID (Cloud Identity — Primary CUI Environment)

All user and administrative access to the Microsoft 365 GCC High tenant is governed by Entra ID (Azure AD, US Government/GCC High cloud instance) and enforced through Conditional Access policies:

- **Non-privileged (standard user) network access:** All standard user accounts are required to complete MFA at every sign-in to Microsoft 365 GCC High services (Exchange Online, SharePoint Online, OneDrive, Teams) via Conditional Access policy `CA001-Require-MFA-AllUsers`, scoped to "All users" and "All cloud apps," with grant control set to "Require multifactor authentication." Session controls enforce periodic re-authentication (sign-in frequency of 8–12 hours) and disallow "remember MFA on trusted device" for CUI-handling roles.
- **Privileged account access (local and network):** Global Administrators, Privileged Role Administrators, SharePoint Administrators, Exchange Administrators, and other directory role holders are governed by Conditional Access policy `CA002-Require-PhishingResistantMFA-Admins`, which restricts authentication methods to phishing-resistant factors (FIDO2 security keys or Windows Hello for Business/certificate-based authentication) rather than SMS or voice. Privileged Identity Management (PIM) is used to enforce just-in-time role activation, which itself requires MFA re-confirmation at activation.
- **Authentication methods approved:** Microsoft Authenticator (push notification with number matching enabled), FIDO2 security keys (required for Global/Privileged Administrators), and certificate-based authentication for select service scenarios. SMS and voice call methods are disabled tenant-wide as a legacy/insecure authentication method per Entra ID Authentication Methods policy, consistent with CMMC Level 2 phishing-resistance expectations.
- **Legacy authentication blocking:** A Conditional Access policy (`CA003-Block-LegacyAuth`) blocks protocols that do not support modern authentication (and therefore cannot enforce MFA), such as POP3, IMAP4, and legacy SMTP AUTH.
- **Break-glass accounts:** Two emergency access accounts are excluded from Conditional Access per Microsoft best practice, secured with long, randomly generated passwords and FIDO2 keys stored in a physical safe; sign-ins are monitored and alert on use.

This satisfies the practice for the cloud/GCC High environment for both privileged and non-privileged network access.

### B. Duo MFA — VPN Remote Access

Remote network access to the corporate environment (including remote connections that traverse to on-premises resources, such as file shares, print services, and the CAD workstation domain) is authenticated through the corporate VPN concentrator with Duo Security integrated as the MFA provider:

- **Enrollment:** All users requiring remote access, including IT and network administrators using VPN for remote privileged administration, are enrolled in Duo and must complete a second factor after primary VPN credential (username/password, synchronized with or independent of AD, per current configuration) authentication.
- **Second factor methods:** Duo Push (via Duo Mobile app) is the primary method; Duo verified/security keys (WebAuthn) are available for administrative users; SMS passcode and phone call are retained only as fallback methods for users without smartphone access, with a plan to deprecate SMS fallback per phishing-resistance hardening goals (see Recommendations below).
- **Privileged network access via VPN:** Domain Administrators and other privileged personnel connecting remotely to reach on-premises administrative interfaces (e.g., Active Directory Users and Computers, server management consoles) authenticate to the VPN with Duo MFA before any network path to privileged local resources is available — satisfying the "network access to privileged accounts" requirement for the on-prem environment when accessed remotely.
- **Device posture:** Duo Device Health application enforces basic endpoint posture checks (OS patch level, disk encryption status) as a condition of completing authentication.

This satisfies the practice for all remote/network access paths into the environment, for both privileged and non-privileged accounts, regardless of destination (cloud or on-prem).

### C. On-Premises Active Directory — Legacy CAD Workstations (Gap Area)

The legacy CAD workstation environment consists of engineering workstations joined to an on-premises Active Directory domain, used for computer-aided design work that may involve CUI (e.g., controlled technical drawings). These workstations authenticate directly against on-prem AD using native Windows logon (Kerberos/NTLM) for:

- **Local access to workstations** (physical console logon at the CAD workstation)
- **Network access to on-prem file shares, license servers, and print services** for users who are already on the internal corporate network (i.e., not traversing VPN)

**Current state:** On-premises Active Directory, as configured, does not natively enforce a second authentication factor for interactive (console) logon or for internal network access to on-prem resources when the user is already inside the corporate network perimeter (LAN-connected, not via VPN/Duo). Native AD/NTLM and Kerberos logon at these workstations currently relies on password-only (single-factor) authentication. This is a **gap** against 3.5.3 for:

- Local access to privileged accounts (local admin / Domain Admin accounts used at or from CAD workstations)
- Network access to non-privileged accounts (standard CAD users authenticating to on-prem file shares/license servers over the internal LAN without traversing VPN/Duo)
- Network access to privileged accounts (Domain Admin sign-ins performed on the internal LAN rather than remotely through the Duo-protected VPN)

**Compensating controls currently in place** (pending full remediation):

1. Physical and network segmentation — CAD workstations reside on a dedicated VLAN with restricted routing, reducing exposure to lateral movement from other network segments.
2. All *remote* access to the CAD VLAN (from outside the corporate network) is required to transit the VPN, which enforces Duo MFA (see Section B) — so external/remote paths are covered.
3. Local AD administrative accounts use unique, complex passwords managed via a privileged access/password vaulting tool with mandatory rotation, and Domain Admin interactive logon is restricted to a small, monitored set of Privileged Access Workstations (PAWs).
4. Enhanced audit logging (Windows Security Event Log forwarding to SIEM) on authentication events for CAD workstation logons and on-prem privileged account use, to detect anomalous single-factor authentication abuse.
5. Physical access controls (badge-restricted engineering lab/CAD room) reduce the likelihood of unauthorized local console access.

**Remediation plan:** See POA&M note below. The organization is evaluating (a) deploying Windows Hello for Business or smart card/PIV-based certificate authentication for on-prem AD logon on CAD workstations, (b) extending Duo MFA coverage to on-prem AD via Duo Authentication for Windows Logon/RDP (Duo's on-prem agent) installed directly on CAD workstations and any jump/admin servers, and (c) longer-term, migrating CAD workstation identity to Entra ID (hybrid join or Entra Domain Services) to bring these endpoints under the same Conditional Access MFA enforcement as the GCC High tenant.

---

## Assessment Objectives

| Objective | Description | Status | Evidence/Notes |
|---|---|---|---|
| **3.5.3[a]** | Privileged accounts are identified | Met | Privileged accounts inventoried across Entra ID (Global/Privileged Role Administrators), Duo/VPN administrative accounts, and on-prem AD (Domain Admins, local Administrators on CAD workstations); maintained in privileged account register. |
| **3.5.3[b]** | Multifactor authentication is implemented for local access to privileged accounts | **Partially Met** | Met for M365 GCC High/Entra ID admin roles (phishing-resistant MFA via Conditional Access + PIM). **Not met** for local/console logon by Domain Admins or local admins directly at on-prem AD-joined systems, including CAD workstations, which currently accept single-factor (password) logon. Compensating controls: PAW restriction, password vaulting, enhanced logging. |
| **3.5.3[c]** | Multifactor authentication is implemented for network access to privileged accounts | **Partially Met** | Met for cloud (Entra ID Conditional Access) and for remote network access via VPN (Duo MFA) reaching on-prem privileged interfaces. **Not met** for privileged account network access performed entirely within the internal LAN (e.g., Domain Admin connecting to a file server from within the corporate network without traversing VPN/Duo), since on-prem AD does not enforce a second factor for LAN-based authentication. |
| **3.5.3[d]** | Multifactor authentication is implemented for network access to non-privileged accounts | **Partially Met** | Met for M365 GCC High application access (Entra ID Conditional Access, all users) and for any remote/VPN-based access (Duo MFA). **Not met** for standard CAD users authenticating to on-prem file shares, CAD license servers, or print services over the internal LAN, where on-prem AD currently permits single-factor logon. |

*(Note: Some CMMC assessment guides enumerate 3.5.3 objectives as [a]–[c]; this SSP uses the four-part breakdown — privileged local, privileged network, non-privileged network, plus the underlying privileged-account identification objective — consistent with the NIST 800-171A assessment procedure for 3.5.3. Adjust lettering to match the current official CMMC Assessment Guide Level 2 version referenced by your C3PAO.)*

---

## Overall Implementation Status Summary

**IA.L2-3.5.3 is assessed as PARTIALLY MET.**

- **Met:** Microsoft 365 GCC High / Entra ID (cloud collaboration environment) and all VPN-based remote network access (Duo MFA), covering both privileged and non-privileged accounts accessing CUI in the cloud environment or connecting remotely.
- **Not Met:** Local (console) and internal-LAN network authentication to on-premises Active Directory for legacy CAD workstations, where native single-factor password authentication remains in use for both privileged (Domain Admin/local admin) and non-privileged (standard CAD user) accounts.

---

## POA&M Note

| Field | Value |
|---|---|
| **POA&M Item ID** | POAM-IA-3.5.3-001 |
| **Associated Practice** | IA.L2-3.5.3 |
| **Weakness/Gap Description** | On-premises Active Directory authentication for legacy CAD workstations (local console logon and internal LAN network access) does not enforce multifactor authentication for privileged or non-privileged accounts. |
| **Source** | Internal self-assessment / gap analysis, identified [date of assessment] |
| **Risk Rating** | Moderate — mitigated by network segmentation, PAW restrictions, password vaulting, and physical access controls, but represents a residual single-factor authentication path to systems that may process CUI. |
| **Remediation Actions** | 1) Deploy Duo Authentication for Windows Logon/RDP agent to on-prem AD-joined CAD workstations and admin jump hosts. 2) Evaluate Windows Hello for Business / PIV smart card authentication for CAD workstation logon. 3) Assess feasibility of hybrid-joining CAD workstations to Entra ID to extend Conditional Access MFA coverage. 4) Update Group Policy and network access control to require MFA-backed authentication for all internal LAN access to CUI-relevant file shares and license servers. |
| **Resources Required** | Duo on-prem agent licensing (if not already covered under existing Duo subscription), IT engineering time for pilot and phased rollout, potential hardware (FIDO2/PIV cards or biometric-capable endpoints) for Windows Hello for Business. |
| **Milestones** | M1: Pilot Duo Windows Logon agent on 2–3 CAD workstations — 30 days. M2: Validate CAD software/license server compatibility with MFA-enforced logon — 60 days. M3: Phased rollout to all CAD workstations and on-prem privileged accounts — 120 days. M4: Full remediation and validation testing — 150 days. |
| **Responsible Party** | IT Security Manager / Active Directory Administrator |
| **Scheduled Completion Date** | [To be set — recommend within 150 days of POA&M creation, consistent with CMMC POA&M closure expectations for moderate-risk items] |
| **Interim Compensating Controls** | Network segmentation (dedicated CAD VLAN), Privileged Access Workstation (PAW) restriction for Domain Admin interactive logon, privileged password vaulting with rotation, badge-restricted physical access to CAD workstation area, SIEM-forwarded authentication logging and alerting on anomalous logons. |

---

## Related Practices / Cross-References

- **IA.L2-3.5.1 / IA.L2-3.5.2** — Identification of users/devices and authentication, which underpin the identity foundation (Entra ID, on-prem AD) on which this MFA control depends.
- **AC.L2-3.1.1 / AC.L2-3.1.2** — Access control practices governing account authorization, closely tied to the privileged account inventory referenced above.
- **IA.L2-3.5.4** (if applicable in scope) — Replay-resistant authentication mechanisms, relevant to the phishing-resistant MFA methods (FIDO2) deployed in Entra ID.
- **SC.L2-3.13.x** — Boundary protection practices, relevant to the VLAN segmentation compensating control for the CAD workstation environment.

---

*This section should be reviewed and updated upon completion of each POA&M milestone, and the Implementation Status field updated to "Met" only after the Duo Windows Logon (or equivalent MFA) deployment to on-prem AD/CAD workstations has been validated and evidenced (screenshots, policy exports, test logon records) for inclusion in the assessment evidence package.*
