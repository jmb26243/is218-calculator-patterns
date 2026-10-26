
class CalculateCommand:
    def __init__(self, calculation, history):
        # Store the calculation and shared history list.
        self.calculation = calculation
        self.history = history

    def execute(self) -> float:
        # Run the calculation first. If it fails, nothing is saved.
        result = self.calculation.execute()

        # Save only successful calculations.
        self.history.append(
            f"{self.calculation.a} {self.calculation.operation.__name__} "
            f"{self.calculation.b} = {result}"
        )

        return result


class HistoryCommand:
    def __init__(self, history):
        self.history = history

    def execute(self) -> list[str]:
        # Return a copy so callers cannot modify the stored history.
        return self.history.copy()

