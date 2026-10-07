---
id: "kps:me:synthesize-sources"
type: "method"
version: "9.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored method; supporting findings separately attributed"
confidence: "proposed implementation, not independently validated"
uses_principles: ["kps:p:multiple-reports-can-share-one-evidence-base", "kps:p:evidence-applicability-depends-on-the-question", "kps:p:observations-can-fit-multiple-explanations"]
uses_models: ["kps:mo:claim-evidence-model"]
references: ["kps:r:cochrane"]
perspectives: ["knowledge-representation", "evidence-reasoning"]
---

# Synthesize sources

## Key takeaway

Build or revise a defensible claim by comparing the evidence it actually needs, not by collecting prestigious links.

## Summary

A source may be authoritative for a definition but irrelevant to efficacy. Several pages may repeat one study. Synthesis separates these cases and exposes unsupported bridges. Question: does a procedure improve retention or merely completion speed? Separate the outcomes, assign each source a role, group common studies and record contrary findings. The synthesis may end in “uncertain”; a predetermined conclusion is not required.

## Inputs and prerequisites

A concrete question, the material or actual record to inspect, and enough context to distinguish observed information from a proposed interpretation. No result is assumed in advance.

## Local explanatory basis

The number of documents repeating a result can exceed the number of independent observations supporting it. Evidence for one population, task, comparison or outcome does not automatically establish an effect for a materially different target. An observed improvement can be compatible with several causal explanations when relevant conditions changed together.

## Objective
Build or revise a defensible claim by comparing the evidence it actually needs, not by collecting prestigious links.

## Rationale
A source may be authoritative for a definition but irrelevant to efficacy. Several pages may repeat one study. Synthesis separates these cases and exposes unsupported bridges.

## Evidence and reasoning
[Cochrane Handbook for Systematic Reviews of Interventions, version 6.5](../references/cochrane-2024-handbook-v6-5.md#reports-and-underlying-studies) informs source-family handling and [Cochrane Handbook for Systematic Reviews of Interventions, version 6.5](../references/cochrane-2024-handbook-v6-5.md#indirectness-relative-to-the-target-question) informs applicability. The procedure is a lightweight adaptation; it is not an exhaustive systematic review or universal evidence hierarchy.

## Steps
1. Write the knowledge question and intended use. Decompose mixed statements into definition, empirical relationship, causal explanation, design choice and instruction.
2. Describe what would support each claim and what would count against it. Search the claim and a plausible alternative, not only wording that favors the preferred Method.
3. Find primary or authoritative materials appropriate to that specific need. Stop adding sources that only repeat an upstream source unless they supply new detail or a correction.
4. Create or reuse Reference records using [Register a reference](register-reference.md). Record access extent and study/source family. A different publisher alone is not independence.
5. Extract claim-level support with a locator. Mark support, challenge, context only or not established; preserve source qualifications and contradictory guidance.
6. Compare populations, tasks, interventions, outcomes, assumptions, conflicts of interest when reported, and what was actually measured. Do not average unlike claims or equate recommendation with efficacy.
7. Write the synthesis: what converges, what disagrees, what might explain the difference, and which gaps remain. One authoritative definition can suffice; broad contested effects usually need more investigation.
8. Separate source-supported premises from the extra assumptions, goals and reasoning that create the KPS conclusion.
9. Stop when additional search is unlikely to change this bounded decision at the needed confidence, or when a material gap is explicitly left unresolved. Record the search boundary; absence in this bounded search is not absence of all evidence.
10. Update the Principle, Model or Method and its scope. Use [Trace a Method rationale](trace-method-rationale.md) to reconnect any action.

## Expected effect
A compact claim/source matrix, synthesis, explicit inference and downstream decision. Small syntheses stay in the object. Substantial shared analyses can live under references/syntheses/ with support-record metadata, but are not external publications.

## Validation and counterevidence
Can another reader recover what each source contributes, identify shared upstream evidence, distinguish the conclusion from a design choice, and state what could reverse it?

## Limits
No fixed source quota or “peer reviewed therefore true” shortcut. Access-limited studies remain access-limited. The published package itself is not independent evidence for its own claims.

## Minimal synthesis table

| Target claim | Located contribution | Independence / scope | Assessment |
|---|---|---|---|
| Definition or relation | Reference and claim anchor | Source family and relevant conditions | Support / challenge / context / gap |

Below the table write **source-supported premises**, **our inference**, **alternatives**, and **search/access limitations**. These are fields, not extra object types.

## Completed example
[Worked synthesis: does retrieval always beat concept mapping?](../SOURCE-SYNTHESIS-EXAMPLE.md) shows why a retrieval-versus-mapping headline is not a universal Method ranking.

## Local evidence summary


[Cochrane Handbook for Systematic Reviews of Interventions, version 6.5](../references/cochrane-2024-handbook-v6-5.md#reports-and-underlying-studies) contributes: Several reports can describe one underlying study; report count is therefore not study count.

[Cochrane Handbook for Systematic Reviews of Interventions, version 6.5](../references/cochrane-2024-handbook-v6-5.md#indirectness-relative-to-the-target-question) contributes: Evidence may be indirect when study populations, interventions, comparisons or outcomes differ from the target question.

Citation identifies support for the stated claim and scope. Any further causal or practical inference remains separately reviewable.

## Deeper knowledge

Canonical dependencies and Reference records provide additional derivation, source inspection and alternatives. They are not required to carry out the local explanation or procedure.

- **Principles:** [Multiple reports can share one evidence base](../principles/multiple-reports-can-share-one-evidence-base.md)
- **Principles:** [Evidence applicability depends on the question](../principles/evidence-applicability-depends-on-the-question.md)
- **Principles:** [Observations can fit multiple explanations](../principles/observations-can-fit-multiple-explanations.md)
- **Models:** [Claim–evidence–inference model](../models/claim-evidence-model.md)
- **References:** [Cochrane Handbook for Systematic Reviews of Interventions, version 6.5](../references/cochrane-2024-handbook-v6-5.md)
