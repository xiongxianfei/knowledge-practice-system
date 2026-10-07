---
id: "kps:me:classify-knowledge"
type: "method"
version: "9.0.0"
language: "KPS 9.x"
status: "active"
reviewed: "2026-10-07"
basis_kind: "authored method; supporting findings separately attributed"
confidence: "proposed implementation, not independently validated"
uses_principles: []
uses_models: ["kps:mo:knowledge-role-model"]
references: []
perspectives: ["knowledge-representation", "evidence-reasoning"]
---

# Classify knowledge

## Key takeaway

Place useful material according to its primary function, without recreating rules inside principles/.

## Summary

A single paragraph can mix a definition, an empirical relationship and an instruction. Classifying by file title alone preserves that ambiguity. Input: “Keep exactly one owner.” If it establishes a selected cardinality, store it in a Model or Method. Extract a separate Principle only when a reusable explanatory relationship survives without the cardinality.

## Inputs and prerequisites

A concrete question, the material or actual record to inspect, and enough context to distinguish observed information from a proposed interpretation. No result is assumed in advance.

## Local explanatory basis

A recorded claim, action and observation have different roles. Making the intended test and its limits explicit lets a later reader inspect the decision without treating a plausible explanation as a measured result.

## Objective
Place useful material according to its primary function, without recreating rules inside principles/.

## Rationale
A single paragraph can mix a definition, an empirical relationship and an instruction. Classifying by file title alone preserves that ambiguity.

## Evidence and reasoning
Use [Knowledge role model](../models/knowledge-role-model.md). The classifier is a KPS convention; there is no claim of scientific discovery of five natural categories.

## Steps
1. State what the material contributes in one sentence before choosing a folder.
2. Use Concept for a distinction; Principle for an independently useful explanation; Model for structured relationships; Method for an operation; Practice for orchestration.
3. For a supposed Principle, remove the preferred REM/KPS/Swim implementation. Does the explanation still make sense and allow alternatives? If not, keep the rule in its Model or Method.
4. Separate fact, interpretation, decision and personal cue. Do not split every sentence; retain local reasoning when it has no independent reuse.
5. Search existing identities and definitions. Revise a matching object or create one coherent new object. A bookmark becomes a Reference, not a Concept.

## Expected effect
A classification decision with the mixed parts either separated or explicitly labelled.

## Validation and counterevidence
A reader can state why the object has its type without relying on its filename. “Keep one source because consistency matters” fails the Principle test.

## Limits
Grammar is a warning signal, not a semantic test. A declarative-sounding rule can still be prescriptive.

## Local evidence summary

This file uses KPS’s declared conventions or an explicit reasoning argument rather than claiming an externally tested intervention. Its explanation and counterexample are local; linked objects identify reusable connections, not independent confirmation.

## Deeper knowledge

Canonical dependencies and Reference records provide additional derivation, source inspection and alternatives. They are not required to carry out the local explanation or procedure.

- **Models:** [Knowledge role model](../models/knowledge-role-model.md)
