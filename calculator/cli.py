
from calculator.calculation import ArithmeticCalculation
from calculator.commands import CalculateCommand, HistoryCommand
from calculator.operations import Operations


OPERATIONS = {
    "add": Operations.add,
    "subtract": Operations.subtract,
    "multiply": Operations.multiply,
    "divide": Operations.divide,
}


def main():
    history = []

    while True:
        try:
            user_input = input("calculator> ")
        except EOFError:
            print()
            break

        parts = user_input.strip().split()

        if not parts:
            continue

        command_name = parts[0].lower()

        if command_name == "exit":
            break

        if command_name == "history":
            entries = HistoryCommand(history).execute()
            if entries:
                for entry in entries:
                    print(entry)
            else:
                print("History is empty.")
            continue

        if command_name not in OPERATIONS:
            print(f"Unknown command: {command_name}")
            continue

        if len(parts) != 3:
            print(f"Usage: {command_name} NUMBER NUMBER")
            continue

        try:
            a = float(parts[1])
            b = float(parts[2])

            # Flow: read input -> select strategy -> create calculation
            # -> create and execute command -> print the answer.
            operation = OPERATIONS[command_name]
            calculation = ArithmeticCalculation.create(a, b, operation)
            command = CalculateCommand(calculation, history)
            result = command.execute()

            print(result)

        except ValueError as error:
            print(error)

