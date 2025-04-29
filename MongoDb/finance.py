from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["finance_tracker"]
expenses = db["expenses"]

def add_expense():
    category = input("Enter category: ")
    amount = input("Enter amount: ")
    description = input("Enter description (optional): ")

    try:
        amount = float(amount)
    except ValueError:
        print("Amount must be a number!")
        return

    expense = {
        "category": category,
        "amount": amount,
        "description": description
    }
    expenses.insert_one(expense)
    print("Expense added successfully!\n")

def view_expenses():
    all_expenses = expenses.find()
    total = 0
    print("\nYour Expenses:\n----------------")
    for exp in all_expenses:
        print(f"{exp['category']} - ${exp['amount']:.2f} - {exp.get('description', '')}")
        total += exp['amount']
    print(f"\nTotal Spent: ${total:.2f}\n")

def main():
    while True:
        print("===== Personal Finance Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Enter choice (1/2/3): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()
