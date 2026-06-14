# QA Rules

This document defines the public-safe QA validation rules for the Lead Intelligence System.

All examples use synthetic data only. No real company, client, owner, tenant, property, contact, CRM, AppFolio, LeadSimple, Gmail, Google Sheets, or internal system data is included.

---

## Purpose

The QA workflow is designed to make lead verification safer, more consistent, and easier to review.

The system should identify:

- Records that are clean enough to pass
- Records that require manual review
- Records that should fail validation
- Records that should be routed into the exception queue

The main rule is simple:

```text
Do not force a match when the data is incomplete, conflicting, or unsupported.
