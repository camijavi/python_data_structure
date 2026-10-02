# Your mission: Given a list of stock items, 
# identify the positions where the stock is 0 
# and show how many products are out of stock.

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from components import printTitle, printSuccess


def offlineDevices():
    printTitle("Control de Stock y Dispositivos Offline")

    stock = [15, 0, 8, 0, 22, 0, 5, 0]

    print(f"Lista de stock: {stock}\n")

    outOfStockIndexes = [index for index, quantity in enumerate(stock) if quantity == 0]

    print(f"Posiciones (índices) con stock 0: {outOfStockIndexes}")
    printSuccess(f"Total de productos fuera de stock: {len(outOfStockIndexes)}")


if __name__ == "__main__":
    offlineDevices()
