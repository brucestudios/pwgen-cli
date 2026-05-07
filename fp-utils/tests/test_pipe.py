import unittest
from fp_utils.pipe import pipe

class TestPipe(unittest.TestCase):
    def test_pipe_two_functions(self):
        def add_one(x):
            return x + 1
        
        def multiply_by_two(x):
            return x * 2
        
        operation = pipe(add_one, multiply_by_two)
        self.assertEqual(operation(3), 8)  # (3 + 1) * 2 = 8

    def test_pipe_single_function(self):
        def add_one(x):
            return x + 1
        
        operation = pipe(add_one)
        self.assertEqual(operation(3), 4)

    def test_pipe_three_functions(self):
        def add_one(x):
            return x + 1
        
        def multiply_by_two(x):
            return x * 2
        
        def subtract_three(x):
            return x - 3
        
        operation = pipe(add_one, multiply_by_two, subtract_three)
        self.assertEqual(operation(3), 3)  # ((3 + 1) * 2) - 3 = 5

if __name__ == '__main__':
    unittest.main()