import sys
import json
import os
import uuid

file_path = "tasks.json"

def loadTasks():
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def saveTasktoJson(tasks):
    with open(file_path, "w") as file:
        json.dump(tasks, file, indent=4)

def addTask(tasknames):
    tasks = loadTasks()
    task = {
        "id": str(uuid.uuid4()),
        "name": tasknames,
        "status": "not done"
    }
    tasks.append(task)
    saveTasktoJson(tasks)

if len(sys.argv) > 2 and sys.argv[1] == "add":
    new_task_name = " ".join(sys.argv[2:])
    addTask(new_task_name)
    print(f"Task '{new_task_name}' added successfully.")
else:
    print("Usage: python app.py add <task_name>")