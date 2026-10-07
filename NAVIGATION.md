---
package_version: "9.0.1"
language: "KPS 9.x"
reviewed: "2026-10-07"
---

# Practical Markdown navigation

## Key takeaway
This is a non-normative explanation of the [authoring contract](AUTHORING.md), with examples for navigation and viewer checks.

Use `## Stage1 Meaningful title` and links to the complete heading slug. A YAML ID does not create an anchor.

## Summary
This package uses one practical Markdown profile: UTF-8 files, YAML frontmatter, ordinary headings, tables, fenced examples and relative Markdown links. Headings use English letters, digits and single spaces so their conventional lowercase hyphenated targets are predictable. This is a documented authoring subset, not a universal Markdown standard or a separately generated edition for each application.

## Stage titles and order
The exact convention is `## Stage1 Breathing and air access`, followed by `Stage2`, and so on within that Practice. Numbers show recommended reading and working order. They do not replace entry prerequisites, safety conditions or a project's decision authority. Revisit stages when needed.

Link to that complete heading with `[Stage1 Breathing and air access](#stage1-breathing-and-air-access)`. A link to just `#stage1` or a metadata value does not work unless that is the complete actual heading. Stage names carry meaning; stage numbers only locate a stage in this version.

## File and fragment targets
Use `[Model](models/example-model.md)` for an entire file and append `#assumptions` only when its actual Assumptions section is the target. Paths are relative to the current file, remain inside this package and include the `.md` extension. File and heading case must match the chosen convention. No raw HTML anchor, wiki-link or special renderer plugin is required.

Within stages use bold labels such as **Goal**, **Why**, **Procedure**, **Success signal** and **Next**. Do not create several identical Summary or Procedure headings with ambiguous auto-numbered anchors. Examples inside fenced code blocks are demonstrations, not live link destinations.

## Renaming and reordering
A change from Stage3 to Stage4 changes the conventional heading fragment. Update the stage map, all incoming local links and any summary-dependency records together. Record the stage name and Practice version in real application records rather than only an ordinal. Outside links into old releases cannot be repaired by the new archive; keep an old release when such historical navigation matters.

## A small click test
Follow [the destination below](#navigation-test-destination), [the package summary](README.md#summary), then use the reader's back command. This checks the actual viewer rather than merely trusting a parser.

## Navigation test destination
This is the local target. [Return to the click test](#a-small-click-test).

## Validation and limits
Run `python validate.py . --manifest`. This checks the authored subset, real target files and heading fragments, not a complete implementation of every Markdown dialect. CHECKS.md records the independent local rendering performed for this release. No live website or desktop application is certified by a local parse. A plain Markdown processor is not required to generate IDs at all; choose a viewer supporting conventional heading links.

## Basis
GitHub's documentation describes lowercasing headings and hyphenating spaces, as well as the need to repair links after heading edits. MkDocs supports YAML and document-relative Markdown links; its published paths may differ from source paths. These support the profile's syntax choices, not a guarantee about all viewers. See [GitHub formatting](references/github-undated-markdown-formatting.md) and [Compatibility](COMPATIBILITY.md). No renderer-specific edition is distributed.
