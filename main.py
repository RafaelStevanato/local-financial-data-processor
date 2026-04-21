# Imports
from pathlib import Path
import pandas as pd


# Project paths
BASE_DIR = Path (__file__).resolve().parent 
DATA_FILE = BASE_DIR / "data" / "financial_data.csv" 
OUTPUT_DIR = BASE_DIR / "output"
SUMMARY_FILE = OUTPUT_DIR / "summary_by_category.csv"
REPORT_FILE = OUTPUT_DIR / "financial_report.txt"


# Functions
def load_data (file_path:Path) -> pd.DataFrame:

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    df = pd.read_csv(file_path, sep = ",")
    required_columns = {"date", "category", "description", "amount"}
    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    
    df["date"] = pd.to_datetime(df["date"], errors = "coerce")

    if df["date"].isna().any():
        raise ValueError (f"Invalid values found in DATE column")
    
    df["amount"] = pd.to_numeric(df["amount"], errors = "coerce")

    if df["amount"].isna().any():
        raise ValueError (f"Invalid values found in AMOUNT column")
    
    return df

def calculate_metrics (df: pd.DataFrame) -> dict:
    
    total = df["amount"].sum()
    average = df["amount"].mean()
    count = len(df)
    total_sales = df[df["amount"] > 0]["amount"].sum()
    total_expenses = df[df["amount"] < 0]["amount"].sum()
    
    return {
        "total": total,
        "average": average,
        "count": count,
        "sales": total_sales,
        "expenses":total_expenses
    }

def generate_report (metrics: dict, summary: pd.DataFrame):

    lines = [
        "SVT FINANCIAL REPORT",
        "===============================",
        f"Total: {metrics['total']:.2f}",
        f"Average: {metrics['average']:.2f}",
        f"Count: {metrics['count']}",
        f"Total Sales: {metrics['sales']:.2f}",
        f"Total Expenses: {metrics['expenses']:.2f}",
        "",
        "SUMMARY BY CATEGORY",
        "-------------------------------",
    ]

    for _, row in summary.iterrows():
        lines.append(
            f"{row['category']}: total={row['total_amount']:.2f}, count={row['count']}"
        )

    report_text = "\n".join(lines)

    OUTPUT_DIR.mkdir (exist_ok = True)
    with open (REPORT_FILE, "w", encoding = "utf-8") as f:
        f.write(report_text)

def group_by_category (df: pd.DataFrame) -> pd.DataFrame:
    summary = df.groupby("category").agg(
        total_amount = ("amount", "sum"),
        count = ("amount", "count"),
    ).reset_index()
    return summary

def main ():
    df = load_data (DATA_FILE)
    metrics = calculate_metrics (df)
    summary = group_by_category (df)
    generate_report (metrics, summary)

if __name__ == "__main__":
    main()