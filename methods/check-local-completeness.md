---
id: "kps:me:check-local-completeness"
type: "method"
version: "9.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored KPS design; explicit reasoning, not an effectiveness trial"
confidence: "provisional application"
uses_principles: ["kps:p:summaries-can-omit-decision-critical-conditions", "kps:p:provenance-does-not-establish-truth"]
uses_models: ["kps:mo:local-summary-dependency-model"]
uses_methods: ["kps:me:make-file-self-contained"]
---

# Check local completeness and faithful compression

## Key takeaway

Check both missing local meaning and distorted copied meaning; neither headings nor working links are enough.

## Summary

This review asks whether a file works for its declared reader without link-chasing and whether its compressed explanation still respects its sources. It combines a link-hidden reading test, an application or representation check, and a dependency comparison. Automated checks provide warnings, not semantic approval.

## Objective

Detect under-specified, misleadingly compressed or unnecessarily duplicated objects before relying on them.

## Inputs and prerequisites

The file, a declared reader/task, its source dependencies and a safe example task or paper simulation. Do not test a hazardous action merely to evaluate the writing.

## Rationale

Missing context can make an instruction unusable. Missing limits can make it appear more general than its support. Independent copies may drift, so readability and source faithfulness are separate checks.

## Steps

1. Hide outbound links and machine-only metadata without changing the substantive text.
2. For a Concept, restate its meaning and a boundary. For a Principle, identify the explanatory relationship, basis and scope. For a Model, follow its elements and transitions. For a Method, walk through inputs, actions, observations and stopping conditions. For a Practice, enter one stage and decide the next or fallback action. For a Reference, identify the work and exactly what was inspected.
3. Mark where an undefined term, missing assumption or external pointer prevents that task. Add only the local information needed.
4. Reveal dependencies. Compare the summary with their current scope, uncertainty, procedure and safety limits.
5. Check that imperative implementation choices did not migrate into a Principle and that a perspective name did not become evidence.
6. Remove large duplicated derivations unless they are genuinely needed for the local task. Retain the concise argument and traceable source.
7. Record pass, revise or unresolved with the observed reason. A self-review is not an independent user test.

## Output and validation

A concrete review note such as “Stage lacks a fallback when air access fails; add support/stop decision” is actionable. “Looks good” or a passed word-count threshold is not sufficient evidence of usability.

## Counterevidence and limits

If the reader still cannot choose the next action with links hidden, the file is incomplete for that task. If source comparison shows an omitted qualifier, the compression needs revision even when readable. A file can pass this review and still contain a false underlying claim.

## Deeper knowledge

Links supply canonical detail and provenance; the local definitions, reasoning and operation above carry the essential meaning.

- **Principles:** [Summaries can omit decision-critical conditions](../principles/summaries-can-omit-decision-critical-conditions.md)
- **Principles:** [Provenance does not establish truth](../principles/provenance-does-not-establish-truth.md)
- **Models:** [Local summary and dependency model](../models/local-summary-dependency-model.md)
- **Methods:** [Make a knowledge file self-contained](make-file-self-contained.md)
