# 9. Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

try:
    sueldo_base = float(input("Ingrese el sueldo base del vendedor: "))
    if sueldo_base < 0:
        raise ValueError("El sueldo base no puede ser negativo.")

    venta1 = float(input("Ingrese el valor de la primera venta: "))
    venta2 = float(input("Ingrese el valor de la segunda venta: "))
    venta3 = float(input("Ingrese el valor de la tercera venta: "))

    if venta1 < 0 or venta2 < 0 or venta3 < 0:
        raise ValueError("Las ventas no pueden ser negativas.")

    total_ventas = venta1 + venta2 + venta3
    comision = total_ventas * 0.10
    total_mes = sueldo_base + comision

    print("\n--- RESULTADOS ---")
    print(f"Comisión total: ${comision:.2f}")
    print(f"Total a recibir en el mes: ${total_mes:.2f}")

except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("Ocurrió un error inesperado:", e)
