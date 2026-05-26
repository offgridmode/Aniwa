# Reporting System Architecture

This document explains the architecture of Aniwa’s reporting system.

The reporting system is responsible for transforming structured profiling results into:

- human-readable outputs
- machine-readable exports
- visual reports
- shareable documents

Aniwa’s reporting architecture is designed to be:

```text
modular, extensible, scalable, and presentation-focused
```

---

# Purpose of the Reporting System

The reporting system exists to make profiling results:

- understandable
- actionable
- shareable
- automatable

---

# High-Level Reporting Flow

```text
DatasetProfile
→ report renderer
→ formatted output
→ terminal / file / export
```

---

# Reporting Philosophy

Aniwa treats reporting as:

```text
a first-class architectural subsystem
```

not simply:

```text
printing text to the screen
```

---

# Why Reporting Matters

Dataset profiling is only useful if users can:

- interpret results quickly
- share findings easily
- automate workflows reliably

---

# Reporting Design Principles

The reporting system follows several principles:

| Principle | Purpose |
|---|---|
| modular | isolated renderers |
| reusable | shared profile structures |
| extensible | future formats |
| beautiful | strong presentation |
| automation-friendly | machine-readable outputs |
| scalable | large datasets and enterprise reports |

---

# Reporting Architecture Overview

Aniwa’s reporting pipeline:

```text
profiling engine
→ DatasetProfile
→ renderer
→ template
→ output
```

---

# Reporting System Location

Current reporting systems are located in:

```text
aniwa/reports/
```

---

# Current Report Files

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

# Why Separate Renderers Matter

Each report format has:

- different constraints
- different UX goals
- different output requirements

---

# Current Supported Report Formats

Aniwa currently supports:

| Format | Purpose |
|---|---|
| console | terminal UX |
| JSON | automation |
| HTML | visual sharing |
| Markdown | documentation |
| Excel | spreadsheet workflows |
| PDF | printable reports |

---

# Central Reporting Architecture

All report systems consume:

```python
DatasetProfile
```

---

# Why Shared Models Matter

Shared profile models ensure:

- consistency
- easier maintenance
- renderer independence

---

# Renderer Isolation Philosophy

Each renderer should remain:

```text
independent
```

from other renderers.

---

# Why Isolation Matters

Isolation improves:

- maintainability
- extensibility
- debugging
- testing

---

# Console Reporting

Console reporting focuses on:

- developer experience
- fast readability
- interactive workflows

---

# Console Renderer Goals

The console renderer prioritizes:

- clarity
- compactness
- beautiful formatting

---

# Console Technology

Aniwa currently uses:

```text
Rich
```

for terminal rendering.

---

# Why Rich Was Chosen

Rich provides:

- tables
- colors
- panels
- formatting
- modern CLI presentation

---

# Console UX Philosophy

Terminal output should feel:

```text
professional and elegant
```

not:

```text
raw debugging output
```

---

# JSON Reporting

JSON reporting focuses on:

- machine readability
- automation
- interoperability

---

# Why JSON Matters

JSON enables:

- CI/CD integration
- APIs
- automation systems
- downstream processing

---

# JSON Architecture

JSON reports should remain:

- stable
- structured
- predictable

---

# JSON Philosophy

JSON output acts as:

```text
Aniwa’s machine interface
```

---

# HTML Reporting

HTML reporting focuses on:

- visualization
- sharing
- dashboards
- presentation

---

# Why HTML Matters

HTML provides:

- portable reports
- rich layouts
- charts
- visual communication

---

# HTML Architecture

HTML rendering generally follows:

```text
DatasetProfile
→ template
→ rendered HTML
```

---

# Template-Based Architecture

HTML systems use:

```text
Jinja2 templates
```

---

# Why Templates Matter

Templates separate:

- logic
- presentation

---

# Template System Location

Templates are typically stored in:

```text
aniwa/templates/
```

---

# Current Template Philosophy

Templates should support:

- branding
- customization
- future theming

---

# Current Template Types

Aniwa currently includes:

| Template |
|---|
| default |
| clean |
| compact |
| dark |
| enterprise |

---

# Template Goals

Templates should provide:

- distinct visual identities
- different use cases
- reusable presentation systems

---

# Markdown Reporting

Markdown reporting focuses on:

- documentation
- GitHub compatibility
- lightweight exports

---

# Why Markdown Matters

Markdown integrates naturally into:

- repositories
- documentation systems
- issues
- wikis

---

# Markdown Philosophy

Markdown reports should remain:

```text
minimal and readable
```

---

# Excel Reporting

Excel reporting focuses on:

- business workflows
- spreadsheet ecosystems
- analyst compatibility

---

# Why Excel Matters

Many teams still work heavily in:

```text
spreadsheet environments
```

---

# Excel Architecture

Excel reports may include:

- worksheets
- tables
- formatting
- statistics
- metadata

---

# PDF Reporting

PDF reporting focuses on:

- presentation
- printing
- enterprise sharing

---

# Why PDF Matters

PDF provides:

- portability
- professional presentation
- immutable sharing

---

# PDF Rendering Challenges

PDF systems are typically more complex because they require:

- layout control
- rendering consistency
- chart embedding

---

# Current Reporting Flow

Conceptually:

```text
profile
→ renderer
→ formatter
→ output writer
```

---

# Output Path Management

Aniwa supports:

- explicit output files
- generated filenames
- output directories

---

# Why Output Management Matters

Good output systems improve:

- automation
- CI/CD integration
- reproducibility

---

# Report Naming Strategy

Default report names include:

| Format | Default |
|---|---|
| JSON | aniwa_report.json |
| HTML | aniwa_report.html |
| Markdown | aniwa_report.md |
| Excel | aniwa_report.xlsx |
| PDF | aniwa_report.pdf |

---

# Output Directory Support

Aniwa supports:

```text
--output-dir
```

for automatic file generation.

---

# Why Output Directories Matter

This improves:

- automation
- batch workflows
- organized exports

---

# Report Section Architecture

Aniwa supports:

```text
selective report sections
```

---

# Why Section Filtering Matters

Users can generate:

- smaller reports
- focused outputs
- faster renders

---

# Current Sections

Current report sections include:

| Section |
|---|
| summary |
| schema |
| quality |
| statistics |
| insights |
| charts |

---

# Conditional Rendering

Renderers should only render sections when:

```text
relevant data exists
```

---

# Why Conditional Rendering Matters

This improves:

- readability
- performance
- report quality

---

# Chart Architecture

Charts are primarily used in:

- HTML
- PDF

reports.

---

# Current Chart Philosophy

Charts should:

- simplify interpretation
- avoid clutter
- support insight discovery

---

# Current Chart Types

Typical charts include:

| Chart |
|---|
| null percentage |
| uniqueness |
| duplicate overview |

---

# Future Visualization Systems

Future systems may include:

- trend charts
- drift visualizations
- correlation matrices
- lineage graphs

---

# Report Metadata

Reports embed metadata describing:

- execution environment
- runtime information
- configuration

---

# Why Metadata Matters

Metadata enables:

- reproducibility
- debugging
- governance
- auditing

---

# Current Metadata Examples

| Metadata |
|---|
| generated_at |
| profiling_mode |
| report_format |
| template |
| dataset_path |

---

# Styling Philosophy

Reports should feel:

```text
modern, clean, and trustworthy
```

---

# Why Visual Design Matters

Good design improves:

- comprehension
- usability
- adoption

---

# Future Reporting Goals

Future systems may support:

- dashboards
- live reports
- interactive visualizations
- collaborative reports

---

# Future Interactive Reporting

Potential future systems:

```text
interactive HTML dashboards
```

---

# Future Enterprise Reporting

Potential enterprise systems may include:

- branding support
- white-label templates
- governance exports

---

# Future API Reporting

Future APIs may expose reports directly:

```text
profile
→ JSON API
→ frontend dashboard
```

---

# Future Streaming Reports

Long-term systems may support:

- real-time updates
- streaming profiling
- continuous dashboards

---

# Future Distributed Reporting

Large enterprise systems may require:

- distributed rendering
- async exports
- background workers

---

# Reporting Performance Philosophy

Reports should remain:

```text
fast and scalable
```

even for large datasets.

---

# Current Optimization Strategy

Current optimizations include:

- section filtering
- conditional charts
- modular rendering

---

# Future Optimization Areas

Potential future optimizations:

- lazy rendering
- incremental reports
- cached visualizations

---

# Error Handling Philosophy

Renderers should fail:

```text
gracefully and informatively
```

---

# Testing Strategy

Every renderer should be tested independently.

---

# Recommended Renderer Tests

Tests should validate:

| Area |
|---|
| formatting |
| serialization |
| output creation |
| edge cases |
| template rendering |

---

# Future Plugin Architecture

Future report systems may become:

```text
plugin-extensible
```

---

# Potential Future Plugins

Plugins may add:

- custom formats
- enterprise reports
- organization branding

---

# Long-Term Vision

The reporting system is evolving toward:

```text
a universal data reporting platform
```

capable of serving:

- developers
- analysts
- enterprises
- governance systems

---

# Final Philosophy

The reporting system exists to transform:

```text
raw profiling data
```

into:

```text
clear, beautiful, actionable intelligence
```

---

# Related Documentation

Continue with:

- architecture/templates-system.md
- architecture/models.md
- architecture/profiling-engine.md
- api/reports.md