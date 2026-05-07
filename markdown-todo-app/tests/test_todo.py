import os
import tempfile
from markdown_todo_app.todo import TodoManager


def test_todo_manager():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.md') as f:
        temp_file = f.name

    try:
        manager = TodoManager(temp_file)

        # Initialize the file
        manager.init()
        assert os.path.exists(temp_file)
        with open(temp_file, 'r') as f:
            lines = f.readlines()
            assert lines[0].strip() == "# TODO List"

        # Add a task
        manager.add("Test task")
        with open(temp_file, 'r') as f:
            lines = f.readlines()
            # Check that the task is added (look for the checkbox line)
            assert any(line.strip() == "- [ ] Test task" for line in lines)

        # List tasks
        items = manager.list()
        assert len(items) == 1
        assert items[0] == (False, "Test task")

        # Complete the task
        assert manager.complete(1) == True
        with open(temp_file, 'r') as f:
            lines = f.readlines()
            assert any(line.strip() == "- [x] Test task" for line in lines)

        # List again to confirm completion
        items = manager.list()
        assert len(items) == 1
        assert items[0] == (True, "Test task")

        # Remove the task
        assert manager.remove(1) == True
        with open(temp_file, 'r') as f:
            lines = f.readlines()
            assert not any(line.strip() == "- [x] Test task" for line in lines)

        # List after removal
        items = manager.list()
        assert len(items) == 0

    finally:
        # Clean up the temporary file
        if os.path.exists(temp_file):
            os.unlink(temp_file)


if __name__ == "__main__":
    test_todo_manager()
    print("All tests passed!")