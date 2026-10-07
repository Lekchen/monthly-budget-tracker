import json
print("==============================")
print(" MONTHLY BUDGET TRACKER")
print("==============================")

expenses = []
monthly_income = 0
budgets = {} 
try:
    with open("budget_data.json", "r") as file:
        data = json.load(file)

    monthly_income = data["monthly_income"]
    budgets = data["budgets"]
    expenses = data["expenses"]

    print("Saved data loaded successfully!")

except FileNotFoundError:
    print("No saved data found.")
while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Set Monthly Income")
    print("4. Set Category Budget")
    print("5. View Budget Summary")
    print("6. Save Data")
    print("7. Exit")

    choice = input("enter your choice: ")
    if choice == "1":
        description = input("Enter description: ")
        category = input("Enter category: ").lower()
        amount = float(input("Enter amount: $"))
        expense ={
            "description": description,
            "category": category,
            "amount": amount

        }
        expenses.append(expense)
        print("Expense added successfully!")
    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses found.")
        else:
            print("==============================")
            print("        YOUR EXPENSES")
            print("==============================")
            total = 0
            for expense in expenses:
                print(expense["description"], "|", expense["category"], "|", f'${expense["amount"]:.2f}')
                total += expense["amount"]

            print("==============================")
            print("Total spent:", f"${total:.2f}")
    elif choice == "3":
        monthly_income = float(input("Enter your monthly income: $"))
        print("Monthy income set sucessfully!")
    elif choice == "4":
        category = input("Enter category: ").lower()
        budget_amount = float(input("Enter budget amount: $"))
        budgets[category] = budget_amount
        print("budget set successfully")
    elif choice == "5":
        print("========================")
        print("      BUDGET SUMMARY    ")
        print("========================")

        print("Monthly Income:", f"${monthly_income:.2f}")
        total_budget = 0
        for category in budgets:
            spent = 0
            for expense in expenses:
                if expense["category"] == category:
                    spent += expense["amount"]
            remaining = budgets[category] - spent
            print(
                category,
                "| Budget:", f"${budgets[category]:.2f}",
                "| Spent:", f"${spent:.2f}",
                "| Remaining:", f"${remaining:.2f}"
)
            total_budget += budgets[category]
        print("Total Budget:", f"${total_budget:.2f}")
    elif choice == "6":
        data = {
            "monthly_income": monthly_income,
            "budgets": budgets,
            "expenses": expenses
        }
        with open("budget_data.json", "w") as file:
            json.dump(data, file, indent=4)
        print("Data saved successfully!")
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")



