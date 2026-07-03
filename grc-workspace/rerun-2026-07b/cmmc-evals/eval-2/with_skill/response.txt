# CMMC Level 2 Gap Assessment

Based on the current-state information provided, here is a gap assessment of the relevant NIST SP 800-171 practice areas, an estimated SPRS score impact, and a prioritized remediation plan.

## Scope Note
This assessment covers the practices directly implicated by the facts given. A full certification-ready gap assessment must cover all 110 Level 2 practices — the items below are the ones your stated current state clearly touches. Treat this as a starting point, not a complete SSP-ready assessment.

## Gap Table

| Practice ID | Domain | Practice Statement | Status | Evidence Needed | Gap Notes |
|---|---|---|---|---|---|
| IA.L2-3.5.3 | IA | MFA for local/network access to privileged accounts and network access to non-privileged accounts | 🟡 PARTIAL | MFA enrollment reports across all CUI-accessing systems | MFA only on cloud email — no MFA on internal apps, file shares, VPN admin access, or endpoints. This is one of the most commonly failed practices and a **critical practice — cannot be POA&M'd at certification**. |
| SC.L2-3.13.11 | SC | Employ FIPS-validated cryptography when used to protect CUI | ❌ NOT MET | Encryption configuration exports showing FIPS 140-2/3 validated modules | No FIPS-validated encryption for CUI at rest. **Critical practice — cannot be POA&M'd at certification.** |
| SC.L2-3.13.16 | SC | Protect CUI at rest | ❌ NOT MET | Encryption/access control evidence for data at rest | Directly tied to the FIPS gap above; CUI on shared drives with no encryption at rest is a significant exposure. |
| AC.L2-3.1.3 | AC | Control the flow of CUI in accordance with approved authorizations | ❌ NOT MET | Data flow diagrams, access control lists, folder/share permissions | Flat network with CUI on shared drives means CUI flow is effectively uncontrolled. **Critical practice — cannot be POA&M'd at certification.** |
| AC.L2-3.1.20 | AC | Verify and control/limit connections to external systems | 🟡 PARTIAL | Network diagram, boundary control config | Flat network topology suggests weak segmentation between CUI and non-CUI systems/external connections. |
| MP.L2-3.8.1 / 3.8.2 | MP | Protect and limit access to CUI on system media | ❌ NOT MET | Access control lists, media inventory | CUI on shared drives with (implied) broad access is a Media Protection gap as well as an Access Control gap. |
| CA.L2-3.12.4 | CA | Develop, document, and periodically update SSPs | ❌ NOT MET | Current, approved SSP | SSP last updated in 2022 — 4 years stale. Must be reviewed/updated at least annually or after significant change. |
| IR.L2-3.6.1 | IR | Establish an operational incident-handling capability | 🟡 PARTIAL | IR plan, roles/responsibilities, tooling | Plan exists but is unvalidated — "established" in name only until tested. |
| IR.L2-3.6.3 | IR | Test the organizational incident response capability | ❌ NOT MET | Tabletop exercise records, after-action reports | Never tested. **IR.L2-3.6.1 is a critical practice, and an untested plan puts its MET status at real risk during assessment** — assessors will likely downgrade 3.6.1 to NOT MET without demonstrated testing. |
| AT.L2-3.2.1 / 3.2.2 | AT | Security awareness and role-based training | ✅ MET | Training records, completion logs | Annual security awareness training in place. Confirm role-based training also covers personnel with specialized security responsibilities (IT admins, ISSO). |
| PS.L2-3.9.1 | PS | Screen individuals prior to authorizing access to CUI systems | ✅ MET | Background check records | Background screening in place for all staff — good baseline control. |
| AU.L2-3.3.1 | AU | Create and retain system audit logs | ❌ NOT MET (assumed) | SIEM/log configuration, retention policy | Not explicitly stated, but a flat network with no mention of centralized logging strongly suggests this is a gap. **Critical practice — cannot be POA&M'd at certification.** Confirm actual state before finalizing this line. |

## Estimated SPRS Score Impact

Starting score: **110**. Applying the standard weighted deductions (highest-impact practices lose 5 points each; no partial credit for partial implementation):

| Practice | Status | Deduction |
|---|---|---|
| IA.L2-3.5.3 (MFA) | NOT MET (partial = full deduction) | −5 |
| SC.L2-3.13.11 (FIPS crypto) | NOT MET | −5 |
| SC.L2-3.13.16 (CUI at rest) | NOT MET | −1 (est.) |
| AC.L2-3.1.3 (CUI flow control) | NOT MET | −5 |
| AC.L2-3.1.20 (external connections) | PARTIAL → full deduction | −1 (est.) |
| MP.L2-3.8.1/3.8.2 (media protection) | NOT MET | −1 each (est.) |
| CA.L2-3.12.4 (SSP current) | NOT MET | −1 (est.) |
| IR.L2-3.6.1 (IR capability) | AT RISK — treat as NOT MET | −3 (est.) |
| IR.L2-3.6.3 (IR testing) | NOT MET | −1 (est.) |
| AU.L2-3.3.1 (audit logging, assumed gap) | NOT MET | −3 |

**Rough estimated current score: ~85–88 out of 110** (exact figure depends on your full 110-practice assessment — this only reflects the domains covered by your current-state summary; other unassessed domains could move the score further in either direction). Note that AC.L2-3.1.3, IA.L2-3.5.3, and SC.L2-3.13.11 are your three highest-value, highest-risk gaps at 5 points each and are also all POA&M-ineligible at certification — these must be fully remediated before you can certify at all, regardless of your overall score.

## Prioritized Remediation Plan

**Tier 1 — Critical practices, must be MET before certification (target: 60–90 days)**
1. **IA.L2-3.5.3 — Expand MFA** beyond cloud email to all systems accessing CUI: VPN, file shares, admin accounts, workstations. This is the single most commonly failed practice industry-wide — prioritize it first.
2. **SC.L2-3.13.11 / SC.L2-3.13.16 — Deploy FIPS-validated encryption** for CUI at rest. Verify any existing "AES-256" claims actually use FIPS 140-2/3 validated cryptographic modules — this is a very common false-positive gap.
3. **AC.L2-3.1.3 — Eliminate the flat network.** Segment CUI into a dedicated enclave (separate VLAN/domain) with access controls enforcing least privilege and need-to-know. This also shrinks your future assessment scope.
4. **AU.L2-3.3.1 — Stand up centralized audit logging** covering all CUI-touching systems (confirm actual current state first).
5. **IR.L2-3.6.1 — Validate/strengthen the incident response plan** so it holds up as a genuinely operational capability, not just a document.

**Tier 2 — High-value, non-critical (target: 90–150 days)**
6. **IR.L2-3.6.3 — Run a tabletop exercise** to test the IR plan and document results; this also strengthens the IR.L2-3.6.1 evidence.
7. **MP.L2-3.8.1/3.8.2 — Lock down shared drives**: apply access controls, remove CUI from general shares, move to the new CUI enclave.
8. **AC.L2-3.1.20 — Formalize external connection controls** as part of the enclave build.

**Tier 3 — Documentation and process (target: parallel, ongoing)**
9. **CA.L2-3.12.4 — Rewrite the SSP** to reflect the new enclave architecture, current controls, and remediation status; this should be the last major deliverable since it documents the end state, but start the skeleton now.
10. **Build the POA&M** for any Tier 2/3 items not yet closed at assessment time — remember only non-critical practices are POA&M-eligible, and any open item has a 180-day closeout clock once conditional certification is granted.

**Sequencing rationale**: Tier 1 items are both the highest SPRS point value and legally required to be fully MET before any certification (conditional or final) — deprioritizing them risks a failed assessment regardless of how well everything else is documented. Fix MFA and encryption first since they are usually the fastest wins (procurement + configuration, not architecture change); the network segmentation effort (AC.L2-3.1.3) typically takes longest and should start in parallel immediately.

---
*This gap assessment is based on the limited current-state summary provided and general compliance guidance — not legal advice. A certification-ready assessment requires evaluating all 110 practices with full evidence collection. Consult a Registered Practitioner or C3PAO for a formal readiness review.*
