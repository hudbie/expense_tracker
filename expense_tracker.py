#!/usr/bin/env python3
"""
Simple Command-Line Expense Tracker with Data Visualization
"""

import json
import os
import datetime
import matplotlib.pyplot as plt
from collections import defaultdict

DATA_FILE = "expenses.json"

class ExpenseTracker:
    def __init__(self):
        self.expenses = self.load_expenses()
    
    def load_expenses(self):
        """Load expenses from JSON file"""
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                return []
        return []
    
    def save_expenses(self):
        """Save expenses to JSON file"""
        with open(DATA_FILE, 'w') as f:
            json.dump(self.expenses, f, indent=2)
    
    def add_expense(self, amount, category, description=""):
        """Add a new expense"""
        expense = {
            'id': len(self.expenses) + 1,
            'amount': float(amount),
            'category': category,
            'description': description,
            'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.expenses.append(expense)
        self.save_expenses()
        print(f"✅ Expense added: ${amount} for {category}")
    
    def view_expenses(self, filter_category=None):
        """View all expenses or filter by category"""
        if not self.expenses:
            print("📝 No expenses recorded yet.")
            return
        
        filtered_expenses = self.expenses
        if filter_category:
            filtered_expenses = [e for e in self.expenses if e['category'].lower() == filter_category.lower()]
        
        if not filtered_expenses:
            print(f"📝 No expenses found for category: {filter_category}")
            return
        
        print(f"\n{'ID':<4} {'Date':<20} {'Category':<15} {'Amount':<10} {'Description'}")
        print("-" * 70)
        total = 0
        for expense in filtered_expenses:
            print(f"{expense['id']:<4} {expense['date']:<20} {expense['category']:<15} ${expense['amount']:<9.2f} {expense['description']}")
            total += expense['amount']
        
        print(f"\n💰 Total: ${total:.2f}")
    
    def get_summary(self):
        """Get summary by category"""
        if not self.expenses:
            print("📝 No expenses to summarize.")
            return
        
        category_totals = defaultdict(float)
        for expense in self.expenses:
            category_totals[expense['category']] += expense['amount']
        
        print("\n📊 Expense Summary by Category:")
        print("-" * 30)
        for category, total in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
            print(f"{category:<15}: ${total:.2f}")
        
        print(f"\n💰 Grand Total: ${sum(category_totals.values()):.2f}")
        return category_totals
    
    def generate_chart(self):
        """Generate pie chart of expenses by category"""
        if not self.expenses:
            print("📝 No expenses to visualize.")
            return
        
        category_totals = self.get_summary()
        
        # Create pie chart
        categories = list(category_totals.keys())
        amounts = list(category_totals.values())
        
        plt.figure(figsize=(10, 8))
        plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=90)
        plt.title('Expense Distribution by Category')
        plt.axis('equal')
        
        # Save the chart
        plt.savefig('expense_chart.png')
        plt.show()
        print("📈 Chart saved as 'expense_chart.png'")

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\n💸 Expense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expenses by Category")
        print("4. View Summary")
        print("5. Generate Chart")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            try:
                amount = float(input("Enter amount: $"))
                category = input("Enter category: ").strip()
                description = input("Enter description (optional): ").strip()
                tracker.add_expense(amount, category, description)
            except ValueError:
                print("❌ Invalid amount. Please enter a number.")
        
        elif choice == '2':
            tracker.view_expenses()
        
        elif choice == '3':
            category = input("Enter category to filter: ").strip()
            tracker.view_expenses(category)
        
        elif choice == '4':
            tracker.get_summary()
        
        elif choice == '5':
            tracker.generate_chart()
        
        elif choice == '6':
            print("👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()