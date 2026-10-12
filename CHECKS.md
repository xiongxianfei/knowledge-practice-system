---
package_version: "10.2.0"
language: "KPS 9.x"
reviewed: "2026-10-12"
---

# Diagram completion verification record

## Key takeaway

Source and render consistency is not evidence of reader effectiveness or scientific truth.

## Summary

The starting local tree matched GitHub main tree a6ebfcbc90d488c153d4c4e806f5a6297819c16c. The audit covers all 20 objects with 18 D2 and SVG pairs, including one retained metadata graph. All IDs, source scopes and 17 stage titles are retained.

## Reproduce

```bash
python validate.py .
python test_validate.py
python test_alignment.py
python test_diagrams.py
python test_diagram_audit.py
python diagram_tools.py --check
```

The diagram policy tests mock CLI execution. The final command separately renders every D2 source with pinned 0.9.0 and compares bytes read-only. The new audit tests check object coverage, reasons, shared sources, embeddings, source links and synthetic arithmetic.

## Content and dependencies

Owners and receiving Practice summaries were inspected for changed meaning before refreshing fingerprints. New reading guides preserve the existing limits. The spacing source was not newly accessible, which is disclosed in SOURCE-REVIEW.md. Diagrams are authored explanations, not copied source figures.

## Limits and execution status

Actual renderer and suite results appear below. The local visual review used Chromium rather than the first CairoSVG conversion, which did not correctly display the D2 styling. No independent reader trial, screen-reader audit, native GitHub browser session or scientific reanalysis is claimed. Other domain repositories are untouched.

## Preparation runner results

D2 0.9.0 rendered 18 pairs and a second read-only render comparison passed. The 52 structural, 12 alignment, 16 diagram-policy and 10 audit/example tests passed on the preparation runner. These 90 tests do not establish explanatory effectiveness. Final PR CI repeats the checks. Visual review is recorded separately after inspection.

## Author visual review

All 18 SVGs were rendered in a local Chromium engine with network access blocked. The review used contact sheets and full-size checks of the vocabulary relations and walkthrough diagram, at intrinsic size or at most 800 pixels wide. Labels, direction, branch conditions and accompanying scope statements were inspected. No clipping or unintended overlap requiring layout changes was found. The first CairoSVG conversion did not display the D2 styling correctly and was not accepted as a successful visual check.

The SVGs remain standard committed D2 output, not manually altered artwork. This is an author inspection of locally rendered diagrams, not a native GitHub browsing session, independent reader study or accessibility certification.

## Local rerun

The downloaded runner artifact SHA256 was verified and its source tree matched GitHub tree fdeeda2e2a1a2045f693292825d1b53f8201ac6b before final cleanup. After removing the temporary writer workflow and adding the audit test to the permanent read-only workflow, all 90 regression tests passed locally. A real local D2 0.9.0 rerender matched all 18 committed SVGs. All 20 previous object IDs, 17 stage titles, six previous D2 and SVG pairs, and the license were checked unchanged.
