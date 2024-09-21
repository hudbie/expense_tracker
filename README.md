## Simple Expense Tracker - Usage Guide

### 📋 Overview
A simple command-line expense tracking application with data visualization capabilities.

### 🚀 Installation

1. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### 🎯 How to Use

#### Running the Main Application
```bash
python main.py
```

#### Quick Statistics
```bash
python quick_stats.py
```

### 📝 Features

1. **Add Expense** 
   - Record amount, category, and optional description
   - Automatically saves with timestamp

2. **View Expenses**
   - See all expenses in a formatted table
   - Option to view only recent expenses

3. **Expense Summary**
   - View total spending by category
   - Sorted by highest spending

4. **Data Visualization**
   - Pie chart showing expense distribution by category
   - Bar chart showing monthly spending trends
   - Charts saved as `expense_charts.png`

5. **Delete Expenses**
   - Remove expenses by ID
   - Automatic ID reassignment

### 💾 Data Storage
- Expenses are stored in `expenses.json`
- Data persists between sessions
- Automatic backup on each modification

### 🎨 Sample Categories
You can use any categories you like. Some suggestions:
- Food & Dining
- Transportation
- Entertainment
- Shopping
- Bills & Utilities
- Healthcare
- Education

### 📊 Sample Usage Flow

1. Run `python main.py`
2. Choose option 1 to add your first expense:
   - Amount: `25.50`
   - Category: `Food`
   - Description: `Lunch with friends`
3. Add a few more expenses with different categories
4. Use option 3 to see category summary
5. Use option 4 to generate visual charts
6. Use option 5 to manage expenses if needed

### 🔧 Requirements
- Python 3.6+
- matplotlib
- pandas

### 💡 Tips
- Use descriptive categories for better visualization
- Regular backups of `expenses.json` are recommended
- Charts are automatically saved and can be shared

The application provides a simple yet powerful way to track and visualize your spending habits directly from the command line!