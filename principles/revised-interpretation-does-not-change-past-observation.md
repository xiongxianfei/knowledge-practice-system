---
id: "kps:p:revised-interpretation-does-not-change-past-observation"
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

# Revised interpretation does not change past observation

## Key takeaway

A later change in interpretation can leave the recorded earlier observation unchanged.

## Summary

A record of what a person reported is distinct from a later claim about its cause. Correcting a transcription error is different from replacing a historical account to fit a new explanation.

## Worked use and boundary

A failure first attributed to a Model is later traced to missing input. Keep the recorded failure and append the corrected explanation; do not claim the original run succeeded.

## Statement
A later change in interpretation can leave the recorded earlier observation unchanged.

## Explanation
A record of what a person reported is distinct from a later claim about its cause. Correcting a transcription error is different from replacing a historical account to fit a new explanation.

## Evidence and source synthesis
Logical distinction between record and assertion. [PROV-Overview](../references/w3c-2013-prov-overview.md#provenance-describes-production-history) supplies compatible entity and derivation vocabulary; it is not an experimental demonstration of improved memory.

## Derivation and applications
Versioned interpretations, dated annotations and linked correction notices all preserve this distinction. The appropriate record depth depends on the consequence of losing the difference.

## Scope
Practice records, source corrections and engineering or learning decisions.

## Limits and alternatives
Records can themselves be wrong. Corrections should identify what changed; privacy and retention constraints may justify deletion instead of indefinite history.

## Qualification and challenge
If a supposed observation was actually an inference, its label needs correction; the distinction still applies.

## Local evidence summary


[PROV-Overview](../references/w3c-2013-prov-overview.md#provenance-describes-production-history) contributes: PROV represents the origins of entities through activities and agents, enabling provenance to be exchanged.

Citation identifies support for the stated claim and scope. Any further causal or practical inference remains separately reviewable.

## Deeper knowledge

Canonical dependencies and Reference records provide additional derivation, source inspection and alternatives. They are not required to carry out the local explanation or procedure.

- **References:** [PROV-Overview](../references/w3c-2013-prov-overview.md)
