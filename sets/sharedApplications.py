# Your mission: Two suppliers offer
# different devices. Identify which ones appear
# in both catalogs.

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from components import printTitle, printSuccess, printWarning


def sharedApplications():
    printTitle("Dispositivos Compartidos entre Proveedores")

    supplierOneProducts = {"Router WiFi 6", "Switch Gigabit 24P", "Servidor NAS Synology", "Cable UTP Cat6", "UPS 1500VA"}
    supplierTwoProducts = {"Servidor NAS Synology", "Cámara IP HD", "Router WiFi 6", "UPS 1500VA", "Rack 19 Pulgadas"}

    print("Catálogo Proveedor 1:")
    print(supplierOneProducts)

    print("\nCatálogo Proveedor 2:")
    print(supplierTwoProducts)

    sharedProducts = supplierOneProducts.intersection(supplierTwoProducts)

    if sharedProducts:
        printSuccess("\nDispositivos presentes en AMBOS catálogos (Intersección):")
        for productName in sorted(sharedProducts):
            print(f"  * {productName}")
        print(f"\nTotal de coincidencias: {len(sharedProducts)}")
    else:
        printWarning("\nNo existen dispositivos compartidos entre ambos catálogos.")


if __name__ == "__main__":
    sharedApplications()