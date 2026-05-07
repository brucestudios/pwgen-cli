import pytest
from openclaw_utils.core import hello_world, add

def test_hello_world():
    assert hello_world() == "Hello, World!"
    assert hello_world("Alice") == "Hello, Alice!"

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0