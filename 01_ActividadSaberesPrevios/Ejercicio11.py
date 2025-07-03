# 11.	Un alumno desea saber cuál será su calificación final en la materia de Algoritmos.  Dicha calificación se compone de los siguientes porcentajes:
# 55% del promedio de sus tres calificaciones parciales.
# 30% de la calificación del examen final. 
# 15% de la calificación de un trabajo final

try:
    parcial1 = float(input("Ingrese la calificación del primer parcial: "))
    parcial2 = float(input("Ingrese la calificación del segundo parcial: "))
    parcial3 = float(input("Ingrese la calificación del tercer parcial: "))

    examen_final = float(input("Ingrese la calificación del examen final: "))
    trabajo_final = float(input("Ingrese la calificación del trabajo final: "))

    calificaciones = [parcial1, parcial2, parcial3, examen_final, trabajo_final]
    for nota in calificaciones:
        if nota < 0 or nota > 5:
            raise ValueError("Todas las calificaciones deben estar entre 0 y 5.")
        
    promedio_parciales = (parcial1 + parcial2 + parcial3) / 3
    calificacion_final = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)
    print(f"\nCalificación final en Algoritmos: {calificacion_final:.2f}")

except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("Ocurrió un error inesperado:", e)
