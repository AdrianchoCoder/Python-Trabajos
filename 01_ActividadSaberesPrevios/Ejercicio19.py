# 19) Ingresar, para un estudiante, sus 5 notas de un curso, nombre, programa, ficha.  Hacer un algoritmo que:
# Muestre el nombre
# Muestre el programa de formación
# Se debe calcular y mostrar su promedio final.

try:
    nombre = input("Ingrese el nombre del estudiante: ")
    programa = input("Ingrese el programa de formación: ")
    ficha = input("Ingrese el número de ficha: ")

    notas = []
    for i in range(1, 6):
        nota = float(input(f"Ingrese la nota {i}: "))
        if nota < 0 or nota > 5:
            raise ValueError("Las notas deben estar entre 0 y 5.")
        notas.append(nota)

    promedio = sum(notas) / len(notas)

    print("\n---- INFORME DEL ESTUDIANTE ----")
    print(f"Nombre del estudiante: {nombre}")
    print(f"Programa de formación: {programa}")
    print(f"Promedio final: {promedio:.2f}")

except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("Ocurrió un error inesperado:", e)
