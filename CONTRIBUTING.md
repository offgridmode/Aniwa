# Contributing to Aniwa

Thank you for your interest in contributing to Aniwa.

Aniwa is an open-source universal dataset profiling and intelligence tool built for developers, analysts, data engineers, researchers, and modern data teams.

We welcome contributions of all kinds:
- bug fixes
- new features
- performance improvements
- documentation updates
- tests
- report enhancements
- profiling modules
- developer experience improvements

---

# Table of Contents

- Development Setup
- Running Aniwa
- Running Tests
- Project Structure
- Contribution Workflow
- Pull Request Guidelines
- Code Style
- Testing Expectations
- Good First Contributions
- Community Guidelines

---

# Development Setup

## 1. Fork the Repository

Fork the repository on GitHub and clone your fork locally.

```bash
git clone https://github.com/YOUR_USERNAME/Aniwa.git
cd Aniwa
```

---

## 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment.

### Windows

```bash
source .venv/Scripts/activate
```

### macOS/Linux

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Install Aniwa locally:

```bash
pip install -e .
```

---

# Running Aniwa

Example usage:

```bash
aniwa examples/customers.csv
```

Generate JSON report:

```bash
aniwa examples/customers.csv --report json --output profile.json
```

Generate HTML report:

```bash
aniwa examples/customers.csv --report html --output profile.html
```

---

# Running Tests

Run all tests:

```bash
pytest
```

Run a specific test file:

```bash
pytest tests/test_profiler.py
```

---

# Project Structure

```text
Aniwa/
│
├── aniwa/
│   ├── cli.py
│   │
│   ├── core/
│   │   ├── profiler.py
│   │   ├── schema.py
│   │   ├── statistics.py
│   │   ├── quality.py
│   │   └── insights.py
│   │
│   ├── io/
│   │   └── readers.py
│   │
│   ├── reports/
│   │   ├── console.py
│   │   ├── json_report.py
│   │   └── html_report.py
│   │
│   ├── models/
│   │   └── profile.py
│   │
│   └── utils/
│
├── tests/
├── examples/
└── README.md
```

---

# Contribution Workflow

## 1. Create a Branch

Create a feature branch from the latest version of `main`.

```bash
git checkout -b feature/add-html-report
```

---

## 2. Make Your Changes

Keep changes:
- focused
- readable
- modular
- well-tested

Avoid unrelated formatting or refactoring changes in the same pull request.

---

## 3. Run Tests

Before opening a pull request:

```bash
pytest
```

Make sure all tests pass.

---

## 4. Commit Your Changes

Example:

```bash
git commit -m "Add HTML report generation"
```

---

## 5. Push Your Branch

```bash
git push origin feature/add-html-report
```

---

## 6. Open a Pull Request

Open a pull request against the `main` branch.

Please include:
- a clear description
- screenshots if UI/report changes are included
- related issue references if applicable

---

# Pull Request Guidelines

Good pull requests are:
- focused
- tested
- documented
- easy to review

Please:
- keep PRs small when possible
- avoid unrelated file changes
- add tests for new functionality
- update documentation when necessary

---

# Code Style

Aniwa aims to maintain:
- clean architecture
- readable code
- modular design
- consistent naming
- developer-friendly APIs

Recommended practices:
- use type hints
- keep functions focused
- avoid deeply nested logic
- write descriptive variable names

---

# Testing Expectations

New features should include:
- unit tests
- edge case handling
- reader validation tests where applicable

Examples:
- CSV reader tests
- Parquet reader tests
- profiling logic tests
- report generation tests

---

# Good First Contributions

Here are some beginner-friendly contribution ideas:

## Profiling Improvements
- improve insights
- add additional quality checks
- improve type inference

## Reporting
- improve Rich terminal formatting
- improve HTML report styling
- add Markdown export

## Testing
- add reader tests
- improve edge case coverage
- add report tests

## Documentation
- improve examples
- improve setup instructions
- add screenshots
- improve roadmap documentation

---

# Community Guidelines

Please be respectful and constructive.

Aniwa is intended to be:
- welcoming
- collaborative
- developer-friendly
- beginner-friendly

Constructive feedback and thoughtful discussions are encouraged.

---

# Vision

Aniwa aims to become a universal dataset intelligence platform that helps people understand data quickly, clearly, and confidently.

Thank you for contributing to Aniwa.

> Aniwa — See your data clearly.
