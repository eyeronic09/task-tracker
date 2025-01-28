import os , sys , json

file_path = "tasks.json"  # Defining the path to the JSON file where tasks are stored

# Load tasks from the JSON file
def loadTasks():
    if not os.path.exists(file_path):  # Check if the JSON file exists
        return {"tasks": [], "counter": 0}  # Return an empty structure if the file doesn't exist
    with open(file_path, "r") as file:  # Open the JSON file in read mode
        try:
            return json.load(file)  # Load and return the JSON data
        except json.JSONDecodeError:
            return {"tasks": [], "counter": 0}  # Return an empty structure if the file is invalid

# Save tasks to the JSON file
def saveTasktoJson(data):
    with open(file_path, "w") as file:  # Open the JSON file in write mode
        json.dump(data, file, indent=4)  # Write the JSON data to the file with indentation

# Add a new task
def addTask(tasknames):
    data = loadTasks()  # Load existing tasks
    tasks = data["tasks"]  # Get the list of tasks
    counter = data["counter"]  # Get the current counter value
  
    new_task = {
        "id": counter + 1,  # Assign a new ID by incrementing the counter
        "name": tasknames,  # Set the task name
        "status": "not done"  # Set the initial status of the task
    }
    tasks.append(new_task)  # Add the new task to the list
    data["counter"] = counter + 1  # Increment the counter
    saveTasktoJson(data)  # Save the updated tasks and counter to the JSON file
    print(f"Task '{tasknames}' added successfully.")  # Print a success message

# Update an existing task by ID
def updateTask(task_id, new_name):
    data = loadTasks()  # Load existing tasks
    tasks = data["tasks"]  # Get the list of tasks
    task_found = False  # Initialize a flag to check if the task is found

    for task in tasks:
        if task["id"] == task_id:  # Check if the current task ID matches the given ID
            task["name"] = new_name  # Update the task name
            task_found = True  # Set the flag to True
            break  # Exit the loop

    if task_found:
        saveTasktoJson(data)  # Save the updated tasks to the JSON file
        print(f"Task ID {task_id} updated to '{new_name}'.")  # Print a success message
    else:
        print(f"Task ID {task_id} not found.")  # Print a message if the task is not found

# Delete a task by ID
def tasksDelete(task_id):
    data = loadTasks()  # Load existing tasks
    tasks = data["tasks"]  # Get the list of tasks
    task_found = False  # Initialize a flag to check if the task is found

    for i in range(len(tasks)):
        if tasks[i]["id"] == task_id:  # Check if the current task ID matches the given ID
            tasks.pop(i)  # Remove the task from the list
            task_found = True  # Set the flag to True
            break  # Exit the loop

    if task_found:
        saveTasktoJson(data)  # Save the updated tasks to the JSON file
        print(f"Task with ID {task_id} deleted successfully.")  # Print a success message
    else:
        print(f"Task with ID {task_id} not found.")  # Print a message if the task is not found

# Handle CLI commands
if len(sys.argv) > 1:  # Check if there are command-line arguments
    command = sys.argv[1]  # Get the command

    if command == "add" and len(sys.argv) > 2:
        taskname = " ".join(sys.argv[2:])  # Concatenate the task name from the arguments
        addTask(taskname)  # Add the task

    elif command == "update" and len(sys.argv) > 3 and sys.argv[2].isnumeric():
        task_id = int(sys.argv[2])  # Get the task ID from the arguments
        new_name = " ".join(sys.argv[3:])  # Concatenate the new task name from the arguments
        updateTask(task_id, new_name)  # Update the task

    elif command == "delete" and len(sys.argv) > 2 and sys.argv[2].isnumeric():
        task_id = int(sys.argv[2])  # Get the task ID from the arguments
        tasksDelete(task_id)  # Delete the task

    else:
        print("Invalid command or arguments.")  # Print an error message for invalid commands
else:
    print("Usage: python app.py <command> [arguments]")  # Print usage instructions if no arguments are provided
