def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a: float, b: int) -> float:
    result = 1.0
    for _ in range(b):
        result *= a
    return result


def modulo(a: float, b: float) -> float:
    while a >= b:
        a -= b
    return a
