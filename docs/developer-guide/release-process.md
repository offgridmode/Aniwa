# Release Process

This document explains the official release workflow for Aniwa, including:

- versioning
- testing
- packaging
- PyPI publishing
- GitHub releases
- release validation
- long-term release strategy

The goal is to ensure releases remain:

```text
stable, reproducible, professional, and scalable
```

---

# Purpose of the Release Process

A strong release process ensures:

- stable public versions
- reproducible builds
- trusted package distribution
- predictable versioning
- healthy project evolution

---

# Release Philosophy

Aniwa releases should prioritize:

| Principle | Purpose |
|---|---|
| stability | reliable installations |
| reproducibility | consistent builds |
| clarity | understandable releases |
| maintainability | long-term scalability |
| professionalism | trusted ecosystem |

---

# Versioning Philosophy

Aniwa follows:

```text
Semantic Versioning (SemVer)
```

---

# Semantic Versioning Structure

Format:

```text
MAJOR.MINOR.PATCH
```

---

# Example

Example:

```text
0.1.1
```

---

# Meaning of Each Version Type

| Type | Meaning |
|---|---|
| MAJOR | breaking changes |
| MINOR | new features |
| PATCH | bug fixes |

---

# Example Release Progression

Example:

```text
0.1.0
0.1.1
0.2.0
1.0.0
```

---

# Current Release Phase

Aniwa is currently in:

```text
early foundational development
```

---

# Why Early Versions Matter

Early releases establish:

- architecture foundations
- contributor workflows
- ecosystem trust

---

# Release Workflow Overview

High-level release flow:

```text
develop
→ test
→ version bump
→ build
→ validate
→ publish
→ release notes
```

---

# Step 1 — Finalize Features

Before releasing:

- merge stable PRs
- finish testing
- complete documentation

---

# Step 2 — Run All Tests

Always run:

```bash
pytest
```

---

# Why Testing Matters

Testing prevents:

- regressions
- broken releases
- installation failures

---

# Step 3 — Run Linting

Run:

```bash
ruff check .
```

---

# Step 4 — Format the Codebase

Run:

```bash
black .
```

---

# Step 5 — Verify CLI Functionality

Test core commands manually.

Example:

```bash
aniwa examples/customers.csv
```

---

# Step 6 — Verify Report Systems

Test:

- JSON reports
- HTML reports
- Markdown reports
- Excel reports
- PDF reports

---

# Step 7 — Verify Config System

Test:

- YAML configs
- TOML configs
- JSON configs

---

# Step 8 — Update Version Number

Update the version in:

```text
aniwa/__init__.py
```

---

# Example

Example:

```python
__version__ = "0.1.2"
```

---

# Step 9 — Update README

Update:

- features
- examples
- roadmap
- release information

---

# Step 10 — Update Documentation

Verify docs remain current.

Update:

- docs/
- examples/
- architecture guides

---

# Step 11 — Review Changelog

Document:

- features
- fixes
- improvements
- breaking changes

---

# Recommended Changelog Sections

Suggested structure:

| Section |
|---|
| Added |
| Improved |
| Fixed |
| Deprecated |

---

# Future Changelog File

Recommended future file:

```text
CHANGELOG.md
```

---

# Step 12 — Build the Package

Build distributions.

Example:

```bash
python -m build
```

---

# Why Builds Matter

Builds generate:

| Artifact |
|---|
| wheel |
| source distribution |

---

# Build Output Location

Artifacts appear in:

```text
dist/
```

---

# Example Build Artifacts

Example:

```text
dist/
├── aniwa-0.1.2.tar.gz
├── aniwa-0.1.2-py3-none-any.whl
```

---

# Step 13 — Validate the Build

Check package integrity.

Example:

```bash
twine check dist/*
```

---

# Why Validation Matters

Validation detects:

- broken metadata
- malformed packages
- publishing issues

---

# Step 14 — Upload to PyPI

Publish the package.

Example:

```bash
twine upload dist/*
```

---

# Recommended Secure Upload Method

Recommended:

```bash
twine upload dist/* -u __token__
```

---

# Why API Tokens Matter

API tokens improve:

- security
- account protection
- automation

---

# Using .pypirc

You may configure:

```text
.pypirc
```

to avoid re-entering tokens repeatedly.

---

# Example .pypirc

Example:

```ini
[pypi]
username = __token__
password = pypi-xxxxxxxx
```

---

# Step 15 — Verify PyPI Installation

After publishing:

```bash
pip install --upgrade aniwa
```

---

# Verify the CLI

Test:

```bash
aniwa --help
```

---

# Step 16 — Create Git Tag

Create a release tag.

Example:

```bash
git tag v0.1.2
```

---

# Push Tags

Example:

```bash
git push origin v0.1.2
```

---

# Why Tags Matter

Tags provide:

- historical tracking
- release references
- reproducibility

---

# Step 17 — Create GitHub Release

Create a GitHub Release using:

- version tag
- release notes
- changelog summary

---

# Why GitHub Releases Matter

GitHub releases improve:

- discoverability
- community visibility
- release history

---

# Recommended Release Title

Example:

```text
Aniwa v0.1.2
```

---

# Recommended Release Structure

Suggested release notes:

| Section |
|---|
| Highlights |
| Added |
| Improved |
| Fixed |
| Next Steps |

---

# Release Validation Checklist

Before publishing, verify:

| Check |
|---|
| tests pass |
| linting passes |
| formatting passes |
| docs updated |
| examples valid |
| package builds |
| CLI works |

---

# Example Manual Validation Commands

---

# Run Tests

```bash
pytest
```

---

# Run Formatter

```bash
black .
```

---

# Run Linter

```bash
ruff check .
```

---

# Build Package

```bash
python -m build
```

---

# Validate Build

```bash
twine check dist/*
```

---

# Install Locally

```bash
pip install -e .
```

---

# Test CLI

```bash
aniwa examples/customers.csv
```

---

# Release Branch Philosophy

Future releases may use:

```text
release branches
```

---

# Why Release Branches Matter

Release branches improve:

- stabilization
- coordinated releases
- enterprise workflows

---

# Future CI/CD Release Automation

Future systems may automate:

- testing
- builds
- publishing
- GitHub releases

---

# Potential Future Tooling

Potential systems:

| Tool |
|---|
| GitHub Actions |
| Dependabot |
| release pipelines |

---

# Example Future Workflow

Potential future flow:

```text
push tag
→ CI pipeline
→ tests
→ build
→ publish
→ release
```

---

# Pre-Release Philosophy

Future versions may support:

| Type |
|---|
| alpha |
| beta |
| rc |

---

# Example Pre-Release Versions

Examples:

```text
0.2.0-alpha
0.2.0-beta
1.0.0-rc1
```

---

# Why Pre-Releases Matter

Pre-releases improve:

- testing
- feedback collection
- stabilization

---

# Backward Compatibility Philosophy

Minor and patch releases should avoid:

```text
unnecessary breaking changes
```

---

# Breaking Change Philosophy

Breaking changes should:

- be documented clearly
- be minimized
- justify architectural value

---

# Release Documentation Philosophy

Every release should include:

- release notes
- migration guidance
- feature summaries

---

# Security Release Philosophy

Security fixes should prioritize:

- rapid patching
- transparent communication
- safe upgrades

---

# Long-Term Release Strategy

Aniwa aims to evolve toward:

```text
enterprise-grade release engineering
```

---

# Future Enterprise Release Features

Potential future systems:

| Feature |
|---|
| signed packages |
| reproducible builds |
| release verification |
| enterprise support channels |

---

# Release Frequency Philosophy

Releases should prioritize:

```text
quality over speed
```

---

# Why Stable Releases Matter

Stable releases improve:

- trust
- adoption
- ecosystem confidence

---

# Contributor Release Expectations

Contributors should:

- test thoroughly
- document changes
- avoid rushed merges

---

# Release Anti-Patterns

Avoid:

| Anti-Pattern |
|---|
| untested releases |
| undocumented breaking changes |
| rushed publishing |
| skipping validation |

---

# Long-Term Vision

Aniwa’s release process is evolving toward:

```text
professional-grade open-source release infrastructure
```

---

# Final Philosophy

The release process exists to ensure that:

```text
every Aniwa release is stable, trustworthy, maintainable, and production-quality
```

---

# Related Documentation

Continue with:

- developer-guide/testing.md
- developer-guide/local-development.md
- architecture/system-design.md
- CONTRIBUTING.md