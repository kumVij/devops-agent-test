import pytest
from utils.calculator import add, divide, multiply, subtract


def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(0, 5) == 5

def test_divide_normal():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

def test_multiply():
    assert multiply(3, 4) == 12

def test_subtract():
    assert subtract(10, 3) == 7

def test_divide_float():
    assert divide(7, 2) == 3.5