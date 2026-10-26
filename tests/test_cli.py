from calculator.cli import main


def run_cli(monkeypatch,capsys,inputs):
    """Run the CLI with supplied input lines and return its output."""
    input_lines = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda prompt="": next(input_lines))
    main()
    return capsys.readouterr().out



def test_cli_calculates_and_exits(monkeypatch, capsys):
    output = run_cli(monkeypatch, capsys, ["add 5 3", "exit"])
    assert "8.0" in output


def test_cli_supports_all_operations(monkeypatch, capsys):
    output = run_cli(
        monkeypatch,
        capsys,
        [
            "add 5 3",
            "subtract 5 3",
            "multiply 5 3",
            "divide 6 3",
            "exit",
        ],
)
    assert "8.0" in output
    assert "2.0" in output
    assert "15.0" in output


def test_cli_shows_history(monkeypatch, capsys):
    output = run_cli(
        monkeypatch,
        capsys,
        ["add 5 3", "history", "exit"],
    )
    assert "5.0 add 3.0 = 8.0" in output


def test_cli_reports_empty_history(monkeypatch, capsys):
    output = run_cli(monkeypatch, capsys, ["history", "exit"])
    assert "History is empty." in output


def test_cli_reports_unknown_command(monkeypatch, capsys):
    output = run_cli(monkeypatch, capsys, ["unknown 1 2", "exit"])
    assert "Unknown command: unknown" in output


def test_cli_reports_wrong_operand_count(monkeypatch, capsys):
    output = run_cli(monkeypatch, capsys, ["add 5", "exit"])
    assert "Usage: add NUMBER NUMBER" in output


def test_cli_reports_invalid_number(monkeypatch, capsys):
    output = run_cli(monkeypatch, capsys, ["add abc 3", "exit"])
    assert "could not convert string to float" in output

def test_cli_reports_division_by_zero(monkeypatch, capsys):
    output = run_cli(monkeypatch, capsys, ["divide 5 0", "exit"])
    assert "Cannot divide by zero" in output

def test_cli_continues_after_error(monkeypatch, capsys):
    output = run_cli(
        monkeypatch,
        capsys,
        ["divide 5 0", "add 2 3", "exit"],
    )
    assert "Cannot divide by zero" in output
    assert "5.0" in output


def test_cli_does_not_save_failed_calculation(monkeypatch, capsys):
    output = run_cli(
        monkeypatch,
        capsys,
        ["divide 5 0", "history", "exit"],
    )
    assert "Cannot divide by zero" in output
    assert "History is empty." in output



def test_cli_ignore_blank_input(monkeypatch, capsys):
    output = run_cli(monkeypatch, capsys, ["", "add 1 2", "exit"])
    assert "3.0" in output


def test_cli_handles_extra_operands(monkeypatch, capsys):
    output = run_cli(monkeypatch, capsys, ["add 1 2 3", "exit"])
    assert "Usage: add NUMBER NUMBER" in output


def test_cli_handles_eof(monkeypatch, capsys):
    def raise_eof(prompt=""):
        raise EOFError

    monkeypatch.setattr("builtins.input", raise_eof)
    main()
    assert capsys.readouterr().out == "\n"
