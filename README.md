# llmAgent

A production-grade Python orchestration layer that hooks into the Ollama infrastructure to dynamically break down complex user tasks into clear, executable goals. This project is architected with strict validation rules, robust exception translation wrapping, and high-density parameterized testing matrices.

---

## 🏗️ Architecture & Component Design

The application follows an **Inversion of Control (IoC) / Dependency Injection** architecture split into clean domain layers:

*   **`src/config.py`**: Central system definitions managing environment parameters, host tokens, and max character constraint limits.
*   **`src/validators.py`**: Core domain logic validating string bounds and scanning inputs for malicious security injection vectors.
*   **`src/resiliance.py`**: Custom domain error definitions (`APIConnectionTimeoutError`, `ProviderRateLimitError`, `AIApplicationError`).
*   **`src/main.py`**: Core client orchestrator managing data stream loops and translation boundaries.

---

## 🛡️ Exception Translation Matrix

Low-level infrastructure and stream connection failures are caught and systematically translated into high-level domain exceptions to support advanced logging telemetry tools:

| Raw Exception Substring | Translated Domain Exception | Business Impact |
| :--- | :--- | :--- |
| Contains `"timeout"` | `APIConnectionTimeoutError` | Triggers a timeout warning log trace |
| Contains `"rate limit"` or `"429"` | `ProviderRateLimitError` | Informs throttling/retry mechanisms |
| Any unhandled catch-all fallback | `AIApplicationError` | Safety net for unexpected component issues |

---

## 🧪 Testing Infrastructure

The test engine uses **Pytest** along with modern, advanced testing practices to validate functionality without executing live network I/O packets:

*   **Mock Factory Pipelines**: Implements linked Factory-Instance mocking structures to control third-party class instantiation scopes.
*   **High-Density Parameterization**: Utilizes `@pytest.mark.parametrize` to run comprehensive validation tests across multiple datasets in parallel.
*   **Parameterized Fixtures**: Leverages `request.param` loops to dynamically cycle a generic `Exception` across different message strings to verify translation matrix paths.
*   **Telemetry Verification**: Incorporates `caplog` tracking to inspect application warnings and severities without altering internal loops.

---

## 🚀 Setup & Local Execution

### 1. Prerequisites
Ensure you have Python 3.12+ installed on your system.

### 2. Environment Setup
Clone the repository and spin up an isolated virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# .venv\Scripts\activate   # On Windows
pip install -r requirements.txt
```

### 3. Run the Application
Execute the command-line orchestrator:
```bash
python -m src.main
```

---

## 📈 Running the Test Suite

Execute the entire unit and validation test suite from the root project directory:
```bash
python -m pytest -v
```

### CI/CD Report Generation
To export a standard, JUnit-compatible XML test report for build server processing (e.g., GitHub Actions, GitLab CI), append the output flag:
```bash
python -m pytest --junitxml=report.xml
```
