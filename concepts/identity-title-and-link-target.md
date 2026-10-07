---
id: "kps:c:identity-title-and-link-target"
type: "concept"
version: "9.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored design with claim-specific basis; not an effectiveness trial"
confidence: "provisional application"
references: []
---

# Identity title and link target

## Key takeaway
An object ID, its reader-facing title, its position in a Practice and its navigable location are different things.

## Summary
An ID denotes an object under a local identity convention. A title explains meaning. A file path locates a document. A heading-derived fragment locates a section for the chosen renderer. None automatically creates another. Separating these prevents a code such as TI-03 from masquerading as a meaningful title or a working anchor.

## Definitions and example
For a Practice, `id: "swim:pr:self-coach-breaststroke"` is metadata. A stage headed `## Stage3 Kick preparation and completion` has the conventional fragment `#stage3-kick-preparation-and-completion`. The ID does not supply that fragment. Stage3 tells the reader the current recommended position, not that the stage is always third or can be performed safely.

## Why the distinction matters
Inserting a stage changes later ordinal headings and therefore their fragments. It need not change the identity of the whole Practice. Renaming a file requires path repair even when its ID is unchanged. A useful historical record names the Practice version and semantic stage, not just a number.

## Boundary
Do not create separate global object IDs for every paragraph. KPS does not require section-level identity; a file path, meaningful heading and version often suffice. Whole-file links are preferable when a specific section is not the real target.

## Evidence and limits
GitHub describes heading-derived section links and repair after edits. It does not define KPS object identity. YAML, StageN titles and the identity convention are this project's design decisions. See [GitHub documentation](../references/github-undated-markdown-formatting.md).

## Deeper knowledge
[Document navigation model](../models/document-navigation-model.md); [Build and check navigation](../methods/build-and-check-navigation.md); [Compatibility](../COMPATIBILITY.md).
