---
package_version: "11.0.0"
language: "KPS 9.x"
reviewed: null
---


# Reusable authoring templates

## Key takeaway
These are non-normative examples implementing the [authoring contract](authoring.md).

A template supports the job of the knowledge type; it does not prove correctness or require every field to become a file.

## Summary
All objects need identity, meaning, locally sufficient content, scope and support. Copy only the useful fields, replacing placeholders with real content. The examples below are fenced templates, not live published knowledge. Reference records support the five knowledge types rather than becoming a sixth type.

For subject coverage rather than an individual object, use the [body of knowledge outline template](#body-of-knowledge-outline) and its [authoring guide](body-of-knowledge-outline-guide.md).

## Body of knowledge outline

Copy the fenced document into `docs/body-of-knowledge-outline.md` in the domain package. Replace every placeholder and example link with actual content, using the domain's package version. The topic and Practice names below are placeholders, not a prescribed subject structure. Repeat area sections as needed. Add image links only after the assets exist. This is supporting navigation with no knowledge-object `id` or `type`; it does not replace a Practice.

```markdown
---
package_version: "REPLACE_WITH_DOMAIN_VERSION"
language: "KPS 9.x"
status: "draft"
reviewed: null
---

# Subject Body of Knowledge Outline

## Key takeaway

State what this subject coverage enables the intended reader to understand and do.

## Summary

Describe the selected subject scope and distinguish intended coverage from the
knowledge and Practices already available.

## Purpose and scope

- Audience and starting knowledge: replace with actual readers and prerequisites.
- Learning target: state a concrete capability or set of capabilities.
- Depth and context: state the level, tradition, setting or other relevant limits.
- Optional branches and exclusions: identify what is optional or outside this edition.

## Overall illustration

When the asset exists, embed it here with descriptive alternative text:
![Replace with a meaningful overview description](../diagrams/body-of-knowledge-overview.png)

[Open the overview at full size](../diagrams/body-of-knowledge-overview.png).
Explain the grouping and any connections. State that this represents intended
coverage, and whether numbers or arrows indicate an actual sequence.
Link the actual editable source or saved generation prompt beside the image.

## Overall outline

| Area | Topics to cover |
|---|---|
| [Area name](#area-name) | Topic name; further topics selected from established accounts |

## Required coverage

Understanding names the required knowledge; capability states the intended depth.
Coverage describes available support, not learner competence. Use Missing,
Source only, Partial or Covered at stated depth, with a specific explanation.

### Area name

| Topic | Understand — required knowledge | Be able to do — intended depth | Existing explanations and gaps |
|---|---|---|---|
| Topic name | Relevant meanings, mechanisms, relationships and limits | A bounded explanation, analysis, decision or task | Status; actual links where available; specific missing support |

## Connections between topics

| Connected topics | Relationship and why it matters |
|---|---|
| Selected topics | Explain a dependency, overlap or other meaningful connection |

## Source basis and adaptations

| Established account | Inspected contribution | Selection and limits |
|---|---|---|
| Actual publication Reference link | Located structure or topic contribution and inspected extent | What was selected, adapted, excluded or left provisional |

Explain any locally authored grouping and disagreements between accounts.
Do not imply that a syllabus establishes the effectiveness of a proposed exercise.

## Maintaining the outline

Keep required topics visible before local explanations exist. Update coverage and
explanation links as content develops. Revise the overview when the represented
structure changes. Reuse explanations across topics where useful; do not require
one file per topic or one object of every KPS role.
```

The [singing worked example](body-of-knowledge-outline-guide.md#worked-example-from-singing) shows how sources, learner targets, coverage and proposed Practices fit together. Use the existing [diagram guidance](diagrams.md) for assets and the package's declared checks for publication.

## Common metadata

Before selecting a template, identify the target Practice, relevant established account and the coherent explanation needed by the reader. A template describes the document's primary job; it does not determine the domain's subdivisions. Include supporting knowledge from other roles inline when needed. Split only for independent use or readability, and retain the relevant source meanings and conditions in overlapping explanations.

```yaml
---
id: "domain:method:meaningful-identity"
type: "method"
version: "1.0.0"
language: "KPS 9.x"
status: "draft"
reviewed: null
uses_principles: []
uses_models: []
references: []
---
```
For the optional dependency-free checker, write metadata values in JSON-compatible YAML as shown. General Markdown content does not depend on that checker.

## Common opening
```markdown
# Meaningful title

## Key takeaway
One useful sentence stating the object itself.

## Summary
What it means, why it matters, how it is used and its main limit.
```

## Concept content
Definition; necessary distinctions; recognizable example and non-example; why it matters; boundaries and evidence; optional deeper links. Do not force procedures into a vocabulary note.

## Principle content
Declarative Statement; explanatory mechanism or relationship; evidence-supported premises; explicit derivation; independently useful applications; limits; possible challenge. Do not disguise a selected instruction as a universal truth. Scientific and domain levels can be metadata; formal or design reasoning must be labelled rather than invented as experiment.

## Model content

Use the following questions to develop a locally sufficient representation. They describe content responsibilities, not compulsory headings. Summarize necessary dependencies inline instead of linking away the explanation.

| Content | Reader question |
|---|---|
| Purpose and scope | What can this Model help explain, and for whom? |
| Entities and attributes | What things or categories matter, and which properties distinguish or describe them? What do the relevant values, categories or units mean? |
| Representation and relationships | How are those things connected or constrained? What does each relation, rule or symbol mean? |
| Worked interpretation | How do the represented attributes and relationships support a conclusion in a concrete case? |
| Assumptions, evidence and limits | What supports the representation, what has been simplified, and where might it fail? |
| Evaluation | How can a reader check the interpretation, identify a mismatch or recognize an unsupported conclusion? |

### Example using the PROV Model

The existing [PROV Data Model](../models/prov-data-model.md) supplies a provenance example. The illustration below reuses its selected relationships; the document names and conversion are synthetic. This is an authoring example, not an observed workflow or a complete PROV specification.

**Purpose and entities.** Explain which input a summary came from and who was associated with its production. An Entity has fixed aspects, such as the particular document version being described. An Activity occurs over time, such as converting that document into a summary. An Agent bears responsibility, such as the editor associated with that conversion. The input document and output summary are separate Entities; their identity and version distinguish which materials are being discussed. These example details do not prescribe required PROV attributes.

**Representation and interpretation.** Read each arrow from left to right:

```text
conversion Activity -- used --> input document Entity
summary Entity -- wasGeneratedBy --> conversion Activity
conversion Activity -- wasAssociatedWith --> editor Agent
summary Entity -- wasDerivedFrom --> input document Entity
```

The first relationship identifies the input used by the conversion; the second identifies the Activity that produced the summary. Association records the responsible Agent, and derivation connects the output to its input. Together these statements let the reader trace the summary's production.

**Assumptions and limits.** The illustration assumes that the recorded identities and relationships describe the intended versions and activity accurately. Even then, the summary may misrepresent its input: provenance does not establish correctness. This selected subset omits the full model's other relationships and constraints and is not a formal serialization.

**Evaluation and support.** Ask which Entity was used, which was generated, and whether the graph establishes that the summary is accurate. The supported answers are the input document, the summary, and no. A reversed `used` arrow would change the stated relationship; a claim of accuracy would exceed what this representation establishes. The [PROV Reference](../references/w3c-2013-prov-dm.md) identifies the underlying W3C publication and inspected scope. This walkthrough applies the existing local explanation; it is not a new conformance or independent reader test.

## Method content
Objective; inputs and prerequisites; rationale; numbered procedure; expected effect; observations and counter-signals; limits or stop conditions; example; deeper evidence. A new comparison procedure is a proposal until used; examples do not establish effectiveness.

## Practice content
This is one example, not a mandatory sequence of supporting headings. Keep the steps locally usable and add only the material that resolves a reader's uncertainty.

Draft the target, prerequisites, output and feedback before building its supporting library, then refine them together. For a learning Practice, an output can be an explanation or an analysis of an unfamiliar case. State what would make that response adequate, what misconception requires revision and what evidence is missing. Existing knowledge can support several Practices without being rewritten into a separate copy for each.

```markdown
# Repair a knowledge link

## Key takeaway
Correct a real target and check it in the intended viewer.

## Summary
Work in a copy of the affected document. Stage numbers show recommended order;
permission and safe working conditions are actual prerequisites.

## Stage map
1. [Stage1 Locate and repair the target](#stage1-locate-and-repair-the-target)

## Stage1 Locate and repair the target
Check the destination before changing the heading.

**Steps**
1. Compare the complete heading with the link's fragment.
2. For "Stage1 Capture a record", use #stage1-capture-a-record.
3. Run the checker and then click the link in the intended viewer.

If the file is missing, repair its path first. If the fragment matches but
navigation fails, inspect viewer support; do not claim a successful click test.

**Worked example**
The short fragment #stage1 does not match the complete example heading.
This is an illustrative repair, not an observed result.

**Useful resource**
[GitHub section links](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#section-links)
explains GitHub heading identifiers, not every reader.

## Current practice summary
Actual document, action, observed result and remaining issue: not recorded.
```

For a branching task, a decision table can replace an ordered list. The inputs, actions and completion/fallback conditions still need to be understandable. Diagrams need a text explanation; quantitative charts need the source data and scale. Never add filler merely to reach a length threshold.

Use `practice_format: "steps-first-v1"` and record a minimum checker of 9.1.0 for this presentation. The old six labels are not required. Practice composition stays optional and must not create circular containment.

## Reference content
Publication identity, creators, publication or update year and its basis, external URL or DOI, actual access date and extent, located claims, evidence family, limitations and non-claims. Use creator-year-short-title filenames, or `undated` when a date was not established. The record must summarize what the source contributes without requiring immediate external access; it is not a copy of the publication.

## Review before publication
Hide links and attempt the intended use; restore links and check the summary remains faithful. Check claim-source fit, headings and fragments, then run the package checker. [Authoring](authoring.md), [Navigation](authoring.md) and [Compatibility](compatibility.md) provide the complete local maintenance instructions.

## Core source alignment example

```yaml
source_alignment: [{"reference":"kps:r:skos","relation":"definition-paraphrase","locator":"Sections 3 and 5"}]
```

Record the actual source and locator, its meaning and boundary, and any qualification. This declaration is not a formal equivalence mapping. KPS-specific authoring routines belong in Practices rather than new generic Methods. The five role labels remain our local organization.
