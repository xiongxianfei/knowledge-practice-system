---
id: "kps:mo:document-navigation-model"
type: "model"
version: "9.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored design with claim-specific basis; not an effectiveness trial"
confidence: "provisional application"
uses_concepts: ["kps:c:identity-title-and-link-target"]
uses_principles: ["kps:p:navigation-depends-on-rendering-conventions"]
references: []
---

# Document navigation model

## Key takeaway
A working section link requires a real file, a real heading and a fragment matching the chosen rendering convention.

## Summary
This model separates logical identity from the source-document navigation used by the practical Markdown profile. It explains where links can fail and why numbering or renaming is a document-wide maintenance operation rather than a cosmetic edit.

## Elements
The source file owns one meaningful title and its section headings. YAML records object identity and language compatibility. A local Markdown link contains an optional relative path and optional heading fragment. The viewer maps headings to HTML IDs. External source URLs are a separate form of reference and are not local section targets.

## Representation
```text
source path -> target file -> actual heading -> conventional fragment
metadata ID -> logical identity only
StageN -> recommended position in this Practice version
```
For `## Stage1 Bound the task`, this profile uses `#stage1-bound-the-task`. ASCII words, digits and single spaces avoid many slug differences. Duplicate headings and custom anchors are excluded from this authored subset.

## Failure cases
A path can point outside the package, a renamed file may no longer exist, a stage may be renumbered while its incoming link remains unchanged, or a metadata ID may be mistaken for an anchor. Passing a local link test still does not establish readable content or a functioning published website.

## Assumptions and predictions
The viewer supports ordinary relative Markdown links and conventional heading IDs. A stage rename should invalidate unrepaired incoming fragments. A language major match should not conceal a different slug convention. A plain Markdown parser without heading IDs falls outside this navigation assumption.

## Evaluation and limits
The checker compares source links with real headings. Independent local rendering checks the same targets using another implementation. A click test in the actual viewer remains necessary; there is no universal Markdown-fragment standard asserted here. GitHub documents the section-link behavior; MkDocs documents YAML and source-relative links. [GitHub](../references/github-undated-markdown-formatting.md); [MkDocs](../references/mkdocs-undated-writing-your-docs.md).

## Deeper knowledge
[Identity title and link target](../concepts/identity-title-and-link-target.md); [Navigation depends on rendering conventions](../principles/navigation-depends-on-rendering-conventions.md); [Build and check navigation](../methods/build-and-check-navigation.md).
