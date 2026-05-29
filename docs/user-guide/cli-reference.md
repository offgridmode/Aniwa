# CLI Reference

This document provides the complete command-line interface reference for Aniwa.

---

## Basic Syntax

```bash
aniwa profile [OPTIONS] PATH
```

Example:

```bash
aniwa profile examples/customers.csv
```

**Note:** Aniwa requires the `profile` command before the dataset path. This allows for future commands like `aniwa compare`, `aniwa validate`, etc.

---

## Core Commands

### Primary Profiling Command

```bash
aniwa profile [OPTIONS] PATH
```

Profile a dataset and generate reports.

### List Presets Command

```bash
aniwa list-presets
```

Display all available profiling presets with descriptions.

### Help Command

```bash
aniwa --help
aniwa profile --help
```

---

## Required Arguments

### PATH

Path to dataset file.

Example:

```bash
aniwa profile examples/customers.csv
```

Supported file types:

- CSV (.csv)
- Excel (.xlsx, .xls)
- JSON (.json)
- Parquet (.parquet)

---

## CLI Options

### --preset

Use a predefined profiling preset.

**Short form:** `-p`

**Example:**
```bash
aniwa profile dataset.csv --preset quick
```

**Supported presets:**

| Preset | Description |
|--------|-------------|
| quick | Fast lightweight profiling for quick data inspection |
| standard | Balanced default profiling with statistics and insights |
| audit | Comprehensive profiling for validation and audit workflows |
| enterprise | Professional branded reporting for stakeholders |

**What presets configure:**
- profiling mode
- report format
- report template
- included/excluded sections
- verbosity level

---

### --report

Specify report format.

**Short form:** `-r`

**Example:**
```bash
aniwa profile dataset.csv --report html
```

**Supported values:**
- console
- json
- html
- excel
- markdown
- pdf

---

### --output

Specify explicit output filename.

**Short form:** `-o`

**Example:**
```bash
aniwa profile dataset.csv --report html --output profile.html
```

---

### --output-dir

Generate reports into a directory.

**Example:**
```bash
aniwa profile dataset.csv --report pdf --output-dir reports/
```

Aniwa automatically:
- creates directories
- generates filenames
- applies extensions

**Generated example:**
```text
reports/aniwa_report.pdf
```

---

### --mode

Specify profiling mode.

**Short form:** `-m`

**Example:**
```bash
aniwa profile dataset.csv --mode fast
```

**Supported values:**
- fast
- deep

---

### --include

Include specific report sections.

**Short form:** `-i`

**Example:**
```bash
aniwa profile dataset.csv --include summary,statistics
```

---

### --exclude

Exclude report sections.

**Short form:** `-e`

**Example:**
```bash
aniwa profile dataset.csv --exclude charts
```

---

### --template

Specify report template.

**Short form:** `-t`

**Example:**
```bash
aniwa profile dataset.csv --report html --template dark
```

**Supported templates:**
- default - Balanced modern design
- clean - Minimal lightweight appearance
- compact - Dense information-focused layout
- enterprise - Professional executive-style reporting
- dark - Dark-mode optimized reporting

---

### --verbosity

Control output detail level.

**Example:**
```bash
aniwa profile dataset.csv --verbosity verbose
```

**Supported levels:**

| Level | Description | Best For |
|-------|-------------|----------|
| quiet | Only errors and final status | CI/CD pipelines, automation |
| normal | Standard output (default) | Everyday use |
| verbose | Detailed progress and timing | Understanding operations |
| debug | Full diagnostic output | Development, troubleshooting |

---

### --config

Specify custom configuration file.

**Short form:** `-c`

**Example:**
```bash
aniwa profile dataset.csv --config examples/config_sample.yaml
```

---

## Complete Examples

### Basic Profiling

```bash
aniwa profile examples/customers.csv
```

### Using Presets

```bash
# Quick inspection
aniwa profile examples/customers.csv --preset quick

# Standard analysis
aniwa profile examples/customers.csv --preset standard

# Audit preparation
aniwa profile examples/customers.csv --preset audit

# Enterprise report
aniwa profile examples/customers.csv --preset enterprise
```

### JSON Report

```bash
aniwa profile examples/customers.csv --report json --output profile.json
```

### HTML Report

```bash
aniwa profile examples/customers.csv --report html --template dark --output profile.html
```

### PDF Report

```bash
aniwa profile examples/customers.csv --report pdf --template enterprise
```

### Fast Profiling

```bash
aniwa profile examples/customers.csv --mode fast
```

### Deep Profiling

```bash
aniwa profile examples/customers.csv --mode deep
```

### Include Specific Sections

```bash
aniwa profile examples/customers.csv --include summary,insights
```

### Exclude Specific Sections

```bash
aniwa profile examples/customers.csv --exclude statistics
```

### Verbosity Examples

```bash
# Quiet mode for CI/CD
aniwa profile dataset.csv --verbosity quiet

# Normal mode (default)
aniwa profile dataset.csv

# Verbose mode with detailed progress
aniwa profile dataset.csv --verbosity verbose

# Debug mode for troubleshooting
aniwa profile dataset.csv --verbosity debug
```

### Output Directory

```bash
aniwa profile examples/customers.csv --report html --output-dir reports/
```

### Custom Config File

```bash
aniwa profile examples/customers.csv --config configs/team.yaml
```

### Combining Multiple Options

```bash
# Preset with overrides
aniwa profile dataset.csv \
    --preset enterprise \
    --mode fast \
    --output-dir reports/ \
    --verbosity verbose

# Full custom configuration
aniwa profile dataset.csv \
    --mode deep \
    --report html \
    --template dark \
    --include summary,statistics,insights \
    --output-dir ./profiles \
    --verbosity verbose

# Audit with custom output
aniwa profile dataset.csv \
    --preset audit \
    --output-dir audits/$(date +%Y%m%d) \
    --verbosity debug 2>&1 | tee audit.log
```

---

## Report Sections

Supported sections that can be included or excluded:

| Section | Description |
|---------|-------------|
| summary | Dataset overview (rows, columns, size) |
| schema | Column names, types, and properties |
| quality | Data quality metrics (nulls, duplicates) |
| statistics | Statistical summaries (mean, median, std) |
| insights | Intelligent data quality insights |
| charts | Visualizations and distributions |

---

## Report Templates

### default
Balanced modern design with clean typography and适度 visual elements.

### clean
Minimal lightweight appearance focusing on content without distraction.

### compact
Dense information-focused layout for detailed analysis with maximum data density.

### enterprise
Professional executive-style reporting with branding and stakeholder focus.

### dark
Dark-mode optimized reporting for low-light environments.

---

## Profiling Modes

### fast mode (`--mode fast`)

Optimized for speed and large datasets.

**Includes:**
- Schema detection
- Null value analysis
- Duplicate detection
- Basic quality metrics

**Excludes:**
- Statistical computations
- Advanced insights
- Correlation analysis
- Chart generation

**Best for:**
- Initial data exploration
- CI/CD pipelines
- Very large datasets (>1M rows)
- Quick structure validation

### deep mode (`--mode deep`)

Comprehensive profiling with full analysis (default).

**Includes everything from fast mode plus:**
- Statistical summaries (min, max, mean, median, std)
- Distribution analysis
- Advanced insights
- Pattern detection

**Best for:**
- Detailed data understanding
- Quality assessment
- Data science preparation
- Audit and compliance

---

## Verbosity Levels

### quiet (`--verbosity quiet`)

Only show critical errors and final completion status.

**What you see:**
- Critical errors (if any)
- Final completion message
- No progress indicators
- No warnings
- No timing information

**Best for:**
- CI/CD pipelines
- Automated scripts
- Production environments
- Batch processing

### normal (`--verbosity normal`)

Standard output with key information (default).

**What you see:**
- High-level stage indicators (→)
- Success confirmations (✓)
- Data quality warnings
- Report generation messages
- Final summary

**Best for:**
- Daily interactive use
- Quick profiling tasks
- Most common scenarios

### verbose (`--verbosity verbose`)

Detailed progress with timing information.

**What you see:**
- Everything from normal mode plus:
- Timing for each stage
- Progress bars for multi-step operations
- Per-column statistics computation
- Timing summary table
- Detailed completion messages

**Best for:**
- Understanding slow operations
- Performance investigation
- Learning what Aniwa does
- Debugging complex datasets

### debug (`--verbosity debug`)

Full diagnostic output for development.

**What you see:**
- Everything from verbose mode plus:
- Internal state and configuration
- Data structure details
- Decision points
- Per-column statistics with values
- Entry/exit of every function
- Stack traces on errors

**Best for:**
- Development
- Reporting bugs
- Understanding internal logic
- Troubleshooting unexpected behavior

---

## Configuration Discovery

Aniwa automatically searches for configuration files in the current working directory:

```text
aniwa.yaml
aniwa.yml
aniwa.toml
aniwa.json
```

### Example Configuration File

```yaml
# aniwa.yaml
mode: deep
report: html
template: enterprise
verbosity: normal

sections:
  include:
    - summary
    - schema
    - quality
    - statistics
    - insights

report:
  output_dir: ./reports
```

---

## CLI Override Rules

Priority order (highest to lowest):

```text
CLI arguments > Preset values > Config file > Defaults
```

### Priority Examples

```bash
# CLI overrides preset
aniwa profile dataset.csv --preset quick --mode deep
# Result: Uses deep mode, not fast

# Preset overrides config file
aniwa profile dataset.csv --preset enterprise
# Result: Uses preset values over config.yaml settings

# CLI overrides everything
aniwa profile dataset.csv --preset enterprise --mode fast --report json
# Result: All CLI values take precedence
```

---

## Error Examples

### Invalid Section

```text
Invalid report section: metrics.
Valid options are: summary, schema, quality, statistics, insights, charts
```

### Invalid Mode

```text
Invalid profiling mode: ultra.
Valid options are: fast, deep
```

### Invalid Preset

```text
Unknown preset: 'mypreset'. Available presets: quick, standard, audit, enterprise
```

### Invalid Verbosity Level

```text
Invalid verbosity level: extreme.
Valid options are: quiet, normal, verbose, debug
```

### Missing File

```text
File does not exist: dataset.csv
```

### Conflicting Output Arguments

```text
Use either --output or --output-dir, not both.
```

### Conflicting Section Arguments

```text
Use either --include or --exclude, not both.
```

---

## Internal CLI Architecture

Primary CLI logic exists in:

```text
aniwa/cli.py
aniwa/presets.py
aniwa/utils/logging.py
```

**Responsibilities:**
- Argument parsing and validation
- Configuration file loading
- Preset application and resolution
- Verbosity management
- Execution orchestration
- Report routing
- Metadata generation
- Error handling

---

## Recommended Usage Patterns

### Quick Data Exploration

```bash
aniwa profile dataset.csv --preset quick
```

### Daily Analysis Workflow

```bash
aniwa profile dataset.csv --preset standard
```

### Professional Reporting

```bash
aniwa profile dataset.csv --preset enterprise --output-dir reports/
```

### Audit & Compliance

```bash
aniwa profile dataset.csv --preset audit --verbosity verbose
```

### CI/CD Automation

```bash
aniwa profile dataset.csv --preset quick --verbosity quiet --report json
```

### Custom Analysis

```bash
aniwa profile dataset.csv --mode deep --include statistics,insights --exclude charts
```

### Performance Investigation

```bash
aniwa profile large_dataset.csv --mode deep --verbosity verbose
```

### Bug Reporting

```bash
aniwa profile problem_dataset.csv --verbosity debug 2>&1 | tee debug.log
```

### Team Standardization

```bash
aniwa profile dataset.csv --config team_config.yaml
```

---

## Quick Reference Card

```bash
# Basic command structure
aniwa profile PATH [OPTIONS]

# Most common commands
aniwa profile dataset.csv                           # Basic profiling
aniwa profile dataset.csv --preset quick            # Quick inspection
aniwa profile dataset.csv --preset standard         # Standard analysis
aniwa profile dataset.csv --preset enterprise       # Professional report
aniwa profile dataset.csv --report html             # HTML report
aniwa profile dataset.csv --verbosity verbose       # Detailed output

# Utility commands
aniwa list-presets                                   # List available presets
aniwa profile --help                                 # Get help
aniwa --help                                         # General help

# Advanced examples
aniwa profile dataset.csv --preset enterprise --mode fast --output-dir reports/
aniwa profile dataset.csv --report html --template dark --include summary,stats
aniwa profile dataset.csv --verbosity debug --preset audit 2>&1 | tee debug.log
```

---

## Best Practices

### For Beginners
1. Start with `aniwa profile dataset.csv --preset quick`
2. Move to `aniwa profile dataset.csv --preset standard` for deeper analysis
3. Use `aniwa profile dataset.csv --preset enterprise` for sharing reports
4. Add `--verbosity verbose` to understand what's happening

### For Daily Use
1. Use `aniwa profile dataset.csv --preset standard` as your default
2. Override with `--mode fast` for very large files
3. Add `--report html` when you need to save results
4. Create a config file for your team's standards

### For CI/CD Pipelines
```bash
aniwa profile dataset.csv \
    --preset quick \
    --verbosity quiet \
    --report json \
    --output-dir ./artifacts
```

### For Data Governance
```bash
aniwa profile dataset.csv \
    --preset audit \
    --output-dir ./audits/$(date +%Y%m%d) \
    --verbosity verbose \
    --template enterprise
```

### For Performance Optimization
1. Use `--preset quick` for datasets > 1M rows
2. Use `--mode fast` when you don't need statistics
3. Use `--exclude charts` to skip visualization generation
4. Run `--verbosity verbose` once to identify bottlenecks

---

## Future CLI Roadmap

Planned CLI capabilities for future releases:

### v0.2.x - Intelligence
- `aniwa compare` - Compare two datasets
- `aniwa diff` - Show detailed differences
- `aniwa monitor` - Continuous profiling

### v0.3.x - Universal Connectivity
- `aniwa connect` - Database connection management
- Database-specific commands for PostgreSQL, MySQL, BigQuery

### v0.4.x - Extensibility
- `aniwa plugin` - Plugin management commands
- `aniwa extension` - Extension installation

### v0.5.x - AI Intelligence
- `aniwa explain` - AI-powered insights
- `aniwa suggest` - Optimization suggestions

### v0.6+ - Governance
- `aniwa validate` - Run validation rules
- `aniwa lineage` - Data lineage tracking
- `aniwa profile --watch` - Real-time profiling

---

## Environment Variables

Future support for environment variables:

```bash
ANIWA_VERBOSITY=debug
ANIWA_REPORT_FORMAT=html
ANIWA_OUTPUT_DIR=./reports
ANIWA_CONFIG_PATH=/etc/aniwa/config.yaml
```

---

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success - Profiling completed normally |
| 1 | Error - Critical error occurred |
| 2 | Warning - Quality issues detected |
| 3 | Invalid input - Bad arguments or file |
| 4 | Configuration error - Invalid config |
