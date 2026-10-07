---
id: "kps:me:build-and-check-navigation"
type: "method"
version: "9.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored design with claim-specific basis; not an effectiveness trial"
confidence: "provisional application"
uses_concepts: ["kps:c:identity-title-and-link-target"]
uses_principles: ["kps:p:navigation-depends-on-rendering-conventions"]
uses_models: ["kps:mo:document-navigation-model"]
references: []
---

# Build and check navigation

## Key takeaway
Build links from actual destination headings and validate them after every rename or stage reorder.

## Summary
Use this operation when writing or publishing a knowledge package. It maintains one practical Markdown source rather than multiple application-specific editions. A successful check establishes destinations under the declared profile, not content truth or universal viewer compatibility.

## Objective and inputs
Inputs are the destination files, their actual headings, the package root and the selected practical Markdown profile. The output is a navigable package and an honest record of tests. The reader can perform the operation using a text editor and the included Python checker.

## Rationale
An identifier is a label, not a rendered anchor. A numbered heading carries its number into its conventional slug, so insertion can change several targets. Writing a link first and assuming its destination exists leaves an invisible dependency error.

## Procedure
1. Keep a meaningful file title and YAML ID separate. Use relative lowercase kebab-case filenames for knowledge files.
2. Number executable stages `Stage1`, `Stage2` and so on. State that these numbers are recommended order, while prerequisites and stop conditions control entry.
3. Make section headings unique and use simple words, digits and single spaces. Use bold labels for repeated stage fields.
4. Derive the fragment from the complete actual heading by lowercasing and replacing spaces with hyphens. Use a whole-file link where no specific section is needed.
5. On reordering, repair the stage map and all incoming local fragments. A metadata ID or old sequence code cannot substitute for the heading.
6. Run `python validate.py .` and resolve missing files, fragments and inconsistent stage maps. Read a representative page in the intended viewer and click both a same-file and cross-file link.
7. Freeze the reviewed release and manifest. Record which renderer was actually exercised and what remains untested.

## Worked example
Heading `## Stage3 Build the explanatory model` is linked by `[Build the explanatory model](#stage3-build-the-explanatory-model)`. If it becomes Stage4, repair every incoming fragment. A link to `#ti-03` is wrong unless a real allowed heading generates exactly that target.

## Expected effect and counterevidence
A reader reaches the named section without decoding an internal code. A missing target, wrong landing position, viewer without heading IDs or a stale stage map counts against completion. Parser agreement alone does not prove that the real application behaves the same.

## Limits and evidence
This is an authored maintenance Method. The chosen subset is informed by [GitHub heading links](../references/github-undated-markdown-formatting.md), [MkDocs source handling](../references/mkdocs-undated-writing-your-docs.md) and [Python Markdown heading generation](../references/python-markdown-undated-toc-extension.md), not a universal syntax guarantee.

## Deeper knowledge
[Document navigation model](../models/document-navigation-model.md); [Navigation guide](../NAVIGATION.md); [Compatibility](../COMPATIBILITY.md).
