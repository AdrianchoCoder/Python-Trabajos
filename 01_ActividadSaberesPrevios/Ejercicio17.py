# # 17.	Desarrollar un algoritmo que permita generar la colilla de pago de los empleados de una empresa. La colilla debe mostrar:
#El Salario del Empleado 
#El Valor de Ahorro mensual programado.
#La suma a deducir por aporte a la Salud (EPS) 12,5 %
#La suma a deducir por aporte al Fondo de Pensiones  16%
#Total a Recibir 
#Toda la información que debe proveer el usuario del programa es el  Salario del Empleado y el Valor de Ahorro mensual programado. El programa debe calcular y devolver el resto de los datos.

try:
    salario = float(input("Ingrese el salario del empleado ($): "))
    ahorro = float(input("Ingrese el valor de ahorro mensual programado ($): "))

    if salario < 0 or ahorro < 0:
        raise ValueError("Los valores no pueden ser negativos.")

    deduccion_eps = salario * 0.125
    deduccion_pension = salario * 0.16
    total_deducciones = deduccion_eps + deduccion_pension + ahorro

    total_recibir = salario - total_deducciones

    print("\n----- COLILLA DE PAGO -----")
    print(f"Salario del empleado: ${salario:,.2f}")
    print(f"Ahorro mensual programado: ${ahorro:,.2f}")
    print(f"Deducción por EPS (12.5%): ${deduccion_eps:,.2f}")
    print(f"Deducción por pensión (16%): ${deduccion_pension:,.2f}")
    print(f"Total deducciones: ${total_deducciones:,.2f}")
    print(f"Total a recibir: ${total_recibir:,.2f}")

except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("Ocurrió un error inesperado:", e)