# Adding Report Formats

This guide explains how to create and integrate new report formats into Aniwa.

Aniwa’s reporting architecture is designed to be:

```text
modular, extensible, scalable, and presentation-focused
```

This makes it possible to support many different output systems over time.

---

# Purpose of Report Formats

Report formats transform:

```text
structured profiling intelligence
```

into:

```text
human-readable or machine-readable outputs
```

---

# Why Multiple Formats Matter

Different users require different outputs:

| User | Preferred Format |
|---|---|
| developers | console |
| automation systems | JSON |
| teams | HTML |
| documentation | Markdown |
| analysts | Excel |
| executives | PDF |

---

# Current Reporting Architecture

Current report systems are located in:

```text
aniwa/reports/
```

---

# Current Report Structure

Typical structure:

```text
aniwa/reports/
├── console.py
├── json_report.py
├── html_report.py
├── markdown_report.py
├── excel_report.py
├── pdf_report.py
```

---

# Reporting Philosophy

Every report format should:

- consume the same profile structure
- remain isolated
- focus on presentation only

---

# Why Renderer Isolation Matters

Isolation improves:

- maintainability
- scalability
- testing
- contributor onboarding

---

# Core Reporting Flow

High-level architecture:

```text
DatasetProfile
→ renderer
→ formatter
→ output
```

---

# DatasetProfile Requirement

All renderers must consume:

```python
DatasetProfile
```

---

# Why Shared Models Matter

Shared models ensure:

- consistency
- predictable outputs
- easier maintenance

---

# Step-by-Step Guide

---

# Step 1 — Choose the Report Format

Identify the new output target.

Examples:

| Format |
|---|
| CSV |
| XML |
| YAML |
| LaTeX |
| PowerPoint |
| Interactive Dashboard |

---

# Step 2 — Define the Use Case

Clarify:

- who will use it
- why it matters
- what it optimizes for

---

# Example Questions

- Is it machine-readable?
- Is it presentation-focused?
- Is it automation-oriented?
- Is it enterprise-facing?

---

# Step 3 — Create the Renderer File

Add a new renderer inside:

```text
aniwa/reports/
```

---

# Example

Example:

```text
aniwa/reports/csv_report.py
```

---

# Step 4 — Create the Renderer Function

Typical renderer structure:

```python
def render_csv_report(
    profile,
    output_path,
):
```

---

# Renderer Responsibilities

A renderer should:

- format data
- structure output
- write/export results

---

# Renderer Non-Responsibilities

Renderers should NOT:

- perform profiling
- mutate profile data
- contain heavy business logic

---

# Step 5 — Use DatasetProfile

Access profiling data through:

```python
profile.summary
profile.columns
profile.insights
```

---

# Step 6 — Generate Output

Generate the appropriate format.

---

# Example CSV Output

Example:

```csv
column,null_percent
email,20
```

---

# Step 7 — Handle Output Writing

Support:

- direct output paths
- output directories
- generated filenames

---

# Example Output Flow

Example:

```python
with open(output, "w") as file:
```

---

# Step 8 — Add CLI Support

Update:

```text
aniwa/cli.py
```

---

# Add Report Enum

Example:

```python
class ReportFormat(str, Enum):
    csv = "csv"
```

---

# Add CLI Dispatch Logic

Example:

```python
if report == ReportFormat.csv:
```

---

# Step 9 — Add Default Filename Support

Update:

```python
resolve_default_name()
```

---

# Example

Example:

```python
ReportFormat.csv: "aniwa_report.csv"
```

---

# Step 10 — Add Output Directory Support

Ensure compatibility with:

```text
--output-dir
```

---

# Step 11 — Add Tests

Every renderer must include tests.

---

# Required Renderer Tests

Tests should validate:

| Test |
|---|
| renderer works |
| file created |
| output valid |
| empty profiles |
| edge cases |

---

# Step 12 — Add Example Outputs

Place example outputs in:

```text
examples/
```

---

# Step 13 — Update Documentation

Update:

- README.md
- docs/
- usage examples

---

# Renderer Design Principles

Good renderers should be:

| Principle | Meaning |
|---|---|
| isolated | independent logic |
| predictable | stable outputs |
| maintainable | readable code |
| scalable | future-proof |

---

# Human-Readable vs Machine-Readable

Report formats generally fall into two categories.

---

# Human-Readable Reports

Examples:

| Format |
|---|
| HTML |
| PDF |
| Markdown |
| Console |

---

# Machine-Readable Reports

Examples:

| Format |
|---|
| JSON |
| CSV |
| XML |
| YAML |

---

# Why This Distinction Matters

Different outputs optimize for:

- humans
- systems
- automation
- interoperability

---

# Template-Based Renderers

Some formats may use templates.

Examples:

| Format |
|---|
| HTML |
| PDF |

---

# Why Templates Matter

Templates separate:

- styling
- layout
- business logic

---

# Current Template Engine

Aniwa currently uses:

```text
Jinja2
```

---

# Chart Support

Visual report formats may support:

- charts
- graphs
- dashboards

---

# Current Visualization Systems

Aniwa currently uses:

```text
Chart.js
```

for HTML charts.

---

# Why Visualizations Matter

Charts improve:

- readability
- communication
- executive reporting

---

# Metadata Requirements

All reports should include metadata.

---

# Recommended Metadata

| Metadata |
|---|
| generated_at |
| profiling_mode |
| report_format |
| dataset_path |
| Aniwa version |

---

# Why Metadata Matters

Metadata improves:

- reproducibility
- auditing
- debugging

---

# Conditional Rendering Philosophy

Renderers should only render sections when data exists.

---

# Why Conditional Rendering Matters

This prevents:

- empty sections
- broken layouts
- clutter

---

# Section Filtering Support

Renderers should respect:

```text
--include
--exclude
```

---

# Current Sections

Current sections include:

| Section |
|---|
| summary |
| schema |
| quality |
| statistics |
| insights |
| charts |

---

# Performance Philosophy

Renderers should remain:

```text
fast and lightweight
```

---

# Why Rendering Performance Matters

Large reports can become:

- memory-heavy
- slow to generate
- difficult to render

---

# Current Optimization Strategies

Current strategies include:

- modular rendering
- conditional sections
- reusable structures

---

# Future Optimization Areas

Potential future improvements:

| Optimization |
|---|
| lazy rendering |
| async exports |
| streaming generation |
| cached visualizations |

---

# Error Handling Philosophy

Renderers should fail:

```text
clearly and gracefully
```

---

# Good Error Example

Example:

```python
raise ValueError(
    "Invalid template selected."
)
```

---

# Logging Philosophy

Future renderers may support:

- debug tracing
- verbose export logs
- performance metrics

---

# Security Philosophy

Renderers should avoid:

- unsafe HTML injection
- arbitrary execution
- untrusted rendering

---

# Accessibility Philosophy

Visual reports should prioritize:

- readability
- responsive layouts
- semantic structure

---

# Future Report Types

Potential future formats:

| Future Format |
|---|
| PowerPoint |
| interactive dashboards |
| notebooks |
| observability exports |
| governance reports |

---

# Future Dashboard Systems

Potential future architecture:

```text
DatasetProfile
→ API
→ frontend dashboard
```

---

# Future Streaming Reports

Future systems may support:

- live dashboards
- streaming metrics
- continuous profiling

---

# Future Plugin Architecture

Long-term systems may support:

```text
third-party report plugins
```

---

# Example Future Plugin System

Example:

```python
register_reporter(
    "custom_dashboard",
    render_dashboard,
)
```

---

# Enterprise Reporting Vision

Future enterprise systems may support:

- branding
- organization templates
- governance exports
- white-label reporting

---

# AI Reporting Vision

Future AI systems may generate:

- natural-language summaries
- executive insights
- intelligent recommendations

---

# Contributor Best Practices

Contributors should prioritize:

- readability
- modularity
- maintainability
- test coverage

---

# Example Renderer Template

Basic example:

```python
def render_csv_report(
    profile,
    output_path,
):
    ...
```

---

# Example Renderer Test

Example:

```python
def test_render_csv_report():
    render_csv_report(profile, "report.csv")
```

---

# Pull Request Checklist

Before submitting:

- renderer works correctly
- tests pass
- documentation updated
- examples added

---

# Long-Term Vision

Aniwa’s reporting system is evolving toward:

```text
a universal data reporting platform
```

capable of supporting:

- developers
- enterprises
- governance systems
- AI workflows

---

# Final Philosophy

The reporting system exists to transform:

```text
structured profiling intelligence
```

into:

```text
clear, useful, beautiful, and scalable outputs
```

---

# Related Documentation

Continue with:

- architecture/reporting-system.md
- architecture/template-engine.md
- api/reports.md
- developer-guide/testing.md