# Tu misión: Crea una lista con al menos 8 dispositivos. 
# Permite agregar un nuevo producto, modificar uno existente
# y mostrar la lista final.



def deviceInventory():
    print("==== INVENTARIO DE DISPOSITIVOS ===\n")
    stock = ["iPhone 18 ProMax", "iPad Air", "Apple Watch", "Airpords", "MacBook Pro", "MacBook Neo", "Mac Mini","AirPods Pro"]

    print(*stock, sep="\n")

    newProduct = input("Ingrese un nuevo producto: ")

    stock.append(newProduct)

    print(*stock, sep="\n")



deviceInventory()