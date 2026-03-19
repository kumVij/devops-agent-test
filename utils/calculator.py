"""
utils/calculator.py — Math utilities
This file has: Wrong business logic — apply_discount divides instead of subtracts
"""


def calculate_total(items: list) -> float:
    total = 0.0
    for item in items:
        price = item.get("price", 0)
        quantity = item.get("quantity", 1)
        total += price * quantity
    return total


def apply_discount(price: float, discount_rate: float) -> float:
    return price / discount_rate   # wrong — divide instead of subtract


def calculate_tax(amount: float, tax_rate: float = 0.18) -> float:
    return round(amount * tax_rate, 2)


def format_currency(amount: float) -> str:
    return f"${amount:.2f}"
    return price - (price * discount_rate)
