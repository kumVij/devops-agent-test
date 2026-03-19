"""
utils/validator.py — Input validation utilities
This file is correct — no bugs here
"""


def validate_order(items: list) -> bool:
    if not items:
        return False
    for item in items:
        if "product_id" not in item:
            return False
        if item.get("quantity", 0) <= 0:
            return False
    return True


def validate_email(email: str) -> bool:
    return "@" in email and "." in email


def validate_amount(amount: float) -> bool:
    return isinstance(amount, (int, float)) and amount > 0