# Eval 99: Breach Notification — With Skill Response

## Prompt
We experienced a data breach affecting 50,000 Brazilian customers. Names, email addresses, and CPF numbers were exposed. What are our LGPD breach notification obligations, to whom, and within what timeframes?

---

## Answer

This breach triggers mandatory notification obligations under LGPD Art. 48 and ANPD Resolution CD/ANPD No. 15/2024. Given the nature of the data exposed — particularly CPF numbers — this is a **high-risk incident** that almost certainly requires notification to both the ANPD and affected data subjects. Here is the complete framework.

---

### 1. Obligation to Notify ANPD — Preliminary Notification Within 3 Working Days

**Legal basis:** Art. 48, §1º LGPD; ANPD Resolution CD/ANPD No. 15/2024

Under Resolution CD/ANPD No. 15/2024, controllers must submit a **preliminary incident notification** to the ANPD within **3 working days** of becoming aware of a security incident that may cause relevant risk or harm to data subjects.

| Step | Deadline | Action |
|------|----------|--------|
| **Detection / awareness** | Day 0 | Internal breach identified and escalated |
| **Preliminary ANPD notification** | Within **3 working days** of awareness | Submit preliminary notification via ANPD's online portal (peticionamento.anpd.gov.br) |
| **Full incident report to ANPD** | Within **20 working days** of confirmation | Submit comprehensive incident report |

**Important:** The 3-working-day clock starts from when the controller **becomes aware** of the incident — not from when the breach actually occurred. Prompt internal escalation processes are therefore critical to avoid clock issues.

---

### 2. Obligation to Notify Affected Data Subjects

**Legal basis:** Art. 48, §1º LGPD

Where the security incident presents a **relevant risk of harm** to data subjects, the controller must also notify the **affected individuals** in addition to the ANPD. The notification to data subjects must occur without undue delay once the risk assessment confirms high risk.

**This breach almost certainly triggers data subject notification** — see Section 5 on CPF below.

Notification to data subjects must be:
- **Communicated in a clear and adequate manner** (Art. 48, §1º)
- Provided through your usual communication channel with affected customers (e.g., email)
- Sufficient to allow data subjects to take protective measures (e.g., credit monitoring, CPF blocking with the Receita Federal)

---

### 3. Required Content of the ANPD Preliminary Notification

ANPD Resolution CD/ANPD No. 15/2024 specifies the information that must be included in the preliminary notification. Your notification must cover:

| Required Element | Detail |
|-----------------|--------|
| **Nature of the incident** | Type of incident (e.g., unauthorised external access, ransomware, accidental exposure); how it occurred |
| **Nature of the affected data** | Categories of personal data exposed — in this case: names, email addresses, CPF numbers (tax identifiers) |
| **Number of data subjects affected** | Confirmed or estimated count — here: approximately 50,000 |
| **Categories of data subjects affected** | Description of who was affected (e.g., Brazilian customers of [company]) |
| **Security and technical measures in place** | Description of security controls that were in place at the time of the breach |
| **Risk assessment** | Assessment of the likely consequences and severity of risk to data subjects |
| **Measures taken or planned** | Containment measures already implemented; remediation steps planned |
| **Contact for ANPD follow-up** | DPO/Encarregado contact name and details |

---

### 4. Full Incident Report — 20 Working Days

In addition to the preliminary notification, LGPD and Resolution CD/ANPD No. 15/2024 require a **comprehensive final incident report** submitted to the ANPD within **20 working days** of breach confirmation. The full report typically includes:

- Complete forensic timeline of the incident
- Full scope of data affected (confirmed, not estimated)
- Root cause analysis
- Complete list of remediation measures implemented
- Outcome of data subject notifications (how many notified, through what channels)
- Ongoing monitoring and preventive measures adopted

---

### 5. CPF Numbers Heighten Risk Level and Trigger Data Subject Notification

The exposure of **CPF numbers** (Cadastro de Pessoas Físicas) is a significant aggravating factor in this breach:

- **CPF is a national identifier** uniquely linked to an individual's tax history, financial records, and identity — it is used across banking, credit, and government services in Brazil
- Exposure of CPF enables identity theft, fraudulent credit applications, and account takeovers in Brazilian financial institutions
- The ANPD evaluates risk under a harm-based framework: CPF exposure + name + email creates a high-risk combination for **identity fraud and financial harm**
- **ANPD Resolution CD/ANPD No. 15/2024** makes clear that high-risk incidents — those likely to cause significant harm — trigger mandatory data subject notification

**The 50,000 individuals affected should be notified** of the breach, what data was exposed, and what steps they can take to protect themselves, including:
- Monitoring their CPF status with the Receita Federal
- Requesting a CPF blocking (bloqueio preventivo) if fraud is suspected
- Monitoring credit bureau reports (Serasa, SPC, Boa Vista)
- Being alert to phishing attempts using their exposed name and email

---

### 6. Immediate Action Checklist

```
[ ] Day 0: Activate incident response team; contain breach; preserve evidence
[ ] Day 0: Assess scope — confirm 50,000 affected, data types exposed (name, email, CPF)
[ ] Day 0-1: Engage DPO (Encarregado); notify senior management/legal
[ ] Within 3 working days: Submit PRELIMINARY notification to ANPD via portal
[ ] Without undue delay: Notify affected data subjects via email
[ ] Within 20 working days: Submit FULL INCIDENT REPORT to ANPD
[ ] Ongoing: Document all steps for accountability records (Art. 50)
[ ] Ongoing: Implement remediation; conduct post-incident review
```

---

### 7. Penalties for Failure to Notify

Failure to notify ANPD within the required timeframes, or failure to notify data subjects when required, constitutes a violation of Art. 48 and can result in:

- **Fines up to 2% of Brazilian revenue** (prior fiscal year, group basis), with a **cap of R$50 million per violation** (Art. 52)
- The late/missing notification itself is a separate violation from the underlying security failure — each may be assessed independently
- ANPD can also order **blocking of processing activities** or require **public disclosure** of the infraction

---

### Summary

| Notification | Recipient | Deadline |
|-------------|-----------|----------|
| Preliminary incident notification | **ANPD** | **3 working days** from awareness (per Resolution CD/ANPD No. 15/2024) |
| Data subject notification | **50,000 affected customers** | Without undue delay; coordinate with ANPD preliminary notification |
| Full incident report | **ANPD** | **20 working days** from confirmation |

The CPF exposure substantially elevates risk and makes data subject notification mandatory. Begin containment, assemble your DPO, and file the preliminary ANPD notification within 3 working days — this is a hard deadline with no grace period.
