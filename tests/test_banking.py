"""
tests/test_banking.py — Tests for banking system
These tests will FAIL because of the 3 bugs in banking.py

Expected failures:
  1. test_get_balance_returns_float     → BUG: returns str not float
  2. test_calculate_interest_correct    → BUG: divides instead of multiplies
  3. test_transfer_rejects_negative     → BUG: missing negative check
"""

import pytest
from banking import BankAccount


class TestDeposit:
    """These tests should PASS — deposit logic is correct."""

    def test_deposit_increases_balance(self):
        account = BankAccount("ACC001", "Alice", 100.0)
        account.deposit(50.0)
        assert account.balance == 150.0

    def test_deposit_returns_new_balance(self):
        account = BankAccount("ACC001", "Alice", 0.0)
        result = account.deposit(200.0)
        assert result == 200.0

    def test_deposit_negative_raises(self):
        account = BankAccount("ACC001", "Alice", 100.0)
        with pytest.raises(ValueError, match="positive"):
            account.deposit(-10.0)


class TestWithdraw:
    """These tests should PASS — withdraw logic is correct."""

    def test_withdraw_decreases_balance(self):
        account = BankAccount("ACC001", "Alice", 200.0)
        account.withdraw(50.0)
        assert account.balance == 150.0

    def test_withdraw_insufficient_funds_raises(self):
        account = BankAccount("ACC001", "Alice", 50.0)
        with pytest.raises(ValueError, match="Insufficient"):
            account.withdraw(100.0)


class TestGetBalance:
    """FAILS — get_balance returns str instead of float."""

    def test_get_balance_returns_float(self):
        account = BankAccount("ACC001", "Alice", 500.0)
        balance = account.get_balance()
        # BUG: returns "500.0" (str) not 500.0 (float)
        assert isinstance(balance, float), \
            f"Expected float but got {type(balance).__name__}: {balance!r}"

    def test_get_balance_correct_value(self):
        account = BankAccount("ACC002", "Bob", 1000.0)
        assert account.get_balance() == 1000.0


class TestCalculateInterest:
    """FAILS — calculate_interest divides instead of multiplying."""

    def test_calculate_interest_correct(self):
        account = BankAccount("ACC001", "Alice", 1000.0)
        # 1000 * 0.05 * 2 = 100.0
        interest = account.calculate_interest(rate=0.05, years=2)
        assert interest == 100.0, \
            f"Expected 100.0 but got {interest}"

    def test_calculate_interest_zero_years(self):
        account = BankAccount("ACC001", "Alice", 1000.0)
        interest = account.calculate_interest(rate=0.05, years=1)
        assert interest == 50.0, \
            f"Expected 50.0 but got {interest}"


class TestTransferFunds:
    """FAILS — transfer_funds missing negative amount check."""

    def test_transfer_moves_funds(self):
        alice = BankAccount("ACC001", "Alice", 500.0)
        bob = BankAccount("ACC002", "Bob", 100.0)
        alice.transfer_funds(bob, 200.0)
        assert alice.balance == 300.0
        assert bob.balance == 300.0

    def test_transfer_rejects_negative(self):
        alice = BankAccount("ACC001", "Alice", 500.0)
        bob = BankAccount("ACC002", "Bob", 100.0)
        # BUG: should raise ValueError for negative amount
        with pytest.raises(ValueError, match="positive"):
            alice.transfer_funds(bob, -100.0)

    def test_transfer_rejects_zero(self):
        alice = BankAccount("ACC001", "Alice", 500.0)
        bob = BankAccount("ACC002", "Bob", 100.0)
        with pytest.raises(ValueError):
            alice.transfer_funds(bob, 0.0)

    def test_transfer_insufficient_funds(self):
        alice = BankAccount("ACC001", "Alice", 100.0)
        bob = BankAccount("ACC002", "Bob", 0.0)
        with pytest.raises(ValueError, match="Insufficient"):
            alice.transfer_funds(bob, 500.0)
            