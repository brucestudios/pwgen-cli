#!/usr/bin/env python3
"""
Awesome Todo CLI - A beautiful command-line todo list application
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta
from enum import Enum
from pathlib import Path
from typing import List, Optional

# Color support
try:
    from colorama import init, Fore, Back, Style
    init()
    COLORS_AVAILABLE = True
except ImportError:
    COLORS_AVAILABLE = False
    # Dummy color classes
    class Fore:
        RED = GREEN = YELLOW = BLUE = MAGENTA = CYAN = WHITE = RESET = ""
    class Back:
        RED = GREEN = YELLOW = BLUE = MAGENTA = CYAN = WHITE = RESET = ""
    class Style:
        BRIGHT = DIM = NORMAL = RESET_ALL = ""

class Priority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

    def __str__(self):
        return self.value

    @classmethod
    def from_string(cls, value: str):
        try:
            return cls(value.lower())
        except ValueError:
            return cls.MEDIUM

class TodoItem:
    def __init__(self, id: int, title: str, description: str = "", 
                 priority: Priority = Priority.MEDIUM, tags: List[str] = None,
                 due_date: Optional[datetime] = None, completed: bool = False,
                 created_at: Optional[datetime] = None):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.tags = tags or []
        self.due_date = due_date
        self.completed = completed
        self.created_at = created_at or datetime.now()

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority.value,
            'tags': self.tags,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'completed': self.completed,
            'created_at': self.created_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        due_date = None
        if data.get('due_date'):
            due_date = datetime.fromisoformat(data['due_date'])
        
        created_at = None
        if data.get('created_at'):
            created_at = datetime.fromisoformat(data['created_at'])
        
        return cls(
            id=data['id'],
            title=data['title'],
            description=data.get('description', ''),
            priority=Priority.from_string(data.get('priority', 'medium')),
            tags=data.get('tags', []),
            due_date=due_date,
            completed=data.get('completed', False),
            created_at=created_at
        )

    def is_overdue(self) -> bool:
        if self.due_date and not self.completed:
            return datetime.now() > self.due_date
        return False

    def days_until_due(self) -> Optional[int]:
        if self.due_date:
            delta = self.due_date - datetime.now()
            return delta.days
        return None

class TodoManager:
    def __init__(self, data_file: str = None):
        if data_file is None:
            home_dir = Path.home()
            self.data_file = home_dir / '.awesome-todo' / 'todos.json'
        else:
            self.data_file = Path(data_file)
        
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        self.todos: List[TodoItem] = []
        self.next_id = 1
        self.load_todos()

    def load_todos(self):
        if self.data_file.exists():
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.todos = [TodoItem.from_dict(item) for item in data.get('todos', [])]
                    self.next_id = data.get('next_id', 1)
            except (json.JSONDecodeError, KeyError):
                self.todos = []
                self.next_id = 1
        else:
            self.todos = []
            self.next_id = 1

    def save_todos(self):
        data = {
            'todos': [todo.to_dict() for todo in self.todos],
            'next_id': self.next_id
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)

    def add_todo(self, title: str, description: str = "", priority: Priority = Priority.MEDIUM,
                 tags: List[str] = None, due_date: Optional[datetime] = None) -> TodoItem:
        todo = TodoItem(
            id=self.next_id,
            title=title,
            description=description,
            priority=priority,
            tags=tags or [],
            due_date=due_date
        )
        self.todos.append(todo)
        self.next_id += 1
        self.save_todos()
        return todo

    def get_todo(self, id: int) -> Optional[TodoItem]:
        for todo in self.todos:
            if todo.id == id:
                return todo
        return None

    def list_todos(self, show_completed: bool = False, priority_filter: Priority = None,
                   tag_filter: str = None, search_term: str = None) -> List[TodoItem]:
        filtered_todos = self.todos
        
        if not show_completed:
            filtered_todos = [todo for todo in filtered_todos if not todo.completed]
        
        if priority_filter:
            filtered_todos = [todo for todo in filtered_todos if todo.priority == priority_filter]
        
        if tag_filter:
            filtered_todos = [todo for todo in filtered_todos if tag_filter in todo.tags]
        
        if search_term:
            search_lower = search_term.lower()
            filtered_todos = [todo for todo in filtered_todos 
                            if search_lower in todo.title.lower() or 
                               search_lower in todo.description.lower()]
        
        return sorted(filtered_todos, key=lambda x: (x.completed, x.priority.value, x.created_at))

    def complete_todo(self, id: int) -> bool:
        todo = self.get_todo(id)
        if todo:
            todo.completed = True
            self.save_todos()
            return True
        return False

    def remove_todo(self, id: int) -> bool:
        todo = self.get_todo(id)
        if todo:
            self.todos.remove(todo)
            self.save_todos()
            return True
        return False

    def update_todo(self, id: int, **kwargs) -> bool:
        todo = self.get_todo(id)
        if todo:
            for key, value in kwargs.items():
                if hasattr(todo, key):
                    setattr(todo, key, value)
            self.save_todos()
            return True
        return False

    def get_stats(self) -> dict:
        total = len(self.todos)
        completed = len([t for t in self.todos if t.completed])
        pending = total - completed
        overdue = len([t for t in self.todos if t.is_overdue()])
        
        priority_counts = {priority.value: 0 for priority in Priority}
        for todo in self.todos:
            priority_counts[todo.priority.value] += 1
        
        return {
            'total': total,
            'completed': completed,
            'pending': pending,
            'overdue': overdue,
            'priority_counts': priority_counts
        }

def format_priority(priority: Priority) -> str:
    if COLORS_AVAILABLE:
        colors = {
            Priority.LOW: Fore.GREEN,
            Priority.MEDIUM: Fore.YELLOW,
            Priority.HIGH: Fore.RED
        }
        color = colors.get(priority, Fore.WHITE)
        return f"{color}{priority.value.upper()}{Style.RESET_ALL}"
    return priority.value.upper()

def format_todo(todo: TodoItem, show_id: bool = True) -> str:
    # Status icon
    status = "✓" if todo.completed else "○"
    if COLORS_AVAILABLE:
        status_color = Fore.GREEN if todo.completed else Fore.CYAN
        status = f"{status_color}{status}{Style.RESET_ALL}"
    
    # Priority
    priority_str = format_priority(todo.priority)
    
    # Due date
    due_str = ""
    if todo.due_date:
        if todo.is_overdue():
            due_str = f"{Fore.RED if COLORS_AVAILABLE else ''}[OVERDUE: {todo.due_date.strftime('%Y-%m-%d')}]{Style.RESET_ALL if COLORS_AVAILABLE else ''}"
        else:
            days_left = todo.days_until_due()
            if days_left is not None:
                if days_left == 0:
                    due_str = f"{Fore.YELLOW if COLORS_AVAILABLE else ''}[DUE TODAY]{Style.RESET_ALL if COLORS_AVAILABLE else ''}"
                elif days_left == 1:
                    due_str = f"{Fore.YELLOW if COLORS_AVAILABLE else ''}[DUE TOMORROW]{Style.RESET_ALL if COLORS_AVAILABLE else ''}"
                else:
                    due_str = f"[{todo.due_date.strftime('%Y-%m-%d')} ({days_left}d)]"
    
    # Tags
    tags_str = ""
    if todo.tags:
        tags_str = " " + " ".join([f"#{tag}" for tag in todo.tags])
    
    # ID prefix
    id_prefix = f"[{todo.id:3d}] " if show_id else ""
    
    # Title with strikethrough if completed
    title = todo.title
    if todo.completed and COLORS_AVAILABLE:
        title = f"{Fore.BLACK}{Style.DIM}{title}{Style.RESET_ALL}"
    
    return f"{id_prefix}{status} {priority_str} {title}{tags_str} {due_str}".strip()

def print_colored(text: str, color: str = Fore.WHITE):
    if COLORS_AVAILABLE:
        print(f"{color}{text}{Style.RESET_ALL}")
    else:
        print(text)

def print_header(title: str):
    print_colored("=" * 50, Fore.BLUE)
    print_colored(title.center(50), Fore.BLUE + Style.BRIGHT)
    print_colored("=" * 50, Fore.BLUE)

def main():
    parser = argparse.ArgumentParser(description="Awesome Todo CLI - A beautiful command-line todo list")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Init command
    init_parser = subparsers.add_parser('init', help='Initialize a new todo list')
    
    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new todo')
    add_parser.add_argument('title', help='Todo title')
    add_parser.add_argument('-d', '--description', default='', help='Todo description')
    add_parser.add_argument('-p', '--priority', choices=['low', 'medium', 'high'], 
                           default='medium', help='Todo priority')
    add_parser.add_argument('-t', '--tags', nargs='*', default=[], help='Todo tags')
    add_parser.add_argument('--due', help='Due date (YYYY-MM-DD)')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List todos')
    list_parser.add_argument('-a', '--all', action='store_true', help='Show completed todos')
    list_parser.add_argument('-p', '--priority', choices=['low', 'medium', 'high'], 
                            help='Filter by priority')
    list_parser.add_argument('-t', '--tag', help='Filter by tag')
    list_parser.add_argument('-s', '--search', help='Search in title/description')
    
    # Complete command
    complete_parser = subparsers.add_parser('complete', help='Mark todo as complete')
    complete_parser.add_argument('id', type=int, help='Todo ID')
    
    # Remove command
    remove_parser = subparsers.add_parser('remove', help='Remove a todo')
    remove_parser.add_argument('id', type=int, help='Todo ID')
    
    # Search command
    search_parser = subparsers.add_parser('search', help='Search todos')
    search_parser.add_argument('term', help='Search term')
    
    # Stats command
    stats_parser = subparsers.add_parser('stats', help='Show statistics')
    
    # Config command
    config_parser = subparsers.add_parser('config', help='Configure settings')
    config_parser.add_argument('--theme', choices=['light', 'dark'], help='Set theme')
    config_parser.add_argument('--default-priority', choices=['low', 'medium', 'high'], 
                              help='Set default priority')
    
    # Backup command
    backup_parser = subparsers.add_parser('backup', help='Backup todo data')
    backup_parser.add_argument('file', nargs='?', help='Backup file path')
    
    # Restore command
    restore_parser = subparsers.add_parser('restore', help='Restore from backup')
    restore_parser.add_argument('file', help='Backup file path')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    manager = TodoManager()
    
    if args.command == 'init':
        print_colored("Todo list initialized!", Fore.GREEN)
        print_colored(f"Data stored at: {manager.data_file}", Fore.BLUE)
    
    elif args.command == 'add':
        due_date = None
        if args.due:
            try:
                due_date = datetime.strptime(args.due, '%Y-%m-%d')
            except ValueError:
                print_colored("Invalid date format. Use YYYY-MM-DD", Fore.RED)
                return
        
        todo = manager.add_todo(
            title=args.title,
            description=args.description,
            priority=Priority.from_string(args.priority),
            tags=args.tags,
            due_date=due_date
        )
        print_colored(f"Added todo #{todo.id}: {todo.title}", Fore.GREEN)
    
    elif args.command == 'list':
        priority_filter = Priority.from_string(args.priority) if args.priority else None
        todos = manager.list_todos(
            show_completed=args.all,
            priority_filter=priority_filter,
            tag_filter=args.tag,
            search_term=args.search
        )
        
        if not todos:
            print_colored("No todos found.", Fore.YELLOW)
            return
        
        print_header("YOUR TODO LIST")
        for todo in todos:
            print(format_todo(todo))
        print_colored(f"\nTotal: {len(todos)} todo(s)", Fore.BLUE)
    
    elif args.command == 'complete':
        if manager.complete_todo(args.id):
            print_colored(f"Completed todo #{args.id}", Fore.GREEN)
        else:
            print_colored(f"Todo #{args.id} not found", Fore.RED)
    
    elif args.command == 'remove':
        if manager.remove_todo(args.id):
            print_colored(f"Removed todo #{args.id}", Fore.GREEN)
        else:
            print_colored(f"Todo #{args.id} not found", Fore.RED)
    
    elif args.command == 'search':
        todos = manager.list_todos(search_term=args.term)
        if not todos:
            print_colored(f"No todos found matching '{args.term}'", Fore.YELLOW)
            return
        
        print_header(f"SEARCH RESULTS FOR: '{args.term}'")
        for todo in todos:
            print(format_todo(todo))
        print_colored(f"\nFound: {len(todos)} todo(s)", Fore.BLUE)
    
    elif args.command == 'stats':
        stats = manager.get_stats()
        print_header("TODO STATISTICS")
        print_colored(f"Total todos: {stats['total']}", Fore.WHITE)
        print_colored(f"Completed: {stats['completed']}", Fore.GREEN)
        print_colored(f"Pending: {stats['pending']}", Fore.YELLOW)
        print_colored(f"Overdue: {stats['overdue']}", Fore.RED if stats['overdue'] > 0 else Fore.GREEN)
        print_colored("\nBy Priority:", Fore.BLUE + Style.BRIGHT)
        for priority, count in stats['priority_counts'].items():
            color = {'low': Fore.GREEN, 'medium': Fore.YELLOW, 'high': Fore.RED}.get(priority, Fore.WHITE)
            print_colored(f"  {priority.upper()}: {count}", color)
    
    elif args.command == 'config':
        print_colored("Configuration options:", Fore.BLUE)
        print_colored("  --theme [light/dark] - Set color theme", Fore.WHITE)
        print_colored("  --default-priority [low/medium/high] - Set default priority", Fore.WHITE)
        print_colored("\nNote: Full configuration system coming soon!", Fore.YELLOW)
    
    elif args.command == 'backup':
        backup_path = args.file or f"todo_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        try:
            import shutil
            shutil.copy2(manager.data_file, backup_path)
            print_colored(f"Backup saved to: {backup_path}", Fore.GREEN)
        except Exception as e:
            print_colored(f"Backup failed: {e}", Fore.RED)
    
    elif args.command == 'restore':
        if not os.path.exists(args.file):
            print_colored(f"Backup file not found: {args.file}", Fore.RED)
            return
        try:
            import shutil
            shutil.copy2(args.file, manager.data_file)
            manager.load_todos()  # Reload from restored file
            print_colored(f"Restored from: {args.file}", Fore.GREEN)
        except Exception as e:
            print_colored(f"Restore failed: {e}", Fore.RED)

if __name__ == "__main__":
    main()