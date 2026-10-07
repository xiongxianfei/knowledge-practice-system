---
package_version: "9.0.1"
language: "KPS 9.x"
reviewed: "2026-10-07"
---

# KPS major line compatibility

## Key takeaway
The package declares `KPS 9.x` compatibility and records `9.0.0` as the release used for this validation. Compatibility scope is not proof that future releases have been tested.

## Summary
Package version and KPS language version answer different questions. The package version identifies this domain's content. The KPS declaration identifies the shared knowledge roles and authoring contract. Each domain remains readable by itself and has no mandatory filesystem dependency on KPS or another domain.

## Declaration
```yaml
kps_language: "9.x"
validated_with: "9.0.0"
markdown_profile: "practical-markdown-v1"
```
The package's own version is in `publication.json`. Knowledge files carry `language: "KPS 9.x"`; their stable IDs remain local to the package. `validated_with` is an audit fact, not an exact runtime dependency.

## What remains compatible within major version 9
The five roles keep their meaning: Concept defines a distinction; Principle explains a reusable relationship; Model represents elements and interactions; Method gives an operation and its rationale; Practice composes knowledge for a real goal. Reference is a supporting source record, not a sixth core role. Perspective remains metadata.

Every substantial document has a takeaway, summary, adequate local content and limits. Practices keep inline stage understanding, action, observation, success and fallback. `Stage1` titles express recommended order, not proof of prerequisites or stable identity. The practical Markdown profile uses YAML, relative file links and heading slugs.

A compatible minor or patch KPS release can clarify documentation or add optional knowledge/tools without changing those required meanings. It must not quietly make existing valid domain content invalid. This is a release policy adopted by this project, not a law of software or knowledge.

## When compatibility needs review
A changed core meaning, newly mandatory incompatible structure or changed navigation contract needs an explicit compatibility assessment and, when breaking, a new language major. A new domain requiring an optional feature introduced later in 9.x should declare that minimum feature/version in its release note instead of claiming support from every earlier tool.

A correction to swimming evidence or a changed engineering recommendation can require a domain release without changing the KPS language. Conversely, an unchanged domain may still need source review when an important reference or context changes.

## How to update a domain
1. Compare the new KPS release against this contract; do not accept only a matching numeral.
2. Review the domain's meanings, metadata, summaries and navigation where affected.
3. Run structural checks and read representative files with links hidden.
4. Record the exact KPS release used for validation and limitations of that check.
5. Keep or revise the major-line declaration on that basis. No scientific or clinical validity follows from language compatibility.

## Independence and limits
References may cite external material; source inspection can require internet access. Ordinary reading of local knowledge does not require sibling files. The duplicated compatibility note and checker are deliberate supporting infrastructure so each archive is independently usable. KPS governs the authoring language; domain knowledge and actual outcomes remain separately assessed.
