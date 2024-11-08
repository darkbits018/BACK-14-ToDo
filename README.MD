## [Features](https://roadmap.sh/projects/task-tracker)
- Add, update, and delete tasks.
- Mark tasks as "todo", "in progress", or "done".
- List all tasks or filter tasks by their status.

## Requirements
- Python 3.x

## Setup
1. Clone the repository or download the `taskmaster.py` file.
2. Run the following command to initialize the project:

   ```bash
   python taskmaster.py help

### Usage

### Available Commands

| Command                           | Description                                                                 |
|-----------------------------------|-----------------------------------------------------------------------------|
| `add <description>`               | Adds a new task with the given description.                                 |
| `update <id> <new description>`   | Updates the description of a task with the specified ID.                    |
| `delete <id>`                     | Deletes the task with the specified ID.                                     |
| `mark <id> <status>`              | Marks a task with the specified ID as "todo", "in progress", or "done".     |
| `list`                            | Lists all tasks.                                                            |
| `list done`                       | Lists all tasks that are marked as "done".                                  |
| `list not done`                   | Lists all tasks that are marked as "not done".                              |
| `list in progress`                | Lists all tasks that are marked as "in progress".                           |
| `help`                            | Displays this help message with all available commands.                     |

### Examples

1. **Add a Task**
   ```bash
   python taskmaster.py add "Buy groceries"

2. **Update a Task**
   ```bash
   python taskmaster.py update 1 "Buy groceries and cook dinner"

3. **Delete a Task**
   ```bash
   python taskmaster.py delete 1

4. **Mark a Task as Done**
   ```bash
   python taskmaster.py mark 1 done

5. **List All Tasks**
   ```bash
   python taskmaster.py list

6. **List by Status**
 - List Not Done Tasks:
   ```bash
   python taskmaster.py list not done
 - List In progress tasks:
   ```bash
   python taskmaster.py list in_progress
 - List Done Tasks:
   ```bash
   python taskmaster.py list done

