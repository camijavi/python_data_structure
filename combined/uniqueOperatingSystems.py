# Your mission: Starting with a list of device
# dictionaries, build a set with the different
# categories.

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from components import printTitle, printSuccess


def uniqueOperatingSystems():
    printTitle("Sistemas Operativos Únicos por Dispositivo")

    deviceList = [
        {"deviceName": "Servidor BD 01", "operatingSystem": "Linux Ubuntu Server"},
        {"deviceName": "Estación de Trabajo A", "operatingSystem": "Windows 11 Pro"},
        {"deviceName": "Servidor Web 01", "operatingSystem": "Linux Ubuntu Server"},
        {"deviceName": "Laptop Diseño", "operatingSystem": "macOS Sequoia"},
        {"deviceName": "Router Core", "operatingSystem": "Cisco IOS XE"},
        {"deviceName": "Estación de Trabajo B", "operatingSystem": "Windows 11 Pro"},
        {"deviceName": "Servidor Backup", "operatingSystem": "Linux RedHat"}
    ]

    print("Lista de dispositivos registrados:")
    for deviceItem in deviceList:
        print(f"- {deviceItem['deviceName']} -> S.O.: {deviceItem['operatingSystem']}")

    uniqueSystems = {deviceItem["operatingSystem"] for deviceItem in deviceList}

    print("\nConjunto de sistemas operativos únicos identificados:")
    for systemName in sorted(uniqueSystems):
        print(f"  * {systemName}")

    printSuccess(f"\nTotal de sistemas operativos distintos: {len(uniqueSystems)}")


if __name__ == "__main__":
    uniqueOperatingSystems()