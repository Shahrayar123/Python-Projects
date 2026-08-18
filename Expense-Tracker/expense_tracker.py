import json

FILE_NAME = "expenses.json"


def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_expenses():
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense():
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    save_expenses()

    print("Expense added successfully!")


def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\n--- Expenses ---")

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. "
            f"₹{expense['amount']:.2f} | "
            f"{expense['category']} | "
            f"{expense['description']}"
        )


def view_total():
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Expenses: ₹{total:.2f}")


def delete_expense():
    if not expenses:
        print("No expenses to delete.")
        return

    view_expenses()

    while True:
        try:
            choice = int(input("Enter expense number to delete: "))

            if 1 <= choice <= len(expenses):
                deleted_expense = expenses.pop(choice - 1)
                save_expenses()

                print(
                    f"Deleted: {deleted_expense['category']} - "
                    f"₹{deleted_expense['amount']:.2f}"
                )
                break

            print("Invalid expense number.")

        except ValueError:
            print("Please enter a valid number.")


def main():
    global expenses

    expenses = load_expenses()

    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            view_total()

        elif choice == "4":
            delete_expense()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-5.")



if __name__ == "__main__":
    main()