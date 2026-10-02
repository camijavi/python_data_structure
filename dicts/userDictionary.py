# Your mission: Build a dictionary where
# the key is the name and the value is the
# phone number. Allow users to look up a contact.

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from components import printTitle, printSuccess, printWarning, printError


def userDictionary():
    printTitle("Directorio de Contactos")

    phoneBook = {
        "María López": "+505 8888-1111",
        "Juan Pérez": "+505 8765-4321",
        "Elena Torres": "+505 8123-9999",
        "Carlos Mendoza": "+505 8444-5555"
    }

    print("Lista de contactos registrados:")
    for contactName in phoneBook:
        print(f"- {contactName}")

    print()
    searchName = input("> Ingrese el nombre del contacto a buscar: ").strip()

    if not searchName:
        printError("El nombre no puede estar vacío.")
        return

    foundContact = False
    for contactName, phoneNumber in phoneBook.items():
        if contactName.lower() == searchName.lower():
            printSuccess(f"Contacto encontrado: {contactName} -> Teléfono: {phoneNumber}")
            foundContact = True
            break

    if not foundContact:
        printWarning(f"No se encontró ningún contacto registrado con el nombre '{searchName}'.")


if __name__ == "__main__":
    userDictionary()