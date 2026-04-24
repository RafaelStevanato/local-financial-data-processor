# Local Financial Data Processor

## Overview
A Python-based local data processing engine that transforms raw financial CSV files into structured outputs with validation, standardization, and KPI calculation.

## Problem
Companies receive CSV/Excel files with inconsistent financial data that require manual cleaning and validation.

## Solution
This project:
- Reads raw CSV files
- Validates structure and content
- Flags invalid rows
- Calculates financial KPIs
- Generates processed data and reports

## Input Format

CSV with columns:

- date
- description
- amount
- category (income / expense)

## Output

- processed_data.csv → validated dataset
- financial_report.txt → KPIs summary

## How to Run

```bash
python main.py
```
- Example KPIs
- Total Income
- Total Expense
- Balance
- Valid / Invalid Transactions

## Tech Stack

- Python
- Pandas