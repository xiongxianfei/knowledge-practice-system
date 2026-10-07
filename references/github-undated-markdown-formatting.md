---
id: "kps:r:github-markdown"
type: "reference"
version: "9.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored design with claim-specific basis; not an effectiveness trial"
source_type: "official software documentation"
creator: "GitHub"
title: "Basic writing and formatting syntax"
publication_year: null
citation_year: null
updated_year: null
date_basis: "No publication date required for source identity; access date recorded separately"
url: "https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax"
accessed: "2026-10-07"
evidence_family: "GitHub documentation"
previous_access_extent: "Official HTML documentation inspected for the named sections. No installed application behavior was inferred as tested."
access_extent: "selected official HTML"
rechecked_this_release: true
current_review_date: "2026-10-07"
current_review_note: "Section links, duplicate headings, editing headings and relative links were inspected. Simple complete headings are the navigation basis; no universal Markdown fragment standard is inferred."
---

# GitHub Basic writing and formatting syntax

## Key takeaway
GitHub documents how headings become section links and how relative file links are resolved.

## Summary
This reference identifies the documented link interface used by the package. The extracted rules support the navigation profile; they do not establish that an untested application configuration behaves identically. The source remains external.


## Current inspection and use limit

Section links, duplicate headings, editing headings and relative links were inspected. Simple complete headings are the navigation basis; no universal Markdown fragment standard is inferred.


## Source identity
**Creator:** GitHub. **Title:** Basic writing and formatting syntax. **Source:** [Official documentation](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax). **Date:** undated; accessed 2026-10-07. **Inspected extent this release:** selected official HTML.

## Evidence lineage
GitHub documentation. MkDocs delegates heading generation to Python-Markdown; those two records are not independent engines.

## Generated section links
The documented section-link algorithm lowercases letters, replaces spaces with hyphens, removes other punctuation and disambiguates repeated headings. A changed heading changes the generated target.

**Locator:** Section links.

## Relative file links
Relative paths are evaluated from the current file and may include a section anchor. Metadata IDs do not automatically create such anchors.

**Locator:** Relative links and Custom anchors.

## Deeper knowledge
The external publication above gives complete documentation. [Package navigation guide](../NAVIGATION.md) explains the selected authoring profile and its limits.
