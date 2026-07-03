SWIFT Architecture Type and CSCF v2026 Applicability — Regional Bank, On-Premises Alliance Access, No HSM
============================================================================================================

Disclaimer: The following is based on general knowledge of the SWIFT Customer Security Programme (CSP) and Customer Security Controls Framework (CSCF) as of my training. SWIFT updates the CSCF annually (new version typically published mid-year, effective for attestation the following year), and exact control numbering, wording, and mandatory/advisory status can shift between versions. Before you finalize your attestation, verify the exact CSCF v2026 control text and architecture-type definitions against the official SWIFT CSP documentation (the "CSCF v2026" PDF and the Architecture Type Definitions document) available on SWIFT's secure customer portal, and confirm scope with your SWIFT CISO/compliance contact or a SWIFT-authorized assessor. Do not treat this as a substitute for the authoritative SWIFT documents.

--------------------------------------------------------------------
1. DETERMINING YOUR ARCHITECTURE TYPE
--------------------------------------------------------------------

SWIFT defines several architecture types (historically labeled A1, A2, A3, A4, B) based on how you connect to SWIFT and where your messaging interface/connector sits.

Based on what you've described:
- You run Alliance Access (a full SWIFT messaging interface) on your own servers.
- Infrastructure is on-premises (not hosted by a service bureau, not cloud-hosted, not outsourced).
- You connect directly to SWIFT (presumably via SWIFT's SNL/network layer — e.g., a SIB, VPN box, or direct network connection — rather than through a third party).
- You have no HSM (Hardware Security Module) for storing SWIFT credentials/keys — meaning you are likely using software-based key storage or a smart-card/token-based alternative rather than a dedicated HSM.

Given this profile, your architecture is most consistent with:

**Architecture Type A1 — Full stack on customer premises, connected directly to SWIFT (self-managed interface + connector, on-premises, direct SWIFT connectivity)**

Key distinguishing features of A1 (vs. other types):
- A1 = You operate the messaging interface (Alliance Access) AND the connector/communication component yourself, on your own premises, with direct SWIFT connectivity. This is the most common architecture for banks that run their own SWIFT infrastructure without outsourcing to a service bureau.
- A2 = Similar to A1 but typically describes a customer connecting via a partial outsource or a lite connectivity model (e.g., using Alliance Lite2 or similar SWIFT-hosted lightweight connectivity) — not your case since you run full Alliance Access.
- A3 = You use a service bureau or third party to operate some/all of your messaging interface — not your case, since you explicitly stated no service bureau.
- A4 = You are a member/participant of a Market Infrastructure (MI) using SWIFT — not applicable unless you're connecting purely through an MI's closed user group.
- B = You are a service bureau or you exclusively use a service bureau's shared infrastructure with no direct SWIFT connectivity of your own — not your case.

**Your architecture type: A1 (on-premises, self-managed, direct SWIFT connection).**

Important note on the HSM gap: The absence of an HSM does NOT change your architecture type classification, but it is highly significant for control compliance (see Control 1.2/2.x below). Under CSCF, HSMs (or equivalent secure hardware — smart cards, tamper-resistant hardware tokens) are effectively required to achieve compliance with certain mandatory controls around protecting connectivity/credential secrets, particularly for A1 users with direct connectivity. Running without any hardware-based key protection is a material gap you should treat as a high-priority remediation item, not just a documentation nuance.

--------------------------------------------------------------------
2. CSCF STRUCTURE RECAP
--------------------------------------------------------------------

The CSCF is organized around 3 Objectives and (in recent versions) 8 Principles, containing a mix of Mandatory and Advisory controls:

- Objective 1: Restrict Internet Access & Protect Critical Systems from General IT Environment
- Objective 2: Reduce Attack Surface & Vulnerabilities
- Objective 3: Physically Secure the Environment
- Objective 4: Prevent Compromise of Credentials
- Objective 5: Manage Identities & Segregate Privileges
- Objective 6: Detect Anomalous Activity to Systems or Transaction Records
- Objective 7: Plan for Incident Response & Information Sharing
- (Objective/Principle groupings have shifted slightly release-to-release; treat the numbering below as indicative of typical CSCF structure, and confirm exact v2026 numbering against the official document.)

Mandatory controls are compulsory for all in-scope SWIFT users (subject to architecture-type applicability annotations in the control text). Advisory controls are strongly recommended best practices, not required for attestation, though many advisory controls become mandatory over time as CSCF versions evolve (this has been a consistent trend release-over-release).

--------------------------------------------------------------------
3. APPLICABILITY MATRIX FOR ARCHITECTURE TYPE A1 (ON-PREMISES, NO HSM)
--------------------------------------------------------------------

Below is the typical mandatory/advisory breakdown as it applies to an A1 architecture. (Control numbers reflect the general CSCF numbering scheme used in recent versions; verify exact numbering in CSCF v2026.)

OBJECTIVE 1 — Restrict Internet Access & Protect Critical Systems
| Control | Title | Status for A1 |
|---|---|---|
| 1.1 | SWIFT Environment Protection (segmentation of secure zone) | Mandatory |
| 1.2 | Operating System Privileged Account Control | Mandatory |
| 1.3 | Virtualisation/Cloud Platform Protection (if applicable) | Mandatory if virtualized on-prem infra used |
| 1.4 | Restriction of Internet Access | Mandatory |
| 1.5 | Customer Environment Protection (for service bureau customers) | Not applicable (you are not a service bureau customer) |

OBJECTIVE 2 — Reduce Attack Surface & Vulnerabilities
| Control | Title | Status for A1 |
|---|---|---|
| 2.1 | Internal Data Flow Security | Mandatory |
| 2.2 | Security Updates/Patching | Mandatory |
| 2.3 | System Hardening | Mandatory |
| 2.4A | Back-Office Data Flow Security | Mandatory |
| 2.4B | Back Office Transaction Data Confidentiality | Advisory |
| 2.5A | External Transmission Data Protection | Mandatory |
| 2.5B | External Transmission Data Protection (Additional) | Advisory |
| 2.6 | Operator Session Confidentiality/Integrity | Mandatory |
| 2.7 | Vulnerability Scanning | Mandatory |
| 2.8 | Outsourced Critical Activity Protection | Not applicable (no outsourcing/service bureau) |
| 2.9 | Transaction Business Controls | Advisory |
| 2.10 | Application Hardening | Advisory |
| 2.11A | RMA Business Controls | Mandatory |
| 2.11B | RMA Business Controls (Additional) | Advisory |

OBJECTIVE 3 — Physically Secure the Environment
| Control | Title | Status for A1 |
|---|---|---|
| 3.1 | Physical Security | Mandatory |

OBJECTIVE 4 — Prevent Compromise of Credentials
| Control | Title | Status for A1 |
|---|---|---|
| 4.1 | Password Policy | Mandatory |
| 4.2 | Multi-Factor Authentication | Mandatory |

OBJECTIVE 5 — Manage Identities & Segregate Privileges
| Control | Title | Status for A1 |
|---|---|---|
| 5.1 | Logical Access Control | Mandatory |
| 5.2 | Token/Mobile Device Management (incl. HSM/token management) | Mandatory — THIS IS YOUR GAP AREA |
| 5.3A | Personnel Vetting Process | Advisory |
| 5.3B | Physical and Logical Password Storage | Mandatory |
| 5.4 | Physical and Logical Password Storage (legacy numbering variant) | Mandatory |

OBJECTIVE 6 — Detect Anomalous Activity
| Control | Title | Status for A1 |
|---|---|---|
| 6.1 | Malware Protection | Mandatory |
| 6.2 | Software Integrity | Mandatory |
| 6.3 | Database Integrity | Mandatory |
| 6.4 | Logging and Monitoring | Mandatory |
| 6.5A | Intrusion Detection | Mandatory |
| 6.5B | Anomaly Detection on Business Content | Advisory |

OBJECTIVE 7 — Plan for Incident Response & Information Sharing
| Control | Title | Status for A1 |
|---|---|---|
| 7.1 | Cyber Incident Response Planning | Mandatory |
| 7.2 | Security Training and Awareness | Mandatory |
| 7.3A | Scenario Risk Assessment | Advisory |
| 7.3B | Vulnerability/Penetration Testing | Advisory (Independent Assessment increasingly emphasized) |
| 7.4A | Vulnerability Scanning (Additional/Penetration Testing) | Advisory |
| 7.4B | Penetration Testing | Advisory |

--------------------------------------------------------------------
4. THE HSM GAP — WHY IT MATTERS FOR YOU SPECIFICALLY
--------------------------------------------------------------------

Control 5.2 (Token/HSM/Credential Management, sometimes titled "Token Management" or referenced alongside "Secure Storage of Sensitive Data") is Mandatory for A1 architecture. In practice, SWIFT's guidance for this control expects that private keys, credentials, and connectivity secrets used for signing/authenticating with SWIFT be protected using hardware-based mechanisms — an HSM, a smart card, or an equivalent tamper-resistant hardware token.

If you currently store keys/credentials purely in software (no HSM, no smart card/token), you likely have a compliance gap against Mandatory Control 5.2, and potentially related aspects of 4.2 (Multi-Factor Authentication) and 2.6 (Operator Session Confidentiality/Integrity) depending on how your PKI and Relationship Management Application (RMA)/signing keys are protected.

Remediation options typically accepted by SWIFT/assessors:
1. Deploy a dedicated HSM for SWIFT key storage (most common and most robust option for A1 on-prem banks).
2. Use SWIFT-qualified secure hardware tokens/smart cards for operator authentication and key protection where full HSM deployment isn't yet feasible, as an interim compensating control.
3. Document a formal remediation plan/timeline if full compliance isn't achievable before your next attestation window — you may still need to declare non-compliance for the relevant control(s) in the KYC-SA (Know Your Customer Security Attestation) portal and provide a remediation date.

Given that you're a regional bank on Architecture A1, this is very likely your single highest-priority CSP gap and should be flagged to your board/risk committee as a finding requiring near-term remediation, since Mandatory controls that are not met must be disclosed in your annual SWIFT attestation and are visible to your counterparties via the KYC-SA registry.

--------------------------------------------------------------------
5. RECOMMENDED NEXT STEPS
--------------------------------------------------------------------

1. Confirm A1 classification formally using SWIFT's official Architecture Type Definitions document for CSCF v2026 (self-assessment questionnaire logic can nuance edge cases, e.g., if you use any cloud-hosted DR/backup components, which could pull in cloud-specific controls).
2. Pull the official CSCF v2026 control list from the SWIFT CSP portal and cross-check every control above — numbering/wording can shift year to year, and new controls are sometimes added or reclassified from Advisory to Mandatory.
3. Prioritize closing the HSM/hardware key-protection gap (Control 5.2 and related) — engage procurement now given HSM lead times.
4. Complete your Independent Assessment (many CSCF versions require an independent internal audit or external assessor review of your self-attestation, especially for Mandatory controls) before submitting your KYC-SA attestation.
5. Re-attest annually via the KYC-SA application within SWIFT's attestation window, disclosing any Mandatory controls not yet met along with remediation timelines.

--------------------------------------------------------------------

Bottom line: You are Architecture Type A1 (self-managed Alliance Access, on-premises, direct SWIFT connectivity, no service bureau/cloud). Under CSCF v2026, the large majority of the ~30+ controls applicable to A1 are Mandatory (spanning environment protection, patching/hardening, physical security, MFA, access control, credential/token protection, malware/logging/monitoring, and incident response/training), while a smaller set — largely around penetration testing, scenario risk assessment, application hardening, and enhanced business/transaction controls — remain Advisory. Your most urgent compliance risk is the lack of an HSM, which bears directly on Mandatory Control 5.2 (secure token/key storage) and should be remediated or formally documented with a compensating control and timeline before your next attestation.
