import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'awesome_utils'))

from awesome_utils import strings

def test_capitalize_words():
    assert strings.capitalize_words("hello world") == "Hello World"
    assert strings.capitalize_words("HELLO WORLD") == "Hello World"
    assert strings.capitalize_words("") == ""
    assert strings.capitalize_words("a") == "A"

def test_snake_to_camel():
    assert strings.snake_to_camel("hello_world") == "helloWorld"
    assert strings.snake_to_camel("hello_world_example") == "helloWorldExample"
    assert strings.snake_to_camel("hello") == "hello"
    assert strings.snake_to_camel("") == ""

def test_camel_to_snake():
    assert strings.camel_to_snake("helloWorld") == "hello_world"
    assert strings.camel_to_snake("helloWorldExample") == "hello_world_example"
    assert strings.camel_to_snake("hello") == "hello"
    assert strings.camel_to_snake("") == ""

def test_truncate():
    assert strings.truncate("Hello World", 8) == "Hel..."
    assert strings.truncate("Hi", 5) == "Hi"
    assert strings.truncate("", 3) == ""
    assert strings.truncate("Hello World", 11) == "Hello World"

def test_slugify():
    assert strings.slugify("Hello World") == "hello-world"
    assert strings.slugify("Hello  World!") == "hello-world"
    assert strings.slugify("---Hello---World---") == "hello-world"
    assert strings.slugify("") == ""