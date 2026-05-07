#!/usr/bin/env python3
import argparse
import json
import os
import sys
from pathlib import Path

DEFAULT_DATA_DIR = Path.home() / ".local" / "share" / "openclaw-todo"
DEFAULT_DATA_FILE = DEFAULT_DATA_DIR / "todos.json"

def ensure_data_dir():
    DEFAULT_DATA_DIR.mkdir(parents=True, exist_ok=True)

def load_todos():
    ensure_data_dir()
    if not DEFAULT_DATA_FILE.exists():
        return []
    try:
        with open(DEFAULT_DATA_FILE, 'r') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except (json.JSONDecodeError, OSError):
        return []

def save_todos(todos):
    ensure_data_dir()
    with open(DEFAULT_DATA_FILE, 'w') as f:
        json.dump(todos, f, indent=2)

def add_task(description):
    todos = load_todos()
    task = {
        "id": len(todos) + 1,
        "description": description,
        "completed": False
    }
    todos.append(task)
    save_todos(todos)
    print(f'Added task: "{description}"')

def list_todos():
    todos = load_todos()
    if not todos:
        print("No tasks found.")
        return
    for task in todos:
        status = "✓" if task["completed"] else " "
        print(f'{task["id"]}. [{status}] {task["description"]}')

def complete_task(task_id):
    todos = load_todos()
    for task in todos:
        if task["id"] == task_id:
            task["completed"] = True
            save_todos(todos)
            print(f'Task {task_id} marked as complete.')
            return
    print(f'Task with id {task_id} not found.')

def delete_task(task_id):
    todos = load_todos()
    for i, task in enumerate(todos):
        if task["id"] == task_id:
            del todos[i]
            # Reassign IDs to keep them sequential
            for j, t in enumerate(todos[i:], start=i):
                t["id"] = j + 1
            save_todos(todos)
            print(f'Task {task_id} deleted.')
            return
    print(f'Task with id {task_id} not found.')

def main():
    parser = argparse.ArgumentParser(description="A simple command-line todo list manager")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # add command
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("description", nargs="+", help="Task description")
    parser_add.set_defaults(func=lambda args: add_task(" ".join(args.description)))

    # list command
    parser_list = subparsers.add_parser("list", help="List all tasks")
    parser_list.set_defaults(func=lambda args: list_todos())

    # complete command
    parser_complete = subparsers.add_parser("complete", help="Mark a task as complete")
    parser_complete.add_argument("id", type=int, help="Task ID to complete")
    parser_complete.set_defaults(func=lambda args: complete_task(args.id))

    # delete command
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("id", type=int, help="Task ID to delete")
    parser_delete.set_defaults(func=lambda args: delete_task(args.id))

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)
    args.func(args)

if __name__ == "__main__":
    main()