---
package_version: "9.0.1"
language: "KPS 9.x"
reviewed: "2026-10-07"
---

# Knowledge Practice System

## Key takeaway
Build locally understandable and evidence-aware knowledge, connect it through explicit reasoning, and compose it into Practices usable in real work.

## Summary
Build locally understandable and evidence-aware knowledge, connect it through explicit reasoning, and compose it into Practices usable in real work.

## What is KPS
KPS is an open-source, self-describing architecture for organising reusable knowledge and applying it in real situations. It uses five **knowledge roles** and structured **Reference records**. The roles are a design convention, not a proven universal taxonomy.

| Role | What it contributes |
|---|---|
| [Concept](concepts/concept.md) | A useful distinction or definition |
| [Principle](concepts/principle.md) | A scoped, declarative explanation; **not a rule or command** |
| [Model](concepts/model.md) | A representation of relationships, assumptions and behavior |
| [Method](concepts/method.md) | An operation, its rationale, how to perform it, and how to assess it |
| [Practice](concepts/practice.md) | Self-contained stages for pursuing a recurring real-world goal |
| [Reference](concepts/source-and-reference.md) | A record identifying an external publication and what it supports |

`references/` is supporting provenance infrastructure—not a sixth knowledge type. KPS describes itself using its own structure. **Validation checks structure, not the factual truth or proven effectiveness of the framework.**

## Start here
1. [Use KPS](practices/use-kps.md) to start from one real knowledge question.
2. [Build a domain knowledge package](practices/build-domain-knowledge.md) to organise a domain with the five roles.
3. [Read the authoring contract](AUTHORING.md) before changing the structure, stage titles, relationships or Markdown conventions.
4. [Use the templates](TEMPLATES.md) as examples and [run the checks](CHECKS.md) before opening a contribution.

**One guiding standard:** every file should be locally understandable at its own abstraction level. Links deepen evidence and reasoning; they do not replace the explanation a reader needs right now.

## Browse the knowledge
- [Knowledge index](INDEX.md) connects files by kind.
- [Method to reason map](WHY-MAP.md) traces Methods back to explanations.
- [Source synthesis example](SOURCE-SYNTHESIS-EXAMPLE.md) distinguishes a source finding from our inference.
- [Navigation examples](NAVIGATION.md) explain ordinary Markdown heading fragments.

## Repository layout
```text
concepts/       reusable definitions and distinctions
principles/     explanatory statements with scope, evidence and limits
models/         structural or behavioral representations
methods/        operations with rationale and validation
practices/      staged operational syntheses
references/     structured records of external sources
validate.py     structural checker
AUTHORING.md    authoritative Markdown authoring contract
```

## Knowledge integrity
Principles are not normative rules. A source's publication prestige does not establish its relevance to a particular claim. Claim-driven source synthesis should distinguish directly supported premises, author inference, disagreement and limits. Practice examples and unperformed checks must not be presented as observed outcomes.

## Contribute
KPS welcomes corrections, more defensible explanations, improved Methods, new worked examples and validator improvements. Please read [Contributing](CONTRIBUTING.md) and [Governance](GOVERNANCE.md). For problems, use the issue templates; for changes, open a pull request with the relevant evidence and validation result. Respect the [Code of conduct](CODE_OF_CONDUCT.md).

## Version and compatibility
This open-source repository edition is **9.0.1**, based on the KPS 9.0.0 knowledge release. Domain projects can declare **KPS 9.x** compatibility while versioning their own content independently. Read [Compatibility](COMPATIBILITY.md) and [Release notes](RELEASE.md). No future release has been automatically validated.

## License
**MIT License** for the KPS-authored documentation and tooling, subject to the rights of their respective authors. Third-party publications remain under their own terms; KPS Reference records describe and link to them without bundling copies. Review [LICENSE](LICENSE) and the [reference register](references/README.md) before republishing any external material.

## Scope
KPS is an authored framework for organizing reasoning. It is not a scientific certification, medical protocol, software security guarantee or engineering conformance standard. Domain implementations must assess their own risks.
