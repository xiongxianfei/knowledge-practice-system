---
package_version: "9.1.0"
language: "KPS 9.x"
reviewed: "2026-10-11"
---

# KPS 9 1 0 steps first authoring release

## Key takeaway

Core Practices become task guides rather than six-label forms; domain packages are not migrated by this change.

## Summary

This release updates the authoritative authoring contract, the four Core Practices, supporting authoring/review guidance, templates and structural tests. Stable knowledge identities, the five roles, StageN numbering and ordinary Markdown navigation remain intact.

## Content changes

The four Practices preserve their 17 stage names and replace repetitive cards with executable steps, context-specific explanations, worked examples, decision tables, text diagrams and annotated source websites. Personal working summaries remain unfilled. Two new Reference records identify narrowly used external guidance; no effectiveness claims or third-party full texts are added.

## Validation changes

The checker no longer demands six labels, the word “procedure” or a minimum stage length. It checks for an actual local action list or decision table, while retaining identity, links, stage order/maps, relationship roles, dependency review and checksum integrity. Missing local image files are errors; image text alternatives and remote-image dependencies receive diagnostic warnings for human review.

## Compatibility

KPS 9.1 accepts earlier valid stage layouts. New steps-first documents require a 9.1 checker; old 9.0 checkers reject their absent labels. Package metadata records that minimum explicitly. No Swim, Technical Insight or REM repository is changed. See [COMPATIBILITY.md](COMPATIBILITY.md).

## Publication status and history

This source change is intended for one PR against `main`, with merge according to the owner's authorization and passing checks. A generated package version is not a GitHub Release or tag. Exact executed checks and remaining limits are in [CHECKS.md](CHECKS.md). Existing scientific source records retain their prior inspection history.
