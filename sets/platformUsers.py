# Your mission: Two lists represent people who 
# attended two events. Determine who attended 
# both and who attended only the first one.

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from components import printTitle, printSuccess


def platformUsers():
    printTitle("Análisis de Asistencia a Eventos de Plataforma")

    eventOneAttendees = ["Ana López", "Carlos Pérez", "Beatriz Solís", "David Ruiz", "Elena Torres"]
    eventTwoAttendees = ["Carlos Pérez", "Elena Torres", "Fernando Vega", "Gloria Morales", "Hugo Mendoza"]

    setOne = set(eventOneAttendees)
    setTwo = set(eventTwoAttendees)

    print(f"Asistentes Evento 1: {eventOneAttendees}")
    print(f"Asistentes Evento 2: {eventTwoAttendees}")

    bothEvents = setOne.intersection(setTwo)
    onlyFirstEvent = setOne.difference(setTwo)

    printSuccess("\nPersonas que asistieron a AMBOS eventos (Intersección):")
    for userName in sorted(bothEvents):
        print(f"  * {userName}")

    printSuccess("\nPersonas que asistieron ÚNICAMENTE al primer evento (Diferencia):")
    for userName in sorted(onlyFirstEvent):
        print(f"  * {userName}")


if __name__ == "__main__":
    platformUsers()