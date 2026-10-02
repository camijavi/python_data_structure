# Your mission: Determine which devices
# provider A offers that provider B does not.

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from components import printTitle, printSuccess


def exclusiveApplications():
    printTitle("Dispositivos Exclusivos del Proveedor A")

    providerADevices = {"Servidor Blade R740", "Switch 48P Cisco", "Router Industrial", "Firewall Fortigate"}
    providerBDevices = {"Switch 48P Cisco", "Firewall Fortigate", "Punto de Acceso UniFi", "Servidor NAS Synology"}

    print("Catálogo Proveedor A:")
    print(providerADevices)

    print("\nCatálogo Proveedor B:")
    print(providerBDevices)

    exclusiveToA = providerADevices.difference(providerBDevices)

    printSuccess("\nDispositivos que ofrece el Proveedor A y que NO ofrece el Proveedor B:")
    for deviceName in sorted(exclusiveToA):
        print(f"  * {deviceName}")

    print(f"\nCantidad de dispositivos exclusivos: {len(exclusiveToA)}")


if __name__ == "__main__":
    exclusiveApplications()