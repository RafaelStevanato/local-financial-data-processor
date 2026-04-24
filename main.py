# Imports
from src.config import INPUT_DATA_FILE, OUTPUT_DATA_FILE, OUTPUT_REPORT_FILE
from src.processor import process_financial_file


# Functions
def main():
    df, kpis = process_financial_file(
        INPUT_DATA_FILE,
        OUTPUT_DATA_FILE,
        OUTPUT_REPORT_FILE
    )

    print("\n=== KPIs ===")
    for key, value in kpis.items():
        print(f"{key}: {value}")

    print(df.head())


if __name__ == "__main__":
    main()