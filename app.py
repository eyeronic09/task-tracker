import sys
import json
import os

file_path = "tasks.json"

def loadTasks():
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def updateTask(task_id , new_name):
    tasks = loadTasks()
    for task in tasks:
        if task["id"] == task_id:
            task["name"] = new_name
            saveTasktoJson(task)
            print(f"Task ID {task_id} updated successfully to '{new_name}'.")
            return
    print(f"Task ID not {task_id} found")
            


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


