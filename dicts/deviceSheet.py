# Your mission: Create a dictionary to represent a
# product's model, IP address, status, and operating
# system. Query and modify its existence.

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from components import printTitle, printSuccess, printWarning


def deviceSheet():
    printTitle("Ficha Técnica del Dispositivo")

    deviceData = {
        "model": "Cisco Catalyst 9300",
        "ipAddress": "192.168.10.25",
        "status": "Activo",
        "operatingSystem": "Cisco IOS XE"
    }

    print("Datos iniciales del dispositivo:")
    for key, value in deviceData.items():
        print(f"- {key}: {value}")

    # Consultar existencia de atributos
    queryKeys = ["ipAddress", "location", "status"]
    print("\nConsulta de atributos:")
    for queryKey in queryKeys:
        if queryKey in deviceData:
            print(f"El atributo '{queryKey}' existe con valor: {deviceData[queryKey]}")
        else:
            printWarning(f"El atributo '{queryKey}' NO existe en la ficha técnica.")

    # Modificar datos existentes y agregar nuevos
    deviceData["status"] = "Mantenimiento"
    deviceData["location"] = "Data Center Principal"
    printSuccess("\nSe actualizó el estado a 'Mantenimiento' y se agregó la ubicación.")

    print("\nFicha técnica actualizada:")
    for key, value in deviceData.items():
        print(f"- {key}: {value}")


if __name__ == "__main__":
    deviceSheet()