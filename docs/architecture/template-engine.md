# Template Engine Architecture

This document explains the architecture, philosophy, rendering flow, scalability strategy, and future evolution of Aniwa’s template engine.

The template engine powers:

- HTML reports
- PDF layouts
- visual styling
- reusable presentation systems
- future dashboard rendering

The template system is a foundational part of Aniwa’s reporting architecture.

---

# Purpose of the Template Engine

The template engine exists to separate:

```text
presentation
```

from:

```text
business logic
```

---

# Why Template Systems Matter

Without templates:

- rendering logic becomes messy
- styling becomes difficult
- customization becomes fragile
- scalability becomes painful

---

# Core Philosophy

Aniwa’s template engine follows several principles:

| Principle | Purpose |
|---|---|
| separation of concerns | cleaner architecture |
| reusability | shared rendering systems |
| extensibility | future templates |
| customization | different report styles |
| maintainability | isolated presentation logic |

---

# High-Level Rendering Flow

```text
DatasetProfile
→ renderer
→ template engine
→ rendered output
→ final report
```

---

# Template Engine Location

Current template systems typically live in:

```text
aniwa/templates/
```

---

# Current Template Architecture

Conceptually:

```text
aniwa/templates/
├── default.html
├── clean.html
├── compact.html
├── dark.html
├── enterprise.html
```

---

# Why Separate Templates Matter

Different users require different presentation styles:

| User Type | Preferred Style |
|---|---|
| developers | compact |
| executives | enterprise |
| dashboards | dark |
| documentation | clean |

---

# Current Template Engine Technology

Aniwa currently uses:

```text
Jinja2
```

for templating.

---

# Why Jinja2 Was Chosen

Jinja2 provides:

- clean syntax
- reusable templates
- conditional rendering
- loops
- template inheritance
- strong Python integration

---

# Template Engine Philosophy

Templates should contain:

```text
presentation logic only
```

not:

```text
profiling business logic
```

---

# Why Business Logic Separation Matters

This improves:

- maintainability
- readability
- scalability
- contributor onboarding

---

# Template Rendering Lifecycle

The rendering lifecycle typically follows:

```text
DatasetProfile
↓
renderer
↓
template context
↓
Jinja2 rendering
↓
HTML output
```

---

# Renderer Responsibilities

The renderer is responsible for:

- preparing data
- validating templates
- invoking the engine
- saving output

---

# Template Responsibilities

Templates are responsible for:

- layout
- styling
- visual organization
- conditional display

---

# DatasetProfile as Template Context

Templates receive:

```python
DatasetProfile
```

as structured rendering data.

---

# Why Structured Context Matters

Structured context provides:

- predictable rendering
- simpler templates
- cleaner architecture

---

# Current Template Data Structure

Typical template context:

```python
profile.summary
profile.columns
profile.quality
profile.insights
profile.metadata
```

---

# Conditional Rendering Philosophy

Templates should render sections only when data exists.

---

# Why Conditional Rendering Matters

This prevents:

- empty sections
- broken layouts
- visual clutter

---

# Example Conditional Rendering

Example:

```jinja2
{% if profile.insights %}
```

---

# Current Template Types

Aniwa currently includes several template styles.

---

# Default Template

Purpose:

```text
balanced professional reporting
```

---

# Clean Template

Purpose:

```text
minimal lightweight reporting
```

---

# Compact Template

Purpose:

```text
dense technical inspection
```

---

# Dark Template

Purpose:

```text
modern dark-themed presentation
```

---

# Enterprise Template

Purpose:

```text
executive and business reporting
```

---

# Why Multiple Templates Matter

Multiple templates improve:

- flexibility
- adoption
- visual personalization

---

# HTML Structure Philosophy

Templates should maintain:

- semantic HTML
- accessibility
- responsiveness
- maintainable structure

---

# CSS Philosophy

Styling should remain:

```text
clean, modern, and modular
```

---

# Current Styling Goals

Aniwa templates prioritize:

- readability
- spacing
- typography
- information hierarchy

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
- embedded in workflows

---

# Current Responsive Strategy

Templates currently use:

- CSS grids
- flexible layouts
- media queries

---

# Chart Integration

Templates integrate visualizations using:

```text
Chart.js
```

---

# Why Charts Matter

Charts improve:

- insight discovery
- readability
- executive communication

---

# Current Chart Types

Current visualizations include:

| Chart |
|---|
| null percentage |
| unique values |
| duplicate overview |

---

# Chart Rendering Flow

```text
profile data
→ serialized JSON
→ Chart.js
→ visualization
```

---

# Why Serialized Chart Data Matters

Serialized data simplifies:

- frontend rendering
- chart reuse
- scalability

---

# Metadata Rendering

Templates render profiling metadata such as:

- runtime
- dataset path
- profiling mode
- report format

---

# Why Metadata Matters

Metadata improves:

- reproducibility
- debugging
- auditing

---

# Template Scalability Philosophy

Templates should remain:

```text
independent and reusable
```

---

# Why Template Scalability Matters

As report complexity grows:

- templates must remain maintainable
- styles must remain isolated

---

# Future Template Inheritance

Future systems may use:

```text
template inheritance
```

---

# Example Future Inheritance

Potential architecture:

```text
base.html
↓
child templates
```

---

# Why Template Inheritance Matters

Inheritance improves:

- reuse
- maintainability
- consistency

---

# Future Component Architecture

Future templates may evolve into:

```text
component-based systems
```

---

# Potential Future Components

Components may include:

| Component |
|---|
| summary cards |
| schema tables |
| charts |
| metadata panels |

---

# Future Interactive Reports

Future systems may support:

- filtering
- collapsible sections
- interactive charts
- dynamic dashboards

---

# Future Dashboard Architecture

Potential future architecture:

```text
API
→ frontend app
→ live dashboards
```

---

# Future Web Application Support

Long-term systems may power:

```text
Aniwa Web
```

---

# Future Theme System

Potential future features:

- theme switching
- organization branding
- custom palettes

---

# Enterprise Branding Vision

Enterprise users may eventually support:

- logos
- colors
- branded exports
- white-label reporting

---

# Future PDF Template Systems

Future PDF systems may share:

- HTML templates
- CSS styling
- rendering engines

---

# Why Shared Rendering Matters

Shared systems reduce:

- duplicated effort
- inconsistent styling

---

# Future Report Localization

Potential future systems may support:

- multiple languages
- localization
- international formatting

---

# Accessibility Philosophy

Templates should remain accessible.

---

# Accessibility Goals

Future accessibility targets:

- semantic HTML
- contrast compliance
- keyboard compatibility

---

# Performance Philosophy

Templates should remain:

```text
fast and lightweight
```

---

# Why Template Performance Matters

Large reports can become expensive.

Efficient templates improve:

- rendering speed
- browser responsiveness
- scalability

---

# Current Optimization Strategies

Current optimizations include:

- conditional rendering
- lightweight layouts
- reusable structures

---

# Future Optimization Strategies

Potential future improvements:

- virtualized tables
- lazy chart rendering
- incremental report loading

---

# Security Philosophy

Templates should never:

- execute arbitrary code
- expose unsafe rendering paths

---

# Safe Rendering Principles

Template systems should prioritize:

- controlled rendering
- sanitized outputs
- predictable execution

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
| chart generation |
| empty states |
| metadata rendering |

---

# Future Plugin Templates

Future plugin systems may allow:

```text
third-party templates
```

---

# Potential Plugin Template Flow

```text
plugin
→ custom template
→ renderer
→ report
```

---

# Long-Term Vision

The template engine is evolving toward:

```text
a universal data presentation framework
```

---

# Strategic Importance

The template system is not merely:

```text
visual decoration
```

It is a:

```text
critical communication layer
```

between:

- data
- intelligence
- humans

---

# Final Philosophy

The template engine exists to ensure that:

```text
complex dataset intelligence becomes visually understandable, beautiful, and actionable
```

---

# Related Documentation

Continue with:

- architecture/reporting-system.md
- architecture/system-design.md
- architecture/performance-strategy.md
- api/reports.md