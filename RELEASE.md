---
package_version: "10.1.0"
language: "KPS 9.x"
reviewed: "2026-10-12"
---

# Core 10 1 0 change record

## Key takeaway

Add selective visual explanations without replacing source-aligned knowledge or steps-first Practices.

## Summary

Five explanatory D2/SVG pairs are embedded where they clarify a distinction, relationship, feedback loop or decision. One additional graph shows a small metadata-derived neighborhood. The release retains all 20 knowledge objects and 17 Practice stage titles, and adds one official D2 Reference for a total of 18.

## Changes

- Add D2 sources, generated SVGs, useful alternative text and nearby interpretation in the selected Concept, Principle, Model, Method and Practice.
- Document selective use in AUTHORING.md and an actionable implementation guide in DIAGRAMS.md.
- Add pinned rendering, read-only freshness checking and 16 diagram policy/failure-path tests. Keep all 52 structural and 12 alignment tests.
- Update the four affected Practice dependency snapshots after comparing their summaries against unchanged source meanings.

## Compatibility

KPS language remains 9.x and the structural checker remains 9.1.0. The D2 0.9.0 tool is required only for authoring/render verification; readers use the committed SVG and text. No new knowledge type, renderer plugin or diagram-per-file quota is introduced. Core 10.0.0's retired objects remain accounted for in MIGRATION.md and Git history.

## Publication and verification boundary

The baseline is main commit `383a7b896ca3f515bd1c6937004e5e62bad9d8c1`. [CHECKS.md](CHECKS.md) records checks actually run. GitHub publication is one PR; merge state must be verified from GitHub rather than inferred from this file. No tag, official Release, independent user trial or sibling-domain migration is implied.
