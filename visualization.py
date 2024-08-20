"""
Data Visualization Module for Expense Tracker
"""

import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from typing import List, Dict, Any

def generate_visualizations(expenses: List[Dict[str, Any]]):
    """Generate various visualizations for expense data"""
    if not expenses:
        print("No expenses data available for visualization.")
        return
    
    # Convert to DataFrame for easier manipulation
    df = pd.DataFrame(expenses)
    df['date'] = pd.to_datetime(df['date'])
    df['amount'] = pd.to_numeric(df['amount'])
    
    # Create subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Expense Analysis Dashboard', fontsize=16, fontweight='bold')
    
    # 1. Pie chart by category
    category_totals = df.groupby('category')['amount'].sum()
    ax1.pie(category_totals.values, labels=category_totals.index, autopct='%1.1f%%', startangle=90)
    ax1.set_title('Expenses by Category')
    
    # 2. Bar chart by category
    category_totals.sort_values(ascending=False).plot(kind='bar', ax=ax2, color='skyblue')
    ax2.set_title('Total Expenses by Category')
    ax2.set_ylabel('Amount ($)')
    ax2.tick_params(axis='x', rotation=45)
    
    # 3. Daily expenses over time
    daily_expenses = df.groupby(df['date'].dt.date)['amount'].sum()
    ax3.plot(daily_expenses.index, daily_expenses.values, marker='o', linewidth=2, markersize=4)
    ax3.set_title('Daily Expenses Over Time')
    ax3.set_ylabel('Amount ($)')
    ax3.tick_params(axis='x', rotation=45)
    
    # 4. Top 5 expenses
    top_expenses = df.nlargest(5, 'amount')[['description', 'amount', 'category']]
    if not top_expenses.empty:
        bars = ax4.barh(
            [f"{row['description'][:20]}..." if len(row['description']) > 20 else row['description'] 
             for _, row in top_expenses.iterrows()],
            top_expenses['amount'],
            color='lightcoral'
        )
        ax4.set_title('Top 5 Largest Expenses')
        ax4.set_xlabel('Amount ($)')
        
        # Add value labels on bars
        for bar in bars:
            width = bar.get_width()
            ax4.text(width, bar.get_y() + bar.get_height()/2, f'${width:.2f}', 
                    ha='left', va='center', fontweight='bold')
    
    plt.tight_layout()
    plt.show()
    
    # Print some statistics
    print("\n" + "="*50)
    print("📊 EXPENSE STATISTICS")
    print("="*50)
    print(f"Total Expenses: ${df['amount'].sum():.2f}")
    print(f"Average Expense: ${df['amount'].mean():.2f}")
    print(f"Largest Expense: ${df['amount'].max():.2f}")
    print(f"Smallest Expense: ${df['amount'].min():.2f}")
    print(f"Number of Expenses: {len(df)}")
    print(f"Date Range: {df['date'].min().strftime('%Y-%m-%d')} to {df['date'].max().strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    print("This module is meant to be imported, not run directly.")