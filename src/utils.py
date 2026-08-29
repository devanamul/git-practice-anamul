def _check_numbers(a, b):
    for value in (a, b):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError(f"Expected a number, got {type(value).__name__}: {value!r}")


def add(a, b):
    _check_numbers(a, b)
    return a + b


def subtract(a, b):
    _check_numbers(a, b)
    return a - b


def multiply(a, b):
    _check_numbers(a, b)
    return a * b
