def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Делить на ноль нельзя")
    return a / b

def subtract(a, b):
    return a - b

def test_subtract():
    assert subtract(5, 3) == 2