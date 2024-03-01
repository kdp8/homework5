"""
Testing the app functions
"""
from app import App

def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    app_instance = App()  # Instantiate the App class
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app_instance.start()  # Call the start method on the instance
    out, err = capfd.readouterr()  # pylint: disable=unused-variable

    # Check that the initial greeting is printed and the REPL exits gracefully
    assert "Type 'exit' to exit." in out
    assert "Exiting..." in out

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    app_instance = App()  # Instantiate the App class
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app_instance.start()  # Call the start method on the instance
    out, err = capfd.readouterr()  # pylint: disable=unused-variable

    # Check that the REPL responds to an unknown command and then exits after 'exit' command
    assert "Type 'exit' to exit." in out
    assert "No such command:" in out
    assert "Exiting..." in out
