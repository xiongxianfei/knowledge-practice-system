---
package_version: "9.0.1"
language: "KPS 9.x"
reviewed: "2026-10-07"
---

# Security policy

## Key takeaway
Validation scripts run on untrusted contributions and do not establish correctness or safety beyond their documented structural checks.

## Summary
Validation scripts run on untrusted contributions and do not establish correctness or safety beyond their documented structural checks.

## Reporting
If GitHub private vulnerability reporting is enabled for the public repository, use the repository's Security tab and private-reporting feature. Do not disclose active security vulnerabilities, secrets, credentials or exploit instructions in public issues. If private reporting is not configured, contact the owner through a private contact channel that the owner supplies on GitHub before sending sensitive information.

## Scope
This repository contains Markdown knowledge and a dependency-free Python validator. Structural checks are not domain certification, evidence verification, medical advice, or a guarantee that community-contributed instructions are safe. Domain authors must assess their own high-stakes use.

## Handling contributions
Review security-sensitive changes to `validate.py`, workflow configuration, and untrusted parsing logic. GitHub Actions checks should use read-only permissions and run without publication credentials on untrusted pull requests. Do not store credentials in source files or workflow examples.
