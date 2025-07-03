# 6. Lea la cantidad de dinero correspondiente a una compra y calcule el valor del IVA (19%), y el valor total de la factura, si al valor de la compra se le autoriza un descuento del 10% (antes de aplicarle el IVA).

while True:
    try:
        compra = float(input('Ingresa el valor de la compra: '))
        if compra <= 0:
            raise Exception("Vuelve a Ingresar el Valor de la Compra...")
    except ValueError:
        print("Porfavor, Verifica haber ingresado el dato correctamente...")
    except Exception as a:
        print(a)
    else:
        iva = compra * 0.19
        break

descuento = str(input('aplica descuento s/n: ')).lower()
if descuento == 's':
    descuento = compra * 0.10
    print(f'''\t --------FACTURA--------
        Precio producto: {compra}
        Valor iva: {iva}
        --------------------------
        Valor total de compra: {compra - descuento}''')
elif descuento == 'n':
        print(f'''\t --------FACTURA--------
        Precio producto: {compra}
        Valor iva: {iva}
        --------------------------
        Valor total de compra: {compra + iva}''')
else:
    print('ERROR 404')