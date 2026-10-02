# Your mission: Merge devices from two
# providers without keeping duplicates and
# display the final catalog.

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from components import printTitle, printSuccess


def consolidatedTechCatalog():
    printTitle("Consolidación de Catálogos de Tecnología")

    providerACatalog = {"Laptop XPS 13", "Monitor Dell 27", "Teclado Mecánico RGB", "Mouse Inalámbrico"}
    providerBCatalog = {"Monitor Dell 27", "Webcam Logi HD", "Impresora HP Laser", "Teclado Mecánico RGB", "Docking Station"}

    print("Catálogo Proveedor A:")
    for deviceName in sorted(providerACatalog):
        print(f"  - {deviceName}")

    print("\nCatálogo Proveedor B:")
    for deviceName in sorted(providerBCatalog):
        print(f"  - {deviceName}")

    consolidatedCatalog = providerACatalog.union(providerBCatalog)

    printSuccess("\nCatálogo Consolidado (Unión sin duplicados):")
    for deviceName in sorted(consolidatedCatalog):
        print(f"  * {deviceName}")

    print(f"\nTotal de productos únicos disponibles: {len(consolidatedCatalog)}")


if __name__ == "__main__":
    consolidatedTechCatalog()
