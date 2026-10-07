---
package_version: "9.0.1"
language: "KPS 9.x"
reviewed: "2026-10-07"
---

# Reusable authoring templates

## Key takeaway
These are non-normative examples implementing the [authoring contract](AUTHORING.md).

A template supports the job of the knowledge type; it does not prove correctness or require every field to become a file.

## Summary
All objects need identity, meaning, locally sufficient content, scope and support. Copy only the useful fields, replacing placeholders with real content. The examples below are fenced templates, not live published knowledge. Reference records support the five knowledge types rather than becoming a sixth type.

## Common metadata
```yaml
---
id: "domain:method:meaningful-identity"
type: "method"
version: "1.0.0"
language: "KPS 9.x"
status: "draft"
reviewed: null
uses_principles: []
uses_models: []
references: []
---
```
For the optional dependency-free checker, write metadata values in JSON-compatible YAML as shown. General Markdown content does not depend on that checker.

## Common opening
```markdown
# Meaningful title

## Key takeaway
One useful sentence stating the object itself.

## Summary
What it means, why it matters, how it is used and its main limit.
```

## Concept content
Definition; necessary distinctions; recognizable example and non-example; why it matters; boundaries and evidence; optional deeper links. Do not force procedures into a vocabulary note.

## Principle content
Declarative Statement; explanatory mechanism or relationship; evidence-supported premises; explicit derivation; independently useful applications; limits; possible challenge. Do not disguise a selected instruction as a universal truth. Scientific and domain levels can be metadata; formal or design reasoning must be labelled rather than invented as experiment.

## Model content
Purpose; necessary terms; actual representation; relationships; assumptions; implications; how to evaluate; evidence and limitations. Summarize necessary dependencies inline instead of linking away the explanation.

## Method content
Objective; inputs and prerequisites; rationale; numbered procedure; expected effect; observations and counter-signals; limits or stop conditions; example; deeper evidence. A new comparison procedure is a proposal until used; examples do not establish effectiveness.

## Practice content
```markdown
# Practice name

## Key takeaway
The recurring goal and central approach.

## Summary
Audience, permitted use, prerequisites and limits.
Stage numbers show recommended order, not mandatory completion.

## Stage map
Generate links from the actual numbered headings.

## Stage1 Meaningful first stage
**Goal:** The bounded result.
**Why:** Essential reasoning in context.
**What to do:** Compact action.
**What to observe:** Relevant signals.
**Success signal:** What supports the next decision.
**Next:** Forward, revisit, stop or get help.

**Understanding**
Necessary Concepts, Principles and Model relationships in plain language.

**Procedure**
Executable local steps, not a list of links.

**Decision points and fallback**
What changes the next action and when not to proceed.

**Deeper knowledge**
Canonical detail and source locators after the usable explanation.

## Current practice summary
Actual findings, uncertainty and next focus; leave unfilled until real use.
```
Stages can logically compose smaller goals within one file. Create a separately reusable Practice only when it has its own meaningful goal and decision logic. Composition must not create an endless call loop.

## Reference content
Publication identity, creators, publication or update year and its basis, external URL or DOI, actual access date and extent, located claims, evidence family, limitations and non-claims. Use creator-year-short-title filenames, or `undated` when a date was not established. The record must summarize what the source contributes without requiring immediate external access; it is not a copy of the publication.

## Review before publication
Hide links and attempt the intended use; restore links and check the summary remains faithful. Check claim-source fit, headings and fragments, then run the package checker. [Authoring](AUTHORING.md), [Navigation](NAVIGATION.md) and [Compatibility](COMPATIBILITY.md) provide the complete local maintenance instructions.
