---
package_version: "10.1.0"
language: "KPS 9.x"
reviewed: "2026-10-12"
---


# AI contribution guidance

## Key takeaway
AI-assisted contributors must follow docs/authoring.md and preserve the difference between source evidence, inference and design choice.

## Summary
AI-assisted contributors must follow docs/authoring.md and preserve the difference between source evidence, inference and design choice.

## Governing contract
Read [docs/authoring.md](docs/authoring.md) before making any change. This file is only a quick pointer for automated assistants; it is **not** a second KPS authoring specification.

## Work method
Inspect the target file, its direct dependencies, and the local evidence. Identify what the change is supposed to improve. Write the smallest independently understandable change. Do not invent observed tests, source inspection, human approvals, repository access, expert support, or performance results. When source evidence is insufficient, state the limit or leave a candidate claim provisional.

## Knowledge constraints
An explanatory Principle must not be rewritten as a command. Models must represent actual relationships. Methods must explain a rationale and a checkable operation. Practices must contain substantive inline stages with `Stage1` names and valid links. References describe external publications and their located contributions rather than becoming summaries of author preferences.

## Verify
Run `python validate.py .` and `python test_validate.py`; review summary dependencies before any refresh. Passing structural tests is not evidence that the material is scientifically correct.

## Practice editing
Write actions first, preserve prerequisites and interpretation, and add examples or visuals only where they improve use. Do not recreate the six-label stage form or optimize prose to a word-count threshold. Inspect `docs/review.md` as well as the structural checker. Never report a self-review as an independent reader trial.

## Source grounded Core editing

Apply docs/alignment.md: verify meaning against the located source, retain uncertainty and name adaptations. Place local workflows in Practices. Run `python test_alignment.py` as well as the structural suite. User-authorized auto-merge is allowed after CI; do not require another approval already supplied. Never disable checks or overwrite unrelated changes to force publication.

## Diagrams

Use D2 selectively for explanatory value. Read the owning text and cited source before drawing; keep edge meanings and limitations explicit. Never edit generated SVGs independently. For a metadata graph, change only justified document metadata and regenerate. Run diagram tests and render checks, but report a visual self-review separately from an independent reader trial. Keep source and SVG together and retain useful alternative text and nearby explanation.
