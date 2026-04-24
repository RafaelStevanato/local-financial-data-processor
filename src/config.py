# Imports
from pathlib import Path

#Variables
BASE_DIRECTORY = Path(__file__).resolve().parent.parent
INPUT_DATA_FILE = BASE_DIRECTORY / "data" / "raw"/ "input.csv"
OUTPUT_DATA_FILE = BASE_DIRECTORY / "output" / "processed_data.csv"
OUTPUT_REPORT_FILE = BASE_DIRECTORY / "output" / "financial_report.txt"
