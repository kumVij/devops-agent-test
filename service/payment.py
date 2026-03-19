"""
services/payment.py — Payment processing service
This file has: TypeError — adding int and str (tax_rate stored as string)
"""

from utils.calculator import calculate_total


class PaymentService:
    def __init__(self, config):
        self.config = config
        self.tax_rate = "0.18"   # BUG: should be float 0.18, stored as string

    def charge(self, order: dict) -> dict:
        base_amount = order.get("total", 0)

        # TypeError: unsupported operand type(s) for *: 'int' and 'str'
        tax_amount = base_amount * self.tax_rate

        total_with_tax = base_amount + tax_amount

        return {
            "order_id": order["id"],
            "amount": total_with_tax,
            "status": "charged",
            "currency": "USD",
        }

    def refund(self, order_id: int, amount: float) -> dict:
        return {
            "order_id": order_id,
            "refund_amount": amount,
            "status": "refunded",
        }