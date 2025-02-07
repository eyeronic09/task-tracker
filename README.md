 # Task Management CLI Application from roadmap.sh https://roadmap.sh/projects/task-tracker
This is a simple command-line task management application built with Python. It allows users to add, update, delete, list, and mark tasks as completed.

## Features
- Add tasks
- Update task names
- Delete tasks
- List all tasks
- List completed tasks
- Update task status
- Persistent storage using a JSON file

## Requirements
- Python 3.x

## Installation
1. Clone the repository or copy the script to your local machine.
2. Ensure you have Python installed.
3. No additional dependencies are required.

## Usage
Run the script using the command-line interface with the following commands:

### Add a Task
```sh
python app.py add "Task Name"
```
Example:
```sh
python app.py add "Buy groceries"
```

### Update a Task Name
```sh
python app.py update <task_id> "New Task Name"
```
Example:
```sh
python app.py update 1 "Buy vegetables"
```

### Delete a Task
```sh
python app.py delete <task_id>
```
Example:
```sh
python app.py delete 1
```

### List All Tasks
```sh
python app.py list
```

### List Completed Tasks
```sh
python app.py list-Done
```

### Update Task Status
```sh
python app.py update-status <task_id> "new_status"
```
Example:
```sh
python app.py update-status 1 "done"
```

## File Storage
Tasks are stored in a `tasks.json` file, which maintains task details such as:
- Task ID
- Task Name
- Status
- Created Time
- Last Updated Time

## Notes
- Ensure `tasks.json` is present in the same directory as the script or it will be created automatically.
- Task IDs are assigned sequentially.
- Task status can be updated to "done" or any custom status.

## License
This project is open-source. Feel free to modify and improve it!

