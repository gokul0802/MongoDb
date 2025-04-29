from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["library_system"]
books = db["books"]

def add_book():
    title = input("Book Title: ")
    author = input("Author: ")
    available = True

    books.insert_one({"title": title, "author": author, "available": available})
    print("Book added!\n")

def borrow_book():
    title = input("Enter title to borrow: ")
    book = books.find_one({"title": title, "available": True})
    if book:
        books.update_one({"_id": book["_id"]}, {"$set": {"available": False}})
        print("Book borrowed!\n")
    else:
        print("Book not available.\n")

def return_book():
    title = input("Enter title to return: ")
    book = books.find_one({"title": title, "available": False})
    if book:
        books.update_one({"_id": book["_id"]}, {"$set": {"available": True}})
        print("Book returned!\n")
    else:
        print("Book not found or already available.\n")

def view_books():
    all_books = books.find()
    print("\nLibrary Catalog:\n----------------")
    for book in all_books:
        status = "Available" if book["available"] else "Borrowed"
        print(f"{book['title']} by {book['author']} - {status}")
    print()

def main():
    while True:
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Exit")
        choice = input("Choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            borrow_book()
        elif choice == '3':
            return_book()
        elif choice == '4':
            view_books()
        elif choice == '5':
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()
