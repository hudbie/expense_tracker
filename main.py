#!/usr/bin/env python3
"""
Main entry point for the Expense Tracker application
"""

from expense_tracker import ExpenseTracker

def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("💰 SIMPLE EXPENSE TRACKER")
    print("="*50)
    print("1. ➕ Add Expense")
    print("2. 👀 View All Expenses")
    print("3. 📊 View Summary")
    print("4. 📈 Generate Charts")
    print("5. 🗑️ Delete Expense")
    print("6. 🚪 Exit")
    print("="*50)

def main():
    tracker = ExpenseTracker()
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            try:
                amount = float(input("Enter amount: $"))
                category = input("Enter category: ").strip()
                description = input("Enter description (optional): ").strip()
                tracker.add_expense(amount, category, description)
            except ValueError:
                print("❌ Invalid amount. Please enter a valid number.")
        
        elif choice == '2':
            limit_input = input("Enter number of recent expenses to show (or press Enter for all): ").strip()
            limit = int(limit_input) if limit_input.isdigit() else None
            tracker.view_expenses(limit)
        
        elif choice == '3':
            tracker.get_summary()
        
        elif choice == '4':
            tracker.visualize_expenses()
        
        elif choice == '5':
            try:
                expense_id = int(input("Enter expense ID to delete: "))
                tracker.delete_expense(expense_id)
            except ValueError:
                print("❌ Invalid ID. Please enter a valid number.")
        
        elif choice == '6':
            print("👋 Thank you for using Expense Tracker! Goodbye!")
            break
        
        else:
            print("❌ Invalid choice. Please enter a number between 1-6.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()