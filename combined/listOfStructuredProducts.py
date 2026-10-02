# Your mission: Create a list of dictionaries
# where each dictionary represents a product.
# Show only the devices whose price is
# greater than a given value.

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from components import printTitle, printSuccess, printWarning, printError


def listOfStructuredProducts():
    printTitle("Filtrado de Productos por Precio")

    productList = [
        {"name": "Laptop Dell XPS", "category": "Computación", "price": 1250.00},
        {"name": "Mouse Inalámbrico", "category": "Accesorios", "price": 25.50},
        {"name": "Teclado Mecánico RGB", "category": "Accesorios", "price": 85.00},
        {"name": "Monitor LG 27'' 4K", "category": "Pantallas", "price": 450.00},
        {"name": "Cable HDMI 2.1", "category": "Cables", "price": 15.00},
        {"name": "Servidor HP ProLiant", "category": "Servidores", "price": 2800.00}
    ]

    print("Lista completa de productos en catálogo:")
    for productItem in productList:
        print(f"- {productItem['name']} ({productItem['category']}): ${productItem['price']:,.2f}")

    print()
    try:
        rawPrice = input("> Ingrese el precio mínimo para filtrar (ej. 100): ").strip()
        if not rawPrice:
            minPrice = 100.0
            print("Utilizando precio mínimo predeterminado: $100.00")
        else:
            minPrice = float(rawPrice)
    except ValueError:
        printError("Entrada no válida. Utilizando precio mínimo de $100.00")
        minPrice = 100.0

    filteredProducts = [productItem for productItem in productList if productItem["price"] > minPrice]

    print(f"\nDispositivos cuyo precio es mayor a ${minPrice:,.2f}:")
    if filteredProducts:
        for productItem in filteredProducts:
            print(f"- {productItem['name']} | Categoría: {productItem['category']} | Precio: ${productItem['price']:,.2f}")
        printSuccess(f"Se encontraron {len(filteredProducts)} producto(s).")
    else:
        printWarning("No se encontraron dispositivos que superen el precio ingresado.")


if __name__ == "__main__":
    listOfStructuredProducts()