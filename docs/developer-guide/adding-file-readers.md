# Adding File Readers

This guide explains how to add new dataset readers to Aniwa.

Aniwa is designed to be:

```text
universal and extensible
```

which means adding support for new dataset formats should be:

- predictable
- modular
- scalable
- contributor-friendly

---

# Purpose of File Readers

File readers are responsible for:

- detecting supported dataset formats
- loading datasets
- converting datasets into Polars DataFrames

The reader layer acts as:

```text
Aniwa’s ingestion system
```

---

# Current Reader Architecture

Current reader systems are located in:

```text
aniwa/io/
```

---

# Current Reader Structure

Typical structure:

```text
aniwa/io/
├── readers.py
```

Future versions may evolve into:

```text
aniwa/io/
├── readers/
│   ├── csv_reader.py
│   ├── json_reader.py
│   ├── parquet_reader.py
│   ├── excel_reader.py
│   └── registry.py
```

---

# Current Supported Formats

Aniwa currently supports:

| Format | Extension |
|---|---|
| CSV | `.csv` |
| JSON | `.json` |
| Excel | `.xlsx`, `.xls` |
| Parquet | `.parquet` |

---

# Reader Philosophy

Readers should remain:

```text
simple, isolated, and efficient
```

---

# Why Isolation Matters

Reader isolation improves:

- maintainability
- debugging
- scalability
- contributor onboarding

---

# Core Reader Responsibilities

Every reader should:

- validate format support
- load data safely
- return a Polars DataFrame
- handle errors gracefully

---

# Standard Reader Flow

Typical execution flow:

```text
file path
→ reader selection
→ parser
→ Polars DataFrame
```

---

# Reader Output Requirement

All readers must return:

```python
polars.DataFrame
```

---

# Why Polars Is Required

Using a single dataframe engine ensures:

- consistency
- performance
- simplified profiling logic

---

# Current Reader Entry Point

Current systems typically route through:

```python
read_dataset()
```

---

# Example Reader Dispatch

Typical logic:

```python
if suffix == ".csv":
    return pl.read_csv(path)
```

---

# Supported Reader Patterns

Readers may support:

| Pattern |
|---|
| direct parsing |
| wrapper parsing |
| conversion pipelines |

---

# Reader Design Principles

Readers should prioritize:

| Principle | Purpose |
|---|---|
| correctness | accurate loading |
| simplicity | maintainability |
| performance | fast execution |
| predictability | stable behavior |

---

# Step-by-Step Guide

---

# Step 1 — Choose the Format

Identify the new dataset format.

Examples:

| Format |
|---|
| XML |
| Avro |
| ORC |
| Feather |
| SQLite |

---

# Step 2 — Evaluate Parsing Libraries

Choose a reliable parser.

Examples:

| Format | Library |
|---|---|
| XML | lxml |
| Avro | fastavro |
| ORC | pyarrow |
| SQLite | sqlite3 |

---

# Step 3 — Create Reader Logic

Add logic inside the reader system.

---

# Example Reader Structure

Example:

```python
if suffix == ".xml":
    return read_xml(path)
```

---

# Step 4 — Convert to Polars

All parsed datasets should become:

```python
pl.DataFrame
```

---

# Example Conversion

Example:

```python
pl.DataFrame(records)
```

---

# Step 5 — Add Extension Support

Register supported extensions.

Example:

```python
SUPPORTED_EXTENSIONS = [
    ".csv",
    ".json",
    ".xml",
]
```

---

# Step 6 — Add Error Handling

Readers should provide:

- helpful errors
- graceful failures
- clear diagnostics

---

# Good Error Example

Example:

```python
raise DatasetReadError(
    "Unsupported dataset type '.xml'."
)
```

---

# Step 7 — Add Tests

Every new reader must include tests.

---

# Required Reader Tests

Tests should validate:

| Test |
|---|
| successful loading |
| invalid files |
| malformed datasets |
| empty datasets |
| edge cases |

---

# Step 8 — Add Example Datasets

Place example files in:

```text
examples/
```

---

# Why Example Files Matter

Examples improve:

- contributor onboarding
- debugging
- testing

---

# Step 9 — Update Documentation

Update:

- README.md
- supported formats docs
- usage examples

---

# Step 10 — Verify CLI Integration

Test end-to-end execution:

```bash
aniwa dataset.xml
```

---

# Reader Architecture Guidelines

Readers should remain:

```text
stateless
```

---

# Why Stateless Readers Matter

Stateless systems improve:

- predictability
- scalability
- testing

---

# Performance Philosophy

Readers should remain:

```text
fast and memory-efficient
```

---

# Why Reader Performance Matters

Dataset loading is often the:

```text
largest bottleneck
```

in profiling systems.

---

# Current Performance Strategies

Current goals include:

- vectorized loading
- minimal copying
- lightweight parsing

---

# Future Reader Optimizations

Future systems may include:

| Optimization |
|---|
| lazy loading |
| chunked loading |
| streaming readers |
| distributed ingestion |

---

# Chunked Reading Vision

Future systems may support:

```text
large dataset chunking
```

---

# Why Chunking Matters

Chunking enables profiling:

- huge CSVs
- memory-heavy datasets
- enterprise files

---

# Streaming Reader Vision

Future readers may support:

```text
stream-based ingestion
```

---

# Future Database Readers

Future readers may connect directly to:

| System |
|---|
| PostgreSQL |
| MySQL |
| DuckDB |
| BigQuery |
| Snowflake |

---

# Future Cloud Readers

Potential future cloud readers:

| Cloud Source |
|---|
| S3 |
| GCS |
| Azure Blob Storage |

---

# Future API Readers

Future ingestion may include:

- REST APIs
- GraphQL
- streaming APIs

---

# Future Data Lake Readers

Potential future integrations:

| System |
|---|
| Delta Lake |
| Iceberg |
| Hudi |

---

# Future Reader Registry

Long-term systems may introduce:

```text
reader registries
```

---

# Why Registries Matter

Registries improve:

- plugin support
- extensibility
- automatic discovery

---

# Example Future Registry

Example:

```python
register_reader(".xml", read_xml)
```

---

# Plugin Reader Vision

Future plugins may allow:

```text
third-party dataset readers
```

---

# Security Philosophy

Readers should prioritize:

- safe parsing
- controlled execution
- predictable behavior

---

# Unsafe Reader Patterns to Avoid

Avoid:

- arbitrary code execution
- unsafe deserialization
- untrusted evaluation

---

# Error Handling Philosophy

Readers should fail:

```text
clearly and gracefully
```

---

# Logging Philosophy

Future readers may support:

- verbose logging
- debug tracing
- profiling diagnostics

---

# Reader Scalability Philosophy

Readers should be designed for:

```text
future enterprise-scale datasets
```

---

# Reader Anti-Patterns

Avoid:

| Anti-Pattern |
|---|
| duplicated parsing logic |
| row-by-row loops |
| hardcoded assumptions |
| silent failures |

---

# Contributor Best Practices

Contributors should prioritize:

- readability
- maintainability
- performance
- testing

---

# Example Reader Template

Basic example:

```python
def read_xml(path: str) -> pl.DataFrame:
    records = parse_xml(path)
    return pl.DataFrame(records)
```

---

# Testing Example

Example test:

```python
def test_read_xml():
    df = read_dataset("examples/sample.xml")
    assert df.height > 0
```

---

# Documentation Checklist

When adding a reader, update:

- README.md
- docs/
- examples/
- tests/

---

# Pull Request Checklist

Before submitting:

- reader works correctly
- tests pass
- examples added
- docs updated
- formatting completed

---

# Long-Term Vision

Aniwa’s ingestion layer is evolving toward:

```text
universal dataset connectivity
```

---

# Strategic Goal

Long-term ingestion goals include:

- files
- databases
- APIs
- streams
- cloud storage
- data lakes

---

# Final Philosophy

The reader system exists to ensure that:

```text
any dataset can eventually become understandable through Aniwa
```

---

# Related Documentation

Continue with:

- architecture/file-readers.md
- architecture/system-design.md
- api/readers.md
- developer-guide/testing.md