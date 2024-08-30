## Simple Expense Tracker Application

A command-line expense tracking application with data visualization capabilities.

### Features
- ✅ Add expenses with amount, category, and description
- ✅ List all expenses with filtering options
- ✅ View expense summary by category
- ✅ Delete expenses by ID
- ✅ Generate visualizations (pie charts, bar charts, time series)
- ✅ Persistent data storage (JSON)

### Installation & Setup

1. **Install Python Dependencies:**
   ```bash
   # Method 1: Run the installation script
   python install_dependencies.py
   
   # Method 2: Install manually
   pip install matplotlib pandas
   ```

2. **Run the Application:**
   ```bash
   python expense_tracker.py
   ```

### How to Use

1. **Starting the Application:**
   - Run `python expense_tracker.py`
   - You'll see a menu with options 1-6

2. **Adding an Expense:**
   - Choose option 1 from the menu
   - Enter the amount (e.g., `25.50`)
   - Enter a category (e.g., `Food`, `Transport`, `Entertainment`)
   - Add an optional description

3. **Viewing Expenses:**
   - Option 2: List all expenses (shows recent expenses first)
   - Option 3: Show summary by category with totals

4. **Data Visualization:**
   - Option 5: Generate charts and graphs
   - Requires matplotlib and pandas to be installed

5. **Managing Expenses:**
   - Option 4: Delete an expense by its ID number

### Data Storage
- Expenses are stored in `expenses.json` file
- Data persists between sessions
- File is automatically created when you add your first expense

### Example Usage Flow
```
1. Add Expense → Amount: 15.50 → Category: Food → Description: Lunch
2. Add Expense → Amount: 45.00 → Category: Transport → Description: Gas
3. Show Summary → See totals by category
4. Generate Visualization → View charts and statistics
```

### Requirements
- Python 3.6+
- matplotlib (for visualizations)
- pandas (for data analysis)

### Troubleshooting
- If visualizations don't work, run `python install_dependencies.py`
- Make sure all files are in the same directory
- On some systems, you might need to install tkinter for matplotlib:
  ```bash
  # Ubuntu/Debian
  sudo apt-get install python3-tk
  # macOS with Homebrew
  brew install python-tk
  ```

The application provides a simple yet powerful way to track and analyze your expenses with beautiful visualizations!