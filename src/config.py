# Imports
from pathlib import Path

#Project Paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "financial_data.csv"
OUTPUT_DIR = BASE_DIR / "output"
SUMMARY_FILE = OUTPUT_DIR / "summary_by_category.csv"
REPORT_FILE = OUTPUT_DIR / "financial_report.txt"
REQUIRED_COLUMNS = ["date", "category", "description", "amount"]