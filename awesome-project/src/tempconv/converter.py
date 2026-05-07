"""Temperature conversion utilities."""

def celsius_to_fahrenheit(c: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5/9

def convert(value: float, from_unit: str, to_unit: str) -> float:
    """Convert temperature between units.
    
    Args:
        value: The temperature value.
        from_unit: Either 'C' or 'F'.
        to_unit: Either 'C' or 'F'.
        
    Returns:
        Converted temperature.
        
    Raises:
        ValueError: If units are not 'C' or 'F'.
    """
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()
    
    if from_unit == to_unit:
        return value
        
    if from_unit == 'C' and to_unit == 'F':
        return celsius_to_fahrenheit(value)
    elif from_unit == 'F' and to_unit == 'C':
        return fahrenheit_to_celsius(value)
    else:
        raise ValueError("Units must be 'C' or 'F'")
