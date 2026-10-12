---
package_version: "10.1.0"
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
{"version":"10.1.0","kps_language":"9.x","validated_with":"9.1.0","minimum_validator":"9.1.0","alignment_profile":"core-established-knowledge-v1"}
```

`version` identifies this Core content release. `validated_with` names the structural authoring/checker revision actually used, not a claim that another institution approved the content. `alignment_profile` identifies this Core's additional curation policy.

## Break and migration

Old links to 41 standalone local objects no longer resolve. The four Practice IDs and all 17 stage titles are retained. Migrate incoming links deliberately using [MIGRATION.md](MIGRATION.md); a new professional definition is not automatically an exact replacement for an old local role definition.

Domain repositories declaring KPS 9.x do not have to adopt these new Core content IDs. They remain independently readable and versioned. No sibling repository is automatically rewritten. The additional alignment test applies to this Core; adoption by a domain is a separate requested change.

## Tool boundary

The structural checker and its 52 existing regressions are retained unchanged. A 9.0 checker still does not understand steps-first content. The 9.1 checker tests structure, not the truth of a source paraphrase. Format changes that alter roles or navigation still require a separate language-compatibility assessment.

## Diagram authoring in Core 10 1 0

The five knowledge roles and steps-first profile are unchanged. Ordinary Markdown readers can display local SVGs without D2. Rendering or checking source/render freshness needs D2 0.9.0; `diagram_tools.py` and `test_diagrams.py` are separate from the 9.1.0 structural validator. Older structural tools cannot claim to have checked D2 rendering. No sibling domain's metadata or checker is changed.
