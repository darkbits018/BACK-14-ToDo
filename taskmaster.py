import json
import os
import sys

TASK_FILE = "tasks.json"


def load_task():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=1)


def add_task(description):
    tasks = load_task()
    new_id = max([task["id"] for task in tasks], default=0) + 1
    tasks.append({"id": new_id, "description": description, "status": "todo"})
    save_tasks(tasks)
    print(f"Task added with ID {new_id}")


def update_task(task_id, new_description):
    tasks = load_task()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            save_tasks(tasks)
            print(f"task {task_id} updated")
            return
    print(f"No task found with ID (task_id")


def delete_task(task_id):
    tasks = load_task()
    updated_tasks = [task for task in tasks if task["id"] != task_id]
    if len(tasks) == len(updated_tasks):
        print(f"No tasks found with ID {task_id}")
    else:
        save_tasks(updated_tasks)
        print(f"Task {task_id} deleted")


def mark_task(task_id, status):
    # Ensure the provided status is valid
    if status not in {"todo", "in progress", "done"}:
        print("Status must be 'todo', 'in progress', or 'done'")
        return

    tasks = load_task()  # Load the existing tasks from JSON
    task_found = False  # Flag to check if task with given ID was found

    for task in tasks:
        if task["id"] == task_id:  # Locate the task by ID
            task["status"] = status  # Update the status
            task_found = True
            break  # Exit loop after finding the task

    if task_found:
        save_tasks(tasks)  # Save the updated tasks list back to the JSON file
        print(f"Task {task_id} marked as {status}.")
    else:
        print(f"No task found with ID {task_id}")


def list_tasks(status=None):
    tasks = load_task()

    if status:
        tasks = [task for task in tasks if task["status"] == status]
    if not tasks:
        print("No tasks found")
        return
    print(f"{'ID':<5} {'Description':<30} {'status':<15}")
    print("-" * 50)

    for task in tasks:
        print(
            f"{task.get('id', 'N/A'):<5} {task.get('description', 'No description'):<30} {task.get('status', 'No status'):<15}")

def print_help():
    print("\nTask Tracker CLI - Command Reference")
    print("-" * 40)
    print("add <description>                : Add a new task with the given description.")
    print("update <id> <new description>    : Update the description of a task with the given ID.")
    print("delete <id>                      : Delete the task with the given ID.")
    print("mark <id> <status>               : Update the status of a task with the given ID to 'todo', 'in progress', "
          "or 'done'.")
    print("list                             : List all tasks.")
    print("list done                        : List all tasks that are done.")
    print("list not done                    : List all tasks that are not done.")
    print("list in progress                 : List all tasks that are in progress.")
    print("help                             : Show this help message.")
    print("\nExample Usage:")
    print("  python taskmaster.py add \"Buy groceries\"")
    print("  python taskmaster.py update 1 \"Buy groceries and cook dinner\"")
    print("  python taskmaster.py mark 1 done\n")



def main():
    args = sys.argv[1:]
    if args:
        command = args[0]

        if command == "help":
            print_help()

        elif command == "add":
            if len(args) > 1:
                add_task(" ".join(args[1:]))
            else:
                print("Please provide a description for the task.")
        elif command == "update":
            if len(args) > 2:
                try:
                    task_id = int(args[1])
                    new_description = " ".join(args[2:])
                    update_task(task_id, new_description)
                except ValueError:
                    print("Task ID must be integer")
            else:
                print("Please provide both task ID and a new description")
        elif command == "delete":
            if len(args) > 1:
                try:
                    task_id = int(args[1])
                    delete_task(task_id)
                except ValueError:
                    print("Task ID must be an integer")
            else:
                print("Please provide a task ID to delete")
        elif command == "mark":
            if len(args) > 2:
                try:
                    task_id = int(args[1])
                    status = args[2].lower()  # Accept status as case-insensitive
                    mark_task(task_id, status)
                except ValueError:
                    print("Task ID must be an integer.")
            else:
                print("Please provide both a task ID and a status (todo, in progress, done).")
        elif command == "list":
            if len(args) > 1:
                status_arg = args[1].lower()
                if status_arg == "done":
                    list_tasks("done")
                elif status_arg == "not_done":
                    list_tasks("todo")
                elif status_arg == "in_progress":
                    list_tasks("in progress")
                else:
                    print("Unknown status. Use 'done', 'not done', or 'in progress'.")
            else:
                list_tasks()  # List all tasks if no status is specified
        else:
            print("Unknown command")
    else:
        print("Please provide a command")


if __name__ == "__main__":
    main()
