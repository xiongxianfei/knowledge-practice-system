---
package_version: "9.0.1"
language: "KPS 9.x"
reviewed: "2026-10-07"
---

# AI contribution guidance

## Key takeaway
AI-assisted contributors must follow AUTHORING.md and preserve the difference between source evidence, inference and design choice.

## Summary
AI-assisted contributors must follow AUTHORING.md and preserve the difference between source evidence, inference and design choice.

## Governing contract
Read [AUTHORING.md](AUTHORING.md) before making any change. This file is only a quick pointer for automated assistants; it is **not** a second KPS authoring specification.

## Work method
Inspect the target file, its direct dependencies, and the local evidence. Identify what the change is supposed to improve. Write the smallest independently understandable change. Do not invent observed tests, source inspection, human approvals, repository access, expert support, or performance results. When source evidence is insufficient, state the limit or leave a candidate claim provisional.

## Knowledge constraints
An explanatory Principle must not be rewritten as a command. Models must represent actual relationships. Methods must explain a rationale and a checkable operation. Practices must contain substantive inline stages with `Stage1` names and valid links. References describe external publications and their located contributions rather than becoming summaries of author preferences.

## Verify
Run `python validate.py .` and `python test_validate.py`; review summary dependencies before any refresh. Passing structural tests is not evidence that the material is scientifically correct.
