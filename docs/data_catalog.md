# Data Catalog

This document defines the synthetic datasets used in the Lead Intelligence System.

All data in this repository is synthetic and public-safe. No real company, client, owner, tenant, property, contact, CRM, AppFolio, LeadSimple, Gmail, Google Sheets, or internal system data is included.

---

## Dataset Overview

| Dataset | Location | Purpose |
|---|---|---|
| Raw marketing leads | `datasets/raw/raw_marketing_leads_mock.csv` | Synthetic inbound and outbound marketing lead records before cleaning |
| Raw client-style records | `datasets/raw/raw_client_records_mock.csv` | Synthetic client-style records used for public-safe matching logic |
| Cleaned marketing leads | `datasets/cleaned/cleaned_marketing_leads.csv` | Planned cleaned version of marketing lead data |
| Cleaned client-style records | `datasets/cleaned/cleaned_client_records.csv` | Planned cleaned version of client-style records |
| Match results | `outputs/client_match_results_mock.csv` | Planned output showing match confidence and recommended action |
| Exception queue | `outputs/exception_queue_mock.csv` | Planned output for records requiring manual review |
| Verification summary | `datasets/analytics/lead_verification_summary_mock.csv` | Planned analytics summary for QA and match-confidence reporting |

---

## Raw Marketing Leads

**File:** `datasets/raw/raw_marketing_leads_mock.csv`

This dataset represents raw marketing lead records collected from multiple synthetic lead sources.

| Field | Description |
|---|---|
| `lead_id` | Synthetic unique lead identifier |
| `lead_created_date` | Date the lead was created |
| `lead_source` | Original lead source label |
| `source_category` | Broader source grouping such as paid search, referral, SEO, or offline campaign |
| `contact_name` | Synthetic lead contact name |
| `contact_email` | Synthetic email address |
| `contact_phone` | Synthetic phone number |
| `property_city` | General city or market associated with the lead |
| `property_type` | Property type category |
| `estimated_units` | Estimated number of units tied to the lead |
| `lead_status` | Current synthetic lead status |
| `notes_raw` | Public-safe notes describing data quality or lead context |

### Example Data Quality Issues

The raw lead file intentionally includes sample issues for QA testing:

- Duplicate lead records
- Missing contact names
- Missing phone numbers
- Invalid email format
- Invalid phone format
- Unknown lead source
- Records requiring manual review

---

## Raw Client-Style Records

**File:** `datasets/raw/raw_client_records_mock.csv`

This dataset represents synthetic client-style records used to test public-safe matching logic.

| Field | Description |
|---|---|
| `client_id` | Synthetic unique client-style record identifier |
| `client_name` | Synthetic client-style name |
| `client_email` | Synthetic email address |
| `client_phone` | Synthetic phone number |
| `property_city` | General city or market associated with the record |
| `property_type` | Property type category |
| `managed_units` | Synthetic unit count associated with the record |
| `client_status` | Synthetic client-style status |
| `record_source` | Public-safe source label for the client-style dataset |

### Example Record Status Values

| Status | Meaning |
|---|---|
| `Active` | Strong client-style record |
| `Prospect` | Potential client-style record |
| `Inactive` | Historical or inactive record |
| `Review` | Record requires review |
| `Duplicate Review` | Possible duplicate record requiring validation |

---

## Planned Cleaned Marketing Leads

**File:** `datasets/cleaned/cleaned_marketing_leads.csv`

This planned dataset will contain standardized lead records after cleaning.

Expected fields:

| Field | Description |
|---|---|
| `lead_id` | Synthetic lead identifier |
| `lead_created_date` | Parsed lead creation date |
| `lead_source_clean` | Standardized lead source |
| `source_category_clean` | Standardized source category |
| `contact_name_clean` | Cleaned contact name |
| `contact_email_clean` | Lowercase and trimmed email |
| `contact_phone_clean` | Normalized phone number |
| `property_city_clean` | Standardized city name |
| `property_type_clean` | Standardized property type |
| `units_bucket` | Unit count category |
| `duplicate_flag` | Indicates whether the lead appears duplicated |
| `email_valid_flag` | Indicates whether email format is valid |
| `phone_valid_flag` | Indicates whether phone format is valid |
| `qa_status` | PASS, REVIEW, or FAIL |
| `qa_notes` | Public-safe explanation of QA result |

---

## Planned Cleaned Client-Style Records

**File:** `datasets/cleaned/cleaned_client_records.csv`

This planned dataset will contain standardized client-style records after cleaning.

Expected fields:

| Field | Description |
|---|---|
| `client_id` | Synthetic client-style record identifier |
| `client_name_clean` | Cleaned client-style name |
| `client_email_clean` | Lowercase and trimmed email |
| `client_phone_clean` | Normalized phone number |
| `property_city_clean` | Standardized city name |
| `property_type_clean` | Standardized property type |
| `units_bucket` | Unit count category |
| `client_status_clean` | Standardized client-style status |
| `qa_status` | PASS, REVIEW, or FAIL |
| `qa_notes` | Public-safe explanation of QA result |

---

## Planned Match Results

**File:** `outputs/client_match_results_mock.csv`

This planned output will compare cleaned marketing leads against cleaned client-style records.

Expected fields:

| Field | Description |
|---|---|
| `lead_id` | Synthetic lead identifier |
| `client_id` | Synthetic client-style record identifier |
| `match_status` | High Confidence Match, Medium Confidence Match, Low Confidence Match, No Match, or Exception |
| `match_confidence` | Numeric or categorical match-confidence score |
| `email_match` | Whether email matched |
| `phone_match` | Whether phone matched |
| `name_similarity_score` | Synthetic similarity score for name comparison |
| `city_match` | Whether city matched |
| `property_type_match` | Whether property type matched |
| `units_bucket_match` | Whether unit bucket matched |
| `recommended_action` | Suggested next action |
| `qa_status` | PASS, REVIEW, or FAIL |
| `qa_notes` | Public-safe explanation of match result |

---

## Planned Exception Queue

**File:** `outputs/exception_queue_mock.csv`

This planned output will hold records that should not be automatically classified.

Expected fields:

| Field | Description |
|---|---|
| `exception_id` | Synthetic exception identifier |
| `lead_id` | Related synthetic lead identifier |
| `exception_type` | Category of issue requiring review |
| `match_issue` | Public-safe explanation of the match problem |
| `review_priority` | High, Medium, or Low review priority |
| `recommended_next_step` | Suggested manual review action |
| `qa_status` | REVIEW or FAIL |
| `public_safe_notes` | Notes that do not expose sensitive information |

---

## Planned Verification Summary

**File:** `datasets/analytics/lead_verification_summary_mock.csv`

This planned output will summarize lead verification quality.

Expected metrics:

| Metric | Description |
|---|---|
| `total_leads` | Total number of synthetic lead records |
| `total_client_records` | Total number of synthetic client-style records |
| `high_confidence_matches` | Count of high-confidence matches |
| `medium_confidence_matches` | Count of medium-confidence matches |
| `low_confidence_matches` | Count of low-confidence matches |
| `no_match_records` | Count of records with no reliable match |
| `exception_queue_records` | Count of records routed to exception review |
| `duplicate_leads_flagged` | Count of duplicate lead records |
| `qa_pass_count` | Count of records passing QA |
| `qa_review_count` | Count of records requiring review |
| `qa_fail_count` | Count of records failing QA |

---

## Confidentiality Rule

This data catalog describes synthetic public-safe files only.

Do not add:

- Real client records
- Real owner records
- Real tenant records
- Real property addresses
- Real emails
- Real phone numbers
- Real CRM exports
- Real AppFolio exports
- Real LeadSimple exports
- Internal spreadsheets
- Gmail content
- Drive documents
- Private dashboard screenshots
- Company-specific confidential metrics
