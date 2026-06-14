"""
Silver Layer Script: Clean and Standardize Records

This script cleans the synthetic raw marketing lead and client-style datasets
used in the Lead Intelligence System.

Public-safe rule:
This script is designed for synthetic data only.
Do not use it with real company, client, owner, tenant, property,
email, phone, CRM, AppFolio, LeadSimple, Gmail, or internal system data.
"""

from pathlib import Path
import re
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]

RAW_LEADS_PATH = BASE_DIR / "datasets" / "raw" / "raw_marketing_leads_mock.csv"
RAW_CLIENTS_PATH = BASE_DIR / "datasets" / "raw" / "raw_client_records_mock.csv"

CLEANED_LEADS_PATH = BASE_DIR / "datasets" / "cleaned" / "cleaned_marketing_leads.csv"
CLEANED_CLIENTS_PATH = BASE_DIR / "datasets" / "cleaned" / "cleaned_client_records.csv"


def clean_text(value):
    """Trim whitespace and convert blank values to empty strings."""
    if pd.isna(value):
        return ""
    return str(value).strip()


def clean_email(value):
    """Lowercase and trim email values."""
    return clean_text(value).lower()


def is_valid_email(value):
    """Basic email format validation for synthetic records."""
    email = clean_email(value)
    return bool(re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email))


def clean_phone(value):
    """Remove non-numeric characters from phone values."""
    if pd.isna(value):
        return ""
    return re.sub(r"\D", "", str(value))


def is_valid_phone(value):
    """Validate that a cleaned phone number has 10 digits."""
    phone = clean_phone(value)
    return len(phone) == 10


def standardize_city(value):
    """Standardize city values."""
    city = clean_text(value).title()
    city_map = {
        "La": "Los Angeles",
        "L.A.": "Los Angeles",
        "Los Angeles": "Los Angeles",
        "Santa Monica": "Santa Monica",
        "Beverly Hills": "Beverly Hills",
        "West Hollywood": "West Hollywood",
        "Culver City": "Culver City",
        "Brentwood": "Brentwood",
        "Malibu": "Malibu",
        "Venice": "Venice",
    }
    return city_map.get(city, city)


def standardize_property_type(value):
    """Standardize property type values."""
    property_type = clean_text(value).title()
    property_type_map = {
        "Apartment": "Apartment",
        "Apartments": "Apartment",
        "Condo": "Condo",
        "Condominium": "Condo",
        "Single Family": "Single Family",
        "Single-Family": "Single Family",
        "Sfr": "Single Family",
        "Multifamily": "Multifamily",
        "Multi Family": "Multifamily",
        "Multi-Family": "Multifamily",
    }
    return property_type_map.get(property_type, property_type)


def create_units_bucket(value):
    """Convert unit counts into reporting buckets."""
    try:
        units = int(value)
    except (TypeError, ValueError):
        return "Unknown"

    if units <= 1:
        return "1 Unit"
    if 2 <= units <= 4:
        return "2-4 Units"
    if 5 <= units <= 10:
        return "5-10 Units"
    if 11 <= units <= 20:
        return "11-20 Units"
    return "21+ Units"


def build_qa_status_and_notes(row, id_column, name_column, email_column, phone_column, source_column=None):
    """Assign public-safe QA status and notes."""
    notes = []

    if clean_text(row.get(id_column, "")) == "":
        notes.append("Missing required ID")

    if clean_text(row.get(name_column, "")) == "":
        notes.append("Missing name")

    if clean_text(row.get(email_column, "")) == "":
        notes.append("Missing email")
    elif not is_valid_email(row.get(email_column, "")):
        notes.append("Invalid email format")

    if clean_text(row.get(phone_column, "")) == "":
        notes.append("Missing phone")
    elif not is_valid_phone(row.get(phone_column, "")):
        notes.append("Invalid phone format")

    if source_column and clean_text(row.get(source_column, "")).lower() in ["", "unknown"]:
        notes.append("Unknown or missing source")

    if row.get("duplicate_flag", False):
        notes.append("Possible duplicate record")

    if "Missing required ID" in notes:
        return "FAIL", "; ".join(notes)

    if notes:
        return "REVIEW", "; ".join(notes)

    return "PASS", "Record passed basic QA checks"


def clean_marketing_leads() -> pd.DataFrame:
    """Clean the synthetic marketing lead dataset."""
    df = pd.read_csv(RAW_LEADS_PATH)

    df["lead_id"] = df["lead_id"].apply(clean_text)
    df["lead_source_clean"] = df["lead_source"].apply(clean_text)
    df["source_category_clean"] = df["source_category"].apply(clean_text)
    df["contact_name_clean"] = df["contact_name"].apply(clean_text)
    df["contact_email_clean"] = df["contact_email"].apply(clean_email)
    df["contact_phone_clean"] = df["contact_phone"].apply(clean_phone)
    df["property_city_clean"] = df["property_city"].apply(standardize_city)
    df["property_type_clean"] = df["property_type"].apply(standardize_property_type)
    df["units_bucket"] = df["estimated_units"].apply(create_units_bucket)

    df["email_valid_flag"] = df["contact_email"].apply(is_valid_email)
    df["phone_valid_flag"] = df["contact_phone"].apply(is_valid_phone)

    df["duplicate_flag"] = (
        df["contact_email_clean"].duplicated(keep=False)
        | df["contact_phone_clean"].duplicated(keep=False)
    )

    qa_results = df.apply(
        lambda row: build_qa_status_and_notes(
            row=row,
            id_column="lead_id",
            name_column="contact_name",
            email_column="contact_email",
            phone_column="contact_phone",
            source_column="lead_source",
        ),
        axis=1,
    )

    df["qa_status"] = [result[0] for result in qa_results]
    df["qa_notes"] = [result[1] for result in qa_results]

    cleaned_columns = [
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
    ]

    return df[cleaned_columns]


def clean_client_records() -> pd.DataFrame:
    """Clean the synthetic client-style record dataset."""
    df = pd.read_csv(RAW_CLIENTS_PATH)

    df["client_id"] = df["client_id"].apply(clean_text)
    df["client_name_clean"] = df["client_name"].apply(clean_text)
    df["client_email_clean"] = df["client_email"].apply(clean_email)
    df["client_phone_clean"] = df["client_phone"].apply(clean_phone)
    df["property_city_clean"] = df["property_city"].apply(standardize_city)
    df["property_type_clean"] = df["property_type"].apply(standardize_property_type)
    df["units_bucket"] = df["managed_units"].apply(create_units_bucket)
    df["client_status_clean"] = df["client_status"].apply(clean_text)

    df["email_valid_flag"] = df["client_email"].apply(is_valid_email)
    df["phone_valid_flag"] = df["client_phone"].apply(is_valid_phone)

    df["duplicate_flag"] = (
        df["client_email_clean"].duplicated(keep=False)
        | df["client_phone_clean"].duplicated(keep=False)
    )

    qa_results = df.apply(
        lambda row: build_qa_status_and_notes(
            row=row,
            id_column="client_id",
            name_column="client_name",
            email_column="client_email",
            phone_column="client_phone",
        ),
        axis=1,
    )

    df["qa_status"] = [result[0] for result in qa_results]
    df["qa_notes"] = [result[1] for result in qa_results]

    cleaned_columns = [
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
    ]

    return df[cleaned_columns]


def main() -> None:
    """Run Silver cleaning workflow."""
    CLEANED_LEADS_PATH.parent.mkdir(parents=True, exist_ok=True)
    CLEANED_CLIENTS_PATH.parent.mkdir(parents=True, exist_ok=True)

    cleaned_leads = clean_marketing_leads()
    cleaned_clients = clean_client_records()

    cleaned_leads.to_csv(CLEANED_LEADS_PATH, index=False)
    cleaned_clients.to_csv(CLEANED_CLIENTS_PATH, index=False)

    print("Silver cleaning complete.")
    print(f"Cleaned leads written to: {CLEANED_LEADS_PATH}")
    print(f"Cleaned client records written to: {CLEANED_CLIENTS_PATH}")


if __name__ == "__main__":
    main()
