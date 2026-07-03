# System Boundary Description

## 1. Purpose

This section defines the authorization boundary for [System Name] ("the System") as required for FedRAMP Moderate authorization. It identifies the components, services, data flows, and interconnections that are within the scope of assessment, and distinguishes them from external, corporate, and leveraged services that fall outside the boundary.

## 2. System Overview

[System Name] is a web-based application that provides [brief description of business function] to federal agency users. The System is hosted entirely within Amazon Web Services (AWS) GovCloud (US), a FedRAMP-authorized Infrastructure-as-a-Service (IaaS) environment. The System leverages the underlying AWS GovCloud FedRAMP High authorization for physical, environmental, and infrastructure-level controls, and inherits those controls per the applicable Customer Responsibility Matrix (CRM).

The System architecture consists of the following major components:

- A web application tier (application servers/containers) serving end-user and API traffic
- A PostgreSQL relational database for persistent data storage
- A Redis in-memory cache used for session management and application performance optimization
- Integration with Okta for identity and access management / authentication
- Integration with SendGrid for outbound transactional and notification email delivery

## 3. Authorization Boundary Diagram

*[Insert boundary diagram here. The diagram must visually depict all components below, boundary lines, data flow direction and arrows, network zones/subnets, and the demarcation between the authorization boundary and external/leveraged/corporate systems, per FedRAMP diagram guidance (e.g., use of a dashed red or clearly labeled line denoting the boundary).]*

## 4. Components Within the Authorization Boundary

### 4.1 Cloud Infrastructure (Leveraged Authorization)
- **AWS GovCloud (US)** — FedRAMP High authorized IaaS. Provides compute (EC2/ECS/EKS as applicable), storage (EBS/S3), networking (VPC), and managed services consumed by the System. Physical/environmental controls, hypervisor security, and foundational network controls are inherited from the AWS GovCloud FedRAMP authorization; the CRM identifies AWS's shared responsibilities.

### 4.2 Network Architecture
- Dedicated Amazon VPC(s) with public and private subnets across multiple Availability Zones for high availability
- Public-facing subnet(s) hosting load balancer(s)/API gateway/WAF for internet-facing traffic
- Private subnet(s) hosting application servers, database, and cache — no direct internet ingress
- Security groups and network ACLs enforcing least-privilege, deny-by-default traffic rules
- AWS WAF and/or equivalent boundary protection for the internet-facing tier
- VPC Flow Logs and network traffic monitoring feeding the System's centralized logging/SIEM

### 4.3 Compute / Application Tier
- Web/application servers (EC2 instances, containers, or serverless compute) running the System's application code
- Auto-scaling configuration bounded within the authorized VPC(s)
- Load balancer(s) (e.g., Application Load Balancer) terminating TLS and distributing traffic to application instances
- Bastion host / AWS Systems Manager Session Manager for authorized administrative access (no direct SSH from the internet)

### 4.4 Data Tier
- **PostgreSQL database** (e.g., Amazon RDS for PostgreSQL, Multi-AZ) — hosted in a private subnet, encrypted at rest (AWS KMS) and in transit (TLS), not directly internet-accessible. Stores application data, including any Controlled Unclassified Information (CUI) or federal data processed by the System.
- **Redis cache** (e.g., Amazon ElastiCache for Redis) — hosted in a private subnet, used for session state and performance caching. Encryption at rest and in transit enabled; access restricted to application tier security groups only.

### 4.5 Identity, Logging, and Management Services
- AWS Identity and Access Management (IAM) for administrative and service-level access control
- AWS Key Management Service (KMS) for encryption key management
- Centralized logging (e.g., CloudWatch, CloudTrail, and/or SIEM integration) capturing audit events across all in-boundary components
- Vulnerability scanning and configuration management tooling operating within the boundary

## 5. External Services and Interconnections (Leveraged/Interconnected Systems)

The following third-party services are **external to the authorization boundary** but interconnect with the System. Each interconnection is documented with a corresponding entry in the System's Interconnection Security Agreement (ISA)/data flow documentation, and data exchanged with these services is limited to what is necessary for the stated function.

### 5.1 Okta (Authentication / Identity Provider)
- **Function**: Provides identity federation and/or multi-factor authentication (MFA) for user login via SAML 2.0 or OIDC.
- **Data exchanged**: Authentication assertions/tokens; user identifiers and attributes required for authorization decisions (e.g., username, email, role/group claims). No system data (application/CUI data) is transmitted to Okta.
- **Boundary treatment**: Okta is a leveraged external SaaS authentication service, outside the FedRAMP authorization boundary. The connection occurs over TLS 1.2+ via outbound API calls and browser redirects. Okta's own compliance posture (e.g., FedRAMP authorization status, if applicable) must be documented; if Okta is not itself FedRAMP authorized, this must be addressed in the risk assessment and the agency's risk acceptance.
- **Note**: If Okta FedRAMP-authorized offering (Okta for Government / Okta GovCloud) is used, cite the applicable FedRAMP authorization package (P-ATO/ATO) and package ID.

### 5.2 SendGrid (Email Delivery)
- **Function**: Outbound transactional and notification email delivery (e.g., password resets, alerts, notifications) via API integration.
- **Data exchanged**: Recipient email addresses and message content limited to notification purposes. No authentication credentials or sensitive CUI should be transmitted via email content; this must be enforced through application-level data handling standards.
- **Boundary treatment**: SendGrid is an external SaaS service outside the authorization boundary. Connection occurs via outbound TLS-encrypted API calls from the application tier. If SendGrid is not FedRAMP authorized, this interconnection requires documented risk acceptance by the Authorizing Official (AO), including a description of compensating controls (e.g., data minimization in email content, restricting PII/CUI from email bodies).

### 5.3 Interconnection Table (to be completed in ISA/Interconnection documentation)

| External Service | Purpose | Direction | Protocol/Port | Data Classification | FedRAMP Status | Authorization Reference |
|---|---|---|---|---|---|---|
| Okta | Authentication/SSO/MFA | Outbound (App → Okta) | HTTPS/443 (SAML/OIDC) | Auth metadata only | [TBD - confirm] | [ATO/P-ATO ID if applicable] |
| SendGrid | Transactional email | Outbound (App → SendGrid) | HTTPS/443 (API) | Notification content, email addresses | [TBD - confirm] | [ATO/P-ATO ID if applicable] |

## 6. Corporate / Management Systems Outside the Boundary

The following are explicitly **excluded** from the authorization boundary but support the System's operation:

- Corporate identity provider used for internal employee/administrator directory services (if distinct from Okta tenant serving the application)
- Corporate ticketing, HR, and IT service management systems
- Developer workstations and corporate office network (code is deployed via CI/CD into the boundary; workstations themselves are not part of the boundary)
- Source code repository and CI/CD pipeline tooling (unless explicitly included — many FedRAMP SSPs treat the deployment pipeline as a separate, documented process with controls addressed in SA-family controls, without including the tooling itself inside the runtime authorization boundary)

## 7. Data Flow Summary

1. End users (federal agency personnel/public users, as applicable) initiate HTTPS connections to the System's public-facing load balancer/WAF within AWS GovCloud.
2. Authentication requests are redirected to Okta for identity verification; Okta returns a signed assertion/token to the application.
3. Authenticated requests are routed to the application tier within the private subnet.
4. The application tier reads/writes persistent data to the PostgreSQL database and reads/writes session/cache data to Redis, both within private subnets, with no direct internet exposure.
5. The application tier makes outbound API calls to SendGrid to trigger transactional emails as needed.
6. All administrative access to infrastructure components occurs through AWS IAM-authenticated, logged pathways (e.g., Systems Manager Session Manager), not direct public network access.
7. All in-boundary components emit logs to a centralized logging/monitoring solution for audit, alerting, and continuous monitoring purposes.

## 8. Boundary Determination Rationale

Per FedRAMP guidance, the authorization boundary encompasses all components that store, process, or transmit federal data and are under the direct configuration/security control of the Cloud Service Provider (CSP). Accordingly:

- **Included**: All AWS GovCloud resources provisioned and configured by the CSP (compute, network, PostgreSQL database, Redis cache, load balancers, logging/monitoring, IAM) because the CSP has direct control over their configuration and security posture, and they store/process/transmit federal data.
- **Excluded (leveraged/interconnected)**: Okta and SendGrid, because they are independently operated, multi-tenant SaaS platforms not configured or controlled by the CSP at the infrastructure level, and are accessed only via defined API/authentication interfaces. These are documented as external services/leveraged authorizations with corresponding interconnection agreements, data flow diagrams, and risk treatment in the SSP.

## 9. Open Items for Completion

- [ ] Confirm and document Okta's FedRAMP authorization status (Okta for Government vs. commercial Okta) and attach ATO/P-ATO reference if applicable
- [ ] Confirm and document SendGrid's FedRAMP authorization status; if not authorized, document AO risk acceptance and compensating controls
- [ ] Finalize and insert the authorization boundary diagram showing all components, subnets, and data flows
- [ ] Complete ISA/interconnection documentation for Okta and SendGrid
- [ ] Confirm whether CI/CD pipeline and code repository should be included in or explicitly excluded from the boundary, with rationale
- [ ] Validate encryption specifications (FIPS 140-2/140-3 validated modules) for data at rest and in transit across all components
- [ ] Confirm multi-AZ/high-availability configuration details for RDS PostgreSQL and ElastiCache Redis
- [ ] Populate System Name and business function description in Sections 1–2

---
*This draft is a starting template for the System Boundary Description section of a FedRAMP Moderate SSP and should be reviewed by the ISSO/system owner, tailored with environment-specific details (account IDs, CIDR ranges, service names), and validated against the current FedRAMP SSP template and FedRAMP Authorization Boundary Guidance before submission to the 3PAO/AO.*
