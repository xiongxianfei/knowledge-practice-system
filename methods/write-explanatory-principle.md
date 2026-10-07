---
id: "kps:me:write-explanatory-principle"
type: "method"
version: "9.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored method; supporting findings separately attributed"
confidence: "proposed implementation, not independently validated"
uses_principles: ["kps:p:explicit-reasoning-exposes-assumptions", "kps:p:evidence-applicability-depends-on-the-question"]
uses_models: ["kps:mo:knowledge-role-model", "kps:mo:claim-evidence-model"]
references: []
perspectives: ["knowledge-representation", "evidence-reasoning"]
uses_methods: ["kps:me:check-local-completeness"]
---

# Write an explanatory Principle

## Key takeaway

Extract reusable explanatory content without disguising a design rule as deeper knowledge.

## Summary

A relationship that survives changes in implementation can inform several responses. A preferred response with “because” appended remains a response. Rewrite “Use stable IDs” by first asking what it explains. “An entity can retain identity while its name changes” is a candidate relationship. A particular identifier syntax stays a Model or Method choice.

## Inputs and prerequisites

A concrete question, the material or actual record to inspect, and enough context to distinguish observed information from a proposed interpretation. No result is assumed in advance.

## Local explanatory basis

Writing the premises and inference connecting a choice makes those stated assumptions available for inspection. Evidence for one population, task, comparison or outcome does not automatically establish an effect for a materially different target.

## Objective
Extract reusable explanatory content without disguising a design rule as deeper knowledge.

## Rationale
A relationship that survives changes in implementation can inform several responses. A preferred response with “because” appended remains a response.

## Evidence and reasoning
Use [Knowledge role model](../models/knowledge-role-model.md), [Claim–evidence–inference model](../models/claim-evidence-model.md) and the synthesis for the candidate claim. Naming alone does not determine epistemic status.

## Steps
1. Start with a supported or explicitly provisional relationship, not a command. Write the relevant scope and conditions in the Statement.
2. Explain the relationship in ordinary language, or give a bounded logical example. Identify scientific findings, domain inference and design convention separately.
3. Use [Synthesize sources](synthesize-sources.md) for material empirical claims. A formal argument may instead show its premises and counterexample conditions.
4. Name more than one plausible downstream response where genuine. Do not manufacture extra Methods just to pass a count.
5. Move fixed cardinalities, exact timings, mandatory schema choices and task instructions into Models, Methods or Practices. Link back to the explanation.
6. Give a declarative filename and title, the evidence synthesis, scope, alternatives and a challenge condition. Record uncertain claims as uncertain.

## Expected effect
An explanatory Principle with traceable support and no dependence on one mandatory implementation.

## Validation and counterevidence
Test: would the explanation remain meaningful if REM used another hierarchy or Swim another safe cue? If not, review its type. A source supports the actual Statement, not merely its topic.

## Limits
Not every field has settled scientific laws. Do not fabricate evidence or universal causal certainty to populate principles/.

## Local evidence summary

This file uses KPS’s declared conventions or an explicit reasoning argument rather than claiming an externally tested intervention. Its explanation and counterexample are local; linked objects identify reusable connections, not independent confirmation.

## Local completeness check

State who can use the file and what they should understand or do. Hide its links: the essential definitions, explanatory relation, representation or procedure, evidence limits and next/fallback decision must remain visible. Restore links and compare the summary with the source meaning. Preserve decision-critical qualifiers; do not copy full derivations just to increase length. Update dependent summaries deliberately when their source changes. These are authoring checks, not empirical evidence of effectiveness.

## Deeper knowledge

Canonical dependencies and Reference records provide additional derivation, source inspection and alternatives. They are not required to carry out the local explanation or procedure.

- **Principles:** [Explicit reasoning exposes assumptions](../principles/explicit-reasoning-exposes-assumptions.md)
- **Principles:** [Evidence applicability depends on the question](../principles/evidence-applicability-depends-on-the-question.md)
- **Models:** [Knowledge role model](../models/knowledge-role-model.md)
- **Models:** [Claim–evidence–inference model](../models/claim-evidence-model.md)
- **Methods:** [Check local completeness and faithful compression](check-local-completeness.md)
