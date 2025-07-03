# 15.	Suponga que tiene Ud. una tienda y desea registrar las ventas en una computadora. Diseñe un algoritmo en pseudocódigo que lea por cada cliente: 
#El monto de la venta, calcule e imprima el IVA.
#calcule e imprima el total a pagar 
#lea la cantidad con la que paga el cliente (solo efectivo), calcule e imprima el cambio. 2

IVA = 0.19

seguir = "s"

while seguir.lower() == "s":
    try:
        venta = float(input("\nMonto de la venta ($): "))
        if venta < 0:
            raise ValueError("El monto de la venta no puede ser negativo.")

        iva = venta * IVA
        total = venta + iva

        print(f"IVA (19%): ${iva:,.2f}")
        print(f"TOTAL A PAGAR: ${total:,.2f}")

        while True:
            efectivo = float(input("Efectivo recibido ($): "))
            if efectivo < total:
                print("Efectivo insuficiente. Ingrese un valor mayor o igual al total.")
            else:
                break

        cambio = efectivo - total
        print(f"Cambio: ${cambio:,.2f}")

    except ValueError as e:
        print("Error:", e)
        continue
    except Exception as e:
        print("Ocurrió un error inesperado:", e)
        continue

    seguir = input("\n¿Registrar otra venta? (s/n): ")

print("\nFin del programa. ¡Gracias por usar el sistema!")
