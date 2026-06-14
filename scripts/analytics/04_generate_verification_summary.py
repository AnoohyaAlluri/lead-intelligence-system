"""
Analytics Layer Script: Generate Verification Summary

This script summarizes synthetic lead verification outputs from the
Lead Intelligence System.

Public-safe rule:
This script is designed for synthetic data only.
Do not use it with real company, client, owner, tenant, property,
email, phone, CRM, AppFolio, LeadSimple, Gmail, or internal system data.
"""

from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]

CLEANED_LEADS_PATH = BASE_DIR / "datasets" / "cleaned" / "cleaned_marketing_leads.csv"
CLEANED_CLIENTS_PATH = BASE_DIR / "datasets" / "cleaned" / "cleaned_client_records.csv"
MATCH_RESULTS_PATH = BASE_DIR / "outputs" / "client_match_results_mock.csv"
EXCEPTION_QUEUE_PATH = BASE_DIR / "outputs" / "exception_queue_mock.csv"

SUMMARY_OUTPUT_PATH = BASE_DIR / "datasets" / "analytics" / "lead_verification_summary_mock.csv"


def safe_count_by_value(df: pd.DataFrame, column_name: str, value: str) -> int:
    """Return count of rows where a column equals a specific value."""
    if column_name not in df.columns:
        return 0

    return int((df[column_name] == value).sum())


def safe_count_boolean_true(df: pd.DataFrame, column_name: str) -> int:
    """Return count of True values in a boolean-like column."""
    if column_name not in df.columns:
        return 0

    return int(df[column_name].astype(str).str.lower().isin(["true", "1", "yes"]).sum())


def calculate_rate(numerator: int, denominator: int) -> float:
    """Calculate percentage rate safely."""
    if denominator == 0:
        return 0.0

    return round((numerator / denominator) * 100, 2)


def build_summary() -> pd.DataFrame:
    """Build a one-row analytics summary from synthetic output files."""
    leads = pd.read_csv(CLEANED_LEADS_PATH)
    clients = pd.read_csv(CLEANED_CLIENTS_PATH)
    matches = pd.read_csv(MATCH_RESULTS_PATH)

    if EXCEPTION_QUEUE_PATH.exists():
        exceptions = pd.read_csv(EXCEPTION_QUEUE_PATH)
    else:
        exceptions = pd.DataFrame()

    total_leads = len(leads)
    total_client_records = len(clients)

    high_confidence_matches = safe_count_by_value(
        matches,
        "match_status",
        "High Confidence Match",
    )

    medium_confidence_matches = safe_count_by_value(
        matches,
        "match_status",
        "Medium Confidence Match",
    )

    low_confidence_matches = safe_count_by_value(
        matches,
        "match_status",
        "Low Confidence Match",
    )

    no_match_records = safe_count_by_value(
        matches,
        "match_status",
        "No Match",
    )

    exception_records = safe_count_by_value(
        matches,
        "match_status",
        "Exception",
    )

    qa_pass_count = safe_count_by_value(matches, "qa_status", "PASS")
    qa_review_count = safe_count_by_value(matches, "qa_status", "REVIEW")
    qa_fail_count = safe_count_by_value(matches, "qa_status", "FAIL")

    duplicate_leads_flagged = safe_count_boolean_true(leads, "duplicate_flag")
    invalid_email_count = int((leads["email_valid_flag"] == False).sum())
    invalid_phone_count = int((leads["phone_valid_flag"] == False).sum())

    summary = {
        "total_leads": total_leads,
        "total_client_records": total_client_records,
        "high_confidence_matches": high_confidence_matches,
        "medium_confidence_matches": medium_confidence_matches,
        "low_confidence_matches": low_confidence_matches,
        "no_match_records": no_match_records,
        "exception_records": exception_records,
        "exception_queue_records": len(exceptions),
        "duplicate_leads_flagged": duplicate_leads_flagged,
        "invalid_email_count": invalid_email_count,
        "invalid_phone_count": invalid_phone_count,
        "qa_pass_count": qa_pass_count,
        "qa_review_count": qa_review_count,
        "qa_fail_count": qa_fail_count,
        "verified_match_rate": calculate_rate(high_confidence_matches, total_leads),
        "exception_review_rate": calculate_rate(exception_records, total_leads),
        "qa_pass_rate": calculate_rate(qa_pass_count, total_leads),
    }

    return pd.DataFrame([summary])


def main() -> None:
    """Run Analytics summary workflow."""
    SUMMARY_OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    summary_df = build_summary()
    summary_df.to_csv(SUMMARY_OUTPUT_PATH, index=False)

    print("Analytics summary complete.")
    print(f"Summary written to: {SUMMARY_OUTPUT_PATH}")


if __name__ == "__main__":
    main()
