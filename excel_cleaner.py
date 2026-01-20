import pandas as pd
import sys
import os

def clean_file(input_path):
    # Read file
    if input_path.endswith(".csv"):
        df = pd.read_csv(input_path)
    elif input_path.endswith(".xlsx"):
        df = pd.read_excel(input_path)
    else:
        print("Unsupported file format")
        return

    # Clean column names
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.fillna("Not Available")

    # Output file name
    base = os.path.splitext(input_path)[0]
    output_path = base + "_cleaned.xlsx"

    # Save output
    df.to_excel(output_path, index=False)

    print(f"Cleaned file saved as: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python excel_cleaner.py <file_path>")
    else:
        clean_file(sys.argv[1])
