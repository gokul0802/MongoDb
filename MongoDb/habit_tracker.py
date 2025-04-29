from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["habit_tracker"]
habits = db["habits"]

def mark_habit():
    habit = input("Enter habit name: ")
    today = datetime.now().date()

    habits.insert_one({
        "habit": habit,
        "date": today
    })
    print("Habit marked for today!\n")

def view_habit_progress():
    habit_name = input("Habit to check: ")
    progress = habits.find({"habit": habit_name})

    print(f"\nProgress for {habit_name}:\n----------------")
    for record in progress:
        print(record['date'])

def main():
    while True:
        print("1. Mark Habit")
        print("2. View Habit Progress")
        print("3. Exit")
        choice = input("Choice: ")

        if choice == '1':
            mark_habit()
        elif choice == '2':
            view_habit_progress()
        elif choice == '3':
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()
