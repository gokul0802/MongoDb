from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["Login_System"]
users = db["Users"]

# Sign up (register)
def signup(username, password):
    users.insert_one({"username": username, "password": password})

# Login (check credentials)
def login(username, password):
    user = users.find_one({"username": username, "password": password})
    if user:
        print("Login Successful!")
    else:
        print("Invalid credentials.")

# Example usage
signup("admin", "admin123")
login("admin", "admin123")
