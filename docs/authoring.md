---
package_version: "11.0.0"
language: "KPS 9.x"
reviewed: null
---


# KPS Authoring Contract

## Key takeaway
This local specification defines the KPS 9.x document format; it is not an externally endorsed knowledge taxonomy.

## Summary
This local specification defines the KPS 9.x document format; it is not an externally endorsed knowledge taxonomy.

## Authority and scope
This document defines the **KPS 9.x authoring convention** for the five knowledge roles, publication-based Reference records, self-contained content, metadata, naming, stage headings and local links. `docs/templates.md` and Practices provide examples or application guidance, not competing authoring requirements. This is a project convention, not a universally standardized Markdown dialect.

An *incompatible change to these requirements* needs a new KPS language major version; compatible explanations, tooling and optional guidance may change within 9.x. A domain package declares `kps_language: "9.x"` and separately records the KPS release it was checked against.

## Folder roles
- `concepts/`: one reusable definition or distinction per document.
- `principles/`: one explanatory, scoped, declarative relationship per document; a **command or chosen engineering constraint** is not itself a Principle.
- `models/`: a purposeful, simplified representation explaining relevant entities, essential attributes, relationships or rules, assumptions, implications and limits.
- `methods/`: a repeatable operation with objective, prerequisites, rationale, executable steps, observations, expected effect and validation/counterevidence.
- `practices/`: a staged operational synthesis that is usable without reading all its links. A Practice can compose other Practices when goals and decision logic genuinely warrant it, but stages do not each require a separate file.
- `references/`: structured Markdown provenance records identifying actual external publications, claim contributions, checked extent, limits and non-claims. **References are not a sixth knowledge type.**

Supporting root-level documents and verification tooling are infrastructure, not extra knowledge types.

## Reconstruct knowledge for a target Practice

Start with what a reader should understand, accomplish or investigate through a target Practice. Reuse established disciplinary concepts, distinctions, models and their relationships as the foundation. Inspect the relevant accounts before choosing knowledge boundaries. Select and reconstruct the material needed for the target, preserving the source's meaning, conditions and limits. A source's teaching order need not become the package's file hierarchy; competing frameworks should remain identifiable rather than being silently blended.

Reconstruction includes selection, explanation, integration and contextual application. Identify the adopted source structure, the subset used and any authored adaptation. Draft the target Practice early and revise its actions and supporting knowledge together. A learning Practice can target explanation, analysis and investigation as well as performance. Its scope does not require documenting an entire discipline or inventing one object of every role.

For coverage guides, use an authored `docs/body-of-knowledge-outline.md` to make the adopted subject structure visible: scope, topics, required understanding and capabilities, relationships, source basis, existing explanations and gaps. Follow the [outline authoring guide](body-of-knowledge-outline-guide.md) and [template](templates.md#body-of-knowledge-outline). It belongs to shared knowledge navigation; Practices select from it and own their activity sequences. The five role folders remain the storage organization, with useful overlap across topics. This optional guidance introduces no new knowledge type, required metadata or generated artifact. The [Core body of knowledge outline](body-of-knowledge-outline.md) demonstrates the result; packages migrate explicitly rather than keeping two competing coverage guides.

Select the subject outline from established accounts and the intended scope before mapping existing files onto it. State where the grouping is an authored synthesis across accounts. A necessary topic remains visible when its explanation is missing. Lead with what topics mean and how they connect. Align existing explanations with each topic in the same table row, identifying partial coverage, source-only records and gaps there. One topic may link to several explanations, and an explanation may support several topics. The source-to-application index and the construction Practice answer different questions and should not determine the subject divisions.

## Primary roles and useful overlap

The five roles describe a document's primary contribution; they do not partition its content into mutually exclusive substances. A Concept can include a small representation; a Model can explain Concepts and Principles; a Method can explain its supporting Model; a Practice can include all of these at the point of use. Keep one primary metadata type and stable identity per object. Supporting content does not need separate identities merely because it serves another role.

Choose document boundaries for coherent explanation, independent reuse and readability. Begin with sections; split when the resulting documents each have a useful purpose and preserve the relationships needed to understand them. Keep a definition and its contextual application consistent while allowing necessary overlap. Link to the owning explanation and preserve its conditions locally; avoid competing definitions or duplicated passages that serve no reader need. Review affected explanations when the shared meaning changes.

For example, a Concept may define elision, a Model may relate it to other speech processes and their conditions, and a learning Practice may explain it beside an analysis task. The overlap supports different purposes. It does not make the concept, representation and procedure interchangeable. These are authoring clarifications within KPS 9.x, without new mandatory fields, headings or role counts.

## Filename and identity
Use lowercase, meaningful kebab-case filenames, such as `spacing-effect.md` for a Principle, `study-data-extraction.md` for a Method or `build-domain-knowledge.md` for a Practice. Reference filenames identify the **publication**, normally `creator-year-short-title.md`, `creator-undated-short-title.md`, or `organization-standard-id-year.md` when the official identifier matters. Do not infer a publication year from the date accessed.

Ordinary documentation filenames also use lowercase kebab-case, for example `authoring.md`, `index.md`, `scientific-policy.md` and `body-of-knowledge-outline.md`. Preserve established repository filenames such as `README.md`, `AGENTS.md`, `LICENSE`, `NOTICE.md` and GitHub community files such as `CONTRIBUTING.md`; tools may depend on their exact spelling. File capitalization does not establish document authority. For an explicit rename, update incoming links, generated navigation, tools, tests and local provenance paths together, and remove the superseded path. Preserve original source paths in provenance and former paths in migration records. Existing files are migrated deliberately, not renamed automatically by this convention.

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
All substantial Markdown knowledge and Reference files use one semantic `# Title`. Models use a short introduction and linked `## Contents`; they do not require Key takeaway, Summary or a fixed set of explanatory headings. An existing Summary may serve as the introduction, and useful existing sections may remain. Other roles and supporting documents retain `## Key takeaway` and `## Summary`. Supply locally sufficient meaning, procedure or representation, examples as appropriate, limits and deeper links. Hide links and ask whether the intended understanding/use task still works; then restore links and check the local summary faithfully preserves its source's relevant conditions. Do **not** copy all linked sources into each file.

Knowledge by role must be self-contained: a Principle explains the actual relationship, not merely a command; a Model includes its representation rather than only a link; a Method includes actionable steps and safeguards; a Practice contains operationally sufficient information **in each stage**, not a list of Methods to visit elsewhere.

## Model meaning and completeness

A Model is a purposeful, simplified representation of a system, phenomenon or structure. It explains the relevant entities, their essential attributes, and their relationships or rules. It enables readers to interpret cases and reason about consequences within stated assumptions and limits. Terms and notation necessary to use the representation are explained locally.

Here, entities are the things or categories represented; attributes are the properties needed to distinguish or describe them for the stated purpose. Essential does not mean exhaustive. Explain relevant attribute values, categories or units where their interpretation matters. Relationships may be structural, classificatory or causal; identify their meaning without implying causation or prediction where the representation does not support it.

Include the representation itself in prose, a table, a diagram, equations or another suitable form. Work through a concrete case when interpretation would otherwise be ambiguous, connecting the entities and attributes through a relationship or rule to a supported conclusion. State the assumptions, evidence and limits that constrain that conclusion. A list of components alone leaves the reader to supply their relationships.

Establish coverage from credible disciplinary sources and the intended scope, rather than the existing file inventory. Compare established accounts where their differences affect the explanation. For a subsystem, use the body-of-knowledge outline as the shared coverage agreement and refine it when investigation reveals missing or misplaced topics. Explain relevant interactions with neighboring subsystems locally; useful overlap is allowed. Identify significant omissions and incomplete coverage.

Establish the foundations needed to follow the explanation, including distinctions that broad outline headings may conceal. Develop important topics to the depth needed for the intended reasoning task; a mention, definition or external link alone may leave the relevant relationship unexplained. Use recognizable topic headings or subsections to make that coverage visible. The existing outline is revisable when source investigation reveals gaps; it is not evidence of sufficient coverage by itself.

Connect the explanations so readers can follow how the representation accounts for a case. Reuse an example where it helps and introduce different cases where necessary; no single example must demonstrate every topic. For interfaces, explain how the representations, constraints or interpretations on the two sides connect, with their conditions and limits. A list of neighboring subsystems is insufficient. These clarifications introduce no prescribed foundation categories, topic count, repeated section structure or new coverage artifact.

These are explanatory responsibilities, not section names. Apart from Contents, the substantive headings, topic count, example format and illustrations follow the subject and reader need. Do not force a universal input–process–output structure or copy one successful Model's layout across disciplines. Preserve canonical definitions while summarizing their necessary meaning at the point of use; links provide depth. The [Model template](templates.md#model-content) illustrates this guidance, and the [Model walkthrough](review.md#walk-through-a-model) checks whether a reader can use it.

The introduction orients the reader to purpose and scope. Contents links to actual sections in document order, using recognizable subject terms and useful subsection links, indented to reflect the heading hierarchy. It makes important coverage visible; it is not a second outline or proof that the scope is complete. Validator 9.2.0 checks the opening and Contents navigation, not scientific coverage or explanation quality. Packages using a Model without the former Key takeaway and Summary opening declare `minimum_validator: "9.2.0"` (or later) in publication.json. Existing domains adopt this change explicitly.

## Method purpose and depth

A Practice need, a reader's difficulty or the discovery of a relevant established procedure can trigger Method documentation. Define the question or intermediate result, then inspect suitable published procedures or analytical approaches before creating or expanding the document. Reuse an existing explanation when it serves the need. A separate Method is useful when the operation has a coherent purpose, repeatable actions and decisions, an interpretable output, and enough independent value to warrant its own explanation. One target Practice can justify it; multiple existing uses are not required. Keep minor actions inline when a separate document adds little value. Recognition in a discipline identifies a candidate, not proof of effectiveness.

Explain the operation deeply enough for competent use: its purpose and applicability, essential inputs and prior knowledge, mechanism or rationale, usable procedure and decisions, outputs and their interpretation, a worked application where useful, and relevant failure modes and limits. Distinguish demonstrated effects from proposed mechanisms and uncertain expectations. Explain alternatives when their differences help the reader choose. These are content responsibilities, not mandatory section names, a fixed sequence or an exhaustive survey. Preserve the common document opening and identity; let the method determine the substantive presentation.

Creating a Method document does not claim invention. Distinguish documenting an established method, adapting or combining supported operations, and proposing an operation whose usefulness remains to be investigated. Preserve established names and meanings when they fit. A reusable adaptation can belong in a Method: identify the supported basis, what changes, why the change fits the intended conditions, and what remains untested. No source needs to prescribe the identical local sequence. Conversely, citations to relevant definitions alone do not establish a procedure's rationale or effectiveness. A proposal must not be presented as established merely because its steps are repeatable; follow the package's declared curation policy for admitting it.

The Method owns the reusable operation, including justified adaptations and its general applicability. The Practice owns the particular goal, selected inputs, contextual choices, coaching questions and next action. Keep these application details in the Practice and retain the essential instructions there when extracting a Method. Link by its meaningful name; neither file should require reading the other to perform its core task. A constructed example illustrates execution and interpretation without claiming observed success. The [Core alignment policy](alignment.md) requires an inspected published basis for standalone Core Methods and keeps unsupported proposals in Practices or private investigation notes.

Work from the need through source investigation and explanation to contextual application. Observations from use may reveal an unclear explanation, unsuitable application conditions or a limitation requiring further investigation; they do not automatically establish a new general claim. Revise the owning explanation or Practice accordingly, preserving the evidence and uncertainty. This is authoring guidance, not a new scientific Method or compulsory workflow artifact.

## Practice responsibilities

A Practice must provide enough information to act, interpret results and choose the next action. Authors may combine these responsibilities and organize them according to the task. These are requirements for useful content, not a prescribed set of headings or fields in every stage.

| Required responsibility | What must be clear to the reader |
|---|---|
| Outcome and scope | What the Practice helps accomplish, where it applies and what counts as success |
| Necessary starting conditions | The knowledge, materials, inputs and relevant constraints needed to begin; do not invent prerequisites |
| Usable actions | What to do, with essential instructions available locally |
| Essential reasoning | Why important choices matter and the relationships needed to adapt them |
| Observations and interpretation | How to judge results against explicit criteria, including relevant quality, cost or effort trade-offs and uncertainty |
| Adaptation and completion | How to continue, finish, pause or obtain help; which choices can change, which constraints must remain, and how to judge an adjustment |
| Evidence boundaries | Which statements are source-supported, authored choices, illustrative cases or actual observations; available reference results and their conditions, or what remains untested |

Explain shared context once and retain the conditions needed at each point of use. A short task may combine an action, reason, observation and next decision in one paragraph. A complex task may need several steps or branches. Cover consequential or likely difficulties rather than attempting an exhaustive list of hypothetical failures. Links add depth; they must not contain instructions essential to performing a stage.

When a method choice materially affects the outcome, explain beside the action why it fits the goal and current conditions, relevant alternatives and trade-offs, and what observation would justify changing it. Distinguish source-supported findings, local observations and author judgment; a reasonable choice is not proof of superiority. The Method owns the reusable operation and its general applicability and limits; the Practice owns contextual selection, adaptation and how the result informs the next decision. Keep essential instructions local. Ordinary actions do not each need a Method file, and stages need not correspond one-to-one with Methods. No separate comparison section or exhaustive alternatives list is required.

Success criteria may be quantitative or qualitative; they must let the reader distinguish a useful result from completion of the steps alone. Explain relevant trade-offs: faster work may not be better if accuracy falls. Where previous results are available, identify their source, task, conditions and evaluation basis before using them as a reference. If no comparable outcome evidence exists, state that limit rather than inventing a benchmark or claiming proven effectiveness. Repeatable instructions do not guarantee equal or better outcomes in another setting.

Make adaptation boundaries intelligible: explain why a constraint matters and distinguish it from a replaceable tool, example or sequence choice. When improvement is needed, connect an observed limitation to a proposed change and its expected benefit, describe a proportionate way to examine the result, and state what would support retaining, revising or abandoning the change. Keep relevant conditions comparable where feasible and record differences that limit interpretation. A before-and-after difference alone does not isolate the change's effect. An inconclusive result can justify a provisional choice or further investigation; it is not proof of improvement. These responsibilities belong beside the relevant actions, not in a new mandatory section or scoring system.

## Practice stages

### Required format

Use the common identity metadata with `type: "practice"` and the steps-first profile described under Format and tool compatibility. Retain one title, Key takeaway, Summary, a linked stage map, substantive inline stages and a current practice summary. The current summary contains only actual recorded experience or an explicitly blank record; a constructed example is not a successful run.

A stage heading uses **exactly** the compact pattern below, consecutively numbered in its current recommended/default order:

```markdown
## Stage1 Breathing and air access
## Stage2 Body support and recovery
## Stage3 Kick preparation and completion
```

**Stage numbers communicate recommended order**, not mandatory sequential completion and not permanent identity. Stage prerequisites and real-world safety/authority boundaries state actual dependencies. Keep names meaningful and preserve stable links when revising existing Practices. If stages move or names change, update the stage map and affected incoming links together.

Keep substantive actions inline under each stage, after the context and prerequisites needed to begin. Use connected prose, a list, a table or a combination according to the task. Steps-first means making the actions and decisions usable at the point of need; it does not prescribe list markers, a fixed number of stages or a particular number of actions.

### Recommended presentation

Place explanations and decision support beside the actions they clarify. Use an example when the expected action or result would otherwise be ambiguous, a table when alternatives need comparison, or a diagram when a relationship is difficult to express compactly. These aids are optional unless needed to make the particular instructions understandable; no example or illustration quota applies.

Do not require `Goal`, `Why`, `What to do`, `What to observe`, `Success signal`, or `Next` at the start of every stage. Use labels only where helpful. Combine responsibilities in natural prose and avoid repeating the same information as an introduction, card and procedure. Prompts, checklists and record templates are optional aids, not additional required sections. Keep stages in the same file unless a split genuinely improves use, and do not add filler to satisfy a word-count threshold.

## Supporting material at the point of use

Link the first useful mention of a Concept, Model or Method to its owning document with ordinary Markdown. Explain the necessary distinction, relationship or operation locally, including relevant conditions and limits. Supporting links provide depth; their presence does not make a stage dependent on them, and their absence does not establish completeness. Avoid repeated links that add no reader value.

Place the support beside the action it clarifies. Add a worked example when the required output would otherwise be ambiguous, a decision table when outcomes lead to different actions, and a diagram when a relationship is hard to express compactly. Explain the visual's essential meaning in nearby text. For quantitative charts retain data, units, scale choices and interpretation; label synthetic data and do not manufacture results.

Prefer text diagrams and Markdown tables for simple relationships. When an image is useful, embed a local PNG or SVG through ordinary Markdown image syntax, add meaningful alternative text and a nearby explanation, and include its source/rights information. Keep essential text available if the image cannot render. Avoid hotlinked images and renderer plugins as dependencies for understanding; external images receive a checker warning rather than an assumption of offline availability.

Link directly to relevant websites where useful, with a short annotation stating what to inspect, what it supports and the important limit. Maintain the full publication identity and inspection extent in `references/`. Essential instructions stay inline. A collection of links is not a self-contained Practice, and embedding a third-party article is not a substitute for synthesis.

## Selective D2 diagrams

D2 is the preferred editable format when a diagram adds a useful distinction, relationship, decision or feedback path. It is not required in every object or stage. Explanatory diagrams beside the relevant text take priority over cross-file maps. Do not create another knowledge type for diagrams or use a graph to turn a local choice into a scientific Principle.

Keep `.d2` and generated `.svg` together under semantic paths in `diagrams/`. Embed the SVG with ordinary relative Markdown image syntax, meaningful alternative text and a nearby account of its essential meaning. Link the D2 source. Readers do not need D2 or renderer plugins. Never hand-edit the generated SVG. Retain source attribution, synthetic-example labels, limitations and edge meanings in the owning document. Visuals of external knowledge must preserve the source's relation directions and scope.

A knowledge relationship graph must use declared metadata edges. Label the relation type and state which objects and edges were omitted. It is not causal evidence or a compulsory reading path. Keep normal Markdown links outside the SVG for dependable navigation.

Register each diagram with its owning document and reason in `diagrams/manifest.json`. Update text and diagram together when meaning changes. With the pinned renderer, `python -m internal.diagram_tools --write` generates artifacts and `python -m internal.diagram_tools --check` rejects stale outputs or a stale metadata graph. The base validator still checks links/images; separate diagram checks validate rendering, not explanatory accuracy. See [Diagram authoring guide](diagrams.md) for the small implementation and review procedure.

## Format and tool compatibility

The five roles, stage numbering and Markdown navigation contract are unchanged. KPS 9.1.0 relaxes fixed stage layout: existing six-label stages can still be checked, but Core now authors steps-first stages rather than two parallel templates. Mark new Practices `practice_format: "steps-first-v1"` and record `minimum_validator: "9.1.0"` in package metadata. Earlier 9.0 validators reject missing labels and cannot validate the new presentation; the 9.x declaration alone does not make old tools understand it. See [Compatibility](compatibility.md) before migrating a domain.

## Markdown links
KPS uses UTF-8 `.md`, ordinary inline relative file links and conservative heading fragments; avoid application-specific wikilinks, embedded HTML anchors and renderer-dependent extensions. For links to a full file, use `[Text](../models/example.md)` rather than a fragile section fragment. For section links, the destination must match the complete real heading under the chosen lowercase/hyphenated profile:

```markdown
[Stage1 Breathing and air access](#stage1-breathing-and-air-access)

## Stage1 Breathing and air access
```

No YAML identity or prefix such as `TI-03` creates an anchor automatically. When renumbering or renaming a Stage, update the heading, stage map and incoming links together. Strict CommonMark itself does not define heading identifiers; test the actual reader when renderer fidelity is important. The practical navigation examples are included in this document, not a separate competing contract.

## Evidence and reference records
Start with a question and candidate claim, identify required evidence, inspect what sources actually establish, check independence and disagreement when material, and separate source premises from KPS's inference. A single directly authoritative source may establish its own definition; multiple citations to one underlying study are not independent evidence.

A Reference must include its full identity, external URL/DOI, reliable publication/update-date basis or `undated`, access and inspection extent, located relevant claims, limitations and **what it does not establish**. Do not copy restricted full texts into the repository or imply full-text access from abstract-only inspection.

## Validation and review
Run `python validate.py .` and `python -m unittest internal.tests.test_validate`. The checker covers structurally testable elements, including section IDs, stage order/maps, metadata relationships, local image targets, and declared dependency changes. It does not infer usability from list markers, tables, link presence or word counts. Whether a reader can act, interpret a result and choose the next action requires the content review in `docs/review.md`. It is **not** a proof of scientific truth or user comprehension. If a canonical source changes, review affected local summaries before refreshing the dependency snapshot using `--accept-reviewed-summaries`.

Root-level GitHub community and automation files are repository infrastructure rather than KPS knowledge objects; the checker applies KPS-specific Markdown rules to the knowledge/content documents, not the GitHub form templates under `.github/`.

## Core professional alignment policy

Core content 10.0.0 adopts [Source alignment](alignment.md). Its standalone Concepts, Principles, Models and Methods identify the actual source, relation and passage. Source-defined meaning takes precedence over a conflicting local paraphrase; scope differences must not be disguised as equivalence. Package-specific workflows and per-task choices remain in Practices; reusable Method adaptations follow the inspected-basis and disclosure requirements above. Necessary file-format rules remain here as specifications, not scientific Principles.

This is a Core curation decision, not a silent change to the five-role KPS 9.x language. The unchanged 9.1.0 structural checker accepts these files; `internal/tests/test_alignment.py` checks the additional live Core source-alignment declarations. A passing test cannot determine authority, faithfulness or scientific validity. Other domain packages adopt the policy separately rather than being changed by this release.

## Practical navigation and viewer checks

KPS object IDs are metadata, not heading fragments. For a heading `## Stage1 Capture a record`, link to `#stage1-capture-a-record`; when renaming it, update inbound links. Avoid application-specific Markdown anchors and test the actual reader, since renderers differ.

**Click test:** Follow a real stage-map link in the intended viewer, use Back, and repeat after changing a heading. A passing link parser cannot establish viewer behavior. Check rendered images with the essential explanations hidden and restored.

See the [GitHub section-link reference](../references/github-undated-markdown-formatting.md) and [Markdown compatibility guidance](compatibility.md) for limits; the [reader review guide](review.md) addresses usability beyond syntax.

