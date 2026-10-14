---
package_version: "11.0.0"
language: "KPS 9.x"
reviewed: null
---

# Knowledge Practice System

## Key takeaway

Apply source-aligned professional knowledge through locally usable, task-oriented Practices. Keep KPS-specific choices distinct from externally established meanings.

## Summary

KPS Core contains 20 knowledge objects (five Concepts, four Principles, two Models, five Methods and four Practices) plus 22 external Reference records. Core 11.0.0 reorganizes repository documentation and tooling without changing those knowledge identities. The layout separates the knowledge library, authoring guidance, maintenance tools and historical records.

![KPS connects knowledge and understanding, inquiry and evidence, representation and organization, synthesis and communication, learning and capability, practical reasoning and action, and experience and knowledge development around the purpose of understanding, applying and investigating](diagrams/body-of-knowledge-overview.png)

Explore the [Body of Knowledge Outline](docs/body-of-knowledge-outline.md) for required understanding, capabilities and gaps. [Open the illustration at full size](diagrams/body-of-knowledge-overview.png). It presents connected subject areas, not a fixed sequence or a claim that every topic is already covered.

## Explore by subject

The [KPS Body of Knowledge Outline](docs/body-of-knowledge-outline.md) connects seven areas and 34 topics: knowledge and understanding; inquiry and evidence; representation and organization; synthesis and communication; learning and capability; practical reasoning and action; experience and knowledge development. Start with its [overall outline](docs/body-of-knowledge-outline.md#overall-outline), then explore topic outcomes, source basis and gaps.

## Start with the task

- [Use KPS](practices/use-kps.md) — answer one bounded question.
- [Build domain knowledge](practices/build-domain-knowledge.md) — turn evidence into usable knowledge.
- [Improve KPS](practices/improve-kps.md) — pilot an improvement on real content.
- [Review and learn](practices/review-and-learn.md) — retain justified observations and conclusions.

Browse the [knowledge library](docs/library.md) for Concepts, Principles, Models, Methods, References, and a small dependency map.

## For authors and maintainers

The [authoring contract](docs/authoring.md) governs structure; the [Core source-alignment policy](docs/alignment.md) distinguishes professional knowledge from KPS-specific applications. See [templates](docs/templates.md), [reader review](docs/review.md), [diagram authoring](docs/diagrams.md), and [compatibility and migration](docs/compatibility.md). [Contributing](.github/CONTRIBUTING.md) describes project decisions and publication.

To define a domain's required coverage, use [Create a body of knowledge outline](docs/body-of-knowledge-outline-guide.md) and its [copyable template](docs/templates.md#body-of-knowledge-outline). The guide connects established subject structures with learner targets, Practices, gaps and summary illustrations, using singing as a worked example.

## Validate

From the repository root:

```bash
python validate.py .
python -m unittest discover -s internal/tests -p "test_*.py"
python -m internal.diagram_tools --check --root .
```

The D2 rendering check requires the pinned version documented in [diagram authoring](docs/diagrams.md). Structural checks do not certify scientific validity or reader usability. Record actual command results in the change PR; [source inspection and review evidence](docs/source-review.md) retains its original scope.

## Scope and rights

KPS uses one source-aligned Core library, locally usable Practices, and linked external publications rather than bundled third-party full texts. Source records preserve inspection limits. KPS-authored content and tools use the [MIT License](LICENSE); third-party publications retain their own rights.
