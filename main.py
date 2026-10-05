print("==============================")
print(" MONTHLY BUDGET TRACKER")
print("==============================")

expenses = []
while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("enter your choice: ")
    if choice == "1":
        description = input("Enter description: ")
        category = input("Enter category: ")
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
                print(expense["description"], "|", expense["category"], "|", f'${expense["amount"]: .2f}')
                total += expense["amount"]

            print("==============================")
            print("Total spent:", f"${total:.2f}")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")



