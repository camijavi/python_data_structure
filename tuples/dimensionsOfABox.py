# Your mission: Store width, height, and depth in a
#  tuple and calculate the volume without modifying the tuple.

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from components import printTitle


def dimensionsOfABox():
    printTitle("Volumen de una Caja")

    # Tupla con las dimensiones de la caja: (ancho, alto, profundidad)
    dimensions = (10.0, 5.0, 4.0)


    width, height, depth = dimensions


    volume = width * height * depth

    print(f"Dimensiones de la caja (ancho, alto, profundidad): {dimensions}")
    print(f"Volumen calculado: {volume:.2f}")


if __name__ == "__main__":
    dimensionsOfABox()
