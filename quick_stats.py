#!/usr/bin/env python3
"""
Quick statistics utility for expense data
"""

import json
from datetime import datetime, timedelta
from expense_tracker import ExpenseTracker

def quick_stats():
    """Display quick statistics about expenses"""
    tracker = ExpenseTracker()
    
    if not tracker.expenses:
        print("📭 No expenses recorded yet.")
        return
    
    total_expenses = len(tracker.expenses)
    total_amount = sum(expense['amount'] for expense in tracker.expenses)
    
    # Recent expenses (last 7 days)
    week_ago = datetime.now() - timedelta(days=7)
    recent_expenses = [
        exp for exp in tracker.expenses 
        if datetime.strptime(exp['date'], "%Y-%m-%d %H:%M:%S") >= week_ago
    ]
    recent_total = sum(exp['amount'] for exp in recent_expenses)
    
    # Average expense
    avg_expense = total_amount / total_expenses if total_expenses > 0 else 0
    
    print("\n📈 QUICK STATISTICS")
    print("="*30)
    print(f"Total Expenses: {total_expenses}")
    print(f"Total Amount: ${total_amount:.2f}")
    print(f"Average per Expense: ${avg_expense:.2f}")
    print(f"Last 7 Days: ${recent_total:.2f}")
    print(f"Expenses this week: {len(recent_expenses)}")
    
    # Most expensive category
    category_totals = {}
    for expense in tracker.expenses:
        category = expense['category']
        category_totals[category] = category_totals.get(category, 0) + expense['amount']
    
    if category_totals:
        top_category = max(category_totals.items(), key=lambda x: x[1])
        print(f"Top Category: {top_category[0]} (${top_category[1]:.2f})")

if __name__ == "__main__":
    quick_stats()