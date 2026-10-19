---
description: "Guidelines and conventions for writing Python scripts and patterns in this repo"
applyTo: "**/*.py"
---

# Python Instructions

## Conventions
- Target Python 3.13. Rely primarily on standard library modules (`typing`, `abc`, `dataclasses`, `collections`, `threading`, `functools`).
- Always annotate function signatures and method returns with complete type hints.
- Every runnable pattern or algorithm file must include an `if __name__ == "__main__":` block demonstrating typical usage and validating outputs.
- Prefer explicit classes or dataclasses for structured data.
- Avoid introducing external third-party dependencies unless strictly required and approved.

## Testing & Verification
- Verify changes by running the script directly with:
  ```bash
  python3 <path/to/script.py>
  ```
- Ensure output exits with status code 0 and prints clear execution logs.
