---
id: "kps:p:navigation-depends-on-rendering-conventions"
type: "principle"
version: "9.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored design with claim-specific basis; not an effectiveness trial"
confidence: "provisional application"
level: "domain"
references: ["kps:r:github-markdown", "kps:r:mkdocs-writing"]
---

# Navigation depends on rendering conventions

## Key takeaway
Valid Markdown link syntax does not by itself establish that its fragment names a destination produced by a viewer.

## Summary
A heading is source text; an anchor is a rendering result. Different conventions can map the same text differently or generate no anchor. Consequently a readable link can still fail, even when the file exists.

## Statement and explanation
Navigation works when the reference's target agrees with the destination that is actually created. A YAML object ID records logical identity but does not normally create a section destination. Changing a heading can alter its fragment without changing the logical object.

## Example
A link to `#ti-03` does not reach `## Stage3 Build the explanatory model` under this package's convention. The expected target is the whole normalized heading. Likewise, Stage3 becoming Stage4 changes that target.

## Evidence and synthesis
GitHub documents lowercasing, space substitution and duplicate-heading suffixes; MkDocs and its Python-Markdown implementation expose heading and path processing. These are implementation descriptions, not independent experiments. Their overlap motivates a conservative single profile; it cannot establish behavior for every renderer. [GitHub](../references/github-undated-markdown-formatting.md); [MkDocs](../references/mkdocs-undated-writing-your-docs.md); [Python Markdown](../references/python-markdown-undated-toc-extension.md).

## Applications and limits
This relationship supports real-target validation, conservative headings or a different deliberately chosen publishing contract. It does not demand one brand of application or a second edition. A site with different processing must be checked in its own environment.

## Deeper knowledge
[Document navigation model](../models/document-navigation-model.md); [Build and check navigation](../methods/build-and-check-navigation.md).
