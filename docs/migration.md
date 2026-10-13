---
package_version: "10.0.0"
language: "KPS 9.x"
reviewed: "2026-10-12"
---

# KPS Core content migration

## Key takeaway

Retired identifiers are recorded here for migration, not retained as duplicate knowledge objects.

## Summary

Core 10.0.0 breaks the previous Core content IDs and paths while retaining the KPS 9.x authoring language and the four Practice IDs and stage names. All 41 previous non-Practice knowledge objects are accounted for below. Their local responsibilities move into Practices; externally grounded replacements are new objects with their own scope, not claimed exact equivalents.

## Retired objects and receiving stages

| Previous file | Previous ID | Receiving Practice stage |
|---|---|---|
| `concepts/method.md` | `kps:c:method` | [Application content](../practices/build-domain-knowledge.md#stage3-create-locally-complete-objects) |
| `concepts/observation-and-interpretation.md` | `kps:c:observation-and-interpretation` | [Application content](../practices/review-and-learn.md#stage1-reconstruct-the-record) |
| `concepts/practice.md` | `kps:c:practice` | [Application content](../practices/build-domain-knowledge.md#stage4-compile-the-practice) |
| `concepts/identity-title-and-link-target.md` | `kps:c:identity-title-and-link-target` | [Application content](../practices/build-domain-knowledge.md#stage5-check-and-release) |
| `concepts/evidence.md` | `kps:c:evidence` | [Application content](../practices/build-domain-knowledge.md#stage2-find-evidence-for-explicit-claims) |
| `concepts/knowledge-object.md` | `kps:c:knowledge-object` | [Application content](../practices/build-domain-knowledge.md#stage3-create-locally-complete-objects) |
| `concepts/local-completeness.md` | `kps:c:local-completeness` | [Application content](../practices/build-domain-knowledge.md#stage4-compile-the-practice) |
| `concepts/source-and-reference.md` | `kps:c:source-and-reference` | [Application content](../practices/build-domain-knowledge.md#stage2-find-evidence-for-explicit-claims) |
| `concepts/principle.md` | `kps:c:principle` | [Application content](../practices/build-domain-knowledge.md#stage3-create-locally-complete-objects) |
| `concepts/rationale.md` | `kps:c:rationale` | [Application content](../practices/build-domain-knowledge.md#stage3-create-locally-complete-objects) |
| `concepts/concept.md` | `kps:c:concept` | [Application content](../practices/build-domain-knowledge.md#stage3-create-locally-complete-objects) |
| `concepts/model.md` | `kps:c:model` | [Application content](../practices/build-domain-knowledge.md#stage3-create-locally-complete-objects) |
| `principles/revised-interpretation-does-not-change-past-observation.md` | `kps:p:revised-interpretation-does-not-change-past-observation` | [Application content](../practices/review-and-learn.md#stage1-reconstruct-the-record) |
| `principles/evidence-applicability-depends-on-the-question.md` | `kps:p:evidence-applicability-depends-on-the-question` | [Application content](../practices/build-domain-knowledge.md#stage2-find-evidence-for-explicit-claims) |
| `principles/navigation-depends-on-rendering-conventions.md` | `kps:p:navigation-depends-on-rendering-conventions` | [Application content](../practices/use-kps.md#stage2-retrieve-and-inspect-the-local-explanation) |
| `principles/summaries-can-omit-decision-critical-conditions.md` | `kps:p:summaries-can-omit-decision-critical-conditions` | [Application content](../practices/build-domain-knowledge.md#stage4-compile-the-practice) |
| `principles/multiple-reports-can-share-one-evidence-base.md` | `kps:p:multiple-reports-can-share-one-evidence-base` | [Application content](../practices/build-domain-knowledge.md#stage2-find-evidence-for-explicit-claims) |
| `principles/provenance-does-not-establish-truth.md` | `kps:p:provenance-does-not-establish-truth` | [Application content](../practices/review-and-learn.md#stage1-reconstruct-the-record) |
| `principles/explicit-reasoning-exposes-assumptions.md` | `kps:p:explicit-reasoning-exposes-assumptions` | [Application content](../practices/build-domain-knowledge.md#stage3-create-locally-complete-objects) |
| `principles/learning-effects-depend-on-task-and-comparison.md` | `kps:p:learning-effects-depend-on-task-and-comparison` | [Application content](../practices/review-and-learn.md#stage4-define-the-next-check) |
| `principles/independent-representations-can-diverge.md` | `kps:p:independent-representations-can-diverge` | [Application content](../practices/use-kps.md#stage4-update-the-smallest-justified-target) |
| `principles/observations-can-fit-multiple-explanations.md` | `kps:p:observations-can-fit-multiple-explanations` | [Application content](../practices/review-and-learn.md#stage2-compare-explanations) |
| `models/knowledge-role-model.md` | `kps:mo:knowledge-role-model` | [Application content](../practices/build-domain-knowledge.md#stage3-create-locally-complete-objects) |
| `models/application-and-revision-model.md` | `kps:mo:application-and-revision-model` | [Application content](../practices/use-kps.md#stage3-use-and-observe) |
| `models/claim-evidence-model.md` | `kps:mo:claim-evidence-model` | [Application content](../practices/build-domain-knowledge.md#stage2-find-evidence-for-explicit-claims) |
| `models/domain-package-model.md` | `kps:mo:domain-package-model` | [Application content](../practices/build-domain-knowledge.md#stage1-define-the-domain-boundary) |
| `models/document-navigation-model.md` | `kps:mo:document-navigation-model` | [Application content](../practices/use-kps.md#stage2-retrieve-and-inspect-the-local-explanation) |
| `models/local-summary-dependency-model.md` | `kps:mo:local-summary-dependency-model` | [Application content](../practices/use-kps.md#stage4-update-the-smallest-justified-target) |
| `models/rationale-trace-model.md` | `kps:mo:rationale-trace-model` | [Application content](../practices/build-domain-knowledge.md#stage3-create-locally-complete-objects) |
| `methods/test-knowledge-in-use.md` | `kps:me:test-knowledge-in-use` | [Application content](../practices/improve-kps.md#stage3-pilot-the-repair-on-real-content) |
| `methods/register-reference.md` | `kps:me:register-reference` | [Application content](../practices/build-domain-knowledge.md#stage2-find-evidence-for-explicit-claims) |
| `methods/build-and-check-navigation.md` | `kps:me:build-and-check-navigation` | [Application content](../practices/build-domain-knowledge.md#stage5-check-and-release) |
| `methods/write-explanatory-principle.md` | `kps:me:write-explanatory-principle` | [Application content](../practices/build-domain-knowledge.md#stage3-create-locally-complete-objects) |
| `methods/trace-method-rationale.md` | `kps:me:trace-method-rationale` | [Application content](../practices/build-domain-knowledge.md#stage3-create-locally-complete-objects) |
| `methods/make-file-self-contained.md` | `kps:me:make-file-self-contained` | [Application content](../practices/build-domain-knowledge.md#stage4-compile-the-practice) |
| `methods/check-local-completeness.md` | `kps:me:check-local-completeness` | [Application content](../practices/build-domain-knowledge.md#stage4-compile-the-practice) |
| `methods/synthesize-sources.md` | `kps:me:synthesize-sources` | [Application content](../practices/build-domain-knowledge.md#stage2-find-evidence-for-explicit-claims) |
| `methods/create-knowledge-object.md` | `kps:me:create-knowledge-object` | [Application content](../practices/build-domain-knowledge.md#stage3-create-locally-complete-objects) |
| `methods/revise-linked-knowledge.md` | `kps:me:revise-linked-knowledge` | [Application content](../practices/use-kps.md#stage4-update-the-smallest-justified-target) |
| `methods/publish-independent-domain.md` | `kps:me:publish-independent-domain` | [Application content](../practices/build-domain-knowledge.md#stage5-check-and-release) |
| `methods/classify-knowledge.md` | `kps:me:classify-knowledge` | [Application content](../practices/build-domain-knowledge.md#stage3-create-locally-complete-objects) |

## External source replacement

The retired `references/cochrane-2024-handbook-v6-5.md` record is replaced with separate records for [question formulation](../references/cochrane-2024-review-questions-chapter-2.md), [data collection](../references/cochrane-2024-collecting-data-chapter-5.md) and [indirectness](../references/cochrane-2024-certainty-chapter-14.md). The displayed handbook citation is version 6.5 (2024); chapter update dates and current inspection dates are distinguished.

## Migration procedure

1. Identify the version of the incoming reference. The inspected 9.1.0 baseline was commit `ff0d546d07cd880c743b9cec170bfb53f2263f21`; use Git history when the old content is needed.
2. For each inbound reference to a retired Core ID, inspect the relevant receiving stage. Do not claim a new source-aligned definition is an exact substitute for the old local one.
3. Remove obsolete paths rather than maintaining a parallel legacy library. Git history retains their previous content.
4. Run the structural and alignment tests. Review scientific scope and human usability separately.
5. Migrate a sibling domain only when requested. This change does not rewrite Swim, Technical Insight or REM.
