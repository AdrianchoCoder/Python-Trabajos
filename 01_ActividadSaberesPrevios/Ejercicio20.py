try:
    precio_unitario = float(input("Ingrese el precio unitario del producto ($): "))
    cantidad = int(input("Ingrese la cantidad comprada: "))
    descuento = float(input("Ingrese el porcentaje de descuento (%): "))

    if precio_unitario < 0 or cantidad < 0 or descuento < 0:
        raise ValueError("Ningún valor puede ser negativo.")

    subtotal_bruto = precio_unitario * cantidad
    monto_descuento = subtotal_bruto * (descuento / 100)
    subtotal_con_descuento = subtotal_bruto - monto_descuento

    iva = subtotal_con_descuento * 0.19

    precio_neto = subtotal_con_descuento + iva

    print("\n---- DETALLE DE FACTURA ----")
    print(f"Subtotal sin descuento: ${subtotal_bruto:,.2f}")
    print(f"Descuento aplicado ({descuento}%) : -${monto_descuento:,.2f}")
    print(f"Subtotal con descuento: ${subtotal_con_descuento:,.2f}")
    print(f"IVA (19%): +${iva:,.2f}")
    print(f"PRECIO NETO A PAGAR: ${precio_neto:,.2f}")

except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("Ocurrió un error inesperado:", e)
