---
package_version: "11.0.0"
language: "KPS 9.x"
reviewed: null
---

# KPS knowledge index

## Key takeaway

Read source-aligned knowledge for reusable meaning and Practices for KPS-specific application.

## Summary

This Core library contains 20 knowledge objects: five Concepts, four Principles, two Models, five Methods and four Practices. Nineteen supporting Reference records preserve source identity and inspection limits. The smaller library removes duplicate local abstractions rather than turning them into professional terminology.

Explore topics and their relationships in the [knowledge and practice subject map](subject-map.md). This page provides the file index by role and the [source-to-application table](#from-sources-to-kps-applications).

## Concepts

- [Evidence Indirectness](../concepts/evidence-indirectness.md)
- [Provenance](../concepts/provenance.md)
- [SKOS Concept](../concepts/skos-concept.md)
- [Study and Report](../concepts/study-and-report.md)
- [Uniform Resource Identifier](../concepts/uniform-resource-identifier.md)

## Principles

- [Indirectness Limits Applicability](../principles/indirectness-limits-applicability.md)
- [Spacing Effect](../principles/spacing-effect.md)
- [Study Level Evidence Independence](../principles/study-level-evidence-independence.md)
- [Testing Effect](../principles/testing-effect.md)

## Models

- [PROV Data Model](../models/prov-data-model.md)
- [SKOS Data Model](../models/skos-data-model.md)

## Methods

- [Cognitive Walkthrough](../methods/cognitive-walkthrough.md)
- [Plan Do Check Act](../methods/pdca.md)
- [PICO Question Formulation](../methods/pico-question-formulation.md)
- [Retrieval Practice](../methods/retrieval-practice.md)
- [Study Data Extraction](../methods/study-data-extraction.md)

## Practices

- [Build an independent domain knowledge package](../practices/build-domain-knowledge.md)
- [Improve KPS without mistaking structure for usefulness](../practices/improve-kps.md)
- [Review an application and retain justified learning](../practices/review-and-learn.md)
- [Use KPS for one real task](../practices/use-kps.md)

## Reference records

- [ASQ Plan Do Check Act Cycle](../references/asq-undated-pdca-cycle.md)
- [Cochrane Certainty of Evidence Chapter 14](../references/cochrane-2024-certainty-chapter-14.md)
- [Cochrane Collecting Data Chapter 5](../references/cochrane-2024-collecting-data-chapter-5.md)
- [Cochrane Review Questions Chapter 2](../references/cochrane-2024-review-questions-chapter-2.md)
- [GitHub Basic writing and formatting syntax](../references/github-undated-markdown-formatting.md)
- [RFC 3986 URI Generic Syntax](../references/ietf-rfc3986-2005-uri-syntax.md)
- [Retrieval practice produces more learning than elaborative studying with concept mapping](../references/karpicke-2011-retrieval-and-concept-mapping.md)
- [Spaced retrieval absolute spacing enhances learning regardless of relative spacing](../references/karpicke-2011-spaced-retrieval.md)
- [Re examining the testing effect as a learning strategy the advantage of retrieval practice over concept mapping as a methodological artifact](../references/mayrhofer-2023-reexamining-the-testing-effect.md)
- [MkDocs Writing your docs](../references/mkdocs-undated-writing-your-docs.md)
- [Concept maps and their construction](../references/novak-canas-2008-concept-maps.md)
- [How to guides](../references/procida-undated-how-to-guides.md)
- [Python Markdown Table of Contents](../references/python-markdown-undated-toc-extension.md)
- [SKOS Reference 2009](../references/w3c-2009-skos-reference.md)
- [PROV DM 2013](../references/w3c-2013-prov-dm.md)
- [PROV Overview](../references/w3c-2013-prov-overview.md)
- [Complex images](../references/w3c-2026-complex-images.md)
- [Cognitive Walkthrough Practitioner Guide Report 93 07](../references/wharton-undated-cognitive-walkthrough-report-93-07.md)

[Alignment policy](alignment.md) distinguishes source definitions from KPS application. [Migration record](migration.md) accounts for retired identifiers.

## Visual reading aids

[Selective diagrams](diagrams.md) explains why each image is present and how to edit it. [Use KPS neighborhood](#one-hop-knowledge-neighborhood) shows one local set of typed dependencies. The [D2 documentation Reference](../references/d2-undated-cli-and-svg-export.md) supports the renderer choices. Images are supporting assets, not additional knowledge objects.

## From sources to KPS applications

| Source-aligned knowledge | What it supports | Our receiving application |
|---|---|---|
| [SKOS Concept](../concepts/skos-concept.md) and [model](../models/skos-data-model.md) | Distinctions between meaning, labels and vocabulary relationships | [Classify and name](../practices/build-domain-knowledge.md#stage3-create-locally-complete-objects) |
| [URI](../concepts/uniform-resource-identifier.md) | Identification and reference resolution terminology | [Repair navigation](../practices/use-kps.md#stage2-retrieve-and-inspect-the-local-explanation) |
| [Provenance](../concepts/provenance.md) and [PROV model](../models/prov-data-model.md) | Production history and derivation | [Preserve records](../practices/review-and-learn.md#stage1-reconstruct-the-record) |
| [PICO](../methods/pico-question-formulation.md) and [data extraction](../methods/study-data-extraction.md) | Explicit questions and source-located study data | [Claim worksheet](../practices/build-domain-knowledge.md#stage2-find-evidence-for-explicit-claims) |
| [Evidence indirectness](../concepts/evidence-indirectness.md) | Applicability gaps in intervention evidence | [Review the target question](../practices/build-domain-knowledge.md#stage2-find-evidence-for-explicit-claims) |
| [Cognitive walkthrough](../methods/cognitive-walkthrough.md) | Task-based predictions about learnability | [Inspect a guide](../practices/build-domain-knowledge.md#stage4-compile-the-practice) |
| [PDCA](../methods/pdca.md) | Iterative improvement procedure | [Improve KPS](../practices/improve-kps.md) |
| [Retrieval practice](../methods/retrieval-practice.md) and [spacing](../principles/spacing-effect.md) | Scoped learning operations and findings | [Choose a learning check](../practices/review-and-learn.md#stage4-define-the-next-check) |

Each relationship above represents KPS's selected application, not institutional endorsement, scientific validation of KPS, or formal semantic equivalence. Apply external terminology only within its source scope.

## One hop knowledge neighborhood

![Use KPS directly uses the Provenance and URI Concepts, Retrieval Practice Method, and PROV Data Model](../diagrams/knowledge-map/use-kps-dependencies.svg)

The [Use KPS Practice](../practices/use-kps.md) declares use of [Provenance](../concepts/provenance.md), [Uniform Resource Identifier](../concepts/uniform-resource-identifier.md), [Retrieval Practice](../methods/retrieval-practice.md) and the [PROV Data Model](../models/prov-data-model.md). The edge labels reproduce `uses_concepts`, `uses_methods` and `uses_models`. They do not mean that every step requires all four documents or that a Method has been validated by its presence on the graph.

This is a one-hop view. Reference records, indirect dependencies and other Practices are intentionally omitted. Ordinary Markdown links above supply navigation; clickable SVG nodes are not required.

[Editable generated D2 source](../diagrams/knowledge-map/use-kps-dependencies.d2). Update the owning documents' metadata, then regenerate; do not add unsupported edges to the D2 file.

