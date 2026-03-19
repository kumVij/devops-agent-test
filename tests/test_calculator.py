"""
tests/test_calculator.py — Tests for calculator utilities
These tests will FAIL because of the bugs in calculator.py and payment.py
"""

import pytest
from utils.calculator import calculate_total, apply_discount, calculate_tax
from utils.validator import validate_order


class TestCalculateTotal:
    def test_single_item(self):
        items = [{"product_id": 1, "price": 50.0, "quantity": 2}]
        assert calculate_total(items) == 100.0

    def test_multiple_items(self):
        items = [
            {"product_id": 1, "price": 30.0, "quantity": 1},
            {"product_id": 2, "price": 20.0, "quantity": 3},
        ]
        assert calculate_total(items) == 90.0

    def test_empty_items(self):
        assert calculate_total([]) == 0.0


class TestApplyDiscount:
    def test_ten_percent_discount(self):
        # apply_discount(100, 0.10) should return 90.0
        # BUG: returns 1000.0 because it divides instead of subtracts
        result = apply_discount(100.0, 0.10)
        assert result == 90.0, f"Expected 90.0 but got {result}"

    def test_twenty_percent_discount(self):
        result = apply_discount(200.0, 0.20)
        assert result == 160.0, f"Expected 160.0 but got {result}"

    def test_zero_discount(self):
        result = apply_discount(100.0, 0.0)
        assert result == 100.0


class TestCalculateTax:
    def test_default_tax_rate(self):
        assert calculate_tax(100.0) == 18.0

    def test_custom_tax_rate(self):
        assert calculate_tax(200.0, 0.10) == 20.0


class TestValidateOrder:
    def test_valid_order(self):
        items = [{"product_id": 1, "quantity": 2}]
        assert validate_order(items) is True

    def test_empty_order(self):
        assert validate_order([]) is False

    def test_missing_product_id(self):
        assert validate_order([{"quantity": 1}]) is False

    def test_zero_quantity(self):
        assert validate_order([{"product_id": 1, "quantity": 0}]) is False