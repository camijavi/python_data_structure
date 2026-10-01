# Tu misión: Crea una lista con al menos 8 dispositivos. 
# Permite agregar un nuevo producto, modificar uno existente
# y mostrar la lista final.



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
    print("==== INVENTARIO DE DISPOSITIVOS ===\n")
    stock = ["iPhone 18 ProMax", "iPad Air", "Apple Watch", "Airpords", "MacBook Pro", "MacBook Neo", "Mac Mini","AirPods Pro"]

    printInventoryTable(stock)

    newProduct = input("Ingrese un nuevo producto: ")

    stock.append(newProduct)

    printInventoryTable(stock)

    editStock = int(input("Ingrese el 'id' del producto que desea modificar"))
    



deviceInventory()