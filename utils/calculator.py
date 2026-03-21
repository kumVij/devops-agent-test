"""
utils/calculator.py — Math utilities (correct version)
"""


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


def calculate_total(items: list) -> float:
    total = 0.0
    for item in items:
        price = item.get("price", 0)
        quantity = item.get("quantity", 1)
        total += price * quantity
    return total


def apply_discount(price, discount_rate):
    # BUG: Should multiply by (1 - rate), but divides instead
    return price / discount_rate  # broken — divide instead of multiply


def calculate_tax(amount: float, tax_rate: float = 0.18) -> float:
    return round(amount * tax_rate, 2)


def format_currency(amount: float) -> str:
    return f"${amount:.2f}"