# Your mission: Use lists of names, ages,
# and cities to build a dictionary list
# using zip().

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from components import printTitle, printSuccess


def buildingUserRecords():
    printTitle("Construcción de Registros de Usuario con zip()")

    namesList = ["Carlos Mendoza", "Sofia Rodríguez", "Mateo Silva", "Lucía Morales"]
    agesList = [25, 30, 22, 28]
    citiesList = ["Managua", "León", "Granada", "Estelí"]

    print("Listas origen de datos:")
    print(f"- Nombres: {namesList}")
    print(f"- Edades: {agesList}")
    print(f"- Ciudades: {citiesList}")

    userRecords = []
    for userName, userAge, userCity in zip(namesList, agesList, citiesList):
        recordDict = {
            "name": userName,
            "age": userAge,
            "city": userCity
        }
        userRecords.append(recordDict)

    printSuccess("\nLista de diccionarios construida utilizando zip():")
    for index, userRecord in enumerate(userRecords, start=1):
        print(f"Registro #{index}: Nombre = {userRecord['name']}, Edad = {userRecord['age']}, Ciudad = {userRecord['city']}")


if __name__ == "__main__":
    buildingUserRecords()