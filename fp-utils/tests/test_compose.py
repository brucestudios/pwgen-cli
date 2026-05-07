import unittest
from fp_utils.compose import compose

class TestCompose(unittest.TestCase):
    def test_compose_two_functions(self):
        def add_one(x):
            return x + 1
        
        def multiply_by_two(x):
            return x * 2
        
        operation = compose(multiply_by_two, add_one)
        self.assertEqual(operation(3), 8)  # (3 + 1) * 2 = 8

    def test_compose_single_function(self):
        def add_one(x):
            return x + 1
        
        operation = compose(add_one)
        self.assertEqual(operation(3), 4)

    def test_compose_three_functions(self):
        def add_one(x):
            return x + 1
        
        def multiply_by_two(x):
            return x * 2
        
        def subtract_three(x):
            return x - 3
        
        operation = compose(subtract_three, multiply_by_two, add_one)
        self.assertEqual(operation(3), 3)  # ((3 + 1) * 2) - 3 = 5

if __name__ == '__main__':
    unittest.main()