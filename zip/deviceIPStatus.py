# Your mission: Link three lists using zip() to 
# display the name, model, IP address, and status
#  of a device in each iteration.

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from components import printTitle, printSuccess


def deviceIPStatus():
    printTitle("Detalles de Dispositivos en Red con zip()")

    deviceNames = ["Servidor Principal", "Switch Core", "Firewall Perimetral", "Punto de Acceso"]
    deviceModels = ["Dell PowerEdge R740", "Cisco Catalyst 9300", "FortiGate 60F", "Ubiquiti UniFi AP"]
    ipAddresses = ["192.168.1.10", "192.168.1.2", "192.168.1.1", "192.168.1.50"]
    deviceStatuses = ["Activo", "Activo", "En Mantenimiento", "Activo"]

    print("Iteración sobre los datos enlazados con zip():\n")

    for deviceName, deviceModel, ipAddress, deviceStatus in zip(deviceNames, deviceModels, ipAddresses, deviceStatuses):
        print(f"Dispositivo: {deviceName}")
        print(f"  - Modelo: {deviceModel}")
        print(f"  - Dirección IP: {ipAddress}")
        print(f"  - Estado: {deviceStatus}\n")

    printSuccess(f"Se enlazaron exitosamente {len(deviceNames)} registros de dispositivos.")


if __name__ == "__main__":
    deviceIPStatus()