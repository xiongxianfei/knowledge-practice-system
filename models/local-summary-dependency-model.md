---
id: "kps:mo:local-summary-dependency-model"
type: "model"
version: "9.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored KPS design; explicit reasoning, not an effectiveness trial"
confidence: "provisional application"
uses_principles: ["kps:p:independent-representations-can-diverge", "kps:p:summaries-can-omit-decision-critical-conditions"]
uses_concepts: ["kps:c:local-completeness"]
---

# Local summary and dependency model

## Key takeaway

A local summary is an authored projection of canonical knowledge, with an explicit review dependency.

## Summary

This model separates a canonical object, its context-specific summary, the receiving task and the record of what was reviewed. Links identify sources of meaning; they do not substitute for local explanation. A dependency change signals the need for review rather than automatically invalidating or approving a summary.

## Purpose

Make locally complete files maintainable without pretending that summaries are independent copies of truth.

## Elements and representation

```text
Canonical object (identity + revision + scoped content)
        | summarized for a stated task
        v
Local explanation / procedure / safeguard
        | used within
Method or Practice stage
        | checked against
Current source + actual reader/task + evidence
```

A dependency record stores the receiving file, source file or ID, inspected revision/fingerprint and the date of review. It is metadata about the summary, not a replacement for the summary.

## Relationships and example

A Model states that video shows an event but does not directly measure force. A Method summarizes this as “Use the clip to locate the event, not infer force magnitude.” A Practice may repeat only “A better-looking frame does not prove lower drag.” Both can be faithful projections for different tasks.

## Update procedure embedded in the model

When a source changes, locate dependent files, compare the changed meaning with each summary, revise or explicitly retain the local wording, then refresh the reviewed fingerprint. Do not refresh fingerprints merely to silence a warning.

## Assumptions evidence and limits

This is a KPS maintenance convention based on independent-copy divergence and conditional information loss. The included dependency checker sees text changes only. It cannot certify scientific accuracy, semantic equivalence, third-party source freshness, or reader comprehension.

## Deeper knowledge

Links supply canonical detail and provenance; the local definitions, reasoning and operation above carry the essential meaning.

- **Concepts:** [Local completeness](../concepts/local-completeness.md)
- **Principles:** [Independent representations can diverge](../principles/independent-representations-can-diverge.md)
- **Principles:** [Summaries can omit decision-critical conditions](../principles/summaries-can-omit-decision-critical-conditions.md)
