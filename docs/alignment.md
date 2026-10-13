---
package_version: "10.0.0"
language: "KPS 9.x"
reviewed: "2026-10-12"
---

# Professional source alignment

## Key takeaway

Align the meaning first and keep the KPS application visibly separate.

## Summary

This is the Core library curation policy, not a claim that a professional body endorses KPS. Established meanings and procedures replace our former standalone local abstractions.

## Admission by knowledge role

| Role | Required basis in this Core edition | What stays in Practices |
|---|---|---|
| Concept | Located definition in a named discipline or specification | Our five file-role definitions and classification decisions |
| Principle | Scoped empirical finding or supported explanatory relationship | Our design rules, extrapolations and working hypotheses |
| Model | Identified external representation with subset and limits stated | Our package, navigation and workflow models |
| Method | Recognizable published procedure with rationale and checks | Our sequence for authoring, publishing and revising KPS |
| Practice | Explicit application synthesis with usable inline steps | The actual KPS-specific workflow belongs here |

The authoring specification remains necessary infrastructure. Removing local conventions from the knowledge library does not make a Markdown format externally standardized. The five roles remain KPS design choices, as explained in the [domain-building Practice](../practices/build-domain-knowledge.md#stage3-create-locally-complete-objects).

## Select authority for the claim

Use defining specifications for their terms and relations, procedural publications for their named techniques, and applicable empirical work for effects. A standards body does not prove a learning benefit by defining a format. An experiment does not prescribe the KPS directory layout. An official software page can document a navigation convention without establishing human comprehension.

Where authorities differ, retain the source vocabulary and scope. Rename an ambiguous object, distinguish the scopes, narrow the claim or keep only a conditional application. Do not average incompatible definitions. A source being prominent does not make it relevant.

## Inspect the actual relationship

Every non-Practice Core object has `source_alignment`: a Reference ID, relation and passage locator. The allowed relations describe documentation: `definition-paraphrase`, `scoped-empirical-finding`, `methodological-relationship`, `standard-model-subset`, and `published-procedure-summary`. They are not formal SKOS mappings and do not imply exact equivalence.

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
