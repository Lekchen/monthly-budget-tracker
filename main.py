print("==============================")
print(" MONTHLY BUDGET TRACKER")
print("==============================")

print("1. Add Expense")
print("2. View Expenses")
print("3. Exit")

choice = input("enter your choice: ")

if choice == "1":
    print("Add Expense")
elif choice == "2":
    print("View Expenses")
elif choice == "3":
    print("Goodbye!")
else:
    print("Invalid choice")