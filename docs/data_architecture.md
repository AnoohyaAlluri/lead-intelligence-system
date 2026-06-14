# Data Architecture

This document explains the public-safe data architecture for the Lead Intelligence System.

All datasets, records, identifiers, names, emails, phone numbers, and examples in this repository are synthetic. No confidential company, client, owner, tenant, property, CRM, AppFolio, LeadSimple, Gmail, Google Sheets, or internal system data is included.

---

## Architecture Purpose

The purpose of this architecture is to convert raw lead and client-style records into a structured verification workflow.

The system is designed to support:

- Lead data cleaning
- Contact field standardization
- Client-style record comparison
- Match-confidence scoring
- Exception routing
- QA validation
- Analytics-ready reporting

The workflow is structured to avoid unsupported assumptions. Records with weak, incomplete, or conflicting signals are routed to review instead of being forced into a verified match.

---

## Layered Architecture

This project uses a medallion-style data structure.

| Layer | Folder | Purpose |
|---|---|---|
| Bronze | `datasets/raw/` | Stores synthetic raw input datasets |
| Silver | `datasets/cleaned/` | Stores cleaned and standardized records |
| Gold | `outputs/` | Stores match results and exception queue outputs |
| Analytics | `datasets/analytics/` | Stores summary metrics and reporting outputs |

---

## End-to-End Workflow

```mermaid
flowchart TD
    A[Raw Marketing Leads] --> B[Bronze Layer]
    C[Raw Client-Style Records] --> B

    B --> D[Silver Cleaning Layer]
    D --> E[Standardized Lead Records]
    D --> F[Standardized Client-Style Records]

    E --> G[Gold Matching Layer]
    F --> G

    G --> H[Match-Confidence Results]
    G --> I[Exception Queue]

    H --> J[QA Validation]
    I --> J

    J --> K[Analytics Summary]
    K --> L[Lead Intelligence Reporting]
