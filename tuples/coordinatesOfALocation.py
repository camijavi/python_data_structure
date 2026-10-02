# Your mission: Represent the latitude and 
# longitude of a business using a tuple. 
# Unpack the values ​​and display them with labels.

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from components import printTitle


def coordinatesOfALocation():
    printTitle("Coordenadas de una Ubicación")


    coordinate = (12.136389, -86.251389)


    latitude, longitude = coordinate

    print(f"Coordenadas de la tupla: {coordinate}")
    print(f"Latitud: {latitude}")
    print(f"Longitud: {longitude}")


if __name__ == "__main__":
    coordinatesOfALocation()
