---
package_version: "11.0.0"
language: "KPS 9.x"
reviewed: "2026-10-12"
---

# Content and authoring compatibility

## Key takeaway

A content-library break is not the same as a language or checker change.

## Summary

Core 10.0.0 removed prior Core object IDs and filenames; 10.1.0 adds diagrams without further identity changes. The KPS 9.x file-role language, StageN navigation and steps-first representation remain unchanged.

## Declarations

```json
{"version":"11.0.0","kps_language":"9.x","validated_with":"9.2.0","minimum_validator":"9.2.0","alignment_profile":"core-established-knowledge-v1"}
```

`version` identifies this Core content release. `validated_with` names the structural authoring/checker revision actually used, not a claim that another institution approved the content. `alignment_profile` identifies this Core's additional curation policy.

## Break and migration

Old links to 41 standalone local objects no longer resolve. The four Practice IDs and all 17 stage titles are retained. Migrate incoming links deliberately using [MIGRATION.md](migration.md); a new professional definition is not automatically an exact replacement for an old local role definition.

Domain repositories declaring KPS 9.x do not have to adopt these new Core content IDs. They remain independently readable and versioned. No sibling repository is automatically rewritten. The additional alignment test applies to this Core; adoption by a domain is a separate requested change.

## Tool boundary

Validator 9.2.0 allows Model introductory prose instead of mandatory Key takeaway and Summary headings, and checks linked Contents. Other roles keep their opening requirements. Existing Model headings may remain; add Contents when adopting this checker. A package using the flexible opening declares a minimum checker of 9.2.0. This is an explicitly adopted authoring/checker revision within KPS 9.x, not a change to the five roles or an official content release. A 9.0 checker still does not understand steps-first content. Structural checks do not establish the truth of a source paraphrase. Format changes that alter roles or navigation still require a separate language-compatibility assessment.

## Diagram authoring in Core 10 1 0

The five knowledge roles and steps-first profile are unchanged. Ordinary Markdown readers can display local SVGs without D2. Rendering or checking source/render freshness needs D2 0.9.0; `diagram_tools.py` and `test_diagrams.py` are separate from the 9.1.0 structural validator. Older structural tools cannot claim to have checked D2 rendering. No sibling domain's metadata or checker is changed.

## Core 11 0 0 repository layout migration

Core 11.0.0 consolidates overlapping root documentation and **intentionally breaks old document URLs**, as authorized. This is a layout migration rather than a change to the five KPS knowledge roles, object identities or 18 Reference records. Existing domain packages should not be rewritten merely because Core is reorganized.

| Previous location | Current location |
|---|---|
| `AUTHORING.md`, `NAVIGATION.md` | [Authoring contract](authoring.md) |
| `ALIGNMENT.md` | [Core source alignment](alignment.md) |
| `INDEX.md`, `WHY-MAP.md`, `KNOWLEDGE-MAP.md` | [Knowledge library](library.md) |
| `DIAGRAMS.md`, `DIAGRAM-AUDIT.md` | [Diagram guide](diagrams.md); [audit registry](../diagrams/audit.json) |
| `TEMPLATES.md`, `REVIEW.md` | [Templates](templates.md), [review guide](review.md) |
| `CONTRIBUTING.md`, `GOVERNANCE.md`, `PUBLISHING.md` | [Contribution and governance](../.github/CONTRIBUTING.md) |
| `CODE_OF_CONDUCT.md`, `SECURITY.md` | `.github/CODE_OF_CONDUCT.md`, `.github/SECURITY.md` |
| `SOURCE-SYNTHESIS-EXAMPLE.md` | [Worked synthesis](examples/source-synthesis.md) |
| `SOURCE-REVIEW.md`, `MIGRATION.md` | [Source inspection record](source-review.md), [identifier migration map](migration.md) |
| `RELEASE.md`, `CHECKS.md`, `verification.json` | Obsolete release reports removed; earlier versions remain in Git |
| `diagram_tools.py`, `test_*.py` | `internal/diagram_tools.py`, `internal/tests/` |
| `diagrams.json`, `diagram-audit.json` | `diagrams/manifest.json`, `diagrams/audit.json` |
| `summary-dependencies.json` | `internal/metadata/summary-dependencies.json` |
| `transition.json` | Duplicate inventory removed; the identifier map remains in [Migration](migration.md) |

The public command `python validate.py .` stays at the root. The validator recognizes both the new internal dependency snapshot location and the original root snapshot location for independent older domain packages. For the reorganized Core, run `python -m unittest discover -s internal/tests -p "test_*.py"` and `python -m internal.diagram_tools --check --root .` (D2 0.9.0 required for rendering checks). Follow the [10.0.0 historical migration record](migration.md) when resolving retired *knowledge* object identities; it is distinct from this file-layout change.

**Dependency review for this layout change:** The GitHub Markdown reference record changed only in its local Markdown link destination; its cited publication, inspected scope and claims remain unchanged. The dependent Use KPS summary was reviewed for semantic consistency before updating the snapshot fingerprint. Other source and practice relationships were preserved.

## Shared tooling maintenance

Core owns the shared structural validator and its regression tests. Domains may retain a pinned copy for independent, offline checks; a workspace sync does not upgrade those copies. Review compatibility before updating a domain's tool or contract pin. Keep domain-specific checks in the domain that owns the content.

The existing diagram tool is retained because it checks committed D2 sources against their SVGs and declared metadata. Its tests and alignment tests protect existing content contracts. Completed migration inventories, fixed release counts and versions no longer constrain the live alignment checker; the useful identifier mapping remains in [Migration](migration.md). The duplicate transition inventory and obsolete release reports are removed. Links in the retained map still undergo ordinary validation. Readers can use the Markdown and committed images without running these tools. No workspace build, sync or publication script is required.

Text uses LF line endings under `.gitattributes`, preserving exact-byte dependency fingerprints across checkouts. Restore intended line endings before interpreting a fingerprint mismatch as a content revision. This rule does not alter the checker, authoring contract or knowledge identities.

## Test ownership

Core retains the structural validator regression suite and live source-alignment and diagram checks. Domain packages validate their own files and verify their pinned copies. Older full suites remain available alongside their validators in Core Git history: `60972c57199ae8bc21d4b7a00ac55552b4105277` for the unchanged Technical Insight checker, `9432f1ee86f641d01444038cc81b7efa596b75dc` for AI Coach, and `ce17edc3ce9fa42e47b1d05740489291a3087fb6` for English and Pentest. Swim's inspected base is `8fd410d1a8dec8b3e38352c9166639906049ec55`; its local Git and manifest adaptations retain focused domain regressions. A pin change requires reviewing its matching upstream tests; a passing suite for one version does not certify another.

The test allowlist covers valid and invalid structure, links, identities and relationships, dependency changes and safe refresh behavior, provenance declarations, and existing diagram/artifact integrity. Historical inventories and arithmetic unrelated to actual repository artifacts are retired. Ordinary Markdown validation continues checking the links in migration documentation.
