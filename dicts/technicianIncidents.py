# Your mission: Store in a dictionary the total
#  sales for each technician and determine
#  who achieved the highest sales.

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from components import printTitle, printSuccess


def technicianIncidents():
    printTitle("Ventas Totales por Técnico")

    technicianSales = {
        "Carlos Pérez": 14500.50,
        "Ana Gómez": 22300.00,
        "Luis Martínez": 18900.75,
        "Sofia Rodríguez": 25100.20,
        "David López": 12800.40
    }

    print("Registro de ventas registradas por técnico:")
    for technicianName, salesAmount in technicianSales.items():
        print(f"- {technicianName}: ${salesAmount:,.2f}")

    bestTechnician = max(technicianSales, key=technicianSales.get)
    maxSales = technicianSales[bestTechnician]

    printSuccess(f"\nEl técnico con mayores ventas es '{bestTechnician}' con un total de ${maxSales:,.2f}")


if __name__ == "__main__":
    technicianIncidents()