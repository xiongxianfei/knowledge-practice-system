---
id: "kps:r:d2-cli"
type: "reference"
version: "10.1.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-12"
source_title: "D2 documentation on CLI SVG export and embedding"
creators: ["D2 contributors"]
source_type: "official software documentation"
publication_year: null
date_basis: "No reliable publication date for these pages; manual identifies version 0.9.0"
accessed: "2026-10-12"
access_extent: "CLI manual, SVG subsection of Exports, SVG embedding subsection of Troubleshooting; HTML inspected"
evidence_family: "d2-official-documentation"
url: "https://d2lang.com/tour/man/"
---

# D2 CLI and SVG export documentation

## Key takeaway

D2 compiles diagram source to SVG, while rendering success and correct diagram meaning remain different questions.

## Summary

The official manual describes D2 0.9.0 commands and flags. The export and troubleshooting pages explain SVG output and embedding limits. These pages inform a local publication tool choice, not a scientific claim about learning benefits or an endorsement of KPS.

## Located contributions

[CLI manual](https://d2lang.com/tour/man/) — Synopsis, exit-status warning, layout, theme, salt, bundle, version and check options. Compiler exit status must be checked even if an output file exists. Its formatting check is not a committed-image freshness check.

[Exports](https://www.d2lang.com/tour/exports/) — SVG subsection. D2 produces SVG with CSS; viewers may differ in font and CSS handling. Committing a generated SVG allows reading without installing D2, but does not establish uniform rendering everywhere.

[Troubleshooting](https://www.d2lang.com/tour/troubleshoot/) — SVG interactivity when embedded as an image. KPS therefore retains ordinary Markdown navigation outside diagrams.

## Limits and independence

All three pages are one official documentation family, not independent evidence of effectiveness. KPS's file locations, selective diagram choices, metadata graph, captions and automated byte comparison are our application decisions. Only the stated HTML sections were inspected; no complete D2 source-code audit or accessibility certification is claimed. External source publications are not bundled.
