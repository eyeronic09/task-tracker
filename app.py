import sys , json



def addlist(task_list, new_tasks):
    """
    Adds new tasks to the task list.

    Args:
        task_list (list): The current list of tasks.
        new_tasks (list): The new tasks to add.

    Returns:
        list: The updated task list.
    """
    task_list.extend(new_tasks)
    print(f"Tasks added successfully: {new_tasks}")
    print("Current Tasks List:", task_list)


    return task_list

# Main Program
if len(sys.argv) > 2 and sys.argv[1] == "add":
    # Collect all tasks from the command-line arguments (skipping the script name and command)
    new_tasks = sys.argv[2:]
    tasks = addlist(tasks, new_tasks)
else:
    print("Usage: python script.py add <task1> <task2> ...")


