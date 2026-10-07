---
id: "kps:me:trace-method-rationale"
type: "method"
version: "9.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored method; supporting findings separately attributed"
confidence: "proposed implementation, not independently validated"
uses_principles: ["kps:p:explicit-reasoning-exposes-assumptions", "kps:p:provenance-does-not-establish-truth"]
uses_models: ["kps:mo:rationale-trace-model"]
references: []
perspectives: ["knowledge-representation", "evidence-reasoning"]
---

# Trace a Method rationale

## Key takeaway

Make visible why an operation is being selected and what remains uncertain.

## Summary

A relevant Principle can constrain several options without selecting one uniquely. The missing bridge includes the task, assumptions, direct evidence and trade-offs. For a summary-generation Method, write: equivalent files may diverge; readers still need local context; therefore use concise summaries with reviewable dependencies. Verify that the proposed review can actually find its source and scope.

## Inputs and prerequisites

A concrete question, the material or actual record to inspect, and enough context to distinguish observed information from a proposed interpretation. No result is assumed in advance.

## Local explanatory basis

Writing the premises and inference connecting a choice makes those stated assumptions available for inspection. A trace showing where a claim came from does not by itself establish that the claim is correct.

## Objective
Make visible why an operation is being selected and what remains uncertain.

## Rationale
A relevant Principle can constrain several options without selecting one uniquely. The missing bridge includes the task, assumptions, direct evidence and trade-offs.

## Evidence and reasoning
Use [Rationale trace model](../models/rationale-trace-model.md). A reference is support for a located premise, not automatic support for the Method’s full effect.

## Steps
1. State the goal, current context and proposed operation.
2. Name the explanatory Principle and situational Model, or state that the Method has empirical guidance without a complete mechanism.
3. List the source-supported premises and exact reference claims. Write the extra assumptions needed for this use.
4. Compare at least one plausible alternative when the decision is consequential. Explain why this option is selected here.
5. Predict an observable effect and an adverse or contrary signal. Distinguish execution failure from failure of the proposed explanation.
6. Attach the written rationale to the Method; add selection/order rationale at the Practice step. Do not store all “why” in a new folder.

## Expected effect
A short, auditable reason chain, not just a “based on physics” label.

## Validation and counterevidence
The uncertain inferential bridge can be named. A circular Model–Principle link is not counted as independent support.

## Limits
More prose cannot fix weak evidence. Some decisions are conventional; label them instead of inventing a causal story.

## Local evidence summary

This file uses KPS’s declared conventions or an explicit reasoning argument rather than claiming an externally tested intervention. Its explanation and counterexample are local; linked objects identify reusable connections, not independent confirmation.

## Deeper knowledge

Canonical dependencies and Reference records provide additional derivation, source inspection and alternatives. They are not required to carry out the local explanation or procedure.

- **Principles:** [Explicit reasoning exposes assumptions](../principles/explicit-reasoning-exposes-assumptions.md)
- **Principles:** [Provenance does not establish truth](../principles/provenance-does-not-establish-truth.md)
- **Models:** [Rationale trace model](../models/rationale-trace-model.md)
