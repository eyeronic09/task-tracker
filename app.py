import sys
import json
import os

file_path = "tasks.json"
"""
def loadTask just open the file and you can store or use it in variable 
"""
def loadTasks():
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def updateTask(task_id, new_name):
    tasks = loadTasks()
    task_found = False

    # Iterate over tasks and update the one with the matching ID
    for task in tasks:
        if task["id"] == task_id:
            task["name"] = new_name
            task_found = True
            break  # Exit loop after updating the task


    if task_found:
        saveTasktoJson(tasks)  # Save all tasks back to the JSON file
        print(f"Task ID {task_id} updated to '{new_name}'.")
    else:
        print(f"Task ID {task_id} not found.")
           


'''
yea so it generate unique id for each task and also check pervisos task id not generate the same 
'''
def get_id(tasks):
    return max((task["id"] for task in tasks), default=0) + 1

'''
open the file and add all the content , pretty self explainatory
'''
def saveTasktoJson(tasks):
    with open(file_path, "w") as file:
        json.dump(tasks, file, indent=4)

'''
add task with unique id and load task form the fuction 
'''
def addTask(tasknames):

    tasks = loadTasks()
    task = {
        "id":get_id(tasks),
        "name": tasknames
    }
    tasks.append(task)
    saveTasktoJson(tasks)

if len (sys.argv) > 1 :
    command = sys.argv[1]
    if command == "add" and len(sys.argv)>2:
        taskname = " ".join(sys.argv[2:])
        addTask(taskname)
    elif command == "update" and len(sys.argv) > 3 and sys.argv[2].isnumeric:
        task_id  = int(sys.argv[2])
        new_name = " ".join(sys.argv[3:])
        updateTask(task_id,new_name)