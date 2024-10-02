#!/usr/bin/env python3
"""
Quick start script with sample data
"""

from expense_tracker import ExpenseTracker
import datetime

def create_sample_data():
    """Create sample expense data for testing"""
    tracker = ExpenseTracker()
    
    sample_expenses = [
        (45.50, "Food", "Lunch at restaurant"),
        (120.00, "Shopping", "New clothes"),
        (80.00, "Entertainment", "Movie tickets"),
        (25.30, "Food", "Groceries"),
        (60.00, "Transport", "Monthly bus pass"),
        (15.75, "Food", "Coffee and snacks"),
        (200.00, "Bills", "Electricity bill"),
        (35.20, "Shopping", "Household items"),
    ]
    
    print("📝 Adding sample expenses...")
    for amount, category, description in sample_expenses:
        tracker.add_expense(amount, category, description)
    
    print("✅ Sample data created!")
    print("Run 'python expense_tracker.py' to start using the application.")

if __name__ == "__main__":
    create_sample_data()