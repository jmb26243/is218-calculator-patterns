
import pytest

from calculator.calculation import ArithmeticCalculation
from calculator.commands import CalculateCommand, HistoryCommand
from calculator.operations import Operations


def test_calculate_command_returns_result_and_saves_history():
    history = []
    calculation = ArithmeticCalculation.create(5, 3, Operations.add)
    command = CalculateCommand(calculation, history)

    assert command.execute() == 8
    assert history == ["5 add 3 = 8"]


def test_failed_calculation_is_not_saved():
    history = []
    calculation = ArithmeticCalculation.create(6, 0, Operations.divide)
    command = CalculateCommand(calculation, history)

    with pytest.raises(ValueError, match="Cannot divide by zero"):
        command.execute()

    assert history == []


def test_history_command_returns_saved_entries():
    history = ["5 add 3 = 8", "6 divide 3 = 2"]
    command = HistoryCommand(history)

    assert command.execute() == history


def test_history_command_returns_a_copy():
    history = ["5 add 3 = 8"]
    command = HistoryCommand(history)

    returned_history = command.execute()
    returned_history.append("fake entry")

    assert history == ["5 add 3 = 8"]


def test_history_command_handles_empty_history():
    command = HistoryCommand([])

    assert command.execute() == []

