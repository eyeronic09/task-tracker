import sys
import json
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
    
    new_task = {
        "id": counter + 1,
        "name": tasknames,
        "status": "not done"
    }
    tasks.append(new_task)
    data["counter"] = counter + 1
    saveTasktoJson(data)
    print(f"Task '{tasknames}' added successfully.")

def updateTask(task_id, new_name):
    data = loadTasks()
    tasks = data["tasks"]
    task_found = False

    for task in tasks:
        if task["id"] == task_id:
            task["name"] = new_name
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




def listTasks():
    data = loadTasks()
    tasks = data["tasks"]
    if tasks:
        for task in tasks:
            print(f"task ID:{task["id"]} , task name {task["name"]} , task status{task["name"]} ")
    else:
        print("no task found.")


        
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

    elif command == "list":
        listTasks()

    else:
        print("Invalid command or arguments.")
else:
    print("Usage: python app.py <command> [arguments]")