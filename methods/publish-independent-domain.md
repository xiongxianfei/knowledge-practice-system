---
id: "kps:me:publish-independent-domain"
type: "method"
version: "9.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored method; supporting findings separately attributed"
confidence: "proposed implementation, not independently validated"
uses_principles: ["kps:p:provenance-does-not-establish-truth"]
uses_models: ["kps:mo:domain-package-model"]
references: []
perspectives: ["knowledge-representation", "evidence-reasoning"]
uses_methods: ["kps:me:check-local-completeness", "kps:me:build-and-check-navigation"]
---

# Publish an independent domain

## Key takeaway

Produce a readable, self-contained package and distinguish structural checks from knowledge validation.

## Summary

A publishable knowledge base needs working navigation and identifiable evidence, but a checksum cannot establish the truth of its claims. Work on a copy in a clean directory. Check relative links, typed targets and any stored dependency snapshots, then extract the ZIP elsewhere and repeat. Passing checks shows file consistency, not domain truth.

## Inputs and prerequisites

A concrete question, the material or actual record to inspect, and enough context to distinguish observed information from a proposed interpretation. No result is assumed in advance.

## Local explanatory basis

A trace showing where a claim came from does not by itself establish that the claim is correct.

## Objective
Produce a readable, self-contained package and distinguish structural checks from knowledge validation.

## Rationale
A publishable knowledge base needs working navigation and identifiable evidence, but a checksum cannot establish the truth of its claims.

## Evidence and reasoning
[Independent domain package model](../models/domain-package-model.md) defines the publication contract. [Provenance does not establish truth](../principles/provenance-does-not-establish-truth.md) explains the limit of a technical check.

## Steps
1. Review goal, type boundaries, principle wording, source scope and important rationales before release.
2. Include only structured Reference records, not copyrighted source copies. Give unknown dates an explicit undated filename.
3. Generate or refresh the index and why map. Check local links, stable identities, allowed types, required sections and reference identities.
4. Run `python validate.py` and `python validate.py --self-test` from the package root. Read warnings rather than treating a green result as scientific review.
5. Create a fresh archive with a manifest, extract it separately, and rerun the check without any sibling package present.
6. Publish download links and label scope, unresolved claims, evidence access limits and whether public hosting actually occurred.

## Expected effect
A checked package with truthful release notes and no hidden local dependencies.

## Validation and counterevidence
Try intentionally broken fixtures; the checker should reject them. Confirm navigation without relying on the old release.

## Limits
The bundled validator does not fetch external URLs, evaluate scientific truth or prove safety/effectiveness.

## Local evidence summary

This file uses KPS’s declared conventions or an explicit reasoning argument rather than claiming an externally tested intervention. Its explanation and counterexample are local; linked objects identify reusable connections, not independent confirmation.

## Local completeness check

State who can use the file and what they should understand or do. Hide its links: the essential definitions, explanatory relation, representation or procedure, evidence limits and next/fallback decision must remain visible. Restore links and compare the summary with the source meaning. Preserve decision-critical qualifiers; do not copy full derivations just to increase length. Update dependent summaries deliberately when their source changes. These are authoring checks, not empirical evidence of effectiveness.

## Deeper knowledge

Canonical dependencies and Reference records provide additional derivation, source inspection and alternatives. They are not required to carry out the local explanation or procedure.

- **Principles:** [Provenance does not establish truth](../principles/provenance-does-not-establish-truth.md)
- **Models:** [Independent domain package model](../models/domain-package-model.md)
- **Methods:** [Check local completeness and faithful compression](check-local-completeness.md)
