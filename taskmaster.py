import click
import json
from datetime import datetime

TASK_FILE = 'db.json'


def load_tasks():
    try:
        with open(TASK_FILE, 'r') as file:
            content = file.read().strip()
            if not content:
                return []
            return json.loads(content)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)


def generate_task_id(tasks):
    """Generate a new task ID"""
    if not tasks:
        return 1
    max_id = max(task['id'] for task in tasks)
    return max_id + 1


@click.group()
def cli():
    """BACK-14 ToDo """


@cli.command()
def add():
    title = click.prompt('Enter task title')
    description = click.prompt('Enter task description')
    # due_date = click.prompt('Enter due date (YYYY-MM-DD)', default='')

    """Add new Task"""
    tasks = load_tasks()
    task_id = generate_task_id(tasks)

    new_tasks = {
        'id': task_id,
        'title': title,
        'description': description,
        # 'due_date': due_date,
        'status': 'pending'
    }
    tasks.append(new_tasks)
    save_tasks(tasks)
    click.echo(f"Task '{title}' added successfully")


@cli.command()
def list():
    """List all tasks"""
    tasks = load_tasks()
    if not tasks:
        click.echo("No tasks Found")
    else:
        for task in tasks:
            click.echo(f"{task['id']}: {task['title']} - {task['description']}  - {task['status']}")
            # - {task['due_date']}


@cli.command()
@click.argument('task_id', type=int)
def complete(task_id):
    """Mark as Completed"""
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'completed'
            save_tasks(tasks)
            click.echo(f"Task '{task['title']}' marked as completed")
            return
        click.echo(f"Task with {task_id} not found")


if __name__ == '__main__':
    cli()
