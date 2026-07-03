# Hosting RESTRICTED Data Offshore (AWS Sydney) — NZISM and NZ Government Cloud Policy Considerations

## Short Answer

It is potentially possible, but it is **not a default or automatic option** — hosting RESTRICTED New Zealand government data offshore (including in an Australian region such as AWS Sydney) requires a formal risk assessment, specific approvals, and compensating controls. It is not something an agency can simply decide to do without going through the appropriate governance and risk-acceptance process. Many agencies default to NZ-based or All-of-Government (AoG) cloud arrangements for classified data precisely because offshore hosting introduces additional legal, sovereignty, and jurisdictional risk that must be explicitly managed.

## Key Considerations

### 1. Data Sovereignty and Jurisdiction
Storing RESTRICTED data in an offshore region (Australia) means the data becomes subject to the foreign jurisdiction's laws (e.g., potential access requests under Australian law) in addition to New Zealand law. This is a primary risk factor the NZISM and related NZ government guidance require agencies to assess — including who could compel access to the data, under what legal authority, and whether that is acceptable given the classification and sensitivity of the information.

### 2. NZISM Cloud Computing Guidance
The NZISM includes a chapter/section specifically addressing cloud computing, which generally requires agencies to:
- Conduct a **cloud risk assessment** before onboarding any cloud service for government information, particularly for classified data
- Consider the **classification of the data** against the cloud service provider's certification status and the jurisdiction(s) where data will be stored/processed/backed up
- Ensure appropriate **encryption** (both at rest and in transit) using NZ-approved cryptographic algorithms and appropriate key management (ideally with the agency retaining control of encryption keys, not solely the cloud provider)
- Confirm the CSP has appropriate **certifications/assessments** (e.g., relevant to the NZ Government's cloud risk assessment framework, or equivalent recognised frameworks)
- Establish contractual and technical controls addressing data residency, access logging, incident notification, and data deletion/return at contract termination

### 3. NZ Government Cloud Policy / All-of-Government (AoG) Cloud Framework
New Zealand's government-wide cloud policy (administered historically via the GCDO/Department of Internal Affairs, and security-endorsed via GCSB/NCSC) generally expects agencies to:
- Use **All-of-Government cloud services** or panel/marketplace arrangements where available, which have often undergone a degree of pre-assessment
- Complete a **cloud risk assessment** appropriate to the sensitivity of the data — the higher the classification, the more rigorous the assessment required
- For classified information (RESTRICTED and above), obtain sign-off from the agency's **Accreditation Authority** and consult with the **GCSB/NCSC** as the national technical authority, since offshore hosting of classified data is a heightened-risk decision
- Explicitly document the decision to host offshore, including risk acceptance by an appropriately senior/delegated authority

### 4. Specific Factors for AWS Sydney (Offshore, but in Australia)
- Being in Australia (a Five Eyes partner) may be viewed more favourably than a non-partner jurisdiction, but this does **not remove the requirement for formal risk assessment and approval** — proximity/alliance relationships reduce but do not eliminate sovereignty and jurisdictional risk.
- You should confirm whether AWS's Sydney region and the specific services you intend to use have been assessed under any NZ Government cloud risk assessment/certification process, and whether AWS has provided the necessary compliance attestations relevant to NZ government requirements.
- Consider whether an **NZ-based region or an NZ-sovereign cloud offering** is available and would avoid the offshore risk question altogether — this is often the simpler compliant path for RESTRICTED data if timelines allow.

### 5. Process You Should Follow
1. **Classify and confirm** the data truly requires RESTRICTED handling and confirm handling requirements under the NZISM for that classification.
2. **Conduct a formal cloud risk assessment** (per NZISM cloud guidance) specifically evaluating offshore storage in AWS Sydney — covering legal/jurisdictional risk, CSP security posture, encryption/key management, access controls, incident response, and exit/data-return provisions.
3. **Consult the GCSB/NCSC** (as the national technical authority for government information security) for guidance/endorsement, given the classification level involved.
4. **Engage your agency's ITSM/CISO and Accreditation Authority** — a decision to host RESTRICTED data offshore should go through your system's C&A process, with the offshore hosting risk explicitly documented and formally accepted (not assumed).
5. **Implement compensating controls**: strong encryption with NZ/agency-controlled keys, contractual data residency and access commitments from AWS, logging/monitoring of access, and a documented incident notification path.
6. **Document the decision** — including rationale, residual risk, and approval — as part of your system's SRMP/SSP and accreditation record.

## Bottom Line

You cannot assume AWS Sydney is an approved default location for RESTRICTED data. Before proceeding, your agency needs to: complete a cloud risk assessment specific to offshore hosting, consult GCSB/NCSC as the national authority, ensure appropriate encryption and key management controls, and obtain formal risk acceptance from your Accreditation Authority as part of the system's certification and accreditation process. If timelines or risk appetite make this difficult, evaluate whether an NZ-based hosting option would meet your operational needs with substantially less compliance overhead.

*Note: Government cloud policy and panel arrangements are periodically updated. Confirm current requirements and any applicable AoG cloud agreements directly with the GCDO/DIA and GCSB/NCSC, and verify AWS's current certifications against NZ government requirements, as these details can change.*
