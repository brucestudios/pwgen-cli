import unittest
from fp_utils.curry import curry

class TestCurry(unittest.TestCase):
    def test_curry_two_args(self):
        @curry
        def add(x, y):
            return x + y
        
        add_five = add(5)
        self.assertEqual(add_five(3), 8)
        self.assertEqual(add(5, 3), 8)

    def test_curry_three_args(self):
        @curry
        def multiply(x, y, z):
            return x * y * z
        
        double = multiply(2)
        double_six = double(3)
        self.assertEqual(double_six(4), 24)
        self.assertEqual(multiply(2, 3, 4), 24)

    def test_curry_with_keywords(self):
        @curry
        def greet(greeting, name, punctuation="!"):
            return f"{greeting} {name}{punctuation}"
        
        hello = greet("Hello")
        hello_world = hello("World")
        self.assertEqual(hello_world(), "Hello World!")
        self.assertEqual(hello("World", punctuation="..."), "Hello World...")

if __name__ == '__main__':
    unittest.main()