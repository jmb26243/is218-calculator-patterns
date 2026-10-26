import runpy




def test_main_module_starts_cli(monkeypatch, capsys):
    # Simulate the user typing exit immdediately.
    monkeypatch.setattr("builtins.input", lambda prompt="": "exit")


    runpy.run_module("calculator.__main__", run_name="__main__")

    # The CLI exits without displaying a calculation result.
    assert capsys.readouterr().out == ""
