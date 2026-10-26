
import pytest

from calculator.calculation import Calculation, ArithmeticCalculation
from calculator.operations import Operations


def test_factory_creates_calculation_with_supplied_values():
    calculation = ArithmeticCalculation.create(5, 3, Operations.add)

    assert isinstance(calculation, ArithmeticCalculation)
    assert calculation.a == 5
    assert calculation.b == 3
    assert calculation.operation is Operations.add


def test_execute_addition():
    calculation = ArithmeticCalculation.create(5, 3, Operations.add)

    assert calculation.execute() == 8


def test_execute_subtraction():
    calculation = ArithmeticCalculation.create(5, 3, Operations.subtract)

    assert calculation.execute() == 2


def test_execute_multiplication():
    calculation = ArithmeticCalculation.create(5, 3, Operations.multiply)

    assert calculation.execute() == 15


def test_execute_division():
    calculation = ArithmeticCalculation.create(6, 3, Operations.divide)

    assert calculation.execute() == 2


def test_abstract_calculation_cannot_be_instantiated():
    with pytest.raises(TypeError):
        Calculation(5, 3, Operations.add)


def test_execute_propagates_operation_error():
    calculation = ArithmeticCalculation.create(6, 0, Operations.divide)

    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation.execute()

