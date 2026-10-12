---
id: "kps:model:prov-data-model"
type: "model"
version: "10.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-12"
basis_kind: "externally grounded knowledge; KPS applications are in Practices"
references: ["kps:r:prov-dm"]
source_alignment: [{"reference": "kps:r:prov-dm", "relation": "standard-model-subset", "locator": "Sections 2.1, 2.2 and 5.1 to 5.3"}]
---

# PROV Data Model

## Key takeaway

Represent what was used and produced separately from who was responsible.

## Summary

This source-aligned subset helps read provenance without suggesting that a trace proves an output correct.

## Representation

```text
Activity -- used --> input Entity
output Entity -- wasGeneratedBy --> Activity
Activity -- wasAssociatedWith --> Agent
output Entity -- wasDerivedFrom --> input Entity
```

Entities have fixed aspects, activities occur over time, and agents bear responsibility. Derivation and association are not statements of scientific correctness.

## Synthetic example

A conversion activity uses an input document and generates a summary. An editor is associated with the activity. The summary can remain inaccurate despite a correctly recorded derivation.

## Assumptions and limits

The full model contains more relationships and constraints than this explanatory subset. The example is not a formal PROV-N or RDF serialization. Workflow order, file hashes and publication decisions remain KPS-specific Practice details, not requirements of PROV.

## Source alignment

[prov-dm](../references/w3c-2013-prov-dm.md) — Sections 2.1, 2.2 and 5.1 to 5.3. Alignment: standard-model-subset. This is a scoped explanation, not institutional endorsement or certification of KPS. The source does not define KPS file roles.
