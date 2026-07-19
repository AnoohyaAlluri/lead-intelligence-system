# 🧠 Lead Intelligence System

![Python](https://img.shields.io/badge/Python-Data%20Pipeline-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Cleaning-green)
![QA](https://img.shields.io/badge/QA-Validation-orange)
![Status](https://img.shields.io/badge/Status-Portfolio%20Ready-brightgreen)
![Data](https://img.shields.io/badge/Data-Synthetic%20Only-lightgrey)

A public-safe synthetic lead intelligence system for marketing analytics, CRM-style data validation, match-confidence scoring, exception routing, and analytics-ready reporting.

This project demonstrates how fragmented marketing lead records can be cleaned, standardized, compared with client-style records, routed through QA review, and converted into structured reporting outputs for growth operations.

> **Data privacy:** This repository uses synthetic data only. It does not contain confidential company data, client records, owner or tenant information, property addresses, emails, phone numbers, CRM exports, internal spreadsheets, Gmail content, or private company files.

---

## 👤 Recruiter Summary

I designed a synthetic lead intelligence workflow that transforms messy lead-management data into a structured data quality and verification system.

The pipeline:

- Cleans and standardizes marketing lead records
- Compares leads with synthetic client-style records
- Assigns match-confidence levels
- Routes uncertain records into an exception queue
- Applies QA validation rules
- Produces analytics-ready verification summaries

The project combines Python, pandas, CRM-style matching logic, exception handling, data governance, QA testing, and growth-operations reporting.

---

## 🧩 Portfolio Positioning

This project is positioned as a **technical marketing operations, CRM data quality, and growth analytics system**.

It demonstrates how a business-development workflow can be redesigned into a repeatable operating system with:

- Defined data layers
- Standardized cleaning rules
- Match-confidence scoring
- QA validation
- Exception queue routing
- Analytics-ready reporting
- Public-safe documentation

---

## 📊 Synthetic Output Metrics

![Lead Intelligence Synthetic KPI Summary](images/lead-intelligence-synthetic-kpi-summary%20%282%29.png)

The pipeline generates completed synthetic output files from mock marketing lead and client-style records.

| Metric | Synthetic Output |
|---|---:|
| Synthetic marketing lead records | 25 |
| Synthetic client-style records | 45 |
| High-confidence matches | 17 |
| Medium-confidence matches | 0 |
| Low-confidence matches | 0 |
| No-match records | 1 |
| Exception queue records | 7 |
| Duplicate leads flagged | 2 |
| Invalid email records | 1 |
| Invalid phone records | 2 |
| QA pass records | 17 |
| QA review records | 8 |
| QA fail records | 0 |
| Verified match rate | 68.0% |
| Exception review rate | 28.0% |
| QA pass rate | 68.0% |

These metrics are based on synthetic data only. They demonstrate pipeline design, QA logic, exception routing, and analytics-ready reporting. They are not company or client performance metrics.

---

## ✨ Project Highlights

- Designed a medallion-style workflow using Bronze, Silver, Gold, and Analytics layers
- Built synthetic raw marketing lead and client-style datasets
- Implemented data cleaning and standardization with Python and pandas
- Created CRM-style match-confidence logic
- Added QA rules for missing fields, invalid emails, invalid phones, duplicates, and conflicting records
- Designed an exception queue that separates uncertain records instead of forcing unsupported matches
- Generated analytics outputs for match status, QA status, exception counts, and verification readiness
- Added automated tests for output structure, approved status values, and summary reconciliation
- Kept all datasets, examples, and documentation public-safe

---

## 📈 Business Value

This project demonstrates how a manual lead-verification workflow can be converted into a repeatable data and analytics system.

The pipeline is designed to:

- Convert raw marketing leads into standardized records
- Reduce unnecessary manual review through structured validation
- Separate verified records from uncertain records
- Prevent unsupported matching assumptions
- Identify incomplete, duplicate, or conflicting records
- Support cleaner attribution and source-quality analysis
- Make lead-verification status easier to report

The core value is not only lead tracking. It is the creation of a cleaner operating system for growth operations, marketing analytics, CRM data quality, and client verification.

---

## 🎯 Project Objective

The objective is to demonstrate how an unstructured lead-management workflow can be transformed into a repeatable lead intelligence system.

```text
Raw marketing lead records
↓
Cleaned and standardized lead data
↓
Client-style record comparison
↓
Match-confidence scoring
↓
Exception queue routing
↓
QA validation
↓
Analytics-ready reporting
```

---

## 💼 Business Problem

Marketing and business-development teams often collect leads from multiple sources, but those records may be incomplete, inconsistent, duplicated, or difficult to connect with verified client outcomes.

Common problems include:

- Inconsistent lead-source names
- Missing or invalid contact information
- Duplicate lead records
- Incomplete property or client-profile fields
- Unclear conversion status
- Weak connections between marketing leads and client records
- No standardized exception queue
- Limited visibility into verified, uncertain, or unusable records

Without a structured workflow, teams risk inaccurate reporting, duplicate outreach, weak attribution, and unsupported assumptions.

---

## 👩‍💻 My Role

I structured this project as a public-safe reconstruction of a real growth-operations workflow.

Responsibilities represented in this project include:

- Designing the lead intelligence workflow
- Defining synthetic marketing lead and client-style datasets
- Structuring cleaning and standardization rules
- Creating match-confidence logic
- Designing exception categories
- Implementing QA validation checks
- Creating analytics-ready output structures
- Documenting the system using synthetic data only

---

## 🏗️ Data Architecture

![Lead Intelligence System Architecture](images/lead-intelligence-system-architecture.png)

| Layer | Folder | Purpose |
|---|---|---|
| 🥉 Bronze | `datasets/raw/` | Synthetic raw marketing leads and client-style records |
| 🥈 Silver | `datasets/cleaned/` | Cleaned and standardized records |
| 🥇 Gold | `outputs/` | Match results and exception queue outputs |
| 📊 Analytics | `datasets/analytics/` | Lead-verification summary metrics |

---

## 🔄 Pipeline Workflow

### 1. Bronze Layer: Raw Data

The Bronze layer stores synthetic marketing lead and client-style records before cleaning.

Example marketing lead fields:

- `lead_id`
- `lead_created_date`
- `lead_source`
- `source_category`
- `contact_name`
- `contact_email`
- `contact_phone`
- `property_city`
- `property_type`
- `estimated_units`
- `lead_status`

Example client-style fields:

- `client_id`
- `client_name`
- `client_email`
- `client_phone`
- `property_city`
- `property_type`
- `managed_units`
- `client_status`

### 2. Silver Layer: Cleaned Records

The Silver layer standardizes fields and prepares records for matching.

Cleaning steps include:

- Standardizing column names
- Cleaning contact names
- Normalizing phone numbers
- Validating email formats
- Standardizing city names
- Standardizing property-type values
- Creating unit buckets
- Flagging missing contact fields
- Flagging duplicate records
- Assigning preliminary QA status

Generated files:

- `datasets/cleaned/cleaned_marketing_leads.csv`
- `datasets/cleaned/cleaned_client_records.csv`

### 3. Gold Layer: Match Results and Exception Queue

The Gold layer creates verification-ready outputs.

Match-result fields include:

- `lead_id`
- `client_id`
- `match_status`
- `match_confidence`
- `email_match`
- `phone_match`
- `name_similarity_score`
- `city_match`
- `property_type_match`
- `units_bucket_match`
- `recommended_action`
- `qa_status`
- `qa_notes`

Exception-queue fields include:

- `exception_id`
- `lead_id`
- `exception_type`
- `match_issue`
- `review_priority`
- `recommended_next_step`
- `qa_status`
- `public_safe_notes`

Generated files:

- `outputs/client_match_results_mock.csv`
- `outputs/exception_queue_mock.csv`

### 4. Analytics Layer: Verification Reporting

The Analytics layer summarizes match quality, QA status, and review readiness.

Metrics include:

- Total leads
- Total client-style records
- High-, medium-, and low-confidence matches
- No-match records
- Exception queue records
- Duplicate leads flagged
- Invalid email and phone records
- QA pass, review, and fail counts
- Verified match rate
- Exception review rate
- QA pass rate

Generated files:

- `datasets/analytics/raw_data_profile_mock.csv`
- `datasets/analytics/lead_verification_summary_mock.csv`

---

## 🧠 Match-Confidence Logic

| Match Status | Description |
|---|---|
| High Confidence Match | Strong match signals exist across contact or profile fields |
| Medium Confidence Match | Partial match signals exist, but review is recommended |
| Low Confidence Match | Weak match signals exist and manual verification is required |
| No Match | No reliable matching signals were found |
| Exception | Conflicting or incomplete information requires structured review |

### Example rules

**High-confidence match**

- Email match or phone match
- City match
- Property-type alignment
- Unit-bucket alignment
- No conflicting client status
- No major QA issue

**Medium-confidence match**

- Name-similarity match
- City match
- Partial property-type or unit-bucket alignment
- Manual review recommended before applying the match

**Low-confidence match**

- Weak name similarity only
- Missing email or phone
- Conflicting city, property-type, or unit information

**Exception**

- A possible match exists, but the record requires human review before classification

---

## 🧪 QA and Exception Handling

The project includes QA logic for:

- Missing lead IDs
- Missing source values
- Missing or invalid emails
- Missing or invalid phone numbers
- Duplicate lead records
- Conflicting match signals
- Incomplete client-style records
- Records requiring manual review

Exception categories include:

- Duplicate Review
- Missing Contact Review
- Conflicting Status Review
- Source Attribution Review
- Client/Profile Review
- Better Export Needed
- No Reliable Match Found

### Core QA principle

```text
Do not force a match when the data is incomplete, conflicting, or unsupported.
```

---

## 🧾 Generated Output Files

| File | Purpose |
|---|---|
| `datasets/analytics/raw_data_profile_mock.csv` | Profiles synthetic raw input files |
| `datasets/cleaned/cleaned_marketing_leads.csv` | Cleaned synthetic marketing leads |
| `datasets/cleaned/cleaned_client_records.csv` | Cleaned synthetic client-style records |
| `outputs/client_match_results_mock.csv` | Match-confidence results |
| `outputs/exception_queue_mock.csv` | Records routed to manual review |
| `datasets/analytics/lead_verification_summary_mock.csv` | Final synthetic verification summary |

---

## ▶️ How to Run the Pipeline

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the complete pipeline:

```bash
python run_pipeline.py
```

Run automated tests:

```bash
pytest
```

---

## 📂 Repository Structure

```text
lead-intelligence-system/
├── datasets/
│   ├── raw/
│   ├── cleaned/
│   └── analytics/
├── docs/
├── scripts/
│   ├── bronze/
│   ├── silver/
│   ├── gold/
│   └── analytics/
├── tests/
├── images/
├── outputs/
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
└── run_pipeline.py
```

---

## 🛠️ Tools and Methods

- Python
- pandas
- CSV-based data workflows
- CRM-style record matching
- Match-confidence scoring
- QA validation
- Exception handling
- Data governance
- Marketing analytics reporting
- GitHub documentation

---

## 🎯 Role Alignment

This project supports roles such as:

- Marketing Analytics Engineer
- Marketing Technology Analyst
- Growth Operations Analyst
- Marketing Operations Analyst
- Revenue Operations Analyst
- CRM Data Analyst
- Data Analyst
- Technical Marketing Analyst
- AI and Data Workflow Builder

---

## 🧠 Skills Demonstrated

- Data cleaning and standardization
- Data validation
- Lead intelligence system design
- CRM-style matching logic
- Match-confidence scoring
- Exception queue routing
- QA rule design
- Synthetic data modeling
- Growth-operations reporting
- Data governance
- Public-safe portfolio documentation
- Python pipeline design
- Analytics-ready output generation

---

## 🔒 Confidentiality Notice

This repository is a public-safe reconstruction of a real growth-operations workflow.

It does not include:

- Real company data
- Real client records
- Real owner or tenant names
- Real property addresses
- Real emails or phone numbers
- Real CRM, AppFolio, or LeadSimple exports
- Internal Google Sheets
- Internal email messages
- Internal dashboard screenshots
- Internal execution logs
- Raw Drive documents
- Any confidential company information

All records, examples, files, and outputs are synthetic or generalized for portfolio demonstration.

---

## ✅ Project Status

**Portfolio-ready**

Completed components:

- Synthetic raw marketing lead dataset
- Synthetic client-style dataset
- Bronze raw-data profiling script
- Silver data-cleaning script
- Gold match-results and exception-queue script
- Analytics verification-summary script
- Generated synthetic output files
- QA validation tests
- Public-safe architecture diagram
- Public-safe KPI summary visual
- Public-safe documentation and case study

Planned enhancements:

- Interactive Streamlit dashboard
- Source-quality analysis
- Match-confidence distribution charts
- Automated GitHub Actions workflow
- Additional unit and integration tests

---

## 🌱 About This Project

This project demonstrates how marketing operations work can be structured as a technical data system.

Growth work is not limited to campaign execution. It can also include data architecture, QA logic, record matching, exception handling, reporting workflows, automation planning, and business-development systems.
