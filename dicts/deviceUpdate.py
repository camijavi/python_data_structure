# Your mission: Represent the inventory as a product-stock dictionary.
# Process multiple entries and exits, updating the values accordingly.

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from components import printTitle, printSuccess, printWarning


def deviceUpdate():
    printTitle("Actualización de Stock de Dispositivos")

    productStock = {
        "Servidor Dell PowerEdge": 15,
        "Switch Cisco Catalyst": 8,
        "Router MikroTik CCR": 12,
        "Firewall Fortinet": 5
    }

    print("Inventario Inicial:")
    for productName, stockQuantity in productStock.items():
        print(f"- {productName}: {stockQuantity} unidades")

    # Movimientos de inventario (positivo = entrada, negativo = salida)
    stockMovements = [
        ("Servidor Dell PowerEdge", 5),
        ("Switch Cisco Catalyst", -3),
        ("Router MikroTik CCR", -10),
        ("Firewall Fortinet", 4),
        ("Monitor HP 24", 6)  # Producto nuevo
    ]

    print("\nProcesando movimientos de inventario:")
    for productName, quantityChange in stockMovements:
        currentStock = productStock.get(productName, 0)
        newStock = currentStock + quantityChange
        if newStock < 0:
            printWarning(f"No hay suficiente stock para '{productName}'. Stock actual: {currentStock}.")
        else:
            productStock[productName] = newStock
            actionType = "Entrada" if quantityChange > 0 else "Salida"
            print(f"- {actionType} de {abs(quantityChange)} unidad(es) para '{productName}'. Nuevo stock: {newStock}")

    printSuccess("\nInventario Final Actualizado:")
    for productName, stockQuantity in productStock.items():
        print(f"- {productName}: {stockQuantity} unidades")


if __name__ == "__main__":
    deviceUpdate()