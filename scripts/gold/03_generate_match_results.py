"""
Gold Layer Script: Generate Match Results and Exception Queue

This script compares cleaned synthetic marketing leads against cleaned
synthetic client-style records.

Public-safe rule:
This script is designed for synthetic data only.
Do not use it with real company, client, owner, tenant, property,
email, phone, CRM, AppFolio, LeadSimple, Gmail, or internal system data.
"""

from pathlib import Path
from difflib import SequenceMatcher
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]

CLEANED_LEADS_PATH = BASE_DIR / "datasets" / "cleaned" / "cleaned_marketing_leads.csv"
CLEANED_CLIENTS_PATH = BASE_DIR / "datasets" / "cleaned" / "cleaned_client_records.csv"

MATCH_RESULTS_PATH = BASE_DIR / "outputs" / "client_match_results_mock.csv"
EXCEPTION_QUEUE_PATH = BASE_DIR / "outputs" / "exception_queue_mock.csv"


def similarity_score(left_value: str, right_value: str) -> float:
    """Return a simple name similarity score from 0 to 100."""
    left = str(left_value or "").strip().lower()
    right = str(right_value or "").strip().lower()

    if not left or not right:
        return 0.0

    return round(SequenceMatcher(None, left, right).ratio() * 100, 2)


def score_match(lead: pd.Series, client: pd.Series) -> dict:
    """Score one synthetic lead against one synthetic client-style record."""
    email_match = (
        lead["contact_email_clean"] != ""
        and lead["contact_email_clean"] == client["client_email_clean"]
    )

    phone_match = (
        lead["contact_phone_clean"] != ""
        and lead["contact_phone_clean"] == client["client_phone_clean"]
    )

    name_score = similarity_score(
        lead["contact_name_clean"],
        client["client_name_clean"],
    )

    city_match = lead["property_city_clean"] == client["property_city_clean"]
    property_type_match = lead["property_type_clean"] == client["property_type_clean"]
    units_bucket_match = lead["units_bucket"] == client["units_bucket"]

    score = 0

    if email_match:
        score += 40

    if phone_match:
        score += 35

    if name_score >= 90:
        score += 15
    elif name_score >= 75:
        score += 10
    elif name_score >= 60:
        score += 5

    if city_match:
        score += 5

    if property_type_match:
        score += 3

    if units_bucket_match:
        score += 2

    return {
        "client_id": client["client_id"],
        "match_confidence": score,
        "email_match": email_match,
        "phone_match": phone_match,
        "name_similarity_score": name_score,
        "city_match": city_match,
        "property_type_match": property_type_match,
        "units_bucket_match": units_bucket_match,
        "client_status_clean": client["client_status_clean"],
        "client_duplicate_flag": client["duplicate_flag"],
        "client_qa_status": client["qa_status"],
    }


def detect_conflict(lead: pd.Series, best_match: dict) -> bool:
    """Detect whether a match should be routed to exception review."""
    if lead["qa_status"] != "PASS":
        return True

    if best_match["client_qa_status"] != "PASS":
        return True

    if bool(lead["duplicate_flag"]):
        return True

    if bool(best_match["client_duplicate_flag"]):
        return True

    if best_match["client_status_clean"] in ["Review", "Duplicate Review"]:
        return True

    return False


def classify_match(score: int, conflict_detected: bool) -> tuple[str, str, str]:
    """Classify match status, QA status, and recommended action."""
    if conflict_detected and score >= 30:
        return (
            "Exception",
            "REVIEW",
            "Route to exception queue before applying match",
        )

    if score >= 80:
        return (
            "High Confidence Match",
            "PASS",
            "Include in verified reporting",
        )

    if score >= 55:
        return (
            "Medium Confidence Match",
            "REVIEW",
            "Review before applying match",
        )

    if score >= 30:
        return (
            "Low Confidence Match",
            "REVIEW",
            "Hold for manual verification",
        )

    return (
        "No Match",
        "REVIEW",
        "Keep unmatched until stronger evidence is available",
    )


def identify_exception_type(lead: pd.Series, match_row: dict) -> str:
    """Assign a public-safe exception type."""
    qa_notes = str(lead.get("qa_notes", "")).lower()

    if "duplicate" in qa_notes or bool(lead.get("duplicate_flag", False)):
        return "Duplicate Review"

    if "email" in qa_notes or "phone" in qa_notes or "name" in qa_notes:
        return "Missing Contact Review"

    if "unknown or missing source" in qa_notes:
        return "Source Attribution Review"

    if match_row.get("client_status_clean") in ["Review", "Duplicate Review"]:
        return "Conflicting Status Review"

    if match_row.get("match_confidence", 0) < 55:
        return "No Reliable Match Found"

    return "Client/Profile Review"


def assign_review_priority(exception_type: str, score: int) -> str:
    """Assign exception review priority."""
    if exception_type in ["Conflicting Status Review", "Client/Profile Review"] and score >= 55:
        return "High"

    if exception_type in ["Duplicate Review", "Missing Contact Review"]:
        return "Medium"

    return "Low"


def build_match_results() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Build match results and exception queue from cleaned synthetic datasets."""
    leads = pd.read_csv(CLEANED_LEADS_PATH)
    clients = pd.read_csv(CLEANED_CLIENTS_PATH)

    match_rows = []
    exception_rows = []

    for _, lead in leads.iterrows():
        scored_clients = [score_match(lead, client) for _, client in clients.iterrows()]
        best_match = max(scored_clients, key=lambda row: row["match_confidence"])

        conflict_detected = detect_conflict(lead, best_match)
        match_status, qa_status, recommended_action = classify_match(
            score=best_match["match_confidence"],
            conflict_detected=conflict_detected,
        )

        match_row = {
            "lead_id": lead["lead_id"],
            "client_id": best_match["client_id"] if best_match["match_confidence"] > 0 else "",
            "match_status": match_status,
            "match_confidence": best_match["match_confidence"],
            "email_match": best_match["email_match"],
            "phone_match": best_match["phone_match"],
            "name_similarity_score": best_match["name_similarity_score"],
            "city_match": best_match["city_match"],
            "property_type_match": best_match["property_type_match"],
            "units_bucket_match": best_match["units_bucket_match"],
            "recommended_action": recommended_action,
            "qa_status": qa_status,
            "qa_notes": lead["qa_notes"],
        }

        match_rows.append(match_row)

        if match_status == "Exception":
            exception_type = identify_exception_type(lead, best_match)
            review_priority = assign_review_priority(
                exception_type=exception_type,
                score=best_match["match_confidence"],
            )

            exception_rows.append(
                {
                    "exception_id": f"EX-{len(exception_rows) + 1:04d}",
                    "lead_id": lead["lead_id"],
                    "exception_type": exception_type,
                    "match_issue": lead["qa_notes"],
                    "review_priority": review_priority,
                    "recommended_next_step": recommended_action,
                    "qa_status": "REVIEW",
                    "public_safe_notes": "Synthetic record requires review before classification",
                }
            )

    return pd.DataFrame(match_rows), pd.DataFrame(exception_rows)


def main() -> None:
    """Run Gold match-results workflow."""
    MATCH_RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    EXCEPTION_QUEUE_PATH.parent.mkdir(parents=True, exist_ok=True)

    match_results, exception_queue = build_match_results()

    match_results.to_csv(MATCH_RESULTS_PATH, index=False)
    exception_queue.to_csv(EXCEPTION_QUEUE_PATH, index=False)

    print("Gold matching complete.")
    print(f"Match results written to: {MATCH_RESULTS_PATH}")
    print(f"Exception queue written to: {EXCEPTION_QUEUE_PATH}")


if __name__ == "__main__":
    main()
