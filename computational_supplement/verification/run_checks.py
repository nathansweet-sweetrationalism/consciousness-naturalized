#!/usr/bin/env python3
"""Reproduce bounded mathematical checks in the public Consciousness Naturalized archive."""

import hashlib
import json
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPTS = [
    "foundational_formal_checks.py",
    "section_xii_formal_checks.py",
    "kh_dependency_finite_model.py",
    "plasticity_supplement_adversarial_checks.py",
    "reser_exact_statistical_audit.py",
]


def main():
    results = []
    for name in SCRIPTS:
        proc = subprocess.run(
            [sys.executable, str(HERE / name)], cwd=HERE, text=True,
            capture_output=True, timeout=60, check=True,
        )
        # All formal check programs must emit valid JSON.
        parsed = json.loads(proc.stdout)
        results.append({
            "file": name,
            "source_sha256": hashlib.sha256((HERE / name).read_bytes()).hexdigest(),
            "returned_json": parsed,
            "stderr": proc.stderr.strip(),
            "exit_code": proc.returncode,
        })
    logic = subprocess.run(
        [sys.executable, str(HERE / "logic_audit.py"),
         str(HERE / "article_2115_classical_logic_claims.json")],
        cwd=HERE, text=True, capture_output=True, timeout=60, check=True,
    )
    logic_result = json.loads(logic.stdout)
    got = [x["status"] for x in logic_result["results"]]
    expected = ["invalid_countermodel"] * 3 + ["valid_classical_propositional"] * 2
    if got != expected:
        raise AssertionError(f"Unexpected logical dispositions: {got}")
    results.append({"file": "logic_audit.py", "returned_json": logic_result,
                    "exit_code": logic.returncode})
    receipt = {
        "run_at_utc": datetime.now(timezone.utc).isoformat(),
        "python": platform.python_version(),
        "claim_scope": "Exact arithmetic, unit checks, stipulated finite models and propositional encodings only. No empirical or phenomenal identity theorem.",
        "results": results,
    }
    out = HERE / "execution_receipt.json"
    out.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Passed {len(results)} script/logic groups; see {out.name}")


if __name__ == "__main__":
    main()
