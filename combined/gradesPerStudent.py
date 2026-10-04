# Your mission: Create a dictionary where 
# each student's value is a list of grades.
# Calculate the average for each student.

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from components import printTitle, printSuccess


def gradesPerStudent():
    printTitle("Promedio de Calificaciones por Estudiante")

    studentGrades = {
        "Ana Sofía": [85.0, 90.5, 92.0],
        "Luis Fernando": [70.0, 65.5, 80.0],
        "Carmen Lucía": [95.0, 98.0, 100.0],
        "Diego Mateo": [60.0, 75.0, 72.5]
    }

    print("Calificaciones y promedios:")
    for studentName, gradeList in studentGrades.items():
        averageGrade = sum(gradeList) / len(gradeList) if gradeList else 0.0
        print(f"- {studentName}: Notas = {gradeList} -> Promedio: {averageGrade:.2f}")

    bestStudent = max(studentGrades, key=lambda s: sum(studentGrades[s]) / len(studentGrades[s]))
    bestAverage = sum(studentGrades[bestStudent]) / len(studentGrades[bestStudent])

    printSuccess(f"\nEstudiante con mayor promedio: '{bestStudent}' con {bestAverage:.2f}")


if __name__ == "__main__":
    gradesPerStudent()