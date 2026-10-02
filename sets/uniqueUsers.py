# Your mission: Given a list with repeated
# customer names, create a set and show how
# many different customers there are.

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from components import printTitle, printSuccess


def uniqueUsers():
    printTitle("Conteo de Clientes Únicos")

    customerList = [
        "Juan Pérez", "María López", "Juan Pérez", "Pedro Gómez",
        "María López", "Sofia Ruiz", "Juan Pérez", "Pedro Gómez",
        "Lucas Torrez", "Ana Sofía", "Sofia Ruiz"
    ]

    print(f"Lista original con registros duplicados ({len(customerList)} registros):")
    print(customerList)

    uniqueCustomersSet = set(customerList)

    print("\nConjunto de clientes únicos obtenido:")
    for customerName in sorted(uniqueCustomersSet):
        print(f"  - {customerName}")

    printSuccess(f"\nSe encontraron {len(uniqueCustomersSet)} clientes únicos de un total de {len(customerList)} registros.")


if __name__ == "__main__":
    uniqueUsers()