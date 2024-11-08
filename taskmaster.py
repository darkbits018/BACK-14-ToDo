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


def main():
    args = sys.argv[1:]
    if args and args[0] == "add":
        if len(args) > 1:
            add_task(" ".join(args[1:]))
        else:
            print("please provide description for task")


if __name__ == "__main__":
    main()
