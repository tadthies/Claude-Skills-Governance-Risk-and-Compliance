# Control 4.2 Finding: Software OTP for SWIFT Operator Authentication

Your assessor is correct to flag this. Here's the full picture — why it's a finding, what CSCF actually requires, and how to close it before your attestation deadline.

## Why Software OTP (Google Authenticator) Is Not Sufficient

**Control 4.2 — Multi-Factor Authentication** is Mandatory across all architecture types (A1, A2, A3, A4, B), including your A1 (Alliance Access, customer-managed, software-based) environment.

The requirement is explicit:

> Software-based OTP (authenticator apps on shared devices) **does not satisfy** this requirement for most architecture types.

The underlying risk logic:
- A phone running Google Authenticator is a **general-purpose, shared device** — it runs other apps, connects to the internet, and can be compromised by malware, SIM-swap, or phishing (real-time OTP relay/MITM attacks) in a way a dedicated hardware token cannot.
- SWIFT CSP's threat model is built around Bangladesh Bank-style attacks, where operator credential compromise was the entry point for fraudulent payment instructions. MFA on a shared, network-connected device does not provide the same assurance as a dedicated, non-networked authentication factor.
- Because Control 4.2 secure sessions also link to **Control 2.6 (Operator Session Confidentiality and Integrity)**, which requires MFA aligned with 4.2, a software-OTP gap on 4.2 typically produces a linked finding on 2.6 as well — worth checking with your assessor.

This is also flagged in the skill's list of most common CSCF non-compliance patterns: *"Software-based OTP for MFA (Control 4.2): Many organisations use authenticator apps rather than hardware tokens. SWIFT CSP requires hardware tokens for most architecture types."*

## What CSCF v2025/v2026 Requires for Control 4.2

**Control 4.2 — Multi-Factor Authentication (Mandatory)**

| Element | Requirement |
|---|---|
| **Purpose** | Require MFA for all interactive operator access to the SWIFT environment |
| **Scope** | MFA mandatory for *all* interactive logins to SWIFT applications (Alliance Access, Alliance Gateway, SWIFT GUI); mandatory for remote administrative access to SWIFT systems |
| **Acceptable methods** | Hardware OTP tokens, smart cards with PIN, FIDO2 hardware keys |
| **Not acceptable** | Software-based OTP on shared/general-purpose devices (does not satisfy the requirement for most architecture types) |
| **Related control** | Token lifecycle management must align with Control 5.2 (Token Management) |

**Evidence artifacts your assessor will expect:**
- MFA configuration evidence for each SWIFT interface (Alliance Access, Alliance Gateway, GUI)
- Token inventory showing all operator tokens
- Authentication logs showing MFA enforcement
- Exemption register, if any accounts are excluded (must be formally approved and documented)

**Note on your attestation timing:** Since you're attesting under the current cycle in July, confirm with your assessor whether you're attesting to v2025 or the v2026 window (opens July 1, 2026, running through December 31, 2026). Control 4.2's hardware-token expectation is unchanged between these versions, so remediation planning is the same either way — but confirm which attestation form/deadline applies to you.

## Remediation Options Before Your July Deadline

Given the timeline pressure, here are your realistic paths, roughly ordered by speed of implementation:

### Option 1 — Deploy hardware OTP tokens (fastest, most direct fix)
1. Procure hardware OTP tokens (e.g., time-based hardware tokens compatible with Alliance Access's authentication module) or FIDO2 hardware keys for every named SWIFT operator.
2. Update Alliance Access / Alliance Gateway authentication configuration to require the hardware factor instead of/in addition to the software TOTP app.
3. Decommission Google Authenticator enrollment for SWIFT operator accounts once hardware tokens are issued.
4. Build a **token inventory register** (Control 5.2 alignment): issuance date, assigned operator, serial number, return process for leavers.
5. Update your MFA/token policy document and capture authentication logs showing hardware-token enforcement as your evidence artifact.

This is the option your assessor is most likely to accept without qualification, since it maps directly to the explicit acceptable-methods list.

### Option 2 — Smart cards with PIN
If your organization already has a PKI/smart-card program (e.g., for building access or general corporate authentication), extending it to SWIFT operator logins can be faster than a net-new hardware token rollout. Requires integration with Alliance Access's authentication mechanism and PIN-based unlock.

### Option 3 — Interim risk acceptance / documented exception
If hardware tokens cannot be physically procured and deployed before your deadline:
- Document a **formal, time-boxed exception** with compensating controls (e.g., enhanced session logging under Control 6.4, tighter session timeouts, restricted operator IP allow-listing) and a committed remediation date.
- This should be raised with your independent assessor now — a documented exception with an active remediation plan is viewed far more favorably than silence, but it does **not** clear the underlying finding; it only manages disclosure risk. Expect it to still show as Partially Implemented on the KYC-SA form.
- This is not a substitute for hardware MFA — treat it strictly as a bridge, not a resolution.

### What NOT to do
Do not attempt to attest Control 4.2 as "Implemented" while software OTP remains in place for SWIFT operator logins — this is a known assessor red flag and misrepresents your control status on a document visible to your counterparties.

## Suggested Immediate Action Plan

| Step | Action | Owner | Target |
|---|---|---|---|
| 1 | Procure hardware OTP tokens or FIDO2 keys for all SWIFT operators | IT Security / Procurement | Immediate |
| 2 | Reconfigure Alliance Access authentication to require hardware factor | SWIFT Infrastructure team | Before attestation |
| 3 | Build token inventory register (Control 5.2) | SWIFT Operations | Before attestation |
| 4 | Decommission software OTP enrollment for SWIFT accounts | IT Security | Before attestation |
| 5 | If timeline is at risk: draft compensating-control exception memo and discuss with assessor now | Compliance / CISO | This week |
| 6 | Update KYC-SA attestation status for 4.2 (and check linked 2.6) once remediated | Compliance | Before submission |

## Gap Assessment Snapshot

| Control ID | Control Name | Status | Evidence Required | Gap Notes |
|---|---|---|---|---|
| 4.2 | Multi-Factor Authentication | 🔴 Not Implemented | Hardware token inventory, MFA config evidence, auth logs | Software OTP (Google Authenticator) on shared devices does not meet CSCF requirement; hardware token or FIDO2 key required |
| 2.6 | Operator Session Confidentiality and Integrity | 🟡 Check | MFA alignment evidence for session auth | MFA method for session authentication must align to 4.2 remediation — verify with assessor whether this is separately flagged |

**Bottom line:** Google Authenticator on operator phones/laptops is a software OTP on a shared device, which CSCF explicitly excludes as sufficient for Control 4.2 in most architecture types (including your A1 setup). The fix is to deploy hardware OTP tokens, smart cards with PIN, or FIDO2 hardware keys to every SWIFT operator, update Alliance Access authentication configuration accordingly, and build the token inventory required under Control 5.2. If procurement/deployment can't complete before your deadline, raise a formal, time-boxed exception with compensating controls with your assessor now rather than waiting.

*Reminder: verify current control wording and any last-mile guidance against the official CSCF documentation on swift.com Knowledge Centre and with your assessor before finalizing your attestation submission.*
