# Your mission: Represent a student's name,
# age, and average grade using a tuple.
# Iterate through its elements and display the information.

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from components import printTitle


def studentRegistration():
    printTitle("Registro de Estudiante")

    studentInfo = ("Carlos Mendoza", 21, 92.5)

    print("Información del estudiante:")
    for item in studentInfo:
        print(f"- {item}")


if __name__ == "__main__":
    studentRegistration()