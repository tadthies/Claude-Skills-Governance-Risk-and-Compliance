# CSCF v2026 Control 4.2 — MFA Hardware Token Requirement

## Why Software OTP (Google Authenticator / TOTP) Is Insufficient

CSCF v2026 Control 4.2 — **Multi-Factor Authentication** — explicitly requires **hardware authentication tokens** for all interactive operator sessions accessing the SWIFT environment. Software-based TOTP applications such as Google Authenticator, Microsoft Authenticator, or Authy do **not** meet this requirement.

Your SWIFT assessor is correct to flag this as a finding.

### The Specific Language

Control 4.2 requires that authentication for SWIFT operators combines at least two factors, and that the "something you have" factor must be a **hardware token** — a physical device that generates or stores credentials and cannot be extracted from the device. Software OTP apps running on a general-purpose smartphone do not satisfy this because:

1. **A smartphone is a general-purpose, internet-connected device** — it can be infected by malware that reads the TOTP seed or intercepts OTP codes in real time
2. **The TOTP seed can be backed up or cloned** — many authenticator apps allow cloud backup, meaning the "something you have" is no longer truly hardware-bound
3. **There is no tamper resistance** — a compromised phone means both factors (password stored in phone memory, OTP from the same phone) can be captured by an attacker simultaneously

The security intent of MFA — that compromising one factor does not compromise the session — breaks down when the second factor lives on a malware-susceptible general-purpose device.

---

## What CSCF v2026 Requires

| Requirement | Detail |
|------------|--------|
| Scope | All interactive operator logon sessions to Alliance Access and any other SWIFT-connected system |
| Factor 1 | Something you know (password compliant with Control 4.1) |
| Factor 2 | Something you have — must be a **hardware token** |
| Hardware token definition | A physical, tamper-resistant device that generates or holds credentials; the secret cannot be extracted from the device |
| Acceptable mechanisms | Dedicated hardware OTP tokens, hardware security keys (FIDO2/WebAuthn), smart card + PIN |
| Not acceptable | Software TOTP apps (Google Authenticator, Authy, Microsoft Authenticator), SMS OTP, email OTP |

---

## Concrete Hardware Token Options

### Option 1: RSA SecurID Hardware Tokens
- Industry standard in financial services for decades
- Physical token displays a 6-digit code that rotates every 60 seconds
- Integrates with Alliance Access via RSA Authentication Manager and RADIUS
- Tamper-resistant; seed never leaves the device
- Typical deployment: RSA Authentication Manager on-premises or RSA Cloud Authentication Service

### Option 2: Thales SafeNet (Gemalto) Hardware OTP Tokens
- SafeNet eToken PASS or OTP 110 series
- Similar TOTP/HOTP mechanism in a dedicated hardware device
- Widely used in banking environments
- Integrates via RADIUS or SafeNet Authentication Service

### Option 3: YubiKey (FIDO2 / OTP)
- YubiKey 5 series supports both hardware OTP and FIDO2/WebAuthn
- FIDO2 provides phishing-resistant authentication — the private key never leaves the device
- YubiKey OTP is hardware-bound (no extractable seed)
- May require custom RADIUS integration for Alliance Access depending on your version

### Option 4: Smart Card + PIN (PKI-based)
- Issue operator smart cards loaded with X.509 certificates
- Integrates via Windows smart card logon or dedicated smart card middleware
- Particularly strong as the private key is hardware-bound on the card chip
- Often combined with physical access badge for dual-purpose use

---

## Remediation Implementation Steps

1. **Assess your operator population**
   - Count all SWIFT operators requiring hardware MFA
   - Include IT admins with privileged access to SWIFT servers under Control 1.2

2. **Select a hardware token platform**
   - Evaluate RSA, Thales SafeNet, or YubiKey against your existing IAM infrastructure
   - Consider RADIUS vs. LDAP integration capability with your version of Alliance Access

3. **Procure hardware tokens**
   - Include spares (typically 10–15% buffer) for lost/broken devices
   - Procurement lead time: 2–6 weeks depending on vendor and quantity

4. **Deploy authentication infrastructure**
   - Install and configure RADIUS or authentication server (e.g., RSA Authentication Manager)
   - Configure Alliance Access to require MFA via the authentication server
   - Test integration in a non-production environment first

5. **Distribute tokens to operators and train**
   - Conduct enrollment sessions: bind each token to the named operator
   - Train operators on token use and reporting of lost/stolen devices
   - Update your token management procedures (Control 5.2 — Token Management)

6. **Update documentation and procedures**
   - Update the Incident Response Plan (Control 7.1) to include token compromise scenarios
   - Update the access control policy to specify hardware token requirement
   - Create a token lifecycle management procedure (issuance, renewal, revocation)

7. **Test and evidence**
   - Conduct a test run: verify no operator can authenticate with only password
   - Capture screenshots of MFA enforcement configuration as attestation evidence

---

## KYC-SA Attestation Timeline Implications

- **v2026 attestation window:** July 1 – December 31, 2026
- **Today's date:** July 2, 2026 — the window has just opened
- **Realistic remediation timeline:** 6–10 weeks for procurement, deployment, and rollout to all operators
- You should be able to complete remediation and attest **Implemented** for Control 4.2 well before the December 31, 2026 deadline
- Do not attest **Implemented** until all SWIFT operators are using hardware tokens — partial rollout requires **Partially Implemented** status
- Given this is a known finding from your assessor, document the remediation plan immediately and begin procurement this week to maintain schedule

Failure to remediate will result in a **Not Implemented** or **Partially Implemented** status for Control 4.2 in your KYC-SA attestation, which is visible to all your SWIFT counterparties.
