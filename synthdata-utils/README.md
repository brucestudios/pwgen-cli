# synthdata-utils

A Python utility library for generating synthetic data for testing, development, and data anonymization.

## Features

- Generate realistic fake data for various data types (names, addresses, emails, etc.)
- Support for generating data in bulk (lists, DataFrames)
- Easy to extend with custom providers
- Well-typed with Python type hints
- Comprehensive test suite

## Installation

```bash
pip install synthdata-utils
```

## Usage

```python
from synthdata import Faker, generate

# Create a faker instance
fake = Faker()

# Generate a single fake name
name = fake.name()
print(name)  # e.g., "Bruce Fang"

# Generate a list of fake emails
emails = fake.email(batch_size=10)
print(emails)

# Generate a dataset as a list of dictionaries
data = generate(
    {
        "id": lambda: fake.uuid4(),
        "name": fake.name,
        "email": fake.email,
        "age": lambda: fake.random_int(min=18, max=80),
        "is_active": fake.boolean,
    },
    batch_size=5,
)
print(data)
```

## Running Tests

```bash
pytest
```

## License

MIT