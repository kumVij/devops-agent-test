"""
app.py — E-commerce order processing app
This file has: missing import (requests not in requirements)
"""

import os
import requests          # NOT in requirements.txt — will cause ModuleNotFoundError
from services.order import OrderService
from services.payment import PaymentService
from config.settings import AppConfig


def main():
    config = AppConfig()
    order_service = OrderService(config)
    payment_service = PaymentService(config)

    print(f"App started on port {config.PORT}")
    print(f"Database: {config.DATABASE_URL}")

    # Process a sample order
    order = order_service.create_order(
        user_id=1,
        items=[{"product_id": 101, "quantity": 2}],
    )
    result = payment_service.charge(order)
    print(f"Order processed: {result}")


if __name__ == "__main__":
    main()