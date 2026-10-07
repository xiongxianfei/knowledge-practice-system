---
id: "kps:mo:claim-evidence-model"
type: "model"
version: "9.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored model with attributed inputs"
confidence: "scope-dependent; see evaluation"
references: ["kps:r:cochrane", "kps:r:prov"]
uses_principles: ["kps:p:multiple-reports-can-share-one-evidence-base", "kps:p:provenance-does-not-establish-truth", "kps:p:evidence-applicability-depends-on-the-question"]
uses_concepts: []
perspectives: ["knowledge-representation", "evidence-reasoning"]
---

# Claim evidence inference model

## Key takeaway

Make the evidentiary role of a source inspectable at claim level.

## Summary

Source S reports an outcome in task A. Candidate claim C concerns task B. The missing edge is the application argument from A to B, not another citation to S. Mark it as an assumption until checked.

## Local explanatory basis

The number of documents repeating a result can exceed the number of independent observations supporting it. A trace showing where a claim came from does not by itself establish that the claim is correct. Evidence for one population, task, comparison or outcome does not automatically establish an effect for a materially different target.

## Purpose
Make the evidentiary role of a source inspectable at claim level.

## Representation
A claim has a statement, scope and epistemic status. A Reference has a publication identity, inspected extent and evidence-family note. An assessment connects a claim to a located passage as **support / challenge / context only / not established**. A synthesis combines assessments and exposes added premises. A design choice additionally declares the goal and trade-off.

```text
external work -> reference passage -> claim assessment
                                  -> synthesis + assumptions
                                  -> explanatory knowledge
                                  -> goal-dependent choice
```

## Assumptions
The source text is accurately represented. Independence is recorded as known, shared or unknown, not inferred from different domains alone.

## Implications
Two reference records can belong to one evidence family. A correction can change source assessment without deleting the original record. A source about a topic is not automatically support.

## Evidence and evaluation
[Cochrane Handbook for Systematic Reviews of Interventions, version 6.5](../references/cochrane-2024-handbook-v6-5.md#reports-and-underlying-studies) informs report/study separation; [Cochrane Handbook for Systematic Reviews of Interventions, version 6.5](../references/cochrane-2024-handbook-v6-5.md#indirectness-relative-to-the-target-question) informs directness. [PROV-Overview](../references/w3c-2013-prov-overview.md#provenance-describes-production-history) informs provenance representation. This schema is KPS’s adaptation, not an implementation of all those standards.

## Limits
The graph records judgments rather than computing truth. It does not implement a formal meta-analysis or universal source ranking.

## Local evidence summary


[Cochrane Handbook for Systematic Reviews of Interventions, version 6.5](../references/cochrane-2024-handbook-v6-5.md#reports-and-underlying-studies) contributes: Several reports can describe one underlying study; report count is therefore not study count.

[Cochrane Handbook for Systematic Reviews of Interventions, version 6.5](../references/cochrane-2024-handbook-v6-5.md#indirectness-relative-to-the-target-question) contributes: Evidence may be indirect when study populations, interventions, comparisons or outcomes differ from the target question.

[PROV-Overview](../references/w3c-2013-prov-overview.md#provenance-describes-production-history) contributes: PROV represents the origins of entities through activities and agents, enabling provenance to be exchanged.

Citation identifies support for the stated claim and scope. Any further causal or practical inference remains separately reviewable.

## Deeper knowledge

Canonical dependencies and Reference records provide additional derivation, source inspection and alternatives. They are not required to carry out the local explanation or procedure.

- **Principles:** [Multiple reports can share one evidence base](../principles/multiple-reports-can-share-one-evidence-base.md)
- **Principles:** [Provenance does not establish truth](../principles/provenance-does-not-establish-truth.md)
- **Principles:** [Evidence applicability depends on the question](../principles/evidence-applicability-depends-on-the-question.md)
- **References:** [Cochrane Handbook for Systematic Reviews of Interventions, version 6.5](../references/cochrane-2024-handbook-v6-5.md)
- **References:** [PROV-Overview](../references/w3c-2013-prov-overview.md)
