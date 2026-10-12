---
package_version: "10.2.0"
language: "KPS 9.x"
reviewed: "2026-10-12"
---

# Knowledge Practice System

## Key takeaway

Apply source-aligned professional knowledge through locally usable, task-oriented Practices. Keep KPS-specific choices distinct from externally established meanings.

## Summary

KPS Core contains 20 knowledge objects (five Concepts, four Principles, two Models, five Methods and four Practices) plus 18 external Reference records. This working layout separates the knowledge library, authoring guidance, maintenance tools and historical records.

## Start with the task

- [Use KPS](practices/use-kps.md) — answer one bounded question.
- [Build domain knowledge](practices/build-domain-knowledge.md) — turn evidence into usable knowledge.
- [Improve KPS](practices/improve-kps.md) — pilot an improvement on real content.
- [Review and learn](practices/review-and-learn.md) — retain justified observations and conclusions.

Browse the [knowledge library](docs/library.md) for Concepts, Principles, Models, Methods, References, and a small dependency map.

## For authors and maintainers

The [authoring contract](docs/authoring.md) governs structure; the [Core source-alignment policy](docs/alignment.md) distinguishes professional knowledge from KPS-specific applications. See [templates](docs/templates.md), [reader review](docs/review.md), [diagram authoring](docs/diagrams.md), and [compatibility and migration](docs/compatibility.md). [Contributing](.github/CONTRIBUTING.md) describes project decisions and publication.

## Validate

From the repository root:

```bash
python validate.py .
python -m unittest discover -s internal/tests -p "test_*.py"
python -m internal.diagram_tools --check --root .
```

The D2 rendering check requires the pinned version documented in [diagram authoring](docs/diagrams.md). Structural checks do not certify scientific validity or reader usability. The [10.2.0 release record](docs/history/10.2.0-release.md) preserves historical verification.

## Scope and rights

KPS uses one source-aligned Core library, locally usable Practices, and linked external publications rather than bundled third-party full texts. Source records preserve inspection limits. KPS-authored content and tools use the [MIT License](LICENSE); third-party publications retain their own rights.
