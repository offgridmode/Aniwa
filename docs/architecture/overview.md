# Architecture Overview

This document provides a high-level overview of Aniwa's architecture, system organization, design philosophy, and internal execution model.

Aniwa is designed as a:

```text
modular dataset profiling and intelligence platform
```

focused on:

- scalability
- maintainability
- extensibility
- developer experience

---

# Purpose of the Architecture

Aniwa's architecture is intentionally designed to support:

- multiple dataset formats
- multiple report systems
- intelligent profiling
- future scalability
- future integrations
- long-term ecosystem growth

---

# Architectural Philosophy

Aniwa is built around several architectural principles:

| Principle | Description |
|---|---|
| modular | systems are isolated and composable |
| universal | supports many data systems |
| developer-first | optimized for CLI and automation |
| extensible | future-ready design |
| intelligent | designed for advanced profiling |
| scalable | prepared for large future systems |

---

# High-Level System Overview

At a high level, Aniwa follows this execution flow:

```text
dataset
→ reader
→ profiler
→ profile models
→ reports
→ output
```

---

# Core Architectural Layers

Aniwa is organized into several major layers:

```text
CLI Layer
↓
Configuration Layer
↓
Reader Layer
↓
Profiling Engine
↓
Data Models
↓
Reporting Layer
↓
Output Systems
```

---

# Current Project Structure

```text
Aniwa/
├── aniwa/
│   ├── cli.py
│   ├── config/
│   ├── core/
│   ├── io/
│   ├── models/
│   ├── reports/
│   ├── templates/
│   └── utils/
│
├── tests/
├── docs/
├── examples/
├── assets/
├── README.md
├── CONTRIBUTING.md
├── requirements.txt
└── pyproject.toml
```

---

# Core System Responsibilities

Each major subsystem has a specific responsibility.

---

# CLI Layer

Location:

```text
aniwa/cli.py
```

Responsibilities:

- command-line interface
- argument parsing
- orchestration
- configuration loading
- report dispatching

---

# Configuration Layer

Location:

```text
aniwa/config/
```

Responsibilities:

- configuration loading
- YAML/TOML/JSON parsing
- flattening configuration structures
- validation support

---

# Reader Layer

Location:

```text
aniwa/io/
```

Responsibilities:

- dataset ingestion
- format detection
- loading datasets into Polars DataFrames

---

# Supported Dataset Types

Current readers support:

| Format |
|---|
| CSV |
| JSON |
| Excel |
| Parquet |

---

# Profiling Engine

Location:

```text
aniwa/core/
```

Responsibilities:

- schema analysis
- statistical profiling
- quality analysis
- insight generation

---

# Models Layer

Location:

```text
aniwa/models/
```

Responsibilities:

- structured profiling objects
- serialization
- report compatibility
- validation

---

# Reporting Layer

Location:

```text
aniwa/reports/
```

Responsibilities:

- rendering outputs
- formatting reports
- export systems

---

# Current Report Types

Aniwa currently supports:

| Report |
|---|
| console |
| JSON |
| HTML |
| Markdown |
| Excel |
| PDF |

---

# Templates Layer

Location:

```text
aniwa/templates/
```

Responsibilities:

- HTML layouts
- PDF styling
- visual themes
- reusable presentation systems

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

# Utilities Layer

Location:

```text
aniwa/utils/
```

Responsibilities:

- helper functions
- reusable utilities
- shared logic

---

# Testing Layer

Location:

```text
tests/
```

Responsibilities:

- regression prevention
- validation
- architecture stability
- feature verification

---

# Architectural Flow

The complete execution flow:

```text
CLI
↓
load config
↓
read dataset
↓
profile dataset
↓
build models
↓
render reports
↓
write output
```

---

# Detailed Runtime Flow

---

# Step 1 — CLI Entry

Execution begins at:

```python
aniwa.cli:app
```

using Typer.

---

# Step 2 — Configuration Resolution

Aniwa resolves configuration using priority order:

```text
CLI arguments
→ config file
→ defaults
```

---

# Step 3 — Dataset Loading

The reader system:

- detects format
- validates support
- loads into Polars

---

# Step 4 — Profiling Execution

The profiler:

- analyzes schema
- computes statistics
- generates insights
- calculates quality metrics

---

# Step 5 — Profile Construction

Profiling results are converted into:

```text
structured profile models
```

---

# Step 6 — Report Rendering

Selected report renderer generates:

- console output
- JSON
- HTML
- Markdown
- Excel
- PDF

---

# Step 7 — Output Generation

Reports are either:

- printed
- exported
- saved to disk

---

# Why This Architecture Matters

This architecture enables:

- feature isolation
- easy testing
- future scalability
- independent subsystem evolution

---

# Modular Architecture Philosophy

Aniwa intentionally avoids:

```text
monolithic architecture
```

instead favoring:

```text
modular subsystem architecture
```

---

# Why Modularity Matters

Modularity improves:

- contributor onboarding
- maintainability
- extensibility
- scalability

---

# Current Architectural Strengths

Current strengths include:

| Strength | Benefit |
|---|---|
| clear separation | easier development |
| typed models | safer outputs |
| modular reports | extensible exports |
| template system | customizable visuals |
| isolated readers | easier new connectors |

---

# Configuration Architecture

Aniwa now supports:

- YAML
- TOML
- JSON

configuration systems.

---

# Configuration Discovery Flow

Automatic discovery order:

```text
aniwa.yaml
aniwa.yml
aniwa.toml
aniwa.json
```

---

# Configuration Philosophy

Configuration systems improve:

- reproducibility
- automation
- team workflows
- CI/CD integration

---

# Report Architecture

Reports are designed as:

```text
independent rendering systems
```

---

# Why Report Isolation Matters

This allows:

- new formats
- reusable renderers
- independent styling systems

---

# Template Architecture

Templates are intentionally separated from renderers.

---

# Why Separate Templates Matter

Separating templates improves:

- maintainability
- visual customization
- future theming systems

---

# Current Data Engine

Aniwa currently uses:

```text
Polars
```

as its primary dataframe engine.

---

# Why Polars Was Chosen

Polars provides:

- speed
- memory efficiency
- modern architecture
- excellent Python integration

---

# Future Scalability

The architecture is designed to eventually support:

- distributed profiling
- cloud systems
- plugin ecosystems
- databases
- observability systems

---

# Future Architectural Expansion

Future systems may include:

| Future System |
|---|
| plugin engine |
| distributed workers |
| metadata storage |
| governance systems |
| lineage systems |
| AI engines |

---

# Plugin Architecture Vision

Future plugins may extend:

- readers
- reports
- profiling systems
- intelligence systems

---

# Long-Term Architectural Goal

Aniwa aims to evolve into:

```text
a universal data intelligence platform
```

not merely:

```text
a profiling CLI
```

---

# Internal Dependency Philosophy

Subsystems should remain:

- loosely coupled
- independently testable
- replaceable

---

# Why Loose Coupling Matters

Loose coupling improves:

- scalability
- maintainability
- contributor experience

---

# Architectural Boundaries

Each subsystem should expose:

```text
clear interfaces
```

instead of leaking internal implementation details.

---

# Future Distributed Architecture

Future architecture may evolve toward:

```text
distributed profiling systems
```

for very large datasets.

---

# Future Cloud Architecture

Potential future platform:

```text
Aniwa Cloud
```

may introduce:

- APIs
- dashboards
- historical profiling
- governance systems

---

# Current Architectural Constraints

Current limitations include:

- local execution only
- file-based profiling only
- no persistent storage
- no distributed systems

---

# Why These Constraints Exist

Aniwa is currently focused on:

```text
building strong foundations first
```

before scaling into larger infrastructure systems.

---

# Architecture Stability Philosophy

Core architecture should evolve:

```text
carefully
```

because architectural instability causes:

- maintenance burden
- contributor confusion
- scaling problems

---

# Testing Philosophy

Architecture should always be protected by:

- unit tests
- integration tests
- regression tests

---

# Documentation Philosophy

Architecture documentation is treated as:

```text
part of the product
```

not an afterthought.

---

# Why Documentation Matters

Good documentation improves:

- contributor onboarding
- maintainability
- ecosystem growth

---

# Recommended Reading Order

To understand the architecture deeply, continue with:

1. execution-flow.md
2. profiler-system.md
3. reporting-system.md
4. models.md
5. config-system.md

---

# Final Architectural Philosophy

Aniwa is designed around one central belief:

```text
understanding data should be fast, intelligent, beautiful, and scalable
```

The architecture exists to support that vision for years to come.