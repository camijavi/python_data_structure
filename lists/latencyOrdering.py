# Your mission: Request 10 response latencies, save them in a list,
#  and display the prices from lowest to highest and then from highest
# to lowest.

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from components import printTitle, printError


def latencyOrdering():
    printTitle("Ordenamiento de Latencias")

    latencies = []

    for i in range(10):
        while True:
            try:
                rawInput = input(f"Ingrese la latencia {i + 1} (ms): ").strip()
                if not rawInput:
                    printError("El valor no puede estar vacío. Intente nuevamente.\n")
                    continue
                userInput = float(rawInput)
                if userInput < 0:
                    printError("La latencia no puede ser negativa. Intente nuevamente.\n")
                    continue
                latencies.append(userInput)
                break
            except ValueError:
                printError("Por favor, ingrese un número válido. Intente nuevamente.\n")

    latencies.sort()
    print(f"\nLatencias de menor a mayor: {latencies}")

    latencies.sort(reverse=True)
    print(f"Latencias de mayor a menor: {latencies}")


if __name__ == "__main__":
    latencyOrdering()
