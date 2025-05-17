# AGENTS.md

## 🧭 Project Overview
This repository contains the "EBR Zoning Strategist," a tool designed to parse and analyze the East Baton Rouge Parish Unified Development Code (UDC). It provides automated, auditable zoning code analysis and scenario modeling for every district and overlay defined by law.

## 🗂️ Code Structure
- **ebr_zoning_strategist/**
  - `models.py`: Pydantic models for regulatory objects with audit trace fields.
  - `parser.py`: Extracts and normalizes zoning data from PDFs/Markdown.
  - `extract_tables.py`: Abstracts table extraction using `pdfplumber` and `camelot`.
  - `engine.py`: Applies parsed code to user scenarios, generating compliance reports.
  - `api.py`: Public API for CLI/notebook or external calls.
  - `cli.py`: Command-line interface for various analyses.
  - `cache.py`: Pickle-based cache for parsed code.
  - `tests/`: Unit and integration tests.
  - `README.md`: Usage and API documentation.

## 🧪 Testing Instructions
- **Run all tests**:
  ```bash
  pytest tests/
  ```
- **Run specific test file**:
  ```bash
  pytest tests/test_parser.py
  ```
- **Run tests with coverage**:
  ```bash
  pytest --cov=ebr_zoning_strategist tests/
  ```
- **Linting**:
  ```bash
  flake8 ebr_zoning_strategist/
  ```
- **Type Checking**:
  ```bash
  mypy ebr_zoning_strategist/
  ```

## 🛠️ Setup Instructions
Before running tests or the application, ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

## 📝 Contribution Guidelines
- **Branch Naming**: Use descriptive names, e.g., `feature/parser-enhancement`.
- **Commit Messages**: Follow the format `Type: Short description`, e.g., `Fix: Handle merged headers in parser`.
- **Pull Requests**: Ensure all tests pass and include relevant descriptions.

## 🔍 Codex Specific Instructions
- **Focus Areas**:
  - Prioritize improving the parser's ability to handle complex tables, merged headers, and multi-row contexts.
  - Enhance the scenario engine to support diverse parcel geometries and overlays.
- **Audit Logging**:
  - Ensure that any ambiguous or unmapped regulatory data is logged in `audit_log.csv`.
  - Do not guess or fill in missing data; always log for manual review.
- **Testing**:
  - After modifications, run the full test suite to ensure no regressions.
  - Maintain or improve the current test coverage percentage.
- **Documentation**:
  - Update `README.md` and `progress_tracker.md` with any changes or enhancements made.
- **Performance**:
  - Monitor and optimize the performance of the parser and engine, especially for batch analyses.

## 📂 File-Specific Notes
- **parser.py**:
  - Focus on enhancing the robustness against irregular table structures.
- **engine.py**:
  - Ensure accurate application of zoning rules based on parsed data.
- **cli.py**:
  - Maintain user-friendly command-line interactions and outputs.

## 📌 Notes
- Codex should operate within the confines of the provided codebase and instructions.
- Any external dependencies or significant architectural changes should be approved before implementation.
