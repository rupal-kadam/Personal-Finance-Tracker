import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def analyze_data(input_file):
    df = pd.read_csv(input_file)
    
    df['Date'] = pd.to_datetime(df['Date'])

    
    # Calculate metrics
    monthly_summary = df.groupby([df['Date'].dt.to_period('M'), 'Category'])['Amount'].sum().unstack()
    savings_rate = monthly_summary['Savings'] / monthly_summary['Salary'] * 100
    expense_ratios = monthly_summary.drop('Salary', axis=1).div(monthly_summary.sum(axis=1), axis=0) * 100
    
    # Visualizations
    plt.figure(figsize=(10, 6))
    monthly_summary.plot(kind='line')
    plt.title('Monthly Income and Expenses')
    plt.ylabel('Amount ($)')
    plt.savefig('monthly_trends.png')
    plt.close()
    
    plt.figure(figsize=(8, 8))
    monthly_summary.mean().plot(kind='pie', autopct='%1.1f%%')
    plt.title('Average Expense Breakdown')
    plt.savefig('expense_breakdown.png')
    plt.close()
    
    print("Savings Rate (%):", savings_rate.mean())
    print("Expense Ratios (%):", expense_ratios.mean())
    return monthly_summary, savings_rate, expense_ratios

if __name__ == "__main__":
    data = os.path.join(os.getcwd(), "Data")
    input_path = os.path.join(data, "finance_data_cleaned.csv")
    analyze_data(input_path)