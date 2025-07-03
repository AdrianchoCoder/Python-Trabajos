# 1. Lea tres números y calcule el resultado de su suma.

while True:
    try:
        numUno = int(input("Ingresa el Primer Numero: "))
        numDos = int(input("Ingresa el Segundo Numero: "))
        numTres = int(input("Ingresa el Tercer Numero: "))
        if numUno <= 0 or numDos <= 0 or numTres <= 0:
            raise Exception("--- El Numero debe ser mayor a 0 ---")
    except ValueError:
        print("Error, Vuelve a Ingresar los Datos...")
    except Exception as a:
        print(a)
    else:
        resultado = numUno + numDos + numTres
        print("El resultado es: ", resultado)
        break