---
id: "kps:p:explicit-reasoning-exposes-assumptions"
type: "principle"
version: "9.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
level: "domain"
basis_kind: "reasoned synthesis"
confidence: "qualified; see evidence and limits"
references: ["kps:r:prov"]
based_on: []
perspectives: ["knowledge-representation", "evidence-reasoning"]
---

# Explicit reasoning exposes assumptions

## Key takeaway

Writing the premises and inference connecting a choice makes those stated assumptions available for inspection.

## Summary

An unexplained action leaves its assumed goal and causal expectations unavailable in the document. Recording “given A and B, try C to obtain D” separates four claims that can be checked independently.

## Worked use and boundary

A proposed link checker assumes the files exist and that a working link helps the task. Writing these assumptions makes missing content distinguishable from a path error. It does not make the assumptions true.

## Statement
Writing the premises and inference connecting a choice makes those stated assumptions available for inspection.

## Explanation
An unexplained action leaves its assumed goal and causal expectations unavailable in the document. Recording “given A and B, try C to obtain D” separates four claims that can be checked independently.

## Evidence and source synthesis
This is a representational argument. [PROV-Overview](../references/w3c-2013-prov-overview.md#provenance-describes-production-history) supports recording origins, but does not establish that longer explanations improve decisions. No empirical KPS effectiveness result is asserted.

## Derivation and applications
Method rationales, choice logs and counterexample checks are alternative applications. A short rationale can be sufficient; explanation length is not a quality score.

## Scope
Consequential methods, inferences and orchestration decisions.

## Limits and alternatives
An explicit rationale can be false, incomplete or post-hoc. Independent evidence is still required for empirical premises.

## Qualification and challenge
If the written chain obscures rather than identifies its actual premises, it does not exhibit the claimed inspection benefit.

## Local evidence summary


[PROV-Overview](../references/w3c-2013-prov-overview.md#provenance-describes-production-history) contributes: PROV represents the origins of entities through activities and agents, enabling provenance to be exchanged.

Citation identifies support for the stated claim and scope. Any further causal or practical inference remains separately reviewable.

## Deeper knowledge

Canonical dependencies and Reference records provide additional derivation, source inspection and alternatives. They are not required to carry out the local explanation or procedure.

- **References:** [PROV-Overview](../references/w3c-2013-prov-overview.md)
