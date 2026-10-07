---
id: "kps:pr:improve-kps"
type: "practice"
version: "9.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored orchestration; not an independently tested programme"
confidence: "provisional for real-world application"
uses_methods: ["kps:me:make-file-self-contained", "kps:me:check-local-completeness", "kps:me:synthesize-sources", "kps:me:test-knowledge-in-use", "kps:me:revise-linked-knowledge", "kps:me:publish-independent-domain", "kps:me:build-and-check-navigation"]
uses_models: ["kps:mo:knowledge-role-model", "kps:mo:domain-package-model"]
uses_principles: []
practice_format: "staged-inline-stageN-v1"
stage_order: "recommended; stated prerequisites and stopping conditions govern entry"
stage_titles: ["Stage1 Locate the actual problem", "Stage2 Compare bounded repairs", "Stage3 Pilot the repair on real content", "Stage4 Release and monitor"]
---

# Improve KPS using KPS

## Key takeaway

Change KPS in response to a specific observed problem, not merely a more attractive label.

## Summary

**Stage order:** Numbers show the recommended reading and working order, not a compulsory completion sequence. Enter the stage matching the present question while respecting its stated prerequisites. Revisit an earlier stage when new evidence warrants it. A stage number is not a stable identity.

KPS is itself a knowledge domain. Its authoring conventions, representations and operating procedures can be examined using its own Methods. This Practice separates an observed usability problem from a proposed ontology change, tests a bounded redesign and updates dependencies without claiming that self-application proves effectiveness.

### Stage map

- [Stage1 Locate the actual problem](#stage1-locate-the-actual-problem)
- [Stage2 Compare bounded repairs](#stage2-compare-bounded-repairs)
- [Stage3 Pilot the repair on real content](#stage3-pilot-the-repair-on-real-content)
- [Stage4 Release and monitor](#stage4-release-and-monitor)

The sequence is a starting route. Revisit a stage when the current decision requires it; no stage is a separate file by default. The current outcome is not assumed.

## Stage1 Locate the actual problem

**Summary**

**Goal:** Describe the failed use and its scope.

**Why:** A complaint about a word may conceal missing content or unclear boundaries.

**What to do:** Record a concrete reading, classification or execution difficulty.

**What to observe:** What the reader attempted and which content was absent or misleading.

**Success signal:** The issue is reproducible on an identified file or example.

**Next:** Compare bounded repairs for alternative explanations.

**Entry and understanding**

Describe the failed use and its scope. The boundary is the stated task, not a requirement to complete every stage of the repository. A complaint about a word may conceal missing content or unclear boundaries.

**Procedure**

1. Preserve the problematic passage and task. Example: “the Method links to a Model but does not state why the action follows.”
2. Distinguish terminological confusion, missing explanation, wrong classification, stale summary and weak evidence.
3. Identify which roles and files are affected. Do not conclude that the whole ontology must change from one title.

**Decision points and fallback**

When there is no actual example, treat the change as a design proposal and test a sample before migration.

## Stage2 Compare bounded repairs

**Summary**

**Goal:** Choose a change that addresses the problem with tolerable costs.

**Why:** Several designs can answer the same explanatory consideration.

**What to do:** Compare wording, section, relationship, split/merge and type-system changes.

**What to observe:** Preserved uses, new burdens and compatibility consequences.

**Success signal:** The selected proposal has a stated reason and counterexample.

**Next:** Pilot the repair on real content for a pilot.

**Entry and understanding**

Choose a change that addresses the problem with tolerable costs. The boundary is the stated task, not a requirement to complete every stage of the repository. Several designs can answer the same explanatory consideration.

**Procedure**

1. List at least one credible alternative or explain why none fits. A “Principle” filled with commands may need content extraction rather than a rename.
2. Write which task each repair improves, what it leaves unresolved and which existing uses it may break.
3. Choose a small pilot and a failure signal. Mark the change as a convention, not a scientific discovery about how all knowledge must work.

**Decision points and fallback**

Prefer the smallest adequate change, but do not preserve IDs or categories when doing so would retain a semantic error.

## Stage3 Pilot the repair on real content

**Summary**

**Goal:** Check local usefulness and canonical consistency.

**Why:** A template can look coherent while failing on an actual object.

**What to do:** Rewrite representative files and walk through a use case with links hidden.

**What to observe:** Missing terms, shifted meaning, duplicated derivations and lost safeguards.

**Success signal:** The intended task is possible and the source meaning remains qualified.

**Next:** Release and monitor to accept or revise.

**Entry and understanding**

Check local usefulness and canonical consistency. The boundary is the stated task, not a requirement to complete every stage of the repository. A template can look coherent while failing on an actual object.

**Procedure**

1. Apply the proposal to a Concept, an explanatory Principle, a Model, a Method and a Practice where relevant.
2. For self-containment, ensure local definitions, rationale, representation/procedure, evidence limits and fallback survive without linked documents.
3. Compare the rewrite with inspected sources and canonical dependencies. Keep disagreements or explicitly document a changed conclusion.
4. Run structural checks, then perform a substantive review. If no independent reader was involved, call it an author review.

**Decision points and fallback**

If a pilot needs huge copied sections, narrow its local task or improve its summary rather than duplicating the entire library.

## Stage4 Release and monitor

**Summary**

**Goal:** Make the accepted change explicit and maintainable.

**Why:** Unannounced semantic changes can alter how old records are interpreted.

**What to do:** Version the affected package, update dependencies and record actual review limits.

**What to observe:** Broken paths, changed meanings and false historical results.

**Success signal:** The published contract and its remaining uncertainties are clear.

**Next:** Return to use; reopen when evidence changes.

**Entry and understanding**

Make the accepted change explicit and maintainable. The boundary is the stated task, not a requirement to complete every stage of the repository. Unannounced semantic changes can alter how old records are interpreted.

**Procedure**

1. Choose a breaking version when the meaning or required authoring contract changes. State which old assumptions are no longer compatible.
2. Revise affected summaries and templates; refresh dependency fingerprints only after comparing meaning.
3. Publish fresh artifacts and state the exact validation performed. Retain old releases separately rather than mixing directories.
4. Observe subsequent use. Self-application demonstrates that the workflow can be performed, not that it is universally optimal.

**Decision points and fallback**

If the proposal remains untested in real use, label application confidence provisional and avoid claims of improved outcomes.

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


- **Models:** [Knowledge role model](../models/knowledge-role-model.md)
- **Models:** [Independent domain package model](../models/domain-package-model.md)
- **Methods:** [Make a knowledge file self-contained](../methods/make-file-self-contained.md)
- **Methods:** [Check local completeness and faithful compression](../methods/check-local-completeness.md)
- **Methods:** [Synthesize sources](../methods/synthesize-sources.md)
- **Methods:** [Test knowledge in use](../methods/test-knowledge-in-use.md)
- **Methods:** [Revise linked knowledge](../methods/revise-linked-knowledge.md)
- **Methods:** [Publish an independent domain](../methods/publish-independent-domain.md)
