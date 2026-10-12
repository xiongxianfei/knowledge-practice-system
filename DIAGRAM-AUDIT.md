---
package_version: "10.2.0"
language: "KPS 9.x"
reviewed: "2026-10-12"
---

# Diagram necessity audit

## Key takeaway

Audit every object for an explanatory gap without requiring every object to contain an image.

## Summary

The audit retains six source and image pairs, adds twelve explanations and reuses two diagrams in related documents. Nineteen of twenty Core objects embed a relevant explanation. Testing Effect stays text-only for the reason below. The small metadata neighborhood remains secondary. Commit every editable D2 source beside its generated SVG.

## Per object decisions

| Knowledge object | Decision | Explanatory purpose or reason for no diagram |
|---|---|---|
| [Evidence Indirectness](concepts/evidence-indirectness.md) | reuse | Embed the relevant explanation locally without duplicating its editable source. |
| [Provenance](concepts/provenance.md) | reuse | Embed the relevant explanation locally without duplicating its editable source. |
| [SKOS Concept](concepts/skos-concept.md) | add | Separate two concept identities from their identical lexical label. |
| [Study and Report](concepts/study-and-report.md) | retain | Show the many-to-many distinction between an investigation and reports. |
| [Uniform Resource Identifier](concepts/uniform-resource-identifier.md) | add | Distinguish resolving a reference from retrieving a resource and interpreting its fragment. |
| [Indirectness Limits Applicability](principles/indirectness-limits-applicability.md) | add | Expose the unestablished bridge between a measured surrogate and the target outcome. |
| [Spacing Effect](principles/spacing-effect.md) | add | Keep total spacing distinct from the pattern of intervals without inventing effect sizes. |
| [Study Level Evidence Independence](principles/study-level-evidence-independence.md) | retain | Explain why repeating the same study outcome does not add independent trials. |
| [Testing Effect](principles/testing-effect.md) | text-only | The scoped finding and contrasting evidence are concise. A generic causal arrow would imply an established mechanism; an effect-size chart requires a separate data extraction and comparison. No decorative chart is added. |
| [PROV Data Model](models/prov-data-model.md) | retain | Keep entity, activity and agent relations and their directions distinct. |
| [SKOS Data Model](models/skos-data-model.md) | add | Distinguish literal labels, broader and related relations, and cross-scheme mappings. |
| [Cognitive Walkthrough](methods/cognitive-walkthrough.md) | add | Make all four learnability questions visible without presenting predictions as observed behavior. |
| [Plan Do Check Act](methods/pdca.md) | retain | Show that checking a trial informs adoption or another planning cycle. |
| [PICO Question Formulation](methods/pico-question-formulation.md) | add | Make the intervention and comparator distinction and common outcome explicit before searching. |
| [Retrieval Practice](methods/retrieval-practice.md) | add | Separate unaided recall, subsequent checking, and later assessment. |
| [Study Data Extraction](methods/study-data-extraction.md) | add | Separate independent extraction from comparison and documented disagreement resolution. |
| [Build an independent domain knowledge package](practices/build-domain-knowledge.md) | add | Separate content-use review from structural checks and the owner-authorized publication choice. |
| [Improve KPS without mistaking structure for usefulness](practices/improve-kps.md) | add | Distinguish local content repairs from governing-rule changes before a pilot and compatibility check. |
| [Review an application and retain justified learning](practices/review-and-learn.md) | add | Separate execution failures and inconclusive attribution from a supported scoped update. |
| [Use KPS for one real task](practices/use-kps.md) | retain | Separate structural checks, real viewer checks and untested behavior. |

## Reading and review

Each diagram has alternative text, a reading guide, limitations and a source link beside its owning explanation. Arrows mean their labels or the expressly identified local procedure, not proof. The URI and spacing examples are synthetic. Shared visuals have one source each. Practice visuals reveal failure paths and decisions rather than repeating every stage.

These decisions are an author assessment of current content. Reader evidence can justify changes later; this is not proof that every future visual need is satisfied. See [SOURCE-REVIEW.md](SOURCE-REVIEW.md) for inspected and unavailable sources.

## Maintenance

[diagram-audit.json](diagram-audit.json) records every current Core object. Its tests check coverage, source reuse and image/source links, not explanatory value. [DIAGRAMS.md](DIAGRAMS.md) gives the pinned rendering commands. No independent reader trial or accessibility certification is claimed.
