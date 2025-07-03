# 24) Un estudiante realiza un préstamo a un plazo de 5 años, donde la tasa fija de interés es del 5% anual, se debe solicitar el monto del préstamo y se desea calcular la siguiente información. 
# • Cuanto dinero se ha pagado de intereses en un año. 
# • Cuanto dinero se ha pagado de intereses en el tercer trimestre del año. 
# • Cuanto dinero se ha pagado de intereses en el primer mes. 
# • Cuanto dinero se paga en total del préstamo solicitado incluyendo intereses. 

print("=== CÁLCULO DE INTERESES DE UN PRÉSTAMO ===")

try:
    monto = float(input("Ingrese el monto del préstamo: "))

    if monto <= 0:
        print("Error: El monto del préstamo debe ser mayor que cero.")
    else:
        tasa_anual = 0.05
        plazo_años = 5

        interes_anual = monto * tasa_anual
        interes_trimestre_3 = interes_anual / 4
        interes_mes_1 = interes_anual / 12
        total_a_pagar = monto + (interes_anual * plazo_años)

        print("\n--- RESULTADOS ---")
        print("Intereses pagados en 1 año: $", interes_anual)
        print("Intereses pagados en el 3er trimestre: $", interes_trimestre_3)
        print("Intereses pagados en el 1er mes: $", interes_mes_1)
        print("Total a pagar al finalizar los 5 años: $", total_a_pagar)

except ValueError:
    print("Error: Ingrese un número válido para el monto del préstamo.")
except Exception as e:
    print("Ha ocurrido un error inesperado:", e)
