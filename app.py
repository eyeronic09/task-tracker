import sys
import json , time
import os

file_path = "tasks.json"

def loadTasks():
    if not os.path.exists(file_path):
        return {"tasks": [], "counter": 0}
    with open(file_path, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {"tasks": [], "counter": 0}

def saveTasktoJson(data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def addTask(tasknames):
    data = loadTasks()
    tasks = data["tasks"]
    counter = data["counter"]
    currentTimeAndDate = time.ctime()
    
    new_task = {
        "id": counter + 1,
        "name": tasknames,
        "status": "not done",
        "created Time" : currentTimeAndDate,
        "last updated at" : currentTimeAndDate
    }
    tasks.append(new_task)
    data["counter"] = counter + 1
    saveTasktoJson(data)
    print(f"Task '{tasknames}' added successfully.")

def updateTask(task_id, new_name):
    data = loadTasks()
    tasks = data["tasks"]
    task_found = False
    lastUpdateTime = time.ctime()

    for task in tasks:
        if task["id"] == task_id:
            task["name"] = new_name
            task["last updated at"] = lastUpdateTime
            task_found = True
            break

    if task_found:
        saveTasktoJson(data)
        print(f"Task ID {task_id} updated to '{new_name}'.")
    else:
        print(f"Task ID {task_id} not found.")

def tasksDelete(task_id):
    data = loadTasks()
    tasks = data["tasks"]
    task_found = False

    for i in range(len(tasks)):
        if tasks[i]["id"] == task_id:
            tasks.pop(i)
            task_found = True
            break

    if task_found:
        saveTasktoJson(data)
        print(f"Task with ID {task_id} deleted successfully.")
    else:
        print(f"Task with ID {task_id} not found.")

def listAll_task():
    data = loadTasks()
    tasks = data["tasks"]
    if tasks:
        for task in tasks:
            print(f"Task ID: {task['id']}, Name: {task['name']}, Status: {task['status']}, Created: {task['created Time']}, Last Updated: {task['last updated at']}")
    else:
        print("no task found.")

def completedTask():
    data = loadTasks()
    tasks = data["tasks"]
    if tasks :
        for task in tasks:
            if task["status"] == "done":
                print(f"task status {task["status"]}")
    else:
        print("no task found")

def updateStatus(new_status, task_id):
    data = loadTasks()
    tasks = data["tasks"]
    task_found = False

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            task_found = True
            break
    if task_found:
        saveTasktoJson(data)
        print(f"Task ID {task_id} updated to '{new_status}'.")
    else:
        print(f"Task ID {task_id} not found.")

    

# Handle CLI commands
if len(sys.argv) > 1:
    command = sys.argv[1]

    if command == "add" and len(sys.argv) > 2:
        taskname = " ".join(sys.argv[2:])
        addTask(taskname)

    elif command == "update" and len(sys.argv) > 3 and sys.argv[2].isnumeric():
        task_id = int(sys.argv[2])
        new_name = " ".join(sys.argv[3:])
        updateTask(task_id, new_name)

    elif command == "delete" and len(sys.argv) > 2 and sys.argv[2].isnumeric():
        task_id = int(sys.argv[2])
        tasksDelete(task_id)

    elif command == "list" and len(sys.argv) == 2:
        listAll_task()
    
    elif command == "list-Done" and len(sys.argv) == 2:
        completedTask()
    
    elif command == "update-status" and len(sys.argv) > 2 and sys.argv[2].isnumeric():
        task_id = int(sys.argv[2])
        new_status = " ".join(sys.argv[3:])
        updateStatus(new_status, task_id) 

    else:
        print("Invalid command or arguments.")
else:
    print("Usage: python app.py <command> [arguments]")