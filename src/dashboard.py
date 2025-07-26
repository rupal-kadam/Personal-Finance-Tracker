import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from analysis import analyze_data
import os 
from pathlib import Path

def create_dashboard(path):
    df = pd.read_csv(path)
    monthly_summary, savings_rate, expense_ratios = analyze_data(path)
    
    # Create Plotly dashboard
    fig = make_subplots(rows=2, cols=2, 
                        subplot_titles=('Monthly Trends', 'Expense Breakdown', 'Savings Rate', 'Expense Ratios'),
                        specs=[[{"type": "xy"}, {"type": "pie"}],
                               [{"type": "xy"}, {"type": "xy"}]])
    
    # Monthly Trends
    for col in monthly_summary.columns:
        fig.add_trace(go.Scatter(x=monthly_summary.index.astype(str), y=monthly_summary[col], name=col), row=1, col=1)
    
    # Expense Breakdown
    fig.add_trace(go.Pie(labels=monthly_summary.mean().index, values=monthly_summary.mean()), row=1, col=2)
    
    # Savings Rate
    fig.add_trace(go.Scatter(x=savings_rate.index.astype(str), y=savings_rate, name='Savings Rate (%)'), row=2, col=1)
    
    # Expense Ratios
    for col in expense_ratios.columns:
        fig.add_trace(go.Scatter(x=expense_ratios.index.astype(str), y=expense_ratios[col], name=f'{col} Ratio (%)'), row=2, col=2)
    
    fig.update_layout(title_text="Personal Finance Dashboard", height=800)
    fig.write_html('dashboard.html')
    print("Dashboard saved as dashboard.html")

if __name__ == "__main__":
    data = os.path.join(os.getcwd(), "Data")
    path = os.path.join(data, "finance_data_cleaned.csv")
    create_dashboard(path)