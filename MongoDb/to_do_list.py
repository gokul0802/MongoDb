from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["TO_DO_LIST"]
tasks = db["List"]

# Add a task
task = {"task": "Finish homework", "status": "Pending"}
tasks.insert_one(task)

# Mark task as completed
tasks.update_one({"task": "Finish homework"}, {"$set": {"status": "Completed"}})

# Show all tasks
for t in tasks.find():
    print(t)
