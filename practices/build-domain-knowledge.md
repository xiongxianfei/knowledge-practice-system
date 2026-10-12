---
id: "kps:pr:build-domain-knowledge"
type: "practice"
version: "10.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-12"
basis_kind: "KPS-specific application synthesis; external methods are distinguished from adaptations"
confidence: "provisional for real-world application"
uses_methods: ["kps:method:pico-question-formulation", "kps:method:study-data-extraction", "kps:method:cognitive-walkthrough"]
uses_models: ["kps:model:skos-data-model", "kps:model:prov-data-model"]
uses_principles: ["kps:principle:study-level-evidence-independence", "kps:principle:indirectness-limits-applicability"]
practice_format: "steps-first-v1"
stage_order: "recommended; stated prerequisites and stopping conditions govern entry"
stage_titles: ["Stage1 Define the domain boundary", "Stage2 Find evidence for explicit claims", "Stage3 Create locally complete objects", "Stage4 Compile the Practice", "Stage5 Check and release"]
references: ["kps:r:skos", "kps:r:prov-dm", "kps:r:data-extraction", "kps:r:indirectness", "kps:r:procida-how-to", "kps:r:wai-complex-images"]
uses_concepts: ["kps:concept:skos-concept", "kps:concept:study-and-report", "kps:concept:evidence-indirectness"]
---


# Build an independent domain knowledge package

## Key takeaway

Build enough knowledge to support one real task, then verify that the task works without link-chasing.

## Summary

Create a small, independent package whose reusable knowledge and task guidance agree. Start with the reader's job rather than a quota of Concepts or Methods. Keep the five knowledge roles distinct, retain the evidence behind claims, and place the essential actions inside each Practice.

Stage numbers give recommended order; source access, safe working conditions and permission to publish are actual prerequisites. Empty templates are not completed investigations. A plain text editor and Python are sufficient for the structural checks; no dedicated authoring application is required.

## Stage map

1. [Stage1 Define the domain boundary](#stage1-define-the-domain-boundary)
2. [Stage2 Find evidence for explicit claims](#stage2-find-evidence-for-explicit-claims)
3. [Stage3 Create locally complete objects](#stage3-create-locally-complete-objects)
4. [Stage4 Compile the Practice](#stage4-compile-the-practice)
5. [Stage5 Check and release](#stage5-check-and-release)

## Stage1 Define the domain boundary

Decide what a reader should accomplish in the first usable slice.

**Steps**

1. Write the audience, recurring task, intended output and exclusions. A useful first scope is “maintain Markdown navigation”; “document all software engineering” is not a bounded deliverable.
2. Inventory existing material and label observations, source extracts, proposals and private records. Do not promote a personal result into a general Principle merely because it is useful.
3. Create the five role directories plus `references/`. Leave a directory empty rather than manufacture knowledge to fill it.
4. Draft a README that names the entry Practice, reader prerequisites and limits. Record package identity and compatibility in `publication.json`.

```text
domain/
  README.md                 reader entry
  concepts/                 definitions
  principles/               explanatory relationships
  models/                   representations
  methods/                  reusable operations
  practices/                complete task guidance
  references/               publication records
```

The tree separates reusable knowledge from publication support. It does not imply that every task needs a new file in every folder.

**Publication metadata starting point**

```json
{"package":"my-domain","version":"1.0.0","kps_language":"9.x","validated_with":"9.1.0","markdown_profile":"practical-markdown-v1","minimum_validator":"9.1.0"}
```

Choose a stable package name and an actual reviewed version. The number does not prove compatibility; inspect the contract before declaring it.

**KPS design boundary:** The five file roles, one-object-per-file rule and dependency fields are our publishing conventions. They are not prescribed by SKOS, PROV, Cochrane or ISO. Use the [authoring contract](../AUTHORING.md) for syntax; use the source-aligned library only for the source's actual meaning. A Model that merely describes our package layout is embedded here, not promoted as external theory. Domain-specific deployment technology remains replaceable.

## Stage2 Find evidence for explicit claims

Search for the support the claim needs, not for an impressive bibliography.

**Steps**

1. List candidate claims and the evidence each requires. A definition needs an appropriate defining source; a performance comparison needs the actual task, comparator and measured outcome.
2. Inspect the relevant passage. Record publication identity, URL, section locator, inspected extent and date. State “abstract only” or “landing page only” when that is all you read.
3. Group reports that share an underlying study. Compare disagreement and applicability instead of treating every citation as independent confirmation.
4. Write a local synthesis that separates source premises, your inference and the remaining uncertainty. Narrow or remove a claim the evidence does not support.

**Source worksheet**

| Claim | Inspected support | Boundary | Consequence for the draft |
|---|---|---|---|
| A format is accepted by a named reader | Its official syntax section | One documented reader | Do not claim universal Markdown behavior |
| A procedure improves outcomes | An applicable comparison | Population and outcome may differ | Keep the recommendation conditional |
| Two reports confirm a finding | Both cite one study | One evidence family | Do not count them as two replications |

[Cochrane Chapter 5](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-05) explains the studies-versus-reports distinction. That is its contribution here; it does not prescribe this KPS workflow. Keep the corresponding [local Reference](../references/cochrane-2024-collecting-data-chapter-5.md) so readers can inspect the provenance later.

**Apply professional sources without borrowing their authority**

1. For terminology or a defined data relation, inspect the defining specification. For effectiveness, inspect the relevant experiment or review; a standards logo does not establish an effect.
2. For an intervention question, [PICO](../methods/pico-question-formulation.md) can clarify population, intervention, comparator and outcome. For an identifier definition, skip PICO and inspect the defining section. Using “reader and task” in place of a clinical population is our explicit analogy, not a Cochrane requirement.
3. Apply the discipline of [study data extraction](../methods/study-data-extraction.md) to a local claim worksheet: source/version, locator, exact supported claim, conditions, contrary evidence and what was not inspected. This small worksheet is not a systematic review.
4. Keep the source, our inference and our chosen action in separate cells. If no source supports a purported definition or established Method, move the local idea into this Practice or leave it a private hypothesis.

```text
Inspected source -> located premise -> qualified inference -> local action
                         |                   |
                 original scope      assumptions and alternatives
```

This is our reasoning bridge, not a new professional model. A single source can define its own term; independent effectiveness claims need different support. Conflicting authorities can define different scopes. Name both rather than silently blending them or forcing exact equivalence.

**Reference identity:** Save one structured Markdown record per publication or clearly identified chapter. Include creator, full title, edition/year basis, URL, inspected locator, access extent and nonclaims. Abstract-only and inaccessible evidence remain limited; do not fabricate a full-text review. The source itself stays external.

## Stage3 Create locally complete objects

Choose a file's role by its job, not by who wrote it.

**Steps**

1. Put definitions in Concepts, explanatory relationships in Principles, representations in Models, and reusable operations in Methods. Put your complete task workflow in a Practice. A selected rule is not an explanatory Principle.
2. Give each object a stable identity, semantic filename, meaningful title, Key takeaway and Summary. Include the terms and conditions necessary to understand it locally.
3. For a Method, provide inputs, rationale, executable actions, output checks and limits. For a Model, show the representation and assumptions rather than merely naming it.
4. Link only genuine dependencies. Where a file summarizes another object, retain the local reason or instruction as well as the link.

**Minimal metadata**

```yaml
---
id: "my-domain:concept:link-target"
type: "concept"
version: "1.0.0"
language: "KPS 9.x"
status: "draft"
---
```

**A useful distinction, not a duplicate file quota**

| Text you are writing | Likely home |
|---|---|
| What a link target means | Concept |
| Why a title change can invalidate navigation | Local explanation in the navigation step, supported by reader documentation |
| How to repair this package destination | Practice step using the documented syntax |
| How to maintain a whole knowledge package | Practice |

If a detail is only useful inside one step, keep it there. Split a file when it gains independent use or becomes difficult to navigate, not merely because a template has another heading.

**Role assignment is KPS application knowledge**

| What the file actually does | KPS role and boundary |
|---|---|
| Explains an externally defined term | Concept; preserve that discipline and scope |
| Explains a published empirical or methodological relationship | Principle; state conditions rather than commands |
| Shows an established representation | Model; distinguish the full model from the subset shown |
| Teaches a published repeatable technique | Method; identify the actual procedure and limitations |
| Chooses and adapts knowledge for a local task | Practice; identify the adaptation as ours |

These are working roles, not external definitions of the five capitalized labels. Our own rule, such as “store each claim in one file,” stays here or in the authoring specification. It does not become a scientific Principle.

**Alignment record to copy:** Include the source Reference, relation (`definition-paraphrase`, `scoped-empirical-finding`, `methodological-relationship`, `standard-model-subset` or `published-procedure-summary`) and exact locator in `source_alignment`. These labels describe our documentation relationship, not formal SKOS mappings. Claiming SKOS `exactMatch` requires the specification's stronger semantics; similar wording is insufficient.

**Write the actual reasoning:** State the source relationship, the assumptions needed in this context, the alternative actions and why this choice is useful. A Method is not uniquely deduced from a Principle. Split a proposed object only when it has independent use; combine overlapping fragments and keep purely local operations in the stage that needs them.

## Stage4 Compile the Practice

Write the actions first. Put supporting information next to the action that needs it.

**Steps**

1. Outline the task as a few meaningful `Stage1`, `Stage2` headings and generate a stage map from the complete headings. Explain prerequisites once at entry and repeat only local hazards where they matter.
2. Write each action with an object, an operation and a visible result. Replace “review the evidence” with “record the study conditions and the exact claim the passage supports.”
3. Add the missing explanation at the point of use. Include a worked example where a reader would otherwise guess; use a table for branching decisions and a diagram for relationships.
4. Give the reader an interpretation and next decision: continue, revise, stop or obtain help. These can be sentences or tables; do not recreate six mandatory labels.
5. Annotate external resources with what to inspect and what they contribute. Keep essential instructions inline. For diagrams, explain the meaning in nearby prose; a chart needs its data, units and assumptions as well.

**Before and after**

```text
Before: Follow the navigation Method. See the style guide.
After:  Compare the fragment with the complete heading.
        For “Stage1 Capture a record”, use
        #stage1-capture-a-record. Test the link in the reader.
        If the fragment matches but navigation fails, check
        that reader rather than changing the document at random.
```

**Choose support by the missing understanding**

| Reader difficulty | Add locally |
|---|---|
| Cannot picture the sequence | Short flow diagram with a prose explanation |
| Cannot distinguish possible results | Decision table with observations and actions |
| Does not know what to produce | Small completed synthetic example and blank record |
| Needs to verify an important claim | Direct source link plus exact contribution and limit |

[Diataxis how-to guidance](https://diataxis.fr/how-to-guides/) supports task-focused instructions and branching. KPS deliberately differs by retaining essential explanations inline; it is not a pure Diataxis how-to. [W3C guidance on complex images](https://www.w3.org/WAI/tutorials/images/complex/) informs the text alternative for a meaningful visual, not a requirement to add images everywhere.

**Check the compiled guide without recreating the old labels**

Hide its links, then attempt one declared task from the stated prerequisites. Mark where the action, terminology, reason, expected result or safe fallback is missing. Restore links and compare the local explanation to its source; a fluent summary can omit the very condition that permits use. This two-pass KPS review is our composition of inspection techniques, not a separately established Method.

For navigation and discoverability, adapt a [cognitive walkthrough](../methods/cognitive-walkthrough.md): at each step inspect whether a reader would pursue the needed goal, notice the action, connect it to the result and recognize progress. Record the assumed reader knowledge and visible cues. A paper inspection predicts difficulties; it does not demonstrate improved comprehension. Obtain actual reader evidence when that claim matters.

## Stage5 Check and release

Test the content as a task guide before treating a green checker as success.

**Steps**

1. Hide links and walk through one safe example on paper. Mark each point where an input, rationale, result or fallback must be guessed. Restore the links and compare local summaries against their sources.
2. Copy the inspected KPS checker and its tests into the package, retaining their provenance and license. From the package root run the commands below. If a check reports an error, inspect its file and diagnostic rather than deleting the check.
3. Review dependent summaries after changes, then refresh their fingerprints. Do not refresh them merely to silence a failure.
4. Inspect the publication diff for private records, secrets, source copies, accidental deletion and unsupported claims. Keep earlier versions in history, not a competing legacy knowledge folder.
5. When publication is requested, use one PR against the actual main branch. Merge automatically only where the owner has authorized it and checks pass. Otherwise leave review with the owner. With no corresponding repository, publish a validated ZIP and report that no repository changed.

```bash
python validate.py .
python test_validate.py
# Only after inspecting changed source summaries:
python validate.py . --accept-reviewed-summaries
python validate.py .
```

A freshly created package needs an initial reviewed dependency snapshot; run the refresh after the initial content review, then rerun validation. Later failures about stale summaries must receive the same substantive review.

**Release decision**

```text
Read-through failure -> repair content -> review again
Structural failure  -> repair target  -> run checks again
Both pass           -> permitted PR or ZIP -> report exact status
```

The two checks answer different questions. A self-review is not an independent usability trial, and neither check establishes scientific truth.

**Identity and navigation check:** Keep the object ID in metadata, the meaningful title in the heading and current order in `StageN`. A metadata ID does not create an anchor. Generate the fragment from the complete heading, resolve relative paths from the containing file, and test the actual viewer. Renumbering requires updating incoming stage links. This is a local Markdown convention, not a property imposed by RFC 3986.

**Publication decision:** Preserve the inspected repository baseline and license. Make one coherent PR against `main`, rerun CI and merge when the owner has authorized it and checks pass. If a corresponding repository is absent, prepare a validated ZIP. Do not manufacture a separate official release or modify sibling domains merely to finish this task.

## Current practice summary

No domain-building outcome is supplied. Record the actual task, inspected sources, unresolved claims, checks run and publication result only after execution. Synthetic examples above are not application records.

## Deeper knowledge

The following files explain the external meanings and procedures used above. Their selection, adaptation and KPS workflow remain our application.

- [PICO Question Formulation](../methods/pico-question-formulation.md)

- [Study Data Extraction](../methods/study-data-extraction.md)

- [Cognitive Walkthrough](../methods/cognitive-walkthrough.md)

- [SKOS Data Model](../models/skos-data-model.md)

- [PROV Data Model](../models/prov-data-model.md)

- [SKOS Concept](../concepts/skos-concept.md)

- [Study and Report](../concepts/study-and-report.md)

- [Evidence Indirectness](../concepts/evidence-indirectness.md)

- [Study Level Evidence Independence](../principles/study-level-evidence-independence.md)

- [Indirectness Limits Applicability](../principles/indirectness-limits-applicability.md)

[Authoring contract](../AUTHORING.md) defines the local file roles. [Alignment and migration](../ALIGNMENT.md) distinguishes external meaning from KPS design.
