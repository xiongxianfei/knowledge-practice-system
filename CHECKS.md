---
package_version: "9.0.1"
language: "KPS 9.x"
reviewed: "2026-10-07"
---

# Validation and quality limits

## Key takeaway
KPS publication tooling checks local links, metadata, stage structure and declared dependency changes, but cannot prove knowledge correctness.

## Summary
KPS publication tooling checks local links, metadata, stage structure and declared dependency changes, but cannot prove knowledge correctness.

## What to run
From the root of the repository, run:

```bash
python validate.py .
python test_validate.py
```

The public GitHub Actions workflow runs these checks on changes to the default branch and on pull requests. It requires no credentials other than the read-only checkout provided by GitHub.

## What it checks
The included checker verifies local file and heading fragments, required KPS content conventions, YAML identity relationships, stage maps, sequential stage numbering, missing Method sections, selected structural hazards, and whether canonical dependency changes require summary review. The regression tests deliberately introduce structural errors and check that validation rejects them.

## What it cannot check
Checks do **not** establish that a Proposition/Principle is true, an intervention works, a source is sufficient for a claim, someone understands the explanation, or any swimmer or engineer is competent. Expert/content review remains necessary.

## Dependency review
When the validator flags a stale summary, inspect the changed canonical source and each affected receiving file. Only after completing the review run `python validate.py . --accept-reviewed-summaries`, then rerun ordinary validation. Do not run the refresh flag merely to make CI green.

## Release artifacts
A tagged downloadable release can include a generated checksum manifest for reproducibility. The living Git repository intentionally does not store a frozen archive checksum manifest that would become stale after every ordinary edit. Git itself identifies committed content by commit hashes.
