# 18. En una universidad los estudiantes pueden pagar el valor de su matrícula en cuatro cuotas de la siguiente forma 
# ●	Primera cuota: 40% 
# ●	Segunda cuota: 25%
# ●	 Tercera cuota: 20% 
# ●	Cuarta cuota: 15% 

# Diga cuanto es el valor que tiene que pagar por cuota un estudiante.
try:
    matricula = float(input("Ingresa el Pago de la Matricula: "))
    if matricula <= 0:
        raise Exception("Porfavor Verifica Haber Ingresado Correctamente el Dato...")
except ValueError:
    print("Porfavor, Verifica Haber llenado el Dato...")
except Exception as a:
    print(a)
else:
    cuota_uno = (matricula * 0.4)
    cuota_dos = (matricula * 0.25)
    cuota_tres = (matricula * 0.2)
    cuota_cuatro = (matricula * 0.15)
    print(f"Las Coutas Mensuales son: \nCuota Uno: {cuota_uno}")
    print(f"Las Coutas Mensuales son: \nCuota Dos: {cuota_dos}")
    print(f"Las Coutas Mensuales son: \nCuota Tres: {cuota_tres}")
    print(f"Las Coutas Mensuales son: \nCuota Cuatro: {cuota_cuatro}")

    Total_a_pagar = cuota_uno + cuota_dos + cuota_tres + cuota_cuatro
    print('TOTAL DE LA MATRICULA: ', Total_a_pagar)