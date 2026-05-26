# Dependency Management

This document explains how Aniwa manages dependencies, packages, tooling, versioning, compatibility, and long-term ecosystem stability.

Dependency management is a critical part of maintaining a:

```text
stable, scalable, and production-quality open-source project
```

---

# Purpose of Dependency Management

Dependency management ensures that:

- installations remain reproducible
- environments remain stable
- contributors can collaborate reliably
- releases remain predictable
- compatibility issues are minimized

---

# Dependency Philosophy

Aniwa follows several dependency principles:

| Principle | Purpose |
|---|---|
| minimalism | avoid unnecessary packages |
| stability | reduce breaking changes |
| maintainability | manageable ecosystem |
| performance | lightweight installs |
| reproducibility | predictable environments |

---

# Core Philosophy

Aniwa should depend only on packages that are:

```text
necessary, reliable, and actively maintained
```

---

# Why Dependency Discipline Matters

Poor dependency management causes:

- installation failures
- version conflicts
- unstable releases
- security risks
- contributor frustration

---

# Current Dependency System

Aniwa currently uses:

```text
pyproject.toml
```

as the primary dependency management system.

---

# Why pyproject.toml Matters

`pyproject.toml` provides:

- modern packaging standards
- dependency management
- build configuration
- project metadata

---

# Current Build System

Aniwa currently uses:

```toml
setuptools
wheel
```

---

# Example Build Configuration

Example:

```toml
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"
```

---

# Primary Dependency File

Main dependency definitions live in:

```text
pyproject.toml
```

---

# Why Centralized Dependencies Matter

Centralization improves:

- consistency
- reproducibility
- maintenance

---

# Current Core Dependencies

Aniwa currently depends on libraries such as:

| Dependency | Purpose |
|---|---|
| polars | dataframe engine |
| typer | CLI framework |
| rich | terminal UI |
| pydantic | structured models |
| jinja2 | template rendering |
| openpyxl | Excel support |
| PyYAML | YAML configs |

---

# Why These Libraries Were Chosen

Libraries were selected based on:

- maturity
- performance
- ecosystem quality
- maintainability

---

# Polars Philosophy

Aniwa uses:

```text
Polars
```

instead of pandas because it provides:

- higher performance
- better scalability
- modern dataframe architecture

---

# Typer Philosophy

Aniwa uses:

```text
Typer
```

because it provides:

- clean CLI development
- type-hint integration
- excellent UX

---

# Rich Philosophy

Aniwa uses:

```text
Rich
```

to provide:

- beautiful terminal interfaces
- readable output
- modern CLI experiences

---

# Pydantic Philosophy

Aniwa uses:

```text
Pydantic
```

for:

- structured validation
- serialization
- typed models

---

# Dependency Categories

Aniwa dependencies generally fall into categories.

---

# Runtime Dependencies

Required during execution.

Examples:

| Dependency |
|---|
| polars |
| typer |
| rich |

---

# Development Dependencies

Used for development workflows.

Examples:

| Dependency |
|---|
| pytest |
| black |
| ruff |

---

# Optional Dependencies

Future systems may support:

```text
optional dependency groups
```

---

# Why Optional Dependencies Matter

Optional dependencies reduce:

- installation weight
- unnecessary complexity

---

# Future Dependency Groups

Potential groups:

| Group |
|---|
| dev |
| docs |
| database |
| cloud |
| AI |

---

# Example Future Extras

Example:

```bash
pip install aniwa[database]
```

---

# Version Pinning Philosophy

Aniwa should avoid:

```text
overly strict pinning
```

unless necessary.

---

# Why Over-Pinning Is Dangerous

Strict pinning can cause:

- dependency conflicts
- ecosystem incompatibility
- installation issues

---

# Recommended Version Strategy

Prefer:

```toml
package>=minimum_version
```

---

# Example

Example:

```toml
polars>=1.0.0
```

---

# Compatibility Philosophy

Aniwa should maintain compatibility with:

- stable Python releases
- actively maintained libraries

---

# Current Python Support

Aniwa currently targets:

```text
Python 3.10+
```

---

# Why Modern Python Matters

Modern Python versions provide:

- performance improvements
- better typing
- cleaner language features

---

# Avoid Unmaintained Libraries

Dependencies should be:

- actively maintained
- stable
- well-documented

---

# Dependency Evaluation Checklist

Before adding a dependency, evaluate:

| Question |
|---|
| Is it actively maintained? |
| Is it widely trusted? |
| Does it solve a real problem? |
| Is the dependency necessary? |
| Does it increase complexity? |

---

# Avoid Dependency Bloat

Avoid adding packages for:

- tiny helper functions
- unnecessary abstractions
- trivial utilities

---

# Why Minimalism Matters

Fewer dependencies improve:

- reliability
- install speed
- maintainability

---

# Security Philosophy

Dependencies introduce:

```text
supply chain risk
```

---

# Security Best Practices

Dependencies should be:

- audited
- updated responsibly
- monitored for vulnerabilities

---

# Future Security Tooling

Future systems may include:

| Tool |
|---|
| pip-audit |
| Dependabot |
| security CI checks |

---

# Updating Dependencies

Dependencies should be updated:

```text
carefully and incrementally
```

---

# Why Incremental Updates Matter

Large dependency jumps can introduce:

- breaking changes
- hidden bugs
- ecosystem instability

---

# Dependency Update Workflow

Recommended workflow:

```text
update
→ test
→ validate
→ release
```

---

# Testing After Dependency Changes

Always run:

```bash
pytest
```

after dependency updates.

---

# Additional Recommended Checks

Recommended commands:

```bash
ruff check .
black .
```

---

# Virtual Environment Philosophy

Always use:

```text
isolated virtual environments
```

---

# Why Virtual Environments Matter

Virtual environments prevent:

- package conflicts
- global pollution
- inconsistent behavior

---

# Creating Virtual Environments

Example:

```bash
python -m venv .venv
```

---

# Activating Environments

Windows:

```bash
source .venv/Scripts/activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

---

# Local Development Installation

Recommended:

```bash
pip install -e .
```

---

# Why Editable Installs Matter

Editable installs improve:

- development speed
- testing workflows
- iteration cycles

---

# Lock File Philosophy

Future versions may introduce:

```text
dependency lock files
```

---

# Why Lock Files Matter

Lock files improve:

- reproducibility
- CI consistency
- deterministic installs

---

# Future Packaging Evolution

Future packaging systems may include:

| Tool |
|---|
| uv |
| poetry |
| hatch |
| pdm |

---

# CI Dependency Strategy

CI pipelines should:

- install dependencies cleanly
- validate environments
- test reproducibility

---

# Cross-Platform Philosophy

Dependencies should work consistently across:

| Platform |
|---|
| Windows |
| Linux |
| macOS |

---

# Dependency Isolation Philosophy

Avoid coupling unrelated systems through shared dependencies.

---

# Example

Example:

```text
HTML reporting should not depend on database libraries.
```

---

# Future Plugin Dependency Support

Future plugin systems may support:

```text
plugin-specific dependencies
```

---

# Why Plugin Isolation Matters

This prevents:

- unnecessary installs
- ecosystem instability

---

# Future Database Dependencies

Database support may introduce optional groups:

| Group |
|---|
| postgres |
| mysql |
| cloud |
| warehouse |

---

# Future AI Dependencies

AI systems may eventually require:

| Dependency Type |
|---|
| vector databases |
| transformers |
| embeddings |
| ML frameworks |

---

# Future Cloud Dependencies

Potential future cloud integrations:

| Platform |
|---|
| AWS |
| GCP |
| Azure |

---

# Documentation Dependencies

Documentation tooling may eventually include:

| Tool |
|---|
| MkDocs |
| Sphinx |
| Material for MkDocs |

---

# Contributor Dependency Philosophy

Contributors should:

- avoid unnecessary packages
- justify new dependencies
- document additions clearly

---

# Pull Request Requirements

PRs adding dependencies should include:

- rationale
- usage explanation
- documentation updates
- compatibility validation

---

# Example Dependency Addition

Example:

```toml
PyYAML>=6.0
```

---

# Dependency Anti-Patterns

Avoid:

| Anti-Pattern |
|---|
| unnecessary packages |
| abandoned libraries |
| duplicated functionality |
| overly strict pinning |
| hidden dependencies |

---

# Long-Term Scalability Philosophy

Dependency strategy should scale for:

```text
years of project growth
```

---

# Long-Term Ecosystem Vision

Aniwa aims to maintain a dependency ecosystem that is:

- modern
- stable
- scalable
- production-quality

---

# Final Philosophy

Dependency management exists to ensure that:

```text
Aniwa remains reliable, maintainable, reproducible, and scalable as the project evolves
```

---

# Related Documentation

Continue with:

- developer-guide/code-style.md
- developer-guide/testing.md
- architecture/system-design.md
- CONTRIBUTING.md