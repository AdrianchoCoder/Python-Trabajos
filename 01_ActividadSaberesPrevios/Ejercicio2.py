# 2. Lea dos números y calcule el resultado de su suma, resta, multiplicación y división.
while True:
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        if num1 <= 0 or num2 <= 0:
            raise Exception("Porfavor, Verifica que el dato sea mayor a 0...")
    except ValueError:
        print("Error, Verifica haber llenado correctamente el dato...")
    except Exception as a:
        print(a)
    else:
        print("Suma:", num1 + num2)
        print("Resta:", num1 - num2)
        print("Multiplicación:", num1 * num2)
        print("División:", num1 / num2)
        break
