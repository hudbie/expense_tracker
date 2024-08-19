#!/usr/bin/env python3
"""
Simple Command-Line Expense Tracking Application
"""

import json
import datetime
import os
from typing import List, Dict, Any

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
        print(f"✓ Expense added: ${amount:.2f} for {category}")
    
    def list_expenses(self, limit: int = None):
        """List all expenses"""
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        
        expenses_to_show = self.expenses[-limit:] if limit else self.expenses
        
        print("\n" + "="*60)
        print(f"{'ID':<4} {'Date':<19} {'Category':<15} {'Amount':<10} {'Description'}")
        print("="*60)
        
        total = 0
        for expense in expenses_to_show:
            print(f"{expense['id']:<4} {expense['date']:<19} {expense['category']:<15} "
                  f"${expense['amount']:<9.2f} {expense['description']}")
            total += expense['amount']
        
        print("="*60)
        print(f"Total: ${total:.2f}")
    
    def get_summary(self):
        """Get expense summary by category"""
        if not self.expenses:
            print("No expenses to summarize.")
            return
        
        summary = {}
        for expense in self.expenses:
            category = expense['category']
            if category not in summary:
                summary[category] = 0
            summary[category] += expense['amount']
        
        print("\n" + "="*40)
        print("EXPENSE SUMMARY BY CATEGORY")
        print("="*40)
        
        total = 0
        for category, amount in sorted(summary.items(), key=lambda x: x[1], reverse=True):
            print(f"{category:<15}: ${amount:>8.2f}")
            total += amount
        
        print("="*40)
        print(f"{'TOTAL':<15}: ${total:>8.2f}")
        
        return summary
    
    def delete_expense(self, expense_id: int):
        """Delete an expense by ID"""
        for i, expense in enumerate(self.expenses):
            if expense['id'] == expense_id:
                deleted_amount = expense['amount']
                del self.expenses[i]
                # Reassign IDs
                for j, exp in enumerate(self.expenses, 1):
                    exp['id'] = j
                self.save_expenses()
                print(f"✓ Expense ${deleted_amount:.2f} deleted successfully.")
                return
        
        print("❌ Expense ID not found.")

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\n" + "="*50)
        print("💰 SIMPLE EXPENSE TRACKER")
        print("="*50)
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Show Summary")
        print("4. Delete Expense")
        print("5. Generate Visualization")
        print("6. Exit")
        print("="*50)
        
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == '1':
            try:
                amount = float(input("Enter amount: $"))
                category = input("Enter category: ").strip()
                description = input("Enter description (optional): ").strip()
                tracker.add_expense(amount, category, description)
            except ValueError:
                print("❌ Invalid amount. Please enter a number.")
        
        elif choice == '2':
            try:
                limit = input("How many recent expenses to show? (Enter for all): ").strip()
                limit = int(limit) if limit else None
                tracker.list_expenses(limit)
            except ValueError:
                print("❌ Invalid number.")
        
        elif choice == '3':
            tracker.get_summary()
        
        elif choice == '4':
            try:
                expense_id = int(input("Enter expense ID to delete: "))
                tracker.delete_expense(expense_id)
            except ValueError:
                print("❌ Invalid ID.")
        
        elif choice == '5':
            try:
                from visualization import generate_visualizations
                generate_visualizations(tracker.expenses)
            except ImportError:
                print("❌ Visualization module not available. Make sure matplotlib is installed.")
        
        elif choice == '6':
            print("👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice. Please enter 1-6.")

if __name__ == "__main__":
    main()