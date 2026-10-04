# Your mission: Given a list of registered
# login names, use a dictionary to
# count how many times each device appears.

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from components import printTitle


def accessCount():
    printTitle("Conteo de Accesos por Dispositivo")

    registeredLogins = [
        "Router-Core-01",
        "Switch-Acceso-02",
        "Servidor-BD-01",
        "Router-Core-01",
        "Laptop-Admin-05",
        "Servidor-BD-01",
        "Router-Core-01",
        "Switch-Acceso-02"
    ]

    deviceCounts = {}
    for deviceName in registeredLogins:
        deviceCounts[deviceName] = deviceCounts.get(deviceName, 0) + 1

    print("Lista de inicios de sesión registrados:")
    print(registeredLogins)

    print("\nFrecuencia de accesos por dispositivo:")
    for deviceName, count in deviceCounts.items():
        print(f"- {deviceName}: {count} acceso(s)")


if __name__ == "__main__":
    accessCount()