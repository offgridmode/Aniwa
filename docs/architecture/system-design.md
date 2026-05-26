# System Design

This document explains the complete system design of Aniwa, including architectural layers, execution flow, subsystem interactions, design principles, scalability direction, and future platform evolution.

Aniwa is designed as a:

```text
modular universal data profiling and intelligence system
```

focused on:

- extensibility
- scalability
- maintainability
- performance
- developer experience

---

# Purpose of This Document

This document explains:

- system architecture
- subsystem relationships
- execution lifecycle
- data flow
- infrastructure design
- scalability planning
- future distributed architecture

---

# High-Level Vision

Aniwa is evolving toward:

```text
a universal data intelligence platform
```

not merely:

```text
a CLI profiling utility
```

---

# System Design Philosophy

Aniwa’s design follows several principles:

| Principle | Purpose |
|---|---|
| modularity | isolated systems |
| scalability | future growth |
| extensibility | plugin-ready architecture |
| simplicity | maintainable codebase |
| performance | efficient execution |
| interoperability | integration-ready systems |

---

# High-Level System Overview

At a high level:

```text
dataset
→ reader
→ profiling engine
→ profile models
→ report system
→ output
```

---

# Core Architectural Layers

Aniwa is divided into several major layers.

---

# Layer 1 — Interface Layer

Responsibilities:

- CLI interaction
- user inputs
- argument parsing
- execution orchestration

---

# Interface Layer Location

```text
aniwa/cli.py
```

---

# Why the Interface Layer Matters

This layer acts as:

```text
the orchestration gateway
```

for the entire system.

---

# Layer 2 — Configuration Layer

Responsibilities:

- configuration discovery
- YAML/TOML/JSON loading
- config validation
- execution defaults

---

# Configuration Layer Location

```text
aniwa/config/
```

---

# Why Configuration Matters

Configuration systems improve:

- automation
- reproducibility
- CI/CD workflows
- team consistency

---

# Layer 3 — Reader Layer

Responsibilities:

- dataset ingestion
- format detection
- dataframe loading

---

# Reader Layer Location

```text
aniwa/io/
```

---

# Current Reader Support

Current formats include:

| Format |
|---|
| CSV |
| JSON |
| Excel |
| Parquet |

---

# Why Reader Isolation Matters

Separate readers improve:

- maintainability
- future integrations
- independent testing

---

# Reader System Flow

```text
dataset file
→ format detection
→ parser
→ Polars DataFrame
```

---

# Layer 4 — Profiling Engine

Responsibilities:

- schema analysis
- quality analysis
- statistics
- insights

---

# Profiling Engine Location

```text
aniwa/core/
```

---

# Profiling Engine Purpose

The profiling engine transforms:

```text
raw datasets
```

into:

```text
structured intelligence
```

---

# Current Profiling Capabilities

Current systems analyze:

| Capability |
|---|
| schema |
| nulls |
| duplicates |
| statistics |
| insights |

---

# Layer 5 — Models Layer

Responsibilities:

- structured profile objects
- serialization
- renderer compatibility

---

# Models Layer Location

```text
aniwa/models/
```

---

# Why Models Matter

Models provide:

- consistency
- type safety
- architecture stability

---

# Core Model Flow

```text
profiling results
→ typed models
→ reports
```

---

# Layer 6 — Reporting Layer

Responsibilities:

- formatting outputs
- rendering reports
- exporting files

---

# Reporting Layer Location

```text
aniwa/reports/
```

---

# Current Report Formats

Aniwa currently supports:

| Format |
|---|
| console |
| JSON |
| HTML |
| Markdown |
| Excel |
| PDF |

---

# Why Report Isolation Matters

Each report format has:

- different UX goals
- different rendering requirements

---

# Layer 7 — Templates Layer

Responsibilities:

- HTML layouts
- PDF styling
- reusable presentation systems

---

# Template Layer Location

```text
aniwa/templates/
```

---

# Current Template Types

Current templates include:

| Template |
|---|
| default |
| clean |
| compact |
| dark |
| enterprise |

---

# Why Templates Matter

Templates separate:

- presentation
- business logic

---

# Layer 8 — Utilities Layer

Responsibilities:

- shared helpers
- reusable utilities
- formatting helpers

---

# Utilities Location

```text
aniwa/utils/
```

---

# Layer 9 — Testing Layer

Responsibilities:

- regression prevention
- architecture validation
- feature verification

---

# Testing Location

```text
tests/
```

---

# End-to-End Execution Flow

Complete execution lifecycle:

```text
CLI
↓
config loading
↓
dataset reading
↓
profiling
↓
model generation
↓
report rendering
↓
output writing
```

---

# Detailed Runtime Lifecycle

---

# Step 1 — CLI Invocation

Execution begins:

```bash
aniwa customers.csv
```

---

# Step 2 — Configuration Resolution

Configuration priority:

```text
CLI arguments
→ config file
→ defaults
```

---

# Step 3 — Dataset Validation

The system validates:

- file existence
- supported format
- readable structure

---

# Step 4 — Reader Dispatch

The appropriate reader loads the dataset.

---

# Step 5 — DataFrame Creation

Data is loaded into:

```python
Polars DataFrame
```

---

# Why Polars Was Chosen

Polars provides:

- high performance
- vectorized execution
- modern dataframe architecture

---

# Step 6 — Profiling Execution

The profiling engine performs:

- summary analysis
- schema analysis
- statistics
- insights

---

# Step 7 — Profile Construction

Results become:

```python
DatasetProfile
```

---

# Step 8 — Metadata Generation

Execution metadata is attached.

---

# Step 9 — Renderer Dispatch

The appropriate renderer is selected.

---

# Step 10 — Report Generation

The renderer creates:

- terminal output
- file exports
- visual reports

---

# Step 11 — Output Writing

Reports are:

- printed
- saved
- exported

---

# Architectural Boundaries

Aniwa intentionally separates:

| Concern | Layer |
|---|---|
| orchestration | CLI |
| ingestion | readers |
| analysis | profiler |
| structure | models |
| presentation | reports |

---

# Why Separation Matters

Separation improves:

- scalability
- testing
- contributor onboarding

---

# Current Monolith Status

Aniwa currently operates as:

```text
modular monolith architecture
```

---

# Why Modular Monoliths Are Good Early

This architecture provides:

- simplicity
- low operational overhead
- strong maintainability

before distributed complexity is introduced.

---

# Future Service-Oriented Architecture

Future systems may evolve toward:

```text
service-oriented architecture
```

---

# Potential Future Services

Future services may include:

| Service |
|---|
| profiling service |
| report service |
| metadata service |
| AI service |
| governance service |

---

# Future Distributed Architecture

Potential future architecture:

```text
API gateway
→ orchestrator
→ worker nodes
→ distributed profiling
→ metadata storage
```

---

# Why Distributed Systems Matter

Distributed systems enable:

- massive datasets
- enterprise-scale execution
- parallel computation

---

# Future Storage Architecture

Potential storage systems:

| Purpose | Technology |
|---|---|
| metadata | PostgreSQL |
| analytics | DuckDB |
| caching | Redis |
| objects | S3 |

---

# Future Cloud Architecture

Potential future platform:

```text
Aniwa Cloud
```

---

# Cloud System Possibilities

Cloud features may include:

- dashboards
- profiling history
- team collaboration
- governance systems

---

# Future Streaming Architecture

Potential streaming flow:

```text
Kafka
→ stream processor
→ profiling engine
→ observability dashboard
```

---

# Future Plugin Architecture

Aniwa is intentionally being designed for future plugins.

---

# Potential Plugin Targets

Plugins may extend:

| Area |
|---|
| readers |
| reports |
| profiling |
| templates |
| governance |

---

# Future AI Architecture

Potential AI systems may include:

- semantic analysis
- natural-language summaries
- anomaly explanations
- intelligent recommendations

---

# Future Governance Architecture

Potential governance systems:

| Capability |
|---|
| lineage |
| trust scoring |
| compliance validation |
| policy systems |

---

# Configuration System Design

Aniwa supports:

- YAML
- TOML
- JSON

configuration systems.

---

# Config Discovery Flow

Automatic discovery order:

```text
aniwa.yaml
aniwa.yml
aniwa.toml
aniwa.json
```

---

# Output System Design

Aniwa supports:

- direct output paths
- output directories
- generated filenames

---

# Why Output Management Matters

This improves:

- automation
- CI/CD integration
- reproducibility

---

# Report Template Design

Templates remain isolated from:

```text
business logic
```

---

# Why Template Isolation Matters

This enables:

- easier styling
- custom themes
- enterprise branding

---

# Error Handling Philosophy

Systems should fail:

```text
gracefully and clearly
```

---

# Current Error Types

Potential errors include:

| Error |
|---|
| unsupported format |
| invalid config |
| malformed dataset |
| template errors |

---

# Validation Philosophy

Validation should occur:

- early
- clearly
- consistently

---

# Performance Philosophy

Aniwa prioritizes:

```text
fast developer feedback loops
```

---

# Current Performance Strategies

Current optimizations include:

- vectorized computation
- modular rendering
- conditional sections

---

# Future Performance Systems

Potential future optimizations:

- lazy execution
- distributed profiling
- chunked processing
- parallel statistics

---

# Security Philosophy

Current systems prioritize:

- safe parsing
- predictable execution

---

# Future Security Systems

Future systems may require:

- RBAC
- authentication
- encrypted storage
- audit logging

---

# Documentation Philosophy

Documentation is treated as:

```text
core infrastructure
```

not optional content.

---

# Why Documentation Matters

Strong documentation enables:

- contributor scalability
- architectural longevity
- ecosystem growth

---

# Long-Term Architectural Vision

Aniwa aims to evolve into:

```text
universal infrastructure for dataset intelligence
```

capable of supporting:

- local workflows
- enterprise systems
- AI pipelines
- governance ecosystems

---

# Final Philosophy

Aniwa’s system design exists to ensure that:

```text
understanding data becomes scalable, intelligent, beautiful, and universally accessible
```

---

# Related Documentation

Continue with:

- architecture/overview.md
- architecture/profiling-engine.md
- architecture/reporting-system.md
- architecture/scalability-roadmap.md