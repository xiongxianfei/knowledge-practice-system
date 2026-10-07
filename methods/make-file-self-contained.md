---
id: "kps:me:make-file-self-contained"
type: "method"
version: "9.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored KPS design; explicit reasoning, not an effectiveness trial"
confidence: "provisional application"
uses_principles: ["kps:p:summaries-can-omit-decision-critical-conditions", "kps:p:independent-representations-can-diverge"]
uses_models: ["kps:mo:local-summary-dependency-model"]
---

# Make a knowledge file self contained

## Key takeaway

Write the smallest complete local explanation or operation, then add links for deeper inspection.

## Summary

Begin with the reader and the decision the file supports. Include the terms, reasoning, representation or procedure, evidence limits and safeguards needed for that local task. Summarize dependencies rather than copying them wholesale. This is an authoring operation, not a guarantee that the content is true.

## Objective

Turn a link-dependent knowledge object into an independently understandable and, where appropriate, executable file.

## Inputs and prerequisites

A draft, its intended reader and task, the canonical knowledge being summarized, and the supporting references. If an important source is inaccessible, record the limit instead of completing it from expectation.

## Rationale

A link tells a reader where to go, not what the current file means. Conversely, a copied explanation can become stale independently. A contextual summary preserves the relevant relationship and condition while maintaining a named source for deeper review.

## Steps

1. Name the intended use in one sentence and state the reader’s prerequisites.
2. Write a Key takeaway and a Summary that express the object itself, not merely advertise its contents.
3. Define any term that the local operation cannot be understood without; keep specialised depth in linked Concepts.
4. State the relationship or rationale in plain language, with the additional assumptions needed here.
5. Include the actual representation for a Model or executable steps, inputs and completion checks for a Method. For a Practice, do this inside each substantive stage.
6. Preserve evidence type, major uncertainty, contraindications and the conditions that change the next decision. A Reference includes publication identity, located claims and access extent.
7. Add an example and non-example or counter-signal when ambiguity is likely. Do not fabricate an observed outcome.
8. Add deeper links and declare the dependencies whose meaning was summarized.
9. Hide those links and try the target reading/use task. Revise missing local content; compress redundant derivations.

## Worked example

Before: “Apply the source rule; see provenance.” After: “Find the exact passage supporting the claim and record the publication, locator and scope. Knowing who published it identifies its origin but does not establish that it supports this claim. If only an abstract is available, limit the extraction accordingly.” The Reference and provenance Model remain available as deeper links.

## Output and validation

The file has a meaningful Summary, enough local reasoning and the role-specific content needed for use. A reader can say what is claimed, what to do with it and what would make that use inappropriate. Run the link-hidden check and inspect dependency consistency.

## Limits

Length is not a pass criterion. A file may be concise and complete for a narrow task, or long and still omit a critical condition. This Method does not certify domain expertise, physical competence or scientific truth.

## Deeper knowledge

Links supply canonical detail and provenance; the local definitions, reasoning and operation above carry the essential meaning.

- **Principles:** [Summaries can omit decision-critical conditions](../principles/summaries-can-omit-decision-critical-conditions.md)
- **Principles:** [Independent representations can diverge](../principles/independent-representations-can-diverge.md)
- **Models:** [Local summary and dependency model](../models/local-summary-dependency-model.md)
