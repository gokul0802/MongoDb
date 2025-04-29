from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/") 
db = client["gokul"]
collection = db["prac1"]

def insert_user(name, age, email):
    user = {"name": name, "age": age, "email": email}
    result = collection.insert_one(user)
    print(f"Inserted user with ID: {result.inserted_id}")

def find_users():
    users = collection.find()
    print("All Users:")
    for user in users:
        print(user)

def update_user(name, new_email):
    result = collection.update_one({"name": name}, {"$set": {"email": new_email}})
    print(f"Matched: {result.matched_count}, Modified: {result.modified_count}")

def delete_user(name,):
    result = collection.delete_one({"name": name})
    print(f"Deleted: {result.deleted_count}")

#insert_user("Gokul","21","gokul501.gk@gmail.com")
#insert_user("Sarthak", "22", "sarthak@gmail.com")

#find_users()

#update_user("Gokul", "Gokul@gmail.com")
#find_users()

#delete_user("Gokul")
#delete_user("Gokul")

#delete_user("Sarthak")

#find_users()

#delete_user("Sarthak")
#delete_user("Sarthak")

find_users() 



