# Local Development Guide

This document explains how to set up, run, test, and contribute to Aniwa locally.

It is designed for:

- contributors
- maintainers
- open-source collaborators
- future core engineers

The goal is to make local development:

```text
simple, reproducible, and scalable
```

---

# Purpose of Local Development

A strong local development workflow ensures:

- contributors can onboard quickly
- development environments remain consistent
- features can be tested safely
- releases remain stable

---

# Development Philosophy

Aniwa development should feel:

```text
modern, clean, and frictionless
```

---

# Development Environment Philosophy

Every contributor should work in:

```text
isolated reproducible environments
```

---

# Why Isolation Matters

Environment isolation prevents:

- dependency conflicts
- global package pollution
- inconsistent behavior
- debugging complexity

---

# Recommended Development Stack

Aniwa currently recommends:

| Tool | Purpose |
|---|---|
| Python | core language |
| Git | version control |
| VS Code | editor |
| Git Bash | terminal |
| pytest | testing |
| black | formatting |
| ruff | linting |

---

# Current Python Requirement

Aniwa currently targets:

```text
Python 3.10+
```

---

# Why Modern Python Matters

Modern Python provides:

- better typing
- improved performance
- cleaner syntax
- stronger tooling

---

# Step 1 — Clone the Repository

Clone the repository locally.

Example:

```bash
git clone https://github.com/ReginaldErzoah/Aniwa.git
```

---

# Step 2 — Navigate Into the Project

Example:

```bash
cd Aniwa
```

---

# Step 3 — Create a Virtual Environment

Create an isolated environment.

Example:

```bash
python -m venv .venv
```

---

# Why Virtual Environments Matter

Virtual environments isolate:

- dependencies
- tooling
- Python packages

from the global system.

---

# Step 4 — Activate the Environment

---

# Windows

Example:

```bash
source .venv/Scripts/activate
```

---

# macOS/Linux

Example:

```bash
source .venv/bin/activate
```

---

# Step 5 — Upgrade pip

Recommended:

```bash
python -m pip install --upgrade pip
```

---

# Why Updating pip Matters

Newer versions improve:

- dependency resolution
- installation reliability
- compatibility

---

# Step 6 — Install Development Dependencies

Install project dependencies.

Example:

```bash
pip install -r requirements.txt
```

---

# Step 7 — Install Aniwa Locally

Install in editable mode.

Example:

```bash
pip install -e .
```

---

# Why Editable Installs Matter

Editable installs allow:

- instant code changes
- rapid development
- faster iteration

without reinstalling repeatedly.

---

# Step 8 — Verify Installation

Test the CLI.

Example:

```bash
aniwa --help
```

---

# Expected Result

You should see:

```text
Aniwa - Universal dataset profiling and intelligence.
```

---

# Project Structure Overview

Current project structure:

```text
Aniwa/
│
├── aniwa/
│   ├── cli.py
│   ├── core/
│   ├── io/
│   ├── models/
│   ├── reports/
│   ├── templates/
│   └── utils/
│
├── tests/
├── examples/
├── docs/
├── README.md
├── CONTRIBUTING.md
├── pyproject.toml
└── requirements.txt
```

---

# Understanding the Architecture

Aniwa is organized into layered systems.

---

# Core Layers

| Layer | Purpose |
|---|---|
| cli | orchestration |
| io | dataset ingestion |
| core | profiling engine |
| models | structured data |
| reports | rendering/export |
| templates | presentation |
| tests | validation |

---

# Running Aniwa Locally

Basic example:

```bash
aniwa examples/customers.csv
```

---

# Running HTML Reports

Example:

```bash
aniwa examples/customers.csv --report html
```

---

# Running JSON Reports

Example:

```bash
aniwa examples/customers.csv --report json
```

---

# Running Markdown Reports

Example:

```bash
aniwa examples/customers.csv --report markdown
```

---

# Running Fast Profiling

Example:

```bash
aniwa examples/customers.csv --mode fast
```

---

# Running Deep Profiling

Example:

```bash
aniwa examples/customers.csv --mode deep
```

---

# Using Configuration Files

Aniwa supports configuration files.

---

# Supported Config Types

Supported formats:

| Format |
|---|
| YAML |
| TOML |
| JSON |

---

# Example Config Usage

Example:

```bash
aniwa examples/customers.csv --config examples/config_sample.yaml
```

---

# Automatic Config Discovery

Aniwa automatically searches for:

```text
aniwa.yaml
aniwa.yml
aniwa.toml
aniwa.json
```

---

# Running Tests

Run all tests using:

```bash
pytest
```

---

# Why Testing Matters

Tests protect against:

- regressions
- broken features
- unstable releases

---

# Running Specific Tests

Example:

```bash
pytest tests/test_cli.py
```

---

# Running With Verbose Output

Example:

```bash
pytest -v
```

---

# Formatting Code

Aniwa uses:

```text
black
```

for formatting.

---

# Format Command

Example:

```bash
black .
```

---

# Why Formatting Matters

Consistent formatting improves:

- readability
- maintainability
- code reviews

---

# Linting Code

Aniwa uses:

```text
ruff
```

for linting.

---

# Ruff Command

Example:

```bash
ruff check .
```

---

# Why Linting Matters

Linting helps detect:

- unused imports
- bugs
- bad patterns
- inconsistent code

---

# Recommended Development Workflow

Recommended cycle:

```text
edit
→ run tests
→ lint
→ format
→ commit
```

---

# Git Workflow

Recommended workflow:

```text
fork
→ branch
→ develop
→ test
→ PR
```

---

# Creating a Branch

Example:

```bash
git checkout -b feature/add-xml-reader
```

---

# Commit Philosophy

Commits should remain:

- focused
- descriptive
- atomic

---

# Good Commit Examples

Examples:

```text
Add YAML config support
Fix HTML chart rendering
Add Markdown report exporter
```

---

# Bad Commit Examples

Avoid:

```text
fix stuff
update
changes
```

---

# Pull Request Philosophy

PRs should:

- solve one problem
- include tests
- update docs
- remain reviewable

---

# Example Development Tasks

Typical contributor tasks:

| Task |
|---|
| add file readers |
| improve reports |
| create templates |
| add insights |
| improve tests |

---

# Debugging Philosophy

Debugging should prioritize:

- reproducibility
- isolation
- clarity

---

# Recommended Debugging Strategy

Workflow:

```text
reproduce
→ isolate
→ inspect
→ fix
→ test
```

---

# Recommended VS Code Extensions

Suggested extensions:

| Extension |
|---|
| Python |
| Ruff |
| Black Formatter |
| GitLens |

---

# VS Code Virtual Environment Setup

Example `.vscode/settings.json`:

```json
{
  "python-envs.defaultEnvManager": "ms-python.python:venv"
}
```

---

# Why Editor Configuration Matters

Good editor setup improves:

- productivity
- consistency
- onboarding

---

# Example Development Commands

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Editable Install

```bash
pip install -e .
```

---

# Run Tests

```bash
pytest
```

---

# Format Code

```bash
black .
```

---

# Run Linter

```bash
ruff check .
```

---

# Run CLI

```bash
aniwa examples/customers.csv
```

---

# Performance Philosophy

Development workflows should remain:

```text
fast and frictionless
```

---

# Why Fast Workflows Matter

Fast iteration improves:

- contributor velocity
- experimentation
- productivity

---

# Cross-Platform Philosophy

Aniwa development should work consistently across:

| Platform |
|---|
| Windows |
| Linux |
| macOS |

---

# Common Development Problems

Typical issues include:

| Problem |
|---|
| dependency conflicts |
| missing virtual environment |
| outdated pip |
| missing editable install |

---

# Recommended Fixes

Always verify:

- environment activated
- dependencies installed
- editable install completed

---

# Architecture Learning Philosophy

Contributors are encouraged to study:

- profiling systems
- dataframe systems
- report architectures
- distributed systems

---

# Recommended Contributor Progression

Suggested learning order:

```text
CLI
→ readers
→ reports
→ profiling engine
→ architecture
```

---

# Long-Term Contributor Philosophy

Aniwa contributors are not just writing features.

They are helping build:

```text
future universal data intelligence infrastructure
```

---

# Long-Term Development Vision

Aniwa development workflows should eventually support:

- distributed systems
- cloud infrastructure
- plugin ecosystems
- enterprise workflows

---

# Final Philosophy

Local development exists to ensure contributors can:

```text
build, test, understand, and evolve Aniwa confidently and efficiently
```

---

# Related Documentation

Continue with:

- developer-guide/code-style.md
- developer-guide/testing.md
- architecture/system-design.md
- CONTRIBUTING.md