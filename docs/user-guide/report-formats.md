# Report Formats

Aniwa supports multiple report formats designed for different workflows, users, and environments.

Report formats determine how profiling results are rendered, stored, shared, and consumed.

---

# Supported Report Formats

Aniwa currently supports:

- console
- json
- html
- excel
- markdown
- pdf

---

# Console Reports

Console reports are the default output format.

Example:

```bash
aniwa dataset.csv
```

---

# Console Report Goals

Console reports prioritize:

- fast feedback
- terminal readability
- developer experience
- lightweight inspection

---

# Console Features

Console reports include:

- dataset summary
- schema overview
- statistics
- insights
- metadata
- rich formatting

---

# Console Architecture

Console rendering is primarily implemented in:

```text
aniwa/reports/console.py
```

Built using:

- Rich
- Rich Tables
- Rich Panels

---

# JSON Reports

JSON reports provide machine-readable profiling output.

Example:

```bash
aniwa dataset.csv \
  --report json \
  --output profile.json
```

---

# JSON Report Goals

JSON reports prioritize:

- automation
- integrations
- APIs
- machine readability
- structured data exchange

---

# JSON Use Cases

JSON reports are ideal for:

- CI/CD pipelines
- APIs
- dashboards
- automation systems
- orchestration platforms

---

# JSON Architecture

JSON rendering is implemented in:

```text
aniwa/reports/json_report.py
```

JSON serialization relies heavily on:

- Pydantic
- structured models

---

# HTML Reports

HTML reports provide visually rich, shareable reports.

Example:

```bash
aniwa dataset.csv \
  --report html \
  --template enterprise
```

---

# HTML Report Goals

HTML reports prioritize:

- presentation
- collaboration
- readability
- visual richness
- stakeholder sharing

---

# HTML Features

HTML reports support:

- charts
- templates
- responsive layouts
- metadata
- visual insights

---

# HTML Templates

Available templates:

- default
- clean
- compact
- enterprise
- dark

---

# HTML Architecture

HTML rendering is implemented in:

```text
aniwa/reports/html_report.py
```

Template system:

```text
aniwa/reports/templates/
```

Rendering technologies:

- Jinja2
- HTML/CSS
- Chart.js

---

# Excel Reports

Excel reports provide spreadsheet-native outputs.

Example:

```bash
aniwa dataset.csv \
  --report excel
```

---

# Excel Report Goals

Excel reports prioritize:

- analyst workflows
- spreadsheet compatibility
- offline sharing
- tabular exploration

---

# Excel Features

Excel reports may include:

- summary sheets
- schema sheets
- statistics sheets
- quality sheets
- formatting
- multiple worksheets

---

# Excel Architecture

Excel rendering is implemented in:

```text
aniwa/reports/excel_report.py
```

Powered by:

- OpenPyXL

---

# Markdown Reports

Markdown reports provide lightweight documentation-friendly output.

Example:

```bash
aniwa dataset.csv \
  --report markdown
```

---

# Markdown Report Goals

Markdown reports prioritize:

- GitHub compatibility
- documentation
- readability
- lightweight portability

---

# Markdown Use Cases

Markdown reports are ideal for:

- GitHub issues
- pull requests
- documentation
- changelogs
- lightweight reporting

---

# Markdown Architecture

Markdown rendering is implemented in:

```text
aniwa/reports/markdown_report.py
```

---

# PDF Reports

PDF reports provide professional printable reporting.

Example:

```bash
aniwa dataset.csv \
  --report pdf \
  --template enterprise
```

---

# PDF Report Goals

PDF reports prioritize:

- audits
- governance
- compliance
- executive reporting
- archival storage

---

# PDF Features

PDF reports support:

- professional layouts
- charts
- templates
- printable formatting
- metadata
- branded reporting

---

# PDF Architecture

PDF rendering is implemented in:

```text
aniwa/reports/pdf_report.py
```

Powered by:

- ReportLab

---

# Report Generation Flow

Internal execution flow:

```text
CLI
→ profiler
→ dataset profile
→ renderer selection
→ report generation
```

---

# Report Selection

Example:

```bash
aniwa dataset.csv --report html
```

Internally:

```python
if report == ReportFormat.html:
    render_html_report(...)
```

---

# Output Resolution

Aniwa automatically resolves:

- filenames
- extensions
- output directories

Example:

```bash
aniwa dataset.csv \
  --report pdf \
  --output-dir reports/
```

Generated output:

```text
reports/aniwa_report.pdf
```

---

# Output File Extensions

| Format | Extension |
|---|---|
| console | none |
| json | .json |
| html | .html |
| excel | .xlsx |
| markdown | .md |
| pdf | .pdf |

---

# Report Metadata

All report formats can include metadata such as:

- profiling duration
- Aniwa version
- Python version
- dataset size
- operating system
- command executed

---

# Report Sections

Supported report sections:

- summary
- schema
- quality
- statistics
- insights
- charts

---

# Including Sections

Example:

```bash
aniwa dataset.csv \
  --include summary,statistics
```

---

# Excluding Sections

Example:

```bash
aniwa dataset.csv \
  --exclude charts
```

---

# Best Report Formats By Use Case

| Use Case | Recommended Format |
|---|---|
| quick inspection | console |
| automation | json |
| stakeholder sharing | html |
| governance | pdf |
| spreadsheets | excel |
| documentation | markdown |

---

# Scalability Considerations

Long-term reporting scalability goals include:

- streaming report generation
- chunked exports
- lazy rendering
- distributed rendering
- template plugins
- report versioning

---

# Future Report Formats

Potential future formats:

- CSV summary exports
- interactive dashboards
- notebook outputs
- Power BI exports
- Tableau exports
- OpenMetadata integration
- DataHub integration

---

# Design Philosophy

Aniwa reporting is designed to be:

- modular
- extensible
- automation-friendly
- visually consistent
- developer-first

---

# Recommended Workflows

---

## Developer Workflow

```bash
aniwa dataset.csv
```

---

## Team Sharing

```bash
aniwa dataset.csv \
  --report html
```

---

## Governance Audit

```bash
aniwa dataset.csv \
  --report pdf \
  --template enterprise
```

---

## CI Automation

```bash
aniwa dataset.csv \
  --report json
```

---

# Common Mistakes

---

## Missing Output Path

Incorrect:

```bash
aniwa dataset.csv --report html
```

Correct:

```bash
aniwa dataset.csv \
  --report html \
  --output profile.html
```

---

## Unsupported Template

Incorrect:

```bash
--template ultra
```

Supported:

- default
- clean
- compact
- enterprise
- dark

---

# Future Vision

Long-term reporting goals include:

- real-time dashboards
- AI-generated narratives
- semantic reports
- collaborative reports
- embedded observability
- dataset trust scoring

---

# Next Steps

Continue with:

- report-templates.md
- sections.md
- charts.md
- metadata.md