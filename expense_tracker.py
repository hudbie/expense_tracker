#!/usr/bin/env python3
"""
Simple Command-Line Expense Tracker with Data Visualization
"""

import json
import os
import datetime
from typing import List, Dict, Any
import matplotlib.pyplot as plt
import pandas as pd

class ExpenseTracker:
    def __init__(self, data_file: str = "expenses.json"):
        self.data_file = data_file
        self.expenses = self.load_expenses()
    
    def load_expenses(self) -> List[Dict[str, Any]]:
        """Load expenses from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                return []
        return []
    
    def save_expenses(self):
        """Save expenses to JSON file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.expenses, f, indent=2)
    
    def add_expense(self, amount: float, category: str, description: str = ""):
        """Add a new expense"""
        expense = {
            'id': len(self.expenses) + 1,
            'amount': amount,
            'category': category,
            'description': description,
            'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.expenses.append(expense)
        self.save_expenses()
        print(f"✅ Expense added: ${amount:.2f} for {category}")
    
    def view_expenses(self, limit: int = None):
        """View all expenses"""
        if not self.expenses:
            print("📭 No expenses recorded yet.")
            return
        
        expenses_to_show = self.expenses if limit is None else self.expenses[-limit:]
        
        print("\n📋 EXPENSE HISTORY:")
        print("-" * 80)
        print(f"{'ID':<4} {'Date':<19} {'Category':<15} {'Amount':<10} {'Description'}")
        print("-" * 80)
        
        total = 0
        for expense in expenses_to_show:
            print(f"{expense['id']:<4} {expense['date']:<19} {expense['category']:<15} "
                  f"${expense['amount']:<9.2f} {expense['description']}")
            total += expense['amount']
        
        print("-" * 80)
        print(f"Total: ${total:.2f}")
    
    def get_summary(self):
        """Get summary by category"""
        if not self.expenses:
            print("📭 No expenses to summarize.")
            return
        
        summary = {}
        for expense in self.expenses:
            category = expense['category']
            amount = expense['amount']
            summary[category] = summary.get(category, 0) + amount
        
        print("\n📊 EXPENSE SUMMARY BY CATEGORY:")
        print("-" * 30)
        for category, total in sorted(summary.items(), key=lambda x: x[1], reverse=True):
            print(f"{category:<15}: ${total:.2f}")
        
        return summary
    
    def visualize_expenses(self):
        """Create visualizations of expenses"""
        if not self.expenses:
            print("📭 No expenses to visualize.")
            return
        
        # Convert to DataFrame for easier manipulation
        df = pd.DataFrame(self.expenses)
        df['date'] = pd.to_datetime(df['date'])
        df['month'] = df['date'].dt.to_period('M')
        
        # Create subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Pie chart by category
        category_totals = df.groupby('category')['amount'].sum()
        ax1.pie(category_totals.values, labels=category_totals.index, autopct='%1.1f%%', startangle=90)
        ax1.set_title('Expenses by Category')
        
        # Bar chart by month
        monthly_totals = df.groupby('month')['amount'].sum()
        monthly_totals.plot(kind='bar', ax=ax2, color='skyblue')
        ax2.set_title('Monthly Expenses')
        ax2.set_xlabel('Month')
        ax2.set_ylabel('Amount ($)')
        plt.xticks(rotation=45)
        
        plt.tight_layout()
        plt.savefig('expense_charts.png', dpi=300, bbox_inches='tight')
        print("📈 Charts saved as 'expense_charts.png'")
        plt.show()
    
    def delete_expense(self, expense_id: int):
        """Delete an expense by ID"""
        for i, expense in enumerate(self.expenses):
            if expense['id'] == expense_id:
                deleted = self.expenses.pop(i)
                # Reassign IDs
                for j, exp in enumerate(self.expenses[i:], start=i):
                    exp['id'] = j + 1
                self.save_expenses()
                print(f"🗑️ Expense {expense_id} deleted: ${deleted['amount']:.2f} for {deleted['category']}")
                return
        print(f"❌ Expense ID {expense_id} not found.")