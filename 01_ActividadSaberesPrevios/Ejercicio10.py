# 10. Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente por su compra.
while True:
    try:
        precio = float(input('Ingrese el valor total de la compra: '))
        if precio <= 0:
            raise Exception("El dato debe ser mayor a 0...")
    except ValueError:
        print("Porfavor, Verifica haber Ingresado el Dato...")
    except Exception as a:
        print(a)
    else:
        precio_final = precio - (precio * 0.15)
        print(f'El total a pagar es: {precio_final}')
        break
