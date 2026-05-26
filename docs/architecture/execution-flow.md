# Execution Flow Architecture

The execution flow architecture defines how Aniwa operates internally from the moment a user runs a command to the moment profiling results are rendered.

This document explains:

- the complete runtime lifecycle
- execution orchestration
- internal system interactions
- data movement through the application
- architectural responsibilities
- scalability implications

Understanding execution flow is critical for:

- contributors
- maintainers
- future architects
- performance optimization
- debugging
- scalability planning

---

# High-Level Execution Philosophy

Aniwa is designed around a pipeline-oriented execution architecture.

Core philosophy:

```text
input
→ ingestion
→ profiling
→ intelligence
→ rendering
→ output
```

This creates:

- modularity
- extensibility
- maintainability
- scalability

---

# High-Level Runtime Flow

```text
User CLI Command
        ↓
CLI Parsing
        ↓
Configuration Resolution
        ↓
Input Validation
        ↓
Dataset Reading
        ↓
Profiling Engine
        ↓
Insight Generation
        ↓
Metadata Generation
        ↓
Report Rendering
        ↓
Output Delivery
```

---

# Why Pipeline Architecture Matters

Pipeline architectures are ideal for:

- data systems
- profiling workflows
- observability systems
- ETL tooling
- scalable infrastructure

Benefits include:

- separation of concerns
- isolated subsystems
- easier testing
- extensibility
- parallelization potential

---

# Full Runtime Lifecycle

---

# Phase 1 — CLI Invocation

Execution begins when the user runs:

```bash
aniwa customers.csv
```

or:

```bash
aniwa customers.csv --report html
```

---

# Entry Point

Primary runtime entry point:

```text
aniwa/cli.py
```

---

# CLI System Responsibilities

The CLI layer is responsible for:

- parsing arguments
- validating options
- loading configuration
- orchestrating execution
- dispatching reports

The CLI is NOT responsible for:

- dataset profiling
- report rendering logic
- statistical calculations

---

# Why Thin CLI Architecture Matters

Thin CLIs are:

- easier to maintain
- easier to scale
- easier to test
- more reusable

---

# Phase 2 — Argument Parsing

Aniwa uses:

```text
Typer
```

for command-line parsing.

---

# Typer Responsibilities

Typer handles:

- option parsing
- enum validation
- argument handling
- CLI help generation
- command routing

---

# Example Runtime Parsing

```bash
aniwa customers.csv --report html --mode deep
```

becomes:

```python
path="customers.csv"
report="html"
mode="deep"
```

---

# Why Typed CLI Systems Matter

Typed CLIs improve:

- reliability
- validation
- readability
- developer experience

---

# Phase 3 — Configuration Resolution

After CLI parsing:

Aniwa loads configuration files.

---

# Configuration Discovery Flow

```text
current directory
→ aniwa.yaml
→ aniwa.yml
→ aniwa.toml
→ aniwa.json
```

---

# Config Resolution Priority

Aniwa resolves runtime settings using:

```text
CLI arguments > config file > defaults
```

---

# Example Resolution

Config:

```yaml
mode: deep
```

CLI:

```bash
--mode fast
```

Final runtime:

```text
fast
```

---

# Why Resolution Order Matters

This creates:

- predictable behavior
- automation compatibility
- flexible overrides

---

# Phase 4 — Runtime Normalization

Configuration values are normalized into internal runtime objects.

Examples:

```python
ReportFormat.html
ProfileMode.deep
```

---

# Why Runtime Normalization Matters

Normalization improves:

- consistency
- validation
- internal type safety

---

# Phase 5 — Section Resolution

Aniwa resolves report sections.

Examples:

```bash
--include summary,statistics
```

or:

```bash
--exclude charts
```

---

# Section Resolution Flow

```text
CLI/config values
→ validate sections
→ resolve include/exclude
→ final section set
```

---

# Why Section Resolution Matters

This enables:

- focused reports
- smaller outputs
- faster rendering
- flexible workflows

---

# Phase 6 — Output Resolution

Aniwa determines final output destinations.

---

# Output Resolution Responsibilities

The system:

- resolves filenames
- applies extensions
- handles output directories
- creates missing directories

---

# Example Flow

```bash
--output-dir reports/
```

becomes:

```text
reports/aniwa_report.html
```

---

# Why Output Resolution Matters

This supports:

- automation
- CI/CD
- reproducibility
- enterprise workflows

---

# Phase 7 — Input Validation

Aniwa validates:

- dataset existence
- supported file types
- configuration integrity
- report options

---

# Validation Philosophy

Validation should occur:

```text
as early as possible
```

---

# Why Early Validation Matters

Benefits:

- faster feedback
- fewer runtime failures
- cleaner error handling

---

# Phase 8 — Dataset Ingestion

Aniwa reads datasets using:

```text
aniwa/io/readers.py
```

---

# Reader Responsibilities

Readers:

- detect formats
- load datasets
- normalize inputs
- return Polars DataFrames

---

# Reader Flow

```text
file path
→ extension detection
→ correct reader
→ DataFrame
```

---

# Supported Formats

Current formats:

| Format |
|---|
| CSV |
| Excel |
| JSON |
| Parquet |

---

# Why Reader Isolation Matters

Reader isolation enables:

- modularity
- future connectors
- extensibility

---

# Future Reader Vision

Future readers may support:

- PostgreSQL
- MySQL
- DuckDB
- BigQuery
- Snowflake
- APIs
- cloud storage

---

# Phase 9 — Profiling Engine

After ingestion:

datasets enter the profiling engine.

---

# Profiling Entry Point

Primary function:

```python
profile_dataframe()
```

---

# Profiling Responsibilities

The profiler:

- analyzes schema
- computes statistics
- detects nulls
- identifies duplicates
- generates insights

---

# Profiling Flow

```text
DataFrame
→ summary analysis
→ schema analysis
→ quality analysis
→ statistics
→ insights
→ DatasetProfile
```

---

# Why Centralized Profiling Matters

Centralized profiling ensures:

- reusable intelligence
- consistent outputs
- shared logic

---

# DatasetProfile Object

The profiler produces:

```python
DatasetProfile
```

---

# Why DatasetProfile Matters

This object acts as:

```text
Aniwa's universal intelligence container
```

---

# DatasetProfile Responsibilities

Contains:

- summaries
- schema
- quality metrics
- statistics
- insights
- metadata

---

# Architectural Importance

This abstraction enables:

```text
one profiling system
→ many outputs
```

---

# Phase 10 — Insight Generation

Aniwa generates intelligent observations.

Examples:

- duplicate warnings
- sparse columns
- high-cardinality columns
- potential sensitive data

---

# Why Insights Matter

Insights elevate Aniwa beyond:

```text
basic statistics
```

into:

```text
dataset intelligence
```

---

# Future Insight Vision

Future insights may include:

- semantic understanding
- anomaly detection
- AI summarization
- trust scoring

---

# Phase 11 — Metadata Generation

Aniwa generates profiling metadata.

Examples:

- profiling duration
- dataset size
- OS
- Python version
- command used
- report format

---

# Why Metadata Matters

Metadata enables:

- auditing
- reproducibility
- debugging
- governance

---

# Phase 12 — Report Dispatching

The CLI dispatches the profile into the correct renderer.

---

# Dispatch Flow

```text
DatasetProfile
→ report type selection
→ renderer
→ output
```

---

# Current Renderers

| Renderer |
|---|
| console |
| json |
| html |
| markdown |
| excel |
| pdf |

---

# Why Dispatch Architecture Matters

Dispatch systems enable:

- modular rendering
- clean extensibility
- isolated outputs

---

# Phase 13 — Rendering

Each renderer transforms the profile into a specific format.

---

# Rendering Philosophy

Renderers should:

- consume profiles
- avoid profiling logic
- remain format-specific

---

# Why Renderer Isolation Matters

This enables:

- cleaner systems
- reusable intelligence
- simpler maintenance

---

# Phase 14 — Output Delivery

Outputs are:

- printed
- written to files
- rendered visually

depending on format.

---

# Console Flow

```text
DatasetProfile
→ Rich tables
→ terminal output
```

---

# HTML Flow

```text
DatasetProfile
→ Jinja templates
→ HTML rendering
→ browser output
```

---

# JSON Flow

```text
DatasetProfile
→ serialization
→ JSON file
```

---

# Excel Flow

```text
DatasetProfile
→ workbook generation
→ spreadsheet
```

---

# PDF Flow

```text
DatasetProfile
→ layout rendering
→ PDF generation
```

---

# Complete Execution Diagram

```text
CLI
 ↓
Configuration
 ↓
Validation
 ↓
Reader
 ↓
DataFrame
 ↓
Profiler
 ↓
DatasetProfile
 ↓
Renderer
 ↓
Output
```

---

# Architectural Layers

Aniwa currently operates with layered architecture.

---

# Current Layers

```text
Presentation Layer
    CLI
        ↓

Configuration Layer
        ↓

Ingestion Layer
        ↓

Profiling Layer
        ↓

Intelligence Layer
        ↓

Rendering Layer
        ↓

Output Layer
```

---

# Why Layered Architecture Matters

Layered systems improve:

- scalability
- maintainability
- modularity
- testing

---

# Separation of Concerns

Aniwa strongly separates:

| Concern | Responsibility |
|---|---|
| CLI | orchestration |
| Readers | ingestion |
| Profiler | intelligence |
| Reports | rendering |
| Config | runtime behavior |

---

# Why Separation Matters

Without separation:

- systems become tightly coupled
- maintenance becomes difficult
- scaling becomes dangerous

---

# Performance Considerations

Current execution is mostly synchronous.

---

# Current Performance Bottlenecks

Potential bottlenecks:

- large dataset loading
- statistics computation
- HTML rendering
- PDF generation

---

# Future Performance Vision

Future optimization areas:

- lazy execution
- streaming
- chunked processing
- parallel profiling
- distributed execution

---

# Future Distributed Vision

Long-term architecture may support:

```text
distributed profiling workers
```

---

# Potential Future Architecture

```text
CLI
→ orchestrator
→ profiling workers
→ aggregation engine
→ report renderer
```

---

# Future Cloud Architecture

Potential future deployment:

- profiling services
- cloud execution
- API endpoints
- orchestration pipelines

---

# Future Observability Vision

Future systems may track:

- profiling history
- execution metrics
- profiling lineage
- monitoring dashboards

---

# Testing Philosophy

Each execution layer should be independently testable.

---

# Current Testing Areas

Tests currently validate:

- CLI behavior
- readers
- profiling
- report generation
- chart rendering

---

# Future Testing Areas

Future tests may include:

- performance benchmarks
- distributed execution
- streaming systems
- large-scale datasets

---

# Common Architectural Mistakes

---

## Fat CLI Design

Avoid placing profiling logic inside CLI files.

---

## Tight Renderer Coupling

Renderers should remain isolated.

---

## Mixed Responsibilities

Each subsystem should have one clear role.

---

## Shared Mutable State

Avoid global runtime mutation.

---

# Long-Term Architectural Vision

Aniwa is evolving toward:

```text
a universal dataset intelligence platform
```

not merely:

```text
a local profiling CLI
```

---

# Summary

Aniwa’s execution flow architecture provides:

- modular execution
- layered orchestration
- reusable profiling
- scalable rendering
- clean subsystem separation
- future extensibility

This architecture forms the operational backbone of the entire platform.

---

# Related Documentation

Continue with:

- architecture/profiler-system.md
- architecture/reporting-system.md
- architecture/config-system.md
- architecture/dataflow.md
- api/profiler.md