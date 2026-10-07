---
package_version: "9.0.1"
language: "KPS 9.x"
reviewed: "2026-10-07"
---

# Governance

## Key takeaway
KPS accepts community contributions, while maintainers protect the semantics, evidence standards and compatibility of each release.

## Summary
KPS accepts community contributions, while maintainers protect the semantics, evidence standards and compatibility of each release.

## Decision process
Contributors propose changes using issues or pull requests. Maintainers review their explanation and evidence, request revisions where needed, and accept changes through reviewed merges. A pull request's approval represents a project decision, not empirical confirmation of the knowledge inside it.

## Language and package versions
The five roles, the authoring contract and compatibility requirements are part of the KPS language. A breaking semantic or required structural change calls for a **new language major line**. Backwards-compatible improvements can appear within the current line. The project package/version changes independently; domain implementations may declare a compatible major language line and retain their own package versions.

## Evidence and scope disputes
A source can be useful without proving every claim ascribed to it. When evidence is contested, record the competing interpretation, inspected extent, scope and uncertainty. Avoid resolving disagreements by citation volume alone. A final project convention should be labelled a convention rather than a scientific law.

## Maintainer responsibility
Maintainers can reject unsupported normative claims, security-risky changes, copyrighted source copies, incompatible unversioned modifications and contributions that violate the conduct policy. They should document significant reversals and keep old tagged releases available for historical navigation.

## Community participation
Anyone may propose improvements through public issues and pull requests. This initial package does not promise a specific response time, formal governance election, or independent expert-review process; those can be adopted if participation justifies them.
