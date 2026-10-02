import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from components import printTitle, printError, printSuccess


def temperaturesInManagua():
    printTitle("Temperaturas en Managua")

    while True:
        try:
            rawDays = input("¿Cuántos días de temperaturas va a ingresar?: ").strip()
            if not rawDays:
                printError("El número de días no puede estar vacío. Intente nuevamente.\n")
                continue
            daysNum = int(rawDays)
            if daysNum <= 0:
                printError("El número de días debe ser mayor a 0. Intente nuevamente.\n")
                continue
            break
        except ValueError:
            printError("Por favor, ingrese un número entero válido. Intente nuevamente.\n")

    temperatures = []

    for d in range(daysNum):
        while True:
            try:
                rawInput = input(f"Temperatura de día ({d + 1}): ").strip()
                if not rawInput:
                    printError("El valor no puede estar vacío. Intente nuevamente.\n")
                    continue
                userInput = float(rawInput)
                if userInput < 0:
                    printError("Las temperaturas no pueden ser negativas. Intente nuevamente.\n")
                    continue
                temperatures.append(userInput)
                break
            except ValueError:
                printError("Por favor, ingrese un número válido. Intente nuevamente.\n")

    hotTemperatures = [t for t in temperatures if t > 30]

    print("\n--- Resultados ---")
    print(f"Lista de todas las temperaturas: {temperatures}")
    print(f"Lista de temperaturas mayores a 30°C: {hotTemperatures}")

    if hotTemperatures:
        printSuccess(f"Se registraron {len(hotTemperatures)} día(s) con temperatura superior a 30°C.")
    else:
        print("No se registraron temperaturas superiores a 30°C.")


if __name__ == "__main__":
    temperaturesInManagua()