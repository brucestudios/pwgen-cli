import argparse
import sys
from .todo_manager import TodoManager

def main():
    parser = argparse.ArgumentParser(description="Todo CLI")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Add command
    parser_add = subparsers.add_parser('add', help='Add a new task')
    parser_add.add_argument('task', type=str, help='Task description')

    # List command
    parser_list = subparsers.add_parser('list', help='List all tasks')

    # Complete command
    parser_complete = subparsers.add_parser('complete', help='Mark a task as complete')
    parser_complete.add_argument('index', type=int, help='Task index to complete')

    # Delete command
    parser_delete = subparsers.add_parser('delete', help='Delete a task')
    parser_delete.add_argument('index', type=int, help='Task index to delete')

    args = parser.parse_args()

    manager = TodoManager()

    if args.command == 'add':
        manager.add_task(args.task)
        print(f'Added task: "{args.task}"')
    elif args.command == 'list':
        tasks = manager.list_tasks()
        if not tasks:
            print("No tasks.")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "✓" if task['completed'] else " "
                print(f"{i}. [{status}] {task['description']}")
    elif args.command == 'complete':
        try:
            manager.complete_task(args.index - 1)  # convert to 0-based
            print(f"Task {args.index} marked as complete.")
        except IndexError:
            print(f"Error: Task index {args.index} out of range.")
            sys.exit(1)
    elif args.command == 'delete':
        try:
            deleted = manager.delete_task(args.index - 1)
            print(f"Deleted task: {deleted['description']}")
        except IndexError:
            print(f"Error: Task index {args.index} out of range.")
            sys.exit(1)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()