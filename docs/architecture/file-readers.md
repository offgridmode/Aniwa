# File Readers Architecture

The file readers system is responsible for ingesting datasets into Aniwa.

It is the gateway between:

```text
external data
```

and:

```text
Aniwa's internal profiling engine
```

Without the readers system, profiling cannot begin.

This document explains:

- reader architecture
- ingestion flow
- file detection
- format handling
- extensibility
- scalability
- future connector systems

---

# Purpose of the Reader System

The reader system exists to:

- load datasets
- normalize inputs
- support multiple formats
- abstract ingestion complexity
- provide a unified DataFrame interface
- prepare data for profiling

---

# Core Reader Philosophy

Aniwa follows a:

```text
unified ingestion architecture
```

This means:

```text
many formats
→ one internal structure
```

---

# Why Unified Ingestion Matters

Without normalization:

- profiling becomes fragmented
- logic becomes duplicated
- maintenance becomes difficult

Unified ingestion enables:

- cleaner profiling systems
- reusable intelligence
- extensibility

---

# High-Level Reader Flow

```text
dataset path
→ file detection
→ correct loader
→ DataFrame normalization
→ profiling engine
```

---

# Reader System Location

```text
aniwa/io/readers.py
```

---

# Current Reader Responsibilities

The readers system currently handles:

- format detection
- dataset loading
- parser dispatching
- normalization
- ingestion validation

---

# Current Supported Formats

Aniwa currently supports:

| Format | Extension |
|---|---|
| CSV | `.csv` |
| Excel | `.xlsx`, `.xls` |
| JSON | `.json` |
| Parquet | `.parquet` |

---

# Why Multi-Format Support Matters

Modern data workflows use many formats.

Supporting multiple formats improves:

- accessibility
- interoperability
- adoption
- enterprise compatibility

---

# Current Reader Architecture

The current architecture follows:

```text
extension detection
→ format-specific reader
→ shared DataFrame output
```

---

# Internal Reader Flow

```python
read_dataset(path)
```

↓

```python
detect extension
```

↓

```python
dispatch to correct loader
```

↓

```python
return Polars DataFrame
```

---

# Why Dispatch-Based Architecture Matters

Dispatch systems improve:

- modularity
- maintainability
- extensibility

---

# Central Reader Entry Point

Primary ingestion function:

```python
read_dataset()
```

---

# Why Central Entry Points Matter

Benefits:

- consistent behavior
- centralized validation
- easier extensibility
- cleaner architecture

---

# Internal Runtime Flow

```text
CLI
→ read_dataset()
→ DataFrame
→ profiler
```

---

# Why Readers Return DataFrames

Aniwa standardizes ingestion into:

```python
Polars DataFrame
```

---

# Why Polars Was Chosen

Polars provides:

- high performance
- memory efficiency
- vectorized operations
- scalability
- modern architecture

---

# Architectural Importance of Polars

Polars acts as:

```text
Aniwa's internal data execution engine
```

---

# Why Standardized DataFrames Matter

This enables:

```text
same profiler
→ all formats
```

without duplicating profiling logic.

---

# CSV Reader System

CSV ingestion uses:

```python
pl.read_csv()
```

---

# CSV Reader Responsibilities

The CSV system handles:

- delimiter parsing
- schema inference
- tabular normalization

---

# Why CSV Support Matters

CSV remains one of the most common data formats globally.

---

# Future CSV Enhancements

Potential future features:

- delimiter auto-detection
- encoding detection
- malformed row recovery
- chunked loading

---

# Excel Reader System

Excel ingestion uses:

```python
pl.read_excel()
```

or compatible loaders.

---

# Excel Reader Responsibilities

Excel support handles:

- spreadsheet parsing
- workbook loading
- tabular extraction

---

# Why Excel Support Matters

Excel is dominant in:

- business analytics
- finance
- operations
- enterprise workflows

---

# Future Excel Enhancements

Future capabilities may include:

- multi-sheet support
- sheet selection
- workbook metadata
- formulas analysis

---

# JSON Reader System

JSON ingestion uses:

```python
pl.read_json()
```

---

# JSON Reader Responsibilities

The JSON reader handles:

- structured documents
- semi-structured records
- schema inference

---

# Why JSON Support Matters

JSON dominates:

- APIs
- web systems
- cloud pipelines
- ML workflows

---

# Future JSON Enhancements

Future support may include:

- nested normalization
- flattening
- schema extraction
- streaming JSON

---

# Parquet Reader System

Parquet ingestion uses:

```python
pl.read_parquet()
```

---

# Why Parquet Matters

Parquet is critical for:

- big data systems
- analytics engineering
- lakehouses
- modern data platforms

---

# Benefits of Parquet

Parquet provides:

- compression
- columnar storage
- efficient scanning
- analytical performance

---

# Future Parquet Enhancements

Potential future features:

- partition awareness
- lazy scanning
- cloud parquet loading

---

# Format Detection System

Aniwa detects formats using:

```python
Path(path).suffix
```

---

# Detection Flow

```text
dataset path
→ extension extraction
→ dispatch map
→ reader selection
```

---

# Why Extension-Based Detection Works

Benefits:

- simplicity
- predictability
- maintainability

---

# Current Reader Dispatch Model

Conceptually:

```python
{
    ".csv": read_csv,
    ".json": read_json,
    ".xlsx": read_excel,
    ".parquet": read_parquet,
}
```

---

# Why Dispatch Maps Matter

Dispatch maps improve:

- extensibility
- readability
- scalability

---

# Unsupported Format Handling

Unsupported formats raise clear errors.

Example:

```text
Unsupported dataset type '.xml'
```

---

# Why Explicit Errors Matter

Benefits:

- easier debugging
- predictable behavior
- cleaner UX

---

# Reader Validation Responsibilities

Readers validate:

- file existence
- supported extensions
- parser compatibility

---

# Why Validation Matters

Validation prevents:

- runtime crashes
- invalid ingestion states
- corrupted execution flows

---

# Reader Error Philosophy

Reader errors should be:

- human-readable
- actionable
- non-cryptic

---

# Example Reader Errors

Good example:

```text
Unsupported dataset type '.xml'
```

Bad example:

```text
ValueError: unexpected parser object
```

---

# Reader Isolation Philosophy

Readers should ONLY:

- ingest data
- normalize data
- return DataFrames

Readers should NOT:

- compute statistics
- generate insights
- render reports

---

# Why Isolation Matters

This prevents:

- tight coupling
- duplicated logic
- architectural confusion

---

# Reader Layer in System Architecture

```text
CLI
 ↓
Configuration
 ↓
Readers
 ↓
Profiler
 ↓
Reports
```

---

# Reader Scalability Vision

The reader layer is intentionally designed for future expansion.

---

# Future Database Readers

Potential future connectors:

| Connector |
|---|
| PostgreSQL |
| MySQL |
| SQLite |
| DuckDB |
| Snowflake |
| BigQuery |

---

# Why Database Readers Matter

Modern datasets increasingly live in:

- warehouses
- databases
- lakehouses

not local files.

---

# Future Cloud Storage Readers

Potential future integrations:

| Storage |
|---|
| S3 |
| Azure Blob |
| Google Cloud Storage |
| MinIO |

---

# Future Streaming Readers

Future ingestion may support:

- streaming datasets
- chunked ingestion
- distributed loading

---

# Why Streaming Matters

Large datasets may exceed memory limits.

Streaming enables:

- scalability
- enterprise profiling
- massive dataset support

---

# Future Lazy Loading Vision

Potential future architecture:

```python
pl.scan_parquet()
```

instead of:

```python
pl.read_parquet()
```

---

# Benefits of Lazy Execution

Lazy execution enables:

- query optimization
- lower memory usage
- faster execution
- distributed scalability

---

# Future Schema Systems

Potential future schema features:

- schema snapshots
- schema evolution
- schema drift detection

---

# Future Dataset Registry Vision

Long-term ingestion systems may support:

- dataset registries
- metadata catalogs
- lineage tracking

---

# Reader Plugin Architecture

Future versions may allow plugins to register readers.

Example:

```python
register_reader(".avro", read_avro)
```

---

# Why Plugin Readers Matter

This enables:

- community extensions
- ecosystem growth
- enterprise customization

---

# Future API Readers

Potential future ingestion:

- REST APIs
- GraphQL endpoints
- Kafka streams
- webhooks

---

# Reader Performance Considerations

Current bottlenecks may include:

- Excel parsing
- large CSV files
- nested JSON structures

---

# Future Optimization Areas

Potential optimizations:

- parallel ingestion
- chunked loading
- lazy execution
- memory-aware scanning

---

# Reader Security Considerations

Readers must safely handle:

- malformed files
- corrupted datasets
- unsafe encodings

---

# Why Reader Security Matters

Ingestion systems are often attack surfaces.

---

# Testing Philosophy

Reader systems require strong testing.

---

# Current Reader Tests

Tests should validate:

- supported formats
- unsupported formats
- malformed files
- schema inference
- ingestion consistency

---

# Future Reader Tests

Future testing areas:

- large datasets
- streaming systems
- cloud readers
- distributed ingestion

---

# Common Reader Design Mistakes

---

## Embedding Profiling Logic

Readers should never compute analytics.

---

## Format-Specific Profiling

Profiling should remain format-agnostic.

---

## Tight Coupling

Readers should remain isolated from reports.

---

## Inconsistent Outputs

All readers should return:

```python
Polars DataFrame
```

---

# Reader Design Principles

---

## Standardize Internally

Normalize all formats into shared structures.

---

## Keep Readers Lightweight

Readers should only ingest and normalize.

---

## Prioritize Extensibility

Reader systems should anticipate future formats.

---

## Prefer Predictability

Avoid overly magical detection systems.

---

# Long-Term Reader Vision

Aniwa’s readers are evolving toward:

```text
a universal data ingestion platform
```

not merely:

```text
a local file parser
```

---

# Future Enterprise Vision

Long-term enterprise capabilities may include:

- warehouse connectivity
- metadata catalogs
- lineage ingestion
- governance integrations
- distributed execution

---

# Summary

Aniwa’s file readers architecture provides:

- unified ingestion
- multi-format support
- standardized DataFrame outputs
- extensibility
- scalable design
- future cloud/database readiness

The readers system forms the foundation of all profiling operations.

---

# Related Documentation

Continue with:

- architecture/execution-flow.md
- architecture/profiler-system.md
- architecture/dataflow.md
- api/readers.md
- api/profiler.md