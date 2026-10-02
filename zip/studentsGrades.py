# Your mission: Link two lists, one of students
# and one of grades, using zip(). Display each
# student along with their grade.

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from components import printTitle, printSuccess


def studentsGrades():
    printTitle("Listado de Estudiantes y Notas con zip()")

    studentsList = ["Andrea Mendoza", "Gabriel Ruiz", "Valeria Gómez", "Fernando Silva", "Natalia Reyes"]
    gradesList = [88.5, 95.0, 78.2, 91.0, 84.0]

    print("Emparejamiento de listas con zip():")
    for studentName, studentGrade in zip(studentsList, gradesList):
        statusStr = "Aprobado" if studentGrade >= 70.0 else "Reprobado"
        print(f"- Estudiante: {studentName:<16} | Nota: {studentGrade:>5.1f} | Estado: {statusStr}")

    averageGrade = sum(gradesList) / len(gradesList)
    printSuccess(f"\nPromedio general del grupo: {averageGrade:.2f}")


if __name__ == "__main__":
    studentsGrades()