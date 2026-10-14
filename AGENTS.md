---
package_version: "11.0.0"
language: "KPS 9.x"
status: "draft"
reviewed: null
---

# Agent guidance

## Key takeaway

Apply the shared Core Engineering Principles together with this repository's authoring, evidence and contribution boundaries.

## Summary

These repository-wide instructions apply to knowledge, code, tools and workflows. The nine Core Engineering Principles are maintained verbatim across the six knowledge repositories; propose shared revisions together and keep domain-specific instructions below. Each repository carries its own copy for independent use. These are working agreements, not scientific KPS Principle objects or a replacement for the authoring contract.

## Project purpose

Help human readers understand, apply and develop knowledge using the five KPS roles. Core owns the authoring convention and shared validator; domain packages adopt changes explicitly. Use the [subject map](docs/subject-map.md) for topics and the [library](docs/library.md) for existing objects.

## Core Engineering Principles

1. **Self-contained knowledge.** Make each substantive document understandable on its own: explain the problem, essential terms, prerequisites, mechanisms, examples, and boundaries. Link to deeper material without requiring readers to follow links to understand the core argument. Keep canonical definitions in one place; avoid needless duplication.

2. **Reader-centered quality.** Evaluate whether a reader can explain *what happens, how, why, and when*; apply the knowledge to a realistic problem; predict likely outcomes and failure modes; and recognize opportunities to improve results. Correctness and clear reasoning matter more than polished prose.

3. **Goal-oriented work.** Identify the intended reader outcome before substantial work. Choose the smallest sufficient change; prioritize important knowledge gaps and useful results. Avoid speculative infrastructure, redundant research, unnecessary documentation, and rituals that do not advance the goal. Do not skip essential verification to save effort.

4. **Reuse before invention.** Look for established theory, standards, sources, methods, libraries, and tools before building alternatives. Prefer suitable, proven approaches; weigh fitness, reliability, cost, maintenance, and lock-in. Create custom solutions only when a material requirement justifies them.

5. **Mechanisms before memorization.** Explain causal relationships, relevant variables, assumptions, boundary conditions, and trade-offs. Show how the mechanism informs decisions and practical action. Surface possible improvements and testable hypotheses, clearly separating proposed innovations from demonstrated results.

6. **Delete obsolete internal compatibility.** When replacing internal code, paths, workflows, or knowledge structures, migrate affected uses and remove superseded implementations. Do not add internal legacy shims, deprecated aliases, dual-write logic, or competing canonical documents. Assess *external* contracts separately and honor actual obligations. Preserve unique evidence, provenance, and historically useful knowledge; remove obsolete representations, not valuable facts.

7. **Fix the problem class.** For defects or inconsistencies, identify the underlying cause and check for related instances. Make the smallest coherent change that addresses the confirmed class; add proportionate checks or regression coverage where useful. Do not turn isolated issues into speculative redesigns.

8. **Think before acting.** Before substantive work, clarify the intended outcome, inspect relevant context, challenge important assumptions, and consider dependencies, risks, and the simplest sound approach. Scale planning to the task: small, reversible changes need no formal plan; consequential or hard-to-reverse changes deserve more analysis. Avoid analysis that does not improve the decision.

9. **Test the core first; validate by risk.** First verify the main outcome: for software, the changed behavior; for knowledge, whether a reader can use it to reason through a representative problem. Expand to affected dependencies, contracts, edge cases, or regressions when the likelihood and impact of failure justify it. Prefer focused checks over redundant tests or unrelated full suites; never omit essential verification merely to save time.

## Project guidance

- Read [Authoring](docs/authoring.md) before changes. For knowledge claims, apply [Source alignment](docs/alignment.md): inspect the located source, retain uncertainty and distinguish source meaning, inference and local design.
- Keep Concepts, Principles, Models, Methods and Practices in their primary roles. Principles explain relationships; Models contain representations; Methods explain checkable operations. References record publications and located contributions.
- For Practice changes, use steps-first content, substantive inline `StageN` stages and valid stage-map links. Preserve prerequisites, interpretation and fallback decisions. Use [Reader review](docs/review.md); do not recreate mandatory six-label stages or impose a word-count threshold.
- Reuse established subject structure for the target Practice. Follow the [body of knowledge outline guide](docs/body-of-knowledge-outline-guide.md) for new coverage documents: define scope, required understanding and capabilities before mapping existing explanations and gaps. Core's current subject map remains its navigation until explicitly migrated. Practices own activity sequences; useful overlap between explanations is allowed.
- Do not invent source inspection, tests, reader trials, approvals, access or results. A self-review is not an independent review; keep unsupported claims provisional.
- For visuals, follow [Diagram guidance](docs/diagrams.md). Keep edge meanings, limits, alternative text and nearby explanations explicit. Keep D2 sources with rendered SVGs and never edit generated SVGs independently; metadata graphs use justified declared relationships. Illustrated overviews follow their separate guidance there.

## Verification

Run from the repository root:

```bash
python3 validate.py .
python3 -m unittest discover -s internal/tests -p 'test_*.py'
python3 -m internal.diagram_tools --check --root .
```

These are the structure, alignment and diagram checks required for publication. Use the pinned D2 renderer documented in [Diagram guidance](docs/diagrams.md). For changed Practices, also inspect the rendered Markdown and intended reader task. Review changed source meaning and receiving summaries before accepting dependency fingerprints; never refresh merely to make a check pass. Report actual results and limits: structural success does not establish scientific truth or reader comprehension.

## Contribution workflow

Follow [Contributing](.github/CONTRIBUTING.md): one coherent change, one branch and one PR to `main`. Honor existing owner authorization for merging after successful checks; otherwise leave the PR for review. Tags and official releases require an explicit request. Preserve unrelated work, protections and LF text under `.gitattributes`; never disable checks to force publication. Do not impose Core upgrades on sibling domains.
