import pytest
from synthdata import Faker, generate


def test_faker_name():
    fake = Faker()
    name = fake.name()
    assert isinstance(name, str)
    assert len(name) > 0


def test_faker_email():
    fake = Faker()
    email = fake.email()
    assert isinstance(email, str)
    assert "@" in email


def test_faker_phone_number():
    fake = Faker()
    phone = fake.phone_number()
    assert isinstance(phone, str)
    # Check format: XXX-XXX-XXXX
    parts = phone.split("-")
    assert len(parts) == 3
    assert len(parts[0]) == 3
    assert len(parts[1]) == 3
    assert len(parts[2]) == 4


def test_faker_address():
    fake = Faker()
    address = fake.address()
    assert isinstance(address, str)
    assert len(address) > 0


def test_faker_date():
    fake = Faker()
    date = fake.date()
    assert isinstance(date, str)
    # Check format: YYYY-MM-DD
    parts = date.split("-")
    assert len(parts) == 3
    assert len(parts[0]) == 4
    assert len(parts[1]) == 2
    assert len(parts[2]) == 2


def test_faker_boolean():
    fake = Faker()
    boolean = fake.boolean()
    assert isinstance(boolean, bool)


def test_faker_random_int():
    fake = Faker()
    integer = fake.random_int(min=10, max=20)
    assert isinstance(integer, int)
    assert 10 <= integer <= 20


def test_faker_random_float():
    fake = Faker()
    flt = fake.random_float(min=0.5, max=1.5)
    assert isinstance(flt, float)
    assert 0.5 <= flt <= 1.5


def test_faker_uuid4():
    fake = Faker()
    uuid = fake.uuid4()
    assert isinstance(uuid, str)
    # Check format: 8-4-4-4-12 (with version 4)
    parts = uuid.split("-")
    assert len(parts) == 5
    assert len(parts[0]) == 8
    assert len(parts[1]) == 4
    assert len(parts[2]) == 4
    assert len(parts[3]) == 4
    assert len(parts[4]) == 12
    # Version 4: the 13th character (index 12) should be '4'
    assert uuid[14] == '4'  # Because the third group is at index 2*5=10? Let's do: 8+1+4+1+4 = 18? Actually, let's just check the version in the third group.
    # The version is the most significant nibble of the third group (index 0 of the third group).
    # We'll check that the third group starts with '4'
    assert parts[2][0] == '4'


def test_faker_batch():
    fake = Faker()
    names = fake.name(batch_size=5)
    assert isinstance(names, list)
    assert len(names) == 5
    assert all(isinstance(name, str) for name in names)


def test_generate():
    schema = {
        "id": lambda: "id",
        "name": Faker().name,
        "value": Faker().random_int,
    }
    data = generate(schema, batch_size=3)
    assert isinstance(data, list)
    assert len(data) == 3
    for record in data:
        assert isinstance(record, dict)
        assert set(record.keys()) == {"id", "name", "value"}
        assert isinstance(record["id"], str)
        assert isinstance(record["name"], str)
        assert isinstance(record["value"], int)