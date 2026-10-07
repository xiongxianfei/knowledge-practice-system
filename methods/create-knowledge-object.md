---
id: "kps:me:create-knowledge-object"
type: "method"
version: "9.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored method; supporting findings separately attributed"
confidence: "proposed implementation, not independently validated"
uses_principles: ["kps:p:independent-representations-can-diverge", "kps:p:explicit-reasoning-exposes-assumptions"]
uses_models: ["kps:mo:knowledge-role-model", "kps:mo:domain-package-model"]
references: []
perspectives: ["knowledge-representation", "evidence-reasoning"]
uses_methods: ["kps:me:check-local-completeness"]
---

# Create a usable knowledge object

## Key takeaway

Turn a relevant idea into a usable, minimally structured Markdown object.

## Summary

A note becomes useful when another task can interpret its meaning, scope and connections without reconstructing the entire source conversation. Create one file about representation drift. Define an equivalent representation, state the conditional divergence argument, explain a possible application and a limit, then link canonical depth. A pile of URLs is not the output.

## Inputs and prerequisites

A concrete question, the material or actual record to inspect, and enough context to distinguish observed information from a proposed interpretation. No result is assumed in advance.

## Local explanatory basis

When equivalent mutable representations can be edited independently, continued agreement is not guaranteed. Writing the premises and inference connecting a choice makes those stated assumptions available for inspection.

## Objective
Turn a relevant idea into a usable, minimally structured Markdown object.

## Rationale
A note becomes useful when another task can interpret its meaning, scope and connections without reconstructing the entire source conversation.

## Evidence and reasoning
The fields implement [Knowledge role model](../models/knowledge-role-model.md) and [Independent domain package model](../models/domain-package-model.md); their usability is a design expectation, not a measured effect.

## Steps
1. Classify with [Classify knowledge](classify-knowledge.md) and check for an existing matching identity.
2. Write the smallest coherent statement or procedure that can be reused. Include context and limits before generalizing.
3. Register needed sources and link claim anchors. Separate personal reports, source statements, inferred explanation and chosen action.
4. Add the type-specific sections. For a Method, include Rationale, Steps, Expected effect, Validation and counterevidence. For a Practice, include goal, routes, selection rationale and feedback.
5. Use nouns for Concepts, declarative relationships for Principles, named representations for Models, operations for Methods and recurring goals for Practices.
6. Link only meaningful dependencies and run the local check. Apply or retrieve the object in one realistic task before growing its metadata.

## Expected effect
One readable object with a stable ID and enough reasoning for its intended use.

## Validation and counterevidence
The content is not a source summary without an application, a copied rule disguised as a Principle, or a collection of empty fields.

## Limits
A tiny local rationale can stay inside a Method. No requirement to create all five types for every task.

## Copyable schemas
[Object and Reference templates](../TEMPLATES.md) contains all five object templates and the supporting Reference template. Template blanks are intentionally unfilled; they are not claims of completed research.

## Local evidence summary

This file uses KPS’s declared conventions or an explicit reasoning argument rather than claiming an externally tested intervention. Its explanation and counterexample are local; linked objects identify reusable connections, not independent confirmation.

## Local completeness check

State who can use the file and what they should understand or do. Hide its links: the essential definitions, explanatory relation, representation or procedure, evidence limits and next/fallback decision must remain visible. Restore links and compare the summary with the source meaning. Preserve decision-critical qualifiers; do not copy full derivations just to increase length. Update dependent summaries deliberately when their source changes. These are authoring checks, not empirical evidence of effectiveness.

## Deeper knowledge

Canonical dependencies and Reference records provide additional derivation, source inspection and alternatives. They are not required to carry out the local explanation or procedure.

- **Principles:** [Independent representations can diverge](../principles/independent-representations-can-diverge.md)
- **Principles:** [Explicit reasoning exposes assumptions](../principles/explicit-reasoning-exposes-assumptions.md)
- **Models:** [Knowledge role model](../models/knowledge-role-model.md)
- **Models:** [Independent domain package model](../models/domain-package-model.md)
- **Methods:** [Check local completeness and faithful compression](check-local-completeness.md)
