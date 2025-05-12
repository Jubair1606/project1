import pandas as pd
import numpy as np
import os

def clean_hope_data(file_path: str, sheet_name: str = 0) -> pd.DataFrame:
    df = pd.read_excel(file_path, sheet_name=sheet_name)

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace('\n', ' ').str.replace(' ', '_')

    # Rename important columns
    rename_map = {
        'patient_id#': 'patient_id',
        'payment_submitted?': 'payment_submitted',
        'application_signed?': 'application_signed'
    }
    df = df.rename(columns=rename_map)

    # Replace common placeholders with NaN
    df.replace(['Missing', 'None', '', 'nan'], np.nan, inplace=True)

    # Convert date columns
    for col in ['grant_req_date', 'dob']:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')

    # Convert numeric fields
    numeric_cols = ['amount', 'remaining_balance', 'total_household_gross_monthly_income']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Normalize booleans
    bool_map = {'yes': True, 'y': True, 'no': False, 'n': False}
    for col in ['payment_submitted', 'application_signed']:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.lower().map(bool_map)

    # Clean string columns
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].astype(str).str.strip().replace("nan", np.nan)

    # Drop rows missing critical IDs
    if 'patient_id' in df.columns:
        df = df.dropna(subset=['patient_id'])

    return df

if __name__ == "__main__":
    input_file = "data/raw_data.xlsx"
    output_file = "data/cleaning_data.xlsx"

    if not os.path.exists("data"):
        os.makedirs("data")

    cleaned_df = clean_hope_data(input_file)
    cleaned_df.to_excel(output_file, index=False)

    print(f"✅ Cleaned data saved to: {output_file}")
