### Personal Finance Tracker and Budget Analysis   
A Python-based tool for tracking and analyzing personal finances, featuring an interactive dashboard built with Pandas, Matplotlib, Seaborn, and Plotly. This project showcases data cleaning, statistical analysis, and visualization skills using a synthetic dataset of income, expenses, and savings.

## Features

Synthetic Dataset: Generates realistic monthly financial data (income, expenses, savings).
Data Cleaning: Handles missing values, standardizes formats, and removes outliers.
Analysis: Calculates savings rate and expense ratios for actionable insights.
Visualizations: Offers line charts for trends, pie charts for expense breakdowns, and an interactive Plotly dashboard.

## Clean Data

Handle Missing Values and Outliers: Fills missing amounts with averages and removes outliers beyond 3 standard deviations in NOAA datasets.
Analyze Trends: Computes monthly and seasonal temperature/precipitation averages; Visualizes trends with Matplotlib and Seaborn.
Interactive Analysis: Uses Plotly for interactive line plots; Modular code in Jupyter notebooks for reusable scripts in src/.

## Project Structure
PersonalFinanceTracker/
├── data/
│   └── finance_data.csv
├── src/
│   ├── data_generator.py
│   ├── data_cleaning.py
│   ├── analysis.py
│   └── dashboard.py
├── requirements.txt
├── README.md
└── .gitignore

## Setup Instructions

Clone the Repository:
    git clone https://github.com/your-username/PersonalFinanceTracker.git
    cd PersonalFinanceTracker

Set Up Environment:
    python -m venv .venv
    source .venv/bin/activate  # Windows: .venv\Scripts\activate

Install Dependencies:
    pip install -r requirements.txt

Generate Data:
    python src/data_generator.py

Run Dashboard:
    python src/dashboard.py

Opens an interactive dashboard (dashboard.html) in your browser.

## Datasets

Synthetic Data: Generated via data_generator.py; saved as data/finance_data.csv.
Expected Format: Columns: Date, Category, Amount, Description.

## Run Analysis
Jupyter Notebooks: Run notebooks/Finance_Analysis.ipynb for detailed analysis.
Results: Visualizations saved as monthly_trends.png, expense_breakdown.png.

## Key Insights
1. Savings Rate: ~20% of income saved monthly, indicating good financial habits.
2. Expense Breakdown: Discretionary spending (e.g., Entertainment) accounts for ~20% of expenses.
3. Trends: Stable Rent and Utilities, variable Entertainment spending.

## Visualizations

1. Monthly Trends: Line chart of income/expense patterns.
2. Expense Breakdown: Pie chart of average category spending.
3. Interactive Dashboard: Dynamic view of trends, savings, and ratios.

## Technologies

Python: Pandas, Matplotlib, Seaborn, Plotly
Environment: Virtualenv
Version Control: Git

## Future Enhancements

1. Support for user-uploaded financial data.
2. Integration with real-time financial APIs.
3. Dashboard filters for category-specific analysis.


## MIT License

Copyright (c) [2025] [Your Name or Your Username]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.