# System Boundary Description — FedRAMP Moderate SSP (Draft)

> **Note**: Use official FedRAMP templates from fedramp.gov — this content should be inserted into SSP Section 9: System Boundary Description and the accompanying boundary/data flow diagrams. This draft reflects FedRAMP Moderate (Class B under CR26) requirements.

---

## System Boundary Description

### 1. Authorization Boundary Overview

The [System Name] authorization boundary encompasses all components that process, store, or transmit federal information on behalf of the U.S. federal government. The boundary is defined by the logical and physical perimeters within which security controls are implemented and for which the Cloud Service Provider (CSP) accepts responsibility or shares responsibility with the federal agency and leveraged service providers.

The system is hosted on **Amazon Web Services (AWS) GovCloud (US)**, a FedRAMP High-authorized IaaS/PaaS environment. FedRAMP-authorized controls inherited from AWS GovCloud are identified in the Customer Responsibility Matrix (CRM) and the Customer IS Policy and Procedures (ISPP). All components within the authorization boundary operate within the AWS GovCloud (US) region.

---

### 2. System Components Within the Authorization Boundary

The following components are **within the authorization boundary** and are subject to FedRAMP Moderate controls:

| Component | Type | Description | Location |
|---|---|---|---|
| Web Application | Application | The primary SaaS application layer serving federal agency users; handles all user interactions and business logic | AWS GovCloud (US) — EC2 / ECS |
| Application Load Balancer | Network | Routes HTTPS traffic to application instances; terminates TLS using FIPS-compliant certificates | AWS GovCloud (US) — ALB |
| PostgreSQL Database | Database | Primary relational data store for all federal information processed by the system; stores structured federal data at rest | AWS GovCloud (US) — RDS |
| Redis Cache | Cache / Memory Store | In-memory caching layer for session data and application performance optimization; may transiently hold federal data | AWS GovCloud (US) — ElastiCache |
| Administrative Interface | Application | Internal administrative console used by CSP personnel for system management; access is restricted to authorized personnel | AWS GovCloud (US) |
| VPC (Virtual Private Cloud) | Network | Isolated network environment containing all in-boundary components; implements network segmentation and security group controls | AWS GovCloud (US) |
| S3 Buckets (Federal Data) | Storage | Object storage for federal data assets, logs, and backups; all buckets are encrypted at rest using FIPS 140-2 validated keys | AWS GovCloud (US) |
| CloudTrail / Logging Infrastructure | Logging | Centralized audit log collection and retention; captures all API and administrative activity within the boundary | AWS GovCloud (US) |

---

### 3. AWS GovCloud as the Infrastructure Layer

**AWS GovCloud (US)** is the underlying IaaS/PaaS provider for all system components within the boundary. AWS GovCloud holds a **FedRAMP High Authorization** (Package ID: FR1116111215), which means:

- **Inherited controls**: A significant subset of physical and environmental (PE), some system and communications protection (SC), and media protection (MP) controls are **fully inherited** from AWS GovCloud. These controls do not need to be re-implemented by the CSP.
- **Shared/leveraged controls**: Additional controls are partially inherited. The CSP's implementation must address the customer-configurable or customer-responsible portions documented in the AWS Customer Responsibility Matrix.
- **CSP-implemented controls**: All application-layer, data management, identity, and access controls are the CSP's responsibility and are fully implemented within the boundary.

All inherited and shared controls are documented in the **Customer IS Policy and Procedures (ISPP)** and **CIS/CRM workbook** appended to this SSP. The boundary diagram specifically identifies which components are customer-managed vs. AWS-managed.

> **Requirement**: The boundary diagram (SSP Appendix A) must depict the AWS GovCloud boundary, the CSP's tenant boundary within it, and the data flows to external services.

---

### 4. External Services and Interconnections (Outside the Authorization Boundary)

The following external services interact with the in-boundary system but are **outside the authorization boundary**. Each must be assessed for FedRAMP status and documented appropriately.

#### 4a. Okta (Authentication / Identity Provider)

| Attribute | Detail |
|---|---|
| Service | Okta Workforce Identity Cloud |
| Purpose | Federated authentication and Single Sign-On (SSO) for federal agency users |
| FedRAMP Status | Okta FedRAMP Moderate Authorized (verify current status at marketplace.fedramp.gov) |
| Data Exchanged | Authentication tokens (SAML/OIDC); user identity attributes; no federal business data transmitted |
| Connection Type | HTTPS/TLS; outbound from application to Okta identity endpoints |
| Responsibility | CSP configures the SAML/OIDC integration; Okta manages the identity service under its own ATO |

**Treatment**: Because Okta holds its own FedRAMP Moderate authorization, authentication delegation to Okta is acceptable for a FedRAMP Moderate system. The SSP must document this interconnection and reference Okta's FedRAMP package in the ISA/MOU section. The CRM must note which authentication controls (IA family) are leveraged from Okta.

**Interconnection Agreement Required**: An **Interconnection Security Agreement (ISA)** or equivalent **Memorandum of Understanding (MOU)** must be established with Okta documenting the data flows, security responsibilities, and terms of the interconnection.

#### 4b. SendGrid (Email Delivery Service)

| Attribute | Detail |
|---|---|
| Service | SendGrid / Twilio SendGrid Email API |
| Purpose | Transactional email delivery (notifications, alerts, account communications) |
| FedRAMP Status | **Verify at marketplace.fedramp.gov** — FedRAMP authorization status must be confirmed before use |
| Data Exchanged | Email addresses, notification content (may contain federal PII or system information) |
| Connection Type | HTTPS/API; outbound from application to SendGrid API endpoints |
| Responsibility | CSP configures API integration; SendGrid delivers email |

**Treatment — Critical Consideration**: If SendGrid is **not FedRAMP authorized**, its use requires explicit review and approval by the sponsoring agency's Authorizing Official (AO). Options include:
1. **Replace with a FedRAMP-authorized email service** (e.g., AWS SES within GovCloud, which is covered under the AWS GovCloud FedRAMP authorization)
2. **Document as a compensating control with AO approval**: If the agency AO accepts the risk, document the interconnection with compensating controls. However, federal email addresses and notification content are typically considered federal information and must be handled within the authorization boundary or by a FedRAMP-authorized service.
3. **Minimize data transmitted**: If SendGrid can be used with no federal PII in the email content (generic notifications only), the risk profile is lower, but this must be validated.

**Interconnection Agreement Required**: Regardless of FedRAMP status, an **Interconnection Security Agreement (ISA)** must be established with SendGrid documenting the data flows, security responsibilities, and scope of federal data transmitted.

---

### 5. Interconnection Security Agreements (ISA / MOU)

For each external service connected to the in-boundary system, FedRAMP requires documentation of the interconnection. At minimum, the following must be captured for each interconnection:

- **Purpose of the interconnection**
- **Data types and sensitivity of information exchanged**
- **Security controls applicable to the interconnection**
- **Roles and responsibilities for each party**
- **Security requirements the external party must meet**
- **Review and re-authorization frequency**

These are documented in **SSP Appendix B (Interconnection Table)** and supported by executed ISA/MOU agreements with each external service provider.

---

### 6. What Is Excluded from the Authorization Boundary

The following are **outside the authorization boundary** and not subject to FedRAMP controls under this authorization:

- Federal agency end-user workstations and networks (agency responsibility)
- Okta's internal identity service infrastructure (covered under Okta's own FedRAMP ATO)
- SendGrid's email delivery infrastructure (subject to ISA and AO review)
- Internet transit between end users and the application load balancer (public internet; perimeter security is implemented at the ALB/WAF layer within the boundary)

---

### 7. Boundary Diagram Requirements

The authorization boundary diagram (SSP Appendix A) must depict:
- All in-boundary components listed in Section 2 above
- AWS GovCloud as the underlying infrastructure layer, with inherited controls noted
- External service connections (Okta, SendGrid) shown as crossing the boundary
- Data flow arrows indicating the direction and type of data exchanged
- Trust zones / network segmentation within the boundary (public subnet, private subnet, database tier)
- Internet-facing entry points (load balancer, WAF)

---

*Use official FedRAMP templates from fedramp.gov — insert this content into SSP Section 9 and align with Appendix A (boundary diagram) and Appendix B (interconnection table). Verify Okta's and SendGrid's current FedRAMP authorization status at marketplace.fedramp.gov before finalizing.*
