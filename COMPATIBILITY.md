---
package_version: "9.1.0"
language: "KPS 9.x"
reviewed: "2026-10-11"
---

# KPS major line and authoring tool compatibility

## Key takeaway

KPS 9.1.0 keeps the five-role language and accepts earlier Practice layouts; steps-first documents require the updated checker.

## Summary

A package version identifies content, a language declaration identifies the knowledge contract, and the minimum checker identifies a tooling feature. Do not infer that every 9.x checker understands every later presentation. This release relaxes stage formatting without changing Concept, Principle, Model, Method or Practice meanings.

## Declaration

```yaml
kps_language: "9.x"
validated_with: "9.1.0"
minimum_validator: "9.1.0"
markdown_profile: "practical-markdown-v1"
```

Knowledge files keep `language: "KPS 9.x"`; new Core Practices declare `practice_format: "steps-first-v1"`. Their stable identities and StageN targets remain independent of formatting labels.

## Compatibility direction

| Content | KPS 9.0 checker | KPS 9.1 checker |
|---|---|---|
| Existing valid six-label stages with inline procedures | Existing behavior | Accepted |
| Steps-first stages without the six labels | Rejects missing labels | Accepted when structurally valid |
| Missing actions or broken local targets | Rejects applicable defects | Rejects applicable defects |

Backward acceptance means the new checker accepts the earlier representation, not that the old checker understands the new one. Existing domain repositories are not edited or automatically upgraded. Retain their inspected 9.0 tooling until migration is requested; adopting steps-first content requires the matching authoring guidance and checker.

## When a new major is needed

Changing a core role's meaning, removing an existing valid representation, or changing the required navigation semantics calls for a breaking-version assessment. Optional support and a relaxation that preserves earlier documents can be introduced within 9.x. This is KPS's explicit compatibility policy, not evidence of cross-tool behavior beyond the stated checks.

## Domain migration

1. Compare the inspected contract with the domain's actual files and declared tooling version.
2. Keep useful content and rewrite Practices as task guides, not by deleting labels alone.
3. Update examples, source annotations and local visuals together with dependencies.
4. Use the new checker and regression suite; review the content separately.
5. Record the exact checked release and minimum checker. Publish only the requested domain.

## Independence and limits

No mandatory filesystem dependency on another package is introduced. A bundled checker is an inspected copy, not a separate authoring authority. A compatibility declaration does not certify factual accuracy, reader comprehension, physical competence or future releases. [AUTHORING.md](AUTHORING.md) remains the normative contract.
