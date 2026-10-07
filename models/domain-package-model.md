---
id: "kps:mo:domain-package-model"
type: "model"
version: "9.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored model with attributed inputs"
confidence: "scope-dependent; see evaluation"
references: ["kps:r:prov"]
uses_principles: ["kps:p:independent-representations-can-diverge"]
uses_concepts: ["kps:c:source-and-reference", "kps:c:knowledge-object"]
perspectives: ["knowledge-representation", "evidence-reasoning"]
---

# Independent domain package model

## Key takeaway

Define this release’s filesystem and identifiers; these are implementation conventions, not explanatory Principles.

## Summary

A standalone domain has its own definitions, explanatory statements, operations and reference records. It declares the KPS language it follows but does not require paths into a sibling domain to be understood.

## Local explanatory basis

When equivalent mutable representations can be edited independently, continued agreement is not guaranteed.

## Purpose
Define this release’s filesystem and identifiers; these are implementation conventions, not explanatory Principles.

## Representation
```text
domain/
  README.md
  concepts/       # nouns and distinctions
  principles/     # declarative explanatory titles
  models/         # named representations
  methods/        # verb phrases
  practices/      # recurring goals; folders only when useful
  references/     # publication-identity records, Markdown only
```

A stable `id` lives in front matter. Names and paths can change after links are repaired. `status` means lifecycle, while `confidence` states support. `level: scientific` or `domain` belongs in metadata, not subdirectories. Perspectives are optional tags. Small evidence syntheses stay inside objects; a shared synthesis can be supporting documentation, not a sixth type.

Metadata uses YAML with JSON-compatible values in the shipped files so the optional validator needs only Python’s standard library. No application-specific wikilinks are required.

## Compatibility and independent evolution

Each package declares the major line `KPS 9.x` and records the exact tested release `9.0.0` separately. Compatibility covers knowledge roles, local-completeness expectations and this Markdown profile. It does not certify future content or test unissued releases. Compatible minor updates may clarify or extend optional tooling without changing the required meanings. A breaking semantic change needs a new language major. Domain content can evolve independently while this contract holds. No sibling files are needed for reading or checking a package.

## Assumptions
The package is readable by itself. Local links resolve inside its own directory. Remote URLs appear in reference records; local files link to them.

## Implications
Root index, release, checks and templates are supporting files. No new dependency on a separate KPS install is needed for ordinary reading.

## Evidence and evaluation
This is the selected storage design. Validate links and use it on a real task before asserting usefulness. [PROV-Overview](../references/w3c-2013-prov-overview.md#provenance-describes-production-history) motivates traceable identity but does not dictate filenames.

## Limits
Publication cannot ensure offline access to external sources. References may outlive URLs and require maintenance.

## Local evidence summary


[PROV-Overview](../references/w3c-2013-prov-overview.md#provenance-describes-production-history) contributes: PROV represents the origins of entities through activities and agents, enabling provenance to be exchanged.

Citation identifies support for the stated claim and scope. Any further causal or practical inference remains separately reviewable.

## Deeper knowledge

Canonical dependencies and Reference records provide additional derivation, source inspection and alternatives. They are not required to carry out the local explanation or procedure.

- **Concepts:** [Source and Reference](../concepts/source-and-reference.md)
- **Concepts:** [Knowledge object](../concepts/knowledge-object.md)
- **Principles:** [Independent representations can diverge](../principles/independent-representations-can-diverge.md)
- **References:** [PROV-Overview](../references/w3c-2013-prov-overview.md)
