# CLI Calculator — Student Submission

## Setup, run, and test

This project is a command-line calculator built with Python 3.12. It supports addition, subtraction, multiplication, and division. It also records successful calculations in history.

Clone the repository and enter the project directory:

```bash
git clone https://github.com/jmb26243/is218-calculator-patterns.git
cd is218-calculator-patterns
```

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Run the calculator:

```bash
python -m calculator
```

Run the tests and require 100% line coverage:

```bash
python -m pytest --cov=calculator --cov-report=term-missing --cov-fail-under=100
```

## Example conversation

```text
calculator> add 5 3
8.0
calculator> multiply -2 4
-8.0
calculator> history
5.0 add 3.0 = 8.0
-2.0 multiply 4.0 = -8.0
calculator> divide 5 0
Cannot divide by zero
calculator> exit
```

The calculator continues running after an error. Only successful calculations are saved in history.

## Static, class, and instance methods

- **Static method:** The methods in `Operations`, such as `add(a, b)`, perform arithmetic using the supplied arguments. They do not need an instance or class state, so they use `@staticmethod`.
- **Class method:** `Calculation.create(cls, a, b, operation)` is a factory method. It uses `cls` to create an instance of the class that calls it, such as `ArithmeticCalculation`.
- **Instance method:** `ArithmeticCalculation.execute(self)` uses the current calculation object's stored values and operation to return the result.

## Factory, Command, and Strategy

The Factory Method is `Calculation.create()`, which constructs a calculation object from two values and an operation.

The Command pattern is represented by `CalculateCommand` and `HistoryCommand`. Each command represents an action and provides an `execute()` method. `CalculateCommand` runs a calculation, records its successful result, and returns the answer.

The Strategy pattern is represented by the operation functions in `Operations`. In `cli.py`, the `OPERATIONS` dictionary maps command names to functions. For example, `add 5 3` selects `Operations.add`, creates an `ArithmeticCalculation`, executes it through `CalculateCommand`, and prints the result.

Adding subtraction, multiplication, or division does not require changing `ArithmeticCalculation.execute()`. The calculation calls whichever operation function it receives.

## OOP concepts

- **Encapsulation:** `ArithmeticCalculation` stores its two operands and selected operation together. `HistoryCommand.execute()` returns a copy of the history list so that a caller cannot modify the original list through the returned value.
- **Abstraction:** `Calculation` is an abstract base class that requires concrete subclasses to implement `execute()`.
- **Inheritance:** `ArithmeticCalculation` inherits from `Calculation`, including its initializer and class method `create()`.
- **Polymorphism:** Different operation functions can be passed into the same calculation structure. The calculation calls the selected function through the same `execute()` method.
- **Composition:** `CalculateCommand` holds a calculation object and a history list. The calculation itself holds an operation function.

## SOLID principles

- **Single responsibility:** `Operations` performs arithmetic, calculation objects execute operations, command objects coordinate actions and history, and `cli.py` handles user input and output.
- **Open/closed:** A new operation can be implemented as a method in `Operations` and registered in the `OPERATIONS` dictionary. The calculation execution logic does not need to change.
- **Liskov substitution:** A concrete calculation should fulfill the `Calculation.execute()` contract by returning a numeric result or raising an appropriate error.
- **Interface segregation:** The calculation abstraction requires only `execute()`, keeping its required interface small.
- **Dependency inversion:** `CalculateCommand` receives a calculation object instead of implementing arithmetic itself. The calculation receives an operation function instead of hard-coding a particular arithmetic operation.

## Tests and GitHub Actions

The test suite checks arithmetic results, decimals, negative numbers, division by zero, factory construction, abstract-class behavior, command results, history protection, and CLI input and error handling.

The local test command passed **39 tests with 100% line coverage**: 85 statements measured and zero missed.

GitHub Actions runs the same coverage-enforcing test command on pushes and pull requests.

**Successful GitHub Actions run:** Replace this line with the URL of the successful run after pushing the completed project.

## Coverage exclusions

The abstract `Calculation.execute()` placeholder uses `# pragma: no cover`. It defines the contract that concrete calculation classes must implement but does not provide executable behavior of its own. The concrete `ArithmeticCalculation.execute()` implementation is tested.

No other coverage exclusions were needed to reach 100% line coverage.

