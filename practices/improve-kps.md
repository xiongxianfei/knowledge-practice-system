---
id: "kps:pr:improve-kps"
type: "practice"
version: "10.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-12"
basis_kind: "KPS-specific application synthesis; external methods are distinguished from adaptations"
confidence: "provisional for real-world application"
uses_methods: ["kps:method:pdca", "kps:method:cognitive-walkthrough"]
uses_models: []
uses_principles: []
practice_format: "steps-first-v1"
stage_order: "recommended; stated prerequisites and stopping conditions govern entry"
stage_titles: ["Stage1 Locate the actual problem", "Stage2 Compare bounded repairs", "Stage3 Pilot the repair on real content", "Stage4 Release and monitor"]
references: ["kps:r:pdca", "kps:r:walkthrough"]
---


# Improve KPS without mistaking structure for usefulness

## Key takeaway

Repair a demonstrated reading or execution problem, then test both the content and the checks that govern it.

## Summary

Use this Practice to change KPS itself. Begin with an actual failure point, compare small repairs, test them on representative content, and publish the justified change. The worked case concerns a stage format that rewards repeated labels rather than usable instructions; it is an authored illustration, not evidence of improved learning.

Stage numbers show recommended order. The actual prerequisites are an identifiable problem, the files it affects, and authority to edit them. A language or tooling change needs a compatibility assessment; it does not authorize editing every domain repository.

## Stage map

1. [Stage1 Locate the actual problem](#stage1-locate-the-actual-problem)
2. [Stage2 Compare bounded repairs](#stage2-compare-bounded-repairs)
3. [Stage3 Pilot the repair on real content](#stage3-pilot-the-repair-on-real-content)
4. [Stage4 Release and monitor](#stage4-release-and-monitor)

## Stage1 Locate the actual problem

Name the task a reader cannot complete, not just the formatting you dislike.

**Steps**

1. Capture the precise file, section and intended reader action. Keep the observation separate from the cause you suspect.
2. Trace the problem to content, the authoring convention, a template, a validator or a renderer. Read each relevant layer; do not infer a rule from one example.
3. Define the evidence that a repair would help. For repeated stage labels, a useful check is whether the revised stage exposes the first action and a usable fallback without link-chasing.
4. Record what must not be lost: rationale, prerequisites, interpretation, source limits and history.

**Diagnosis map**

```text
Reader problem
  +-- Missing action or explanation -> knowledge content
  +-- Repetition demanded everywhere -> authoring contract or template
  +-- Good content rejected          -> validator implementation
  +-- Link valid but not navigable   -> viewer or destination convention
```

The branches identify places to inspect, not a proven causal classification. More than one can apply. If the report only says “too long,” obtain a concrete use case before shortening away a critical condition.

## Stage2 Compare bounded repairs

Prefer the repair that solves the observed problem without creating a second source of authority.

**Steps**

1. Compare a local edit with a contract or validator change. State which files and readers each option affects.
2. Write the new rule in `AUTHORING.md` only if it is an actual authoring convention. A rule about Markdown is not a scientific Principle.
3. Specify machine checks separately from human review. A program can detect a missing target; it cannot establish that the linked evidence supports a claim.
4. Record the compatibility boundary and a migration route before changing templates.

| Candidate repair | Benefit | What must still be checked |
|---|---|---|
| Delete repeated labels only | Less repetition | Are the actions still complete? |
| Move instructions into linked Methods | Shorter stage | Would the reader need several other files? |
| Put steps first and explain decisions locally | Direct use remains possible | Did important limits survive compression? |
| Require an image in every stage | Predictable layout | Would this add decoration without information? |

No option wins because it is fashionable. For this task, select content based on missing reader understanding, and use graphics only when they explain a real relation.

**Use an established improvement cycle:** Treat the proposed repair as a [PDCA](../methods/pdca.md) change: plan a bounded improvement, try it, check the result and act accordingly. Our choices of Markdown structure, local completeness and release workflow belong to this Practice, not to ASQ's original procedure. Prefer a source-compatible repair to inventing another reusable category.

## Stage3 Pilot the repair on real content

A template is not a pilot. Apply the change to the actual files a reader would use.

**Steps**

1. Rewrite a simple stage and a difficult stage with steps first. Keep their identities and meaningful headings when the task is unchanged.
2. Hide links and walk through a safe case. Record what the reader must produce, how they interpret it and where they stop. Mark a paper walk-through as such.
3. Inspect a worked example, a decision table and any local image. Verify that their content agrees with the steps; an attractive diagram must not introduce an untested causal claim.
4. Run positive and negative checker tests. Accept usable short stages and stage decision tables; reject missing destinations, empty action lists, broken images and link-only instructions. Do not restore a word quota as a proxy for usefulness.
5. Recheck dependency summaries only after the content comparison. Update tests deliberately when requirements change; do not remove failing integrity tests merely to get a pass.

**Example acceptance record**

```text
File and stage:
Reader task and prerequisites:
Paper walk-through or actual execution:
First point that required guessing:
Correction made and remaining uncertainty:
Structural tests actually run:
```

A synthetic fixture can exercise the checker but cannot establish real-reader comprehension. If the content still requires guessing, revise it even when CI is green.

**Evaluate usability without claiming a trial:** Use the [cognitive walkthrough](../methods/cognitive-walkthrough.md) questions on a specified reader and task. Note the visible cues and the knowledge a successful action assumes. Record predictions of difficulty separately from observed reader behavior. To investigate an actual improvement, compare task, assistance and familiarity conditions as well as document versions; several changed factors leave causal attribution uncertain.

## Stage4 Release and monitor

Make the change discoverable without forcing unrelated packages to migrate now.

**Steps**

1. Update the authoritative contract, examples, checker, regression suite, review guidance and release notes together. Preserve object roles and prior evidence unless the change warrants revising them.
2. Record the exact checker version. A newer checker may accept old documents while an older checker rejects new layouts; describe that direction instead of saying “all versions work.”
3. Publish one coherent diff to the corresponding repository. Respect the owner's current merge authorization and repository protections; do not create stacked PRs merely to divide writing work.
4. Verify the final remote state and report only what happened. Leave other domain repositories untouched unless their migration was requested.
5. Set a concrete future review trigger, such as a reader report of an unclear step. This is a proposed trigger, not a scheduled background task.

Useful verification resources: [GitHub relative-link guidance](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#relative-links) for repository navigation, and [W3C complex-image guidance](https://www.w3.org/WAI/tutorials/images/complex/) for accessible visual explanations. Neither supplies evidence that this KPS release improves productivity.

## Current practice summary

Record the observed problem, selected repair, checks performed, publication status and remaining uncertainty from actual work. No completed improvement or user trial is presumed here.

## Deeper knowledge

The following files explain the external meanings and procedures used above. Their selection, adaptation and KPS workflow remain our application.

- [Plan Do Check Act](../methods/pdca.md)

- [Cognitive Walkthrough](../methods/cognitive-walkthrough.md)

[Authoring contract](../AUTHORING.md) defines the local file roles. [Alignment and migration](../ALIGNMENT.md) distinguishes external meaning from KPS design.
