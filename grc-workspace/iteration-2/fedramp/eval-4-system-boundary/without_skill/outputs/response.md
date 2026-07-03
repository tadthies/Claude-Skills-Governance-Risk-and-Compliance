# System Boundary Description — FedRAMP Moderate SSP (Draft)

> **Note**: This content should be inserted into the System Boundary Description section of your FedRAMP Moderate SSP (typically Section 9). Use official FedRAMP templates from fedramp.gov.

---

## System Boundary Description

### 1. Authorization Boundary Overview

The [System Name] authorization boundary defines the scope of the FedRAMP authorization and encompasses all components that process, store, or transmit federal information. Only components within this boundary are covered by the security controls documented in this System Security Plan (SSP). Components outside the boundary — including external SaaS tools used by the system — are addressed through interconnection agreements and are subject to their own security authorizations.

The system is deployed on **Amazon Web Services (AWS) GovCloud (US)**, which serves as the underlying infrastructure-as-a-service (IaaS) and platform-as-a-service (PaaS) layer. AWS GovCloud holds a FedRAMP High Authorization; many physical, environmental, and infrastructure-level security controls are inherited from AWS GovCloud under the shared responsibility model.

---

### 2. System Components Within the Authorization Boundary

The following components are **within the FedRAMP authorization boundary** and are subject to FedRAMP Moderate controls:

| Component | Type | Description |
|---|---|---|
| Web Application | Application | The core SaaS application; handles user requests, business logic, and federal data processing. Hosted on AWS GovCloud (EC2/ECS). |
| Application Load Balancer (ALB) | Network | Receives and distributes inbound HTTPS traffic to the web application tier. TLS termination using FIPS-compliant certificates. |
| PostgreSQL Database | Database (RDS) | Primary relational data store for all federal information. Data is encrypted at rest using FIPS 140-2 validated AES-256. |
| Redis Cache (ElastiCache) | In-Memory Cache | Stores session state and cached data to improve performance. May transiently hold federal data. |
| AWS GovCloud VPC | Network | Isolated virtual network environment. Contains all in-boundary components, with security groups and NACLs enforcing network segmentation. |
| S3 Buckets | Object Storage | Stores application data, logs, and backups. Encrypted at rest; access controlled via IAM policies. |
| CloudTrail / Logging | Logging / SIEM | Centralized audit log collection for all API calls and administrative activity within the boundary. |
| Administrative Portal | Application | Internal management interface for CSP personnel. Restricted to authorized staff via MFA-protected access. |

---

### 3. AWS GovCloud as the Infrastructure Layer

**AWS GovCloud (US)** is the FedRAMP-authorized IaaS/PaaS platform underlying all in-boundary components. Key points:

- **FedRAMP Authorization**: AWS GovCloud holds a FedRAMP High authorization. This is a higher baseline than FedRAMP Moderate, meaning all controls applicable to Moderate are covered at the infrastructure level.
- **Inherited controls**: Physical and environmental (PE family) controls, facility security, hardware maintenance, and certain media protection controls are fully inherited from AWS GovCloud. These do not need to be re-implemented by the CSP.
- **Shared responsibility**: Controls such as network access control, encryption configuration, and identity management are shared between AWS and the CSP. The CSP must implement the customer-responsible portions.
- **Documented in the CRM**: All inherited and shared controls are identified in the Customer Responsibility Matrix (CRM) appendix to this SSP.

The authorization boundary is drawn at the **tenant/account level within AWS GovCloud** — the CSP's AWS GovCloud account(s) and the resources within them constitute the in-boundary environment.

---

### 4. External SaaS Integrations

The system integrates with two external SaaS tools that are **outside the authorization boundary**. These integrations involve data flowing across the boundary and must be carefully documented and managed.

#### 4a. Okta (Authentication)

- **Purpose**: Federated identity and Single Sign-On (SSO) for end users
- **Data exchanged**: Authentication tokens (SAML 2.0 / OIDC), user identity attributes. No federal business data is transmitted to Okta.
- **FedRAMP Status**: Okta holds a FedRAMP Moderate authorization (verify current status at marketplace.fedramp.gov)
- **Risk**: Since Okta is FedRAMP Moderate authorized and only receives authentication metadata (not federal business data), this integration is acceptable for a FedRAMP Moderate system
- **Required documentation**: An **Interconnection Security Agreement (ISA)** or **Memorandum of Understanding (MOU)** must be executed with Okta, documenting the integration scope, data types exchanged, and security responsibilities

#### 4b. SendGrid (Email)

- **Purpose**: Transactional email delivery (notifications, alerts, system emails)
- **Data exchanged**: Email addresses, notification content. Depending on content, federal PII or system-sensitive information may be included in emails.
- **FedRAMP Status**: Verify at marketplace.fedramp.gov. **If SendGrid is not FedRAMP authorized**, this is a significant finding that requires resolution:
  - Option 1: Replace with AWS SES within GovCloud (covered under the AWS GovCloud FedRAMP authorization)
  - Option 2: Obtain AO approval with documented compensating controls and risk acceptance
  - Option 3: Strictly limit email content to non-federal, non-PII notifications (reduces but may not eliminate the risk)
- **Required documentation**: An **Interconnection Security Agreement (ISA)** documenting data flows, security requirements, and responsibilities

---

### 5. Interconnection Security Agreements (ISA / MOU)

For each external system connected to the in-boundary environment, FedRAMP requires an **Interconnection Security Agreement (ISA)** or **Memorandum of Understanding (MOU)**. These agreements document:

- The purpose of the interconnection
- Types of data transmitted across the boundary
- Security controls applicable to the interconnection
- Respective security responsibilities of each party
- Conditions under which the interconnection may be terminated

ISAs for Okta and SendGrid must be completed, reviewed by the agency AO, and included in the SSP's interconnection table (typically Appendix B).

---

### 6. Boundary Diagram

The authorization boundary diagram (required as an appendix to the SSP) must show:
- All in-boundary components and their relationships
- AWS GovCloud as the underlying infrastructure layer
- External connections (Okta, SendGrid) crossing the boundary
- Data flows with directionality indicated
- Trust zones and network segmentation (public vs. private subnets, database tier isolation)
- User access paths (federal agency users accessing the web application over the internet via the load balancer)

---

*Insert this content into the System Boundary Description section of the official FedRAMP SSP template. Verify all external service FedRAMP authorizations at marketplace.fedramp.gov.*
