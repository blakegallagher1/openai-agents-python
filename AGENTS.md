# AGENTS.md

## Project Overview

This repository contains the EBR Zoning Strategist—a modular Python tool for automated, auditable analysis and scenario modeling of the East Baton Rouge Parish Unified Development Code (UDC).

## Directory Structure

- **ebr_zoning_strategist/**
    - `models.py` – Pydantic models, all objects fully auditable (source, page, table).
    - `parser.py` – Extracts, normalizes, maps zoning data from PDF/markdown.
    - `extract_tables.py` – Table extraction using pdfplumber/camelot.
    - `engine.py` – Scenario engine: parcel, use, overlays → full compliance JSON report.
    - `api.py` – Public API.
    - `cli.py` – Command-line interface.
    - `cache.py` – Pickle-based cache.
    - `tests/` – Unit/integration tests.
    - `README.md` – Usage/API docs.

## Setup Instructions

Codex must execute this script before doing anything:
```bash
codex/setup.sh
This creates a virtual environment and installs all dependencies from requirements.txt.

Network Isolation:
Codex disables network after this script runs. All dependencies must install at this stage. If you need OS-level libraries (e.g., for camelot or geopandas), pre-install via Docker or ensure all wheels are available.

Testing
All tests: pytest tests/

Test file: pytest tests/test_parser.py

Coverage: pytest --cov=ebr_zoning_strategist tests/

Lint: flake8 ebr_zoning_strategist/

Type: mypy ebr_zoning_strategist/

Contribution & PRs
Branches: feature/<desc>, fix/<desc>

Commits: Type: short desc (e.g., Fix: correct buffer mapping)

PRs: All tests must pass, coverage must not decrease, docs updated if needed.

Codex Task Guidance
Parser: Maximize coverage of all district/overlay tables. All ambiguous/unsupported cases → audit log, never guessed.

Scenario Engine: Validate every result, flag all compliance/gaps, report in JSON.

Audit Logging: Every mapping error, fallback, or skipped item must be logged (source, page, reason).

Tests: Every engine/parser function and edge case.

Docs: Always update README.md and progress_tracker.md as changes ship.

Performance: Optimize for large batch runs (1–100,000 parcels).

File Notes
parser.py: Handle irregular/merged/ambiguous tables, propagate context.

engine.py: All code logic must be auditable, overlay/adjacency logic explicit.

cli.py: Support scenario reporting, JSON outputs, audit log inspection.

Outstanding Problems
Harden parser to all EBR edge cases (merged headers, missing columns, ambiguous tables).

Ensure >90% coverage of districts/overlays, with remainder flagged for QA.

Batch analysis/scaling, automation of audit log/manual fix mapping.

High Leverage Improvements
Further generalize parser/engine logic, never sacrifice auditability.

If scale bottlenecked, switch cache to Parquet or other backend.

Automate audit log → manual fix mapping if possible.

