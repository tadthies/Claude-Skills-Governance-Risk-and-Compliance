Short answer: Almost certainly not directly subject to NIS2 as a regulated "essential" or "important" entity based on the facts given — but you need to check one thing before ruling it out completely, and you may still face NIS2 obligations indirectly through your customer's contract.

## 1. Are you directly in scope?

NIS2 (Directive (EU) 2022/2555) uses a "size-cap" rule combined with sector classification.

**Step 1 — Sector test.** NIS2 only applies to entities operating in the sectors listed in Annex I (essential entities, e.g., energy, transport, banking, health, digital infrastructure, public administration) or Annex II (important entities, e.g., manufacturing, food, chemicals, postal services, and — most relevant to you — "digital providers" such as providers of online marketplaces, online search engines, and social networking platforms, plus a broader "digital service providers" / "managed service providers" / "managed security service providers" catchall, and "ICT service management (B2B)" providers).

HR software (a SaaS/cloud platform for HR management) does not fall squarely into an Annex I or Annex II sector as a matter of course. It's not energy, health, banking, digital infrastructure (DNS, cloud computing, data centers, CDNs, trust services, public electronic communications), nor is it inherently a "managed service provider" (MSP) or "managed security service provider" (MSSP) under the Annex II definitions — unless you are managing your customers' IT/network infrastructure or security on their behalf, which a typical HR SaaS application is not.

**Step 2 — Size cap test.** Even if you did fall into a covered sector/subsector, NIS2 generally only applies to:
- Medium and large entities: ≥50 employees **OR** ≥€10M annual turnover/balance sheet total (this is the "medium enterprise" threshold from the EU SME definition, Annex to Recommendation 2003/361/EC).

At 75 employees and €15M revenue, you would exceed the medium-enterprise threshold (so the size cap would not exempt you *if* you were in a covered sector). Some categories (e.g., providers of public electronic communications networks, trust service providers, DNS providers, certain digital infrastructure) are in scope *regardless of size*, but HR SaaS is not one of these size-agnostic categories.

**Conclusion on direct applicability:** Based on what you've described — B2B HR software, not IT/security management of client networks, not critical digital infrastructure — you are very likely **out of scope for direct NIS2 designation**. You should still confirm this by:
- Checking how your country's NIS2 transposition law defines "digital service" and "managed service provider" — transposition varies by EU member state, and some states have gone further than the minimum directive text.
- Confirming you don't provide any adjacent services that could reclassify you (e.g., if you also host/manage IT infrastructure for clients, provide identity/access management as a managed service, or operate as a cloud computing service provider in a way that meets the Annex I "digital infrastructure — cloud computing services" definition).
- If you operate in Germany, note the transposition (NIS2UmsuCG) has specific interpretations of "managed service provider" that are broader than some other states.

## 2. Why the customer is asking anyway — indirect exposure

Even if you're not directly regulated, your customer likely *is* an essential or important entity (or supplier to one), and NIS2 Article 21(2)(d) explicitly requires in-scope entities to address **supply chain security**, including "security-related aspects concerning the relationships between each entity and its direct suppliers or service providers." That means your customer's own NIS2 compliance obligations flow down to you contractually — they will likely ask you to:
- Complete a security questionnaire or attestation
- Sign contractual security clauses (incident notification timelines, right to audit, minimum security controls)
- Demonstrate baseline technical and organizational security measures similar in spirit to Article 21

So even without being directly designated, you should expect **contractual NIS2-driven requirements** from customers who are themselves in scope. This is common practice and will likely keep recurring with other customers too.

## 3. What Article 21 requires (in case you're in scope, or want to align voluntarily to win/keep customers)

Article 21 requires in-scope entities to take "appropriate and proportionate technical, operational and organisational measures" to manage cybersecurity risks, following an all-hazards approach, and covers at minimum:

1. **Risk analysis and information system security policies**
2. **Incident handling** — prevention, detection, and response processes
3. **Business continuity and crisis management** — backup management, disaster recovery, crisis management procedures
4. **Supply chain security** — including security aspects of relationships with direct suppliers/service providers
5. **Security in network and information systems acquisition, development, and maintenance** — including vulnerability handling and disclosure
6. **Policies and procedures to assess the effectiveness of cybersecurity risk-management measures**
7. **Basic cyber hygiene practices and cybersecurity training**
8. **Policies and procedures on the use of cryptography and, where appropriate, encryption**
9. **Human resources security, access control policies, and asset management**
10. **Use of multi-factor authentication (MFA) or continuous authentication, secured voice/video/text communications, and secured emergency communication systems where appropriate**

Governance is also explicitly addressed in **Article 20**: management bodies must approve the cybersecurity risk-management measures, oversee implementation, and can be held personally liable for non-compliance; management must also undergo cybersecurity training.

**Incident reporting (Article 23)** is a separate but related obligation for in-scope entities: significant incidents must be reported to the national CSIRT/competent authority — an early warning within 24 hours, an incident notification within 72 hours, and a final report within one month.

## Recommended next steps

1. **Confirm scope definitively** — get a short legal opinion from counsel (or a NIS2 specialist) in the member state(s) where you're established, since transposition details vary and "managed service provider" definitions can be broader than expected.
2. **Ask the customer for specifics** — find out whether they're asking because (a) they believe you're directly in scope, or (b) they need you to meet supply-chain security requirements as their vendor under their own Article 21(2)(d) obligations. This will clarify whether you need formal NIS2 registration/compliance or just contractual security assurances.
3. **Regardless of direct applicability, consider voluntary alignment** — implementing Article 21-style controls (risk management policy, incident response plan, MFA, encryption, access control, vendor risk management, business continuity/backup plans, security training) is good practice and will likely become a standard customer requirement across your B2B SaaS customer base as more of your customers become NIS2-regulated.
4. **If you have existing SOC 2 or ISO 27001 programs**, most Article 21 measures map closely to those control sets — a gap analysis against Article 21 using your existing controls as a baseline is usually efficient rather than starting from scratch.
5. **Watch for national registration requirements** — some member states require in-scope (and in some cases even out-of-scope but adjacent) entities to register with the national competent authority; check your specific jurisdiction's rules and any de minimis reporting requirements.

This is general compliance guidance, not legal advice — given real regulatory and financial exposure (management liability under Article 20, potential fines), confirm your specific scope determination with qualified local counsel.
