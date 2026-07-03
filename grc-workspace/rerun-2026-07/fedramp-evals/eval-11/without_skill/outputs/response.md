FedRAMP Authorization Process: Start to Finish
===============================================

FedRAMP (Federal Risk and Authorization Management Program) is the standardized
approach the US federal government uses to assess, authorize, and continuously
monitor cloud products and services. If you want to sell cloud software to
federal agencies, your service offering will almost certainly need to go
through FedRAMP authorization (unless it qualifies for a narrow exception).

Below is the end-to-end process, the two main authorization paths, and a
recommendation for a first-time authorization.

--------------------------------------------------------------------
1. THE FEDRAMP PROCESS, PHASE BY PHASE
--------------------------------------------------------------------

Phase 1 — Prepare / Readiness
- Determine your impact level (Low, Moderate, or High) based on FIPS 199 /
  NIST SP 800-60 categorization of the data your system will process, store,
  or transmit. Most commercial SaaS vendors targeting civilian agencies land
  at "Moderate," which covers roughly 80% of authorizations.
- Identify your authorization path (Agency ATO vs. JAB P-ATO — see below) and,
  if pursuing JAB, get on the JAB's prioritization radar via the FedRAMP PMO.
- Complete a Readiness Assessment (optional but strongly recommended, and
  required if you want to be listed as "FedRAMP Ready" on the marketplace).
  A FedRAMP-accredited Third Party Assessment Organization (3PAO) evaluates
  your environment and produces a Readiness Assessment Report (RAR).
- Build out your cloud environment to meet the applicable NIST SP 800-53
  control baseline (as tailored by FedRAMP) for your target impact level —
  roughly 125 controls at Low, 325 at Moderate, 421 at High.
- Stand up foundational artifacts: system boundary diagram, inventory,
  policies/procedures, and begin drafting the System Security Plan (SSP).

Phase 2 — Develop your authorization package (Documentation)
- System Security Plan (SSP): the core document describing your system
  boundary, architecture, data flows, and how each required control is
  implemented.
- Supporting policies and plans: Incident Response Plan, Configuration
  Management Plan, Contingency Plan, Rules of Behavior, IT Contingency Plan,
  and a Control Implementation Summary (CIS)/Customer Responsibility Matrix
  (CRM).
- Engage a 3PAO to independently assess the system.

Phase 3 — Assessment
- The 3PAO develops a Security Assessment Plan (SAP), which is reviewed and
  approved by the authorizing body (the sponsoring agency for Agency ATO, or
  the JAB for P-ATO).
- The 3PAO performs the assessment: control testing, vulnerability scanning
  (network, web application, database, container), penetration testing, and
  interviews.
- Results are documented in a Security Assessment Report (SAR), including any
  findings/weaknesses.
- You develop a Plan of Action and Milestones (POA&M) to track remediation of
  any open findings, with risk-based timelines (typically 30/90/180 days for
  high/moderate/low findings).

Phase 4 — Authorization
- Agency path: The sponsoring federal agency's Authorizing Official (AO)
  reviews the full package (SSP, SAR, POA&M, etc.) and makes a risk-based
  decision to grant an Authority to Operate (ATO) directly to the agency.
- JAB path: The Joint Authorization Board (composed of CIOs from DoD, DHS,
  and GSA) reviews the package and, if satisfied, issues a Provisional ATO
  (P-ATO) — "provisional" because it signals other agencies can rely on it,
  but each agency must still issue its own ATO before using the service.
- Once authorized, the package is submitted to the FedRAMP PMO for
  significant/final review, and the system is listed on the FedRAMP
  Marketplace as "Authorized."

Phase 5 — Continuous Monitoring (ConMon)
- Authorization is not a one-time event. You must maintain the authorization
  through ongoing continuous monitoring: monthly vulnerability scans, monthly
  POA&M updates, annual assessments by a 3PAO, annual penetration testing,
  and prompt reporting of significant changes or incidents.
- Failure to maintain ConMon can result in suspension or revocation of your
  authorization.

Typical timeline: 12–18 months for a first Moderate-impact authorization is
common, though it varies widely based on organizational readiness, system
complexity, and responsiveness during assessment.

--------------------------------------------------------------------
2. AGENCY ATO vs. JAB P-ATO
--------------------------------------------------------------------

Agency ATO
- Sponsor: A single federal agency that wants to use your product sponsors
  you and acts as the Authorizing Official.
- Process: You work directly with that agency's security team throughout
  documentation, assessment, and authorization.
- Outcome: The agency issues its own ATO. Other agencies can technically
  "leverage" this package via FedRAMP's reuse model, but each additional
  agency typically still performs its own review and issues a separate ATO
  before granting access (though the heavy lifting of the original
  assessment is reused, saving significant time/cost).
- Availability: Open to any CSP that can find a sponsoring agency — this is
  the more common and more accessible path, especially for companies without
  an existing federal customer relationship (note: as of the FedRAMP 20x /
  post-2023 "Rev5" prioritization changes, agency sponsorship is effectively
  required to enter the process at all).
- Pace: Generally faster to first authorization because scope and priorities
  are negotiated one-on-one with a single agency motivated to get you
  authorized (they want to use your product).

JAB P-ATO
- Sponsor: The Joint Authorization Board itself (DoD, DHS, GSA CIOs), via a
  competitive nomination/prioritization process — the JAB selects a very
  limited number of CSPs per year (historically single digits to low tens).
- Process: More rigorous and centralized; JAB reviewers set a high bar since
  the resulting P-ATO is meant to be broadly reusable across the government.
- Outcome: A "provisional" ATO intended as a strong reuse signal — agencies
  still must review and grant their own ATO, but the JAB's vetting carries
  significant weight and often accelerates agency-level adoption.
- Availability: Highly competitive and limited-capacity; you typically need
  strong evidence of multi-agency demand and executive sponsorship to even
  be considered.
- Pace: Often slower to obtain initially (competition for slots, more rigid
  process) but can pay off faster in downstream sales velocity once achieved,
  since many agencies view P-ATO as a stronger/more trusted stamp.

Key structural point: Neither path grants automatic government-wide access.
FedRAMP authorization (via either path) makes it dramatically easier and
faster for additional agencies to grant their own ATO through reuse, but
"portability" is a reuse facilitation model, not automatic blanket approval.

--------------------------------------------------------------------
3. WHICH PATH SHOULD YOU CONSIDER FOR A FIRST AUTHORIZATION?
--------------------------------------------------------------------

For a cloud software vendor pursuing its first FedRAMP authorization, the
Agency ATO path is almost always the right starting point, for these reasons:

1. Sponsorship is required either way. Under the current FedRAMP process,
   you cannot self-initiate — you need an agency sponsor to enter the
   program. If you don't already have a federal customer champion pushing
   for JAB prioritization, Agency ATO is the realistic entry point.
2. JAB slots are scarce and competitive. The JAB authorizes a small number
   of CSPs annually and typically prioritizes offerings with proven,
   broad, cross-agency demand — a profile that usually fits established
   vendors with existing federal traction, not first-time entrants.
3. Faster, more predictable path to your first customer. An agency that
   wants your product now has a direct incentive to move efficiently through
   documentation and assessment with you, since they get a usable system at
   the end. This tends to produce more realistic timelines and more
   collaborative reviews than the more bureaucratic JAB process.
4. You can "graduate" later. Many CSPs pursue an Agency ATO first, prove
   the model works, sign additional client agencies via reuse, and only
   later (if there's clear multi-agency government-wide demand) is JAB
   P-ATO worth pursuing — some never need it, since agency-to-agency reuse
   of a solid Agency ATO package is often sufficient for growth.
5. Lower cost and risk to start. Agency sponsorship lets you scope the
   engagement around one committed customer's needs rather than betting
   resources on winning a competitive JAB slot with no guaranteed adopter.

Practical next steps:
- Identify a federal agency (ideally one already expressing purchase intent
  or currently in your sales pipeline) willing to sponsor you.
- Engage a FedRAMP-accredited 3PAO early for a readiness assessment.
- Decide your target impact level (Moderate is the most common and broadly
  useful starting point unless your data/use case clearly requires Low or
  High).
- Consider whether FedRAMP's newer "FedRAMP 20x" pilot pathways or the
  "Low-Impact SaaS (LI-SaaS)" baseline apply if your offering is a
  lower-risk SaaS product — these can meaningfully reduce timeline and cost
  for qualifying systems.
- Budget realistically: first-time Moderate authorizations commonly run
  from several hundred thousand to over a million dollars in 3PAO fees,
  tooling, staff time, and remediation costs, on top of the 12–18 month
  timeline.

Bottom line: Start with Agency ATO, sponsored by a federal agency that
already wants your product. Treat JAB P-ATO as a longer-term goal to
pursue only once you have multiple agencies interested and a track record
that makes you a competitive candidate for one of the JAB's limited slots.
