import sys
from pathlib import Path

from components import BOLD, CYAN, GREEN, RED, RESET, YELLOW, clearConsole, printError, printTitle

def displayBanner():
    """Muestra un banner estético para la aplicación."""
    clearConsole()
    banner = f"""
{BOLD}{CYAN}====================================================
       ESTRUCTURAS DE DATOS EN PYTHON - MENÚ
===================================================={RESET}
"""
    print(banner)


def displayMenu(title, options):
    """
    Muestra un menú formateado con opciones.
    :param title: Título del menú.
    :param options: Diccionario u orden de opciones {opcion: descripción}.
    """
    print(f"\n{BOLD}{GREEN}=== {title} ==={RESET}\n")
    for key, description in options.items():
        print(f"  {BOLD}{CYAN}[{key}]{RESET} {description}")
    print()


def getOption(promptText="> Seleccione una opción: "):
    """Solicita la entrada del usuario de forma limpia."""
    return input(f"{BOLD}{YELLOW}{promptText}{RESET}").strip()


def promptPause():
    """Pausa la ejecución para que el usuario pueda leer los resultados."""
    input(f"\n{BOLD}{YELLOW}[Presione ENTER para continuar...]{RESET}")
