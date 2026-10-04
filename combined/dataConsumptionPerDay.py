# Your mission: Use a dictionary whose values 
# are sales lists. Calculate the total sold 
# for each day.

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from components import printTitle, printSuccess


def dataConsumptionPerDay():
    printTitle("Ventas Totales por Día")

    dailySales = {
        "Lunes": [120.50, 80.25, 45.00],
        "Martes": [200.00, 150.30, 95.00],
        "Miércoles": [90.00, 110.50, 130.20],
        "Jueves": [300.25, 175.80],
        "Viernes": [180.00, 210.00, 95.50, 140.00]
    }

    print("Ventas registradas por día:")
    for dayName, salesList in dailySales.items():
        totalSold = sum(salesList)
        print(f"- {dayName}: Lista de ventas = {salesList} | Total del día = ${totalSold:,.2f}")

    grandTotal = sum(sum(salesList) for salesList in dailySales.values())
    printSuccess(f"\nTotal general vendido en la semana: ${grandTotal:,.2f}")


if __name__ == "__main__":
    dataConsumptionPerDay()