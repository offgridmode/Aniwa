# Adding Report Templates

This guide explains how to create, structure, extend, and maintain report templates in Aniwa.

Templates are one of the most important parts of Aniwa’s reporting system because they control:

- layout
- styling
- visual hierarchy
- presentation quality
- report usability

Templates transform:

```text
structured profiling intelligence
```

into:

```text
beautiful, understandable visual reports
```

---

# Purpose of Templates

Templates separate:

```text
presentation
```

from:

```text
business logic
```

---

# Why Templates Matter

Without templates:

- renderers become difficult to maintain
- styling becomes inconsistent
- customization becomes fragile
- visual scalability becomes difficult

---

# Template Philosophy

Aniwa templates are designed to be:

| Principle | Purpose |
|---|---|
| modular | reusable layouts |
| maintainable | isolated presentation |
| extensible | future themes |
| responsive | multi-device support |
| beautiful | professional UX |

---

# Template Engine Overview

Current rendering flow:

```text
DatasetProfile
→ renderer
→ Jinja2 template
→ HTML output
→ final report
```

---

# Current Template Engine

Aniwa currently uses:

```text
Jinja2
```

---

# Why Jinja2 Was Chosen

Jinja2 provides:

- clean syntax
- reusable templates
- conditionals
- loops
- template inheritance
- strong Python integration

---

# Current Template Location

Templates are typically stored in:

```text
aniwa/templates/
```

---

# Example Template Structure

Example:

```text
aniwa/templates/
├── default.html
├── clean.html
├── compact.html
├── dark.html
├── enterprise.html
```

---

# Current Template Types

Aniwa currently supports:

| Template |
|---|
| default |
| clean |
| compact |
| dark |
| enterprise |

---

# Why Multiple Templates Matter

Different users prefer different report styles.

Examples:

| User | Preferred Style |
|---|---|
| developers | compact |
| executives | enterprise |
| dashboards | dark |
| documentation | clean |

---

# Template Responsibilities

Templates should handle:

- layout
- styling
- spacing
- rendering organization
- conditional display

---

# Templates Should NOT Handle

Templates should NOT contain:

- profiling logic
- dataframe computation
- business rules
- dataset analysis

---

# Why Logic Separation Matters

Separation improves:

- maintainability
- readability
- scalability
- contributor onboarding

---

# Template Data Source

Templates consume:

```python
DatasetProfile
```

---

# Typical Template Context

Example:

```python
profile.summary
profile.columns
profile.insights
profile.metadata
```

---

# Step-by-Step Guide

---

# Step 1 — Create the Template File

Add a new template inside:

```text
aniwa/templates/
```

---

# Example

Example:

```text
aniwa/templates/minimal.html
```

---

# Step 2 — Start With Standard HTML Structure

Basic example:

```html
<!DOCTYPE html>
<html>
<head>
</head>
<body>
</body>
</html>
```

---

# Step 3 — Add Jinja2 Variables

Example:

```jinja2
{{ profile.summary.rows }}
```

---

# Step 4 — Add Conditional Rendering

Example:

```jinja2
{% if profile.insights %}
```

---

# Why Conditional Rendering Matters

This prevents:

- empty sections
- broken layouts
- visual clutter

---

# Step 5 — Organize Sections Clearly

Recommended sections:

| Section |
|---|
| header |
| metadata |
| summary |
| schema |
| statistics |
| insights |
| charts |

---

# Step 6 — Add Styling

Templates may include:

- inline CSS
- linked stylesheets
- reusable utility classes

---

# Current Styling Philosophy

Aniwa styling should feel:

```text
modern, clean, and professional
```

---

# Design Priorities

Templates should prioritize:

- readability
- spacing
- information hierarchy
- accessibility

---

# Typography Philosophy

Typography should remain:

- clean
- minimal
- readable

---

# Recommended Font Styles

Good font categories:

| Style |
|---|
| sans-serif |
| developer-friendly |
| modern UI fonts |

---

# Color Philosophy

Templates should maintain:

- strong contrast
- visual consistency
- restrained palettes

---

# Layout Philosophy

Layouts should remain:

```text
structured and uncluttered
```

---

# Responsive Design Philosophy

Reports should work across:

- desktops
- tablets
- mobile devices

---

# Why Responsiveness Matters

Reports are often:

- shared
- viewed remotely
- embedded into workflows

---

# Current Responsive Strategies

Typical techniques:

- CSS grids
- media queries
- flexible containers

---

# Chart Integration

Templates may include charts.

---

# Current Chart Engine

Aniwa currently uses:

```text
Chart.js
```

---

# Why Charts Matter

Charts improve:

- readability
- executive communication
- insight discovery

---

# Current Chart Types

Typical charts:

| Chart |
|---|
| null percentages |
| unique values |
| duplicate overview |

---

# Chart Rendering Flow

Typical flow:

```text
DatasetProfile
→ JSON serialization
→ Chart.js
→ visualization
```

---

# Metadata Rendering

Templates should render metadata such as:

- profiling mode
- dataset path
- generated time
- Aniwa version

---

# Why Metadata Matters

Metadata improves:

- reproducibility
- governance
- debugging

---

# Example Metadata Block

Example:

```jinja2
{{ profile.metadata.generated_at }}
```

---

# Empty State Philosophy

Templates should gracefully handle:

- missing sections
- empty datasets
- absent insights

---

# Example Empty State

Example:

```html
<p>No insights detected.</p>
```

---

# Template Naming Philosophy

Template names should remain:

```text
clear and descriptive
```

---

# Good Template Names

Examples:

| Name |
|---|
| clean |
| dark |
| enterprise |
| compact |

---

# Bad Template Names

Avoid vague names like:

```text
template2
```

---

# Template Scalability Philosophy

Templates should remain:

```text
modular and extensible
```

---

# Why Scalability Matters

Report systems grow significantly over time.

---

# Future Template Inheritance

Future systems may use:

```text
base templates
```

---

# Example Future Structure

Example:

```text
base.html
↓
enterprise.html
↓
dark.html
```

---

# Why Template Inheritance Matters

Inheritance improves:

- reuse
- consistency
- maintainability

---

# Future Component Systems

Future templates may evolve into:

```text
component-based architectures
```

---

# Potential Future Components

Possible reusable components:

| Component |
|---|
| summary cards |
| schema tables |
| metadata panels |
| chart blocks |

---

# Future Dashboard Templates

Potential future systems:

- interactive dashboards
- live profiling UIs
- observability interfaces

---

# Future Theme Systems

Potential future features:

- custom themes
- organization branding
- dark/light switching

---

# Enterprise Branding Vision

Future enterprise systems may support:

- company logos
- brand palettes
- white-label reports

---

# Future Interactive Systems

Potential future capabilities:

| Feature |
|---|
| collapsible sections |
| dynamic filtering |
| searchable tables |
| interactive charts |

---

# Accessibility Philosophy

Templates should remain accessible.

---

# Accessibility Goals

Future accessibility improvements:

- semantic HTML
- keyboard support
- contrast compliance

---

# Performance Philosophy

Templates should remain:

```text
fast and lightweight
```

---

# Why Performance Matters

Large reports can become:

- slow to render
- memory-heavy
- browser-intensive

---

# Current Optimization Strategies

Current goals include:

- conditional rendering
- lightweight layouts
- reusable structures

---

# Future Optimization Areas

Potential improvements:

| Optimization |
|---|
| lazy loading |
| virtualized tables |
| deferred chart rendering |

---

# Security Philosophy

Templates should avoid:

- unsafe rendering
- arbitrary execution
- untrusted injection

---

# Safe Rendering Practices

Prefer:

- escaped rendering
- sanitized inputs
- controlled rendering paths

---

# Testing Philosophy

Templates should be tested independently.

---

# Recommended Template Tests

Tests should validate:

| Area |
|---|
| rendering success |
| responsive layout |
| chart rendering |
| empty states |
| metadata rendering |

---

# Example Template Test

Example:

```python
def test_template_renders():
```

---

# Template Anti-Patterns

Avoid:

| Anti-Pattern |
|---|
| business logic in templates |
| excessive inline scripting |
| cluttered layouts |
| duplicated structures |

---

# Contributor Best Practices

Contributors should prioritize:

- readability
- consistency
- maintainability
- responsiveness

---

# Pull Request Checklist

Before submitting:

- template renders correctly
- responsive design works
- charts render properly
- tests pass
- documentation updated

---

# Future Plugin Template Vision

Future systems may support:

```text
third-party template plugins
```

---

# Example Future Plugin Flow

Example:

```text
plugin
→ custom template
→ renderer
→ report
```

---

# Long-Term Vision

Aniwa’s template system is evolving toward:

```text
a universal data presentation framework
```

---

# Strategic Importance

Templates are not merely:

```text
visual decoration
```

They are:

```text
the communication layer between data intelligence and humans
```

---

# Final Philosophy

The template system exists to ensure that:

```text
dataset intelligence becomes visually understandable, elegant, and actionable
```

---

# Related Documentation

Continue with:

- architecture/template-engine.md
- architecture/reporting-system.md
- api/reports.md
- developer-guide/adding-report-formats.md