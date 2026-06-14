# Requirements

This document defines the business, data, technical, QA, and confidentiality requirements for the Lead Intelligence System.

This repository uses synthetic data only. No real company, client, owner, tenant, property, contact, CRM, AppFolio, LeadSimple, Gmail, Google Sheets, or internal system data is included.

---

## Project Purpose

The Lead Intelligence System is designed to demonstrate how raw marketing lead records can be converted into a structured, QA-ready, analytics-ready verification workflow.

The project focuses on:

- Lead data cleaning
- Contact field standardization
- Client-style record comparison
- Match-confidence scoring
- Exception queue routing
- QA validation
- Analytics-ready reporting

---

## Business Requirements

The system should help answer public-safe business questions such as:

- Which synthetic leads appear ready for verification?
- Which leads have strong match signals?
- Which leads require manual review?
- Which records have missing or invalid contact data?
- Which records appear duplicated?
- Which source categories produce cleaner lead records?
- Which records should be routed to an exception queue?

---

## Data Requirements

The project must include two public-safe raw input datasets.

### Raw Marketing Leads

File:

```text
datasets/raw/raw_marketing_leads_mock.csv
