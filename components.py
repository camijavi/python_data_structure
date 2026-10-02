import os

# ANSI color codes
RESET = "\033[0m"
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
CYAN = "\033[96m"
BOLD = "\033[1m"


def clearConsole():
    """Clears the terminal console based on the operating system."""
    os.system("cls" if os.name == "nt" else "clear")


def printError(message):
    """Prints an error message with prefix 'ERROR: ' in red text."""
    print(f"{RED}ERROR: {message}{RESET}")


def printWarning(message):
    """Prints a warning message with prefix 'ADVERTENCIA: ' in yellow text."""
    print(f"{YELLOW}ADVERTENCIA: {message}{RESET}")


def printSuccess(message):
    """Prints a success message with prefix 'EXITO: ' in green text."""
    print(f"{GREEN}EXITO: {message}{RESET}")


def printTitle(title):
    """Formats and prints a section or screen title."""
    print(f"\n{BOLD}{CYAN}==== {title.upper()} ===={RESET}\n")
