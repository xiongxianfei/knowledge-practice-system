---
package_version: "10.1.0"
language: "KPS 9.x"
reviewed: "2026-10-12"
---

# Selective diagram verification record

## Key takeaway

Publication checks and rendering checks do not establish source faithfulness or independent reader comprehension.

## Summary

The starting local source tree exactly matched repository main at commit `383a7b896ca3f515bd1c6937004e5e62bad9d8c1`, tree `ad2031486b78827244e4aa604dbaa97d2d46836d`. This revision adds selective diagrams without retiring or redefining any knowledge objects.

## Checks performed

All 52 structural regression tests, 12 source-alignment/migration tests and 16 new diagram policy/failure-path tests passed locally. The diagram unit tests mock CLI execution to exercise missing/stale artifacts, changed metadata, wrong version, failed compilation and read-only behavior; they are not actual rendering tests.

Separately, D2 0.9.0 rendered all six sources on a GitHub Actions Linux runner with the fixed archive SHA-256 verified. Each SVG was rerendered and compared byte-for-byte. The generated PNG previews were inspected locally; three overly wide layouts were changed to vertical layouts and rerendered. This is author visual inspection, not an independent accessibility or usability audit.

The final repository workflow repeats actual D2 rendering and comparison under read-only permissions, alongside all three Python regression suites. The temporary asset-preparation workflow is not included in the final source tree. GitHub CI and merge status must be verified from GitHub; this record does not predeclare either.

## Content and dependency review

The Concept drawing illustrates many-to-many study/report relationships. The Principle drawing follows the stated synthetic same-participant and same-outcome example, not a universal count rule. The PROV drawing preserves the four named relation directions. PDCA retains the check-to-action feedback without promising causal proof. The Practice diagram separates failed structure, failed navigation and unavailable observation. The neighborhood has four declared use edges and explicitly excludes indirect dependencies and References.

The four Practices consuming the changed Concept, Principle, Model and Method summaries were reviewed. Their existing source meanings and application limits remain valid; only then were their dependency fingerprints refreshed. Earlier source access and empirical-learning claims were not silently revalidated. [SOURCE-REVIEW.md](SOURCE-REVIEW.md) identifies the new inspection scope.

## Reproduce

```bash
python validate.py .
python test_validate.py
python test_alignment.py
python test_diagrams.py
python diagram_tools.py --check
```

The last command requires D2 0.9.0; ordinary reading and structural tests do not. After extracting a downloadable package containing a manifest, run `python validate.py . --manifest`. [DIAGRAMS.md](DIAGRAMS.md) describes rendering and semantic review.

## Limits

No real reader trial, screen-reader test, native GitHub browser inspection, universal SVG-viewer guarantee, external-link crawl or new scientific-effectiveness assessment is claimed. Diagram byte agreement verifies source/render freshness under the pinned tool, not whether the explanation is correct. Text remains available when a viewer cannot display SVGs.
