# Testing Guide

This document explains the testing philosophy, architecture, workflows, strategies, and long-term validation systems used in Aniwa.

Testing is one of the most important engineering systems in the project because it ensures:

- reliability
- stability
- scalability
- contributor confidence
- release quality

Aniwa treats testing as:

```text
core infrastructure
```

not an optional development step.

---

# Purpose of Testing

Testing ensures that:

- features work correctly
- regressions are prevented
- releases remain stable
- contributors can collaborate safely

---

# Testing Philosophy

Aniwa testing prioritizes:

| Principle | Purpose |
|---|---|
| correctness | features behave properly |
| reproducibility | predictable outcomes |
| maintainability | sustainable engineering |
| scalability | long-term project growth |
| confidence | safer contributions |

---

# Core Philosophy

Aniwa aims for:

```text
high-confidence engineering
```

through:

```text
predictable automated validation
```

---

# Why Testing Matters

Without testing:

- regressions increase
- contributors break existing systems
- releases become unstable
- debugging becomes expensive

---

# Current Testing Framework

Aniwa currently uses:

```text
pytest
```

---

# Why pytest Was Chosen

pytest provides:

- clean syntax
- strong ecosystem
- scalability
- excellent developer experience

---

# Test Directory Structure

Tests are stored in:

```text
tests/
```

---

# Example Test Structure

Example:

```text
tests/
├── test_cli.py
├── test_readers.py
├── test_reports.py
├── test_config.py
├── test_insights.py
```

---

# Test Organization Philosophy

Tests should mirror:

```text
the architecture of the project
```

---

# Why Mirrored Structures Matter

Mirrored structures improve:

- discoverability
- maintainability
- contributor onboarding

---

# Core Testing Categories

Aniwa currently focuses on several testing layers.

---

# Unit Tests

Unit tests validate:

```text
individual functions and modules
```

---

# Integration Tests

Integration tests validate:

```text
systems working together
```

---

# CLI Tests

CLI tests validate:

- commands
- options
- argument handling
- UX behavior

---

# Reader Tests

Reader tests validate:

- dataset loading
- supported formats
- malformed files

---

# Report Tests

Report tests validate:

- rendering
- export generation
- output structure

---

# Config Tests

Config tests validate:

- YAML loading
- TOML loading
- JSON loading
- override priority

---

# Insight Tests

Insight tests validate:

- rule triggering
- severity correctness
- false positives

---

# Metadata Tests

Metadata tests validate:

- runtime tracking
- report metadata
- command reconstruction

---

# Current Testing Flow

Typical development flow:

```text
implement
→ test
→ validate
→ refactor
→ release
```

---

# Running Tests

Run all tests using:

```bash
pytest
```

---

# Running Verbose Tests

Example:

```bash
pytest -v
```

---

# Running Specific Tests

Example:

```bash
pytest tests/test_cli.py
```

---

# Running Individual Test Functions

Example:

```bash
pytest tests/test_cli.py::test_help
```

---

# Why Granular Testing Matters

Granular testing improves:

- debugging speed
- iteration speed
- contributor productivity

---

# Testing Philosophy

Tests should be:

| Principle | Meaning |
|---|---|
| isolated | independent |
| deterministic | repeatable |
| readable | understandable |
| maintainable | sustainable |

---

# Deterministic Testing

Tests should always produce:

```text
predictable outcomes
```

---

# Why Determinism Matters

Non-deterministic tests create:

- flaky CI
- contributor confusion
- unreliable validation

---

# Good Test Naming

Good test names explain behavior.

---

# Examples

Examples:

```python
test_read_csv()
test_invalid_config()
test_render_html_report()
```

---

# Bad Test Names

Avoid vague names like:

```python
test_stuff()
test_feature()
```

---

# Test Function Philosophy

Each test should validate:

```text
one clear behavior
```

---

# Why Small Tests Matter

Small tests improve:

- readability
- debugging
- maintainability

---

# Assertion Philosophy

Assertions should remain:

```text
explicit and readable
```

---

# Good Assertion Example

Example:

```python
assert df.height == 5
```

---

# Avoid Weak Assertions

Avoid:

```python
assert result
```

when more specific validation is possible.

---

# Edge Case Philosophy

Always test:

- invalid inputs
- empty datasets
- malformed files
- extreme values

---

# Why Edge Cases Matter

Most real-world failures happen at:

```text
system boundaries
```

---

# Example Edge Cases

Examples:

| Case |
|---|
| empty CSV |
| corrupted JSON |
| unsupported extension |
| invalid config values |

---

# Reader Testing Philosophy

Readers should validate:

- correct parsing
- format handling
- conversion to Polars

---

# Example Reader Test

Example:

```python
def test_read_csv():
    df = read_dataset("examples/customers.csv")

    assert df.height > 0
```

---

# Config Testing Philosophy

Config systems must validate:

- loading
- precedence
- invalid values
- graceful failure

---

# Config Priority Testing

Verify:

```text
CLI > config > defaults
```

---

# Example Config Test

Example:

```python
def test_cli_overrides_config():
```

---

# Report Testing Philosophy

Reports should validate:

- rendering success
- file creation
- structure correctness

---

# Example Report Test

Example:

```python
def test_render_json_report():
```

---

# HTML Report Validation

HTML reports should validate:

- rendering
- templates
- chart injection

---

# PDF Report Validation

PDF systems should validate:

- successful generation
- layout correctness
- export integrity

---

# Markdown Report Validation

Markdown reports should validate:

- formatting
- readability
- structure

---

# CLI Testing Philosophy

CLI tests should validate:

- help output
- options
- invalid arguments
- execution flow

---

# Example CLI Test

Example:

```python
def test_help():
```

---

# Metadata Testing Philosophy

Metadata systems should validate:

- generated timestamps
- version info
- execution metadata

---

# Template Testing Philosophy

Templates should validate:

- rendering
- responsiveness
- empty states

---

# Insight Testing Philosophy

Insight systems should validate:

- proper triggering
- severity assignment
- noise reduction

---

# False Positive Philosophy

Insight systems should avoid:

```text
excessive unnecessary warnings
```

---

# Performance Testing Philosophy

Performance systems should eventually validate:

- execution speed
- memory usage
- scalability

---

# Why Performance Testing Matters

Aniwa is designed for:

```text
large-scale data profiling
```

---

# Future Performance Benchmarks

Future benchmarks may track:

| Metric |
|---|
| runtime |
| memory usage |
| large dataset handling |

---

# Future Scalability Tests

Potential future tests:

- distributed execution
- chunked processing
- parallel profiling

---

# Mocking Philosophy

Mocking should be used:

```text
carefully and minimally
```

---

# Why Excessive Mocking Is Dangerous

Too much mocking can hide:

- real integration failures
- architectural problems

---

# Integration Testing Philosophy

Integration tests ensure:

```text
subsystems work together correctly
```

---

# Example Integration Flow

Example:

```text
reader
→ profiler
→ report
```

---

# Manual Testing Philosophy

Some features still require:

```text
human validation
```

---

# Examples

Examples:

| Area |
|---|
| visual reports |
| PDF layouts |
| CLI UX |
| chart rendering |

---

# Recommended Manual Checks

Before releases:

- inspect HTML reports
- verify PDFs
- test configs manually
- validate examples

---

# Example Manual Validation

Example:

```bash
aniwa examples/customers.csv --report html
```

---

# Continuous Integration Vision

Future systems may automate:

- testing
- formatting
- linting
- release validation

---

# Potential Future Tooling

Potential future systems:

| Tool |
|---|
| GitHub Actions |
| CI pipelines |
| automated release testing |

---

# Future Coverage Systems

Future systems may include:

```text
coverage tracking
```

---

# Why Coverage Matters

Coverage helps identify:

- untested systems
- weak validation areas

---

# Recommended Future Tools

Potential tools:

| Tool |
|---|
| coverage.py |
| pytest-cov |

---

# Failure Philosophy

When tests fail:

```text
investigate first, patch second
```

---

# Debugging Workflow

Recommended process:

```text
reproduce
→ isolate
→ inspect
→ fix
→ retest
```

---

# Avoid Test Suppression

Never ignore failing tests without understanding:

- root cause
- architectural impact

---

# Regression Philosophy

Every major bug should eventually receive:

```text
a regression test
```

---

# Why Regression Tests Matter

Regression tests prevent:

```text
old bugs from returning
```

---

# Contributor Testing Expectations

Contributors should:

- add tests for new features
- update broken tests
- validate edge cases

---

# Pull Request Requirements

Good PRs should include:

- tests
- validation
- documentation updates

---

# Testing Anti-Patterns

Avoid:

| Anti-Pattern |
|---|
| flaky tests |
| vague assertions |
| giant test functions |
| silent failures |
| skipped edge cases |

---

# Long-Term Testing Vision

Aniwa’s testing infrastructure is evolving toward:

```text
enterprise-grade validation systems
```

---

# Future Enterprise Testing

Potential future capabilities:

| Capability |
|---|
| distributed testing |
| benchmark automation |
| security testing |
| cloud validation |

---

# Strategic Importance

Testing is not merely:

```text
a development task
```

It is:

```text
a foundational engineering system
```

that protects the long-term quality of the project.

---

# Final Philosophy

Testing exists to ensure that:

```text
Aniwa remains reliable, scalable, maintainable, and trustworthy as it evolves
```

---

# Related Documentation

Continue with:

- developer-guide/local-development.md
- developer-guide/code-style.md
- architecture/system-design.md
- CONTRIBUTING.md