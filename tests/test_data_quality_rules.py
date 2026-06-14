"""
QA Tests: Lead Intelligence System

These tests validate the public-safe synthetic pipeline outputs.

Public-safe rule:
These tests are designed for synthetic data only.
Do not use them with real company, client, owner, tenant, property,
email, phone, CRM, AppFolio, LeadSimple, Gmail, or internal system data.
"""

from pathlib import Path
import subprocess
import sys

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]

RAW_LEADS_PATH = BASE_DIR / "datasets" / "raw" / "raw_marketing_leads_mock.csv"
RAW_CLIENTS_PATH = BASE_DIR / "datasets" / "raw" / "raw_client_records_mock.csv"
CLEANED_LEADS_PATH = BASE_DIR / "datasets" / "cleaned" / "cleaned_marketing_leads.csv"
CLEANED_CLIENTS_PATH = BASE_DIR / "datasets" / "cleaned" / "cleaned_client_records.csv"
MATCH_RESULTS_PATH = BASE_DIR / "outputs" / "client_match_results_mock.csv"
EXCEPTION_QUEUE_PATH = BASE_DIR / "outputs" / "exception_queue_mock.csv"
SUMMARY_PATH = BASE_DIR / "datasets" / "analytics" / "lead_verification_summary_mock.csv"
RUN_PIPELINE_PATH = BASE_DIR / "run_pipeline.py"


def run_pipeline_once():
    """Run the synthetic pipeline before validating generated outputs."""
    result = subprocess.run(
        [sys.executable, str(RUN_PIPELINE_PATH)],
        cwd=BASE_DIR,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, (
        "Pipeline failed.\n"
        f"STDOUT:\n{result.stdout}\n"
        f"STDERR:\n{result.stderr}"
    )


def test_raw_input_files_exist():
    """Validate that required synthetic raw input files exist."""
    assert RAW_LEADS_PATH.exists()
    assert RAW_CLIENTS_PATH.exists()


def test_pipeline_generates_expected_outputs():
    """Validate that the full pipeline generates expected output files."""
    run_pipeline_once()

    expected_outputs = [
        CLEANED_LEADS_PATH,
        CLEANED_CLIENTS_PATH,
        MATCH_RESULTS_PATH,
        EXCEPTION_QUEUE_PATH,
        SUMMARY_PATH,
    ]

    for path in expected_outputs:
        assert path.exists(), f"Missing expected output: {path}"


def test_cleaned_leads_required_columns():
    """Validate cleaned lead output structure."""
    run_pipeline_once()

    df = pd.read_csv(CLEANED_LEADS_PATH)

    required_columns = {
        "lead_id",
        "lead_created_date",
        "lead_source_clean",
        "source_category_clean",
        "contact_name_clean",
        "contact_email_clean",
        "contact_phone_clean",
        "property_city_clean",
        "property_type_clean",
        "estimated_units",
        "units_bucket",
        "lead_status",
        "duplicate_flag",
        "email_valid_flag",
        "phone_valid_flag",
        "qa_status",
        "qa_notes",
    }

    assert required_columns.issubset(set(df.columns))


def test_cleaned_client_records_required_columns():
    """Validate cleaned client-style output structure."""
    run_pipeline_once()

    df = pd.read_csv(CLEANED_CLIENTS_PATH)

    required_columns = {
        "client_id",
        "client_name_clean",
        "client_email_clean",
        "client_phone_clean",
        "property_city_clean",
        "property_type_clean",
        "managed_units",
        "units_bucket",
        "client_status_clean",
        "record_source",
        "duplicate_flag",
        "email_valid_flag",
        "phone_valid_flag",
        "qa_status",
        "qa_notes",
    }

    assert required_columns.issubset(set(df.columns))


def test_match_results_required_columns():
    """Validate match result output structure."""
    run_pipeline_once()

    df = pd.read_csv(MATCH_RESULTS_PATH)

    required_columns = {
        "lead_id",
        "client_id",
        "match_status",
        "match_confidence",
        "email_match",
        "phone_match",
        "name_similarity_score",
        "city_match",
        "property_type_match",
        "units_bucket_match",
        "recommended_action",
        "qa_status",
        "qa_notes",
    }

    assert required_columns.issubset(set(df.columns))


def test_approved_match_status_values():
    """Validate match status values."""
    run_pipeline_once()

    df = pd.read_csv(MATCH_RESULTS_PATH)

    approved_statuses = {
        "High Confidence Match",
        "Medium Confidence Match",
        "Low Confidence Match",
        "No Match",
        "Exception",
    }

    assert set(df["match_status"]).issubset(approved_statuses)


def test_approved_qa_status_values():
    """Validate QA status values."""
    run_pipeline_once()

    df = pd.read_csv(MATCH_RESULTS_PATH)

    approved_statuses = {"PASS", "REVIEW", "FAIL"}

    assert set(df["qa_status"]).issubset(approved_statuses)


def test_summary_reconciles_with_match_results():
    """Validate that summary totals reconcile with match output."""
    run_pipeline_once()

    matches = pd.read_csv(MATCH_RESULTS_PATH)
    summary = pd.read_csv(SUMMARY_PATH).iloc[0]

    assert int(summary["total_leads"]) == len(matches)

    expected_high = int((matches["match_status"] == "High Confidence Match").sum())
    expected_medium = int((matches["match_status"] == "Medium Confidence Match").sum())
    expected_low = int((matches["match_status"] == "Low Confidence Match").sum())
    expected_no_match = int((matches["match_status"] == "No Match").sum())
    expected_exception = int((matches["match_status"] == "Exception").sum())

    assert int(summary["high_confidence_matches"]) == expected_high
    assert int(summary["medium_confidence_matches"]) == expected_medium
    assert int(summary["low_confidence_matches"]) == expected_low
    assert int(summary["no_match_records"]) == expected_no_match
    assert int(summary["exception_records"]) == expected_exception
