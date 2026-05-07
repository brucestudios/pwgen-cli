"""Command-line interface for the Markdown TODO app."""

import argparse
import sys
from .todo import TodoManager


def main() -> None:
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="A simple TODO manager that stores tasks in a Markdown file."
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # init command
    subparsers.add_parser("init", help="Initialize a new TODO file")

    # add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("task", help="The task description")

    # list command
    subparsers.add_parser("list", help="List all tasks")

    # complete command
    complete_parser = subparsers.add_parser("complete", help="Mark a task as complete")
    complete_parser.add_argument("index", type=int, help="The task number to complete")

    # remove command
    remove_parser = subparsers.add_parser("remove", help="Remove a task")
    remove_parser.add_argument("index", type=int, help="The task number to remove")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    manager = TodoManager()

    if args.command == "init":
        manager.init()
        print("TODO file initialized.")
    elif args.command == "add":
        manager.add(args.task)
        print(f'Added: "{args.task}"')
    elif args.command == "list":
        items = manager.list()
        if not items:
            print("No tasks found.")
        else:
            for i, (completed, text) in enumerate(items, 1):
                status = "x" if completed else " "
                print(f"{i}. [{status}] {text}")
    elif args.command == "complete":
        if manager.complete(args.index):
            print(f"Task {args.index} marked as complete.")
        else:
            print(f"Error: Task {args.index} not found.")
            sys.exit(1)
    elif args.command == "remove":
        if manager.remove(args.index):
            print(f"Task {args.index} removed.")
        else:
            print(f"Error: Task {args.index} not found.")
            sys.exit(1)


if __name__ == "__main__":
    main()