---
package_version: "9.0.1"
language: "KPS 9.x"
reviewed: "2026-10-07"
---

# Contributing to KPS

## Key takeaway
Contributions are welcome when they make KPS clearer, more defensible, more usable, or easier to validate without hiding uncertainty.

## Summary
Contributions are welcome when they make KPS clearer, more defensible, more usable, or easier to validate without hiding uncertainty.

## How to start
Browse [the knowledge index](INDEX.md), [the authoring contract](AUTHORING.md), [the source synthesis example](SOURCE-SYNTHESIS-EXAMPLE.md), and open an issue to clarify a new knowledge type, significant semantic change or contentious claim before doing a large rewrite. For a small typo or broken link, a direct pull request is welcome.

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
1. Read [Authoring](AUTHORING.md) and the existing canonical objects that the change affects.
2. Edit the smallest meaningful set of files, keeping each revised file self-contained.
3. Update incoming links if a file, heading, or `StageN` order changes.
4. Review the receiving summaries when a referenced canonical object changes; do not blindly refresh them.
5. Run `python validate.py .` and `python test_validate.py`. Include failures and limitations in the PR if they cannot be resolved.
6. Submit a pull request describing: **problem, changed claim/contract, evidence or rationale, affected objects, validation and remaining uncertainty**.

## Review criteria
Reviewers consider semantic role correctness, traceable reasoning, source-claim relevance, self-contained usability, cross-file compatibility, risk and maintenance impact. A passing validator is necessary for structure, not sufficient for knowledge quality. Maintainers may request a narrower contribution if evidence or scope is unclear.

## Contribution license
Contributions submitted for inclusion in the KPS-authored material are intended to be distributed under this repository's [MIT License](LICENSE). Do not submit third-party materials you lack permission to relicense; link to them using Reference records instead. If you cannot accept the license terms, discuss the issue before submitting a pull request.

## Respectful collaboration
Read the [Code of conduct](CODE_OF_CONDUCT.md). Do not include passwords, private user records, medical histories, third-party personal information or private implementation details in public issues or pull requests.
