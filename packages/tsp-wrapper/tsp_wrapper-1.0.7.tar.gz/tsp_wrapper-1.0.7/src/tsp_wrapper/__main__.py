"""
Invokes typer application when the tsp_wrapper module is run as a script.

Example: python -m tsp_wrapper shell
"""
from tsp_wrapper.core import management
from tsp_wrapper import setup

if __name__ == "__main__":
    setup()
    management.execute_from_command_line()
