# Your mission: Create a list of tuples to
#  represent various points on a route.
#  Iterate through the list showing latitude and longitude.

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from components import printTitle


def pointsOnARoute():
    printTitle("Puntos en una Ruta")

    routePoints = [
        (12.136389, -86.251389),
        (12.145000, -86.240000),
        (12.152000, -86.231000),
        (12.160000, -86.220000)
    ]

    print("Coordenadas de la ruta:")
    for i, (latitude, longitude) in enumerate(routePoints, start=1):
        print(f"Punto {i}: Latitud = {latitude}, Longitud = {longitude}")


if __name__ == "__main__":
    pointsOnARoute()