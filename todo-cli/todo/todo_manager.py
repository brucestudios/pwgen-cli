import json
import os

class TodoManager:
    def __init__(self, storage_file='todos.json'):
        self.storage_file = storage_file
        self.todos = self.load_todos()

    def load_todos(self):
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as f:
                return json.load(f)
        return []

    def save_todos(self):
        with open(self.storage_file, 'w') as f:
            json.dump(self.todos, f, indent=2)

    def add_task(self, description):
        todo = {
            'description': description,
            'completed': False
        }
        self.todos.append(todo)
        self.save_todos()

    def list_tasks(self):
        return self.todos

    def complete_task(self, index):
        if 0 <= index < len(self.todos):
            self.todos[index]['completed'] = True
            self.save_todos()
        else:
            raise IndexError("Task index out of range")

    def delete_task(self, index):
        if 0 <= index < len(self.todos):
            return self.todos.pop(index)
        else:
            raise IndexError("Task index out of range")