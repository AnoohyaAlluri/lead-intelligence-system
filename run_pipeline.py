"""
Pipeline Runner: Lead Intelligence System

Runs the public-safe synthetic lead intelligence pipeline in order:

1. Bronze: Profile raw synthetic datasets
2. Silver: Clean and standardize records
3. Gold: Generate match results and exception queue
4. Analytics: Generate verification summary

Public-safe rule:
This project uses synthetic data only.
Do not use this pipeline with real company, client, owner, tenant,
property, email, phone, CRM, AppFolio, LeadSimple, Gmail, or internal system data.
"""

from pathlib import Path
import subprocess
import sys


BASE_DIR = Path(__file__).resolve().parent


PIPELINE_STEPS = [
    "scripts/bronze/01_profile_raw_data.py",
    "scripts/silver/02_clean_records.py",
    "scripts/gold/03_generate_match_results.py",
    "scripts/analytics/04_generate_verification_summary.py",
]


def run_step(script_path: str) -> None:
    """Run one pipeline step and stop if it fails."""
    full_path = BASE_DIR / script_path

    if not full_path.exists():
        raise FileNotFoundError(f"Pipeline step not found: {full_path}")

    print(f"\nRunning: {script_path}")
    result = subprocess.run(
        [sys.executable, str(full_path)],
        cwd=BASE_DIR,
        check=False,
    )

    if result.returncode != 0:
        raise RuntimeError(f"Pipeline step failed: {script_path}")

    print(f"Completed: {script_path}")


def main() -> None:
    """Run the full synthetic lead intelligence pipeline."""
    print("Starting Lead Intelligence System pipeline...")

    for step in PIPELINE_STEPS:
        run_step(step)

    print("\nPipeline completed successfully.")
    print("Generated outputs:")
    print("- datasets/analytics/raw_data_profile_mock.csv")
    print("- datasets/cleaned/cleaned_marketing_leads.csv")
    print("- datasets/cleaned/cleaned_client_records.csv")
    print("- outputs/client_match_results_mock.csv")
    print("- outputs/exception_queue_mock.csv")
    print("- datasets/analytics/lead_verification_summary_mock.csv")


if __name__ == "__main__":
    main()
