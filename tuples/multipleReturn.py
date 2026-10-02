# Your mission: Create a function that receives
# a list of sales and returns a tuple with total, average,
# and maximum sale.

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from components import printTitle


def calculateSalesSummary(sales):
    if not sales:
        return 0.0, 0.0, 0.0
    total = sum(sales)
    average = total / len(sales)
    maxSale = max(sales)
    return total, average, maxSale


def multipleReturn():
    printTitle("Resumen de Ventas (Retorno Múltiple)")

    salesList = [150.0, 320.5, 89.0, 450.0, 210.25]

    total, average, maxSale = calculateSalesSummary(salesList)

    print(f"Ventas registradas: {salesList}\n")
    print(f"Total de ventas: ${total:.2f}")
    print(f"Promedio de ventas: ${average:.2f}")
    print(f"Venta máxima: ${maxSale:.2f}")


if __name__ == "__main__":
    multipleReturn()