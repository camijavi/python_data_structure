# Your mission: Compare the data consumption
# of two weeks and show the difference between
# them for each day.

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from components import printTitle, printSuccess


def dataConsumptionComparison():
    printTitle("Comparación de Consumo de Datos Semanal (zip)")

    daysOfWeek = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    weekOneConsumption = [10.5, 12.0, 8.5, 15.0, 14.2, 20.0, 18.5]
    weekTwoConsumption = [12.0, 11.5, 9.0, 18.2, 14.2, 22.5, 16.0]

    print(f"{'Día':<10} | {'Semana 1 (GB)':<13} | {'Semana 2 (GB)':<13} | {'Diferencia (GB)':<15}")
    print("-" * 58)

    for dayName, consWeekOne, consWeekTwo in zip(daysOfWeek, weekOneConsumption, weekTwoConsumption):
        consumptionDiff = consWeekTwo - consWeekOne
        diffSign = "+" if consumptionDiff > 0 else ""
        print(f"{dayName:<10} | {consWeekOne:<13.1f} | {consWeekTwo:<13.1f} | {diffSign}{consumptionDiff:<15.1f}")

    totalWeekOne = sum(weekOneConsumption)
    totalWeekTwo = sum(weekTwoConsumption)
    printSuccess(f"\nTotal Semana 1: {totalWeekOne:.1f} GB | Total Semana 2: {totalWeekTwo:.1f} GB | Diferencia Total: {totalWeekTwo - totalWeekOne:+.1f} GB")


if __name__ == "__main__":
    dataConsumptionComparison()