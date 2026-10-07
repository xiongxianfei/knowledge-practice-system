---
id: "kps:p:provenance-does-not-establish-truth"
type: "principle"
version: "9.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
level: "domain"
basis_kind: "reasoned synthesis"
confidence: "qualified; see evidence and limits"
references: ["kps:r:prov", "kps:r:cochrane"]
based_on: []
perspectives: ["knowledge-representation", "evidence-reasoning"]
---

# Provenance does not establish truth

## Key takeaway

A trace showing where a claim came from does not by itself establish that the claim is correct.

## Summary

The same complete provenance structure can describe an accurate observation, a mistaken inference or an invented report. Source lineage and truth are therefore different properties.

## Worked use and boundary

Knowing who authored a claim and which version was read helps an audit. The source could still contain an error or concern the wrong population. Provenance is an input to appraisal, not the appraisal result.

## Statement
A trace showing where a claim came from does not by itself establish that the claim is correct.

## Explanation
The same complete provenance structure can describe an accurate observation, a mistaken inference or an invented report. Source lineage and truth are therefore different properties.

## Evidence and source synthesis
[PROV-Overview](../references/w3c-2013-prov-overview.md#provenance-describes-production-history) defines a provenance approach. [Cochrane Handbook for Systematic Reviews of Interventions, version 6.5](../references/cochrane-2024-handbook-v6-5.md#indirectness-relative-to-the-target-question) illustrates why even available study evidence can be indirect. These are distinct contributions, not two experiments proving the same effect.

## Derivation and applications
References identify origin; synthesis evaluates support; a knowledge object states the inference. A link remains useful even when it records a challenge rather than support.

## Scope
Claims drawn from documents, observations, generated text or other knowledge objects.

## Limits and alternatives
Provenance can be necessary for judging reliability, and its absence can be important. The claim is not that provenance has no value.

## Qualification and challenge
For a narrowly defined claim about what a particular author wrote, the original passage may itself be the direct evidence; this does not establish the truth of everything asserted in that passage.

## Local evidence summary


[PROV-Overview](../references/w3c-2013-prov-overview.md#provenance-describes-production-history) contributes: PROV represents the origins of entities through activities and agents, enabling provenance to be exchanged.

[Cochrane Handbook for Systematic Reviews of Interventions, version 6.5](../references/cochrane-2024-handbook-v6-5.md#indirectness-relative-to-the-target-question) contributes: Evidence may be indirect when study populations, interventions, comparisons or outcomes differ from the target question.

Citation identifies support for the stated claim and scope. Any further causal or practical inference remains separately reviewable.

## Deeper knowledge

Canonical dependencies and Reference records provide additional derivation, source inspection and alternatives. They are not required to carry out the local explanation or procedure.

- **References:** [PROV-Overview](../references/w3c-2013-prov-overview.md)
- **References:** [Cochrane Handbook for Systematic Reviews of Interventions, version 6.5](../references/cochrane-2024-handbook-v6-5.md)
