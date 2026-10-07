---
id: "kps:pr:build-domain-knowledge"
type: "practice"
version: "9.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored orchestration; not an independently tested programme"
confidence: "provisional for real-world application"
uses_methods: ["kps:me:make-file-self-contained", "kps:me:check-local-completeness", "kps:me:classify-knowledge", "kps:me:register-reference", "kps:me:synthesize-sources", "kps:me:write-explanatory-principle", "kps:me:create-knowledge-object", "kps:me:publish-independent-domain", "kps:me:build-and-check-navigation"]
uses_models: ["kps:mo:domain-package-model"]
uses_principles: []
practice_format: "staged-inline-stageN-v1"
stage_order: "recommended; stated prerequisites and stopping conditions govern entry"
stage_titles: ["Stage1 Define the domain boundary", "Stage2 Find evidence for explicit claims", "Stage3 Create locally complete objects", "Stage4 Compile the Practice", "Stage5 Check and release"]
---

# Build a domain knowledge package

## Key takeaway

Build a small usable domain around an actual task, with evidence and local explanations before broad expansion.

## Summary

**Stage order:** Numbers show the recommended reading and working order, not a compulsory completion sequence. Enter the stage matching the present question while respecting its stated prerequisites. Revisit an earlier stage when new evidence warrants it. A stage number is not a stable identity.

A domain package applies KPS to one field. It contains the five knowledge folders and supporting Reference records, with no required runtime dependence on another package. This Practice establishes scope, inspects claims, writes reusable objects and compiles them into operational stages. The filesystem is a convention; usability and factual support still need separate review.

### Stage map

- [Stage1 Define the domain boundary](#stage1-define-the-domain-boundary)
- [Stage2 Find evidence for explicit claims](#stage2-find-evidence-for-explicit-claims)
- [Stage3 Create locally complete objects](#stage3-create-locally-complete-objects)
- [Stage4 Compile the Practice](#stage4-compile-the-practice)
- [Stage5 Check and release](#stage5-check-and-release)

The sequence is a starting route. Revisit a stage when the current decision requires it; no stage is a separate file by default. The current outcome is not assumed.

## Stage1 Define the domain boundary

**Summary**

**Goal:** Choose the work and audience the package will serve.

**Why:** A library without a target use cannot tell which detail is essential.

**What to do:** State goals, exclusions, prerequisites and the first recurring Practice.

**What to observe:** Scope creep and unsupported assumptions about the reader.

**Success signal:** A reader can tell what is included and what is not.

**Next:** Find evidence for explicit claims for claims and evidence.

**Entry and understanding**

Choose the work and audience the package will serve. The boundary is the stated task, not a requirement to complete every stage of the repository. A library without a target use cannot tell which detail is essential.

**Procedure**

1. Write a package summary naming the domain, audience, real goals and exclusions. For physical tasks, state actual safety prerequisites rather than assuming reading creates competence.
2. Create concepts/, principles/, models/, methods/, practices/ and references/. The last folder is supporting source records, not a sixth knowledge type.
3. Choose one recurring task as the integration target. Use plain lowercase kebab-case filenames and stable IDs independent of paths.

**Decision points and fallback**

If the scope is too large to populate coherently, keep the larger topic as future work rather than generate thin placeholder files.

## Stage2 Find evidence for explicit claims

**Summary**

**Goal:** Establish what source support is actually needed.

**Why:** Several sources can repeat one upstream account, and authority does not establish claim relevance.

**What to do:** Decompose important claims, inspect supporting and challenging sources, and write a bounded synthesis.

**What to observe:** Exact scope, evidence families, unavailable content and unresolved disagreement.

**Success signal:** Important premises, inferences and local design choices are distinguishable.

**Next:** Create locally complete objects for reusable objects.

**Entry and understanding**

Establish what source support is actually needed. The boundary is the stated task, not a requirement to complete every stage of the repository. Several sources can repeat one upstream account, and authority does not establish claim relevance.

**Procedure**

1. Split a candidate paragraph into definitions, empirical relationships, causal explanations and design recommendations. Write what evidence each one would need.
2. Search for claim-relevant material. Prefer the actual publication for attribution; check whether apparently independent reports share a study or handbook.
3. Create a Markdown Reference naming the publication, date basis, URL, access extent, claim locator, contribution and limitations. Do not archive full external material in this package.
4. Compare agreement, contradiction and scope. A single official source can establish its own definition; a broad effectiveness claim usually needs more than a convenient quotation.
5. Write the synthesis: sources support A; assumption B is added for this task; therefore C is a candidate. Retain disagreement and missing evidence.

**Decision points and fallback**

When only an abstract is available, restrict the claim. When sources do not justify the intended action, weaken the claim, find another approach or leave it provisional.

## Stage3 Create locally complete objects

**Summary**

**Goal:** Make each reusable object understandable at its own role.

**Why:** The reader should not reconstruct essential meaning from a chain of links.

**What to do:** Write the takeaway, summary, actual content, local evidence and limits for every file.

**What to observe:** Rules disguised as Principles, vague Models and link-only Methods.

**Success signal:** Each file passes a role-specific link-hidden review.

**Next:** Compile the Practice for Practice synthesis.

**Entry and understanding**

Make each reusable object understandable at its own role. The boundary is the stated task, not a requirement to complete every stage of the repository. The reader should not reconstruct essential meaning from a chain of links.

**Procedure**

1. Use a Concept for a definition; a Principle for a reusable explanatory relationship; a Model for the representation; a Method for an operation; a Practice for orchestration.
2. For each file, write its meaning before its links. Define needed terms, explain assumptions, include a worked example or boundary, and distinguish source findings from inference.
3. For a Method, provide inputs, steps, expected signal, counterevidence and stop/fallback conditions. For a Model, include elements, relationships and assumptions inline.
4. Remove forced category filling. A local reason can stay in a Method; an unnecessary standalone object can be merged.
5. Hide links and test the intended reading/use task. Compare compressed content against canonical scope and evidence before declaring it locally complete.

**Decision points and fallback**

If a Principle is mainly “must use this exact structure,” put that choice in the Model or Method and retain the deeper explanation separately.

## Stage4 Compile the Practice

**Summary**

**Goal:** Make the knowledge usable for the recurring goal.

**Why:** Reusable depth and immediate operational use need different amounts of detail.

**What to do:** Write stages with inline why, action, observation, success and next/fallback.

**What to observe:** Whether stage decisions work without opening another file.

**Success signal:** A reader with the prerequisites can choose and execute the next stage.

**Next:** Check and release for release review.

**Entry and understanding**

Make the knowledge usable for the recurring goal. The boundary is the stated task, not a requirement to complete every stage of the repository. Reusable depth and immediate operational use need different amounts of detail.

**Procedure**

1. Write an opening Summary and stage map. Each stage has Goal, Why, What to do, What to observe, Success signal and Next.
2. Embed the locally necessary Model explanation and selected Method variant. Link full derivations afterward, not in place of instructions.
3. Add cross-stage troubleshooting and one blank current-state summary. Stages may be revisited; do not present a rigid progression unless evidence or task constraints justify it.
4. Keep stages in one file while usable. Compose a separately reusable Practice only when it has an independent goal and logic; do not create files for every step.

**Decision points and fallback**

If the Practice exposes an explanatory gap, revise the supporting Model or Method as well as the prose. More words alone do not solve the gap.

## Stage5 Check and release

**Summary**

**Goal:** Publish a coherent, honest package.

**Why:** File integrity and evidence quality are different claims.

**What to do:** Check links, identities, references, local summaries, safety and actual source access; then package independently.

**What to observe:** Stale dependencies, phantom records and unsupported claims of validation.

**Success signal:** The package works alone and reports precisely what was checked.

**Next:** Use the package on a real task and revise from evidence.

**Entry and understanding**

Publish a coherent, honest package. The boundary is the stated task, not a requirement to complete every stage of the repository. File integrity and evidence quality are different claims.

**Procedure**

1. Run the structural validator, then conduct a prose review with links hidden. Structural passing is not semantic certification.
2. Read each selected Reference against its contribution; preserve abstract-only or unavailable sections. Check important disagreements are not silently removed.
3. Write release scope, limitations and a checksum manifest. Extract the archive into a fresh directory without sibling packages and run checks again.
4. Report only actual checks and observations. A blank template is not an executed Practice Record.

**Decision points and fallback**

Do not publish unresolved safety-critical guidance as ready for use. A package can be a proposed design rather than an adopted contract.

Run `python validate.py . --manifest` after the release files and manifest have been generated. The checker catches structural defects; it does not validate source conclusions or render an installed desktop app.

**Deeper procedure:** [Build and check navigation](../methods/build-and-check-navigation.md).

## Troubleshooting

If the object is understandable only after opening links, add the minimum missing meaning locally. If it becomes huge, separate general depth from the task-specific summary. If sources disagree, preserve the disagreement and narrow the claim. If the validator passes but the task remains unclear, revise the prose; a structural pass is not a usability result.

## Current practice summary

**Actual task:** Not recorded.  
**What worked:** Not recorded.  
**Unresolved:** Not recorded.  
**Next check:** Not selected.  
**Review date and record:** Not recorded.

Fill these only from actual use. A generated example or template is not a completed application.

## Local evidence and authorship

The stages are authored KPS procedures, not an independently evaluated productivity programme. Source synthesis borrows the distinction between studies and reports; provenance supplies origin information rather than truth; empirical learning comparisons apply only to their actual tasks and measures. The five-role organization and local-completeness contract remain explicit design choices.

## Deeper knowledge

The linked objects provide reusable detail and source inspection beyond the locally executable stages.


- **Models:** [Independent domain package model](../models/domain-package-model.md)
- **Methods:** [Make a knowledge file self-contained](../methods/make-file-self-contained.md)
- **Methods:** [Check local completeness and faithful compression](../methods/check-local-completeness.md)
- **Methods:** [Classify knowledge](../methods/classify-knowledge.md)
- **Methods:** [Register a reference](../methods/register-reference.md)
- **Methods:** [Synthesize sources](../methods/synthesize-sources.md)
- **Methods:** [Write an explanatory Principle](../methods/write-explanatory-principle.md)
- **Methods:** [Create a usable knowledge object](../methods/create-knowledge-object.md)
- **Methods:** [Publish an independent domain](../methods/publish-independent-domain.md)
