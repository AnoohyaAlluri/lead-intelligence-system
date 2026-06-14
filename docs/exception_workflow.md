# Exception Workflow

This document explains how uncertain, incomplete, duplicate, or conflicting records are routed for review in the Lead Intelligence System.

All examples use synthetic data only. No real company, client, owner, tenant, property, contact, CRM, AppFolio, LeadSimple, Gmail, Google Sheets, or internal system data is included.

---

## Purpose

The exception workflow exists to prevent unsupported matches.

Instead of forcing a lead-to-client style match when the data is incomplete or conflicting, the system routes the record into an exception queue.

The goal is to protect data quality, attribution accuracy, reporting reliability, and follow-up decisions.

---

## Core Rule

```text
When the evidence is incomplete, conflicting, or weak, route the record to review.
