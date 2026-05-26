# Report Sections

Aniwa reports are modular.

Users can control which sections appear in profiling reports using:

- `--include`
- `--exclude`

This allows highly focused reports optimized for:

- debugging
- governance
- auditing
- documentation
- automation
- CI pipelines

---

# Why Modular Sections Matter

Not every workflow needs every profiling section.

Examples:

| Workflow | Useful Sections |
|---|---|
| debugging | schema, insights |
| governance | quality, insights |
| auditing | summary, quality, metadata |
| documentation | summary, statistics |
| automation | JSON schema-only |
| ML validation | statistics, insights |

Modular reporting keeps reports:

- smaller
- faster
- more readable
- workflow-specific

---

# Available Sections

Aniwa currently supports:

| Section | Description |
|---|---|
| summary | dataset-level overview |
| schema | column structure profiling |
| quality | nulls, duplicates, uniqueness |
| statistics | numeric statistical analysis |
| insights | intelligent warnings and observations |
| charts | visual profiling charts |

---

# Section Architecture

Internally, sections are represented using the `ReportSection` enum.

Example:

```python
class ReportSection(str, Enum):
    summary = "summary"
    schema = "schema"
    quality = "quality"
    statistics = "statistics"
    insights = "insights"
    charts = "charts"
```

---

# Default Behavior

By default, Aniwa includes all sections.

Equivalent behavior:

```bash
aniwa dataset.csv
```

is effectively:

```bash
aniwa dataset.csv \
  --include summary,schema,quality,statistics,insights,charts
```

---

# Including Sections

Use `--include` to explicitly include sections.

Example:

```bash
aniwa dataset.csv \
  --include summary,insights
```

This generates a report containing only:

- summary
- insights

---

# Excluding Sections

Use `--exclude` to remove sections.

Example:

```bash
aniwa dataset.csv \
  --exclude statistics
```

This generates a report containing everything except:

- statistics

---

# Important Rule

`--include` and `--exclude` cannot be used together.

Incorrect:

```bash
aniwa dataset.csv \
  --include summary \
  --exclude charts
```

This raises an error.

---

# Validation System

Aniwa validates section names before profiling begins.

Example invalid command:

```bash
aniwa dataset.csv \
  --include metrics
```

Error:

```text
Invalid report section: metrics
```

---

# Internal Resolution Flow

Section resolution flow:

```text
CLI
→ validate_sections()
→ resolve_sections()
→ profile_dataframe()
→ report rendering
```

---

# Summary Section

The summary section provides dataset-level metrics.

Includes:

- row count
- column count
- dataset size
- duplicate overview

---

# Schema Section

The schema section provides structural profiling.

Includes:

- column names
- inferred types
- type consistency
- null counts
- unique counts

---

# Quality Section

The quality section analyzes data integrity.

Includes:

- null analysis
- duplicate detection
- uniqueness analysis
- sparse columns

---

# Statistics Section

The statistics section provides numeric profiling.

Includes:

- minimum
- maximum
- mean
- median
- standard deviation

Applies only to numeric columns.

---

# Insights Section

The insights section provides intelligent observations.

Examples:

- possible ID columns
- potential PII detection
- sparse columns
- suspicious cardinality
- duplicate warnings

---

# Charts Section

The charts section provides visual analysis.

Includes:

- null percentage charts
- unique value charts
- duplicate charts

Currently available in:

- HTML reports
- PDF reports

---

# Performance Implications

Different sections have different computational costs.

---

## Low Cost

Fast sections:

- summary
- schema

---

## Medium Cost

Moderate sections:

- quality
- insights

---

## Higher Cost

More expensive sections:

- statistics
- charts

Especially on:

- large datasets
- wide tables
- high-cardinality data

---

# Fast Mode Interaction

In fast mode, some expensive operations may be reduced.

Example:

```bash
aniwa dataset.csv --mode fast
```

Fast mode prioritizes:

- speed
- lightweight profiling
- quick inspection

---

# Deep Mode Interaction

Deep mode performs complete profiling.

Example:

```bash
aniwa dataset.csv --mode deep
```

Deep mode enables:

- full statistics
- complete analysis
- richer insights

---

# Section-Aware Rendering

Reports dynamically render sections.

Example:

```jinja2
{% if profile.columns %}
```

This prevents:

- empty tables
- invalid layouts
- broken charts

---

# JSON Report Sections

JSON reports also honor section filtering.

Example:

```bash
aniwa dataset.csv \
  --report json \
  --include summary
```

Result:

```json
{
  "summary": {...}
}
```

---

# HTML Report Sections

HTML reports dynamically hide excluded sections.

This improves:

- readability
- rendering performance
- report focus

---

# PDF Report Sections

PDF reports also support filtering.

Useful for:

- governance exports
- lightweight audit reports
- stakeholder documentation

---

# Configuration File Support

Sections may be configured in:

- YAML
- TOML
- JSON configs

Example:

```yaml
sections:
  include:
    - summary
    - insights
```

---

# Internal Section Resolution Logic

Resolution order:

```text
CLI arguments
→ config file
→ defaults
```

Priority:

```text
CLI > config > defaults
```

---

# Section Dependency Philosophy

Sections should remain:

- modular
- composable
- isolated

This allows:

- plugin systems
- future extensions
- independent rendering

---

# Future Section Expansion

Planned future sections include:

- correlations
- outliers
- semantic analysis
- embeddings
- lineage
- observability
- AI summaries
- drift analysis

---

# Possible Future Architecture

Future architecture may evolve into:

```text
sections/
├── summary.py
├── schema.py
├── statistics.py
├── insights.py
├── correlations.py
└── plugins/
```

---

# Enterprise Use Cases

Section filtering enables:

- lightweight compliance reports
- engineering-focused reports
- audit exports
- ML validation pipelines

---

# CI/CD Integration

Examples:

---

## Minimal CI Report

```bash
aniwa dataset.csv \
  --report json \
  --include quality,insights
```

---

## Governance Report

```bash
aniwa dataset.csv \
  --report pdf \
  --include summary,quality,insights
```

---

# Recommended Usage Patterns

---

## Debugging

```bash
--include schema,insights
```

---

## Governance

```bash
--include quality,insights
```

---

## Executive Reporting

```bash
--include summary,charts
```

---

## Data Science

```bash
--include statistics,insights
```

---

# Best Practices

---

## Keep Reports Focused

Avoid unnecessary sections.

---

## Use Fast Mode for Exploration

Useful for quick schema inspection.

---

## Use Deep Mode for Audits

Useful for production-quality analysis.

---

# Common Mistakes

---

## Misspelled Section Names

Incorrect:

```bash
--include stat
```

Correct:

```bash
--include statistics
```

---

## Using Spaces Incorrectly

Incorrect:

```bash
--include summary, insights
```

Correct:

```bash
--include summary,insights
```

---

# Long-Term Vision

Sections are foundational to Aniwa's future architecture.

Future systems may allow:

- dynamic plugins
- custom analyzers
- enterprise policies
- AI-generated sections
- user-defined section pipelines

---

# Future Plugin Possibilities

Example future architecture:

```text
aniwa/plugins/sections/
```

Allowing:

- custom governance checks
- ML profiling modules
- domain-specific validation
- enterprise extensions

---

# Summary

Aniwa sections provide:

- modular profiling
- focused reporting
- scalable architecture
- flexible workflows
- future extensibility

They are a core foundation of Aniwa's long-term intelligence platform vision.

---

# Next Steps

Continue with:

- charts.md
- metadata.md
- configuration.md
- profiling-modes.md