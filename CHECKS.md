---
package_version: "10.0.0"
language: "KPS 9.x"
reviewed: "2026-10-12"
---

# Professional alignment verification record

## Key takeaway

Mechanical checks verify the publication and migration declarations, not the truth or authority of a claim.

## Summary

Core 10.0.0 replaces 41 local standalone objects with a smaller externally aligned library and moves their KPS-specific responsibilities into four Practices. The starting source tree matched GitHub main at `ff0d546d07cd880c743b9cec170bfb53f2263f21`, tree `46d0198be19cd849d44a75cdf6ab3a169d293f91`.

## Checks actually run

The unchanged 9.1 structural checker validates stages, local links, typed references, dependency records and manifest integrity. All 52 structural regression tests passed. All 12 new alignment and migration tests passed. Final computed counts are recorded in `verification.json`; that file records the local verification, not future GitHub state.

The curation tests require a declared reference, relationship and source locator for each non-Practice object. They reject missing or incompatible declarations, preserved retired objects and invalid migration targets. They do not inspect a remote passage or decide whether it supports the prose.

## Content review performed

Author self-review compared the new summaries with their located passages and retained scope. SKOS and PROV are identified subsets, PICO and data extraction retain the intervention-review context, PDCA and cognitive walkthrough keep their procedural purpose, and learning findings retain study boundaries and uncertainty. The duplicate-extraction requirement is not reduced to a generic suggestion. Source access is recorded in [Source review](SOURCE-REVIEW.md).

Each former object's useful KPS responsibility was assigned to a real Practice stage and inspected there. The four Practices retain all 17 original stage titles. New local reasoning, record structures, publication decisions and adaptations are explicitly application knowledge. [Migration](MIGRATION.md) provides the full accounting.

## Scope and limits

This is an author self-review and structural test suite, not an independent usability trial, systematic evidence review, professional certification or institutional endorsement. No real personal-learning result was recorded. Existing scientific inspection history is not claimed as new research. No sibling domain repository is migrated.

## Reproduce

```bash
python validate.py .
python test_validate.py
python test_alignment.py
```

For an extracted ZIP with a generated manifest, also run `python validate.py . --manifest`. The living source tree does not need an archive manifest. GitHub CI and merge status must be verified separately at publication time.
