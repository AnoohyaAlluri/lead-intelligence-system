"""
Bronze Layer Script: Raw Data Profiling

This script profiles the synthetic raw input datasets used in the
Lead Intelligence System.

Public-safe rule:
This script is designed for synthetic data only.
Do not use it with real company, client, owner, tenant, property,
email, phone, CRM, AppFolio, LeadSimple, Gmail, or internal system data.
"""

from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]

RAW_LEADS_PATH = BASE_DIR / "datasets" / "raw" / "raw_marketing_leads_mock.csv"
RAW_CLIENTS_PATH = BASE_DIR / "datasets" / "raw" / "raw_client_records_mock.csv"
OUTPUT_PATH = BASE_DIR / "datasets" / "analytics" / "raw_data_profile_mock.csv"


def profile_dataset(file_path: Path, dataset_name: str, id_column: str) -> dict:
    """
    Create a simple public-safe profile for one synthetic dataset.
    """

    if not file_path.exists():
        raise FileNotFoundError(f"Missing input file: {file_path}")

    df = pd.read_csv(file_path)

    total_rows = len(df)
    total_columns = len(df.columns)

    missing_value_count = int(df.isna().sum().sum())
    duplicate_id_count = int(df[id_column].duplicated().sum()) if id_column in df.columns else 0

    blank_required_id_count = 0
    if id_column in df.columns:
        blank_required_id_count = int(df[id_column].isna().sum() + (df[id_column].astype(str).str.strip() == "").sum())

    return {
        "dataset_name": dataset_name,
        "file_name": file_path.name,
        "total_rows": total_rows,
        "total_columns": total_columns,
        "missing_value_count": missing_value_count,
        "duplicate_id_count": duplicate_id_count,
        "blank_required_id_count": blank_required_id_count,
    }


def main() -> None:
    """
    Profile synthetic raw files and export a summary CSV.
    """

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    profiles = [
        profile_dataset(
            file_path=RAW_LEADS_PATH,
            dataset_name="raw_marketing_leads",
            id_column="lead_id",
        ),
        profile_dataset(
            file_path=RAW_CLIENTS_PATH,
            dataset_name="raw_client_records",
            id_column="client_id",
        ),
    ]

    profile_df = pd.DataFrame(profiles)
    profile_df.to_csv(OUTPUT_PATH, index=False)

    print("Bronze profiling complete.")
    print(f"Output written to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
