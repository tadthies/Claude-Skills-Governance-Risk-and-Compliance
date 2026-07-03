# System Boundary Description — SSP Section 7 (General System Description / System Environment)

*Drafted for insertion into the official FedRAMP SSP template, Section 7. Target Certification Class: **C** (current "Moderate" baseline under CR26; NIST SP 800-53 Rev 5, 323 controls). Legacy label "FedRAMP Moderate" is used below alongside the CR26 Class C designation per the PMO transition guidance.*

> Use official FedRAMP templates from fedramp.gov — this content should be inserted into the appropriate template section (SSP Section 7, plus supporting tables that feed Appendix K – Integrated Inventory Workbook and Appendix I – CIS/CRM Workbook).

---

## 7.1 Authorization Boundary Narrative

[System Name] ("the System") is a [SaaS / web application] delivered as a browser-based application hosted entirely within **Amazon Web Services GovCloud (US)**, a FedRAMP High-authorized Infrastructure-as-a-Service (IaaS) environment. The authorization boundary encompasses all components that process, store, or transmit federal information on behalf of [Agency/Customer], specifically:

- **Application tier**: Web application servers (containerized/EC2-based, specify compute service) running in GovCloud, behind an Application Load Balancer, serving the front-end and API layer
- **Data tier**: A PostgreSQL database (Amazon RDS for PostgreSQL, GovCloud region) storing federal data at rest
- **Caching tier**: A Redis in-memory cache (Amazon ElastiCache for Redis, GovCloud region) used for session state and application caching
- **Supporting infrastructure**: VPC networking, security groups/NACLs, load balancers, AWS Config, CloudTrail, GuardDuty, and Security Hub, all deployed within the GovCloud region

All boundary components reside exclusively within AWS GovCloud (US) region endpoints. No standard AWS commercial region endpoints are used for any component that processes, stores, or transmits federal data — this distinction must be maintained to keep the system inside the authorized boundary.

**Everything that processes, stores, or transmits federal data is inside this boundary.** No federal data is written to, cached in, or transmitted through any service outside the boundary defined below.

---

## 7.2 Leveraged Authorization (Inherited Controls)

The System leverages **AWS GovCloud (US)**, which holds a FedRAMP High Provisional Authorization to Operate (P-ATO) as the underlying IaaS. Physical & Environmental (PE) controls and a substantial portion of System & Communications Protection (SC) controls are inherited from this leveraged authorization. Inherited vs. hybrid vs. CSP-implemented control responsibilities are documented in detail in **Appendix I (CIS/CRM Workbook)** and must be kept consistent with this boundary description.

---

## 7.3 External Connections / Interconnections Table

External services connected to in-scope components must be either FedRAMP-authorized or documented here with compensating controls. Both external integrations below are outside the authorization boundary and are documented as external connections, not inherited systems.

| # | External Service | Purpose | Direction | Data Exchanged | FedRAMP Status | Connection Security | Boundary Treatment |
|---|---|---|---|---|---|---|---|
| 1 | **Okta** (Identity Provider) | User authentication / SSO, MFA enforcement | Bidirectional (System ↔ Okta) | Authentication tokens (SAML/OIDC assertions), user identity attributes (username, email, role claims) — **no federal mission data** | Verify current Okta FedRAMP authorization status (Okta maintains a FedRAMP High-authorized offering; confirm the specific tenant/offering in use is the authorized instance) | TLS 1.2+ in transit; OAuth 2.0/OIDC or SAML 2.0 federation; MFA enforced | External — outside boundary. If the specific Okta instance/tenant used is NOT the FedRAMP-authorized offering, this must be documented as a non-authorized external connection with compensating controls and flagged as a POA&M risk item pending remediation or ISA |
| 2 | **SendGrid** (Email/Notification Service) | Transactional/notification email delivery (e.g., password reset, alerts) | Outbound only (System → SendGrid) | Email addresses, notification content — **confirm no CUI or federal mission data is included in email payloads** | Verify current SendGrid FedRAMP authorization status; if not FedRAMP-authorized, this is an unauthorized external connection requiring compensating controls or removal from data flows carrying federal data | TLS 1.2+ in transit; API key authentication | External — outside boundary. Recommend restricting SendGrid to system-generated notification metadata only, never CUI, to minimize boundary risk |

**Action item for CSP**: Confirm and document the exact FedRAMP authorization status (Marketplace listing, authorization package ID, and impact level) for both Okta and SendGrid before this SSP is submitted. If either service is not independently FedRAMP-authorized at or above Class C (Moderate), an Interconnection Security Agreement (ISA) and compensating controls (e.g., data minimization, no CUI transmitted, contractual security requirements) must be documented, and this should be flagged as a POA&M candidate if a compensating control gap exists.

---

## 7.4 Ports, Protocols, and Services (Summary)

| Component | Protocol | Port | Purpose | Encryption |
|---|---|---|---|---|
| End user ↔ Application Load Balancer | HTTPS | 443 | User/admin web traffic | TLS 1.2+, FIPS 140-2/3 validated module |
| Application ↔ PostgreSQL (RDS) | PostgreSQL (TLS-wrapped) | 5432 | Application data read/write | TLS 1.2+ in transit; AES-256 at rest (AWS KMS, FIPS validated) |
| Application ↔ Redis (ElastiCache) | Redis (TLS-enabled) | 6379 | Session/cache read/write | TLS in transit (in-transit encryption enabled); encryption at rest enabled |
| Application ↔ Okta | HTTPS (OIDC/SAML) | 443 | Authentication federation | TLS 1.2+ |
| Application ↔ SendGrid | HTTPS (REST API) | 443 | Outbound email/notifications | TLS 1.2+ |
| Admin/management access ↔ AWS Console/CLI | HTTPS | 443 | Privileged administrative access (FIPS endpoints) | TLS 1.2+, MFA required |

*Note: This table must be embedded alongside the network/data flow diagram and kept internally consistent with the External Connections table above — a common source of 3PAO findings is a mismatch between the narrative, the diagram, and this table.*

---

## 7.5 Network / Data Flow Diagram (Placeholder)

*[Insert architecture diagram here.]* The diagram must depict, at minimum:

1. The GovCloud VPC boundary drawn explicitly around the application tier, PostgreSQL (RDS), and Redis (ElastiCache) — this line **is** the authorization boundary
2. Public-facing ingress path (end user → ALB → application tier)
3. Internal data flows (application → RDS, application → ElastiCache)
4. Administrative/management access path (privileged users → AWS IAM/Console/CLI, with MFA)
5. Both external connections (Okta, SendGrid) drawn **outside** the boundary line, with arrows showing direction of data flow and labels matching Section 7.3
6. Logging/monitoring data flows to centralized SIEM (AWS CloudTrail/Config/GuardDuty/Security Hub or equivalent aggregation)

**Common finding to avoid**: Admin/management traffic paths and monitoring/logging data flows are frequently omitted from boundary diagrams — ensure both are explicitly drawn.

---

## 7.6 Boundary Exclusions (Explicitly Out of Scope)

- Corporate/internal IT systems not used to deliver the CSO (e.g., internal HR systems, corporate email — unless SendGrid is used for internal notifications, in which case re-evaluate)
- Any AWS commercial (non-GovCloud) region resources
- Okta and SendGrid infrastructure themselves (only the connection/integration points are documented; the vendors' internal environments are out of scope and covered by their own authorization or contractual assurances)
- Developer/CI-CD environments not connected to the production boundary (document separately if shared)

---

## 7.7 Open Items / Recommended POA&M or Pre-Submission Actions

1. **Confirm Okta and SendGrid FedRAMP authorization status** — this is the single most likely source of a 3PAO finding for this architecture. If either is not authorized at Class C/Moderate or higher, document compensating controls and an ISA, or restrict data shared with the unauthorized service to non-federal, non-CUI metadata only.
2. Verify Redis (ElastiCache) and RDS PostgreSQL both have encryption at rest enabled using FIPS 140-2/3 validated modules (AWS KMS) — populate **Appendix L (Cryptographic Modules Table)**.
3. Ensure all GovCloud resources use **GovCloud region endpoints** (not standard commercial endpoints) for every boundary component, including FIPS endpoints for IA-related traffic.
4. Populate **Appendix K (Integrated Inventory Workbook)** with every asset named above (ALB, application instances, RDS instance, ElastiCache cluster) — must be 100% accurate; auditors sample from this workbook.
5. Ensure vulnerability scanning coverage extends to the web application, PostgreSQL database, and any container images — a common architecture finding is scan coverage gaps on data-tier or cache-tier components.
6. Cross-reference this boundary description with the CIS/CRM workbook (Appendix I) to confirm PE controls are marked as inherited from AWS GovCloud, and SC controls are marked hybrid/inherited as appropriate.

---

*This draft should be inserted into SSP Section 7 (General System Description / System Environment) of the official FedRAMP SSP template. It must remain internally consistent with the architecture diagrams, the External Connections table, the Ports/Protocols/Services table, Appendix I (CIS/CRM), and Appendix K (IIW) — inconsistency across these artifacts is one of the most common sources of 3PAO findings and authorization delays.*
