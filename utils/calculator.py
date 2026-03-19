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

def apply_discount(price: float, discount_rate: float) -> float:
    if discount_rate == 0:
        return price
    return price * (1 - discount_rate)   # correct formula

def calculate_tax(amount: float, tax_rate: float = 0.28) -> float:
    return round(amount * tax_rate, 2)

def format_currency(amount: float) -> str:
    return f"${amount:.2f}"