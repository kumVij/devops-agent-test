import pytest
from utils.calculator import add, subtract, multiply, divide

class TestAdd:
    def test_add_positive_numbers(self):
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        assert add(-1, -2) == -3

class TestSubtract:
    def test_subtract_positive(self):
        assert subtract(10, 4) == 6

class TestMultiply:
    def test_multiply_positive(self):
        assert multiply(5, 6) == 30

class TestDivide:
    def test_divide_positive(self):
        assert divide(15, 3) == 5.0

    def test_divide_by_zero_raises(self):
        with pytest.raises(ValueError):
            divide(10, 0)