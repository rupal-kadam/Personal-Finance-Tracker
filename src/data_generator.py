'''
<xaiArtifact artifact_id="037b6a18-151a-46a7-99cd-2c7e4a000b59" artifact_version_id="0f4bb568-751c-4dc4-926c-ea73786ddb14" title="data_generator.py" contentType="text/python">
'''
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from pathlib import Path
import os


def generate_finance_data():
    start_date = datetime(2024, 1, 1)
    dates = [start_date + timedelta(days=30 * i) for i in range(12)]
    categories = ['Salary', 'Rent', 'Groceries', 'Utilities', 'Entertainment', 'Savings']
    
    data = []
    for date in dates:
        for category in categories:
            if category == 'Salary':
                amount = random.uniform(3000, 5000)
            elif category == 'Savings':
                amount = random.uniform(500, 1500)
            else:
                amount = random.uniform(100, 1000)
            data.append({
                'Date': date.strftime('%Y-%m-%d'),
                'Category': category,
                'Amount': round(amount, 2),
                'Description': f"{category} expense"
            })
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(folder_path, 'finance_data.csv'), index=False)
    print("Synthetic data generated and saved to data/finance_data.csv")

if __name__ == "__main__":
    folder_path = os.path.join(os.getcwd(), "Data")
    os.makedirs(folder_path, exist_ok=True) 
    generate_finance_data()
