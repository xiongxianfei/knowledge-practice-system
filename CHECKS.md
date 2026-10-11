---
package_version: "9.1.0"
language: "KPS 9.x"
reviewed: "2026-10-11"
---

# KPS 9 1 0 verification record

## Key takeaway

The checks verify publication structure and specific regression behavior, not factual truth or independent reader comprehension.

## Summary

The steps-first revision preserves 45 core objects and adds two Reference records. All four Practices were rewritten with their 17 existing stage names retained. The local baseline tree exactly matched fetched GitHub main at commit `60972c57199ae8bc21d4b7a00ac55552b4105277` before editing.

## Checks actually run

| Check | Result |
|---|---|
| Current source structure | 74 Markdown documents, 423 local links, 138 typed relationships |
| Core objects and References | 45 objects and 10 Reference records |
| Practice navigation | 17 stages, consecutive names and resolvable stage maps |
| Regression suite | 52 tests passed |
| Independent local rendering | All 752 heading identifiers matched Pandoc GFM output |
| Backward acceptance | The complete previous 9.0.1 source package passed the 9.1 checker |
| Dependency review | 14 affected recipients inspected before refreshing fingerprints |

The regression suite retains the prior integrity checks and covers steps without repeated labels, concise stages, decision tables, conditional branches, rejected link-only or absent actions, fenced examples, local image targets, image warnings, minimum checker declarations and Git/cache exclusion. The old label test was changed to test actual inline actions; no manifest or link test was removed.

## Content review performed

This was an author self-review and paper walk-through, not an independent usability trial. The link-repair case was followed through question, candidate repair, structural result, viewer check and qualified record. Domain-building and review workflows were inspected for missing prerequisites, fabricated outcomes and instructions outsourced to links. Inline diagrams and decision tables were compared with their surrounding steps. No actual personal use result was filled in.

Affected dependencies included the Practice definition, the four Practices, the local-completeness and navigation Methods, and their current consumers. Their remaining scope and meaning were checked; unrelated scientific claims were not revalidated. Source access performed for this change is recorded in [SOURCE-REVIEW.md](SOURCE-REVIEW.md).

## Scope and limits

The checker recognizes a limited Markdown/YAML profile. An action-shaped list or table can still contain poor instructions; syntactic acceptance is not semantic approval. Missing local image destinations are errors. Empty text alternatives and remote-image dependencies are warnings requiring review. No image renderer, accessibility-conformance audit, live website test, external URL crawl or field-effectiveness trial was performed.

No sibling domain repository is migrated. CI state, PR identity and merge state must be verified from GitHub when publishing; this file does not predeclare them.

## Reproduce

```bash
python validate.py .
python test_validate.py
```

For a prepared ZIP containing `MANIFEST.sha256`, also run `python validate.py . --manifest` after extracting it. Release manifests are generated artifacts, not mandatory source-repository bookkeeping. [REVIEW.md](REVIEW.md) describes the separate content review.
