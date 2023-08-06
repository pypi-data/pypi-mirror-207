"""
Invokes skailar-admin when the skailar module is run as a script.

Example: python -m skailar check
"""
from skailar.core import management

if __name__ == "__main__":
    management.execute_from_command_line()
