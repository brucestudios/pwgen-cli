import pytest
from python_utils import strings

def test_capitalize_words():
    assert strings.capitalize_words("hello world") == "Hello World"
    assert strings.capitalize_words("PYTHON") == "Python"
    assert strings.capitalize_words("") == ""
    assert strings.capitalize_words("single") == "Single"

def test_reverse_string():
    assert strings.reverse_string("hello") == "olleh"
    assert strings.reverse_string("") == ""
    assert strings.reverse_string("a") == "a"

def test_is_palindrome():
    assert strings.is_palindrome("racecar") == True
    assert strings.is_palindrome("RaceCar") == True
    assert strings.is_palindrome("A man a plan a canal Panama") == True
    assert strings.is_palindrome("hello") == False

def test_remove_whitespace():
    assert strings.remove_whitespace("hello world") == "helloworld"
    assert strings.remove_whitespace("  hello  ") == "hello"
    assert strings.remove_whitespace("\thello\nworld\r") == "helloworld"
    assert strings.remove_whitespace("") == ""