# Report Templates

Aniwa supports multiple report templates designed for different users, workflows, branding styles, and presentation environments.

Templates allow users to customize the visual appearance and layout of generated reports without changing the underlying profiling logic.

---

# Why Templates Matter

Different workflows require different reporting styles.

Examples:

- developers prefer compact reports
- executives prefer polished dashboards
- auditors prefer enterprise formatting
- researchers prefer lightweight layouts

Aniwa templates solve this problem through a modular rendering system.

---

# Current Templates

Aniwa currently supports:

- default
- clean
- compact
- enterprise
- dark

---

# Template Architecture

Templates are implemented as standalone Jinja2 HTML templates.

Location:

```text
aniwa/reports/templates/
```

Example structure:

```text
aniwa/reports/templates/
├── default.html
├── clean.html
├── compact.html
├── enterprise.html
└── dark.html
```

---

# Rendering Flow

Internal rendering flow:

```text
CLI
→ render_html_report()
→ template selection
→ Jinja rendering
→ HTML output
```

---

# Template Selection

Users select templates through the CLI.

Example:

```bash
aniwa dataset.csv \
  --report html \
  --template dark
```

---

# Default Template

The default template provides balanced reporting.

Goals:

- general-purpose readability
- moderate spacing
- clean typography
- strong compatibility

Best for:

- everyday usage
- general profiling
- team collaboration

---

# Clean Template

The clean template focuses on minimalism.

Goals:

- simplicity
- whitespace
- clarity
- elegant presentation

Characteristics:

- minimal borders
- light styling
- reduced visual noise

Best for:

- presentations
- documentation
- lightweight sharing

---

# Compact Template

The compact template prioritizes information density.

Goals:

- maximize visible information
- reduce whitespace
- optimize scanning

Characteristics:

- tighter spacing
- smaller typography
- dense tables

Best for:

- engineers
- analysts
- debugging
- large datasets

---

# Enterprise Template

The enterprise template focuses on professional reporting.

Goals:

- executive readability
- governance reporting
- polished presentation
- corporate aesthetics

Characteristics:

- structured cards
- strong hierarchy
- enterprise-style layout
- enhanced visuals

Best for:

- audits
- stakeholders
- governance
- client reports

---

# Dark Template

The dark template provides a modern dark-mode interface.

Goals:

- reduced eye strain
- modern developer aesthetics
- night-friendly viewing

Characteristics:

- dark backgrounds
- bright charts
- high contrast

Best for:

- developers
- technical teams
- dark-mode users

---

# Template Features

Templates can control:

- colors
- typography
- spacing
- layouts
- cards
- charts
- metadata display
- tables
- responsiveness

---

# Shared Template Data

All templates receive the same profile object.

Example:

```python
template.render(profile=dataset_profile)
```

This guarantees:

- consistent profiling logic
- interchangeable visual layers
- reusable rendering systems

---

# Shared Sections

Templates may render:

- summary
- metadata
- schema
- statistics
- insights
- charts

---

# Chart Integration

Templates support Chart.js visualizations.

Supported charts include:

- null analysis
- unique counts
- duplicate analysis

---

# Responsive Design

Templates are responsive by default.

Goals:

- mobile compatibility
- tablet readability
- desktop optimization

---

# Template Styling Philosophy

Aniwa templates prioritize:

- readability
- modularity
- maintainability
- performance
- visual clarity

---

# HTML Technologies Used

Aniwa templates rely on:

- HTML5
- CSS3
- Jinja2
- Chart.js

---

# Why Jinja2?

Jinja2 was selected because it provides:

- flexible templating
- fast rendering
- Python integration
- reusable layouts
- conditional rendering

---

# Conditional Rendering

Templates dynamically render sections.

Example:

```jinja2
{% if profile.columns %}
```

This prevents:

- empty sections
- broken layouts
- unnecessary rendering

---

# Template Modularity

Templates should remain:

- isolated
- interchangeable
- extensible

Each template should:

- avoid profiling logic
- focus purely on presentation

---

# Future Template Goals

Future improvements may include:

- branding systems
- custom themes
- plugin templates
- user-defined templates
- accessibility themes
- localization
- print optimization

---

# Planned Template System Evolution

Future architecture may support:

```text
aniwa/plugins/templates/
```

Allowing:

- community templates
- enterprise branding packs
- custom visual ecosystems

---

# Creating a Custom Template

Future versions may support:

```bash
aniwa dataset.csv \
  --template my-company
```

Possible architecture:

```text
templates/
plugins/
user_templates/
```

---

# Recommended Design Principles

When designing templates:

- prioritize readability
- avoid visual clutter
- maintain responsiveness
- support accessibility
- minimize rendering complexity

---

# Accessibility Goals

Future accessibility goals include:

- WCAG compliance
- colorblind-safe palettes
- keyboard navigation
- screen reader support
- high-contrast modes

---

# Enterprise Reporting Vision

Long-term enterprise reporting goals:

- branded reports
- governance dashboards
- compliance exports
- executive summaries
- audit trails

---

# Template Performance

Large datasets can impact rendering performance.

Optimization strategies include:

- lazy chart rendering
- chunked table rendering
- pagination
- virtualization
- async rendering

---

# PDF Template Relationship

PDF reports may reuse HTML template structures.

Possible future flow:

```text
HTML Template
→ PDF Renderer
→ PDF Export
```

Benefits:

- consistency
- reduced duplication
- unified branding

---

# Template Metadata

Templates may expose:

- Aniwa version
- generation timestamps
- runtime metadata
- dataset metadata

---

# Example Usage

---

## Default Template

```bash
aniwa dataset.csv \
  --report html
```

---

## Dark Template

```bash
aniwa dataset.csv \
  --report html \
  --template dark
```

---

## Enterprise Template

```bash
aniwa dataset.csv \
  --report pdf \
  --template enterprise
```

---

## Compact Template

```bash
aniwa dataset.csv \
  --report html \
  --template compact
```

---

# Recommended Template Usage

| Workflow | Recommended Template |
|---|---|
| development | compact |
| governance | enterprise |
| documentation | clean |
| presentations | clean |
| engineering | dark |
| audits | enterprise |

---

# Common Mistakes

---

## Unsupported Template Names

Incorrect:

```bash
--template futuristic
```

Correct:

```bash
--template dark
```

---

## Forgetting Report Type

Incorrect:

```bash
aniwa dataset.csv --template dark
```

Correct:

```bash
aniwa dataset.csv \
  --report html \
  --template dark
```

---

# Long-Term Vision

Aniwa templates are intended to evolve into a complete reporting ecosystem supporting:

- interactive reporting
- collaborative analytics
- semantic reporting
- AI-generated narratives
- observability integrations
- governance dashboards

---

# Next Steps

Continue with:

- sections.md
- charts.md
- metadata.md
- configuration.md