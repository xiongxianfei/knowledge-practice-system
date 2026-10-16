---
package_version: "10.0.0"
language: "KPS 9.x"
reviewed: null
---

# Professional source alignment

## Key takeaway

Align the meaning first and keep the KPS application visibly separate.

## Summary

This is the Core library curation policy, not a claim that a professional body endorses KPS. Standalone explanations preserve an inspected published basis. Reusable Method adaptations identify their authored contribution without borrowing the source's authority for it.

## Admission by knowledge role

| Role | Required basis in this Core edition | What stays in Practices |
|---|---|---|
| Concept | Located definition in a named discipline or specification | Our five file-role definitions and classification decisions |
| Principle | Scoped empirical finding or supported explanatory relationship | Our design rules, extrapolations and working hypotheses |
| Model | Identified external representation with subset and limits stated | Our package, navigation and workflow models |
| Method | Identified published operation or analytical approach, with rationale and checks; reusable adaptations distinguish supported parts from authored changes | Particular application choices, our package-authoring workflow and unsupported procedural proposals |
| Practice | Explicit application synthesis with usable inline steps | The actual KPS-specific workflow belongs here |

The authoring specification remains necessary infrastructure. Removing local conventions from the knowledge library does not make a Markdown format externally standardized. The five roles remain KPS design choices, as explained in the [domain-building Practice](../practices/build-domain-knowledge.md#stage3-create-locally-complete-objects).

## Established structure and contextual reconstruction

Reuse the source's concepts, distinctions, representations and relationships when selecting support for a target Practice. Record the adopted framework and subset; a textbook chapter order is a teaching choice, not a required file hierarchy. Selection and reorganization are our application decisions. Preserve dependencies that make the source explanation work, and identify adaptations instead of transferring the source's authority to them.

The admission table concerns the primary contribution of standalone Core objects. Supporting definitions, representations and procedures may overlap within and between objects when needed for local understanding. Such overlap must preserve source meaning and scope. A local workflow remains an authored Practice even when it uses an established Model; an inline definition does not turn the whole workflow into a Concept. Domain packages retain their own declared curation policies; this clarification does not impose Core's alignment metadata on them.

For a Method, an inspected analytical example can establish an operation without prescribing a numbered script. Explain the source-supported comparison or decision, its conditions and checks, then distinguish any local ordering, simplification or combination. The source need not contain our exact sequence. Mere topical relevance is insufficient: if the source only defines terms, further reasoning or procedural support is needed before claiming a grounded method. A reusable adaptation can stand alone when it has independent explanatory value. An unsupported proposal remains in a Practice or private investigation notes in this Core collection until its basis justifies admission. This refines the former blanket placement of authored adaptations in Practices; it does not confer established status or demonstrated efficacy on adaptations.

## Select authority for the claim

Use defining specifications for their terms and relations, procedural publications for their named techniques, and applicable empirical work for effects. A standards body does not prove a learning benefit by defining a format. An experiment does not prescribe the KPS directory layout. An official software page can document a navigation convention without establishing human comprehension.

Where authorities differ, retain the source vocabulary and scope. Rename an ambiguous object, distinguish the scopes, narrow the claim or keep only a conditional application. Do not average incompatible definitions. A source being prominent does not make it relevant.

## Inspect the actual relationship

Every non-Practice Core object has `source_alignment`: a Reference ID, relation and passage locator. The allowed relations describe documentation: `definition-paraphrase`, `scoped-empirical-finding`, `methodological-relationship`, `standard-model-subset`, and `published-procedure-summary`. They are not formal SKOS mappings and do not imply exact equivalence.

For an adapted Method, `published-procedure-summary` describes the located published operation being summarized, not an assertion that every local step appears there. Explain the adaptation separately in the body. Do not use that relation for an unsupported proposal or a source that supplies no procedural or analytical operation. No new alignment relation or automated judgment of methodological quality is introduced.

A Reference records edition/date, URL, inspection extent, contribution and nonclaims. Summaries keep the needed meaning locally; links let a reader inspect provenance. An inaccessible passage is an evidence limit, not permission to fill it from memory. Multiple citations repeating one source are not independent evidence.

## What the tests establish

The alignment tests check declared relationships, locators, valid targets and the completed migration of retired files. They cannot establish that the paraphrase is faithful, the source is authoritative for the claim, or the evidence is sufficient. Read the actual passages and preserve disagreement before refreshing fingerprints.

## Boundary examples

- SKOS defines concepts and mapping relations; it does not define KPS's five roles.
- PROV describes production history; it does not certify truth.
- PICO and study extraction retain their intervention-review context. A document-improvement analogy is labelled in a Practice.
- PDCA is documented by ASQ. KPS's release process is our application, not an ASQ certification.
- Retrieval findings do not validate the folder structure or guarantee general superiority.

The [migration record](migration.md) identifies the location of each retired local object. The [source review](source-review.md) records what was inspected for this edition.
