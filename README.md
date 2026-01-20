# Excel Data Cleaner using Python

## Description
A Python tool that cleans messy Excel or CSV files automatically by fixing column names, removing duplicate rows, handling missing values, and exporting a clean Excel file.

## Features
- Supports Excel (.xlsx) and CSV (.csv)
- Standardizes column names
- Removes duplicate records
- Handles missing values automatically

## Tech Stack
- Python 3.11
- Pandas
- OpenPyXL

## Project Structure
excel-data-cleaner/
│
├── excel_cleaner.py
├── messy_data.xlsx
├── messy_data_cleaned.xlsx
├── requirements.txt
└── README.md


## How to Run
1. Install dependencies:
```bash
pip install -r requirements.txt


Run the script:
-->> python excel_cleaner.py your_file.xlsx


Output
A cleaned Excel file will be created with _cleaned added to the file name.

Example:
Cleaned file saved as: messy_data_cleaned.xlsx

Use Case
Useful for businesses, analysts, and teams dealing with messy spreadsheet data.

Author
Raju
