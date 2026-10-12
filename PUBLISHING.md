---
package_version: "10.0.0"
language: "KPS 9.x"
reviewed: "2026-10-12"
---

# Publish a permitted knowledge change

## Key takeaway

Use one checked change and one history record rather than a chain of dependent publication tasks.

## Summary

This is a local publication policy, not a scientific Method. The complete task guidance is in [Build domain knowledge](practices/build-domain-knowledge.md#stage5-check-and-release). GitHub records the work; it does not determine the knowledge.

## Existing repository

1. Inspect the current main branch, existing license and open work before editing. Preserve unrelated changes.
2. Complete the requested knowledge change, review source fidelity and run `python validate.py .`, `python test_validate.py`, and the Core curation checks `python test_alignment.py`.
3. Create one branch and one ready-for-review PR against main. Confirm that its diff equals the reviewed change.
4. Check CI against the actual PR head. Merge automatically only when the owner has authorized it and the checks pass; otherwise leave the PR for the owner.
5. Confirm the result on main. Report the actual PR, checks and merge status. Do not create tags or official releases unless requested.

## No corresponding repository

Produce a complete ZIP with a checksum manifest. Extract and validate it independently before providing it. Do not modify an unrelated repository or claim that a ZIP was published on GitHub.

## Review boundaries

Preserve private records, publication rights and the existing [license](LICENSE). A source-linked paragraph is not permission to redistribute its full publication. The package contains Reference records, not downloaded articles. No sibling domain changes are implied by a Core release.

[Compatibility](COMPATIBILITY.md) explains content, language and checker versions. [Review](REVIEW.md) and [Checks](CHECKS.md) separate content judgment from structural tests.
