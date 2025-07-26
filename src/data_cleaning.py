import pandas as pd
import numpy as np
import os
from pathlib import Path

def clean_data(input_file, output_file):
    df = pd.read_csv(Path(input_file))
    
    # Handle missing values
    df['Amount'] = df['Amount'].fillna(df['Amount'].mean())
    
    # Standardize formats
    df['Date'] = pd.to_datetime(df['Date'])
    df['Category'] = df['Category'].str.title()
    df['Amount'] = df['Amount'].round(2)
    
    # Remove outliers (amounts > 3 std deviations)
    df = df[np.abs(df['Amount'] - df['Amount'].mean()) <= (3 * df['Amount'].std())]
    
    df.to_csv(Path(output_file), index=False)
    print("Data cleaned and saved to", output_file)
    return df

if __name__ == "__main__":
    data = os.path.join(os.getcwd(), "Data")
    input = os.path.join(data, "finance_data.csv")
    output = os.path.join(data, "finance_data_cleaned.csv")
    clean_data(input, output)