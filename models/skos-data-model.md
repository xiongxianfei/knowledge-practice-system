---
id: "kps:model:skos-data-model"
type: "model"
version: "10.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-12"
basis_kind: "externally grounded knowledge; KPS applications are in Practices"
references: ["kps:r:skos"]
source_alignment: [{"reference": "kps:r:skos", "relation": "standard-model-subset", "locator": "Sections 3, 5, 8 and 10"}]
---

# SKOS Data Model

## Key takeaway

Concept relationships and labels are separate parts of a vocabulary representation.

## Summary

This is an explanatory subset of W3C SKOS, not a replacement ontology or an implementation of the KPS folder structure.

## Representation

```text
Concept -- prefLabel --> preferred wording
Concept -- broader --> broader concept
Concept -- related --> associated concept
Concept -- closeMatch or exactMatch --> concept in another scheme
```

`exactMatch` expresses stronger interchangeability than `closeMatch`; only the former is transitive. `broader` itself is not a transitive property. These are vocabulary semantics, not causal arrows.

## Illustrative use

Two synthetic taxonomies can use similar names but different scopes. A mapping should preserve that distinction rather than manufacture exact equivalence because the labels match.

## Assumptions and limits

Only a subset is shown. Actual SKOS data use RDF and the complete specification's constraints. Plain Markdown metadata and the diagram above do not establish conformance. KPS's file roles and dependency fingerprints are separate implementation choices described in Practices.

## Source alignment

[skos](../references/w3c-2009-skos-reference.md) — Sections 3, 5, 8 and 10. Alignment: standard-model-subset. This is a scoped explanation, not institutional endorsement or certification of KPS. The source does not define KPS file roles.
