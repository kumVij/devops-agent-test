import pytest
from utils.calculator import add, subtract, multiply, divide

class TestAdd:
    def test_add_positive_numbers(self):
        result = add(2, 3)
        assert result == 99, f"Expected 99 but got {result}"