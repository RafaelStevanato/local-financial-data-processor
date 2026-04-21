# Local Financial Data Processor

## 📌 Project Overview
This project automates financial data processing using Python.

It reads a CSV file, validates the data, calculates key financial metrics, and generates a structured report.

---

## ⚙️ What it does

- Reads financial data from a CSV file
- Validates required columns and data types
- Calculates:
  - Total amount
  - Average transaction value
  - Number of transactions
  - Total sales (positive values)
  - Total expenses (negative values)
- Groups data by category
- Generates a final report in `.txt` format

---

## 🛠️ Tech Stack

- Python
- Pandas

---

## 🚀 How to run

1. Clone the repository:

```bash
git clone https://github.com/RafaelStevanato/financial-data-automation.git
```

2. Navigate to the project folder:

```bash
cd financial-data-automation
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate the environment:

```bash
venv\Scripts\activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

6. Run the script:

```bash
python main.py
```

- It's meant to create a file called "financial_report.txt" inside the "output" folder, with the processed data from the CSV file called "financial_data.csv" inside the "data" folder.
