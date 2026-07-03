# SWIFT CSCF Control 4.2 — MFA and Hardware Token Requirements

## Why Software OTP May Not Be Sufficient for SWIFT

The SWIFT Customer Security Controls Framework (CSCF) Control 4.2 — **Multi-Factor Authentication** — sets specific requirements for operator authentication to SWIFT systems. Your assessor's finding relates to the quality of the second authentication factor.

### The Problem with Software TOTP

Software-based TOTP applications like Google Authenticator run on general-purpose smartphones or computers. The CSCF takes the view that a software-based authenticator on a general-purpose device does not provide the same level of assurance as a dedicated hardware token because:

1. **Malware risk**: If the device running Google Authenticator is compromised by malware, an attacker could potentially read the TOTP seed stored in the app, intercept the OTP codes, or manipulate the authentication flow
2. **Device sharing and backup risk**: TOTP seeds in software apps can often be backed up, transferred, or restored — undermining the "something you have" factor
3. **General-purpose device exposure**: Smartphones can run arbitrary apps, browse the internet, and receive malicious content — they are a higher-risk platform than a dedicated hardware device

### What the CSCF Requires

CSCF Control 4.2 requires hardware-based MFA for SWIFT operator authentication. The second factor must be a **dedicated hardware token** — a physical device that:
- Generates or stores credentials in tamper-resistant hardware
- Does not allow the cryptographic secret to be extracted
- Is a single-purpose device (not a general-purpose smartphone)

Software OTP on a smartphone typically does not meet this standard under CSCF requirements.

---

## Compliant Hardware Token Options

### Option 1: RSA SecurID Hardware Tokens
- Physical hardware token generating 6-digit codes every 60 seconds
- Integrates with Alliance Access via RSA Authentication Manager + RADIUS
- Widely deployed in banking environments
- Seeds stored in tamper-resistant hardware on the token

### Option 2: Thales SafeNet Hardware Tokens
- SafeNet OTP 110 or eToken PASS
- Similar time-based OTP in dedicated hardware
- Works with RADIUS authentication integration
- Often used as an alternative to RSA in financial institutions

### Option 3: FIDO2 Hardware Security Keys (e.g., YubiKey)
- YubiKey 5 series or similar FIDO2 authenticators
- Phishing-resistant authentication using public key cryptography
- Private key never leaves the device
- Strong hardware assurance — may require compatibility check with your Alliance Access version

### Option 4: Smart Card / PKI Tokens
- Smart cards with embedded X.509 certificates
- Widely used in financial services for dual-purpose (logical and physical access)
- Requires smart card reader integration

---

## Remediation Steps

1. **Select hardware token platform**: Evaluate RSA SecurID, Thales SafeNet, or YubiKey based on your existing infrastructure (Active Directory, RADIUS, LDAP)

2. **Assess integration requirements**: Determine how Alliance Access integrates with your chosen authentication server (RADIUS is most common)

3. **Procure hardware tokens**: Order sufficient tokens for all SWIFT operators plus spares. Allow 2–4 weeks for delivery

4. **Deploy authentication server**: Install RSA Authentication Manager, SafeNet Authentication Service, or equivalent. Configure RADIUS integration with Alliance Access

5. **Enroll operators**: Bind each hardware token to a named SWIFT operator

6. **Test and validate**: Verify all operators can authenticate with hardware tokens and that software-only authentication is blocked

7. **Update documentation**: Update your MFA policy and token management procedures (relates to Control 5.2 — Token Management)

8. **Attestation timeline**: The SWIFT CSP attestation cycle typically runs on an annual basis. Check your current attestation deadline to ensure remediation is complete before you need to attest Control 4.2

---

## Attestation Implications

Until hardware tokens are deployed for all SWIFT operators, Control 4.2 should be attested as **Partially Implemented** or **Not Implemented** in your KYC-SA form. Your SWIFT counterparties can see this status, so timely remediation protects your compliance reputation.

Consult the current CSCF version document from SWIFT (swift.com) for the exact language of Control 4.2 requirements, as SWIFT updates the framework annually.
