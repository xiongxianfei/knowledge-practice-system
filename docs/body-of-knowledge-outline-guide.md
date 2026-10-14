---
package_version: "11.0.0"
language: "KPS 9.x"
status: "draft"
reviewed: null
---

# Create a body of knowledge outline

## Key takeaway

Reuse established subject structures, set the depth through the learner's intended capabilities, and map existing explanations only after defining required coverage.

## Summary

A body of knowledge is the organized knowledge and skills within a subject and stated scope. Its outline describes what the package needs to cover, how deeply, and where readers can find support. It guides development as well as reading. In KPS, maintain it as `docs/body-of-knowledge-outline.md`, supported by an overall illustration when useful.

This guide describes a KPS authoring approach, not an externally standardized taxonomy or an additional knowledge role. It applies the [authoring contract](authoring.md); the [reusable template](templates.md#body-of-knowledge-outline) supplies a starting document. Concepts, Principles, Models, Methods and Practices remain the primary knowledge roles. The outline belongs to shared knowledge navigation; Practices own activity sequences.

## Define the target and boundaries

Write down the intended reader, what they should understand and be able to do, their starting knowledge, the relevant context or tradition, and the depth of this edition. Name exclusions and optional branches. For example, learning a suitable song by ear does not require beginning with notation reading.

Select one or a few realistic Practice targets to make the scope concrete. Keep the full selected subject coverage visible even when the first Practice uses only a small part. A beginner foundation can include awareness of a topic whose advanced application is deferred.

## Reuse established subject structures

Inspect suitable textbooks, curricula, professional syllabuses or other authoritative subject accounts. Compare their purposes, divisions, terminology and depth. Use claim-specific research when developing explanations of mechanisms or procedures. There is no fixed source quota: inspect enough to justify the chosen scope and preserve material disagreement.

Record which publication and sections were actually inspected, what structure they contribute, what is excluded and what is an authored adaptation. Use the package's Reference records for publication details and access limits. A syllabus can support including a topic without establishing that a proposed exercise is effective.

Choose area and topic boundaries from those accounts and the target. Where accounts differ, explain the selected interpretation or keep alternatives visible. Do not silently merge incompatible meanings. If a source is unavailable, mark the relevant selection as provisional and identify the source work still needed.

## Build the complete topic outline

List the major areas and their topics together near the top of the document. Use descriptive names and links to the detailed coverage sections. Area numbers are navigation labels unless an actual sequence is explicitly intended.

Choose enough detail to make required coverage visible without turning every term into a document. Topics may overlap; cross-links should explain the connection. The five KPS roles describe how an explanation contributes, so they do not determine the subject divisions. Existing filenames must not determine which topics are included.

## Specify understanding and capability

For each topic, fill these columns before using the file inventory to assess coverage:

| Topic | Understand — required knowledge | Be able to do — intended depth | Existing explanations and gaps |
|---|---|---|---|
| A meaningful subject subdivision | Essential distinctions, mechanisms, relationships and limits | A bounded explanation, comparison, decision, analysis or practical task | Links to relevant material and the specific support still missing |

Use a concrete capability to express depth. Replace a vague goal such as “master pitch” with a bounded target such as comparing an attempted note with a reference and recognizing uncertainty. Some topics require only awareness or explanation at the selected level; do not invent a physical exercise for every row.

These outcomes describe intended learning support. They are not observed learner results, completion certificates or evidence that a proposed activity works. Detailed prerequisites, actions and fallback choices belong in the relevant Practice.

## Map existing explanations and gaps

Use intended Practices while selecting scope and depth, then keep the outline focused on subject coverage. Put task navigation in the README or library, activity sequences in Practices, and development priorities in the relevant issue or work plan. The outline does not need a separate Practice mapping, authoring-instructions table or development roadmap.

Map existing Concepts, Principles, Models, Methods and Practices into the coverage rows. One explanation can support several topics, and a topic can draw on several explanations. Link to canonical material and summarize the relevant contribution; do not create one file per row or one object of every role.

Use plain coverage descriptions consistently:

- **Missing:** no relevant local explanation or recorded source contribution has been identified.
- **Source only:** a relevant external contribution is recorded, but a local explanation is missing.
- **Partial:** local material contributes, but a stated part of the required coverage remains unsupported.
- **Covered at stated depth:** local material addresses the row's requirements. This says nothing about a particular learner's competence.

Name the remaining gap beside the links. A topic-level link to a Practice is useful when it supplies part of the actual coverage; it need not become a separate task catalogue. Use those gaps to prioritize development outside the outline. Develop a focused Practice and its supporting explanations together, keeping the wider coverage outline intact.

## Illustrate the written outline

Settle the area names and scope first. Create one readable overall illustration showing every major area and the learning purpose. Add detailed illustrations only when they make the topic structure easier to read. Do not put all coverage-table prose into the picture.

Embed the overview near the beginning of the outline and reuse it in the README. Store the asset under `diagrams/`, for example `body-of-knowledge-overview.png`, with the exact generation prompt for AI artwork or the editable source for a diagram. Include meaningful alternative text, a full-size link and a caption explaining intended coverage. Keep the complete text outline available when images cannot render.

Match labels to the written outline, distinguish optional branches, and explain any arrows. Visual associations must not imply causation, compulsory learning order or completed coverage. Inspect typography and completeness at normal reading size. Follow [diagram guidance](diagrams.md#illustrated-project-overview) for the distinction between editorial illustrations and reproducible D2 diagrams.

## Worked example from singing

The [singing outline at commit 526c765](https://github.com/xiongxianfei/singing-kps/blob/526c765661f579dca3e865135fc4a8f04003abda/docs/body-of-knowledge-outline.md) is a concrete authoring example. This fixed version keeps the example interpretable as the domain develops. It is linked for further reading; the reasoning needed here is summarized below.

| Decision | Singing application |
|---|---|
| Target | Help a beginner understand singing, learn a short suitable song and make informed practice choices. |
| Source structure | Its recorded NATS syllabus contribution concerns voice function and learning; Trinity contributes performance, diction and reading; Open Music Theory contributes musical foundations; NIDCD supplies voice-care boundaries. Their purposes differ. |
| Selection | Ten areas and 34 topics form an authored beginner scope. Western notation is an optional branch; advanced techniques and clinical care are excluded. The ten-area grouping is not attributed to any single source. |
| Required coverage | Reference-pitch matching includes a reference, pitch and octave comparisons, and uncertainty. The target is to attempt a comfortable reference note in a supported task and compare the result. |
| Current gap in that version | The existing first session addresses contour and pulse. It does not supply the reference-pitch matching lesson. |
| Development choice | Propose “Match a reference pitch” with supporting explanations and usable reference audio. Follow with rhythm and melody work toward a suitable song, allowing parallel development where appropriate. |
| Visual summary | One overall illustration shows all ten areas; two detailed illustrations show the 34 topics. All are embedded in the written outline. |

The ten areas are voice production and breathing; vocal care; listening, pitch and intonation; beat, rhythm and meter; resonance and timbre; registers, range and transitions; articulation and diction; notation and sight singing; songs, phrasing and performance; and practice, feedback and skill development.

This example summarizes the inspected repository document and its recorded source basis. It does not claim a new inspection of those external publications, a completed pitch-matching Practice or a learner trial. The singing scope and topic counts are examples, not defaults for other subjects. That fixed revision includes a Practice pathway; the template here keeps such task navigation outside the coverage outline.

## Maintain one coverage guide

Use the [template](templates.md#body-of-knowledge-outline) to write the outline in the domain repository. Replace placeholders with its actual scope, sources and outcomes. Keep existing explanations and coverage notes aligned as content develops. Update images when the represented structure changes; a stable overall image need not change for every new lesson.

If replacing an existing subject map, consolidate useful content into the outline, update incoming links and remove the superseded coverage document in the same focused change. Existing packages adopt this guidance explicitly; it introduces no new mandatory metadata, language version or automatic migration. The [Core outline](body-of-knowledge-outline.md) applies this guidance to KPS itself.

Use existing package checks for links and structure and inspect whether a reader can identify the scope, a topic's required depth and a relevant Practice or gap. Keep source inspection, author judgment and actual learner observations distinct. No generator, new test suite or separate coverage database is needed.
