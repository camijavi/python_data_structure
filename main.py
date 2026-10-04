import sys
from pathlib import Path

# Configurar el path del proyecto
sys.path.append(str(Path(__file__).resolve().parent))

# Importar funciones de interfaz de usuario
from ui import displayBanner, displayMenu, getOption, promptPause
from components import clearConsole, printError, printSuccess

# Importar ejercicios de listas
from lists.deviceInventory import deviceInventory
from lists.latencyOrdering import latencyOrdering
from lists.offlineDevices import offlineDevices
from lists.temperaturesInManagua import temperaturesInManagua
from lists.weeklySales import weeklySales

# Importar ejercicios de tuplas
from tuples.coordinatesOfALocation import coordinatesOfALocation
from tuples.dimensionsOfABox import dimensionsOfABox
from tuples.multipleReturn import multipleReturn
from tuples.pointsOnARoute import pointsOnARoute
from tuples.studentRegistration import studentRegistration

# Importar ejercicios de diccionarios
from dicts.accessCount import accessCount
from dicts.deviceSheet import deviceSheet
from dicts.deviceUpdate import deviceUpdate
from dicts.technicianIncidents import technicianIncidents
from dicts.userDictionary import userDictionary

# Importar ejercicios combinados
from combined.dataConsumptionPerDay import dataConsumptionPerDay
from combined.gradesPerStudent import gradesPerStudent
from combined.listOfStructuredProducts import listOfStructuredProducts
from combined.supportRequestLog import supportRequestLog
from combined.uniqueOperatingSystems import uniqueOperatingSystems

# Importar ejercicios de zip
from zip.buildingUserRecords import buildingUserRecords
from zip.dataConsumptionComparison import dataConsumptionComparison
from zip.deviceIPStatus import deviceIPStatus
from zip.devicesIPAddresses import devicesIPAddresses
from zip.studentsGrades import studentsGrades

# Importar ejercicios de conjuntos (sets)
from sets.consolidatedTechCatalog import consolidatedTechCatalog
from sets.exclusiveApplications import exclusiveApplications
from sets.platformUsers import platformUsers
from sets.sharedApplications import sharedApplications
from sets.uniqueUsers import uniqueUsers


def executeSubMenu(categoryName, exercises):
    """
    Administra el bucle de un submenú para una categoría de ejercicios.
    :param categoryName: Nombre de la categoría a mostrar.
    :param exercises: Lista de tuplas (opcion, descripción, función).
    """
    while True:
        displayBanner()
        optionsDict = {key: desc for key, desc, _ in exercises}
        optionsDict["A"] = "Ejecutar todos los ejercicios de esta categoría"
        optionsDict["0"] = "Volver al Menú Principal"

        displayMenu(f"Categoría: {categoryName}", optionsDict)
        userChoice = getOption().upper()

        if userChoice == "0":
            break
        elif userChoice == "A":
            for _, desc, func in exercises:
                clearConsole()
                try:
                    func()
                except Exception as ex:
                    printError(f"Ocurrió un error al ejecutar {desc}: {ex}")
                promptPause()
        else:
            matchFunc = None
            matchDesc = None
            for key, desc, func in exercises:
                if key == userChoice:
                    matchFunc = func
                    matchDesc = desc
                    break

            if matchFunc:
                clearConsole()
                try:
                    matchFunc()
                except Exception as ex:
                    printError(f"Ocurrió un error al ejecutar {matchDesc}: {ex}")
                promptPause()
            else:
                printError("Opción no válida. Intente nuevamente.")
                promptPause()


def main():
    """Función principal que ejecuta el menú de navegación de estructuras de datos."""
    listsExercises = [
        ("1", "Inventario de Dispositivos", deviceInventory),
        ("2", "Ordenamiento de Latencias", latencyOrdering),
        ("3", "Dispositivos Offline y Stock 0", offlineDevices),
        ("4", "Temperaturas en Managua", temperaturesInManagua),
        ("5", "Ventas Semanales", weeklySales)
    ]

    tuplesExercises = [
        ("1", "Coordenadas de una Ubicación", coordinatesOfALocation),
        ("2", "Dimensiones de una Caja", dimensionsOfABox),
        ("3", "Retorno Múltiple de Ventas", multipleReturn),
        ("4", "Puntos en una Ruta", pointsOnARoute),
        ("5", "Registro de Estudiante", studentRegistration)
    ]

    dictsExercises = [
        ("1", "Conteo de Accesos por Dispositivo", accessCount),
        ("2", "Ficha Técnica de Dispositivo", deviceSheet),
        ("3", "Actualización de Stock de Dispositivos", deviceUpdate),
        ("4", "Incidencias y Ventas por Técnico", technicianIncidents),
        ("5", "Directorio de Contactos (Búsqueda)", userDictionary)
    ]

    combinedExercises = [
        ("1", "Ventas Totales por Día", dataConsumptionPerDay),
        ("2", "Promedio de Notas por Estudiante", gradesPerStudent),
        ("3", "Lista de Productos Estructurados", listOfStructuredProducts),
        ("4", "Registro de Solicitudes de Soporte", supportRequestLog),
        ("5", "Sistemas Operativos Únicos", uniqueOperatingSystems)
    ]

    zipExercises = [
        ("1", "Construcción de Registros de Usuario", buildingUserRecords),
        ("2", "Comparación de Consumo de Datos", dataConsumptionComparison),
        ("3", "Detalles de Dispositivos en Red", deviceIPStatus),
        ("4", "Diccionario Dispositivo-IP", devicesIPAddresses),
        ("5", "Listado de Estudiantes y Notas", studentsGrades)
    ]

    setsExercises = [
        ("1", "Consolidación de Catálogos de Tecnología", consolidatedTechCatalog),
        ("2", "Aplicaciones/Dispositivos Exclusivos", exclusiveApplications),
        ("3", "Asistencia de Usuarios a Eventos", platformUsers),
        ("4", "Aplicaciones/Dispositivos Compartidos", sharedApplications),
        ("5", "Conteo de Clientes Únicos", uniqueUsers)
    ]

    mainMenuOptions = {
        "1": "Listas (Lists)",
        "2": "Tuplas (Tuples)",
        "3": "Diccionarios (Dicts)",
        "4": "Estructuras Combinadas (Combined)",
        "5": "Uso de Zip (Zip)",
        "6": "Conjuntos (Sets)",
        "0": "Salir del Programa"
    }

    while True:
        displayBanner()
        displayMenu("Menú Principal - Seleccione una Categoría", mainMenuOptions)
        choice = getOption()

        if choice == "1":
            executeSubMenu("Listas", listsExercises)
        elif choice == "2":
            executeSubMenu("Tuplas", tuplesExercises)
        elif choice == "3":
            executeSubMenu("Diccionarios", dictsExercises)
        elif choice == "4":
            executeSubMenu("Estructuras Combinadas", combinedExercises)
        elif choice == "5":
            executeSubMenu("Zip", zipExercises)
        elif choice == "6":
            executeSubMenu("Conjuntos", setsExercises)
        elif choice == "0":
            clearConsole()
            printSuccess("¡Gracias por utilizar el sistema de Estructuras de Datos!")
            break
        else:
            printError("Opción no válida. Por favor, seleccione un número del menú.")
            promptPause()


if __name__ == "__main__":
    main()
