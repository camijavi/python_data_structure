# Your mission: Build a device-IP dictionary
# from two related lists using zip().

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from components import printTitle, printSuccess


def devicesIPAddresses():
    printTitle("Diccionario Dispositivo-IP mediante zip()")

    deviceList = ["Servidor Web", "Servidor Base de Datos", "Router Principal", "Switch de Acceso", "Firewall"]
    ipList = ["10.0.0.1", "10.0.0.2", "10.0.0.254", "10.0.0.10", "10.0.0.253"]

    print(f"Lista de Dispositivos: {deviceList}")
    print(f"Lista de Direcciones IP: {ipList}")

    deviceIpDict = dict(zip(deviceList, ipList))

    printSuccess("\nDiccionario generado exitosamente:")
    for deviceName, ipAddress in deviceIpDict.items():
        print(f"- {deviceName} -> IP: {ipAddress}")


if __name__ == "__main__":
    devicesIPAddresses()