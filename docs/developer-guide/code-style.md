# Code Style Guide

This document defines the official coding standards, architectural conventions, formatting principles, and engineering practices used throughout Aniwa.

The goal of this guide is to ensure that Aniwa remains:

- maintainable
- scalable
- readable
- contributor-friendly
- production-quality

over the long term.

---

# Philosophy

Aniwa code should feel:

```text
simple, clean, modern, scalable, and intentional
```

---

# Why Code Style Matters

Consistent code style improves:

- maintainability
- onboarding
- debugging
- scalability
- collaboration

---

# Core Engineering Principles

Aniwa follows several engineering principles:

| Principle | Meaning |
|---|---|
| readability | code should be easy to understand |
| simplicity | avoid unnecessary complexity |
| modularity | isolated responsibilities |
| scalability | future-friendly design |
| consistency | predictable patterns |
| maintainability | sustainable engineering |

---

# General Philosophy

Prefer code that is:

```text
clear over clever
```

---

# Readability First

Readable code is more valuable than:

- compressed code
- overly clever abstractions
- unnecessary optimizations

---

# File Organization Philosophy

Files should remain:

```text
focused and modular
```

---

# Good File Characteristics

A good file should:

- have a clear responsibility
- remain reasonably sized
- avoid unrelated logic

---

# Bad File Characteristics

Avoid files that:

- contain many unrelated systems
- mix responsibilities
- become excessively large

---

# Module Philosophy

Modules should represent:

```text
single conceptual responsibilities
```

---

# Example Good Separation

Example:

```text
readers.py
statistics.py
insights.py
```

---

# Naming Philosophy

Names should be:

- descriptive
- predictable
- explicit

---

# Good Variable Names

Examples:

```python
dataset_profile
duplicate_rows
null_percentage
```

---

# Bad Variable Names

Avoid:

```python
x
data2
tmp
```

unless context is extremely obvious.

---

# Function Naming

Functions should describe:

```text
what they do
```

---

# Good Function Names

Examples:

```python
read_dataset()
render_html_report()
generate_insights()
```

---

# Bad Function Names

Avoid vague names like:

```python
handle()
process()
run()
```

without context.

---

# Class Naming

Classes should use:

```python
PascalCase
```

---

# Example

Examples:

```python
DatasetProfile
ProfileMetadata
```

---

# Function Length Philosophy

Functions should remain:

```text
small and focused
```

---

# Why Small Functions Matter

Small functions improve:

- readability
- testing
- debugging

---

# Recommended Function Characteristics

Functions should ideally:

- perform one task
- remain easy to scan
- avoid excessive nesting

---

# Avoid Deep Nesting

Prefer:

```python
early returns
```

over:

```python
deeply nested conditionals
```

---

# Example Preferred Style

Good:

```python
if not data:
    return
```

---

# Example Avoided Style

Avoid:

```python
if data:
    if something:
        if another:
```

---

# Line Length

Recommended line length:

```text
88–100 characters
```

---

# Why Reasonable Line Length Matters

This improves:

- readability
- diffs
- side-by-side review

---

# Import Organization

Imports should be grouped logically.

---

# Import Order

Recommended order:

```python
# standard library

# third-party libraries

# local imports
```

---

# Example

Example:

```python
import json
from pathlib import Path

import polars as pl
import typer

from aniwa.core.profiler import profile_dataframe
```

---

# Type Hint Philosophy

Aniwa strongly encourages:

```python
type hints
```

---

# Why Type Hints Matter

Type hints improve:

- readability
- tooling
- maintainability
- debugging

---

# Example Type Hints

Example:

```python
def load_config(
    file_path: str,
) -> dict[str, Any]:
```

---

# Avoid Ambiguous Types

Prefer:

```python
dict[str, Any]
```

over:

```python
dict
```

---

# Enum Philosophy

Use enums for:

- controlled values
- CLI options
- internal constants

---

# Example

Example:

```python
class ReportFormat(str, Enum):
```

---

# Constants Philosophy

Shared constants should be centralized.

---

# Example

Example:

```python
CONFIG_FILE_NAMES = (...)
```

---

# Avoid Magic Values

Avoid unexplained hardcoded values.

---

# Bad Example

Avoid:

```python
if x > 37:
```

---

# Good Example

Prefer:

```python
MAX_NULL_THRESHOLD = 37
```

---

# Comment Philosophy

Comments should explain:

```text
why
```

not:

```text
what
```

---

# Avoid Obvious Comments

Avoid:

```python
# increment count
count += 1
```

---

# Good Comments

Prefer comments that explain:

- reasoning
- architecture
- tradeoffs

---

# Docstring Philosophy

Public functions should include docstrings.

---

# Example

Example:

```python
"""
Profile a dataset.
"""
```

---

# Error Handling Philosophy

Errors should be:

- explicit
- informative
- actionable

---

# Good Error Example

Example:

```python
raise typer.BadParameter(
    "Invalid profiling mode."
)
```

---

# Avoid Silent Failures

Never suppress important failures silently.

---

# Exception Philosophy

Catch exceptions only when:

- adding context
- recovering gracefully
- improving UX

---

# Avoid Broad Exceptions

Avoid:

```python
except:
```

---

# Prefer Explicit Exceptions

Prefer:

```python
except ValueError:
```

---

# Logging Philosophy

Future logging systems should prioritize:

- clarity
- usefulness
- debuggability

---

# Architecture Philosophy

Systems should remain:

```text
modular and layered
```

---

# Separation of Concerns

Avoid mixing:

| Concern | Example |
|---|---|
| profiling | reporting |
| rendering | parsing |
| CLI | business logic |

---

# Business Logic Placement

Business logic belongs in:

```text
core systems
```

not:

```text
CLI or templates
```

---

# Template Philosophy

Templates should contain:

- presentation logic only

---

# Reader Philosophy

Readers should:

- only ingest data
- avoid profiling logic

---

# Renderer Philosophy

Renderers should:

- only render outputs
- avoid business logic

---

# Testing Philosophy

Every important feature should include tests.

---

# Test Organization

Tests belong in:

```text
tests/
```

---

# Recommended Test Naming

Examples:

```text
test_readers.py
test_reports.py
test_insights.py
```

---

# Test Philosophy

Tests should validate:

- correctness
- edge cases
- regressions

---

# Edge Cases Matter

Always test:

- empty datasets
- malformed inputs
- invalid configs
- extreme values

---

# Performance Philosophy

Optimize only when necessary.

---

# Avoid Premature Optimization

Prefer:

```text
clarity first
```

before:

```text
micro-optimizations
```

---

# Vectorization Philosophy

Prefer:

```python
Polars vectorized operations
```

over:

```python
row-by-row loops
```

---

# Why Vectorization Matters

Vectorization improves:

- speed
- scalability
- memory efficiency

---

# Configuration Philosophy

Configuration systems should remain:

- predictable
- validated
- user-friendly

---

# CLI Philosophy

CLI systems should prioritize:

- simplicity
- discoverability
- consistency

---

# Naming Conventions

| Element | Convention |
|---|---|
| files | snake_case |
| functions | snake_case |
| classes | PascalCase |
| constants | UPPER_CASE |
| variables | snake_case |

---

# File Naming Examples

Good:

```text
json_report.py
config_loader.py
```

Bad:

```text
JsonReport.py
configLoader.py
```

---

# Formatting Tools

Recommended tools:

| Tool | Purpose |
|---|---|
| black | formatting |
| ruff | linting |
| pytest | testing |

---

# Black Formatting

Recommended command:

```bash
black .
```

---

# Ruff Linting

Recommended command:

```bash
ruff check .
```

---

# Pytest

Recommended command:

```bash
pytest
```

---

# Pull Request Philosophy

PRs should remain:

- focused
- reviewable
- isolated

---

# Good Pull Requests

Good PRs:

- solve one problem
- include tests
- update documentation

---

# Avoid Large Mixed PRs

Avoid PRs that:

- solve unrelated issues
- refactor everything simultaneously
- mix formatting with features

---

# Documentation Philosophy

Documentation is considered:

```text
core infrastructure
```

---

# Why Documentation Matters

Good documentation improves:

- contributor scalability
- project longevity
- onboarding

---

# Contributor Philosophy

Contributors should prioritize:

- clarity
- maintainability
- architectural consistency

---

# Long-Term Engineering Philosophy

Aniwa is designed for:

```text
long-term sustainability
```

not:

```text
short-term hacks
```

---

# Future Scalability Philosophy

Code written today should remain understandable:

```text
years later
```

---

# Final Philosophy

Aniwa code should feel:

```text
intentional, elegant, scalable, and deeply maintainable
```

Every contributor helps shape:

```text
the future architecture of the project
```

---

# Related Documentation

Continue with:

- architecture/system-design.md
- architecture/overview.md
- developer-guide/testing.md
- CONTRIBUTING.md