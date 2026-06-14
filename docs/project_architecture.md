# Project Architecture

This document provides a visual overview of the Lead Intelligence System.

All diagrams are public-safe and use synthetic workflow concepts only. No real company data, client records, property records, CRM exports, internal spreadsheets, or private system information is included.

---

## End-to-End Lead Intelligence Workflow

```mermaid
flowchart TD
    A[Raw Marketing Leads] --> B[Bronze Layer]
    C[Raw Client-Style Records] --> B

    B --> D[Silver Cleaning Layer]

    D --> E[Cleaned Marketing Leads]
    D --> F[Cleaned Client-Style Records]

    E --> G[Gold Matching Layer]
    F --> G

    G --> H[Match-Confidence Results]
    G --> I[Exception Queue]

    H --> J[QA Validation]
    I --> J

    J --> K[Analytics Summary]
    K --> L[Growth Operations Reporting]
