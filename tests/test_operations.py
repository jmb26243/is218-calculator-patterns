import pytest

from calculator.operations import Operations


def test_add():
    assert Operations.add(5,3) == 8


def test_subtract():
    assert Operations.subtract(5,3) == 2


def test_multiply():
    assert Operations.multiply(5,3) == 15


def test_divide():
    assert Operations.divide(6,3) == 2


def test_operations_support_decimals_and_negative_numbers():
    assert Operations.add(-2.5, 1.5) == -1.0
    assert Operations.subtract(-2, 3) == -5
    assert Operations.multiply(-2, 3) == -6
    assert Operations.divide(-6, 2) == -3


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Operations.divide(6, 0)
