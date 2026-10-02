import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from components import clearConsole, printError, printWarning, printSuccess, printTitle


def printInventoryTable(items):
    print(f"{'Id':<4} | {'productName':<20} | {'Id':<4} | {'productName':<20}")
    print("-" * 55)
    for i in range(0, len(items), 2):
        id1 = i + 1
        name1 = items[i]
        if i + 1 < len(items):
            id2 = i + 2
            name2 = items[i + 1]
            print(f"{id1:<4} | {name1:<20} | {id2:<4} | {name2:<20}")
        else:
            print(f"{id1:<4} | {name1:<20} | {'':<4} | {'':<20}")
    print()


def deviceInventory():
    clearConsole()
    printTitle("Inventario de Dispositivos")
    stock = ["iPhone 18 ProMax", "iPad Air", "Apple Watch", "Airpords", "MacBook Pro", "MacBook Neo", "Mac Mini", "AirPods Pro"]

    printInventoryTable(stock)

    while True:
        newProduct = input("> Ingrese un nuevo producto: ").strip()
        if newProduct:
            break
        printError("El nombre del producto no puede estar vacío. Intente nuevamente.\n")

    stock.append(newProduct)
    printSuccess(f"Producto '{newProduct}' agregado exitosamente.\n")

    printInventoryTable(stock)

    while True:
        try:
            editStock = int(input("> Ingrese el 'id' del producto que desea modificar: "))
            if 1 <= editStock <= len(stock):
                break
            printWarning(f"El 'id' debe estar entre 1 y {len(stock)}. Intente nuevamente.\n")
        except ValueError:
            printError("Ingrese un número válido. Intente nuevamente.\n")

    while True:
        newProductName = input(f"> Ingrese el nuevo nombre para '{stock[editStock - 1]}': ").strip()
        if newProductName:
            break
        printError("El nombre del producto no puede estar vacío. Intente nuevamente.\n")

    oldProduct = stock[editStock - 1]
    stock[editStock - 1] = newProductName
    printSuccess(f"Producto '{oldProduct}' actualizado a '{newProductName}' exitosamente.")

    printTitle("Inventario Actualizado")
    printInventoryTable(stock)


deviceInventory()