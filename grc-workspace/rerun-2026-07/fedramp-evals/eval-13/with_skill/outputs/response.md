# FedRAMP 20x: What It Is and How It Changes Authorization

## Executive Summary

FedRAMP 20x is the FedRAMP PMO's modernized authorization pathway, and under the current CR26 (FedRAMP Consolidated Rules for 2026) framework, **it is now the primary and preferred authorization pathway** — not a pilot program running alongside the traditional process. It replaces the old document-heavy, point-in-time authorization model with continuous, API-driven, automated authorization. For nearly every CSP starting a new authorization effort today, the recommendation is to **pursue FedRAMP 20x**, not the traditional (legacy) path. Traditional SSP/SAP/SAR-based authorization still exists for complex systems and legacy transitions during the CR26 transition window, but it is no longer the default route.

This is reinforced by a hard deadline: **FedRAMP Ready retires on July 28, 2026** — in about 3.5 weeks from today. Any CSP currently pursuing FedRAMP Ready needs to pivot immediately.

---

## What Is FedRAMP 20x?

FedRAMP 20x is a restructured authorization model built around three core shifts:

| Old Model (Traditional FedRAMP) | FedRAMP 20x |
|---|---|
| Point-in-time authorization based on a static document package | **Continuous authorization** — ongoing validation rather than a one-time snapshot |
| Manual submission of SSP, SAP, SAR as large narrative documents | **Modular, API-driven submissions** — structured data submitted incrementally |
| Manual evidence collection and review | **Automated evidence collection** — tooling-driven, reducing 3PAO/PMO manual review burden |
| FIPS 199-based baseline labels: Low / Moderate / High / LI-SaaS | **CR26 Certification Classes A–D** (NTC-0004): A = pilot/transitional entry (e.g., via SOC 2 Type II through Program Certification), B = LI-SaaS/Low, C = Moderate, D = High |
| JAB P-ATO or Agency ATO | JAB P-ATO is **fully suspended**; **FedRAMP PMO is the sole authorization body** |

Key mechanics to know:

- **Certification Class A** is new and has no legacy equivalent — it's a lighter-weight entry path that lets a CSP enter the federal marketplace via an external framework (initially SOC 2 Type II) through Program Certification, with a **2-year window** to progress to a full Class B/C/D certification.
- **OSCAL is mandatory by September 30, 2026** (per RFC-0024) — all CSPs must be able to submit machine-readable, structured authorization packages. This is foundational to how 20x's automation works.
- **Security Inbox requirement** (effective January 5, 2026): authorized CSPs must maintain a barrier-free channel for urgent vulnerability directives — part of the faster, more continuous posture 20x assumes.
- Traditional SSP/SAP/SAR/POA&M templates still exist and remain valid for CSPs on legacy/Agency Authorization paths, particularly for complex systems where 20x's automated model doesn't yet fit well.

---

## How This Changes the Authorization Process

1. **From static to continuous.** Authorization is no longer a single "point-in-time" ATO event followed by periodic ConMon check-ins on a mostly-frozen package. It shifts toward ongoing, automated validation.
2. **From document narrative to structured/API data.** Instead of writing hundreds of pages of prose control-by-control, CSPs increasingly submit structured, machine-readable evidence (OSCAL-formatted) that can be validated programmatically.
3. **From FIPS 199 labels to Certification Classes.** Systems are now classified A–D rather than Low/Moderate/High/LI-SaaS. The requirements underlying each class are unchanged from the corresponding legacy baseline (B↔Low, C↔Moderate, D↔High) — only the label and, for Class A, the on-ramp mechanism are new.
4. **From JAB to PMO-only.** There is no more Joint Authorization Board P-ATO route; the FedRAMP PMO is the sole authorizing body, which simplifies (but also centralizes) the approval chain.
5. **Lower barrier to entry via Class A.** A CSP with an existing SOC 2 Type II can potentially enter the federal market faster through Program Certification, then mature into a full Class B/C/D authorization over a 2-year runway — this didn't exist under the traditional model.

---

## Should You Plan for FedRAMP 20x or Traditional FedRAMP?

**Recommendation: Plan for FedRAMP 20x**, for the large majority of CSPs. Reasons:

- It is explicitly the FedRAMP PMO's primary and preferred pathway going forward.
- FedRAMP Ready — the on-ramp many CSPs used to prepare for traditional authorization — **retires July 28, 2026**, just weeks from now. CSPs still in that pipeline need to redirect now.
- The OSCAL mandate (Sept 30, 2026) means even CSPs on legacy paths will need to invest in the same automated, machine-readable tooling that 20x is built around — so there's little long-term advantage to avoiding it.
- If you already hold, or can obtain, a SOC 2 Type II, **Class A** may offer a materially faster on-ramp to a federal ATO than starting a traditional package from scratch.

**When traditional/legacy Agency Authorization may still make sense (for now):**
- Highly complex systems where 20x's automated/modular submission model isn't yet mature enough to represent the system accurately.
- CSPs already deep into a traditional SSP/SAP/SAR package with a 3PAO engaged — finishing under the existing framework may be more efficient than re-scoping mid-stream, especially since old and new labels are linked during the CR26 transition period.
- Systems clearly targeting Class D (High) where the full rigor of a traditional 3PAO assessment is expected regardless of submission format.

### Priority Action List
1. **Confirm your current path.** If you're pursuing FedRAMP Ready today, pivot immediately — it retires July 28, 2026.
2. **Determine your target Certification Class** (A, B, C, or D) based on the sensitivity of federal data in scope.
3. **Assess Class A eligibility** — do you have (or can you obtain) a SOC 2 Type II report to use as an on-ramp?
4. **Start OSCAL readiness now** — evaluate OSCAL-capable GRC tooling regardless of which path you choose; the September 30, 2026 mandate applies broadly.
5. **Stand up a Security Inbox** if you don't already have one (required since January 5, 2026 for authorized CSPs).
6. **If mid-package on a traditional path**, consult with your 3PAO and the FedRAMP PMO on whether to continue as-is or transition to 20x — don't switch reflexively without evaluating sunk progress.
7. **Run a readiness/gap assessment** against the standard control families regardless of path — the underlying NIST SP 800-53 Rev 5 control requirements (Low/Mod/High ↔ Class B/C/D) don't change; only the submission and authorization mechanics do.

---

*Note: FedRAMP 20x, CR26, and the Certification Class structure are an active, evolving area of FedRAMP policy. Always verify current guidance at fedramp.gov before finalizing a strategy, and use official FedRAMP PMO templates for any authorization package content.*
