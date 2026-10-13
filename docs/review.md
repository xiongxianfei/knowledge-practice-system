---
package_version: "10.0.0"
language: "KPS 9.x"
reviewed: "2026-10-12"
---


# Review content by trying the task

## Key takeaway

A passed parser does not establish that a reader can act or interpret the result.

## Summary

Use a link-hidden walk-through and a source-fidelity check before publication. For a Practice, try the actions and decisions; for a Model, interpret its entities, attributes and relationships in a concrete case. This is a review procedure, not a report of a completed independent usability test. Record the actual task, reviewer role and unresolved difficulties.

## Walk through one stage

1. Choose a declared reader, a safe representative task and the actual document version. Read the prerequisites before hiding outbound links.
2. Follow the steps on paper or in an authorized environment. Identify the input, operation and expected artifact without guessing missing instructions.
3. Interpret a normal result and a failure or ambiguous result. Check that the reader can continue, revise, stop or obtain help.
4. Inspect each example, table and diagram at its point of use. Verify that it answers a real question and agrees with the instructions. If images are disabled, their essential meaning must remain in text.
5. Restore links and inspect the evidence. Check source contribution, uncertainty, independence and what is not established. A real URL is not evidence of claim-source fit.
6. Record pass, revise or unresolved with the specific observation. Label self-review, paper simulation and actual user trial differently.

## Walk through a Model

1. Choose the intended reader, a question within the Model's stated scope and the actual document version. Hide outbound links and attempt the interpretation using the local explanation. Note any required term or notation whose meaning must be guessed.
2. Identify the represented entities or categories and explain the attributes relevant to that question, including the meaning of values, categories or units. Check that the reader can distinguish the cases the Model is intended to distinguish.
3. Follow a relationship or rule through a concrete example. Explain how the represented details lead to the conclusion; merely naming components or repeating the Summary is insufficient. If a diagram cannot render, check that its essential meaning remains in text.
4. State an assumption or limitation and identify a case or conclusion the Model does not support. For a causal or predictive Model, examine an appropriate counterexample or mismatch with observations. For a structural or classificatory Model, check relation meaning and category boundaries without inventing a causal claim.
5. Restore links and inspect source support. Check that the local definitions, attributes and relationships preserve the source's relevant conditions, and distinguish source statements from authored synthesis and constructed examples.
6. Record pass, revise or unresolved with the point where interpretation required guessing and any remaining evidence limit. Label an author's self-review separately from an independent reader trial. A successful walkthrough of one example does not establish general validity.

For the PROV example in the [Model template](templates.md#example-using-the-prov-model), ask the reader to identify the input and output Entities, explain why their versions matter, follow `used` and `wasGeneratedBy` in the stated direction, and explain why derivation does not prove summary accuracy. These are proposed review prompts, not recorded reader results.

## Evidence of a useful review

| Weak review note | Actionable note |
|---|---|
| The stage is too short | The step needs an input format and an example output |
| More diagrams are needed | The reader cannot distinguish the successful and failure branches |
| All links work | Source section supports only one renderer; narrow the claim |
| CI passed so it is ready | The steps still omit the stop condition; revise content |
| The Model names all its components | The reader cannot interpret an attribute or follow a relationship to a conclusion; explain that meaning locally |

## Local completeness record

```text
Reader and task:
Document version and relevant section or stage:
Review kind: self-review / paper simulation / independent task trial
Where execution or interpretation required guessing:
Missing or misleading support:
Source-fidelity issue:
Change made and unresolved limitation:
```

Do not fill these fields from expected results. Domain validity, physical competence and authorization remain separate judgments.

## Structural checks and limits

Run `python validate.py .` and `python -m unittest internal.tests.test_validate`. Resolve file/fragment, metadata, image and dependency errors. The checker accepts substantive action lists or decision tables without the six-label form; it cannot prove that those actions are useful, safe or true. [AUTHORING.md](authoring.md) is the authority; [CHECKS.md](history/10.2.0-release.md) reports checks actually performed for this release.

## Source fidelity review

For every Concept, Principle, Model and Method, compare the actual passage with the local statement. Check the discipline, edition, certainty, missing conditions and model subset. Inspect an opposing source when it could change the claim. A declared `source_alignment` field is not evidence that this review happened. Keep local adaptations in Practices and record actual inspected extent.
