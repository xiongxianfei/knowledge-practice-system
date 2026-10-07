---
id: "kps:me:revise-linked-knowledge"
type: "method"
version: "9.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored method; supporting findings separately attributed"
confidence: "proposed implementation, not independently validated"
uses_principles: ["kps:p:revised-interpretation-does-not-change-past-observation", "kps:p:independent-representations-can-diverge"]
uses_models: ["kps:mo:application-and-revision-model"]
references: []
perspectives: ["knowledge-representation", "evidence-reasoning"]
uses_methods: ["kps:me:check-local-completeness"]
---

# Revise linked knowledge

## Key takeaway

Change the smallest supported part of the system and inspect its dependent uses.

## Summary

Updating one explanation can leave its old applications unsupported even when their links still resolve. Record and interpretation also have different historical roles. When a source narrows a claim from “always” to “in the tested task,” review not only its Principle but every Model, Method and Practice that summarizes it. A checksum can identify change; the reviewer decides what text must change.

## Inputs and prerequisites

A concrete question, the material or actual record to inspect, and enough context to distinguish observed information from a proposed interpretation. No result is assumed in advance.

## Local explanatory basis

A later change in interpretation can leave the recorded earlier observation unchanged. When equivalent mutable representations can be edited independently, continued agreement is not guaranteed.

## Objective
Change the smallest supported part of the system and inspect its dependent uses.

## Rationale
Updating one explanation can leave its old applications unsupported even when their links still resolve. Record and interpretation also have different historical roles.

## Evidence and reasoning
[Claim–evidence–inference model](../models/claim-evidence-model.md) distinguishes support relationships; [Application and revision model](../models/application-and-revision-model.md) separates outcomes from interpretation.

## Steps
1. Name the triggering observation, source correction, counterexample or change of goal.
2. Check whether the error concerns a statement, scope, rationale, procedure, selection or record. Do not rewrite all objects by default.
3. Use source synthesis for the disputed claim. Retain contradictory evidence and mark unresolved questions.
4. Revise the statement and confidence. Move a wrongly typed rule into its Model or Method rather than rewriting it as vague explanatory prose.
5. Inspect inbound links and each affected rationale. A valid path is not proof that the changed claim still supports the Method.
6. Version material changes and record the reason. Preserve dated original observations only where useful and appropriate; no requirement to archive everything forever.

## Expected effect
Revised knowledge, repaired uses and a brief explanation of the change.

## Validation and counterevidence
Dependent Methods accurately describe their current basis. Old tests are not represented as tests of a new version.

## Limits
This does not authorize changing approved external requirements or user-owned live systems without appropriate permission.

## Local evidence summary

This file uses KPS’s declared conventions or an explicit reasoning argument rather than claiming an externally tested intervention. Its explanation and counterexample are local; linked objects identify reusable connections, not independent confirmation.

## Local completeness check

State who can use the file and what they should understand or do. Hide its links: the essential definitions, explanatory relation, representation or procedure, evidence limits and next/fallback decision must remain visible. Restore links and compare the summary with the source meaning. Preserve decision-critical qualifiers; do not copy full derivations just to increase length. Update dependent summaries deliberately when their source changes. These are authoring checks, not empirical evidence of effectiveness.

## Deeper knowledge

Canonical dependencies and Reference records provide additional derivation, source inspection and alternatives. They are not required to carry out the local explanation or procedure.

- **Principles:** [Revised interpretation does not change past observation](../principles/revised-interpretation-does-not-change-past-observation.md)
- **Principles:** [Independent representations can diverge](../principles/independent-representations-can-diverge.md)
- **Models:** [Application and revision model](../models/application-and-revision-model.md)
- **Methods:** [Check local completeness and faithful compression](check-local-completeness.md)
