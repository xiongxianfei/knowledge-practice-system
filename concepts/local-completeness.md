---
id: "kps:c:local-completeness"
type: "concept"
version: "9.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored KPS design; explicit reasoning, not an effectiveness trial"
confidence: "provisional application"
uses_concepts: ["kps:c:knowledge-object", "kps:c:rationale"]
---

# Local completeness

## Key takeaway

A file contains the meaning and safeguards needed for its declared use; it does not contain all knowledge.

## Summary

Local completeness is a reading and use contract. A reader with the declared prerequisites can understand the file’s central claim, its reason, its intended use and its important limits without opening another file. The contract differs by role: a Model needs its representation; a Method needs executable steps; a Reference needs the contribution and its access limits.

## Definition and use

“Local” refers to this file and this reader/task, not to the entire field. “Complete” means decision-critical definitions, reasoning and constraints are present. A swimming Method may assume the reader can safely regain support, but must say that before an unsupported task. It cannot assume that reading an explanation supplies that competence.

## Example and non example

Incomplete: “Use the comparison Method; see the Model for why.” Complete for a small document check: select two plausible explanations, state a discriminating observation, inspect the actual file, record what is seen and retain unresolved alternatives. The general experimental Method remains linked for depth.

Copying an entire source into the file is not a stronger definition of completeness. A short Reference can explain what a study found and what was inspected while requiring the original for verification.

## Evidence and limits

This is a selected authoring convention, not an empirical threshold for word count or a guarantee of usability. Hiding links is a useful review exercise; passing a heading checker does not establish comprehension. The reader, task, prerequisites and omitted depth must be stated.

## Deeper knowledge

Links supply canonical detail and provenance; the local definitions, reasoning and operation above carry the essential meaning.

- **Concepts:** [Knowledge object](knowledge-object.md)
- **Concepts:** [Rationale](rationale.md)
