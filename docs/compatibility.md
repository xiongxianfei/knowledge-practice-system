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
{"version":"11.0.0","kps_language":"9.x","validated_with":"9.1.0","minimum_validator":"9.1.0","alignment_profile":"core-established-knowledge-v1"}
```

`version` identifies this Core content release. `validated_with` names the structural authoring/checker revision actually used, not a claim that another institution approved the content. `alignment_profile` identifies this Core's additional curation policy.

## Break and migration

Old links to 41 standalone local objects no longer resolve. The four Practice IDs and all 17 stage titles are retained. Migrate incoming links deliberately using [MIGRATION.md](history/10.0.0-migration.md); a new professional definition is not automatically an exact replacement for an old local role definition.

Domain repositories declaring KPS 9.x do not have to adopt these new Core content IDs. They remain independently readable and versioned. No sibling repository is automatically rewritten. The additional alignment test applies to this Core; adoption by a domain is a separate requested change.

## Tool boundary

The structural checker and its 52 existing regressions are retained unchanged. A 9.0 checker still does not understand steps-first content. The 9.1 checker tests structure, not the truth of a source paraphrase. Format changes that alter roles or navigation still require a separate language-compatibility assessment.

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
| `SOURCE-REVIEW.md`, `MIGRATION.md`, `RELEASE.md`, `CHECKS.md` | `docs/history/` (versioned historical records) |
| `diagram_tools.py`, `test_*.py` | `internal/diagram_tools.py`, `internal/tests/` |
| `diagrams.json`, `diagram-audit.json` | `diagrams/manifest.json`, `diagrams/audit.json` |
| `summary-dependencies.json`, `transition.json` | `internal/metadata/` |
| `verification.json` | `docs/history/10.1.0-verification.json` |

The public command `python validate.py .` stays at the root. The validator recognizes both the new internal dependency snapshot location and the original root snapshot location for independent older domain packages. For the reorganized Core, run `python -m unittest discover -s internal/tests -p "test_*.py"` and `python -m internal.diagram_tools --check --root .` (D2 0.9.0 required for rendering checks). Follow the [10.0.0 historical migration record](history/10.0.0-migration.md) when resolving retired *knowledge* object identities; it is distinct from this file-layout change.

**Dependency review for this layout change:** The GitHub Markdown reference record changed only in its local Markdown link destination; its cited publication, inspected scope and claims remain unchanged. The dependent Use KPS summary was reviewed for semantic consistency before updating the snapshot fingerprint. Other source and practice relationships were preserved.
