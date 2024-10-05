## Simple Expense Tracker

A command-line expense tracking application with data visualization built in Python.

### Features
- ✅ Add expenses with category and description
- 📝 View all expenses or filter by category
- 📊 View expense summary by category
- 📈 Visualize expenses with pie charts
- 🗑️ Delete expenses by ID
- 💾 Persistent data storage (JSON)

### Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   Or run the installation script:
   ```bash
   python install.py
   ```

2. **(Optional) Create sample data:**
   ```bash
   python quick_start.py
   ```

### Usage

**Start the application:**
```bash
python expense_tracker.py
```

**Menu Options:**
1. **Add Expense** - Record a new expense with amount, category, and description
2. **View All Expenses** - Display all recorded expenses
3. **View Expenses by Category** - Filter and view expenses by specific category
4. **Expense Summary** - Show total expenses grouped by category
5. **Visualize Expenses** - Display a pie chart of expense distribution
6. **Delete Expense** - Remove an expense by its ID
7. **Exit** - Quit the application

### Example Usage

1. **Adding an expense:**
   ```
   Enter amount: $25.50
   Enter category: Food
   Enter description: Lunch
   ```

2. **Viewing summary:**
   The application will display totals by category and overall spending.

3. **Visualization:**
   A pie chart will open showing the distribution of your expenses across categories.

### Data Storage

Expenses are stored in `expenses.json` file in the same directory. The data persists between sessions.

### Requirements

- Python 3.6+
- matplotlib (for visualization)

### File Structure
- `expense_tracker.py` - Main application
- `requirements.txt` - Dependencies
- `install.py` - Installation helper
- `quick_start.py` - Sample data generator
- `expenses.json` - Data file (created automatically)

Enjoy tracking your expenses! 💰