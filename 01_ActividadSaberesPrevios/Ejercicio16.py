# 16.	Suponga que un conductor le pide a usted que le haga un algoritmo para calcular cuánto le corresponde en un día trabajado, teniendo en cuenta que tiene derecho a el 19% del total recaudado.
try:
    total_recaudado = float(input("Ingrese el total recaudado en el día ($): "))

    if total_recaudado < 0:
        raise ValueError("El total recaudado no puede ser negativo.")

    porcentaje_conductor = 0.19
    pago_conductor = total_recaudado * porcentaje_conductor

    print(f"\nAl conductor le corresponde el 19% del total.")
    print(f"Total recaudado: ${total_recaudado:,.2f}")
    print(f"Pago al conductor: ${pago_conductor:,.2f}")

except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("Ocurrió un error inesperado:", e)
