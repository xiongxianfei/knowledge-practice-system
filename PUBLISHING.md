---
package_version: "9.0.1"
language: "KPS 9.x"
reviewed: "2026-10-07"
---

# Publishing KPS on GitHub

## Key takeaway
Create one independent public repository for KPS, review the proposed license and community contacts, and publish the validated sources without bundling unrelated domain packages.

## Summary
Create one independent public repository for KPS, review the proposed license and community contacts, and publish the validated sources without bundling unrelated domain packages.

## Before publishing
- Review [LICENSE](LICENSE), copyright attribution and external references. MIT is the **proposed default** for KPS-authored documentation and code; check that you have rights to publish all included material under it.
- Supply a private moderation/contact route for [Code of conduct](CODE_OF_CONDUCT.md) and [Security](SECURITY.md), particularly if you want outsiders to report issues privately.
- Review the history and files for private data, secrets or accidentally bundled third-party materials.
- Confirm that `AUTHORING.md` matches the desired contract and `publication.json` records the correct release.
- Run validation and check the source files directly before publishing publicly.

## Create the repository
On GitHub choose **New repository**. Use the proposed name `knowledge-practice-system`, select **Public**, and leave README, .gitignore and License creation **unchecked** because they are included locally. The user interface may differ; GitHub's official creation guide describes the current flow: https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository

## Push the files
From a terminal in the extracted root directory:

```bash
git init -b main
git add .
git commit -m "Publish Knowledge Practice System 9.0.1"
git remote add origin https://github.com/YOUR-ACCOUNT/knowledge-practice-system.git
git push -u origin main
```

Replace `YOUR-ACCOUNT` with the actual repository owner, and authenticate using your own supported GitHub credential flow. If you create or clone an initialized repository instead of an empty one, follow GitHub's standard merge/push instructions rather than forcing histories.

## After publishing
Enable Issues and pull requests, review the code-of-conduct and security contact, configure branch protection or branch rules as appropriate, verify the [validation workflow](.github/workflows/validate.yml), and tag a release only after inspecting its checked content. Contributions should follow [Contributing](CONTRIBUTING.md). If the author's knowledge package is later hosted as GitHub Pages or MkDocs, keep the same source in one repository rather than maintaining inconsistent published copies.

## Scope
The GitHub repository is an open-source **knowledge framework**. Swim and REM are independent applications and are intentionally not included in its source tree.
