---
id: "kps:p:independent-representations-can-diverge"
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

# Independent representations can diverge

## Key takeaway

When equivalent mutable representations can be edited independently, continued agreement is not guaranteed.

## Summary

Consider A and B with the same value. An allowed update to A alone produces different values. The possibility follows from independent mutability, not from a measured rate of human error.

## Worked use and boundary

A Model describes a comparison as tentative. A Method summary omits that qualifier and presents it as certain. The files can both be readable while disagreeing; a dependency review must check the meaning, not just the link.

## Statement
When equivalent mutable representations can be edited independently, continued agreement is not guaranteed.

## Explanation
Consider A and B with the same value. An allowed update to A alone produces different values. The possibility follows from independent mutability, not from a measured rate of human error.

## Evidence and source synthesis
This is a conditional design argument, not a scientific trial. [PROV-Overview](../references/w3c-2013-prov-overview.md#provenance-describes-production-history) supplies provenance vocabulary, but is not evidence that duplication always causes mistakes.

## Derivation and applications
A shared definition, generated projection, synchronized replica or explicit reconciliation procedure are different responses. The selected response depends on availability, history and coordination costs; a one-source rule does not follow uniquely.

## Scope
Representations intended to carry the same meaning, where independent updates are permitted.

## Limits and alternatives
Deliberate historical snapshots need not agree with the current state. Enforced synchronization changes the premise. Names that look similar may denote different claims.

## Qualification and challenge
A demonstration that the alleged copies cannot change independently, or are not meant to agree, removes this explanation for that case.

## Local evidence summary


[PROV-Overview](../references/w3c-2013-prov-overview.md#provenance-describes-production-history) contributes: PROV represents the origins of entities through activities and agents, enabling provenance to be exchanged.

Citation identifies support for the stated claim and scope. Any further causal or practical inference remains separately reviewable.

## Deeper knowledge

Canonical dependencies and Reference records provide additional derivation, source inspection and alternatives. They are not required to carry out the local explanation or procedure.

- **References:** [PROV-Overview](../references/w3c-2013-prov-overview.md)
