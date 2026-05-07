import pytest
from src.tempconv.converter import celsius_to_fahrenheit, fahrenheit_to_celsius, convert

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-40) == -40

def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    assert fahrenheit_to_celsius(-40) == -40

def test_convert_same_unit():
    assert convert(25, 'C', 'C') == 25
    assert convert(77, 'F', 'F') == 77

def test_convert_c_to_f():
    assert convert(0, 'C', 'F') == 32
    assert convert(100, 'C', 'F') == 212

def test_convert_f_to_c():
    assert convert(32, 'F', 'C') == 0
    assert convert(212, 'F', 'C') == 100

def test_invalid_unit():
    with pytest.raises(ValueError):
        convert(10, 'X', 'C')
    with pytest.raises(ValueError):
        convert(10, 'C', 'X')