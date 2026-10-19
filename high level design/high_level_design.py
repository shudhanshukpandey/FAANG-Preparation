"""High-Level Design (HLD) & Distributed Systems Master Test Runner.

Executes all 62 architectural pattern simulations across 18 system design pillars:
  - 01_core_concepts
  - 02_networking_and_traffic
  - 03_load_balancing
  - 04_api_design_and_gateways
  - 05_communication_patterns
  - 06_caching_strategies
  - 07_database_architectures
  - 08_database_scaling
  - 09_storage_systems
  - 10_architectural_patterns
  - 11_microservices_resilience
  - 12_distributed_consensus
  - 13_distributed_transactions
  - 14_data_structures_for_scale
  - 15_big_data_and_streaming
  - 16_deployment_and_observability
  - 17_security_and_identity
  - 18_ai_and_llm_infrastructure
"""

import os
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

PILLARS = [
    "01_core_concepts",
    "02_networking_and_traffic",
    "03_load_balancing",
    "04_api_design_and_gateways",
    "05_communication_patterns",
    "06_caching_strategies",
    "07_database_architectures",
    "08_database_scaling",
    "09_storage_systems",
    "10_architectural_patterns",
    "11_microservices_resilience",
    "12_distributed_consensus",
    "13_distributed_transactions",
    "14_data_structures_for_scale",
    "15_big_data_and_streaming",
    "16_deployment_and_observability",
    "17_security_and_identity",
    "18_ai_and_llm_infrastructure",
]


def run_all():
    total_passed = 0
    total_failed = 0

    print("=" * 75)
    print("🚀 High-Level Design (HLD) Distributed Systems Test Suite Runner")
    print("=" * 75)

    for pillar in PILLARS:
        pillar_path = BASE_DIR / pillar
        if not pillar_path.exists():
            continue

        print(f"\n📂 Scanning Pillar: {pillar}")
        py_files = sorted(pillar_path.glob("*/*.py"))

        for py_file in py_files:
            rel_name = py_file.relative_to(BASE_DIR)
            res = subprocess.run([sys.executable, str(py_file)], capture_output=True, text=True)
            if res.returncode == 0:
                print(f"  ✅ {rel_name}")
                total_passed += 1
            else:
                print(f"  ❌ {rel_name} FAILED!")
                print(res.stderr or res.stdout)
                total_failed += 1

    print("\n" + "=" * 75)
    print(f"HLD Execution Summary: {total_passed} Passed | {total_failed} Failed")
    print("=" * 75)

    if total_failed > 0:
        sys.exit(1)


if __name__ == "__main__":
    run_all()
