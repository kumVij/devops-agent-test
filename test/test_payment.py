"""
tests/test_payment.py — Tests for payment service
These tests will FAIL because tax_rate is stored as string in PaymentService
"""

import pytest
from services.payment import PaymentService
from config.settings import AppConfig


class TestPaymentService:
    def setup_method(self):
        # AppConfig will raise KeyError for DATABASE_URL
        # so we mock a minimal config
        class MockConfig:
            STRIPE_KEY = "test_key"
            MAX_RETRIES = 3
            TIMEOUT = 30

        self.payment = PaymentService(MockConfig())

    def test_charge_calculates_tax_correctly(self):
        order = {"id": 1, "total": 100.0}
        # BUG: TypeError because tax_rate = "0.18" (string) not 0.18 (float)
        result = self.payment.charge(order)
        assert result["amount"] == 118.0, f"Expected 118.0 but got {result['amount']}"

    def test_charge_returns_correct_status(self):
        order = {"id": 2, "total": 50.0}
        result = self.payment.charge(order)
        assert result["status"] == "charged"

    def test_refund_returns_correct_amount(self):
        result = self.payment.refund(order_id=1, amount=50.0)
        assert result["refund_amount"] == 50.0
        assert result["status"] == "refunded"


class TestChargeEdgeCases:
    def test_zero_amount_order(self):
        class MockConfig:
            STRIPE_KEY = ""
            MAX_RETRIES = 3
            TIMEOUT = 30

        payment = PaymentService(MockConfig())
        order = {"id": 3, "total": 0}
        result = payment.charge(order)
        assert result["amount"] == 0