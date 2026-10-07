---
id: "kps:r:mkdocs-writing"
type: "reference"
version: "9.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored design with claim-specific basis; not an effectiveness trial"
source_type: "official software documentation"
creator: "MkDocs"
title: "Writing your docs"
publication_year: null
citation_year: null
updated_year: null
date_basis: "No publication date required for source identity; access date recorded separately"
url: "https://www.mkdocs.org/user-guide/writing-your-docs/"
accessed: "2026-10-07"
evidence_family: "Python-Markdown implementation lineage"
previous_access_extent: "Official HTML documentation inspected for the named sections. No installed application behavior was inferred as tested."
access_extent: "selected official HTML"
rechecked_this_release: true
current_review_date: "2026-10-07"
current_review_note: "Heading links, relative Markdown file links and YAML metadata documentation were inspected. No installed MkDocs website or custom theme was tested."
---

# MkDocs Writing your docs

## Key takeaway
MkDocs describes source-relative Markdown links, generated output paths and heading anchors supplied by its Markdown extensions.

## Summary
This reference identifies the documented link interface used by the package. The extracted rules support the navigation profile; they do not establish that an untested application configuration behaves identically. The source remains external.


## Current inspection and use limit

Heading links, relative Markdown file links and YAML metadata documentation were inspected. No installed MkDocs website or custom theme was tested.


## Source identity
**Creator:** MkDocs. **Title:** Writing your docs. **Source:** [Official documentation](https://www.mkdocs.org/user-guide/writing-your-docs/). **Date:** undated; accessed 2026-10-07. **Inspected extent this release:** selected official HTML.

## Evidence lineage
Python-Markdown implementation lineage. MkDocs delegates heading generation to Python-Markdown; those two records are not independent engines.

## Source paths and output rewriting
Links to Markdown documents should use source-relative paths. MkDocs rewrites these for the generated site; section fragments are retained.

**Locator:** Linking to pages.

## Heading generation
MkDocs uses the Python-Markdown Table of Contents extension for generated heading identifiers. Nondefault extensions can change behavior.

**Locator:** Linking to headings.

## Homepage naming
README.md can serve as an index page when no competing index.md is present.

**Locator:** Index pages.

## Scope and nonclaims
The record does not certify a particular theme, plugin, custom slug function or local MkDocs installation. This package is documentation input, not a deployed site.

## Deeper knowledge
The external publication above gives complete documentation. [Package navigation guide](../NAVIGATION.md) explains the selected authoring profile and its limits.
