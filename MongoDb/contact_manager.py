from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["contact_manager"]
contacts = db["contacts"]

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")

    contacts.insert_one({"name": name, "phone": phone, "email": email})
    print("Contact saved!\n")

def view_contacts():
    all_contacts = contacts.find()
    print("\nContacts List:\n----------------")
    for c in all_contacts:
        print(f"{c['name']} - {c['phone']} - {c['email']}")
    print()

def search_contact():
    name = input("Enter name to search: ")
    contact = contacts.find_one({"name": {"$regex": name, "$options": "i"}})

    if contact:
        print(f"Found: {contact['name']} - {contact['phone']} - {contact['email']}\n")
    else:
        print("Contact not found.\n")

def main():
    while True:
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")
        choice = input("Choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()
