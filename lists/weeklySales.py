# Your mission: Record seven days' sales in a list.
# Calculate the total, the average, and show the day 
# with the highest sales.

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from components import printTitle, printError


def weeklySales():

    printTitle("Registro de Ventas Semanales")
    sales = []

    for s in range(7):
        while True:
            try:
                rawInput = input(f"Día {s + 1}: ").strip()
                if not rawInput:
                    printError("El valor no puede estar vacío. Intente nuevamente.\n")
                    continue
                userInput = float(rawInput)
                if userInput < 0:
                    printError("Las ventas no pueden ser negativas. Intente nuevamente.\n")
                    continue
                break
            except ValueError:
                printError("Por favor, ingrese un número válido. Intente nuevamente.\n")

        sales.append(userInput)

    print(f"Total ventas: {sum(sales):.2f}")
    print(f"Promedio ventas: {sum(sales) / len(sales):.2f}")
    print(f"Día con mayores ventas: {sales.index(max(sales)) + 1}")


weeklySales()