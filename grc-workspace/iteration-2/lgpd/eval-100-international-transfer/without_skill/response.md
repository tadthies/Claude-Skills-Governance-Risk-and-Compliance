# Eval 100: International Transfer — Without Skill Response (Baseline)

## Prompt
We need to transfer personal data of Brazilian customers to our parent company's servers in the EU (Germany). What transfer mechanism do we need under LGPD? Also, we want to also transfer some data to our US-based analytics vendor. What do we need for that?

---

## Answer

Under LGPD, international data transfers are governed by Articles 33–36. Both of your proposed transfers require a valid transfer mechanism, but the specific requirements differ based on the destination.

### Transfer to EU (Germany)

Brazil's ANPD has been working on recognizing certain countries as providing adequate data protection. The EU, with its GDPR framework, is generally considered to have strong data protection standards. As of my knowledge, Brazil and the EU have been working toward mutual recognition.

If the ANPD has issued a formal adequacy decision for the EU, then transfers to Germany would be straightforward — you could rely on the adequacy determination without needing additional contractual mechanisms.

If a formal adequacy decision has not yet been issued, you would need one of the alternative mechanisms:
- **Standard contractual clauses** that guarantee LGPD-equivalent protection
- **Binding corporate rules (BCRs)** for intragroup transfers
- **Specific consent** from data subjects acknowledging the international transfer

For intragroup transfers to a parent company, standard contractual clauses or BCRs are the most practical options.

### Transfer to US Analytics Vendor

The United States does not have a comprehensive data protection law comparable to LGPD or GDPR, and the ANPD has not issued a general adequacy finding for the US. Therefore, for transfers to a US-based vendor, you will need:

- **Standard contractual clauses** — a contract with the US analytics vendor that includes data protection obligations equivalent to LGPD requirements
- These clauses should cover: purpose limitation, security measures, data subject rights support, breach notification, sub-processor controls, and audit rights
- Or alternatively, **specific consent** from each data subject for the international transfer (generally impractical for routine business operations)

### Key Contractual Protections for US Vendor DPA

Your Data Processing Agreement with the US analytics vendor should include:
- Processing only on controller instructions
- Appropriate security measures
- Assistance with data subject rights requests
- Breach notification obligations
- Return or deletion of data on contract termination
- Restrictions on sub-processors

### Recommendation

1. Verify whether the ANPD has issued a formal adequacy decision for the EU — if so, document this as your transfer mechanism for Germany
2. Execute a DPA with appropriate contractual clauses with your US analytics vendor before transferring any data
3. Update your Records of Processing Activities (RoPA) to document the transfer mechanisms used
4. Update your privacy notice to disclose international transfers and the mechanisms used
