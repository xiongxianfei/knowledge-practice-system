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

First inspect the target and its knowledge selection using the reconstruction review below. A successful walkthrough of an example chosen from the draft cannot establish that the draft includes the knowledge the target requires.

1. Choose a declared reader, a safe representative task and the actual document version. Read the prerequisites before hiding outbound links.
2. Follow the steps on paper or in an authorized environment. Identify the input, operation and expected artifact without guessing missing instructions.
3. Interpret a normal result and a failure or ambiguous result against the stated success criteria and relevant trade-offs. Check that the reader can continue, revise, stop or obtain help. Propose an adjustment to the uncertain case: identify what can change, what must remain and what observation would justify retaining or rejecting the adjustment. A paper walkthrough checks the guidance; it does not establish the adjustment's effectiveness.
4. Inspect each example, table and diagram at its point of use. Verify that it answers a real question and agrees with the instructions. If images are disabled, their essential meaning must remain in text.
5. Restore links and inspect the evidence. Check source contribution, uncertainty, independence and what is not established. A real URL is not evidence of claim-source fit.
6. Record pass, revise or unresolved with the specific observation. Label self-review, paper simulation and actual user trial differently.

## Walk through a Model

1. Compare the stated scope and important topics with the inspected disciplinary accounts and, for subsystems, the body-of-knowledge outline. Look for essential omissions even if the existing examples work. Check that Contents exposes and locates the important explanations. Choose the intended reader, a question within that scope and the actual document version. Hide outbound links and attempt the interpretation using the local explanation. Note any required term or notation whose meaning must be guessed.
2. Identify the represented entities or categories and explain the attributes relevant to that question, including the meaning of values, categories or units. Check that the reader can distinguish the cases the Model is intended to distinguish.
3. Follow a relationship or rule through a concrete example. Explain how the represented details lead to the conclusion; merely naming components or repeating the Summary is insufficient. If a diagram cannot render, check that its essential meaning remains in text.
4. State an assumption or limitation and identify a case or conclusion the Model does not support. For a causal or predictive Model, examine an appropriate counterexample or mismatch with observations. For a structural or classificatory Model, check relation meaning and category boundaries without inventing a causal claim.
5. Restore links and inspect source support. Check that the local definitions, attributes and relationships preserve the source's relevant conditions, and distinguish source statements from authored synthesis and constructed examples.
6. Record pass, revise or unresolved with the point where interpretation required guessing and any remaining evidence limit. Label an author's self-review separately from an independent reader trial. A successful walkthrough of one example does not establish general validity.

For the PROV example in the [Model template](templates.md#example-using-the-prov-model), ask the reader to identify the input and output Entities, explain why their versions matter, follow `used` and `wasGeneratedBy` in the stated direction, and explain why derivation does not prove summary accuracy. These are proposed review prompts, not recorded reader results.

## Review knowledge reconstruction

1. Identify the target Practice, intended reader, output and conditions. For a learning target, state what the reader should explain, analyze or investigate; naming headings is insufficient.
2. Inspect the adopted disciplinary accounts and the selected subset. Check whether their important distinctions, relationships and prerequisites survive reconstruction. Distinguish the source structure from our teaching order and file boundaries. State missing support and unresolved framework differences.
3. Trace representative target questions to the actual explanations and procedures. Select a new case or ambiguity from those questions and source boundaries, rather than only from examples already in the draft. Inspect whether the reader can reason through it with links hidden.
4. Check useful overlap across roles. A Concept, Model and Practice may explain the same distinction for different purposes; compare the meaning and conditions, not sentence identity. Combine fragments when separation breaks understanding; split only where independent use or readability warrants it.
5. Record separately whether coverage, local usability and source fidelity pass, need revision or remain unresolved. Structural checks and editorial self-review do not establish learning effectiveness or independent scientific approval.

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

## Practice reconstruction editorial review

On 2026-10-13 the authoring assistant checked the revised authoring, alignment and template guidance together with Build domain knowledge 10.3.0. The walkthrough starts with a learning target, selects an established account and reconstructs an explanation before choosing a primary role and file boundary. It permits the same necessary distinction in a Concept, Model and Practice while checking consistency. Stage1 now drafts the Practice; Stage4 refines it, preserving existing stage anchors. Coverage, usability and source fidelity have separate review questions.

The changes are KPS application guidance, not new empirical claims or externally prescribed taxonomy. Existing Core admission rules, metadata and validator behavior remain intact. No existing knowledge recipient depends on the changed Practice in the dependency snapshot, and no declared dependency content changed; no fingerprint refresh was needed. Linked library and contributor descriptions still fit its purpose. This was an assistant editorial walkthrough, not an independent reader trial or a measured learning result.

## Structural checks and limits

Run `python validate.py .` and `python -m unittest internal.tests.test_validate`. Resolve file/fragment, metadata, image and dependency errors. The checker accepts substantive action lists or decision tables without the six-label form; it cannot prove that those actions are useful, safe or true. [Authoring](authoring.md) is the authority. Record commands and actual results in the change PR; [source review](source-review.md) preserves inspection scope and limits.

## Source fidelity review

For every Concept, Principle, Model and Method, compare the actual passage with the local statement. Check the discipline, edition, certainty, missing conditions and model subset. Inspect an opposing source when it could change the claim. A declared `source_alignment` field is not evidence that this review happened. Keep local adaptations in Practices and record actual inspected extent.

## Flexible Model authoring review

On 2026-10-14 the authoring assistant separated the Model's minimal structure from its explanatory responsibilities. Identity, title, introductory prose and linked Contents provide orientation; coverage, representation, connections and evidence limits remain substantive responsibilities without fixed section names or quotas. The Model template, authoring contract and walkthrough were compared for agreement. Other knowledge roles retain their existing opening rules.

The two Core Models gain Contents without changing their source-defined explanations or selected relationships. Their summaries and the three receiving Practice summaries (Build domain knowledge, Review and learn, Use KPS) were compared before refreshing dependency fingerprints. No new source inspection, independent review or reader trial is claimed for these navigation edits.

Validator 9.2.0 accepts a plain introduction or an existing Summary, checks that Contents links address local sections in heading order, and requires a suitable declared tool floor for the flexible opening. It does not grade topic completeness or infer explanatory quality from section names. Four bounded regression methods cover the flexible opening, absent introduction, malformed Contents and the tool floor; existing non-Model opening checks remain. All 86 Core tests and the 18 D2/SVG source-render checks passed. The renderer was initially absent from PATH; the existing pinned D2 0.9.0 binary was then used successfully. This is a proposed checker revision, not an official release or automatic upgrade of other domains.
