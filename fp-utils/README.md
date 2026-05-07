# fp-utils

Functional programming utilities for Python.

## Installation

```bash
pip install fp-utils
```

## Usage

### Compose

Compose functions from right to left.

```python
from fp_utils import compose

def add_one(x):
    return x + 1

def multiply_by_two(x):
    return x * 2

# Create a new function: multiply_by_two(add_one(x))
operation = compose(multiply_by_two, add_one)
result = operation(3)  # (3 + 1) * 2 = 8
```

### Curry

Curry a function to allow partial application.

```python
from fp_utils import curry

@curry
def add(x, y):
    return x + y

add_five = add(5)
result = add_five(3)  # 8
```

### Pipe

Pipe functions from left to right.

```python
from fp_utils import pipe

def add_one(x):
    return x + 1

def multiply_by_two(x):
    return x * 2

# Create a new function: add_one(x) then multiply_by_two
operation = pipe(add_one, multiply_by_two)
result = operation(3)  # (3 + 1) * 2 = 8
```

## Development

To install in development mode:

```bash
pip install -e .
```

## Running Tests

```bash
pytest
```

## License

MIT