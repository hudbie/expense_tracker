## Simple Expense Tracker

A command-line expense tracking application with data visualization capabilities.

### Features
- ✅ Add expenses with amount, category, and description
- 📝 View all expenses or filter by category
- 📊 View expense summary by category
- 📈 Generate pie chart visualization
- 💾 Automatic data persistence (JSON file)

### Installation

1. **Install dependencies:**
   ```bash
   python install.py
   ```
   Or manually:
   ```bash
   pip install matplotlib
   ```

### Usage

1. **Run the application:**
   ```bash
   python expense_tracker.py
   ```

2. **Menu Options:**
   - **1. Add Expense**: Record a new expense
   - **2. View All Expenses**: Display all recorded expenses
   - **3. View Expenses by Category**: Filter expenses by specific category
   - **4. View Summary**: Show total expenses grouped by category
   - **5. Generate Chart**: Create and display a pie chart visualization
   - **6. Exit**: Quit the application

### Example Usage

```
💸 Expense Tracker
1. Add Expense
2. View All Expenses
3. View Expenses by Category
4. View Summary
5. Generate Chart
6. Exit

Enter your choice (1-6): 1
Enter amount: $25.50
Enter category: Food
Enter description (optional): Lunch at cafe
✅ Expense added: $25.5 for Food
```

### Data Storage

- Expenses are stored in `expenses.json` file
- Chart is saved as `expense_chart.png`

### Requirements

- Python 3.6+
- matplotlib (for chart generation)

### Files Structure

```
expense_tracker/
├── expense_tracker.py    # Main application
├── requirements.txt      # Dependencies
├── install.py           # Installation script
├── expenses.json        # Data file (created automatically)
└── expense_chart.png    # Chart file (created when generating charts)
```

Enjoy tracking your expenses! 💰