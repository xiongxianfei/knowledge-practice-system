---
package_version: "10.0.0"
language: "KPS 9.x"
reviewed: "2026-10-12"
---

# Knowledge Practice System

## Key takeaway

Reuse established knowledge and make KPS-specific application explicit.

## Summary

KPS Core 10.0.0 organizes professional knowledge and applies it through steps-first Practices. This is a decisive content refactoring: 41 former local Concepts, Principles, Models and Methods are retired as standalone objects. Their useful application responsibilities are embedded in the four retained Practices.

## Start with the task

[Use KPS](practices/use-kps.md) answers one bounded question. [Build domain knowledge](practices/build-domain-knowledge.md) connects sources to usable knowledge. [Improve KPS](practices/improve-kps.md) tests a change. [Review and learn](practices/review-and-learn.md) preserves actual observations and revisable conclusions.

## What is reusable and what is ours

| Library | Examples | Boundary |
|---|---|---|
| Concepts | SKOS Concept, Provenance, URI, Study and Report, Evidence Indirectness | Named source meanings, not universal definitions |
| Principles | Testing Effect, Spacing Effect, evidence independence and applicability | Scoped findings or methodological relationships, not rules |
| Models | SKOS and PROV data models | Explanatory subsets, not RDF conformance claims |
| Methods | PICO, Study Data Extraction, PDCA, Cognitive Walkthrough, Retrieval Practice | Published procedures, not newly named KPS workflows |
| Practices | Use, build, improve, review | Our task-specific synthesis, explicitly identified |

The library contains **20 core objects and 17 Reference records**. Smaller does not mean that every removed statement was false. Local workflow abstractions no longer masquerade as reusable professional knowledge. [INDEX.md](INDEX.md) lists the current library; [MIGRATION.md](MIGRATION.md) accounts for each old ID and destination.

## Authoring and source alignment

[AUTHORING.md](AUTHORING.md) is the local format contract. [ALIGNMENT.md](ALIGNMENT.md) is the Core curation policy. [TEMPLATES.md](TEMPLATES.md) gives examples, not another authority. The five roles, StageN convention and Markdown profile remain KPS choices; none is attributed to W3C, Cochrane or ASQ.

Every substantial file has a takeaway and summary. Practices put actions first and retain needed reasoning, examples, interpretation and fallback inline. Source records state actual inspection extent. No source PDF, private record, measured learning outcome or institutional endorsement is bundled or invented.

## Versions and checks

Core **content version 10.0.0** marks breaking IDs and paths. The five-role **KPS 9.x authoring language** is unchanged, and the included structural checker remains **9.1.0**. The new Core alignment test is an additional curation check, not a new domain-language requirement. See [COMPATIBILITY.md](COMPATIBILITY.md).

```bash
python validate.py .
python test_validate.py
python test_alignment.py
```

These checks do not prove factual correctness or usability. [CHECKS.md](CHECKS.md) separates executed checks from their limits. [REVIEW.md](REVIEW.md) describes the content review.

## Publication and rights

Use one change branch and PR; merge when authorized and checks pass. Keep Git history rather than parallel obsolete files. No separate tag or official release is implied. Swim, Technical Insight and REM are unchanged by this Core-only revision.

KPS-authored content and tooling use the retained [MIT license](LICENSE); cited works retain their own rights. Follow [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
