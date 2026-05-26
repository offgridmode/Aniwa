# Data Models Architecture

This document explains the internal data modeling system used throughout Aniwa.

Data models are one of the most important architectural foundations of the project because they define:

- profiling structures
- report structures
- metadata systems
- internal interfaces
- serialization behavior
- future API compatibility

---

# Purpose of the Models Layer

The models layer provides:

```text
structured representations of profiling results
```

instead of relying on:

- raw dictionaries
- loosely typed objects
- inconsistent structures

---

# Why Models Matter

Without models:

- systems become fragile
- reports become inconsistent
- validation becomes difficult
- serialization becomes unreliable

---

# Benefits of the Models Layer

The models system provides:

| Benefit | Description |
|---|---|
| consistency | predictable data structures |
| validation | safer profiling outputs |
| maintainability | easier development |
| serialization | JSON/export compatibility |
| extensibility | future-proof architecture |
| typing | safer internal systems |

---

# Models Architecture Overview

Aniwa primarily uses:

```text
Pydantic models
```

for structured profiling results.

---

# Current Model Categories

The models layer currently includes:

```text
aniwa/models/
```

---

# Current Model Structure

```text
aniwa/models/
├── enums.py
├── profile.py
```

---

# Architectural Philosophy

Aniwa models should be:

- explicit
- strongly typed
- serializable
- modular
- extensible

---

# High-Level Flow

```text
dataset
→ profiler
→ model objects
→ reports
→ exports
```

---

# Why Structured Models Are Critical

Structured models enable:

- report generation
- API compatibility
- testing
- metadata systems
- future distributed systems

---

# Current Core Model

The primary model is:

```text
DatasetProfile
```

This acts as the:

```text
central profiling container
```

---

# Conceptual DatasetProfile Structure

```python
DatasetProfile
├── summary
├── columns
├── quality
├── insights
├── metadata
```

---

# Why DatasetProfile Exists

It centralizes all profiling outputs into:

```text
one unified object
```

which becomes the source of truth for:

- reports
- exports
- renderers
- future APIs

---

# Profile Lifecycle

The profile lifecycle looks like this:

```text
reader
→ DataFrame
→ profiler
→ DatasetProfile
→ reports
```

---

# Summary Models

Summary models contain:

- row counts
- column counts
- dataset dimensions

---

# Example Summary Model

```python
class Summary(BaseModel):
    rows: int
    columns: int
```

---

# Why Summary Models Matter

Summary models provide:

- lightweight dataset overviews
- report headers
- metadata inputs

---

# Column Models

Column models represent:

```text
individual dataset columns
```

---

# Typical Column Information

Column models may contain:

| Field | Purpose |
|---|---|
| name | column name |
| dtype | inferred type |
| null_count | missing values |
| null_percent | null percentage |
| unique_count | distinct values |

---

# Column Model Architecture

Conceptually:

```python
ColumnProfile
├── structural info
├── quality metrics
├── statistics
├── semantic metadata
```

---

# Why Column Models Matter

Column-level modeling enables:

- granular profiling
- extensible statistics
- intelligent insights

---

# Numeric Statistics Models

Numeric models contain:

- min
- max
- mean
- median
- standard deviation

---

# Example Numeric Stats

```python
class NumericStats(BaseModel):
    min: float
    max: float
    mean: float
    median: float
    std: float
```

---

# Why Separate Statistics Models Matter

Statistics evolve independently from columns.

This improves:

- modularity
- extensibility
- future advanced analytics

---

# Quality Models

Quality models represent:

- duplicates
- nulls
- anomalies
- validation findings

---

# Example Quality Structure

```python
QualityProfile
├── duplicate_rows
├── duplicate_percent
├── null_statistics
```

---

# Why Quality Models Matter

Quality models separate:

```text
dataset trust metrics
```

from:

```text
structural profiling
```

---

# Insight Models

Insights represent:

```text
intelligent observations
```

generated during profiling.

---

# Example Insight Structure

```python
Insight
├── level
├── message
```

---

# Why Insights Are Important

Insights transform Aniwa from:

```text
basic statistics
```

into:

```text
intelligent profiling
```

---

# Insight Levels

Typical levels include:

| Level |
|---|
| info |
| warning |
| critical |

---

# Metadata Models

Metadata models describe:

- runtime environment
- profiling execution
- system metadata

---

# Example Metadata Fields

| Field |
|---|
| generated_at |
| aniwa_version |
| python_version |
| operating_system |
| dataset_path |
| profiling_mode |

---

# Why Metadata Matters

Metadata enables:

- reproducibility
- debugging
- governance
- auditing

---

# Metadata as Provenance

Metadata effectively acts as:

```text
profiling provenance
```

---

# ReportSection Enum

Aniwa uses enums for:

```text
safe report configuration
```

---

# Example Enum

```python
class ReportSection(str, Enum):
    summary = "summary"
    schema = "schema"
    statistics = "statistics"
```

---

# Why Enums Matter

Enums prevent:

- invalid report options
- inconsistent section names
- configuration bugs

---

# Model Validation

Pydantic provides automatic validation.

---

# Validation Benefits

Validation ensures:

- correct types
- predictable structures
- safer report rendering

---

# Example Validation

```python
rows: int
```

prevents:

```python
rows = "five"
```

---

# Serialization Architecture

Models are designed for:

```text
easy serialization
```

---

# Current Serialization Targets

Current export targets:

| Format |
|---|
| JSON |
| HTML |
| Markdown |
| PDF |
| Excel |

---

# Why Serialization Matters

Serialization enables:

- exports
- APIs
- storage
- interoperability

---

# Future API Compatibility

Structured models make future APIs easier.

Potential future systems:

- REST APIs
- GraphQL
- SDKs

---

# Model Stability Philosophy

Models should evolve:

```text
carefully
```

because reports and integrations depend on them.

---

# Breaking Changes Risk

Changing models carelessly can break:

- reports
- tests
- integrations
- plugins

---

# Recommended Model Evolution Strategy

Prefer:

- additive changes
- optional fields
- backward compatibility

Avoid:

- destructive renames
- breaking structures

---

# Future Model Expansion

Future models may include:

- correlations
- drift analysis
- semantic metadata
- lineage structures
- governance metadata

---

# Future Semantic Models

Potential future semantic systems:

```python
SemanticColumnProfile
├── pii_probability
├── semantic_type
├── confidence_score
```

---

# Future Governance Models

Potential governance structures:

```python
GovernanceProfile
├── trust_score
├── compliance_status
├── lineage_metadata
```

---

# Future AI Models

Potential AI structures:

```python
AIInsight
├── explanation
├── recommendation
├── severity
```

---

# Why Modular Models Matter

Large systems become easier to maintain when models are separated into:

- focused components
- reusable structures
- isolated domains

---

# Current Architectural Limitation

Current models are relatively compact.

As Aniwa grows, models may eventually need subdivision into:

```text
models/
├── profiling/
├── quality/
├── metadata/
├── governance/
├── intelligence/
```

---

# Recommended Long-Term Architecture

Long-term systems should organize models by domain.

---

# Future Internal Contracts

Models may evolve into:

```text
internal contracts
```

between subsystems.

---

# Example Future System

```text
profiling engine
→ DatasetProfile
→ intelligence engine
→ governance engine
```

---

# Why Typed Contracts Matter

Typed contracts improve:

- reliability
- scalability
- maintainability

---

# Future Distributed Systems

Future distributed architectures may rely heavily on:

- serialized models
- event payloads
- worker communication

---

# Future Event-Driven Architecture

Potential future systems:

```text
worker
→ serialized profile
→ event bus
→ reporting service
```

---

# Testing Models

Models should always be tested.

---

# Recommended Model Tests

Test:

- validation
- serialization
- defaults
- edge cases
- optional fields

---

# Example Tests

```python
assert profile.summary.rows == 100
```

---

# Future Schema Versioning

Long-term systems may require:

```text
model versioning
```

---

# Why Schema Versioning Matters

Versioning helps support:

- backward compatibility
- migrations
- long-lived APIs

---

# Potential Future Standards

Future integrations may support:

- OpenMetadata
- JSON Schema
- OpenAPI
- Avro

---

# Long-Term Philosophy

Models should become:

```text
the canonical language of Aniwa
```

---

# Final Architectural Principle

The models layer is not just:

```text
data containers
```

It is:

```text
the structural foundation of the entire Aniwa ecosystem
```

---

# Related Documentation

Continue with:

- api/models.md
- architecture/profiler-system.md
- architecture/reporting-system.md
- architecture/execution-flow.md