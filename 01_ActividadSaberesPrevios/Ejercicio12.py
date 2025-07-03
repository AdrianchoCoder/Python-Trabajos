# 12. Un maestro desea saber qué porcentaje de hombres y qué porcentaje de mujeres hay en un grupo de alumnos.

hombres = int(input("Ingrese la cantidad de hombres: "))
mujeres = int(input("Ingrese la cantidad de mujeres: "))

total_estudiantes = hombres + mujeres

porcentaje_hombres = (hombres / total_estudiantes) * 100
porcentaje_mujeres = (mujeres / total_estudiantes) * 100

print(f"Porcentaje de hombres: {porcentaje_hombres:.2f}%")
print(f"Porcentaje de mujeres: {porcentaje_mujeres:.2f}%")