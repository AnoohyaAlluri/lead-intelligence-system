# Matching Rules

This document explains the public-safe matching logic used in the Lead Intelligence System.

All matching logic in this repository uses synthetic data only. No real company, client, owner, tenant, property, CRM, AppFolio, LeadSimple, Gmail, Google Sheets, or internal system data is included.

---

## Purpose

The purpose of the matching workflow is to compare synthetic marketing lead records against synthetic client-style records and assign a match-confidence classification.

The system does not force uncertain matches. Records with incomplete, conflicting, or weak signals are routed into an exception queue for manual review.

---

## Matching Inputs

The matching workflow compares fields from two synthetic datasets:

| Dataset | Location |
|---|---|
| Raw marketing leads | `datasets/raw/raw_marketing_leads_mock.csv` |
| Raw client-style records | `datasets/raw/raw_client_records_mock.csv` |

---

## Fields Used for Matching

| Field | Matching Purpose |
|---|---|
| `contact_email` / `client_email` | Strongest direct match signal |
| `contact_phone` / `client_phone` | Strong direct match signal |
| `contact_name` / `client_name` | Secondary similarity signal |
| `property_city` | Location alignment signal |
| `property_type` | Property profile alignment signal |
| `estimated_units` / `managed_units` | Unit-count alignment signal |
| `lead_status` / `client_status` | Status conflict or verification signal |

---

## Match Status Definitions

| Match Status | Definition |
|---|---|
| High Confidence Match | Strong direct match signals exist and no major conflicts are present |
| Medium Confidence Match | Partial match signals exist, but manual review is recommended |
| Low Confidence Match | Weak match signals exist and manual verification is required |
| No Match | No reliable overlap is found |
| Exception | Conflicting, missing, or unclear data prevents automatic classification |

---

## High-Confidence Match Rule

A record can be classified as a high-confidence match when:

- Email matches or phone matches
- City matches
- No major conflict exists in record status
- Property type is aligned or not materially conflicting

Example:

```text
Lead email = Client email
Lead city = Client city
Client status = Active or Prospect
Result = High Confidence Match
