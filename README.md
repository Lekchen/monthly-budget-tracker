# Monthly Budget Tracker

A Python application for tracking monthly expenses, managing category budgets, and monitoring personal spending. The program stores financial data locally using JSON and can automatically generate formatted Excel reports with charts.

## Features

- Add expenses with a date, description, category, and amount
- View all recorded expenses
- Calculate total spending
- Set monthly income
- Create budgets for different spending categories
- Track spending for each budget category
- Calculate remaining budget amounts
- Calculate total spending and savings
- Validate dates and monetary inputs
- Save financial data using JSON
- Automatically load saved data when the program starts
- Generate formatted Excel reports
- Generate a Budget vs. Spent bar chart
- Generate a Spending by Category pie chart

## Technologies Used

- Python
- JSON
- openpyxl
- Microsoft Excel
- Git
- GitHub

## How It Works

The program provides a command-line menu with the following options:

1. Add Expense
2. View Expenses
3. Set Monthly Income
4. Set Category Budget
5. View Budget Summary
6. Save Data
7. Generate Excel Report
8. Exit

Users can enter their monthly income, create spending budgets for different categories, and record individual expenses.

The program calculates how much has been spent in each category and how much of the category budget remains.

## Data Storage

The application stores data locally in:

`budget_data.json`

The JSON file stores:

- Monthly income
- Category budgets
- Expenses

When the application starts, previously saved information is automatically loaded.

The `budget_data.json` file is excluded from GitHub using `.gitignore` so personal financial information is not uploaded to the repository.

## Excel Report

The program can automatically generate:

`monthly_budget_report.xlsx`

The Excel workbook contains two worksheets:

### Expenses

The Expenses worksheet contains:

- Date
- Description
- Category
- Amount

### Budget Summary

The Budget Summary worksheet contains:

- Category
- Budget
- Amount spent
- Remaining budget
- Monthly income
- Total budget
- Total spending
- Remaining budget
- Savings

The report also includes:

- Budget vs. Spent bar chart
- Spending by Category pie chart

## Input Validation

The application validates user input to help prevent invalid data.

For example:

- Expense amounts must be valid numbers greater than $0
- Monthly income must be greater than $0
- Category budgets must be greater than $0
- Dates must be valid and use the `YYYY-MM-DD` format

Invalid input is handled without terminating the program.

## Installation

Make sure Python is installed on your computer.

Install the required package:

```bash
pip install openpyxl
```

## Running the Program

Clone the repository:

```bash
git clone https://github.com/Lekchen/monthly-budget-tracker.git
```

Move into the project directory:

```bash
cd monthly-budget-tracker
```

Run the application:

```bash
python main.py
```

## Example

A user could set:

```text
Monthly Income: $2000

Food Budget: $300
Transportation Budget: $150
```

Then record expenses such as:

```text
2026-10-07 | Walmart | food | $42.50
2026-10-07 | Gas | transportation | $30.00
```

The program calculates spending and remaining budgets and can export the results to Excel.

## Future Improvements

Possible future improvements include:

- Monthly and yearly spending reports
- Search and filter expenses
- Edit and delete expenses
- Additional financial analytics
- Graphical user interface (GUI)
- Automatic monthly report generation

## Author

**Rinchen Gyeltshen**
