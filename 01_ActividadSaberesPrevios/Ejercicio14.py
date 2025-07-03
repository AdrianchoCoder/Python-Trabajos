# 14. Se trata de escribir el algoritmo que permita emitir la factura correspondiente a una compra de varios artículos (4) determinados, del que se adquieren una o varias unidades. El IVA es del 19%.

subtotal = 0
for i in range(1, 5):
    print(f"\nArtículo {i}")
    precio = float(input("Precio unitario: "))
    cantidad = int(input("Cantidad: "))
    subtotal += precio * cantidad

iva = subtotal * 0.19
total = subtotal + iva

print("\n----- FACTURA -----")
print(f"Subtotal: ${subtotal:.2f}")
print(f"IVA (19%): ${iva:.2f}")
print(f"Total a pagar: ${total:.2f}")
