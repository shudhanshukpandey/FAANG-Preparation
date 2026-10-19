"""Low-Level Design (LLD) & Object-Oriented Design (OOD) Master Test Runner.

Executes all pattern demonstrations across:
  - 01_oop_fundamentals
  - 02_design_principles
  - 04_creational_patterns
  - 05_structural_patterns
  - 06_behavioral_patterns
  - 07_enterprise_backend_patterns
  - 08_resilience_and_concurrency
  - 09_classic_machine_coding
"""

import os
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

MODULES = [
    "01_oop_fundamentals",
    "02_design_principles",
    "04_creational_patterns",
    "05_structural_patterns",
    "06_behavioral_patterns",
    "07_enterprise_backend_patterns",
    "08_resilience_and_concurrency",
    "09_classic_machine_coding",
]


def run_all():
    total_passed = 0
    total_failed = 0

    print("=" * 70)
    print("🚀 Low-Level Design (LLD) Master Test Suite Runner")
    print("=" * 70)

    for mod in MODULES:
        mod_path = BASE_DIR / mod
        if not mod_path.exists():
            continue

        print(f"\n📂 Scanning Module: {mod}")
        py_files = sorted(mod_path.glob("*/*.py"))

        for py_file in py_files:
            rel_name = py_file.relative_to(BASE_DIR)
            res = subprocess.run([sys.executable, str(py_file)], capture_output=True, text=True)
            if res.returncode == 0:
                print(f"  ✅ {rel_name}")
                total_passed += 1
            else:
                print(f"  ❌ {rel_name} FAILED!")
                print(res.stderr)
                total_failed += 1

    print("\n" + "=" * 70)
    print(f"Summary: {total_passed} Passed | {total_failed} Failed")
    print("=" * 70)


if __name__ == "__main__":
    run_all()
