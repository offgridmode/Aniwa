# Adding Insights

This guide explains how to create, extend, and maintain Aniwa’s insight generation system.

Insights are one of the most important parts of Aniwa because they transform:

```text
raw statistics
```

into:

```text
human-readable intelligence
```

---

# Purpose of Insights

Insights help users quickly identify:

- suspicious patterns
- quality problems
- unusual structures
- possible risks
- meaningful observations

without manually inspecting every metric.

---

# Why Insights Matter

Most users do not want to manually analyze:

- null percentages
- uniqueness counts
- cardinality distributions
- statistics tables

Insights simplify interpretation.

---

# Insight Philosophy

Aniwa’s insight system is designed to be:

| Principle | Purpose |
|---|---|
| modular | isolated insight rules |
| explainable | understandable logic |
| scalable | future expansion |
| lightweight | fast execution |
| useful | actionable output |

---

# Insight Architecture Overview

High-level flow:

```text
DataFrame
→ profiling metrics
→ insight rules
→ Insight objects
→ reports
```

---

# Insight System Location

Current insight systems typically live in:

```text
aniwa/core/
```

or:

```text
aniwa/insights/
```

depending on future architecture evolution.

---

# Current Insight Flow

Conceptually:

```text
profile_dataframe()
↓
generate metrics
↓
evaluate rules
↓
create insights
↓
attach to DatasetProfile
```

---

# What an Insight Contains

Each insight typically contains:

| Field | Purpose |
|---|---|
| level | severity |
| message | human-readable explanation |

---

# Example Insight

Example:

```python
Insight(
    level="warning",
    message="Column 'email' may contain sensitive information."
)
```

---

# Insight Severity Levels

Current levels may include:

| Level |
|---|
| info |
| warning |
| critical |

---

# Severity Philosophy

Severity levels should communicate:

```text
importance and urgency
```

---

# INFO Insights

INFO insights describe:

- informational observations
- low-risk findings
- helpful context

---

# WARNING Insights

WARNING insights describe:

- potential issues
- suspicious patterns
- data quality concerns

---

# CRITICAL Insights

CRITICAL insights describe:

- severe quality issues
- dangerous inconsistencies
- major dataset problems

---

# Current Insight Categories

Aniwa currently supports insights such as:

| Insight |
|---|
| duplicate rows |
| sparse columns |
| possible PII |
| high-cardinality columns |

---

# Insight Design Principles

Good insights should be:

| Principle | Meaning |
|---|---|
| actionable | users know what it means |
| concise | short and clear |
| relevant | avoids noise |
| explainable | predictable logic |

---

# Bad Insight Example

Avoid vague insights like:

```text
Something looks suspicious.
```

---

# Good Insight Example

Prefer:

```text
Column 'customer_id' contains 100% unique values and may represent an identifier.
```

---

# Insight Generation Strategy

Insights are typically rule-based.

---

# Why Rule-Based Systems Matter

Rule-based systems are:

- explainable
- deterministic
- testable
- maintainable

---

# Example Insight Rule

Example:

```python
if duplicate_percent > 10:
    add_warning(...)
```

---

# Step-by-Step Guide

---

# Step 1 — Identify a Useful Pattern

Choose a dataset characteristic worth highlighting.

Examples:

| Pattern |
|---|
| sparse columns |
| suspicious null rates |
| likely IDs |
| possible PII |
| outliers |

---

# Step 2 — Define the Detection Logic

Define how the insight is triggered.

---

# Example Logic

Example:

```python
if null_percent > 50:
```

---

# Step 3 — Choose Severity Level

Select:

- info
- warning
- critical

based on impact.

---

# Step 4 — Create a Human-Readable Message

Messages should explain:

- what happened
- why it matters

---

# Example Message

Example:

```python
"Column 'email' contains 20% null values."
```

---

# Step 5 — Append the Insight

Example:

```python
insights.append(
    Insight(...)
)
```

---

# Step 6 — Add Tests

Every insight must include tests.

---

# Required Insight Tests

Tests should validate:

| Test |
|---|
| insight triggers correctly |
| false positives avoided |
| severity correctness |
| edge cases |

---

# Step 7 — Update Documentation

Update:

- docs/
- examples
- insight references

---

# Example Insight Template

Basic example:

```python
if unique_percent > 95:
    insights.append(
        Insight(
            level="info",
            message=f"Column '{column}' may contain unique identifiers."
        )
    )
```

---

# Common Insight Categories

---

# Quality Insights

Quality insights analyze:

- duplicates
- missing values
- sparsity

---

# Schema Insights

Schema insights analyze:

- unusual datatypes
- mixed structures
- inconsistent schemas

---

# Statistical Insights

Statistical insights analyze:

- outliers
- extreme distributions
- anomalies

---

# Semantic Insights

Semantic insights analyze:

- emails
- phone numbers
- IDs
- addresses

---

# Governance Insights

Future governance insights may analyze:

- compliance risks
- PII exposure
- policy violations

---

# AI Insights

Future AI systems may generate:

- natural-language explanations
- recommendations
- summaries

---

# Performance Philosophy

Insights should remain:

```text
lightweight and scalable
```

---

# Why Performance Matters

Insight systems execute frequently.

Poor insight logic can slow profiling dramatically.

---

# Performance Best Practices

Prefer:

- vectorized operations
- lightweight rules
- reusable metrics

Avoid:

- repeated dataframe scans
- row-by-row loops

---

# False Positive Philosophy

Insight systems should avoid:

```text
excessive noise
```

---

# Why Noise Is Dangerous

Too many unnecessary warnings reduce:

- trust
- usefulness
- readability

---

# Insight Prioritization Philosophy

Only generate insights that are:

```text
meaningful and actionable
```

---

# Insight Scalability Philosophy

The insight engine should scale toward:

```text
enterprise-grade data intelligence
```

---

# Future Insight Categories

Potential future systems:

| Future Insight |
|---|
| drift detection |
| semantic classification |
| AI recommendations |
| governance scoring |
| anomaly explanations |

---

# Future Semantic Intelligence

Potential semantic systems:

- email detection
- credit card detection
- phone number recognition
- address inference

---

# Future AI Insight Systems

Long-term AI systems may generate:

```text
natural-language dataset explanations
```

---

# Example Future AI Insight

Example:

```text
This dataset appears to represent customer transaction history with moderate data quality issues.
```

---

# Future Recommendation Engine

Future systems may recommend:

- cleaning strategies
- schema fixes
- validation rules

---

# Future Trust Scoring

Potential systems may compute:

```text
dataset trust scores
```

---

# Why Trust Systems Matter

Trust scoring helps users quickly evaluate:

- reliability
- risk
- quality

---

# Future Governance Intelligence

Potential future systems:

| Governance Feature |
|---|
| PII scoring |
| compliance checks |
| lineage awareness |
| policy validation |

---

# Insight Modularity

Insights should remain isolated from:

- report rendering
- reader systems
- CLI logic

---

# Why Isolation Matters

Isolation improves:

- maintainability
- extensibility
- testing

---

# Insight Registry Vision

Future systems may introduce:

```text
insight registries
```

---

# Example Future Registry

Example:

```python
register_insight(check_sparse_columns)
```

---

# Plugin Insight Vision

Future plugins may add:

- industry-specific rules
- governance checks
- AI models

---

# Industry-Specific Insight Examples

Potential verticals:

| Industry |
|---|
| finance |
| healthcare |
| retail |
| logistics |

---

# Logging Philosophy

Future insight systems may support:

- verbose tracing
- rule diagnostics
- execution metrics

---

# Testing Philosophy

Every insight rule should be:

```text
predictable and testable
```

---

# Example Insight Test

Example:

```python
def test_duplicate_insight():
    profile = profile_dataframe(df)

    assert any(
        insight.level == "warning"
        for insight in profile.insights
    )
```

---

# Insight Anti-Patterns

Avoid:

| Anti-Pattern |
|---|
| vague messages |
| noisy warnings |
| repeated scans |
| duplicated rules |
| hardcoded assumptions |

---

# Contributor Best Practices

Contributors should prioritize:

- clarity
- usefulness
- maintainability
- performance

---

# Pull Request Checklist

Before submitting:

- insight logic works correctly
- tests pass
- documentation updated
- false positives minimized

---

# Long-Term Vision

Aniwa’s insight engine is evolving toward:

```text
a universal data intelligence system
```

capable of helping users:

- understand data
- trust data
- improve data quality
- reason about datasets intelligently

---

# Final Philosophy

The insight system exists to transform:

```text
dataset metrics
```

into:

```text
clear, actionable, intelligent understanding
```

---

# Related Documentation

Continue with:

- architecture/profiling-engine.md
- architecture/models.md
- api/profiler.md
- developer-guide/testing.md