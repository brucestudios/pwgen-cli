import random
import string
from typing import Any, Callable, Dict, List, Optional, Union


class Faker:
    """A simple synthetic data generator."""

    def __init__(self, seed: Optional[int] = None):
        if seed is not None:
            random.seed(seed)

    # --- Basic data types ---

    def name(self) -> str:
        """Generate a random name."""
        first_names = [
            "Bruce",
            "Peter",
            "James",
            "John",
            "Michael",
            "David",
            "Chris",
            "Steven",
            "Mark",
            "Paul",
        ]
        last_names = [
            "Fang",
            "Smith",
            "Johnson",
            "Williams",
            "Brown",
            "Jones",
            "Garcia",
            "Miller",
            "Davis",
            "Rodriguez",
        ]
        return f"{random.choice(first_names)} {random.choice(last_names)}"

    def email(self) -> str:
        """Generate a random email."""
        name = self.name().lower().replace(" ", ".")
        domains = ["example.com", "test.org", "demo.net"]
        return f"{name}@{random.choice(domains)}"

    def phone_number(self) -> str:
        """Generate a random phone number."""
        return f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"

    def address(self) -> str:
        """Generate a random address."""
        streets = ["Main St", "Oak Ave", "Pine Rd", "Elm St", "Maple Dr"]
        cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
        states = ["NY", "CA", "IL", "TX", "AZ"]
        return f"{random.randint(1, 9999)} {random.choice(streets)}, {random.choice(cities)}, {random.choice(states)} {random.randint(10000, 99999)}"

    def date(self) -> str:
        """Generate a random date in YYYY-MM-DD format."""
        year = random.randint(2000, 2025)
        month = random.randint(1, 12)
        day = random.randint(1, 28)  # Simplified to avoid month/day issues
        return f"{year:04d}-{month:02d}-{day:02d}"

    def boolean(self) -> bool:
        """Generate a random boolean."""
        return random.choice([True, False])

    def random_int(self, min: int = 0, max: int = 100) -> int:
        """Generate a random integer in the range [min, max]."""
        return random.randint(min, max)

    def random_float(self, min: float = 0.0, max: float = 1.0) -> float:
        """Generate a random float in the range [min, max]."""
        return random.uniform(min, max)

    def uuid4(self) -> str:
        """Generate a random UUID4-like string."""
        return "-".join(
            [
                "".join(random.choices(string.hexdigits.lower(), k=8)),
                "".join(random.choices(string.hexdigits.lower(), k=4)),
                "4".join(random.choices(string.hexdigits.lower(), k=3)),
                "".join(random.choices("89ab", k=1))
                + "".join(random.choices(string.hexdigits.lower(), k=3)),
                "".join(random.choices(string.hexdigits.lower(), k=12)),
            ]
        )

    # --- Helper methods ---

    def _batch(self, func: Callable, batch_size: int) -> List[Any]:
        """Helper to generate a batch of items."""
        return [func() for _ in range(batch_size)]

    # --- Public batch methods ---

    def name(self, batch_size: Optional[int] = None) -> Union[str, List[str]]:
        """Generate a random name or a list of names."""
        if batch_size is None:
            return self.name()
        return self._batch(self.name, batch_size)

    def email(self, batch_size: Optional[int] = None) -> Union[str, List[str]]:
        """Generate a random email or a list of emails."""
        if batch_size is None:
            return self.email()
        return self._batch(self.email, batch_size)

    def phone_number(self, batch_size: Optional[int] = None) -> Union[str, List[str]]:
        """Generate a random phone number or a list of phone numbers."""
        if batch_size is None:
            return self.phone_number()
        return self._batch(self.phone_number, batch_size)

    def address(self, batch_size: Optional[int] = None) -> Union[str, List[str]]:
        """Generate a random address or a list of addresses."""
        if batch_size is None:
            return self.address()
        return self._batch(self.address, batch_size)

    def date(self, batch_size: Optional[int] = None) -> Union[str, List[str]]:
        """Generate a random date or a list of dates."""
        if batch_size is None:
            return self.date()
        return self._batch(self.date, batch_size)

    def boolean(self, batch_size: Optional[int] = None) -> Union[bool, List[bool]]:
        """Generate a random boolean or a list of booleans."""
        if batch_size is None:
            return self.bool()
        return self._batch(self.boolean, batch_size)

    def random_int(
        self, min: int = 0, max: int = 100, batch_size: Optional[int] = None
    ) -> Union[int, List[int]]:
        """Generate a random integer or a list of random integers."""
        if batch_size is None:
            return self.random_int(min, max)
        return self._batch(lambda: self.random_int(min, max), batch_size)

    def random_float(
        self, min: float = 0.0, max: float = 1.0, batch_size: Optional[int] = None
    ) -> Union[float, List[float]]:
        """Generate a random float or a list of random floats."""
        if batch_size is None:
            return self.random_float(min, max)
        return self._batch(lambda: self.random_float(min, max), batch_size)

    def uuid4(self, batch_size: Optional[int] = None) -> Union[str, List[str]]:
        """Generate a random UUID4 or a list of UUID4s."""
        if batch_size is None:
            return self.uuid4()
        return self._batch(self.uuid4, batch_size)


def generate(
    schema: Dict[str, Callable], batch_size: int = 1
) -> List[Dict[str, Any]]:
    """
    Generate a list of dictionaries based on a schema.

    Args:
        schema: A dictionary where keys are field names and values are callables
                that generate the field value.
        batch_size: Number of records to generate.

    Returns:
        A list of dictionaries, each representing a record.
    """
    faker = Faker()
    results = []
    for _ in range(batch_size):
        record = {key: func() for key, func in schema.items()}
        results.append(record)
    return results