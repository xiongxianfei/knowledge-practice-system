---
language: "KPS 9.x"
package_version: "9.0.1"
reviewed: "2026-10-07"
---

# Method to reason map

## Key takeaway
A Method names an action; its rationale explains why that action is a candidate rather than an inevitable consequence.

## Summary
The map links operations to their deeper explanatory dependencies. Each Method already summarizes the needed reasoning inline. These links provide depth, not a substitute for local understanding. A typed relationship indicates intended use, not evidence of effectiveness.

## Operations and explanations
| Operation | Explanatory Principles | Models |
|---|---|---|
| [Build and check navigation](methods/build-and-check-navigation.md) | [Navigation depends on rendering conventions](principles/navigation-depends-on-rendering-conventions.md) | [Document navigation model](models/document-navigation-model.md) |
| [Check local completeness and faithful compression](methods/check-local-completeness.md) | [Summaries can omit decision critical conditions](principles/summaries-can-omit-decision-critical-conditions.md); [Provenance does not establish truth](principles/provenance-does-not-establish-truth.md) | [Local summary and dependency model](models/local-summary-dependency-model.md) |
| [Classify knowledge](methods/classify-knowledge.md) | The local rationale states the basis and limits. | [Knowledge role model](models/knowledge-role-model.md) |
| [Create a usable knowledge object](methods/create-knowledge-object.md) | [Independent representations can diverge](principles/independent-representations-can-diverge.md); [Explicit reasoning exposes assumptions](principles/explicit-reasoning-exposes-assumptions.md) | [Knowledge role model](models/knowledge-role-model.md); [Independent domain package model](models/domain-package-model.md) |
| [Make a knowledge file self contained](methods/make-file-self-contained.md) | [Summaries can omit decision critical conditions](principles/summaries-can-omit-decision-critical-conditions.md); [Independent representations can diverge](principles/independent-representations-can-diverge.md) | [Local summary and dependency model](models/local-summary-dependency-model.md) |
| [Publish an independent domain](methods/publish-independent-domain.md) | [Provenance does not establish truth](principles/provenance-does-not-establish-truth.md) | [Independent domain package model](models/domain-package-model.md) |
| [Register a reference](methods/register-reference.md) | [Provenance does not establish truth](principles/provenance-does-not-establish-truth.md); [Multiple reports can share one evidence base](principles/multiple-reports-can-share-one-evidence-base.md) | [Independent domain package model](models/domain-package-model.md) |
| [Revise linked knowledge](methods/revise-linked-knowledge.md) | [Revised interpretation does not change past observation](principles/revised-interpretation-does-not-change-past-observation.md); [Independent representations can diverge](principles/independent-representations-can-diverge.md) | [Application and revision model](models/application-and-revision-model.md) |
| [Synthesize sources](methods/synthesize-sources.md) | [Multiple reports can share one evidence base](principles/multiple-reports-can-share-one-evidence-base.md); [Evidence applicability depends on the question](principles/evidence-applicability-depends-on-the-question.md); [Observations can fit multiple explanations](principles/observations-can-fit-multiple-explanations.md) | [Claim evidence inference model](models/claim-evidence-model.md) |
| [Test knowledge in use](methods/test-knowledge-in-use.md) | [Learning effects depend on task and comparison](principles/learning-effects-depend-on-task-and-comparison.md); [Observations can fit multiple explanations](principles/observations-can-fit-multiple-explanations.md) | [Application and revision model](models/application-and-revision-model.md) |
| [Trace a Method rationale](methods/trace-method-rationale.md) | [Explicit reasoning exposes assumptions](principles/explicit-reasoning-exposes-assumptions.md); [Provenance does not establish truth](principles/provenance-does-not-establish-truth.md) | [Rationale trace model](models/rationale-trace-model.md) |
| [Write an explanatory Principle](methods/write-explanatory-principle.md) | [Explicit reasoning exposes assumptions](principles/explicit-reasoning-exposes-assumptions.md); [Evidence applicability depends on the question](principles/evidence-applicability-depends-on-the-question.md) | [Knowledge role model](models/knowledge-role-model.md); [Claim evidence inference model](models/claim-evidence-model.md) |

## Reading the reasoning
Identify the goal and context, read the Method rationale, inspect relevant assumptions and competing explanations, and decide what would count against adopting it. Do not turn a successful local trial into proof of a universal mechanism. [Source synthesis](SOURCE-SYNTHESIS-EXAMPLE.md) explains source comparison.
