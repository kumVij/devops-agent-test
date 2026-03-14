import pytest
import requests  # this package is NOT in requirements.txt — will cause ImportError

from utils.calculator import add, subtract, multiply, divide


class TestAdd:
    def test_add_positive_numbers(self):
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        assert add(-1, -2) == -3
