---
package_version: "10.0.0"
language: "KPS 9.x"
reviewed: "2026-10-12"
---


# KPS Authoring Contract

## Key takeaway
This local specification defines the KPS 9.x document format; it is not an externally endorsed knowledge taxonomy.

## Summary
This local specification defines the KPS 9.x document format; it is not an externally endorsed knowledge taxonomy.

## Authority and scope
This document defines the **KPS 9.x authoring convention** for the five knowledge roles, publication-based Reference records, self-contained content, metadata, naming, stage headings and local links. `TEMPLATES.md`, `NAVIGATION.md` and Practices provide examples or application guidance, not competing authoring requirements. This is a project convention, not a universally standardized Markdown dialect.

An *incompatible change to these requirements* needs a new KPS language major version; compatible explanations, tooling and optional guidance may change within 9.x. A domain package declares `kps_language: "9.x"` and separately records the KPS release it was checked against.

## Folder roles
- `concepts/`: one reusable definition or distinction per document.
- `principles/`: one explanatory, scoped, declarative relationship per document; a **command or chosen engineering constraint** is not itself a Principle.
- `models/`: a representation with essential terms, relationships, assumptions, implications and limits.
- `methods/`: a repeatable operation with objective, prerequisites, rationale, executable steps, observations, expected effect and validation/counterevidence.
- `practices/`: a staged operational synthesis that is usable without reading all its links. A Practice can compose other Practices when goals and decision logic genuinely warrant it, but stages do not each require a separate file.
- `references/`: structured Markdown provenance records identifying actual external publications, claim contributions, checked extent, limits and non-claims. **References are not a sixth knowledge type.**

Supporting root-level documents and verification tooling are infrastructure, not extra knowledge types.

## Filename and identity
Use lowercase, meaningful kebab-case filenames, such as `spacing-effect.md` for a Principle, `study-data-extraction.md` for a Method or `build-domain-knowledge.md` for a Practice. Reference filenames identify the **publication**, normally `creator-year-short-title.md`, `creator-undated-short-title.md`, or `organization-standard-id-year.md` when the official identifier matters. Do not infer a publication year from the date accessed.

Metadata must include a stable `id`, `type`, `version`, `language` and `status` for a knowledge object. Stable IDs are **not** Markdown link anchors. Metadata is for identities, indexing and typed dependency hints; body prose explains why the relationships matter.

```yaml
---
id: "domain:method:study-data-extraction"
type: "method"
version: "1.0.0"
language: "KPS 9.x"
status: "draft"
uses_principles: []
uses_models: []
references: []
---
```

The included dependency-free validator accepts JSON-compatible single-line YAML field values. This is a deliberate limited profile; it is not a general YAML parser.

## Local completeness
All substantial Markdown knowledge and Reference files use one semantic `# Title`, `## Key takeaway`, and `## Summary`, then locally sufficient meaning, procedure or representation, examples as appropriate, limits and deeper links. Hide links and ask whether the intended understanding/use task still works; then restore links and check the local summary faithfully preserves its source's relevant conditions. Do **not** copy all linked sources into each file.

Knowledge by role must be self-contained: a Principle explains the actual relationship, not merely a command; a Model includes its representation rather than only a link; a Method includes actionable steps and safeguards; a Practice contains operationally sufficient information **in each stage**, not a list of Methods to visit elsewhere.

## Practice stages
A Practice heading uses **exactly** the compact pattern below, consecutively numbered in its current recommended/default order:

```markdown
## Stage1 Breathing and air access
## Stage2 Body support and recovery
## Stage3 Kick preparation and completion
```

**Stage numbers communicate recommended order**, not mandatory sequential completion and not permanent identity. Stage prerequisites and real-world safety/authority boundaries state actual dependencies. Keep the Stage name semantic and visible; avoid opaque code headings such as `TI-03` or `F4`.

Write **steps first**, after only the context and prerequisites needed to begin safely. Numbered actions are the usual presentation; a decision table or branching procedure can be clearer for a non-linear task. Keep the action, necessary explanation, expected output or interpretation, and next/fallback decision locally available. These are content responsibilities, not six mandatory labels.

Do not require `Goal`, `Why`, `What to do`, `What to observe`, `Success signal`, or `Next` at the start of every stage. Labels may be used where genuinely helpful. Do not repeat the same content as an introduction, card and procedure. Use bold `Steps` or another descriptive label for recurring blocks; give navigable subheadings unique meaningful names.

Start a Practice with a meaningful Summary and a stage map. End with a current working summary containing only actual recorded experience, or an explicitly blank record. Stages remain in the same file unless a split genuinely improves use. No fixed stage length or quota of examples, charts or links defines completeness.

## Supporting material at the point of use

Place the support beside the action it clarifies. Add a worked example when the required output would otherwise be ambiguous, a decision table when outcomes lead to different actions, and a diagram when a relationship is hard to express compactly. Explain the visual's essential meaning in nearby text. For quantitative charts retain data, units, scale choices and interpretation; label synthetic data and do not manufacture results.

Prefer text diagrams and Markdown tables for simple relationships. When an image is useful, embed a local PNG or SVG through ordinary Markdown image syntax, add meaningful alternative text and a nearby explanation, and include its source/rights information. Keep essential text available if the image cannot render. Avoid hotlinked images and renderer plugins as dependencies for understanding; external images receive a checker warning rather than an assumption of offline availability.

Link directly to relevant websites where useful, with a short annotation stating what to inspect, what it supports and the important limit. Maintain the full publication identity and inspection extent in `references/`. Essential instructions stay inline. A collection of links is not a self-contained Practice, and embedding a third-party article is not a substitute for synthesis.

## Format and tool compatibility

The five roles, stage numbering and Markdown navigation contract are unchanged. KPS 9.1.0 relaxes fixed stage layout: existing six-label stages can still be checked, but Core now authors steps-first stages rather than two parallel templates. Mark new Practices `practice_format: "steps-first-v1"` and record `minimum_validator: "9.1.0"` in package metadata. Earlier 9.0 validators reject missing labels and cannot validate the new presentation; the 9.x declaration alone does not make old tools understand it. See [Compatibility](COMPATIBILITY.md) before migrating a domain.

## Markdown links
KPS uses UTF-8 `.md`, ordinary inline relative file links and conservative heading fragments; avoid application-specific wikilinks, embedded HTML anchors and renderer-dependent extensions. For links to a full file, use `[Text](../models/example.md)` rather than a fragile section fragment. For section links, the destination must match the complete real heading under the chosen lowercase/hyphenated profile:

```markdown
[Stage1 Breathing and air access](#stage1-breathing-and-air-access)

## Stage1 Breathing and air access
```

No YAML identity or prefix such as `TI-03` creates an anchor automatically. When renumbering or renaming a Stage, update the heading, stage map and incoming links together. Strict CommonMark itself does not define heading identifiers; test the actual reader when renderer fidelity is important. `NAVIGATION.md` contains explanatory examples, not a second contract.

## Evidence and reference records
Start with a question and candidate claim, identify required evidence, inspect what sources actually establish, check independence and disagreement when material, and separate source premises from KPS's inference. A single directly authoritative source may establish its own definition; multiple citations to one underlying study are not independent evidence.

A Reference must include its full identity, external URL/DOI, reliable publication/update-date basis or `undated`, access and inspection extent, located relevant claims, limitations and **what it does not establish**. Do not copy restricted full texts into the repository or imply full-text access from abstract-only inspection.

## Validation and review
Run `python validate.py .` and `python test_validate.py`. The checker covers structurally testable elements, including section IDs, stage order/maps, metadata relationships, missing inline actions, local image targets, and declared dependency changes. It does not enforce repeated stage labels or a word-count minimum. The absence of a required action structure is a mechanical error; the usefulness of the steps, examples, source fit, interpretation and fallback requires the content review in `REVIEW.md`. It is **not** a proof of scientific truth or user comprehension. If a canonical source changes, review affected local summaries before refreshing the dependency snapshot using `--accept-reviewed-summaries`.

Root-level GitHub community and automation files are repository infrastructure rather than KPS knowledge objects; the checker applies KPS-specific Markdown rules to the knowledge/content documents, not the GitHub form templates under `.github/`.

## Core professional alignment policy

Core content 10.0.0 adopts [ALIGNMENT.md](ALIGNMENT.md). Its standalone Concepts, Principles, Models and Methods identify the actual source, relation and passage. Source-defined meaning takes precedence over a conflicting local paraphrase; scope differences must not be disguised as equivalence. KPS-specific workflows, reasoning aids and design choices are embedded in Practices. Necessary file-format rules remain here as specifications, not scientific Principles.

This is a Core curation decision, not a silent change to the five-role KPS 9.x language. The unchanged 9.1.0 structural checker accepts these files; `test_alignment.py` checks the additional Core declarations and migration. A passing test cannot determine authority, faithfulness or scientific validity. Other domain packages adopt the policy separately rather than being changed by this release.
