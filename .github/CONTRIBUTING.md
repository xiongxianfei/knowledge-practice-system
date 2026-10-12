---
package_version: "10.0.0"
language: "KPS 9.x"
reviewed: "2026-10-12"
---


# Contributing to KPS

## Key takeaway
Contributions are welcome when they make KPS clearer, more defensible, more usable, or easier to validate without hiding uncertainty.

## Summary
Contributions are welcome when they make KPS clearer, more defensible, more usable, or easier to validate without hiding uncertainty.

## How to start
Browse [the knowledge index](../docs/library.md), [the authoring contract](../docs/authoring.md), [the source synthesis example](../docs/examples/source-synthesis.md), and open an issue to clarify a new knowledge type, significant semantic change or contentious claim before doing a large rewrite. For a small typo or broken link, a direct pull request is welcome.

## Contribution types
- Correct a Concept's definition, scope or example.
- Replace a rule-like Principle with an explanatory, declarative relationship.
- Correct a Model's relationships, assumptions or counterexamples.
- Improve a Method's rationale, steps, counter-signals or safety limits.
- Make a Practice's staged content locally usable rather than link-dependent.
- Add claim-specific Reference records and source syntheses that expose disagreements.
- Improve tooling, navigation, tests or documentation without making unverifiable claims.

## Evidence expectations
Explain the precise claim being added or changed. Identify which parts are directly supported by cited material and which are an interpretation or KPS-specific design choice. For scientific and practical efficacy claims, look for independent, domain-relevant evidence when consequences warrant it; do not invent a source count. Record known competing evidence and the population/context limits. Do not paste copyrighted full publications into Reference files.

## Author a change
1. Read [Authoring](../docs/authoring.md) and the existing canonical objects that the change affects.
2. Edit the smallest meaningful set of files, keeping each revised file self-contained.
3. Update incoming links if a file, heading, or `StageN` order changes.
4. Review the receiving summaries when a referenced canonical object changes; do not blindly refresh them.
5. Run `python validate.py .` and `python test_validate.py`. Include failures and limitations in the PR if they cannot be resolved.
6. Submit a pull request describing: **problem, changed claim/contract, evidence or rationale, affected objects, validation and remaining uncertainty**.

## Review criteria
Reviewers consider semantic role correctness, traceable reasoning, source-claim relevance, self-contained usability, cross-file compatibility, risk and maintenance impact. A passing validator is necessary for structure, not sufficient for knowledge quality. Maintainers may request a narrower contribution if evidence or scope is unclear.

## Contribution license
Contributions submitted for inclusion in the KPS-authored material are intended to be distributed under this repository's [MIT License](../LICENSE). Do not submit third-party materials you lack permission to relicense; link to them using Reference records instead. If you cannot accept the license terms, discuss the issue before submitting a pull request.

## Respectful collaboration
Read the [Code of conduct](CODE_OF_CONDUCT.md). Do not include passwords, private user records, medical histories, third-party personal information or private implementation details in public issues or pull requests.

## Maintainer authority and project governance

Maintainers evaluate proposed changes against the authoring contract, source-alignment policy, usability and compatibility. Their approval is a project decision, not evidence that a knowledge claim has been scientifically validated. Material reversals should be recorded. KPS language major changes and independently versioned Core content are distinct; do not silently force migrations on other domain packages.

Contributors may raise issues or pull requests; there is no promised response time, formal election process, or institutional endorsement. Maintainers may reject unsupported claims, insecure implementations, incompatible unversioned changes, or improperly licensed material.

## Publication boundary

Use one reviewed change, one branch, and one pull request against the actual main branch. Run the required structure, alignment and diagram checks. Merge automatically **only** with owner authorization after successful checks; otherwise leave the PR for review. Do not create tags or official releases without a request. Where no corresponding repository exists, validate and distribute a complete ZIP with a checksum manifest. Do not copy restricted source publications or modify sibling domains without permission. The full task procedure lives in [Build domain knowledge](../practices/build-domain-knowledge.md#stage5-check-and-release).

