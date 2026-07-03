# NIS2 Applicability — German Electricity DSO (200 employees, €50M turnover)

## Short answer
Yes, you fall under NIS2. Based on the figures given, your default classification is an **Important Entity (IE)**, not an Essential Entity — but this depends on a German designation check you need to confirm (see Step 3).

## Step-by-step analysis

### Step 1 — Sector scope (Annex I)
Electricity distribution network operators (DSOs) fall within the **energy** sector of **Annex I** (high-criticality sectors), alongside electricity producers, TSOs, district heating, oil, gas, and hydrogen. You are squarely in scope on sector grounds.

### Step 2 — Size threshold (Art. 2(1))
NIS2 applies from **medium-sized** entities upward: ≥50 employees, OR annual turnover and balance sheet total both above €10M.

- Your company: 200 employees, €50M turnover → well above the medium-sized threshold.
- **Conclusion: in scope on size grounds.**

### Step 3 — Essential vs. Important Entity (Art. 3)
This is where precision matters, because Annex I membership does not automatically mean "Essential."

- **Essential Entity (EE)** requires exceeding the *large*-enterprise ceiling: ≥250 employees, **or** turnover >€50M **and** balance sheet >€43M (in addition to being Annex I).
- **Important Entity (IE)** = everything else in scope — i.e., medium-sized Annex I entities that don't clear the large-enterprise ceiling.

Your numbers: 200 employees (below 250) and €50M turnover (not *strictly above* €50M, and balance sheet total not stated as exceeding €43M). You do **not** clear the large-enterprise ceiling on the facts given.

**Default classification: Important Entity (IE).**

You would only become an Essential Entity if:
- Germany designates you as essential via the national transposition act (the BSIG amendment implementing NIS2 sets German-specific KRITIS-style thresholds and designation criteria for energy operators — electricity DSOs above certain supply thresholds are commonly captured this way), or
- You are separately designated critical under the CER Directive (EU) 2022/2557, which automatically makes you an Essential Entity under NIS2 Art. 3(1)(f).

**Action item:** confirm with the German BSI (Bundesamt für Sicherheit in der Informationstechnik) or your legal counsel whether your specific network qualifies for KRITIS/BSIG designation as essential — DSOs are a common category for national essential-entity designation regardless of the general size test. Do not rely solely on the default IE classification without this check.

### Step 4 — Jurisdiction and registration
- **Jurisdiction (Art. 26):** Germany, as your place of establishment.
- **Registration (Art. 27):** You must register with the German competent authority (BSI) per the national transposition — providing entity details, sector, and contact information. Registration is mandatory whether you land as EE or IE.

## Key obligations (apply identically to EE and IE)

Classification changes the *supervisory regime and penalty ceiling*, not the substantive obligations — Arts. 20, 21, and 23 apply the same way to both tiers.

### 1. Governance (Art. 20)
- Management body must **approve** your Art. 21 risk-management measures and **oversee** implementation.
- Management body must undergo, and offer staff, regular cybersecurity **training**.
- Members of the management body can face **personal liability** under German law for infringements.
- Evidence to build: board approval minutes, training completion records, a standing board agenda item for cyber oversight.

### 2. Risk management measures (Art. 21(2)(a)–(j)) — 10 measures
1. Risk analysis & information security policies
2. Incident handling (detection, response, recovery)
3. Business continuity — backup, disaster recovery, crisis management
4. **Supply chain security** (informed by EU coordinated risk assessments under Art. 22)
5. Security in acquisition, development, and maintenance, incl. vulnerability handling/disclosure
6. Policies to assess effectiveness of the measures
7. Basic cyber hygiene and staff training
8. Cryptography and, where appropriate, encryption policies
9. HR security, access control, asset management
10. Multi-factor/continuous authentication, secured voice/video/text comms, secured emergency communications

Measures must be **proportionate** to your risk exposure, size, and the severity of potential incidents (Art. 21(1)). As a DSO, your operational technology (SCADA/grid control) exposure typically pushes you toward the more rigorous end of proportionality even as an IE, given the potential societal impact of disruption.

### 3. Incident reporting (Art. 23)
For a "significant incident" (severe operational disruption/financial loss, or considerable damage to others), you must report to the German CSIRT/BSI on this timeline from the moment of awareness:
- **≤24 hours:** early warning
- **≤72 hours:** incident notification with initial severity/impact assessment
- **On request:** intermediate status reports
- **≤1 month** after the 72h notification: final report

### 4. Supervision and penalties (as an Important Entity)
- **Supervision:** ex-post only — BSI acts on evidence or indication of non-compliance (audits, information requests), not proactive inspection.
- **Maximum administrative fine:** at least **€7,000,000 or 1.4% of total worldwide annual turnover**, whichever is higher (Art. 34). Germany's BSIG may set this ceiling higher.
- **Management liability:** personal liability remains, even without the EE-level suspension powers.

If Germany designates you an Essential Entity instead, supervision becomes **ex-ante** (proactive on-site inspections, regular/targeted audits) and the fine ceiling rises to **at least €10,000,000 or 2% of worldwide turnover**, whichever is higher.

## Recommended next steps
1. Confirm BSIG/KRITIS designation status with BSI to lock in EE vs. IE.
2. Register with BSI under Art. 27 if not already done.
3. Run a gap assessment against the 10 Art. 21(2) measures, prioritizing OT/grid-control security given the energy-sector risk profile.
4. Stand up the 24h/72h/1-month incident reporting workflow with BSI as the named recipient.
5. Document Art. 20 board approval and training now — this is commonly the weakest evidence area at first review.

*This is general compliance information, not legal advice. Confirm your German transposition status and KRITIS designation with BSI or qualified counsel.*
