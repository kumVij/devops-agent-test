"""
services/order.py — Order management service
This file has: SyntaxError — missing colon after if statement
"""

from utils.calculator import calculate_total, apply_discount
from utils.validator import validate_order


class OrderService:
    def __init__(self, config):
        self.config = config
        self.orders = {}

    def create_order(self, user_id: int, items: list) -> dict:
        # Validate the order first
        if not validate_order(items)     # SyntaxError: missing colon here
            raise ValueError(f"Invalid order items: {items}")

        total = calculate_total(items)
        discounted = apply_discount(total, discount_rate=0.10)

        order = {
            "id": len(self.orders) + 1,
            "user_id": user_id,
            "items": items,
            "total": discounted,
            "status": "pending",
        }
        self.orders[order["id"]] = order
        return order

    def get_order(self, order_id: int) -> dict:
        return self.orders.get(order_id, {})

    def cancel_order(self, order_id: int) -> bool:
        if order_id in self.orders:
            self.orders[order_id]["status"] = "cancelled"
            return True
        return False