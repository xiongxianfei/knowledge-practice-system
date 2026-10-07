---
id: "kps:me:register-reference"
type: "method"
version: "9.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored method; supporting findings separately attributed"
confidence: "proposed implementation, not independently validated"
uses_principles: ["kps:p:provenance-does-not-establish-truth", "kps:p:multiple-reports-can-share-one-evidence-base"]
uses_models: ["kps:mo:domain-package-model"]
references: ["kps:r:prov", "kps:r:cochrane"]
perspectives: ["knowledge-representation", "evidence-reasoning"]
---

# Register a reference

## Key takeaway

Identify one external work and record exactly what was inspected and used.

## Summary

Publication-based identity avoids several records for the same source merely because it supports different topics. Stable IDs preserve logical identity when titles improve. A journal paper and an author-hosted copy have one publication identity. Record both locations as alternatives, the inspected sections and date, then connect the specific claims. Do not set the publication year to the current access year.

## Inputs and prerequisites

A concrete question, the material or actual record to inspect, and enough context to distinguish observed information from a proposed interpretation. No result is assumed in advance.

## Local explanatory basis

A trace showing where a claim came from does not by itself establish that the claim is correct. The number of documents repeating a result can exceed the number of independent observations supporting it.

## Objective
Identify one external work and record exactly what was inspected and used.

## Rationale
Publication-based identity avoids several records for the same source merely because it supports different topics. Stable IDs preserve logical identity when titles improve.

## Evidence and reasoning
[PROV-Overview](../references/w3c-2013-prov-overview.md#provenance-describes-production-history) supports provenance representation. [Cochrane Handbook for Systematic Reviews of Interventions, version 6.5](../references/cochrane-2024-handbook-v6-5.md#reports-and-underlying-studies) supports grouping multiple reports; the filename convention below is our design.

## Steps
1. Locate the publisher/author record and check title, creator, publication/update date, edition, DOI or standard number where relevant. Do not replace an unknown year with the access year.
2. Name the file creator-year-short-title.md; use creator-undated-short-title.md where the date is not established. For a standard include its full issuing designation, identifier and edition year. Distinct same-year works use a fuller title or short identifier suffix.
3. Check for the same DOI, publication identifier or canonical URL already in references/. Different formats of one work ordinarily share one record; different editions get separate records when their content is used.
4. Give the record an ID that remains stable if its filename changes. Record access extent: full text, selected sections, abstract, or metadata only.
5. Extract the minimal supported claim, a section/paragraph locator, what is not established, and its evidence family. A URL is not a claim locator by itself.
6. Check visible correction/retraction/version notices relevant to the work. Mark uninspected corrections or inaccessible detail as a gap, not as cleared.
7. Link the relevant knowledge file to the specific claim anchor. Leave downstream inference outside the reference record.

## Expected effect
A structured Markdown record pointing outward; no downloaded article, PDF or dataset is required.

## Validation and counterevidence
The year is attributable, the source can be identified independently of the filename, and the cited paragraph actually supports the claim. Renamed files have repaired inbound links.

## Limits
Metadata-only access cannot justify detailed content claims. Source ownership does not make every source assertion true.

## Naming examples from this package
`w3c-2013-prov-overview.md` identifies a specification overview; `mayrhofer-2023-reexamining-the-testing-effect.md` identifies a paper. Full title and authorship remain inside each record. `good-source.md`, topic-only names and `S01.md` are not the chosen convention.

## Local evidence summary


[PROV-Overview](../references/w3c-2013-prov-overview.md#provenance-describes-production-history) contributes: PROV represents the origins of entities through activities and agents, enabling provenance to be exchanged.

[Cochrane Handbook for Systematic Reviews of Interventions, version 6.5](../references/cochrane-2024-handbook-v6-5.md#reports-and-underlying-studies) contributes: Several reports can describe one underlying study; report count is therefore not study count.

Citation identifies support for the stated claim and scope. Any further causal or practical inference remains separately reviewable.

## Publication versus inspection

Keep the publication identity stable while documenting the inspected chapter, passage or abstract. An author-hosted copy is an alternative host of the same work, not corroboration. Record known errata with that publication. Distinguish original publication date from update date and access date; a current copyright footer is not a publication year. The local contribution must identify the claim, not merely the broad topic.

## Deeper knowledge

Canonical dependencies and Reference records provide additional derivation, source inspection and alternatives. They are not required to carry out the local explanation or procedure.

- **Principles:** [Provenance does not establish truth](../principles/provenance-does-not-establish-truth.md)
- **Principles:** [Multiple reports can share one evidence base](../principles/multiple-reports-can-share-one-evidence-base.md)
- **Models:** [Independent domain package model](../models/domain-package-model.md)
- **References:** [PROV-Overview](../references/w3c-2013-prov-overview.md)
- **References:** [Cochrane Handbook for Systematic Reviews of Interventions, version 6.5](../references/cochrane-2024-handbook-v6-5.md)
