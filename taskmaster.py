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
    if status not in {"todo", "in progress", "done"}:
        print("status must be 'todo', 'in progress', or 'done'")
        return
    tasks = load_task()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] == status
            save_tasks(tasks)
            print(f"Task {task_id} marked as {status}")
            return
    print(f"No task found with ID {task_id}")


def main():
    args = sys.argv[1:]
    if args:
        command = args[0]

        if command == "add":
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
            if len(args)>1:
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
        else:
            print("Unknown command")
    else:
        print("Please provide a command")


if __name__ == "__main__":
    main()
