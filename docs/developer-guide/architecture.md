# Architecture

This document explains the architecture of Aniwa, including:

- system structure
- execution flow
- core modules
- profiling pipeline
- reporting systems
- scalability strategy
- future architectural direction

Aniwa is designed as:

```text
modular universal data profiling infrastructure
```

not merely:

```text
a CLI utility
```

---

# Purpose of the Architecture

The architecture exists to ensure:

- scalability
- maintainability
- extensibility
- performance
- contributor friendliness

---

# Architectural Philosophy

Aniwa architecture is built around several principles:

| Principle |
|---|
| modular |
| scalable |
| developer-first |
| extensible |
| automation-friendly |
| maintainable |

---

# Core Philosophy

Aniwa is designed around:

```text
separation of concerns
```

This means each system should own:

```text
one primary responsibility
```

---

# High-Level Architecture

Aniwa currently consists of several major layers:

```text
CLI
→ Configuration
→ Readers
→ Profiling Engine
→ Models
→ Reports
→ Templates
```

---

# High-Level Execution Flow

The current execution pipeline:

```text
User Command
→ CLI Parsing
→ Config Resolution
→ Dataset Reading
→ Profiling Engine
→ Insight Generation
→ Report Rendering
→ Output Export
```

---

# Current Project Structure

```text
Aniwa/
│
├── aniwa/
│   ├── cli.py
│   │
│   ├── config/
│   │
│   ├── core/
│   │
│   ├── io/
│   │
│   ├── models/
│   │
│   ├── reports/
│   │
│   ├── templates/
│   │
│   └── utils/
│
├── docs/
├── tests/
├── examples/
│
├── README.md
├── pyproject.toml
└── requirements.txt
```

---

# Why the Structure Matters

This structure enables:

- isolated systems
- easier testing
- contributor scalability
- architectural clarity

---

# CLI Layer

Primary file:

```text
aniwa/cli.py
```

---

# Responsibilities of the CLI

The CLI layer handles:

- argument parsing
- command orchestration
- config loading
- report routing
- execution flow

---

# Why the CLI Exists

The CLI acts as:

```text
the orchestration layer
```

for the entire system.

---

# Current CLI Responsibilities

The CLI currently controls:

| Responsibility |
|---|
| input parsing |
| config resolution |
| report selection |
| profiling mode |
| section filtering |
| metadata generation |

---

# Configuration Layer

Primary area:

```text
aniwa/config/
```

---

# Responsibilities of the Config System

The configuration system handles:

- YAML configs
- TOML configs
- JSON configs
- config flattening
- validation
- precedence resolution

---

# Config Priority Order

Aniwa follows:

```text
CLI > config file > defaults
```

---

# Why This Matters

This provides:

- reproducibility
- flexibility
- automation compatibility

---

# Automatic Config Discovery

Aniwa automatically searches for:

```text
aniwa.yaml
aniwa.yml
aniwa.toml
aniwa.json
```

---

# Reader Layer

Primary location:

```text
aniwa/io/
```

---

# Responsibilities of Readers

Readers handle:

- dataset ingestion
- format detection
- conversion to Polars DataFrames

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

# Why Readers Are Isolated

Reader isolation enables:

- easier extensibility
- cleaner debugging
- modular format support

---

# Reader Execution Flow

Typical reader flow:

```text
path
→ extension detection
→ parser selection
→ dataframe conversion
```

---

# Why Polars Was Chosen

Aniwa uses:

```text
Polars
```

because it provides:

- high performance
- vectorized computation
- modern dataframe architecture

---

# Core Profiling Engine

Primary location:

```text
aniwa/core/
```

---

# Responsibilities of the Profiling Engine

The profiling engine handles:

- schema analysis
- quality analysis
- statistics
- insights
- metadata generation

---

# Why the Profiling Engine Matters

The profiling engine is:

```text
the intelligence core of Aniwa
```

---

# Profiling Pipeline

Current profiling flow:

```text
dataset
→ schema analysis
→ quality analysis
→ statistics
→ insights
→ profile object
```

---

# Profiling Modes

Current modes:

| Mode |
|---|
| fast |
| deep |

---

# Fast Mode

Fast mode prioritizes:

```text
lightweight rapid analysis
```

---

# Deep Mode

Deep mode prioritizes:

```text
full dataset understanding
```

---

# Why Multiple Modes Matter

Different workflows require different tradeoffs between:

- speed
- depth
- resource usage

---

# Insight System

The insight layer detects:

- suspicious patterns
- quality issues
- sparse columns
- possible PII
- duplicate rows

---

# Why Insights Matter

Users want:

```text
meaningful understanding
```

not merely:

```text
raw statistics
```

---

# Models Layer

Primary location:

```text
aniwa/models/
```

---

# Responsibilities of Models

Models provide:

- structured data representation
- type-safe architecture
- report consistency

---

# Why Models Matter

Models create:

- predictable data structures
- cleaner serialization
- safer extensibility

---

# Current Model Categories

Current models include:

| Model Type |
|---|
| metadata |
| schema |
| statistics |
| insights |
| reports |

---

# Reporting Layer

Primary location:

```text
aniwa/reports/
```

---

# Responsibilities of Reports

The reporting system handles:

- rendering
- serialization
- export generation

---

# Current Report Formats

Supported formats:

| Format |
|---|
| console |
| JSON |
| HTML |
| Markdown |
| Excel |
| PDF |

---

# Why Reports Are Modular

Modular reports enable:

- independent extensions
- cleaner maintenance
- easier customization

---

# Report Rendering Flow

Current rendering flow:

```text
profile object
→ formatter
→ renderer
→ output
```

---

# Console Reports

Console reports prioritize:

- readability
- developer UX
- terminal clarity

---

# HTML Reports

HTML reports prioritize:

- shareability
- visualization
- presentation

---

# JSON Reports

JSON reports prioritize:

- machine-readability
- automation
- integrations

---

# Markdown Reports

Markdown reports prioritize:

- documentation workflows
- GitHub compatibility
- portability

---

# Template System

Primary location:

```text
aniwa/templates/
```

---

# Responsibilities of Templates

Templates control:

- layout
- styling
- presentation structure

---

# Why Templates Matter

Templates separate:

```text
presentation from logic
```

---

# Template Philosophy

Templates should remain:

- reusable
- isolated
- customizable

---

# Utility Layer

Primary location:

```text
aniwa/utils/
```

---

# Responsibilities of Utilities

Utilities contain:

- helper functions
- reusable shared logic
- formatting systems

---

# Why Utilities Exist

Utilities reduce:

- duplication
- tightly coupled code
- architectural clutter

---

# Metadata System

Aniwa automatically generates metadata including:

| Metadata |
|---|
| runtime |
| dataset size |
| file type |
| version |
| execution command |

---

# Why Metadata Matters

Metadata improves:

- reproducibility
- debugging
- governance
- auditing

---

# Section-Based Architecture

Aniwa supports selective report sections.

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

# Why Section Modularity Matters

This enables:

- smaller reports
- customizable workflows
- automation flexibility

---

# Error Handling Philosophy

Aniwa prioritizes:

```text
clear actionable errors
```

---

# Good Error Example

Example:

```text
Invalid report format: yaml
```

---

# Bad Error Example

Avoid:

```text
Unhandled exception occurred
```

---

# Scalability Philosophy

Aniwa is designed with:

```text
future scalability in mind
```

---

# Why Scalability Matters

The architecture should eventually support:

- massive datasets
- distributed systems
- cloud infrastructure
- enterprise workflows

---

# Current Scalability Strategies

Current scalability considerations:

| Strategy |
|---|
| modular systems |
| isolated readers |
| layered architecture |
| reusable models |

---

# Future Scalability Directions

Potential future systems:

| Future System |
|---|
| chunked processing |
| streaming profiling |
| distributed execution |
| async pipelines |

---

# Future Connectivity Vision

Aniwa aims to support:

| System |
|---|
| PostgreSQL |
| MySQL |
| DuckDB |
| BigQuery |
| Snowflake |

---

# Why Universal Connectivity Matters

Modern data ecosystems are:

```text
distributed and fragmented
```

---

# Future Plugin Architecture

Potential future plugin systems:

| Plugin |
|---|
| readers |
| reports |
| governance |
| AI modules |

---

# Why Plugins Matter

Plugins allow:

```text
ecosystem scalability through community extension
```

---

# Future AI Architecture

Future AI systems may support:

- semantic understanding
- anomaly explanation
- dataset summarization
- intelligent recommendations

---

# Future Governance Systems

Potential governance layers:

- PII detection
- trust scoring
- lineage tracking
- compliance validation

---

# Cloud Architecture Vision

Future cloud systems may include:

```text
web UI
→ APIs
→ profiling services
→ metadata storage
```

---

# Distributed Systems Vision

Long-term systems may evolve toward:

```text
distributed profiling infrastructure
```

---

# Why Distributed Systems Matter

Distributed systems enable:

- massive scale
- enterprise workloads
- parallel computation

---

# Long-Term Architecture Philosophy

Aniwa architecture is designed with:

```text
10–20+ year evolution in mind
```

---

# Why Long-Term Thinking Matters

Strong foundations reduce:

- rewrites
- technical debt
- architectural fragmentation

---

# Architectural Anti-Patterns

Avoid:

| Anti-Pattern |
|---|
| tightly coupled systems |
| duplicated logic |
| monolithic reports |
| hidden side effects |
| unclear execution flow |

---

# Contributor Architecture Philosophy

Contributors should prioritize:

- modularity
- maintainability
- readability
- scalability

---

# Why Contributor Alignment Matters

Consistent architecture improves:

- ecosystem health
- contributor onboarding
- long-term maintainability

---

# Strategic Importance

Aniwa architecture exists to ensure that:

```text
the platform can evolve from a profiling CLI into universal data intelligence infrastructure
```

---

# Final Philosophy

Aniwa architecture is designed to remain:

```text
modular, scalable, intelligent, extensible, and sustainable over decades of ecosystem growth
```

---

# Related Documentation

Continue with:

- developer-guide/profiling-engine.md
- developer-guide/reporting-system.md
- roadmap.md
- philosophy.md