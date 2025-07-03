# 22)Se tienen tres baldes de agua, uno de cinco litros, otros de tres litros y otro de un litro; si el de un litro tarda una hora y media en llenarse, resuelva cuanto tiempo pueden tardar en llenarse los otros baldes. 
# Si tiene tres baldes, pero se desconoce su tamaño debe de resolver igualmente el ejercicio. 

try:
    vol1 = float(input("Volumen del balde 1 (en litros): "))
    vol2 = float(input("Volumen del balde 2 (en litros): "))
    vol3 = float(input("Volumen del balde 3 (en litros): "))

    if vol1 <= 0 or vol2 <= 0 or vol3 <= 0:
        print("Error: Los volúmenes deben ser mayores que cero.")
    else:
        tiempo_conocido = 1.5

        tiempo1 = vol1 * tiempo_conocido
        tiempo2 = vol2 * tiempo_conocido
        tiempo3 = vol3 * tiempo_conocido

        print("\n--- RESULTADOS ---")
        print("Tiempo de llenado del balde 1:", tiempo1, "horas")
        print("Tiempo de llenado del balde 2:", tiempo2, "horas")
        print("Tiempo de llenado del balde 3:", tiempo3, "horas")

except ValueError:
    print("Error: Ingrese solo números.")
except Exception as e:
    print("Ha ocurrido un error inesperado:", e)
